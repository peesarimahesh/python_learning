largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num1 = float(num)
    except:
        print('Invalid input')
        continue
    if int(num) > largest:
        largest = int(num)
        #print('largest')
        #print(largest,num)
    if smallest is None:
        smallest = int(num)
    elif int(num) < smallest:
        smallest = int(num)
print('Maximum is', largest)
print('Minimum is', smallest)