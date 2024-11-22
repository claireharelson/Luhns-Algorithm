# using Luhn's verification to validate a credit card number

# using a while loop to run 2 iterations for the 2 CC numbers
iteration = 0
while iteration < 2:
    iteration += iteration + 1
    card_number = input("Enter credit card number here: ")
    Checksum1 = 0
    Checksum2 = 0

# calculating the even digits, working left to right
    for i in range(1, 16, 2):
        Checksum1 += int(card_number[i])

# calculating the odd digits, working left to right
    for i in range(0, 16, 2):
        n = int(card_number[i])*2
        if n >= 10:     # any 2 digit output will be added together
            n = str(n)
            Checksum2 += int(n[0]) + int(n[1])
        else:
            Checksum2 += n

    # calculate total sum
    Checksum = str((Checksum1 + Checksum2)%10)
    valid_value = int(Checksum[len(Checksum)-1])

    print("Checksum = " + Checksum)

    if valid_value == 0:
        print(card_number + " is a valid CC number.")
    else:
        print(card_number + " is an invalid CC number.")