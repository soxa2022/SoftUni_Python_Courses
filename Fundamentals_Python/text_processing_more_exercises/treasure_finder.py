def find_code(text, nums, i=0):
    message = ""
    for ch in text:
        message += chr(ord(ch) - nums[i])
        if i < len(nums) - 1:
            i += 1
        else:
            i = 0
    return message


def code(msg: str):
    index = msg.index("&")
    new_msg = msg[index + 1:]
    msg_end = new_msg.index("&")
    types = new_msg[:msg_end]
    start = new_msg.index("<")
    end = new_msg.index(">")
    coordinates = new_msg[start + 1:end]
    return f"Found {types} at {coordinates}"


numbers = [int(x) for x in input().split()]
while True:
    symbols = input()
    if symbols == "find":
        break
    print(code(find_code(symbols, numbers)))
