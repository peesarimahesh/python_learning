largest = 0
while True:
    l1 = input('Enter a number')
    if l1 == 'done':
        break
    try:
        l1_f = float(l1)
    except:
        print('Invalid input')
        continue
    if l1_f > largest:
        largest = l1
        print(largest, l1)
print('Final largest number is', largest)
