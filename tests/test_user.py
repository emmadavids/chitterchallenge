from lib.user import *

def test_user_instantiates():
    emma = User(1, "Emma", "Emu", "helloworld", "chocolate@coffee.com")
    assert emma.id == 1
    assert emma.actualname == "Emma"
    assert emma.username == "Emu"
    assert emma.password == "helloworld"
    assert emma.email == "chocolate@coffee.com"