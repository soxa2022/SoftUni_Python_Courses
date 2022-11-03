class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        username, mail_with_domain = email.split("@")
        mail, domain = mail_with_domain.split('.')
        return all([self.__is_name_valid(username), self.__is_domain_valid(domain), self.__is_mail_valid(mail)])