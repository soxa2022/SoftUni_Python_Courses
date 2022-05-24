last_sector = input()
count_rows = int(input())
count_places_odd_row = int(input())
count_places_even_row = count_places_odd_row + 2
count_places = 0
for i in range(65, ord(last_sector) + 1):
    for j in range(1, count_rows + 1):
        if j % 2 != 0:
            letter = 97
            for k in range(1, count_places_odd_row + 1):
                print(f"{chr(i)}{j}{chr(letter)}")
                letter += 1
                count_places += 1
        if j % 2 == 0:
            letter = 97
            for m in range(1,  count_places_even_row + 1):
                print(f"{chr(i)}{j}{chr(letter)}")
                letter += 1
                count_places += 1
    count_rows += 1
print(count_places)








