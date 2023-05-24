from lib.peep import *
import datetime

def test_peep_instantiates():
    peep = Peep(1, "hello world", datetime.datetime.now(), 1)
    assert peep.id == 1
    assert peep.content == "hello world"
    assert peep.user_id == 1
    assert isinstance(peep.time, datetime.datetime)