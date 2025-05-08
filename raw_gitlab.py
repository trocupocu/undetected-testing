import urllib.parse
import string
import secrets
import logging
import datetime
from sbvirtualdisplay import Display


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def process_cookie_file(file_path):
    """
    Reads the cookie file, which may originally be structured like:
    {"cookies": [ { ... }, { ... } ]}
    This function converts it into a list of cookie dicts and also removes
    any leading dots from the domain names.
    """
    # Read the file content as JSON.
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # If the JSON object is wrapped with a "cookies" key, unpack it.
    cookies = data.get("cookies", data)
    
    # Clean up each cookie by removing a leading dot from the domain if present.
    for cookie in cookies:
        domain = cookie.get("domain")
        if domain and domain.startswith("."):
            cookie["domain"] = domain.lstrip(".")
    
    return cookies


from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.webdriver.common.action_chains import ActionChains





import re
import time
import os
import random 
import json
from pymongo import MongoClient
from selenium.webdriver.common.keys import Keys
import types
import sys

import logging




api_url = "http://18.171.168.179:20017/generate"
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
cookie_file1 = os.path.join(documents_path, "cookies1.txt")
cookie_file1 = os.path.abspath(cookie_file1)
cookie_file = os.path.join(documents_path, "cookieskick")
cookie_file = os.path.abspath(cookie_file)
current_folder = os.getcwd()
saved_cookies_folder = os.path.join(current_folder, "saved_cookies")
output_filename = "processed_cookies.txt"
try:
    processed_cookie_file = process_and_save_cookie_file(cookie_file, saved_cookies_folder, output_filename)
except:
    processed_cookie_file = ""
cookie_file = os.path.join(saved_cookies_folder,processed_cookie_file)
chatter = 0
from seleniumbase.core.sb_cdp import CDPMethods
def slower_gui_drag_and_drop(self, drag_selector, drop_selector, timeframe=0.35):
    rnd = random.randint(1,3)
    time.sleep(rnd)
    self._CDPMethods__slow_mode_pause_if_set()  # call the mangled method from the original class
    self.bring_active_window_to_front()
    rnd = random.randint(1,10)
    time.sleep(rnd)
    x1, y1 = self.get_gui_element_center(drag_selector)
    rnd = random.randint(1,5)
    time.sleep(rnd)
    #element = self.find_element(drop_selector, timeout=timeout)
    #element.scroll_into_view()
    self._CDPMethods__add_light_pause()

    #time.sleep(10)
    x2, y2 = self.get_gui_element_center(drop_selector)
    #time.sleep(10)
    self._CDPMethods__add_light_pause()
    rnd = random.randint(1,5)
    time.sleep(rnd)
    self.gui_drag_drop_points(x1, y1, x2, y2, timeframe=timeframe)
    #time.sleep(10)



MONGO_URI = os.getenv("MONGO_URI")
def retrieve_and_lock_random_cookie():
    """
    Connects to the 'trocu' database and retrieves one random document from the
    'cookiesk' collection where is_locked is False. Once a document is found,
    it prints the 'cookies' field and updates the document by setting is_locked
    to True along with a locked_at timestamp.
    
    Returns the value of the 'cookies' field if successful, or None if no
    unlocked document is available or an error occurs.
    """
    try:
        # Connect to MongoDB using MongoClient with your MONGO_URI.
        client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
        db = client["trocu"]
        collection = db["cookiesk"]

        # Build an aggregation pipeline to randomly sample one unlocked document.
        pipeline = [
            {"$match": {"is_locked": False}},
            {"$sample": {"size": 1}}
        ]
        docs = list(collection.aggregate(pipeline))
        if not docs:
            logging.info("No unlocked cookie document available.")
            return None
        
        doc = docs[0]
        cookie_value = doc.get("cookies")
        logging.info("Retrieved cookie: %s", cookie_value)

        # Lock the document by setting is_locked to True and adding the locked_at timestamp.
        update_result = collection.update_one(
            {"_id": doc["_id"], "is_locked": False},  # Ensure the document is still unlocked.
            {"$set": {"is_locked": True, "locked_at": datetime.utcnow()}}
        )

        if update_result.modified_count:
            logging.info("Cookie document locked successfully.")
        else:
            logging.info("The document was already locked by someone else.")

        return cookie_value

    except Exception as e:
        logging.error("Error retrieving and locking cookie: %s", e)
        return None

    finally:
        client.close()


