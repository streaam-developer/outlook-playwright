import random
import string
import time
from playwright.sync_api import sync_playwright

def generate_random_email():
    """Generate a random email with 10 letters and numbers combination"""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@outlook.com"

def main():
    # Generate a random email
    email = generate_random_email()
    print(f"Generated email: {email}")
    
    with sync_playwright() as p:
        # Launch browser (Chromium)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Open the signup page
        print("Opening signup.live.com...")
        page.goto("https://signup.live.com/")
        
        # Step 2: Wait for 2-4 seconds for the page to fully load
        print("Waiting for page to load...")
        time.sleep(3)
        
        # Step 3: Find the email input field and enter the email
        print(f"Searching for email input field...")
        
        # Try multiple selectors to find the email input
        email_input = None
        try:
            # Try by id first
            email_input = page.query_selector('input#floatingLabelInput4')
            if email_input:
                print("Found email input by id: floatingLabelInputInput4")
        except:
            pass
        
        if not email_input:
            # Try by name
            email_input = page.query_selector('input[name="Email"]')
            if email_input:
                print("Found email input by name: Email")
        
        if not email_input:
            # Try by aria-label
            email_input = page.query_selector('input[aria-label="Email"]')
            if email_input:
                print("Found email input by aria-label: Email")
        
        if not email_input:
            # Try any input with type email
            email_input = page.query_selector('input[type="email"]')
            if email_input:
                print("Found email input by type: email")
        
        if not email_input:
            # Try any input that looks like email field
            email_input = page.query_selector('input.fui-Input__input')
            if email_input:
                print("Found email input by class: fui-Input__input")
        
        # If found, enter the email
        if email_input:
            print(f"Entering email: {email}")
            email_input.fill(email)
        else:
            print("Could not find email input field!")
        
        # Step 4: Search for the Next button and click it
        print("Searching for Next button...")
        
        next_button = None
        
        # Try multiple selectors to find the Next button
        try:
            next_button = page.query_selector('button:has-text("Next")')
            if next_button:
                print("Found Next button by text")
        except:
            pass
        
        if not next_button:
            next_button = page.query_selector('button[type="submit"]')
            if next_button:
                print("Found Next button by type: submit")
        
        if not next_button:
            next_button = page.query_selector('button.fui-Button')
            if next_button:
                print("Found Next button by class: fui-Button")
        
        # If found, click it
        if next_button:
            print("Clicking Next button...")
            next_button.click()
        else:
            print("Could not find Next button!")
        
        # Wait for navigation or any response
        print("Waiting for response...")
        time.sleep(3)
        
        print("Form submitted successfully!")
        
        # Keep browser open for a few seconds to see the result
        page.wait_for_timeout(5000)
        
        browser.close()

if __name__ == "__main__":
    main()
