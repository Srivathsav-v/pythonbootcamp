def palindrome(x):
    reversed = x[-1::-1]
    return x.casefold() ==  reversed.casefold()

def palindrome_sentence(x):
    x=""
    for char in x:
        if char.isalnum():
            string+=char

    return x.casefold() ==  x[::-1].casefold()


sentence=input("enter a sentence : ")
if palindrome_sentence(sentence):
    print(f" '{sentence}' is a palindrome ")
else:
    print(f" '{sentence}' is not a palindrome ")

# word=input("enter a word : ")
# 