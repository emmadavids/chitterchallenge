from lib.peep_repository import PeepRepository
from lib.peep import Peep
from datetime import datetime, timedelta

def test_get_all_peeps(db_connection):
    db_connection.seed("seeds/peepers.sql")  # Seed our database with some test data
    repository = PeepRepository(db_connection)  # Create a new PeepRepository

    peeps, usernames = repository.all()  # Get all peeps

    assert peeps == [
        Peep(1, 'Just conjured a potion that grants invisibility. Impressive, huh?', datetime.strptime('2023-05-22 15:48', "%Y-%m-%d %H:%M"), 1),
        Peep(2, 'Rescued a dragon from a tower today. Some days are just stranger than others.', datetime.strptime('2023-05-22 15:48', "%Y-%m-%d %H:%M"), 2),
        Peep(3, 'Learnt a new spell today. Will help with my teleportation!', datetime.strptime('2023-05-21 15:48', "%Y-%m-%d %H:%M"), 1),
        Peep(4, 'Found a unicorn in my backyard. It’s gonna be a magical day!', datetime.strptime('2023-05-20 15:48', "%Y-%m-%d %H:%M"), 3),
        Peep(5, 'Tea party with the gnomes. You haven’t lived until you’ve tried gnome brew.', datetime.strptime('2023-05-19 15:48', "%Y-%m-%d %H:%M"), 2),
        Peep(6, 'Started a new project - mapping out the fairy forest. Wish me luck!', datetime.strptime('2023-05-18 15:48', "%Y-%m-%d %H:%M"), 3),
        Peep(7, 'Invisible for the whole day. The peace and quiet was bliss.', datetime.strptime('2023-05-17 15:48', "%Y-%m-%d %H:%M"), 1),
    ]
def test_create_peep(db_connection):
    db_connection.seed("seeds/peepers.sql")
    repository = PeepRepository(db_connection)
    now = datetime.now().replace(microsecond=0)
    repository.create(Peep(None, "eighth peep", datetime.strptime('23-05-2023 15:21:02', "%d-%m-%Y %H:%M:%S"), 3))
    peeps, usernames = repository.all()

    assert peeps == [
        Peep(8, "eighth peep", now, 3),
        Peep(2, "Rescued a dragon from a tower today. Some days are just stranger than others.", datetime.strptime('2023-05-22 15:48:00', "%Y-%m-%d %H:%M:%S"), 2),
        Peep(1, "Just conjured a potion that grants invisibility. Impressive, huh?", datetime.strptime('2023-05-22 15:48:00', "%Y-%m-%d %H:%M:%S"), 1),
        Peep(3, "Learnt a new spell today. Will help with my teleportation!", datetime.strptime('2023-05-21 15:48:00', "%Y-%m-%d %H:%M:%S"), 1),
        Peep(4, "Found a unicorn in my backyard. It’s gonna be a magical day!", datetime.strptime('2023-05-20 15:48:00', "%Y-%m-%d %H:%M:%S"), 3),
        Peep(5, "Tea party with the gnomes. You haven’t lived until you’ve tried gnome brew.", datetime.strptime('2023-05-19 15:48:00', "%Y-%m-%d %H:%M:%S"), 2),
        Peep(6, "Started a new project - mapping out the fairy forest. Wish me luck!", datetime.strptime('2023-05-18 15:48:00', "%Y-%m-%d %H:%M:%S"), 3),
        Peep(7, "Invisible for the whole day. The peace and quiet was bliss.", datetime.strptime('2023-05-17 15:48:00', "%Y-%m-%d %H:%M:%S"), 1),

    ]

# def test_delete_Peep(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
#     repository = PeepRepository(db_connection) # Create a new ArtistRepository
#     repository.delete(1) # Get all artists
#     # Assert on the results
#     result = repository.all()
#     assert result == [
#         Peep(2, 'Second Peep', 'This is my second Peep.', 5, 2)]


