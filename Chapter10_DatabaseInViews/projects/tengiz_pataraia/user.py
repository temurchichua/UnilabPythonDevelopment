class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.username
    
    def check_password(self,password):
        if self.password == password:
            return True
        else:
            return False