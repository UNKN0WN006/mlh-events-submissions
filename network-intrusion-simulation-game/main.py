"""
Super Rare Network Game: A command-line adventure where you defend a secret space mission from cyber threats.
"""

def main():
    print("""
    =====================================
    SUPER RARE NETWORK DEFENDER SIMULATOR
    =====================================
    You are the lead cybersecurity engineer for a top-secret space mission.
    Your goal: Protect the mission from cyber attacks and keep the crew safe!
    """)
    score = 0
    incidents = [
        {
            "desc": "A suspicious login attempt is detected from a foreign country.",
            "choices": [
                "Ignore it.",
                "Investigate and block the IP.",
                "Alert the crew and reset all passwords."
            ],
            "correct": 1
        },
        {
            "desc": "Malware is found on a mission-critical server.",
            "choices": [
                "Quarantine the server and analyze the malware.",
                "Reboot the server and hope for the best.",
                "Delete all files to remove the malware."
            ],
            "correct": 0
        },
        {
            "desc": "Encrypted traffic is detected between the spacecraft and an unknown ground station.",
            "choices": [
                "Monitor the traffic for now.",
                "Immediately cut off all communications.",
                "Initiate secure protocol and investigate the source."
            ],
            "correct": 2
        }
    ]
    for i, incident in enumerate(incidents):
        print(f"\nIncident {i+1}: {incident['desc']}")
        for idx, choice in enumerate(incident['choices']):
            print(f"  {chr(65+idx)}) {choice}")
        user = input("Your choice (A/B/C): ").strip().upper()
        if user == chr(65 + incident['correct']):
            print("Correct! Mission secure.")
            score += 1
        else:
            print("Not the best choice. The mission is at risk!")
    print(f"\nGame Over! You secured {score} out of {len(incidents)} incidents.")
    if score == len(incidents):
        print("Legendary! The mission is a total success.")
    elif score > 0:
        print("Not bad, but there were some close calls.")
    else:
        print("Mission failed. The space agency needs you to train harder!")

if __name__ == "__main__":
    main()
