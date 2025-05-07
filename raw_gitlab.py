from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.cdp.save_screenshot("ssasa.png", folder='./latest_logs')
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.cdp.save_screenshot("ssasa2.png", folder='./latest_logs')
    sb.assert_text("Username", '[for="user_login"]', timeout=3)
    sb.assert_element('label[for="user_login"]')
    sb.highlight('button:contains("Sign in")')
    sb.highlight('h1:contains("GitLab.com")')
    sb.post_message("SeleniumBase wasn't detected", duration=4)
    print("Success! Website did not detect SeleniumBase!")
