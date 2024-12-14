from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Import the time module for adding delays

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")

# Initialize the WebDriver without specifying a path (GitHub Actions default)
driver = webdriver.Chrome(options=chrome_options)

# List of URLs to process
urls = [
"https://gdmirrorbot.nl/file/erxk9z8",
"https://gdmirrorbot.nl/file/kermsme",
"https://gdmirrorbot.nl/file/l3e80zf",
"https://gdmirrorbot.nl/file/yya56ii",
"https://gdmirrorbot.nl/file/mdhih6s",
"https://gdmirrorbot.nl/file/halivqr",
"https://gdmirrorbot.nl/file/klxb1vl",
"https://gdmirrorbot.nl/file/vifmrbw",
"https://gdmirrorbot.nl/file/qbtojio",
"https://gdmirrorbot.nl/file/dpspnzk",
"https://gdmirrorbot.nl/file/lf3lppa",
"https://gdmirrorbot.nl/file/hiu8dnp",
"https://gdmirrorbot.nl/file/ycj8n9g",
"https://gdmirrorbot.nl/file/x1ixbvj",
"https://gdmirrorbot.nl/file/hm44be4",
"https://gdmirrorbot.nl/file/qa4dl11",
"https://gdmirrorbot.nl/file/ry7wxav",
"https://gdmirrorbot.nl/file/eqona50",
"https://gdmirrorbot.nl/file/necm1v2",
"https://gdmirrorbot.nl/file/gi87tu8",
"https://gdmirrorbot.nl/file/gg8x986",
"https://gdmirrorbot.nl/file/vw1sbj8",
"https://gdmirrorbot.nl/file/ukuv1o7",
"https://gdmirrorbot.nl/file/ik6oj0g",
"https://gdmirrorbot.nl/file/c18cxr3",
"https://gdmirrorbot.nl/file/j1oapoc"
]

# Function to process each link
def process_link(url):
    print(f"Accessing URL: {url}")
    driver.get(url)
    
    try:
        print("Waiting for redirection...")
        WebDriverWait(driver, 10).until(EC.url_contains("gtm.snapinsta.monster"))
        redirected_url = driver.current_url
        print(f"Redirected to: {redirected_url}")

        if "gtm.snapinsta.monster" in redirected_url:
            try:
                print("Waiting for 'Generate New Link' button to become visible...")
                generate_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//input[@type='submit' and @value='Generate New Link']"))
                )
                print("Scrolling to the 'Generate New Link' button...")
                driver.execute_script("arguments[0].scrollIntoView(true);", generate_button)

                # Use JavaScript click to avoid interception issues
                print("Clicking the 'Generate New Link' button...")
                driver.execute_script("arguments[0].click();", generate_button)
                print("Successfully clicked the 'Generate New Link' button.")

                # Optionally, wait for the new page to load after clicking
                print("Waiting for the new page to load...")
                WebDriverWait(driver, 10).until(EC.staleness_of(generate_button))
                print("New page has loaded.")

            except Exception as e:
                print(f"An error occurred while trying to click the button: {e}")
        else:
            print("Redirection did not lead to the expected site.")

    except Exception as e:
        print(f"An error occurred during redirection: {e}")

# Loop through each URL and process with a 1-minute delay
for url in urls:
    process_link(url)
    print("Waiting for 600 sec before proceeding to the next URL...")
    time.sleep(60)  # Wait for 30 sec

# Close the WebDriver
print("Closing the WebDriver...")
driver.quit()
print("Done.")
