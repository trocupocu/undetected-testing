import random
import string
import secrets
import datetime
import os
from seleniumbase import SB
from sbvirtualdisplay import Display


MONGO_URI = os.getenv("MONGO_URI")


def subtract_years(date, years):
    try:
        return date.replace(year=date.year - years)
    except ValueError:
        # Handles the case for February 29th in non-leap years
        return date.replace(month=2, day=28, year=date.year - years)


def generate_random_birth_date(self):
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
    sb.activate_cdp_mode(
        url,
        platform='Win32',
        user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/135.0.0.0 Safari/537.36")
    )
    rnd = random.randint(4, 7)
    sb.sleep(rnd)
    sb.uc_gui_click_captcha()
    try:
        sb.cdp.mouse_click('button:contains("Accept")')
    except Exception as e:
        print(e)
    kkk = 0
    while not sb.is_element_present('button:contains("Sign Up")'):
        sb.uc_gui_click_captcha()
        rnd = random.randint(1, 10)
        sb.sleep(rnd)
        kkk += 1
        if kkk == 5:
            sb.cdp.save_screenshot("screenshot.png")
            break
display.stop()
