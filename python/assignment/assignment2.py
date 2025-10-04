# Write a Python program that hides all digits of a credit card number except the last 4 digits. Replace the hidden part with *.
# Input: "1234567812345678"
# Output: "************5678"

credit_card = "1234567812345678"
last4= len(credit_card)-4 
star = "*"* (len(credit_card)-4)
print(star + credit_card[last4:])