computer_parts=[]
choice="-"

while choice !='0':
    if choice in "1234560":
        print(f"you have entered {choice} choice")
    else:
        print('''enter choices from below:
              1:hans
              2.lace
              3.lance
              4.tamn
              5.booke
              6.nadsad
              0.exit''')
    choice=input()
