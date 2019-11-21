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