#cookie = retrieve_and_lock_random_cookie()

#,proxy="socks5://127.0.0.1:9052"
from seleniumbase import BaseCase
import pyautogui
CDPMethods.gui_drag_and_drop = slower_gui_drag_and_drop
BaseCase.main(__name__, __file__)
display = Display(visible=0, size=(1440, 1880))
display.start()
class MyTestClass(BaseCase):

    def generate_gamer_username(self):
        # Expanded lists of cool adjectives and nouns.
        adjectives = [
            "Swift", "Silent", "Fierce", "Mystic", "Shadow",
            "Epic", "Wild", "Cosmic", "Vicious", "Stealthy",
            "Mighty", "Hyper", "Electric", "Galactic", "Neon",
            "Infernal", "Infinite", "Blazing", "Thunder", "Luminous",
            "Phantom", "Obsidian", "Savage", "Raging", "Metal","Epic", "Legendary", "Mythic", "Vivid", "Radiant", "Stellar", "Cosmic",
            "Mysterious", "Infinite", "Dynamic", "Electric", "Astro", "Galactic", "Neon",
            "Futuristic", "Retro", "Crimson", "Sapphire", "Emerald", "Cobalt", "Amber",
            "Golden", "Shadow", "Phantom", "Silent", "Vortex", "Frozen", "Sonic", "Ultra",
            "Blazing", "Lunar", "Solar", "Obsidian", "Celestial", "Brave", "Bold", "Wild",
            "Enchanted", "Majestic", "Eternal", "Gravity", "Virtuous", "Mystic", "Arcane",
            "Vibrant", "Mercurial", "Primal", "Savage", "Rogue", "Sleek", "Stealthy", "Fierce"
        ]
        
        nouns = [
            "Warrior", "Ninja", "Ranger", "Samurai", "Archer",
            "Viking", "Slayer", "Hunter", "Assassin", "Gladiator",
            "Dragon", "Phoenix", "Reaper", "Knight", "Vortex",
            "Storm", "Surge", "Maestro", "Specter", "Maverick",
            "Titan", "Nebula", "Cyclone", "Bolt", "Rebel",    "Ninja", "Dragon", "Phoenix", "Viper", "Falcon", "Tiger", "Wolf", "Samurai",
            "Wizard", "Viking", "Knight", "Storm", "Raven", "Shadow", "Rebel", "Ghost",
            "Specter", "Titan", "Raider", "Champion", "Assassin", "Warrior", "Guardian",
            "Jester", "Sphinx", "Galaxy", "Comet", "Nebula", "Meteor", "Quantum", "Pixel",
            "Jolt", "Blitz", "Cyclone", "Stallion", "Ranger", "Rogue", "Maverick", "Pioneer",
            "Pirate", "Renegade", "Prophet", "Saber", "Cyborg", "Reaper", "Hurricane",
            "Thunder", "Serpent", "Vortex", "Rift", "Eclipse", "Rider", "Sonic"
        ]
        
        # Choose a random adjective and noun from the lists.
        chosen_adj = random.choice(adjectives)
        chosen_noun = random.choice(nouns)
        
        # Randomize the case for each chosen word.
        randomized_adj = chosen_adj.upper() if random.choice([True, False]) else chosen_adj.lower()
        randomized_noun = chosen_noun.upper() if random.choice([True, False]) else chosen_noun.lower()
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
    def third_mail(self):
        self.sleep(5)
        url = "https://smailpro.com/"
        self.cdp.open("https://smailpro.com/")
        rnd = random.randint(5,10)
        self.sleep(rnd)

        email_value = self.get_text("div[x-text='getTemporaryEmailAddress()']")
        rnd = random.randint(1,5)
        self.sleep(rnd)
        print(email_value)
        try:
            self.cdp.click('button:contains("Consent")')
        except:
            print()
        self.switch_to_window(0)
        rnd = random.randint(1,5)
        self.sleep(rnd)

        self.cdp.press_keys("input[name='email']", email_value)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='username']", self.generate_gamer_username())
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.type("input[name='birthdate']", self.generate_random_birth_date())
        rnd = random.randint(5,10)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='password']", self.generate_strong_password())
        rnd = random.randint(1,5)
        self.sleep(rnd)

        if self.is_element_present("p.text-danger-lower"):
            rnd = random.randint(5,15)
            random_letter = random.choice(string.ascii_uppercase)
            clearname = self.cdp.find_element("input[name='username']")
            clearname.clear_input()

            self.cdp.type("input[name='username']", f"{self.generate_gamer_username()}")
            self.sleep(rnd)
        kkk = 0
        while not self.is_element_present("input[name='code']"):
            #self.cdp.gui_hover_and_click('[data-test="sign-up-submit"]', '[data-test="sign-up-submit"]')
            self.cdp.scroll_into_view('[data-test="sign-up-submit"]')
            self.cdp.mouse_click('[data-test="sign-up-submit"]')
            rnd = random.randint(12,17)
            self.sleep(rnd)
            kkk +=1
            if kkk >= 5:
                break
        self.switch_to_window(1)
        
        url = "https://smailpro.com/"
        rnd = random.randint(1,5)
        self.cdp.open(url)
        self.sleep(rnd)
        self.cdp.refresh()
        self.sleep(rnd)
        # Retrieve the text inside the <div>.
        kkk = 0
        while not self.is_element_present("span[x-text='mes.textSubject']"):
            self.cdp.open("https://smailpro.com/")
            rnd = random.randint(5,9)
            print(kkk)
            self.sleep(rnd)
            self.cdp.click("#refresh")
            self.sleep(rnd)
            kkk +=1
            if kkk >= 10:
                self.save_screenshot("stack2.png")
                break
        #self.cdp.mouse_click("div.truncate")
        rnd = random.randint(2,5)
        self.sleep(rnd)
        email_text = self.get_text("span[x-text='mes.textSubject']")
        print(email_text)
        return email_text
    def insert_cookie(self,cookie_value):
        """
        Connects to the 'trocu' database and inserts a new document into the 'cookiesk' collection.
        The document contains:
        - 'cookies': the provided cookie_value.
        - 'is_locked': set to False by default.
        
        Returns the inserted document's ID or None if an error occurs.
        """
        MONGO_URI = "mongodb+srv://trocupocu:BE5fESTFMj0TdO2Q@chatdata.rmtsfd5.mongodb.net/?retryWrites=true&w=majority&appName=chatdata"
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
            logging.info("Inserted cookie document with id: %s", result.inserted_id)
            return result.inserted_id

        except Exception as e:
            logging.error("Error inserting cookie: %s", e)
            return None
        finally:
            client.close()

    def secondary_mail(self):
        self.sleep(5)
        url = "https://mail.tm/en/"
        self.cdp.open("https://mail.tm/en/")
        rnd = random.randint(8,15)
        self.sleep(rnd)

        email_value = self.get_attribute("#Dont_use_WEB_use_API_OK", "value")
        rnd = random.randint(1,5)
        self.sleep(rnd)
        print(email_value)
        try:
            self.cdp.click("Accept")
        except:
            print()
        self.switch_to_window(0)
        rnd = random.randint(1,5)
        self.sleep(rnd)

        self.cdp.press_keys("input[name='email']", email_value)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='username']", self.generate_gamer_username())
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.type("input[name='birthdate']", self.generate_random_birth_date())
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='password']", self.generate_strong_password())
        rnd = random.randint(1,5)
        self.sleep(rnd)

        if self.is_element_present("p.text-danger-lower"):
            rnd = random.randint(5,15)
            random_letter = random.choice(string.ascii_uppercase)
            clearname = self.cdp.find_element("input[name='username']")
            clearname.clear_input()
            self.cdp.type("input[name='username']", f"{self.generate_gamer_username()}")
            self.sleep(rnd)
        kkk = 0
        while not self.is_element_present("input[name='code']"):
            #self.cdp.gui_hover_and_click('[data-test="sign-up-submit"]', '[data-test="sign-up-submit"]')
            self.cdp.scroll_into_view('[data-test="sign-up-submit"]')
            self.cdp.mouse_click('[data-test="sign-up-submit"]')
            rnd = random.randint(12,17)
            self.sleep(rnd)
            kkk +=1
            if kkk >= 5:
                break
        self.switch_to_window(1)
        url = "https://mail.tm/en/"
        self.cdp.open(url)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.refresh()
        rnd = random.randint(1,5)
        self.sleep(rnd)
        # Retrieve the text inside the <div>.
        kkk = 0
        while not self.is_element_present("div.truncate"):
            self.cdp.open("https://mail.tm/en/")
            rnd = random.randint(5,9)
            print(kkk)
            
            self.sleep(rnd)
            self.cdp.refresh()
            self.sleep(rnd)
            kkk +=1
            if kkk >= 10:
                self.save_screenshot("stack1.png")
                break
        self.cdp.click("div.truncate")
        rnd = random.randint(2,5)
        self.sleep(rnd)
        email_text = self.get_text("h2[class*='text-2xl']")
        print(email_text)
        return email_text
    def mail_create1(self):
        self.cdp.open("https://www.emailfake.com")
        #tab_handle = self.current_window_handle
        rnd = random.randint(1,5)
        self.sleep(rnd)
        try:
            self.cdp.mouse_click('button:contains("Consent")')
        except:
            print()
        raw_text = self.get_text("#checkdomainset")
        match = re.search(r'\d+', raw_text)
        if match:
            number_value = int(match.group())  # Convert the extracted string to an integer
            print("Extracted number:", number_value)
        else:
            print("No number found in the element's text.")
        if number_value>120:
            self.cdp.mouse_click("div.e7m.dropselect")
            self.wait_for_element_visible("#newselect")
            
            # Locate all dropdown option elements.
            options = self.find_elements("#newselect div.tt-suggestion p")
            
            threshold = 120
            for idx, option in enumerate(options):
                option.click()
                self.sleep(3)  # Wait for page update
                
                self.wait_for_element("#checkdomainset")
                raw_text = self.get_text("#checkdomainset")
                print(f"Option {idx+1} raw text: {raw_text}")
                
                match = re.search(r'\d+', raw_text)
                if match:
                    number_value = int(match.group())
                    print(f"Extracted number: {number_value}")
                    
                    if number_value > threshold:
                        print(f"Number {number_value} is higher than {threshold}. Moving to next option.")
                        # Re-open the dropdown if it gets closed after the click.
                        self.cdp.mouse_click("div.e7m.dropselect")
                        self.wait_for_element_visible("#newselect")
                        continue
                    else:
                        print(f"Option accepted with number {number_value}.")
                        break
                else:
                    print("No number found in the text.")
                    self.cdp.mouse_click("div.e7m.dropselect")
                    self.wait_for_element_visible("#newselect")

        name = self.get_attribute("#userName", "value")
        print(name)
        email = self.get_text("#email_ch_text")
        print(email)
        self.switch_to_window(0)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='email']", email)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='username']", name)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.type("input[name='birthdate']", self.generate_random_birth_date())
        rnd = random.randint(5,10)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='password']", self.generate_strong_password())
        rnd = random.randint(1,5)
        self.sleep(rnd)
        if self.is_element_present("p.text-danger-lower"):
            rnd = random.randint(5,15)
            random_letter = random.choice(string.ascii_uppercase)
            clearname = self.cdp.find_element("input[name='username']")
            clearname.clear_input()
            self.cdp.type("input[name='username']", f"{self.generate_gamer_username()}")
            self.sleep(rnd)
        kkk = 0
        while not self.is_element_present("input[name='code']"):
            #self.cdp.gui_hover_and_click('[data-test="sign-up-submit"]', '[data-test="sign-up-submit"]')
            self.cdp.scroll_into_view('[data-test="sign-up-submit"]')
            self.cdp.mouse_click('[data-test="sign-up-submit"]')
            self.sleep(1)
            self.save_screenshot("stack4.png")
            rnd = random.randint(12,17)
            self.sleep(rnd)
            kkk +=1
            if kkk >= 5:
                break
        
        #self.cdp.mouse_click('[data-test="sign-up-submit"]')
        rnd = random.randint(1,15)
        self.sleep(rnd)
        self.switch_to_window(1)
        self.sleep(3)
        self.cdp.open("https://www.emailfake.com")
        self.sleep(3)
        kkk = 0
        email_text = ""
        while not self.is_element_present("#email-table"):
            self.cdp.open("https://www.emailfake.com")
            rnd = random.randint(5,9)
            print(kkk)
            self.sleep(rnd)
            self.cdp.refresh()
            self.sleep(rnd)
            kkk +=1
            if kkk >= 4:
                self.save_screenshot("stack3.png")
                return email_text
        email_text = self.get_text("#email-table")
        return email_text
        

    def secondary_mail1(self):
        self.sleep(5)
        url = "https://tempmailo.com/"
        self.cdp.open(url)
        kkk = 0
        while not self.is_element_present("#i-email"):
            kkk +=1
            self.uc_gui_click_captcha()
            self.sleep(25)
            if kkk >= 4:
                break
            kkk +=1
        raw_text = self.get_text("#i-email")
        self.switch_to_window(0)
        rnd = random.randint(1,5)
        self.sleep(rnd)

        self.cdp.press_keys("input[name='email']", raw_text)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='username']", self.generate_gamer_username())
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.type("input[name='birthdate']", self.generate_random_birth_date())
        rnd = random.randint(5,10)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='password']", self.generate_strong_password())
        rnd = random.randint(1,5)
        self.sleep(rnd)

        if self.is_element_present("p.text-danger-lower"):
            rnd = random.randint(5,15)
            random_letter = random.choice(string.ascii_uppercase)
            clearname = self.cdp.find_element("input[name='username']")
            clearname.clear_input()

            self.cdp.type("input[name='username']", f"{self.generate_gamer_username()}")
            self.sleep(rnd)
        kkk = 0
        while not self.is_element_present("input[name='code']"):
            #self.cdp.gui_hover_and_click('[data-test="sign-up-submit"]', '[data-test="sign-up-submit"]')
            self.cdp.scroll_into_view('[data-test="sign-up-submit"]')
            self.cdp.mouse_click('[data-test="sign-up-submit"]')
            rnd = random.randint(12,17)
            self.sleep(rnd)
            kkk +=1
            if kkk >= 5:
                break
        self.switch_to_window(1)
        self.sleep(5)
        kkk = 0
        while not self.is_element_present("div.mail-item-sub"):
            self.cdp.open("https://tempmailo.com/")
            rnd = random.randint(5,9)
            print(kkk)
            
            self.sleep(rnd)
            self.cdp.refresh()
            self.sleep(rnd)
            kkk +=1
            if kkk >= 10:
                self.save_screenshot("stack1.png")
                break

        email_text = self.get_text("div.mail-item-sub")
        print(email_text)
        return email_text

    def click_on_accept_button(self):
        # Click on the dialog to ensure it's active.
        self.sleep(5)
        kkk = 0
        self.cdp.mouse_click("button[type='submit']")
        while not self.is_element_enabled("button[type='submit']"):
            #self.cdp.gui_hover_and_click('div[role="dialog"]','div[role="dialog"]')
            if self.is_element_visible("div[data-orientation='vertical']"):
                rnd = random.randint(1,10)
                self.cdp.gui_drag_and_drop("div[data-orientation='vertical']", "button[type='submit']", timeframe=rnd)
            else:
                self.cdp.mouse_click('div[role="dialog"]')
            #self.cdp.mouse_click('div[role="dialog"]')
            #self.cdp.mouse_click('div[role="dialog"]')
            rnd = random.randint(1,5)
            self.sleep(rnd)
            kkk+=1
            if kkk >= 10 :
                break
        #self.sleep(5)
        rnd = random.randint(1,7)
        self.sleep(rnd)
        #self.cdp.gui_drag_and_drop("div[data-orientation='vertical']", "//button[contains(., 'I accept')]", timeframe=rnd)
        '''bara = self.cdp.find_element("div[data-orientation='vertical']")
        posbara = bara.get_position()
        #self.hover("div[data-orientation='vertical']")
        #self.cdp.mouse_click("div[data-orientation='vertical']")
        self.sleep(2)
        y_off=100
        while not self.is_element_enabled("//button[contains(., 'I accept')]"):
            y_off +=15
            finaly = posbara.y+y_off
            self.cdp.gui_click_x_y(posbara.x,finaly)
            #self.click_with_offset("div[data-orientation='vertical']",x=0,y=y_off)'''
        #self.sleep(2)
        self.cdp.mouse_click("button[type='submit']")
        #self.cdp.gui_hover_and_click("//button[contains(., 'I accept')]","//button[contains(., 'I accept')]")

    def create_acc(self):
        #self.cdp.mouse_click('button:contains("Sign Up")')
        kkk = 0
        while not self.is_element_present("input[name='email']"):
            #self.cdp.gui_hover_and_click('button:contains("Sign Up")', 'button:contains("Sign Up")')
            if self.is_element_visible("body nav button:nth-of-type(3)"):
                self.cdp.mouse_click("body nav button:nth-of-type(3)")
            self.cdp.mouse_click('button:contains("Sign Up")')
            rnd = random.randint(12,17)
            self.sleep(rnd)
            kkk +=1
            if kkk >= 5:
                self.save_screenshot("stackx.png")
                break
        self.open_new_tab(switch_to=True)


        rnd = random.randint(1,3)
        if rnd ==1:
            email_text = self.third_mail()
        elif rnd ==2:
            email_text = self.secondary_mail()
        elif rnd ==3:
            email_text = self.mail_create1()
        else:
            email_text = self.secondary_mail1()
        # Use a regex pattern to find 6 digits followed by " - Sign Up Verification Code"
        match = re.search(r"(\d{6})\s*-\s*Sign Up Verification Code", email_text)

        if match:
            verification_code = match.group(1)
            print("Verification code:", verification_code)
            # You can now use the variable 'verification_code' as needed.
            self.cdp.open("https://duckduckgo.com/")
        else:
            print()
        self.switch_to_window(0)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.cdp.press_keys("input[name='code']", verification_code)
        rnd = random.randint(1,5)
        self.sleep(rnd)
        self.click_on_accept_button()
        kkk = 0
        while not self.is_element_present("//button[contains(text(), 'Get Started')]"):
            #self.cdp.gui_hover_and_click("//button[contains(., 'I accept')]","//button[contains(., 'I accept')]")
            self.cdp.mouse_click("//button[contains(., 'I accept')]")
            rnd = random.randint(10,15)
            self.sleep(rnd)
            kkk+=1
            if kkk >= 5:
                break
        self.cdp.mouse_click("//button[contains(text(), 'Get Started')]")     
        #self.cdp.gui_hover_and_click("//button[contains(text(), 'Get Started')]","//button[contains(text(), 'Get Started')]")
        rnd = random.randint(1,5)
        self.sleep(rnd)

    def generate_random_birth_date(self):
        today = datetime.date.today()
        
        # Helper function to subtract years while handling leap year issues.
        def subtract_years(date, years):
            try:
                return date.replace(year=date.year - years)
            except ValueError:
                # Handles the case for February 29th in non-leap years
                return date.replace(month=2, day=28, year=date.year - years)
        
        # Calculate the start and end dates for the valid birth date range.
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

    def generate_strong_password(self,length=12):
        """
        Generate a cryptographically secure random strong password.

        The password will have at least one lowercase letter, one uppercase letter,
        one digit, and one special character (punctuation). The overall length of the
        password must be a minimum of 8 characters.
        """
        if length < 8:
            raise ValueError("Password length should be at least 8 characters")

        # Define character pools for each category
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        punctuation = string.punctuation

        # Ensure the inclusion of at least one character from each required category
        password_chars = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
            secrets.choice(punctuation)
        ]

        # Fill the rest of the password length with a mix of all characters
        if length > 4:
            all_characters = lower + upper + digits + punctuation
            password_chars.extend(secrets.choice(all_characters) for _ in range(length - 4))

        # Shuffle the result to eliminate any predictable patterns
        secrets.SystemRandom().shuffle(password_chars)
        return ''.join(password_chars)
    def retrieve_and_delete_first_chat_entry(self):
        """
        Connects to the MongoDB Atlas collection 'chat', retrieves the first document (sorted by _id)
        by extracting the 'chattext' field, and then deletes that document.
        
        Returns:
            The value of 'chattext' from the retrieved document, or None if no document is found.
        """
        MONGO_URI = os.getenv("MONGO_URI")
        try:
            client = MongoClient(MONGO_URI,tls=True,tlsAllowInvalidCertificates=True)
            db = client["trocu"]
            collection = db["chat"]

            # Retrieve and delete the earliest inserted document.
            # Sorting with _id (which is an ObjectId) in ascending order typically gives you
            # the oldest (or first) inserted document.
            doc = collection.find_one_and_delete({},sort=[('_id', 1)])
            
            if not doc:
                logging.info("No chat entries found in the collection.")
                return None

            chattext = doc.get("chattext")
            logging.info("Retrieved and deleted chat entry with chattext: %s", chattext)
            return chattext

        except Exception as e:
            logging.error("Error retrieving and deleting chat entry: %s", e)
            return None
        finally:
            client.close()

    def get_generated_message(url, prompt):
        """
        Send a prompt to the given URL and return the generated message.
        
        Args:
            url (str): The API endpoint URL.
            prompt (str): The prompt to send.
        
        Returns:
            str or None: The generated message from the 'generated_message' key if successful,
                        otherwise None in case of a timeout, error, or empty response.
        """
        prompt = str(prompt)
        payload = {"prompt": prompt}
        print(prompt)
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            print(data)
            generated_message = data.get("generated_message", "").strip()
            if not generated_message:
                return None
            print(generated_message)
            return generated_message
            
        except requests.Timeout:
            # The request timed out after 10 seconds.
            print("Request timed out after 10 seconds.")
            return None
        except requests.RequestException as e:
            # Catch any other request exceptions.
            print("An error occurred:", e)
            return None

    def test_full_account_creation_flow(self):
        if True:
            url = "https://kick.com/browse"
            self.activate_cdp_mode(url)
            
            #self.cdp.maximize()
            #####self.maximize()
            
            #self.set_window_size(640, 480)
            rnd = random.randint(4,7)
            self.sleep(rnd)
            self.uc_gui_click_captcha()
            self.sleep(2)
            self.connect()
            self.uc_gui_handle_captcha()
            self.cdp.save_screenshot("ssasa.png", folder='./latest_logs')
            #self.cdp.maximize()
            #original_handle = self.current_window_handle
            rnd = random.randint(1,4)
            self.sleep(rnd)

            rnd = random.randint(1,4)
            self.sleep(rnd)

            #self.slower_gui_drag_and_drop('button:contains("Accept")', 'button:contains("Accept")', timeframe=1)
            try:
                self.cdp.mouse_click('button:contains("Accept")')
            except:
                print()
            rnd = random.randint(2,10)
            self.sleep(rnd)
            chatter = 0
            kkk = 0
            while not self.is_element_present('button:contains("Sign Up")'):
                self.uc_gui_click_captcha()
                #self.set_window_size(640, 480)
                rnd = random.randint(10,30)
                self.sleep(rnd)
                kkk +=1
                if kkk == 5:
                    break
            #try:
            rnd = random.randint(10,10)
            if (rnd == 10):
                self.create_acc()
                chatter = 1
                cookie_value = self.execute_cdp_cmd('Storage.getCookies', cmd_args={})
                print(cookie_value)
                inserted_id = self.insert_cookie(cookie_value)
            '''            #except Exception as e:
            #    print(e)
            #    self.switch_to_window(0) 

            url = "https://kick.com/brutalles"
            self.cdp.open(url)
            rnd = random.randint(2,10)
            self.sleep(rnd)
            if True:             
                

                if self.is_element_present('button:contains("Accept")'):
                    self.cdp.mouse_click('button:contains("Accept")')
                if self.is_element_present('button:contains("agree")'):
                    self.cdp.mouse_click('button:contains("agree")')
                if not self.is_element_present("p.editor-paragraph"):
                    self.switch_to_window(0)
                rnd = random.randint(1,24)
                self.sleep(rnd)
                while not self.is_element_present('button:contains("Follow")'):
                    self.switch_to_window(0)
                    rnd = random.randint(10,20)
                    self.sleep(rnd)
                self.cdp.mouse_click('button:contains("Follow")')
                rnd = random.randint(10,20)

                self.sleep(rnd)
                self.cdp.mouse_click('button:contains("Follow")')'''
        assert True
display.stop()








