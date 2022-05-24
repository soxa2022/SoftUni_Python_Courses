input_line = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0
while input_line != "stop":
    number = int(input_line)
    if number < 0:
        print("Number is negative.")
        input_line = input()
        continue
    count = 0
    for i in range(1, number + 1):
        if (number % i) == 0:
            count += 1
    if count == 2:
        sum_prime_numbers += number
    else:
        sum_non_prime_numbers += number
    # for i in range(2, number):
    #     if (number % i) == 0:
    #         sum_non_prime_numbers += number
    #         break
    # else:
    #     sum_prime_numbers += number
    input_line = input()
print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
