book_name = input()
current_book = input()
count_book = 0
is_found_it = False
while current_book != "No More Books":
    if current_book == book_name:
        is_found_it = True
        break
    current_book = input()
    count_book += 1
if is_found_it:
    print(f"You checked {count_book} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count_book} books.")
