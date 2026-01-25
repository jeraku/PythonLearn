s = "A man, a plan, a canal: Panama"
# s=s.replace(" ", "").replace(",", "").replace(":", "")
# s=s.lower()
# print(s)
special = [","]
for val in s:
    # if val in s:
    #     print(val)
    print(val)
    if val.isalpha():
        print(val)

# print(s[::-1])