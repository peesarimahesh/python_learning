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

