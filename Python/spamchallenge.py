menu = [
["egg", "bacon"],
["egg", "sausage", "bacon"],
["egg", "spam"],
["egg", "bacon", "spam"],
["egg", "bacon", "sausage", "spam"],
["spam", "bacon", "sausage", "spam"],
["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for lis in menu:
    #print("list is : {} ".format(i))
    for index in range(len(lis)-1,-1,-1):
        if lis[index]== "spam":
            del lis[index]
    print(lis)
