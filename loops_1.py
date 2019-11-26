# Question 1: Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum

val = 1
val1 = 0
while True:
    num = input('Enter the values:')
    if num == 'done':
        break
    try:
        num1 = float(num)
    except:
        print('Invalid input')
        continue
    val = val * int(num)
    val1 = val1 + int(num)
    if val > 1000:
        val = val1
print(val)

# Question 2: Given a range of numbers. Iterate from o^th number to the end number
# and print the sum of the current number and previous number
j = 0
for i in [1,2,3,4,5,6]:
    j = j + i
print(j)

# Question 3: Accept string from the user and display only those characters
# which are present at an even index
str = input('Enter a string value:')
#cnt = len(str)
for i,c in enumerate(str):
    if i % 2 == 0:
        #print(i)
        print(c)
# solution2, copied
for i in range(0, len(str), 2):
    print(str[i])

# Question 4: Given a string and an int n, remove characters from string starting
# from zero up to n and return a new string
str = input('Enter a string value:')
num = input('Enter a string value:')
val = ''
for i in range(len(str)):
    if i >= int(num):
        val = val + str[i]
print(val)

# Question 5: Given a list of ints, return True if first and last number of a list is same
num = input('Enter a number value:')
if num[0] == num[len(num)-1]:
    print('True')

# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
l1 = [5,7,9,10,11,13,15,17,20,21,25,30]
for i in range(len(l1)-1):
    if l1[i] % 5 == 0:
        print(l1[i])

# Question 7: Return the number of times that the string “Emma” appears anywhere in the given string
str = "Emma is a good developer. Emma is also a writer."
print(str.count("Emma"))

# Question 8: Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
for i in range(6):
    for j in range(i):
        print(i, end = ' ')
    print("")

# Question 9: Reverse a given number and return true if it is the same as the original number

