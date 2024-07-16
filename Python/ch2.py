

print("please choose your option from the list below :")
print("1.\teat")
print("2.\tsleep")
print("3.\tdrink")
print("4.\tcode")
print("0.\texit")

while True:
    choice=input()

    if choice == "0":
        break
    elif choice in "12345":
        print("you chose {}".format(choice))
    

