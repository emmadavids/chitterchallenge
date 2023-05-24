-- Drop tables if they already exist
DROP TABLE IF EXISTS peeps CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    actualname text,
    username text,
    password text,
    email text
);


-- Create the peeps table
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    content text,
    time timestamp,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- Seed data for users
INSERT INTO users (actualname, username, password, email)
VALUES 
('Merlin', 'MysteriousMerlin', 'potion123', 'merlin@magic.com'),
('Fiona', 'FabulousFiona', 'dragon789', 'fiona@fantasy.com'),
('Dante', 'DynamicDante', 'spell456', 'dante@divine.com');


-- Seed data for peeps
INSERT INTO peeps (content, time, user_id)
VALUES 
('Just conjured a potion that grants invisibility. Impressive, huh?', '2023-05-22 15:48', 1),
('Rescued a dragon from a tower today. Some days are just stranger than others.', '2023-05-22 15:48', 2),
('Learnt a new spell today. Will help with my teleportation!', '2023-05-21 15:48', 1),
('Found a unicorn in my backyard. It’s gonna be a magical day!', '2023-05-20 15:48', 3),
('Tea party with the gnomes. You haven’t lived until you’ve tried gnome brew.', '2023-05-19 15:48', 2),
('Started a new project - mapping out the fairy forest. Wish me luck!', '2023-05-18 15:48', 3),
('Invisible for the whole day. The peace and quiet was bliss.', '2023-05-17 15:48', 1);