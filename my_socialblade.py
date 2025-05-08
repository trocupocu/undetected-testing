import random
import string
import secrets
import datetime
import os
import re
from seleniumbase import SB
from sbvirtualdisplay import Display
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

def insert_cookie(cookie_value):
    """
    Connects to the 'trocu' database and inserts a new document into the 'cookiesk' collection.
    The document contains:
    - 'cookies': the provided cookie_value.
    - 'is_locked': set to False by default.
    
    Returns the inserted document's ID or None if an error occurs.
    """
    MONGO_URI = os.getenv("MONGO_URI")
    try:
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["trocu"]
        collection = db["cookiesk"]
        # Build the document to insert
        new_doc = {
            "cookies": cookie_value,
            "is_locked": False
        }
        # Insert the document
        result = collection.insert_one(new_doc)
        return result.inserted_id
    except Exception as e:
        return None
    finally:
        client.close()

def subtract_years(date, years):
    try:
        return date.replace(year=date.year - years)
    except ValueError:
        # Handles the case for February 29th in non-leap years
        return date.replace(month=2, day=28, year=date.year - years)


def generate_gamer_username():
    # Expanded lists of cool adjectives and nouns.
    adjectives = [
        "Swift", "Silent", "Fierce", "Mystic", "Shadow",
        "Epic", "Wild", "Cosmic", "Vicious", "Stealthy",
        "Mighty", "Hyper", "Electric", "Galactic", "Neon",
        "Infernal", "Infinite", "Blazing", "Thunder", "Luminous",
        "Phantom", "Obsidian", "Savage", "Raging", "Metal",
        "Epic", "Legendary",
        "Mythic", "Vivid", "Radiant", "Stellar", "Cosmic",
        "Mysterious", "Infinite", "Dynamic", "Electric", "Astro",
        "Galactic", "Neon",
        "Futuristic", "Retro", "Crimson", "Sapphire", "Emerald",
        "Cobalt", "Amber",
        "Golden", "Shadow", "Phantom", "Silent", "Vortex",
        "Frozen", "Sonic", "Ultra",
        "Blazing", "Lunar", "Solar", "Obsidian", "Celestial",
        "Brave", "Bold", "Wild",
        "Enchanted", "Majestic", "Eternal", "Gravity",
        "Virtuous", "Mystic", "Arcane",
        "Vibrant", "Mercurial", "Primal", "Savage",
        "Rogue", "Sleek", "Stealthy", "Fierce"
    ]
    nouns = [
        "Warrior", "Ninja", "Ranger", "Samurai", "Archer",
        "Viking", "Slayer", "Hunter", "Assassin", "Gladiator",
        "Dragon", "Phoenix", "Reaper", "Knight", "Vortex",
        "Storm", "Surge", "Maestro", "Specter", "Maverick",
        "Titan", "Nebula", "Cyclone", "Bolt", "Rebel",
        "Ninja", "Dragon",
        "Phoenix", "Viper", "Falcon", "Tiger", "Wolf", "Samurai",
        "Wizard", "Viking", "Knight", "Storm", "Raven",
        "Shadow", "Rebel", "Ghost",
        "Specter", "Titan", "Raider", "Champion", "Assassin",
        "Warrior", "Guardian",
        "Jester", "Sphinx", "Galaxy", "Comet", "Nebula", "Meteor",
        "Quantum", "Pixel",
        "Jolt", "Blitz", "Cyclone", "Stallion", "Ranger", "Rogue",
        "Maverick", "Pioneer",
        "Pirate", "Renegade", "Prophet", "Saber", "Cyborg",
        "Reaper", "Hurricane",
        "Thunder", "Serpent", "Vortex", "Rift", "Eclipse",
        "Rider", "Sonic"
    ]
    # Choose a random adjective and noun from the lists.
    chosen_adj = random.choice(adjectives)
    chosen_noun = random.choice(nouns)
    # Randomize the case for each chosen word.
    if random.choice([True, False]):
        randomized_adj = chosen_adj.upper()
    else:
        randomized_adj = chosen_adj.lower()
    if random.choice([True, False]):
        randomized_noun = chosen_noun.upper()
    else:
        randomized_noun = chosen_noun.lower()
    if random.choice([True, False]):
        if random.choice([True, False]):
            randomized_adj = random.randint(0, 9)
        else:
            randomized_noun = random.randint(0, 9)
    # Add a random two-digit number to the username.
    number = random.randint(0, 99)
    # Format the number with leading zeros for consistency.
    username1 = f"{randomized_adj}{randomized_noun}{number:02d}"
    if random.choice([True, False]):
        username = username1.upper()
    else:
        username = username1.lower()
    return username


def generate_random_birth_date():
    today = datetime.date.today()
    start_date = subtract_years(today, 70)  # 70 years ago
    end_date = subtract_years(today, 18)    # 18 years ago
    # Determine the total number of days between the start and end dates.
    days_between = (end_date - start_date).days
    # Pick a random number of days to add to the start date.
    random_days = random.randint(0, days_between)
    # Generate the random birth date.
    random_birth_date = start_date + datetime.timedelta(days=random_days)
    # Return the date as a string formatted as "MMDDYYYY"
    return random_birth_date.strftime("%m%d%Y")


