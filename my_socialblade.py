import random
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
        password_chars.extend(secrets.choice(all_characters) for _ in range(length - 4))
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)
from seleniumbase import SB

with SB(uc=True, test=True, ad_block=True, pls="none") as sb:
    url = "https://kick.com/browse"
    sb.activate_cdp_mode(url)
    rnd = random.randint(4,7)
    sb.sleep(rnd)
    sb.uc_gui_click_captcha()
    try:
        sb.cdp.mouse_click('button:contains("Accept")')
    except:
        print()
    while not sb.is_element_present('button:contains("Sign Up")'):
        sb.uc_gui_click_captcha()
        rnd = random.randint(10,30)
        sb.sleep(rnd)
        kkk +=1
        if kkk == 5:
            break
    
    
