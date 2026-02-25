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
        
        # === MONTH SELECTION ===
        # Based on the HTML: BirthMonthDropdown is a button with role="combobox"
        try:
            month_dropdown = page.locator('#BirthMonthDropdown')
            if month_dropdown.count() > 0:
                # Focus on the dropdown and press key to open
                month_dropdown.focus()
                time.sleep(0.5)
                page.keyboard.press('Space')
                print("Opened month dropdown with Space")
                time.sleep(1)
                
                # Navigate to the correct month using arrow keys
                # Start from top and navigate to the month index
                for _ in range(month_index):
                    page.keyboard.press('ArrowDown')
                    time.sleep(0.1)
                time.sleep(0.3)
                page.keyboard.press('Enter')
                print(f"Selected month: {month_name}")
        except Exception as e:
            print(f"Month selection failed: {e}")
            # Fallback: Try direct click
            try:
                month_dropdown = page.locator('#BirthMonthDropdown')
                if month_dropdown.count() > 0:
                    month_dropdown.click(force=True, timeout=5000)
                    time.sleep(1)
                    # Type to search
                    page.keyboard.type(month_name[:3])
                    time.sleep(0.5)
                    page.keyboard.press('Enter')
                    print(f"Selected month via typing: {month_name}")
            except Exception as e2:
                print(f"Month fallback also failed: {e2}")
        
        # === DAY SELECTION ===
        # Based on the HTML: BirthDayDropdown is a button with role="combobox"
        try:
            day_dropdown = page.locator('#BirthDayDropdown')
            if day_dropdown.count() > 0:
                # Click the dropdown to open it
                day_dropdown.click()
                print("Clicked day dropdown")
                time.sleep(2)  # Wait for dropdown to fully open
                
                # Try to find and click the day option
                day_options = page.locator(f'text="{day}"')
                if day_options.count() > 0:
                    day_options.first.click()
                    print(f"Selected day: {day}")
                else:
                    # Try typing the number and pressing enter
                    page.keyboard.type(str(day))
                    time.sleep(0.3)
                    page.keyboard.press('Enter')
                    print(f"Selected day via keyboard: {day}")
        except Exception as e:
            print(f"Day selection failed: {e}")
            try:
                # Alternative: Try using aria-label approach
                day_dropdown = page.locator('button[aria-label="Birth day"]')
                if day_dropdown.count() > 0:
                    day_dropdown.click()
                    time.sleep(1)
                    page.keyboard.type(str(day))
                    time.sleep(0.5)
                    page.keyboard.press('Enter')
                    print(f"Selected day via keyboard: {day}")
            except:
                pass
        
        # === YEAR INPUT ===
        # Based on the HTML: Year input has id="floatingLabelInput21"
        try:
            # First try the exact ID from the HTML
            year_input = page.locator('#floatingLabelInput21')
            if year_input.count() > 0:
                year_input.click()
                time.sleep(0.5)
                year_input.fill(str(year))
                print(f"Entered year: {year}")
            else:
                # Try by name attribute
                year_input = page.locator('input[name="BirthYear"]')
                if year_input.count() > 0:
                    year_input.click()
                    time.sleep(0.5)
                    year_input.fill(str(year))
                    print(f"Entered year: {year}")
                else:
                    # Try by aria-label
                    year_input = page.locator('input[aria-label="Birth year"]')
                    if year_input.count() > 0:
                        year_input.click()
                        time.sleep(0.5)
                        year_input.fill(str(year))
                        print(f"Entered year: {year}")
                    else:
                        # Try any number input in the form
                        year_input = page.locator('input[type="number"]')
                        if year_input.count() > 0:
                            year_input.click()
                            time.sleep(0.5)
                            year_input.fill(str(year))
                            print(f"Entered year: {year}")
        except Exception as e:
            print(f"Year input failed: {e}")
        
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
