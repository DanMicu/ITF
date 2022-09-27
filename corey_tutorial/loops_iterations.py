nums = [1,2,3,4,5]
for num in nums: # for loops go through a certain number of values
    for letter in 'abc': #loop within a loop
        print(num,letter)
    if num == 3:
        print("found it!")
        # break # stops when it finds the value we wanted for num in the list
        continue # finds the value we wanted and then continues the loop
    print(num)


# for i in range(10): # starts at 0 and and goes up to but not including the number in brackets
#     print(i)

# for i in range(1,11): # from 1 and up to but not including 11
#     print(i)

# while loops keep going until a certain condition is met or until break

# x = 0
# while True: # infinite loop
# # while x < 10: # while x is lower than 10 the loop runs, when it reaches 10 it asks python if 10<10 which is false so it stops
#     # if x == 5:
#     #     break # stops when it finds the value we wanted (5)
#     print(x)
#     x += 1