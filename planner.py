import openai
import os
from typing import List, Dict
import json
from datetime import datetime

class GoalPlanner:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def break_down_goal(self, goal: str) -> List[Dict]:
        """
        Break down a high-level goal into specific, actionable steps using GPT-4.
        
        Args:
            goal (str): The high-level goal provided by the user
            
        Returns:
            List[Dict]: A list of steps, each containing:
                - step_id: Unique identifier
                - description: What needs to be done
                - tool: Which tool to use
                - status: Current status (pending, in_progress, completed)
        """
        prompt = f"""
        Break down the following goal into specific, actionable steps:
        "{goal}"
        
        For each step, specify:
        1. A clear description of what needs to be done
        2. Which tool should be used (search, summarize, write_email, send_email)
        3. Any specific parameters or requirements
        
        Format the response as a JSON array of steps.
        """
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a task planning expert. Break down goals into clear, actionable steps."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            
            # Parse the response and add metadata
            steps = json.loads(response.choices[0].message.content)["steps"]
            
            # Add metadata to each step
            for i, step in enumerate(steps):
                step["step_id"] = i + 1
                step["status"] = "pending"
                step["created_at"] = datetime.now().isoformat()
            
            return steps
            
        except Exception as e:
            # Log the error and retry with a simpler prompt
            print(f"Error in goal breakdown: {str(e)}")
            return self._fallback_breakdown(goal)
    
    def _fallback_breakdown(self, goal: str) -> List[Dict]:
        """
        A simpler fallback method for breaking down goals if the main method fails.
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