input_line = input()
percent_seats = 0
count_tickets = 0
total_tickets = 0
count_kid_ticket = 0
count_standard_ticket = 0
count_student_ticket = 0
total_kid_tickets = 0
total_standard_tickets = 0
total_student_tickets = 0
while input_line != "Finish":
    free_seats = int(input())
    type_ticket = input()
    while type_ticket != "End":
        if type_ticket == "kid":
            count_kid_ticket += 1
        elif type_ticket == "standard":
            count_standard_ticket += 1
        elif type_ticket == "student":
            count_student_ticket += 1
        count_tickets = count_kid_ticket + count_student_ticket + count_standard_ticket
        if count_tickets == free_seats:
            break
        type_ticket = input()
    percent_seats = (count_tickets / free_seats) * 100
    print(f"{input_line} - {percent_seats:.2f}% full.")
    total_tickets += count_tickets
    total_kid_tickets += count_kid_ticket
    total_standard_tickets += count_standard_ticket
    total_student_tickets += count_student_ticket
    count_kid_ticket = 0
    count_standard_ticket = 0
    count_student_ticket = 0
    count_tickets = 0
    input_line = input()
print(f"Total tickets: {total_tickets}")
print(f"{(total_student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(total_standard_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(total_kid_tickets / total_tickets * 100):.2f}% kids tickets.")
