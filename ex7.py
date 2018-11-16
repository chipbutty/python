#Palindrome - ex.7
#word1 = "kayak"
word1 = raw_input("Enter a word: ")
print word1
word2 = word1[::-1]
print word2
if word1 == word2:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
