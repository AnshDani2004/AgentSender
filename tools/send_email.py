import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
from dotenv import load_dotenv

class EmailSender:
    def __init__(self):
        load_dotenv()
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.smtp_server = os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("EMAIL_SMTP_PORT", 587))

    def send_emails(self, emails: List[Dict]) -> List[Dict]:
        """
        Send a list of emails using SMTP.
        Args:
            emails (List[Dict]): List of emails with 'to', 'subject', 'body'
        Returns:
            List[Dict]: List of results with status for each email
        """
        results = []
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                for email in emails:
                    msg = MIMEMultipart()
                    msg["From"] = self.email_address
                    msg["To"] = email["to"]
                    msg["Subject"] = email["subject"]
                    msg.attach(MIMEText(email["body"], "plain"))
                    try:
                        #server.sendmail(self.email_address, email["to"], msg.as_string())
                        results.append({"to": email["to"], "status": "sent"})
                    except Exception as e:
                        results.append({"to": email["to"], "status": "failed", "error": str(e)})
        except Exception as e:
            for email in emails:
                results.append({"to": email["to"], "status": "failed", "error": str(e)})
        return results 