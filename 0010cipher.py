import string
word = input()
numbers = []
for i in range(len(word)):
    number = string.ascii_lowercase.index(word[i].lower())
    numbers.append(number+1)
numbers.reverse()
for i in numbers:
    print(i, end = " ")
