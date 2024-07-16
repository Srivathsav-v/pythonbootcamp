
name=str(input("enter your name: "))
age=int(input(f"whats your age {name}: "))
print(f"your name is {name} and age is {age}")

print("hello {0} you are {1}".format(name,age))

if age>=18 :
    print("you can vote")
else:
    print("you cannot vote, you have still {} years left".format(18-age))
