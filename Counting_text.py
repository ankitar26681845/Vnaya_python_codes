# Write a program to find the number of words in the text entered by the user and then sort the words.
text = input("enter the input")
word = text.split()
count = 0
for i in word:
    count +=1
print(f"the total number of words are {count}")
word.sort()
print("The sorted order for the text is ")
for w in word:
    print("{}".format(w))
