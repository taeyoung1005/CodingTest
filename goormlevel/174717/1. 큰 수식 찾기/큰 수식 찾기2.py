first_input, last_input = map(str, input().split())

temp1 = eval(first_input)
temp2 = eval(last_input)

print(temp1 if temp1 > temp2 else temp2)
