from lib.user_repository import UserRepository
from lib.user import User 


def test_get_all_users(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/peepers.sql")  # Seed our database with some test data
    repository = UserRepository(db_connection)  # Create a new UserRepository
    users = repository.all()  # Get all users
    # Assert on the results
    print(users)
    assert users == [
        User(1, 'Merlin', 'MysteriousMerlin', 'potion123', 'merlin@magic.com'),
        User(2, 'Fiona', 'FabulousFiona', 'dragon789', 'fiona@fantasy.com'),
        User(3, 'Dante', 'DynamicDante', 'spell456', 'dante@divine.com'),
    ]
    

def test_create_user(db_connection):
    db_connection.seed("seeds/peepers.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "Emma Davids", "emmaqueenofcarbs", "percypigs", "ilovesunshine@beach.com"))
    result = repository.all()
    assert result == [
        User(1, 'Merlin', 'MysteriousMerlin', 'potion123', 'merlin@magic.com'),
        User(2, 'Fiona', 'FabulousFiona', 'dragon789', 'fiona@fantasy.com'),
        User(3, 'Dante', 'DynamicDante', 'spell456', 'dante@divine.com'),
        User(4, "Emma Davids", "emmaqueenofcarbs", "percypigs", "ilovesunshine@beach.com")
    ]

# def test_delete_user(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
#     repository = UserRepository(db_connection) # Create a new ArtistRepository
#     users = repository.delete(1) # Get all artists
#     # Assert on the results
#     result = repository.all()
#     assert result == [
#         User(2, 'Jane Smith', 'janesmith@example.com'),
#     ]
