import random
import string
import time
from playwright.sync_api import sync_playwright

def generate_random_email():
    """Generate a random email with 10 letters and numbers combination"""
    # First 2 characters must be alphabets
    first_two = ''.join(random.choices(string.ascii_lowercase, k=2))
    # Remaining 8 characters can be letters and numbers
    remaining = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    username = first_two + remaining
    return f"{username}@outlook.com"

def generate_random_name(length=6):
    """Generate a random name with specified length"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

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
            email_input = page.query_selector('input#floatingLabelInput4')
            if email_input:
                print("Found email input by id: floatingLabelInput4")
        except:
            pass
        
        if not email_input:
            email_input = page.query_selector('input[name="Email"]')
            if email_input:
                print("Found email input by name: Email")
        
        if not email_input:
            email_input = page.query_selector('input[aria-label="Email"]')
            if email_input:
                print("Found email input by aria-label: Email")
        
        if not email_input:
            email_input = page.query_selector('input[type="email"]')
            if email_input:
                print("Found email input by type: email")
        
        if not email_input:
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
        
        if next_button:
            print("Clicking Next button...")
            next_button.click()
        else:
            print("Could not find Next button!")
        
        # Step 5: Wait 2-4 seconds after clicking Next
        print("Waiting 3 seconds for password page...")
        time.sleep(3)
        
        # Step 6: Find password input and enter password
        print("Searching for password input...")
        
        password = "rMuD@e5HH5vuvJE"
        password_input = None
        
        try:
            password_input = page.query_selector('input#floatingLabelInput14')
            if password_input:
                print("Found password input by id: floatingLabelInput14")
        except:
            pass
        
        if not password_input:
            password_input = page.query_selector('input[type="password"]')
            if password_input:
                print("Found password input by type: password")
        
        if password_input:
            print(f"Entering password: {password}")
            password_input.fill(password)
        else:
            print("Could not find password input!")
        
        # Click Next button for password
        print("Searching for Next button...")
        next_button = None
        
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
        
        if next_button:
            print("Clicking Next button...")
            next_button.click()
        else:
            print("Could not find Next button!")
        
        # Step 7: Wait 5-6 seconds for birth date page
        print("Waiting 5 seconds for birth date page...")
        time.sleep(5)
        
        # Step 8: Enter birth date (Month, Day, Year)
        print("Entering birth date...")
        
        # Month names list
        months = ["January", "February", "March", "April", "May", "June", 
                  "July", "August", "September", "October", "November", "December"]
        
        # Select random month (by name)
        month_name = random.choice(months)
        month_index = months.index(month_name) + 1
        # Select random day (1-27)
        day = random.randint(1, 27)
        # Select random year (1950-1990)
        year = random.randint(1950, 1990)
        
        print(f"Birth date: Month={month_name}, Day={day}, Year={year}")
        
        # Try to find and fill month - click dropdown first, then select from list
        try:
            # Click on month dropdown to open the list
            month_dropdown = page.query_selector('#BirthMonthDropdown')
            if month_dropdown:
                month_dropdown.click()
                print("Clicked month dropdown")
                time.sleep(1)
                # Select the month from the list
                month_option = page.query_selector(f'li[data-month="{month_index}"]')
                if not month_option:
                    month_option = page.query_selector(f'text={month_name}')
                if month_option:
                    month_option.click()
                    print(f"Selected month: {month_name}")
        except Exception as e:
            print(f"Month selection failed: {e}")
            # Try alternative - type in the field
            try:
                month_input = page.query_selector('#BirthMonthDropdown')
                if month_input:
                    month_input.fill(month_name)
                    print(f"Entered month: {month_name}")
            except:
                pass
        
        # Try to find and fill day - click dropdown first, then select from list
        try:
            # Click on day dropdown to open the list
            day_dropdown = page.query_selector('#BirthDayDropdown')
            if day_dropdown:
                day_dropdown.click()
                print("Clicked day dropdown")
                time.sleep(1)
                # Select the day from the list
                day_option = page.query_selector(f'li[data-day="{day}"]')
                if not day_option:
                    day_option = page.query_selector(f'text={day}')
                if day_option:
                    day_option.click()
                    print(f"Selected day: {day}")
        except Exception as e:
            print(f"Day selection failed: {e}")
            # Try alternative - type in the field
            try:
                day_input = page.query_selector('#BirthDayDropdown')
                if day_input:
                    day_input.fill(str(day))
                    print(f"Entered day: {day}")
            except:
                pass
        
        # Try to find and fill year input - can type directly
        try:
            year_input = page.query_selector('#floatingLabelInput24')
            if year_input:
                year_input.fill(str(year))
                print(f"Entered year: {year}")
        except Exception as e:
            print(f"Year input failed: {e}")
            # Try by label
            try:
                year_input = page.query_selector('input[aria-label="Year"]')
                if year_input:
                    year_input.fill(str(year))
                    print(f"Entered year: {year}")
            except:
                pass
        
        # Click Next button for birth date
        print("Searching for Next button...")
        next_button = None
        
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
        
        if next_button:
            print("Clicking Next button...")
            next_button.click()
        else:
            print("Could not find Next button!")
        
        # Step 9: Wait 4-5 seconds for name page
        print("Waiting 4 seconds for name page...")
        time.sleep(4)
        
        # Step 10: Enter first name and last name
        print("Entering name...")
        
        first_name = generate_random_name(6)
        last_name = generate_random_name(6)
        
        print(f"First name: {first_name}, Last name: {last_name}")
        
        # Find and fill first name
        try:
            first_name_input = page.query_selector('input#firstNameInput')
            if first_name_input:
                first_name_input.fill(first_name)
                print(f"Entered first name: {first_name}")
        except Exception as e:
            print(f"First name input failed: {e}")
            try:
                first_name_input = page.query_selector('input[aria-label="First name"]')
                if first_name_input:
                    first_name_input.fill(first_name)
                    print(f"Entered first name: {first_name}")
            except:
                pass
        
        # Find and fill last name
        try:
            last_name_input = page.query_selector('input#lastNameInput')
            if last_name_input:
                last_name_input.fill(last_name)
                print(f"Entered last name: {last_name}")
        except Exception as e:
            print(f"Last name input failed: {e}")
            try:
                last_name_input = page.query_selector('input[aria-label="Last name"]')
                if last_name_input:
                    last_name_input.fill(last_name)
                    print(f"Entered last name: {last_name}")
            except:
                pass
        
        # Click Next button for name
        print("Searching for Next button...")
        next_button = None
        
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
        
        if next_button:
            print("Clicking Next button...")
            next_button.click()
        else:
            print("Could not find Next button!")
        
        print("Form submitted successfully!")
        
        # Keep browser open to see the result
        page.wait_for_timeout(10000)
        
        browser.close()

if __name__ == "__main__":
    main()
