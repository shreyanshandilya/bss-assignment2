import random

print("🔮 Welcome to Shreyansh Shandilya's Fortune Teller (21JE1234) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        "Great things await you, Shreyansh! Keep smiling.",
        "Happiness brings luck—enjoy the moment!",
        "Your joy is contagious. Good vibes ahead!"
    ],
    "sad": [
        "Tough times don’t last, but tough people like you do.",
        "Even the darkest night will end and the sun will rise.",
        "Your strength is inspiring—better days are near."
    ],
    "neutral": [
        "Balance is the key. A surprise is coming your way.",
        "Still waters run deep. Trust the calm.",
        "You are on the right track. Keep going!"
    ],
    "stressed": [
        "Take a deep breath—peace is coming soon.",
        "You're doing great, even if it doesn't feel like it.",
        "Hang in there, Shreyansh! A breakthrough is near."
    ]
}

if mood in fortunes:
    print("✨ Your fortune: " + random.choice(fortunes[mood]) + " ✨")
else:
    print("🤔 I couldn't recognize that mood. Try again with happy/sad/neutral/stressed.")
