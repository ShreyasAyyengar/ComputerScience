class User:
    def __init__(self, username, password, email, age, verification_question, is_admin):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.verification_question = verification_question
        self.is_admin = is_admin

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

    def get_verification_question(self):
        return self.verification_question

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_age(self, age):
        self.age = age

    def set_verification_question(self, question):
        self.verification_question = question

    def is_admin(self):
        return self.is_admin

