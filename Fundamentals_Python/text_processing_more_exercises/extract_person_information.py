number = int(input())
name = ""
age = ''
for _ in range(number):
    text = input()
    start_idx = text.index("@")
    end_idx = text.index("|")
    name = text[start_idx + 1:end_idx]
    start_idx = text.index("#")
    end_idx = text.index("*")
    age = text[start_idx + 1:end_idx]
    print(f"{name} is {age} years old.")
