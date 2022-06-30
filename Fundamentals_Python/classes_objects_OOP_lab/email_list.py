class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


input_line = input()
lst_emails = list()
while input_line != "Stop":
    commands = input_line.split(" ")
    s = commands[0]
    r = commands[1]
    c = commands[2]
    email = Email(s, r, c)
    lst_emails.append(email)
    input_line = input()
indices = list(map(int, input().split(", ")))
for i in range(len(lst_emails)):
    current_email = lst_emails[i]
    if i in indices:
        current_email.send()
    print(current_email.get_info())
