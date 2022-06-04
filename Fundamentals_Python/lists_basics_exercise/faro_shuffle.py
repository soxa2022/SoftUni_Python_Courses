# lst_cards = [card for card in input().split(' ')]
lst_cards = input().split(" ")
count_shuffles = int(input())
index = len(lst_cards) // 2
for _ in range(count_shuffles):
    first_deck = lst_cards[:index]
    second_deck = lst_cards[index:]
    lst_cards = []  # shuffle_deck = lst_cards
    for idx in range(len(first_deck)):
        lst_cards.append(first_deck[idx])
        lst_cards.append(second_deck[idx])
print(lst_cards)
