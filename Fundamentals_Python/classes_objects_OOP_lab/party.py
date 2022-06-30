# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# name = input()
# while name != "End":
#     party.people.append(name)
#     name = input()
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")


class Party:
    def __init__(self):
        self.people = []

    def get_info(self):
        all_people = self.people
        # return f'Going: {", ".join(all_people)}\nTotal: {len(all_people)}'
        return f"""Going: {', '.join(all_people)}
Total: {len(all_people)}"""


name = input()
party = Party()
while True:
    if name == "End":
        break
    party.people.append(name)
    name = input()
info = party.get_info()
print(info)
