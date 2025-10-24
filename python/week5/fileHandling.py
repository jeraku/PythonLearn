file = open("./python/week5/filename.txt", "w")
# file.write("Jegan Raj Kumar S\n")
# file.write("Jegan Raj Kumar S\n")
# file.write("Jegan Raj Kumar S\n")
file.writelines(
    ["jegan Raj kumar\n", "test lines "]
)
# Iterable -> collection of data
file.close()


file = open("./python/week5/filename.txt", "r")
content = file.readlines()
print(content)
# Iterable -> collection of data
for line in content:
    print(line)
file.close()