def generate_strong_password(length=12):
    if length < 8:
        raise ValueError("")
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    password_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    if length > 4:
        all_characters = lower + upper + digits + punctuation
        password_chars.extend(secrets.choice(all_characters)
                              for _ in range(length - 4))
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)


with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
    url = "https://kick.com/browse"
    sb.activate_cdp_mode(url)
    rnd = random.randint(0, 7)
    sb.sleep(rnd)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.connect()
    sb.uc_gui_handle_captcha()
    sb.cdp.click('button:contains("Accept")')
    kkk = 0
    while not sb.cdp.find_element('button:contains("Sign Up")'):
        sb.uc_gui_click_captcha()
        sb.sleep(2)
        sb.uc_gui_handle_captcha()
        sb.save_screenshot("ssasa.png", folder='./latest_logs')
        rnd = random.randint(1, 10)
        sb.sleep(rnd)
        kkk += 1
        if kkk == 5:
            sb.save_screenshot("screenshot.png")
            break
    sb.uc_click('button:contains("Sign Up")', reconnect_time=4)
    driver2 = sb.get_new_driver(undetectable=True)
    sb.disconnect()
    driver2.connect()
    url = "https://mail.tm/en/"
    driver2.uc_open_with_reconnect(url)
    email_value = driver2.get_attribute("#Dont_use_WEB_use_API_OK", "value")
    kkk = 0
    while(len(str(email_value)) < 5):
        email_value = driver2.get_attribute("#Dont_use_WEB_use_API_OK", "value")
        sb.sleep(2)
        kkk += 1
        if kkk >= 5:
            break
    driver2.disconnect()
    sb.connect()
    # driver2.minimize_window()
    sb.switch_to_default_driver()
    # sb.connect()
    # sb.maximize_window()
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()
    sb.bring_active_window_to_front()
    xelem = sb.cdp.click('input[autocomplete="email"]')
    sb.uc_gui_press_keys(email_value)
    xelem = sb.cdp.click("input[name='username']")
    sb.uc_gui_press_keys(generate_gamer_username())
    rnd = random.randint(1, 5)
    sb.sleep(rnd)
    xelem = sb.cdp.click("input[name='birthdate']")
    sb.uc_gui_press_keys(generate_random_birth_date())
    rnd = random.randint(1, 5)
    sb.sleep(rnd)
    xelem = sb.cdp.click("input[name='password']")
    sb.uc_gui_press_keys(generate_strong_password())
    rnd = random.randint(1, 5)
    sb.sleep(rnd)
    if sb.is_element_present("p.text-danger-lower"):
        rnd = random.randint(5, 15)
        random_letter = random.choice(string.ascii_uppercase)
        xelem = sb.cdp.click("input[name='username']")
        sb.uc_gui_press_keys(f"{generate_gamer_username()}")
        sb.sleep(rnd)
    kkk = 0
    while not sb.is_element_present("input[name='code']"):
        xelem = sb.cdp.click('[data-test="sign-up-submit"]')
        rnd = random.randint(5, 15)
        sb.sleep(rnd)
        kkk += 1
        if kkk >= 5:
            break
    sb.save_screenshot("stackx.png", folder="./latest_logs")
    driver2.connect()
    sb.switch_to_driver(driver2)
    kkk = 0
    while not driver2.is_element_present("div[class*='hidden md:block']"):
        driver2.uc_open_with_reconnect("https://mail.tm/en/")
        rnd = random.randint(1, 9)
        driver2.sleep(rnd)
        driver2.refresh()
        driver2.sleep(rnd)
        kkk += 1
        if kkk >= 5:
            break
    sb.bring_active_window_to_front()
    # driver2.click("div.truncate")
    rnd = random.randint(2, 5)
    driver2.sleep(rnd)
    email_text = driver2.get_text("div[class*='hidden md:block']")
    print(email_text)
    sb.quit_extra_driver()
    sb.switch_to_default_driver()
    sb.bring_active_window_to_front()
    sb.click("input[name='code']")
    sb.uc_gui_press_keys(email_text)
    #sb.click("button[type='submit']")
    kkk = 0
    while not sb.is_element_visible("div[data-orientation='vertical']"):
        sb.hover('div[role="dialog"]')
        sb.sleep(5)
        kkk += 1
        if kkk >= 5:
            break
    # x1, y1 = sb.get_gui_element_center("div[data-orientation='vertical']")
    y_off = random.randint(0, 200)
    kkk = 0
    while not sb.is_element_enabled("button[type='submit']"):
        if sb.is_element_visible("div[data-orientation='vertical']"):
            y_off += random.randint(1, 20)
            try:
                sb.click_with_offset("div[data-orientation='vertical']", x = 0, y = y_off)
            except Exception as e:
                print(e)
        else:
            sb.hover('div[role="dialog"]')
        rnd = random.uniform(0, 2)
        sb.sleep(rnd)
        kkk += 1
        if kkk >= 50:
            break
    sb.click("button[type='submit']")
    rnd = random.randint(10, 15)
    sb.sleep(rnd)
    sb.click("//button[contains(text(), 'Get Started')]")
    rnd = random.randint(10, 15)
    sb.sleep(rnd)
    cookie_value = sb.execute_cdp_cmd('Storage.getCookies', cmd_args={})
    print(cookie_value)
    inserted_id = insert_cookie(cookie_value)
