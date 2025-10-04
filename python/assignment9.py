'''Student Score Analysis (Dictionaries + Looping)
You are given a dictionary of students and their marks:
scores = {"Alice": 85, "Bob": 67, "Charlie": 92, "Diana": 67, "Ethan": 75}
Write a program to:
Find the student(s) with the highest score.
Find all students who scored the lowest marks.
Print the results in the format:
Top scorer(s): Charlie with 92
Lowest scorer(s): Bob, Diana with 67
Due: 01/10/2025, 07:00:00'''

scores = {"Alice": 85, "Bob": 67, "Charlie": 92, "Diana": 67, "Ethan": 75}
list_val=[]
for v in scores.values():
    list_val.append(v)
list_val.sort(reverse=True)
print(f"score: {list_val}")
hscore=""
lscore =[]
lenvalue=len(list_val)-1
for k,v in scores.items():
    if(v==list_val[0]):
        hscore=k
    if(v==list_val[lenvalue]):
        lscore.append(k)
print(f"Top scorer(s): {hscore} with  {list_val[0]}")
print(f"Lowest scorer(s): {lscore} with {list_val[lenvalue]}")


print("===================")

scores = {"Alice": 85, "Bob": 67, "Charlie": 92, "Diana": 67, "Ethan": 75}

# Get all scores
all_scores = list(scores.values())

# Find highest and lowest scores
highest = max(all_scores)
lowest = min(all_scores)

# Find students with those scores
top_scorers = [name for name, score in scores.items() if score == highest]
low_scorers = [name for name, score in scores.items() if score == lowest]

# Format output
print(top_scorers)
print(f"Top scorer(s): {', '.join(top_scorers)} with {highest}")
print(f"Lowest scorer(s): {', '.join(low_scorers)} with {lowest}")