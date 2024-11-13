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
"https://gdmirrorbot.nl/file/ftyt2ze",
"https://gdmirrorbot.nl/file/lhn9b49",
"https://gdmirrorbot.nl/file/umog2dl",
"https://gdmirrorbot.nl/file/c0zthuq",
"https://gdmirrorbot.nl/file/dlsntnu",
"https://gdmirrorbot.nl/file/mgm5iss",
"https://gdmirrorbot.nl/file/d4ltp5p",
"https://gdmirrorbot.nl/file/ivww0fn",
"https://gdmirrorbot.nl/file/el1y1qk",
"https://gdmirrorbot.nl/file/z0wq4kr",
"https://gdmirrorbot.nl/file/gdiauqy",
"https://gdmirrorbot.nl/file/qdea391",
"https://gdmirrorbot.nl/file/ywrz5ql",
"https://gdmirrorbot.nl/file/untqlxc",
"https://gdmirrorbot.nl/file/qqyecmp",
"https://gdmirrorbot.nl/file/akhbw5s",
"https://gdmirrorbot.nl/file/dfzujo7",
"https://gdmirrorbot.nl/file/iir7yn8",
"https://gdmirrorbot.nl/file/mf43mam",
"https://gdmirrorbot.nl/file/qia5b1a",
"https://gdmirrorbot.nl/file/hxs1gy8",
"https://gdmirrorbot.nl/file/unt2egl",
"https://gdmirrorbot.nl/file/myuw0pq",
"https://gdmirrorbot.nl/file/evqa8hb",
"https://gdmirrorbot.nl/file/p12btpx",
"https://gdmirrorbot.nl/file/ie11aqi",
"https://gdmirrorbot.nl/file/nth091z",
"https://gdmirrorbot.nl/file/u8htv01",
"https://gdmirrorbot.nl/file/gxrmsww",
"https://gdmirrorbot.nl/file/a7mv1ck",
"https://gdmirrorbot.nl/file/svfa2fo",
"https://gdmirrorbot.nl/file/sxeejwz",
"https://gdmirrorbot.nl/file/tpdwn8l",
"https://gdmirrorbot.nl/file/a7u95ob",
"https://gdmirrorbot.nl/file/cchw56e",
"https://gdmirrorbot.nl/file/zkijfft",
"https://gdmirrorbot.nl/file/vrinxqe",
"https://gdmirrorbot.nl/file/m7gwb2o",
"https://gdmirrorbot.nl/file/qzolo4m",
"https://gdmirrorbot.nl/file/z9qjrwt",
"https://gdmirrorbot.nl/file/cbs01yh",
"https://gdmirrorbot.nl/file/pzb4un3",
"https://gdmirrorbot.nl/file/cdnp4u6",
"https://gdmirrorbot.nl/file/r4o5rx2",
"https://gdmirrorbot.nl/file/izfjqja",
"https://gdmirrorbot.nl/file/wt8nzp5",
"https://gdmirrorbot.nl/file/hk8v7u1",
"https://gdmirrorbot.nl/file/xqpd05h",
"https://gdmirrorbot.nl/file/hvtlo5a",
"https://gdmirrorbot.nl/file/s6hrsm7",
"https://gdmirrorbot.nl/file/rdwf6t6",
"https://gdmirrorbot.nl/file/gu767b5",
"https://gdmirrorbot.nl/file/slys3cw",
"https://gdmirrorbot.nl/file/fwwmxfn",
"https://gdmirrorbot.nl/file/yx3iss9",
"https://gdmirrorbot.nl/file/drl852a",
"https://gdmirrorbot.nl/file/s3ayumz",
"https://gdmirrorbot.nl/file/fsbd3ne",
"https://gdmirrorbot.nl/file/h24s90u",
"https://gdmirrorbot.nl/file/u71on6u",
"https://gdmirrorbot.nl/file/bhe6ah5",
"https://gdmirrorbot.nl/file/l7iljk3",
"https://gdmirrorbot.nl/file/kr4r79v",
"https://gdmirrorbot.nl/file/g2ekol7",
"https://gdmirrorbot.nl/file/tp5j6mm",
"https://gdmirrorbot.nl/file/qlm7ee6",
"https://gdmirrorbot.nl/file/jjz0a7m",
"https://gdmirrorbot.nl/file/sthzkng",
"https://gdmirrorbot.nl/file/lg6m5w5",
"https://gdmirrorbot.nl/file/y3fqyef",
"https://gdmirrorbot.nl/file/joizn8l",
"https://gdmirrorbot.nl/file/zvc1nfc",
"https://gdmirrorbot.nl/file/uamye58",
"https://gdmirrorbot.nl/file/d1w024o",
"https://gdmirrorbot.nl/file/ibt2k93",
"https://gdmirrorbot.nl/file/mg3okf8",
"https://gdmirrorbot.nl/file/czi8abr",
"https://gdmirrorbot.nl/file/v3fu69c",
"https://gdmirrorbot.nl/file/f8g6ba8",
"https://gdmirrorbot.nl/file/w7wzkfb",
"https://gdmirrorbot.nl/file/z3lxw0o",
"https://gdmirrorbot.nl/file/zsq8bwx",
"https://gdmirrorbot.nl/file/nnmivwu",
"https://gdmirrorbot.nl/file/lsdy9ix",
"https://gdmirrorbot.nl/file/tzxbcxi",
"https://gdmirrorbot.nl/file/h5jl5b2",
"https://gdmirrorbot.nl/file/hxsjpyt",
"https://gdmirrorbot.nl/file/eiet4oc",
"https://gdmirrorbot.nl/file/jgpuzef",
"https://gdmirrorbot.nl/file/vecwrap",
"https://gdmirrorbot.nl/file/a4hrehf",
"https://gdmirrorbot.nl/file/zc0ohnp",
"https://gdmirrorbot.nl/file/m6thdbz",
"https://gdmirrorbot.nl/file/trgt02r",
"https://gdmirrorbot.nl/file/hni02fx",
"https://gdmirrorbot.nl/file/jipnn1l",
"https://gdmirrorbot.nl/file/pu63cpj"
]

# Function to process each link
def process_link(url):
    print(f"Accessing URL: {url}")
    driver.get(url)
    
    try:
        print("Waiting for redirection...")
        WebDriverWait(driver, 10).until(EC.url_contains("snapinsta.storyy.shop"))
        redirected_url = driver.current_url
        print(f"Redirected to: {redirected_url}")

        if "snapinsta.storyy.shop" in redirected_url:
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
    print("Waiting for 60 sec before proceeding to the next URL...")
    time.sleep(60)  # Wait for 30 sec

# Close the WebDriver
print("Closing the WebDriver...")
driver.quit()
print("Done.")
