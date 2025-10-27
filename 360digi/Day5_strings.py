''' string is immutable
'''

inp = "jeganrajkumar"
print(inp[0])

#string slicing (indexing) -> str[start:stop:step]
print(inp[1:3])
print(inp[::-1])

print(inp[-3:-1])
print(inp*3)
print(inp + "test")
print(len(inp))
print(inp[:5])

strlist= list(inp)
print(strlist)
format="%.2f %s is %d"
res = format %(6.4543, "jegans test string fomrat ", 10 )
print(res)
#triple quotes 

result = """ used for 
multi line commenst or string 
vlaues addtion """
print(result)
print(type(result))
test = "pYtHoN Okay"
print(test.capitalize())
print(test.lower())
print(len(test))
print(test.swapcase())
