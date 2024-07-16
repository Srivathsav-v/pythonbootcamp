'''
Input:
num - a list of integers with maximum length of 1000
target - integer

Output:
print the two numbers whose sum is equal target

Conditions:
len(nums) < 1000

'''

''''
Your logic in sudo code - plain english

initial logic:
i thought of taking two for loops and iterating them and comparingh 
each value with all the values from the list and adding the first loop value and
the second loop value is traget then print those value along with their indexes


we will start by taking a list, target value and an empty dictonary 
first we iterate throuh indexes and range of length of the given list
after that we will check through the difference of the number from the 
list(by using the index) with the target value i.e difference= target - number from the list
after that we check this difference if it is there on hashmap(dict), if it is there in dict 
then we print the value and difference
if it is not there in the dictonary we strore the value and index in the dictonary

'''

'''
Implement Testcase
testcase 1:
    a=[2,7,8,9,12]
    target=17

    expected output: [8,9] indexes are [2 3]

testcase 2:
a=[2,7,8,9,12]
target=9

expected output: [2,7] indexes are [0 1]

testcase 3:
a=[2,7,8,9,12]
target = 24

expected output:nothing as there is no repeated numbers in the list

testcase 4:
a=[2,7,8,9,12,12]
target=24

expected output: [2,7] indexes are [0 1]

testcase 5:
a=[2,7,8,9,14,-1]
target=13

expected output: 14 -1  and indexes are  4 5

testcase 6:
a=[2,7,8,9,14,-1,-3,-5]
target=-6

op:--1 -5  and indexes are  5 7

testcase 7:
a=[0,0]
target=0

op:-0 0  and indexes are  0 1

testcase 8:
a=[]
target=0

op:-nothing
'''

a=[2,7,8,9,12]
target = 9

hashmap={}

for i in range(len(a)):
    # print(i,a[i])
    j=target-a[i]
    # print(j)
    k=a[i]
    if j in hashmap.keys():
        print(j,a[i]," and indexes are ",hashmap.get(j),i)
        break

    else:
        hashmap[a[i]]=i

# print(hashmap)    



# for i in a:
#     for j in a:
#         if(i+j==target):
#             print("Found the two sum numbers", i,j)

# Rohin comments on  exit() statement

# Find answers/ Read about below 
# how to come out of running loop
'''to come out of the running loop we have to use break ,It stops the execution of the loop and
resumes execution at the next statement after the loop.'''


# how to exit from the program
'''quit and exit these both when used stops the exicution of the program 
so we should never use it in loops as it terminates the programn and doesnot execute any statements 
after the loop'''
# Implement range logic in for loop
# pydocs
# pytest - Testing Framework
# unittest - Unit Testing

