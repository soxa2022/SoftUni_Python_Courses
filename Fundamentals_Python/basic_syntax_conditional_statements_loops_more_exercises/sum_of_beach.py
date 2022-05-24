text = input()
lower = text.lower()
list_words = ["sand", "water", "fish", "sun"]
counter = 0
for word in list_words:
    counter += (lower.count(word))
print(counter)

# text = input()
# lower = text.lower()
# list_words = ["sand", "water", "fish", "sun"]
# counter = 0
# for word in list_words:
#     if word in lower:
#         counter += 1
# print(counter)
# Не работи при наличие на думата word повече от веднъж в текста.

