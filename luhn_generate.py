# using Luhn's generation to determine check number

identifier = input("Please enter an identifier: ")
sum1 = 0
sum2 = 0

# calculating the even numbers, working right to left
for i in range(-2, -16, -2):
    sum1 += int(identifier[i])

# calculating the odd numbers, working right to left
for i in range(-1, -16, -2):
   n = int(identifier[i])*2
   if n >= 10:  # any 2 digit output will be added together
       n = str(n)
       sum2 += int(n[0]) + int(n[1])
   else:
       sum2 += n

# calculate total sum
sum = str(10 - ((sum1 + sum2)%10))

print("The valid credit card number is: " + identifier + sum + " and the newly computed check digit is: " + sum)