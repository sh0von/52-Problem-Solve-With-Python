T =int(input())
for i in range (T):
    number  = input("Enter number: ")
    # Reversing number
    reverse = number[::-1]
    # Converting number and its reverse to integer
    number = int(number)
    reverse = int(reverse)
    #  Finding first digit
    first_digit = reverse % 10
    # Finding last digit
    last_digit = number % 10
    # Finding sum
    total_sum = first_digit + last_digit
    # Displaying sum
    print("Sum of first & last digit of %d is %d" %(number, total_sum))