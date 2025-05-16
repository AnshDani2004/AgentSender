import openai
import os
from typing import List, Dict
import json
from datetime import datetime

class LeadSearcher:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def search_leads(self, query: str, num_leads: int = 5) -> List[Dict]:
        """
        Search for leads based on a query. Currently uses GPT to simulate search results.
        In the future, this can be connected to real search APIs.
        
        Args:
            query (str): Search query (e.g., "AI startup founders")
            num_leads (int): Number of leads to return
            
        Returns:
            List[Dict]: List of leads, each containing:
                - name: Lead's name
                - company: Company name
                - role: Their role
                - email: Email address (simulated for now)
                - company_description: Brief company description
        """
        prompt = f"""
        Generate {num_leads} realistic but fictional leads for the following search query:
        "{query}"
        
        For each lead, provide:
        1. Full name
        2. Company name
        3. Role/title
        4. Professional email address
        5. Brief company description
        
        Format the response as a JSON array of leads.
        """
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a lead generation expert. Generate realistic but fictional leads."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            
            leads = json.loads(response.choices[0].message.content)["leads"]
            
            # Add metadata to each lead
            for lead in leads:
                lead["found_at"] = datetime.now().isoformat()
                lead["source"] = "simulated_search"  # Will be replaced with real source in future
            
            return leads
            
        except Exception as e:
            print(f"Error in lead search: {str(e)}")
            return self._generate_fallback_leads(query, num_leads)
    
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