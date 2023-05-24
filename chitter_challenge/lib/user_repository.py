from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["actualname"], row["username"], row["password"], row["email"])
            users.append(item)
        return users
    
    def create(self, user):
        found_username = self._connection.execute('SELECT * FROM users WHERE username = %s', [user.username])
        found_email = self._connection.execute('SELECT * FROM users WHERE email = %s', [user.email])

        if not found_username and not found_username:
            self._connection.execute(
                'INSERT INTO users (actualname, username, password, email) VALUES (%s, %s, %s, %s)',
                [user.actualname, user.username, user.password, user.email]
                )
        else:
            if found_email:
                return "email already has account"
            elif found_username:
                return "username already taken"


        # Return the conflict as a string
        
    def find_by_username(self, username):
        row = self._connection.execute('SELECT * FROM users WHERE username = %s', [username])
        if row is not None:
            return User(row[0]["id"], row[0]["actualname"], row[0]["username"], row[0]["password"], row[0]["email"])
        else:
            return None