Name: Claire Harelson (charels1)

Module info: Module 3: Luhn's Algorithm

Approach: For part one of the question, I created a while loop that would execute twice. Within the loop, I created
the variable 'card_number' and prompted the user to input the CC number here. I then created two running variables,
'Checksum1' and 'Checksum2' and equated both to zero. For the even digits I used the range function to begin on the
second digit and parse through the whole CC number skipping one each time. I then set Checksum1 to be the total of
these numbers added together. For the odd digits, I again used the range function to begin on the first digit of
the CC number and include every other number going from left to right. I created a variable 'n' and set it equal to
these numbers multiplied by 2. I used an 'if' statement to have the two-digit numbers added together and 'else' to
have the single digit numbers added directly to Checksum2. I then set the total Checksum to be equal to the individual
Checksums modulo 10 and used an if/else statement to print my desired output.

For the second part of the question, I followed the same process. However, for the range function I used negative
numbers so that the numbers would be calculated from right to left this time. The other difference here was when
calculating the total sum, I used a different equation. I then followed this with a print statement to produce the
desired output.

Known bugs: No known bugs.

Citations: https://www.youtube.com/watch?v=DavcPCzMTxM -- referenced this Youtube video to help determine how to add
the digits together of the two digit outputs after the x2 multiplication of odd digits.