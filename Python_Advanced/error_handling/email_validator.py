from re import findall, match


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


domain_list = ['.com', '.bg', '.org', '.net']
check_list = []
line_input = input()

pattern = r"^[A-Za-z]{4,}"
domain_pattern = r'\.[a-z]+$'
valid_pattern = r'\b[a-z]{4,}@[a-z]+\.[a-z]{2,3}\b'
while not line_input == 'End':
    if len(findall(pattern, line_input)) == 0:
        raise NameTooShortError('Name must be more than 4 characters')
    elif '@' not in line_input:
        raise MustContainAtSymbolError("Email must contain @")
    elif findall(domain_pattern, line_input)[0] not in domain_list:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    elif match(valid_pattern, line_input):
        print("Email is valid")
    else:
        raise InvalidEmailError('Invalid email')
    line_input = input()

# while not line_input == 'End':
#     if '@' in line_input[:5]:
#         raise NameTooShortError('Name must be more than 4 characters')
#     if '@' not in line_input:
#         raise MustContainAtSymbolError("Email must contain @")
#     for domain in domain_list:
#         if domain not in line_input:
#             check_list.append(False)
#         else:
#             check_list.append(True)
#     if not any(check_list):
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#     else:
#         print("Email is valid")
#     line_input = input()
