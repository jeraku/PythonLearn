# Write a Python program to decode the message by using string indexing, slicing, and string methods. Extract useful information from the message, such as the agent’s name, code number, or hidden words
# message = "XxYyZz1234HelloAgent007WelcomeToMission"

message = "XxYyZz1234HelloAgent007WelcomeToMission"
agentName=message[0:10]
print(f"Agent name is {agentName}")
codeNumber = message[20:23]
print(f"Agent code is {codeNumber}")
hidden_message =  message[10:20] + " " + message[23:]
print(f"Hidden message is {hidden_message}")