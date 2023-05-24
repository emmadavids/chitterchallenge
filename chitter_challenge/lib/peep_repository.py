from lib.peep import *
import datetime

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT peeps.*, users.username FROM peeps INNER JOIN users ON peeps.user_id = users.id ORDER BY time DESC')
        peeps = []
        usernames = {}
        for row in rows:
            time = row["time"].replace(microsecond=0)
            item = Peep(row["id"], row["content"], time, row["user_id"])
            peeps.append(item)
            usernames[row["user_id"]] = row["username"]
        return peeps, usernames
        
        
    def create(self, peep):
        now = datetime.datetime.now().replace(microsecond=0)
        self._connection.execute(
            'INSERT INTO peeps (content, time, user_id) VALUES (%s, %s, %s)',
                [peep.content, now, peep.user_id]
                )
