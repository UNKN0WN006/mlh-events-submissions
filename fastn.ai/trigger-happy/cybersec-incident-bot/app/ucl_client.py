import os
import requests
from dotenv import load_dotenv
load_dotenv()

SLACK_CHANNEL = os.getenv("SLACK_CHANNEL_ID")

def send_to_slack(type, desc, level):
    # Example UCL call to Slack (pseudo)
    data = {
        "channel": SLACK_CHANNEL,
        "text": f"Incident: {type}\nDesc: {desc}\nLevel: {level}"
    }
    # Replace with actual UCL endpoint and payload
    try:
    # Send incident to UCL agent for Slack action
    data = {
        "channel": SLACK_CHANNEL,
        "text": f"Incident: {type}\nDesc: {desc}\nLevel: {level}"
    }
    try:
        r = requests.post(f"{UCL_URL}/slack/send", json=data)
        if r.status_code == 200:
            return r.json().get("ts", "Sent!")
        return "Failed to send"
    except Exception as e:
        return str(e)
