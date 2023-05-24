from playwright.sync_api import Page, expect
import time
import re


def test_get_peeps_formatted(page, test_web_address, db_connection):
    db_connection.seed("seeds/peepers.sql")
    page.goto(f'http://{test_web_address}/peeps')
    div_tags = page.locator("li").all()
    actual_texts = []
    for element in div_tags:
        text = element.inner_text()
        actual_texts.append(text)
    assert actual_texts == [
        "MysteriousMerlin peeped: Just conjured a potion that grants invisibility. Impressive, huh? at 2023-05-22 15:48:00",
        "FabulousFiona peeped: Rescued a dragon from a tower today. Some days are just stranger than others. at 2023-05-22 15:48:00",
        "MysteriousMerlin peeped: Learnt a new spell today. Will help with my teleportation! at 2023-05-21 15:48:00",
        "DynamicDante peeped: Found a unicorn in my backyard. It’s gonna be a magical day! at 2023-05-20 15:48:00",
        "FabulousFiona peeped: Tea party with the gnomes. You haven’t lived until you’ve tried gnome brew. at 2023-05-19 15:48:00",
        "DynamicDante peeped: Started a new project - mapping out the fairy forest. Wish me luck! at 2023-05-18 15:48:00",
        "MysteriousMerlin peeped: Invisible for the whole day. The peace and quiet was bliss. at 2023-05-17 15:48:00"
    ]


def test_get_all_users(db_connection, page, test_web_address):
    db_connection.seed("seeds/peepers.sql")
    page.goto(f"http://{test_web_address}/peeps")
    dropdown = page.locator(".user")
    dropdown_text = dropdown.inner_text().split('\n')
    dropdown_options = [line for line in dropdown_text if line.strip()]
    assert dropdown_options == ["MysteriousMerlin", "FabulousFiona", "DynamicDante"]  


def test_create_peep(db_connection, page, test_web_address):
    db_connection.seed("seeds/peepers.sql")
    page.goto(f"http://{test_web_address}/peeps")
    add = page.locator(".add")
    expect(add).to_have_text("Add a new peep")
    dropdown = page.locator(".user")
    dropdown.select_option("DynamicDante")
    page.fill("input[name='peep']", "eating watermelon with coffee")
    page.click("text=Click to Peep!")
    unordered_list = page.locator("ul")
    expect(unordered_list).to_contain_text("DynamicDante peeped: eating watermelon with coffee")


def test_create_new_user(db_connection, page, test_web_address):
    db_connection.seed("seeds/peepers.sql")
    page.goto(f'http://{test_web_address}/peeps')
    page.click("text=Sign up here")
    page.fill("input[name='actualname']", "Homer Simpson")
    page.fill("input[name='username']", "donutlover")
    page.fill("input[name='password']", "password123")
    page.fill("input[name='email']", "homer@springfield.com")
    page.click("text=Submit")
    # page.click("text=Dropdown")
    page.goto(f'http://{test_web_address}/peeps')
    dropdown = page.locator(".user")
    dropdown_text = dropdown.inner_text().split('\n')
    dropdown_options = [line for line in dropdown_text if line.strip()]
    assert "donutlover" in dropdown_options

def test_duplicate_username_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/peepers.sql")
    page.goto(f'http://{test_web_address}/peeps')
    page.click("text=Sign up here")
    page.fill("input[name='actualname']", "Homer Simpson")
    page.fill("input[name='username']", "DynamicDante")
    page.fill("input[name='password']", "password123")
    page.fill("input[name='email']", "homer@springfield.com")
    page.click("text=Submit")
    error = page.locator(".username-error")
    expect(error).to_have_text("Username already taken") 

def test_duplicate_email_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/peepers.sql")
    page.goto(f'http://{test_web_address}/peeps')
    page.click("text=Sign up here")
    page.fill("input[name='actualname']", "Homer Simpson")
    page.fill("input[name='username']", "DynamicDante")
    page.fill("input[name='password']", "password123")
    page.fill("input[name='email']", "merlin@magic.com")
    page.click("text=Submit")
    error = page.locator(".email-error")
    expect(error).to_have_text("An account with this email already exists") 

