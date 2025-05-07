from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://kick.com/browse"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    sb.cdp.gui_click_x_y(236.0, 429.0)
    sb.assert_text("Username", '[for="user_login"]', timeout=3)
    sb.assert_element('label[for="user_login"]')
    sb.highlight('button:contains("Sign in")')
    sb.highlight('h1:contains("GitLab.com")')
    sb.post_message("SeleniumBase wasn't detected", duration=4)
    print("Success! Website did not detect SeleniumBase!")
