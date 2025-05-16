from typing import Dict, List
from planner import GoalPlanner
from tools.search import LeadSearcher
from tools.write_email import EmailWriter
from tools.send_email import EmailSender
from memory.storage import MemoryStorage
import time

class AgentSender:
    def __init__(self, tone: str = "professional"):
        self.planner = GoalPlanner()
        self.searcher = LeadSearcher()
        self.writer = EmailWriter()
        self.sender = EmailSender()
        self.memory = MemoryStorage()
        self.current_goal = None
        self.current_steps = []
        self.leads = []
        self.emails = []
        self.tone = tone
    
    def set_goal(self, goal: str, tone: str = None):
        """Set a new goal and break it down into steps."""
        self.current_goal = goal
        if tone:
            self.tone = tone
        self.current_steps = self.planner.break_down_goal(goal)
        
        # Log the initial goal and steps
        self.memory.save_step({
            "type": "goal_set",
            "goal": goal,
            "steps": self.current_steps
        })
    
    def execute_step(self, step: Dict) -> Dict:
        """Execute a single step and return the result."""
        step["status"] = "in_progress"
        self.memory.save_step(step)
        
        try:
            if step["tool"] == "search":
                self.leads = self.searcher.search_leads(step["description"])
                self.memory.save_leads(self.leads)
                result = self.leads
            elif step["tool"] == "write_email":
                if not self.leads:
                    self.leads = self.memory.get_all_leads()
                self.emails = self.writer.write_emails(self.leads, tone=self.tone)
                for email in self.emails:
                    self.memory.save_email(email)
                result = self.emails
            elif step["tool"] == "send_email":
                if not self.emails:
                    self.emails = self.memory.get_all_emails()
                send_results = self.sender.send_emails(self.emails)
                for res in send_results:
                    self.memory.save_step({"type": "email_send_result", **res})
                result = send_results
            else:
                result = {"error": f"Tool {step['tool']} not implemented yet"}
            
            step["status"] = "completed"
            step["result"] = result
            
        except Exception as e:
            step["status"] = "failed"
            step["error"] = str(e)
            result = {"error": str(e)}
        
        self.memory.save_step(step)
        return result
    
    def run(self) -> List[Dict]:
        """Run the agent loop until all steps are completed."""
        if not self.current_goal:
            raise ValueError("No goal set. Call set_goal() first.")
        
        results = []
        while self.current_steps:
            # Get the next pending step
            next_step = next(
                (step for step in self.current_steps if step["status"] == "pending"),
                None
            )
            
            if not next_step:
                break
            
            # Execute the step
            result = self.execute_step(next_step)
            results.append(result)
            
            # Add a small delay between steps
            time.sleep(1)
        
        return results
    
    def get_progress(self) -> Dict:
        """Get the current progress of the agent."""
        if not self.current_steps:
            return {"status": "no_goal"}
        
        total_steps = len(self.current_steps)
        completed_steps = sum(1 for step in self.current_steps if step["status"] == "completed")
        failed_steps = sum(1 for step in self.current_steps if step["status"] == "failed")
        
        return {
            "goal": self.current_goal,
            "total_steps": total_steps,
            "completed_steps": completed_steps,
            "failed_steps": failed_steps,
            "pending_steps": total_steps - completed_steps - failed_steps,
            "progress_percentage": (completed_steps / total_steps) * 100 if total_steps > 0 else 0
        } 