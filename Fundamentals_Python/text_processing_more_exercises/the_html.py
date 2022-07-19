title = input()
content = input()
comment = input()
print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t{content}\n</article>")
while not comment == "end of comments":
    print(f"<div>\n\t{comment}\n</div>")
    comment = input()