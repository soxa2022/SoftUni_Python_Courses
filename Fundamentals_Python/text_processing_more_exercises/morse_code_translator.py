code = [x.strip() for x in input().split(" | ")]
morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
         '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
         '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V',
         '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
text = []
for words in code:
    chars = words.split()
    word = ''
    for ch in chars:
        word += morse[ch]
    text.append(word)
print(" ".join(text))
