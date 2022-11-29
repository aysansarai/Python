# Task 1 -- Basic
for i in range(151):
    print(i)

# Task 2 -- Multiples of Five 
for i in range(5, 1001):
    if(i % 5 == 0):
        print(i)

# Task 3 -- Counting, the Dojo Way 
for i in range(1, 101):
    if(i % 5 == 0):
        print("Coding")
    elif(i % 10 == 0):
        print("Coding Dojo")

# Task 4 -- Whoa. That Sucker's Hugecd D
sum = 0
for i in range(0, 500000):
    if(i % 2 != 0):
        sum += i
print(sum)

# Task 5 -- Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# Task 6 -- Flexible Counter 
def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum,highNum+1):
        if(i % mult == 0):
            print(i)

flexibleCounter(2,9,3)

