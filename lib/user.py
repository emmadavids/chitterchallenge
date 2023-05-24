class User:
    def __init__(self, id, actualname, username, password, email):
        self.id = id
        self.actualname = actualname
        self.username = username
        self.password = password
        self.email = email
    
    def __eq__(self, other):#allows us to compare if one instance of artist is equal to another, by comparing all properties shown above
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.actualname}, {self.username}, {self.password}, {self.email})"
    # def is_valid(self):
    #     if self.artist_name == None or self.artist_name == "":
    #         return False
    #     if self.genre == None or self.genre == "":
    #         return False
    #     return True

    # def generate_errors(self):
    #     errors = []
    #     if self.artist_name == None or self.artist_name == "":
    #         errors.append("Artist name can't be blank")
    #     if self.genre == None or self.genre == "":
    #         errors.append("genre can't be blank")
    #     if len(errors) == 0:
    #         return None
    #     else:
    #         return ", ".join(errors)

    # @property
    # def is_authenticated(self):
    #     return self.authenticated

    # @property
    # def is_active(self):
    #     return self.active

    # @property
    # def is_anonymous(self):
    #     return False  # Users are never anonymous in this simple example

    # def get_id(self):
    #     return str(self.id)  # Assuming that self.id is an integer

    # def check_password(self, password):
    #     return self.password == password  # Very simple password check

    # def authenticate(self, password):
    #     self.authenticated = self.check_password(password)

    # def logout(self):
    #     self.authenticated = False