import json
import os
from datetime import datetime
from typing import Dict, List, Any
import pandas as pd

class MemoryStorage:
    def __init__(self, logs_dir: str = "logs"):
        self.logs_dir = logs_dir
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create necessary directories if they don't exist."""
        os.makedirs(self.logs_dir, exist_ok=True)
        os.makedirs(os.path.join(self.logs_dir, "leads"), exist_ok=True)
        os.makedirs(os.path.join(self.logs_dir, "emails"), exist_ok=True)
        os.makedirs(os.path.join(self.logs_dir, "steps"), exist_ok=True)
    
    def save_leads(self, leads: List[Dict]):
        """Save discovered leads to a JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.logs_dir, "leads", f"leads_{timestamp}.json")
        
        with open(filename, 'w') as f:
            json.dump({
                "timestamp": timestamp,
                "leads": leads
            }, f, indent=2)
    
    def save_email(self, email_data: Dict):
        """Save a generated email to a JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.logs_dir, "emails", f"email_{timestamp}.json")
        
        with open(filename, 'w') as f:
            json.dump({
                "timestamp": timestamp,
                **email_data
            }, f, indent=2)
    
    def save_step(self, step_data: Dict):
        """Save a completed step to a JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.logs_dir, "steps", f"step_{timestamp}.json")
        
        with open(filename, 'w') as f:
            json.dump({
                "timestamp": timestamp,
                **step_data
            }, f, indent=2)
    
    def get_all_leads(self) -> List[Dict]:
        """Retrieve all saved leads."""
        leads = []
        leads_dir = os.path.join(self.logs_dir, "leads")
        
        for filename in os.listdir(leads_dir):
            if filename.endswith('.json'):
                with open(os.path.join(leads_dir, filename), 'r') as f:
                    data = json.load(f)
                    leads.extend(data.get("leads", []))
        
        return leads
    
    def get_all_emails(self) -> List[Dict]:
        """Retrieve all saved emails."""
        emails = []
        emails_dir = os.path.join(self.logs_dir, "emails")
        
        for filename in os.listdir(emails_dir):
            if filename.endswith('.json'):
                with open(os.path.join(emails_dir, filename), 'r') as f:
                    emails.append(json.load(f))
        
        return emails
    
    def get_all_steps(self) -> List[Dict]:
        """Retrieve all saved steps."""
        steps = []
        steps_dir = os.path.join(self.logs_dir, "steps")
        
        for filename in os.listdir(steps_dir):
            if filename.endswith('.json'):
                with open(os.path.join(steps_dir, filename), 'r') as f:
                    steps.append(json.load(f))
        
        return steps
    
    def export_to_csv(self, data_type: str = "leads"):
        """Export data to CSV format."""
        if data_type == "leads":
            data = self.get_all_leads()
            df = pd.DataFrame(data)
        elif data_type == "emails":
            data = self.get_all_emails()
            df = pd.DataFrame(data)
        elif data_type == "steps":
            data = self.get_all_steps()
            df = pd.DataFrame(data)
        else:
            raise ValueError(f"Unknown data type: {data_type}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.logs_dir, f"{data_type}_{timestamp}.csv")
        df.to_csv(filename, index=False)
        return filename 