leaderboard = [("ssAlice", 95), ("eeBeob", 89), ("ttCharlie", 92), ("qqDave", 87), ("AAEve", 90)]

for i, (name, score) in enumerate(leaderboard[:10], start=1):
    print(f"{i}. {name} - {score} points")