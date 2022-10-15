"""
This program will extract LinkedIn pages from messages.txt and connect to them.
To use, simply copy messages into messages.txt, and input login information into linkedin_constants.py
Then, it will automatically extract LinkedIn pages, and it will connect to all the pages found.
"""
# imports
import undetected_chromedriver as uc
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.options import ChromiumOptions
from time import sleep
from linkedin_constants import *

# from pprint import pprint


def clean_link(link: str) -> str:
    """Given a message containing a link, return only the link"""
    # split apart the message into words and find the one containing the link
    message_text = link.split()
    for message in message_text:
        if "www.linkedin.com" in message:
            # remove whitespace
            return message.strip()


def connect(driver: uc.Chrome, link: str) -> None:
    """Given a webdriver and a LinkedIn page, use the web driver to connect with them."""
    print("Trying to connect with", link)
    driver.get(link)
    sleep(2)
    # html makes it tough to find the connect button :(
    profile_bar = driver.find_element(By.CSS_SELECTOR, "div[class='pvs-profile-actions ']")
    try:
        connect_button = profile_bar.find_element(By.CLASS_NAME, 'artdeco-button--primary')
        connect_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        # in case connect is hidden in dropdown
        more_buttons = profile_bar.find_element(By.CLASS_NAME, 'artdeco-dropdown__trigger')
        more_buttons.click()
        connect_button = profile_bar.find_element(By.CSS_SELECTOR, "li-icon[type='connect']")
        connect_button.click()
        # connection category, other
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Other']").click()
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Connect']").click()

    sleep(1)
    # add message to connect and confirmation to send
    add_note = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add a note']")
    add_note.click()
    message_box = driver.find_element(By.ID, "custom-message")
    message_box.send_keys(CONNECT_MESSAGE)
    send_now = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Send now']")
    send_now.click()
    print("Connection request sended.")


def main() -> None:
    """
    First, read the messages.txt text file and extract all LinkedIn containing messages from it.
    Then, clean all the links to have just the links themselves.
    Then, log into LinkedIn and connect to every LinkedIn link.
    """
    links = []

    # extract links containing messages
    print("Reading messages...")
    with open("messages.txt", encoding="utf-8") as messages:
        for line in messages:
            # check if message has a LinkedIn link in it
            if line.count('https') == 1 and 'www.linkedin.com/in' in line:
                links.append(line)
    print(f"Found {len(links)} messages.")

    links = [clean_link(link) for link in links]

    if links:
        # Set up webdriver and sign in procedure
        options = ChromiumOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")

        driver = uc.Chrome(options=options)
        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        print("Signing into LinkedIn...")

        email = driver.find_element(By.ID, 'username')
        email.send_keys(LINKED_EMAIL)
        password = driver.find_element(By.ID, 'password')
        password.send_keys(LINKED_PASS)
        driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()
        print("Sign in successful.")
        sleep(2)

        # Connect to links
        for i in range(len(links)):
            try:
                print(f"Attempt {i + 1}: ", end="")
                connect(driver, links[i])
            except selenium.common.exceptions.NoSuchElementException:
                print("Link did not work.")

    # Clear the messages text
    with open("messages.txt", "w", encoding="utf-8"):
        pass
    print("Process finished. Message document cleared.")


if __name__ == '__main__':
    main()
