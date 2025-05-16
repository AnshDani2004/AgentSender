from typing import List, Dict
from datetime import datetime

class GoalPlanner:
    def __init__(self):
        # Define common patterns for goal breakdown
        self.patterns = {
            "find": ["search", "write_email", "send_email"],
            "research": ["search", "summarize", "write_email"],
            "outreach": ["search", "write_email", "send_email"],
            "contact": ["search", "write_email", "send_email"],
            "connect": ["search", "write_email", "send_email"]
        }
    
    def break_down_goal(self, goal: str) -> List[Dict]:
        """
        Break down a high-level goal into specific, actionable steps using pattern matching.
        
        Args:
            goal (str): The high-level goal provided by the user
            
        Returns:
            List[Dict]: A list of steps, each containing:
                - step_id: Unique identifier
                - description: What needs to be done
                - tool: Which tool to use
                - status: Current status (pending, in_progress, completed)
        """
        # Convert goal to lowercase for pattern matching
        goal_lower = goal.lower()
        
        # Determine the type of goal based on keywords
        goal_type = None
        for keyword in self.patterns:
            if keyword in goal_lower:
                goal_type = keyword
                break
        
        # If no pattern matches, use default steps
        if goal_type is None:
            return self._fallback_breakdown(goal)
        
        # Create steps based on the pattern
        steps = []
        for i, tool in enumerate(self.patterns[goal_type], 1):
            step = {
                "step_id": i,
                "description": self._get_step_description(tool, goal),
                "tool": tool,
                "status": "pending",
                "created_at": datetime.now().isoformat()
            }
            steps.append(step)
        
        return steps
    
    def _get_step_description(self, tool: str, goal: str) -> str:
        """Generate a description for a step based on the tool and goal."""
        descriptions = {
            "search": f"Research and find relevant leads for: {goal}",
            "summarize": "Generate summaries of the found leads and their companies",
            "write_email": "Create personalized outreach emails for each lead",
            "send_email": "Send the prepared emails to the leads"
        }
        return descriptions.get(tool, f"Execute {tool} step for: {goal}")
    
    def _fallback_breakdown(self, goal: str) -> List[Dict]:
        """
        A simpler fallback method for breaking down goals if no pattern matches.
        """
        return [
            {
                "step_id": 1,
                "description": "Research and find relevant leads",
                "tool": "search",
                "status": "pending",
                "created_at": datetime.now().isoformat()
            },
            {
                "step_id": 2,
                "description": "Generate personalized emails for each lead",
                "tool": "write_email",
                "status": "pending",
                "created_at": datetime.now().isoformat()
            },
            {
                "step_id": 3,
                "description": "Send the emails",
                "tool": "send_email",
                "status": "pending",
                "created_at": datetime.now().isoformat()
            }
        ] 