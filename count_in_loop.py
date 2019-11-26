# to count how many times we execute in a loop, we create a counter
# variable tht starts at 0 and we add one to it.

zork = 0
print('count Before the loop',zork)
for thing in [3,4,5,6,7,12,14,15]:
    zork = zork + 1
    print(zork,thing)
print('Count After the Loop',zork)