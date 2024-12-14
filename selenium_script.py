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
"https://gdmirrorbot.nl/file/px962db",
"https://gdmirrorbot.nl/file/pl1onkp",
"https://gdmirrorbot.nl/file/uj2lvyd",
"https://gdmirrorbot.nl/file/xmcv2ra",
"https://gdmirrorbot.nl/file/i4hlog2",
"https://gdmirrorbot.nl/file/ds24z3d",
"https://gdmirrorbot.nl/file/bb9jr4p",
"https://gdmirrorbot.nl/file/de0gpfy",
"https://gdmirrorbot.nl/file/ugxlkmn",
"https://gdmirrorbot.nl/file/m0x0k70",
"https://gdmirrorbot.nl/file/kazslg6",
"https://gdmirrorbot.nl/file/m86i79o",
"https://gdmirrorbot.nl/file/aygu0vf",
"https://gdmirrorbot.nl/file/u8838v8",
"https://gdmirrorbot.nl/file/fmkwt3w",
"https://gdmirrorbot.nl/file/gwvzfrv",
"https://gdmirrorbot.nl/file/mcr96wu",
"https://gdmirrorbot.nl/file/oeu8b3p",
"https://gdmirrorbot.nl/file/tw2y69l",
"https://gdmirrorbot.nl/file/xckm9hp",
"https://gdmirrorbot.nl/file/n0m98cx",
"https://gdmirrorbot.nl/file/ddswgb9",
"https://gdmirrorbot.nl/file/zdgx2x2",
"https://gdmirrorbot.nl/file/z92lskj",
"https://gdmirrorbot.nl/file/zmfzdz6",
"https://gdmirrorbot.nl/file/wezxt5i",
"https://gdmirrorbot.nl/file/n4h25rw",
"https://gdmirrorbot.nl/file/j30p2hg",
"https://gdmirrorbot.nl/file/lhc4e21",
"https://gdmirrorbot.nl/file/g7slduj",
"https://gdmirrorbot.nl/file/ok9vglb",
"https://gdmirrorbot.nl/file/c1mn9ef",
"https://gdmirrorbot.nl/file/ehibb2b",
"https://gdmirrorbot.nl/file/ajgyee1",
"https://gdmirrorbot.nl/file/hgqzhsq",
"https://gdmirrorbot.nl/file/ms2ht7d",
"https://gdmirrorbot.nl/file/qm3qf4j",
"https://gdmirrorbot.nl/file/z87s40j",
"https://gdmirrorbot.nl/file/yenoimw",
"https://gdmirrorbot.nl/file/rzq2yjy",
"https://gdmirrorbot.nl/file/f3nff19",
"https://gdmirrorbot.nl/file/t521v3r",
"https://gdmirrorbot.nl/file/usvo9pe",
"https://gdmirrorbot.nl/file/t9f5fsx",
"https://gdmirrorbot.nl/file/sytk3k9",
"https://gdmirrorbot.nl/file/g3f549f",
"https://gdmirrorbot.nl/file/j7bckkc",
"https://gdmirrorbot.nl/file/aqxy6u9",
"https://gdmirrorbot.nl/file/xxsqx3r",
"https://gdmirrorbot.nl/file/fjkeust",
"https://gdmirrorbot.nl/file/eposbzt",
"https://gdmirrorbot.nl/file/s9ru9cd",
"https://gdmirrorbot.nl/file/ah8evvx",
"https://gdmirrorbot.nl/file/svfz4q2",
"https://gdmirrorbot.nl/file/ua0qpea",
"https://gdmirrorbot.nl/file/rbg1ml3",
"https://gdmirrorbot.nl/file/a57qcsh",
"https://gdmirrorbot.nl/file/yb0zd0r",
"https://gdmirrorbot.nl/file/rsjv7nj",
"https://gdmirrorbot.nl/file/zpwp0sg",
"https://gdmirrorbot.nl/file/fdau05r",
"https://gdmirrorbot.nl/file/snce6pe",
"https://gdmirrorbot.nl/file/ogyit6f",
"https://gdmirrorbot.nl/file/bu6bjco",
"https://gdmirrorbot.nl/file/hvm1dlp",
"https://gdmirrorbot.nl/file/l8kek0q",
"https://gdmirrorbot.nl/file/vawkpe7",
"https://gdmirrorbot.nl/file/dttg53q",
"https://gdmirrorbot.nl/file/odkpvyk",
"https://gdmirrorbot.nl/file/ex941ty",
"https://gdmirrorbot.nl/file/jwlrkjr",
"https://gdmirrorbot.nl/file/o7io0ua",
"https://gdmirrorbot.nl/file/acm8k3a",
"https://gdmirrorbot.nl/file/umqvvn3",
"https://gdmirrorbot.nl/file/oon2kb9",
"https://gdmirrorbot.nl/file/uv5otpu",
"https://gdmirrorbot.nl/file/vnvwpy1",
"https://gdmirrorbot.nl/file/u4nz5yv",
"https://gdmirrorbot.nl/file/u11k5g9",
"https://gdmirrorbot.nl/file/weytf00",
"https://gdmirrorbot.nl/file/diqoilb",
"https://gdmirrorbot.nl/file/zblj0dz",
"https://gdmirrorbot.nl/file/bujli9x",
"https://gdmirrorbot.nl/file/ubu9qsm",
"https://gdmirrorbot.nl/file/p6glmka",
"https://gdmirrorbot.nl/file/casr5h6",
"https://gdmirrorbot.nl/file/epj8stn",
"https://gdmirrorbot.nl/file/gnger48",
"https://gdmirrorbot.nl/file/hkti8ll",
"https://gdmirrorbot.nl/file/cc0pgt8",
"https://gdmirrorbot.nl/file/xmnroez",
"https://gdmirrorbot.nl/file/zjnuu94",
"https://gdmirrorbot.nl/file/l08bpnr",
"https://gdmirrorbot.nl/file/fh9ncbn",
"https://gdmirrorbot.nl/file/qeunbs3",
"https://gdmirrorbot.nl/file/zhb6rsg",
"https://gdmirrorbot.nl/file/candhjs",
"https://gdmirrorbot.nl/file/tmct8je",
"https://gdmirrorbot.nl/file/jtdqwxz",
"https://gdmirrorbot.nl/file/rt6gwaw",
"https://gdmirrorbot.nl/file/f6t3mar",
"https://gdmirrorbot.nl/file/f0ca1lz",
"https://gdmirrorbot.nl/file/qc79nn1",
"https://gdmirrorbot.nl/file/kiuz79w",
"https://gdmirrorbot.nl/file/g3qxydn",
"https://gdmirrorbot.nl/file/cdtwd2i",
"https://gdmirrorbot.nl/file/xxih1dh",
"https://gdmirrorbot.nl/file/nnep5ze",
"https://gdmirrorbot.nl/file/nmvmcsr",
"https://gdmirrorbot.nl/file/q4b7ufd",
"https://gdmirrorbot.nl/file/d5ptujk",
"https://gdmirrorbot.nl/file/qdnuabj",
"https://gdmirrorbot.nl/file/eqculo6",
"https://gdmirrorbot.nl/file/a4r35yo",
"https://gdmirrorbot.nl/file/pmjnqeb",
"https://gdmirrorbot.nl/file/sfsbv8a",
"https://gdmirrorbot.nl/file/hlsloey",
"https://gdmirrorbot.nl/file/tf6kmtq",
"https://gdmirrorbot.nl/file/r7hq3f7",
"https://gdmirrorbot.nl/file/n1n8sgw",
"https://gdmirrorbot.nl/file/nl7h276",
"https://gdmirrorbot.nl/file/ppcjdwx",
"https://gdmirrorbot.nl/file/ue4y9zi",
"https://gdmirrorbot.nl/file/g3hbg23",
"https://gdmirrorbot.nl/file/tcia7x3",
"https://gdmirrorbot.nl/file/vvdsjae",
"https://gdmirrorbot.nl/file/oxd3ump",
"https://gdmirrorbot.nl/file/uv27cyu",
"https://gdmirrorbot.nl/file/a2lv3j1",
"https://gdmirrorbot.nl/file/to4lb92",
"https://gdmirrorbot.nl/file/ty35gqy",
"https://gdmirrorbot.nl/file/ph4xxrc",
"https://gdmirrorbot.nl/file/sizsxw6",
"https://gdmirrorbot.nl/file/oqeqke4",
"https://gdmirrorbot.nl/file/wwr0tq4",
"https://gdmirrorbot.nl/file/ok4g55u",
"https://gdmirrorbot.nl/file/fnsxifc",
"https://gdmirrorbot.nl/file/r1tuiy1",
"https://gdmirrorbot.nl/file/l1dxgoy",
"https://gdmirrorbot.nl/file/xcr6ngy",
"https://gdmirrorbot.nl/file/c96spmp",
"https://gdmirrorbot.nl/file/k8bjdqn",
"https://gdmirrorbot.nl/file/gl3up3s",
"https://gdmirrorbot.nl/file/k0jhckc",
"https://gdmirrorbot.nl/file/x54ga67",
"https://gdmirrorbot.nl/file/bg5b1ud",
"https://gdmirrorbot.nl/file/i4aszmd",
"https://gdmirrorbot.nl/file/smfqsvq",
"https://gdmirrorbot.nl/file/nx3b72w",
"https://gdmirrorbot.nl/file/gquv2kt",
"https://gdmirrorbot.nl/file/tkme3zu",
"https://gdmirrorbot.nl/file/d23x5ws",
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
