import random
import string
import secrets
import datetime
import os
import re
from seleniumbase import SB
from sbvirtualdisplay import Display


MONGO_URI = os.getenv("MONGO_URI")


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
    username = username1.upper() if random.choice([True, False]) else username1.lower()
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


display = Display(visible=0, size=(1440, 1880))
display.start()
with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
    url = "https://kick.com/browse"
    sb.uc_open_with_reconnect(url, 5)
    rnd = random.randint(0, 7)
    sb.sleep(rnd)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()
    try:
        sb.uc_click('button:contains("Accept")', reconnect_time=4)
    except Exception as e:
        print(e)
    kkk = 0
    while not sb.is_element_present('button:contains("Sign Up")'):
        sb.uc_gui_click_captcha()
        sb.sleep(2)
        sb.uc_gui_handle_captcha()
        sb.cdp.save_screenshot("ssasa.png", folder='./latest_logs')
        rnd = random.randint(1, 10)
        sb.sleep(rnd)
        kkk += 1
        if kkk == 5:
            sb.cdp.save_screenshot("screenshot.png")
            break
    sb.uc_click('button:contains("Sign Up")', reconnect_time=4)
    driver2 = sb.get_new_driver(undetectable=True)
    url = "https://mail.tm/en/"
    driver2.uc_open_with_reconnect(url)
    email_value = driver2.get_attribute("#Dont_use_WEB_use_API_OK", "value")
    sb.uc_gui_press_keys("input[name='email']", email_value)
    sb.uc_gui_press_keys("input[name='username']", generate_gamer_username())
    rnd = random.randint(1, 5)
    sb.sleep(rnd)
    sb.uc_gui_press_keys("input[name='birthdate']",
                         generate_random_birth_date())
    rnd = random.randint(1, 5)
    sb.sleep(rnd)
    sb.uc_gui_press_keys("input[name='password']",
                         generate_strong_password())
    rnd = random.randint(1, 5)
    sb.sleep(rnd)
    if sb.is_element_present("p.text-danger-lower"):
        rnd = random.randint(5, 15)
        random_letter = random.choice(string.ascii_uppercase)
        sb.uc_gui_press_keys("input[name='username']",
                             f"{generate_gamer_username()}")
        sb.sleep(rnd)
    kkk = 0
    while not sb.is_element_present("input[name='code']"):
        sb.uc_click('[data-test="sign-up-submit"]')
        rnd = random.randint(1, 17)
        sb.sleep(rnd)
        kkk += 1
        if kkk >= 5:
            break
    driver2.refresh()
    kkk = 0
    while not driver2.is_element_present("div.truncate"):
        driver2.uc_open_with_reconnect("https://mail.tm/en/")
        rnd = random.randint(1, 9)
        driver2.sleep(rnd)
        driver2.refresh()
        driver2.sleep(rnd)
        kkk += 1
        if kkk >= 10:
            break
    driver2.uc_click("div.truncate")
    rnd = random.randint(2, 5)
    driver2.sleep(rnd)
    email_text = driver2.get_text("h2[class*='text-2xl']")
    sb.quit_extra_driver()
    match = re.search(r"(\d{6})\s*-\s*Sign Up Verification Code", email_text)
    if match:
        verification_code = match.group(1)
    sb.uc_gui_press_keys("input[name='code']", verification_code)
    sb.uc_click("button[type='submit']")
display.stop()
