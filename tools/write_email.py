from typing import List, Dict

class EmailWriter:
    def __init__(self):
        # Define templates for different tones
        self.templates = {
            "professional": (
                "Subject: Unlock New Possibilities with Our Dev Tool\n\n"
                "Hi {name},\n\n"
                "I came across your work at {company} and was impressed by your impact in the AI space. "
                "We're building a new developer tool that could help {company_description}. "
                "Would you be open to a quick chat about how it might benefit your team?\n\n"
                "Best regards,\nYour Name"
            ),
            "friendly": (
                "Subject: Quick Hello from a Fellow AI Enthusiast!\n\n"
                "Hey {name},\n\n"
                "Saw what you're doing at {company}—super cool! "
                "I've been working on a dev tool that could be a great fit for {company_description}. "
                "Want to connect and swap ideas?\n\n"
                "Cheers,\nYour Name"
            ),
            "funny": (
                "Subject: This Email Contains 0% Spam, 100% AI Magic 🪄\n\n"
                "Hi {name},\n\n"
                "Promise this isn't a robot (well, maybe a little). "
                "Loved what you're doing at {company}. "
                "I've got a dev tool that could make {company_description} even cooler. "
                "Up for a quick chat? I promise no more puns.\n\n"
                "To infinity and beyond,\nYour Name"
            )
        }
    
    def write_emails(self, leads: List[Dict], tone: str = "professional") -> List[Dict]:
        """
        Generate personalized emails for each lead using the selected tone.
        Args:
            leads (List[Dict]): List of leads
            tone (str): Email tone ('professional', 'friendly', 'funny')
        Returns:
            List[Dict]: List of emails with subject and body
        """
        template = self.templates.get(tone, self.templates["professional"])
        emails = []
        for lead in leads:
            email_body = template.format(
                name=lead["name"],
                company=lead["company"],
                company_description=lead.get("company_description", "their work")
            )
            emails.append({
                "to": lead["email"],
                "subject": email_body.split("\n")[0].replace("Subject: ", ""),
                "body": "\n".join(email_body.split("\n")[1:]),
                "lead": lead
            })
        return emails 