nums=input("enter the numbers using any seperatiors you like : ")
seperators=""

for x in nums:
    if not x.isnumeric():
        seperators+=x

print(seperators)