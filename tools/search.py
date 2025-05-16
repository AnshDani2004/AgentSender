from typing import List, Dict
from datetime import datetime

class LeadSearcher:
    def __init__(self):
        self.mock_leads = [
            {
                "name": "Sarah Chen",
                "company": "AI Vision Labs",
                "role": "CEO & Co-founder",
                "email": "sarah@aivisionlabs.com",
                "company_description": "Building computer vision solutions for healthcare diagnostics"
            },
            {
                "name": "Michael Rodriguez",
                "company": "NLP Innovations",
                "role": "Founder & CTO",
                "email": "michael@nlpinnovations.com",
                "company_description": "Developing advanced natural language processing tools for enterprise"
            },
            {
                "name": "Emma Thompson",
                "company": "RoboLearn",
                "role": "CEO",
                "email": "emma@robolearn.ai",
                "company_description": "Creating AI-powered educational robots for children"
            }
        ]
    
    def search_leads(self, query: str, num_leads: int = 5) -> List[Dict]:
        """
        Search for leads based on a query. Uses mock data for testing.
        
        Args:
            query (str): Search query (e.g., "AI startup founders")
            num_leads (int): Number of leads to return
            
        Returns:
            List[Dict]: List of leads, each containing:
                - name: Lead's name
                - company: Company name
                - role: Their role
                - email: Email address
                - company_description: Brief company description
        """
        # Return a subset of mock leads based on num_leads
        leads = self.mock_leads[:min(num_leads, len(self.mock_leads))]
        
        # Add metadata to each lead
        for lead in leads:
            lead["found_at"] = datetime.now().isoformat()
            lead["source"] = "mock_data"
        
        return leads
    
    def _generate_fallback_leads(self, query: str, num_leads: int) -> List[Dict]:
        """
        Generate fallback leads if the main search fails.
        """
        return [
            {
                "name": "John Smith",
                "company": "AI Innovations Inc",
                "role": "CEO & Founder",
                "email": "john@aiinnovations.com",
                "company_description": "AI startup focused on machine learning solutions",
                "found_at": datetime.now().isoformat(),
                "source": "fallback_generator"
            }
        ] * num_leads 