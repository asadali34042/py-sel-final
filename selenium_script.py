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
"https://gdmirrorbot.nl/file/ngek90c",
"https://gdmirrorbot.nl/file/s1lrqz9",
"https://gdmirrorbot.nl/file/rg3256b",
"https://gdmirrorbot.nl/file/jmxow97",
"https://gdmirrorbot.nl/file/wc6gk5q",
"https://gdmirrorbot.nl/file/qll3605",
"https://gdmirrorbot.nl/file/a0cuylq",
"https://gdmirrorbot.nl/file/lwdu9ld",
"https://gdmirrorbot.nl/file/h8rqe68",
"https://gdmirrorbot.nl/file/usnbhel",
"https://gdmirrorbot.nl/file/viamcew",
"https://gdmirrorbot.nl/file/af9cyi3",
"https://gdmirrorbot.nl/file/a7o1oe7",
"https://gdmirrorbot.nl/file/ztis0x8",
"https://gdmirrorbot.nl/file/jquxubv",
"https://gdmirrorbot.nl/file/dgswkna",
"https://gdmirrorbot.nl/file/vdu2iun",
"https://gdmirrorbot.nl/file/h5h592q",
"https://gdmirrorbot.nl/file/lacvwor",
"https://gdmirrorbot.nl/file/qisx34c",
"https://gdmirrorbot.nl/file/rf10m12",
"https://gdmirrorbot.nl/file/d8pm7as",
"https://gdmirrorbot.nl/file/j7bwonc",
"https://gdmirrorbot.nl/file/wyxkh3j",
"https://gdmirrorbot.nl/file/l76mtzu",
"https://gdmirrorbot.nl/file/cgrq1jg",
"https://gdmirrorbot.nl/file/etery4a",
"https://gdmirrorbot.nl/file/lpxzka7",
"https://gdmirrorbot.nl/file/h88cx3d",
"https://gdmirrorbot.nl/file/etj4d4j",
"https://gdmirrorbot.nl/file/o44pwak",
"https://gdmirrorbot.nl/file/q3oa1tj",
"https://gdmirrorbot.nl/file/w5llrgf",
"https://gdmirrorbot.nl/file/msopa3r",
"https://gdmirrorbot.nl/file/e7q1iwb",
"https://gdmirrorbot.nl/file/jh3f3rk",
"https://gdmirrorbot.nl/file/a0dvb7m",
"https://gdmirrorbot.nl/file/gkimnsr",
"https://gdmirrorbot.nl/file/s4jj48z",
"https://gdmirrorbot.nl/file/u87lbnd",
"https://gdmirrorbot.nl/file/t8oww7y",
"https://gdmirrorbot.nl/file/ye1lo3x",
"https://gdmirrorbot.nl/file/blhxf90",
"https://gdmirrorbot.nl/file/uilnpn8",
"https://gdmirrorbot.nl/file/i6igdkk",
"https://gdmirrorbot.nl/file/qnbfe3c",
"https://gdmirrorbot.nl/file/upqf0cf",
"https://gdmirrorbot.nl/file/pmpv2mv",
"https://gdmirrorbot.nl/file/ysy97ge",
"https://gdmirrorbot.nl/file/ps1mwlm",
"https://gdmirrorbot.nl/file/ziak11u",
"https://gdmirrorbot.nl/file/oi2gzgw",
"https://gdmirrorbot.nl/file/etawqet",
"https://gdmirrorbot.nl/file/c3sh58o",
"https://gdmirrorbot.nl/file/dba2tb6",
"https://gdmirrorbot.nl/file/ca1t8he",
"https://gdmirrorbot.nl/file/ubqf9zw",
"https://gdmirrorbot.nl/file/d068odk",
"https://gdmirrorbot.nl/file/xhqli16",
"https://gdmirrorbot.nl/file/a8uwx7s",
"https://gdmirrorbot.nl/file/ff5h31u",
"https://gdmirrorbot.nl/file/v6fxzp8",
"https://gdmirrorbot.nl/file/k8zr6wr",
"https://gdmirrorbot.nl/file/adsppk0",
"https://gdmirrorbot.nl/file/f33t9s7",
"https://gdmirrorbot.nl/file/qi7etvb",
"https://gdmirrorbot.nl/file/ersem5o",
"https://gdmirrorbot.nl/file/zvw1h7x",
"https://gdmirrorbot.nl/file/v0f540d",
"https://gdmirrorbot.nl/file/tql2wug",
"https://gdmirrorbot.nl/file/oa8483s",
"https://gdmirrorbot.nl/file/vq5dz3z",
"https://gdmirrorbot.nl/file/camgicv",
"https://gdmirrorbot.nl/file/hd86q8k",
"https://gdmirrorbot.nl/file/bg81ynd",
"https://gdmirrorbot.nl/file/wnpb8w1",
"https://gdmirrorbot.nl/file/d661mj1",
"https://gdmirrorbot.nl/file/gvib8o4",
"https://gdmirrorbot.nl/file/blogmma",
"https://gdmirrorbot.nl/file/eowhtox",
"https://gdmirrorbot.nl/file/hj5wg7b",
"https://gdmirrorbot.nl/file/fpjk8g7",
"https://gdmirrorbot.nl/file/ry5dipv",
"https://gdmirrorbot.nl/file/vgoapym",
"https://gdmirrorbot.nl/file/faflllr",
"https://gdmirrorbot.nl/file/tvp6n65",
"https://gdmirrorbot.nl/file/r8oilqv",
"https://gdmirrorbot.nl/file/g0fqqhj",
"https://gdmirrorbot.nl/file/d6roxp6",
"https://gdmirrorbot.nl/file/n9byjp8",
"https://gdmirrorbot.nl/file/if9gpl1",
"https://gdmirrorbot.nl/file/h1wfzh9",
"https://gdmirrorbot.nl/file/benmslw",
"https://gdmirrorbot.nl/file/becijb6",
"https://gdmirrorbot.nl/file/xa8pmyj",
"https://gdmirrorbot.nl/file/yao6505",
"https://gdmirrorbot.nl/file/fi1g05k",
"https://gdmirrorbot.nl/file/baodqul",
"https://gdmirrorbot.nl/file/rm9hl4g",
"https://gdmirrorbot.nl/file/oro846z",
"https://gdmirrorbot.nl/file/mtx8i3x",
"https://gdmirrorbot.nl/file/f84ll4l",
"https://gdmirrorbot.nl/file/kjitqj7",
"https://gdmirrorbot.nl/file/qivfyuw",
"https://gdmirrorbot.nl/file/w5cadgf",
"https://gdmirrorbot.nl/file/e69cajg",
"https://gdmirrorbot.nl/file/i8wpjre",
"https://gdmirrorbot.nl/file/n9aow3r",
"https://gdmirrorbot.nl/file/p75zl8v",
"https://gdmirrorbot.nl/file/sv5lxnn",
"https://gdmirrorbot.nl/file/prx5t08",
"https://gdmirrorbot.nl/file/z9h1vem",
"https://gdmirrorbot.nl/file/iyb9orz",
"https://gdmirrorbot.nl/file/o49re55",
"https://gdmirrorbot.nl/file/nxszqay",
"https://gdmirrorbot.nl/file/j649t3p",
"https://gdmirrorbot.nl/file/q8xrsxr",
"https://gdmirrorbot.nl/file/govd1n9",
"https://gdmirrorbot.nl/file/e5l5ibf",
"https://gdmirrorbot.nl/file/fatpp0m",
"https://gdmirrorbot.nl/file/jaqa9b1",
"https://gdmirrorbot.nl/file/l8w00w3",
"https://gdmirrorbot.nl/file/nqfqlij",
"https://gdmirrorbot.nl/file/r7tk0rq",
"https://gdmirrorbot.nl/file/ruuj045",
"https://gdmirrorbot.nl/file/igia9yr",
"https://gdmirrorbot.nl/file/lzmxs5y",
"https://gdmirrorbot.nl/file/dumrz6f",
"https://gdmirrorbot.nl/file/f35ywgm",
"https://gdmirrorbot.nl/file/elymrl0",
"https://gdmirrorbot.nl/file/vbb1bhk",
"https://gdmirrorbot.nl/file/jymvkj8",
"https://gdmirrorbot.nl/file/rhqfnue",
"https://gdmirrorbot.nl/file/pj47zov",
"https://gdmirrorbot.nl/file/u37mr4f",
"https://gdmirrorbot.nl/file/hqu5kbm",
"https://gdmirrorbot.nl/file/smipuwk",
"https://gdmirrorbot.nl/file/tmai8g9",
"https://gdmirrorbot.nl/file/rw62io3",
"https://gdmirrorbot.nl/file/clquu12",
"https://gdmirrorbot.nl/file/zunammi",
"https://gdmirrorbot.nl/file/m2m1trd",
"https://gdmirrorbot.nl/file/cy42ske",
"https://gdmirrorbot.nl/file/p4l0xyf",
"https://gdmirrorbot.nl/file/t27mi0d",
"https://gdmirrorbot.nl/file/c2fjdxg",
"https://gdmirrorbot.nl/file/bbgfpdg",
"https://gdmirrorbot.nl/file/r5ad0js",
"https://gdmirrorbot.nl/file/kowa2o4",
"https://gdmirrorbot.nl/file/rphteud",
"https://gdmirrorbot.nl/file/vvljwfk",
"https://gdmirrorbot.nl/file/bev52o1",
"https://gdmirrorbot.nl/file/c02zpw5",
"https://gdmirrorbot.nl/file/hyphr3r",
"https://gdmirrorbot.nl/file/yyntpuf",
"https://gdmirrorbot.nl/file/osxhl9j",
"https://gdmirrorbot.nl/file/n3hoks4",
"https://gdmirrorbot.nl/file/itr98y5",
"https://gdmirrorbot.nl/file/r5w49f8",
"https://gdmirrorbot.nl/file/jg35e1q",
"https://gdmirrorbot.nl/file/n4ovpsu",
"https://gdmirrorbot.nl/file/iswtvbz",
"https://gdmirrorbot.nl/file/g6oy316",
"https://gdmirrorbot.nl/file/srxcnwv",
"https://gdmirrorbot.nl/file/w3wq1n3",
"https://gdmirrorbot.nl/file/zq0uz0s",
"https://gdmirrorbot.nl/file/mtkelx9",
"https://gdmirrorbot.nl/file/cdiu6tt",
"https://gdmirrorbot.nl/file/osgzafu",
"https://gdmirrorbot.nl/file/s7qyuwt",
"https://gdmirrorbot.nl/file/c8rkyny",
"https://gdmirrorbot.nl/file/vv6gh1i",
"https://gdmirrorbot.nl/file/mdzan96",
"https://gdmirrorbot.nl/file/juhsr5o",
"https://gdmirrorbot.nl/file/e3cysg5",
"https://gdmirrorbot.nl/file/vfc7usy",
"https://gdmirrorbot.nl/file/o7w13yz",
"https://gdmirrorbot.nl/file/b9wzh1d",
"https://gdmirrorbot.nl/file/mepgu51",
"https://gdmirrorbot.nl/file/d9vx2nz",
"https://gdmirrorbot.nl/file/huyemi0",
"https://gdmirrorbot.nl/file/ulvl218",
"https://gdmirrorbot.nl/file/jj6eq7k",
"https://gdmirrorbot.nl/file/limtii0",
"https://gdmirrorbot.nl/file/vjmv1f0",
"https://gdmirrorbot.nl/file/dera3mj",
"https://gdmirrorbot.nl/file/ip72504",
"https://gdmirrorbot.nl/file/sa3uibq",
"https://gdmirrorbot.nl/file/zdo0mws",
"https://gdmirrorbot.nl/file/foflsft",
"https://gdmirrorbot.nl/file/kd7ru1v",
"https://gdmirrorbot.nl/file/byeqz8v",
"https://gdmirrorbot.nl/file/wgxl6q9",
"https://gdmirrorbot.nl/file/mrxo9cs",
"https://gdmirrorbot.nl/file/mjl5w7o",
"https://gdmirrorbot.nl/file/he598do",
"https://gdmirrorbot.nl/file/rwr1x6u",
"https://gdmirrorbot.nl/file/sm769zs",
"https://gdmirrorbot.nl/file/hk2lur5",
"https://gdmirrorbot.nl/file/fhc5mut",
"https://gdmirrorbot.nl/file/v1pqwa0",
"https://gdmirrorbot.nl/file/cnwwhmu",
"https://gdmirrorbot.nl/file/vneqta6",
"https://gdmirrorbot.nl/file/kthlrud",
"https://gdmirrorbot.nl/file/ii7rufv",
"https://gdmirrorbot.nl/file/vl7fn8t",
"https://gdmirrorbot.nl/file/sxa1ngm",
"https://gdmirrorbot.nl/file/ggb5tp6",
"https://gdmirrorbot.nl/file/nnjlhoi",
"https://gdmirrorbot.nl/file/uborlkf",
"https://gdmirrorbot.nl/file/il30hhw",
"https://gdmirrorbot.nl/file/kinr2xt",
"https://gdmirrorbot.nl/file/h1cdxw2",
"https://gdmirrorbot.nl/file/kx52wwy",
"https://gdmirrorbot.nl/file/swfjg2i",
"https://gdmirrorbot.nl/file/gp9whhw",
"https://gdmirrorbot.nl/file/zfkzids",
"https://gdmirrorbot.nl/file/ffvkb7y",
"https://gdmirrorbot.nl/file/kcapg55",
"https://gdmirrorbot.nl/file/tpp0j6v",
"https://gdmirrorbot.nl/file/t6ev8aa",
"https://gdmirrorbot.nl/file/vtkmwoi",
"https://gdmirrorbot.nl/file/pe0pfqr",
"https://gdmirrorbot.nl/file/qblbqtu",
"https://gdmirrorbot.nl/file/i4kuc1t",
"https://gdmirrorbot.nl/file/wkptht2",
"https://gdmirrorbot.nl/file/girteb2",
"https://gdmirrorbot.nl/file/i4exccg",
"https://gdmirrorbot.nl/file/d4kajza",
"https://gdmirrorbot.nl/file/jyrz9af",
"https://gdmirrorbot.nl/file/kg92q3y",
"https://gdmirrorbot.nl/file/b96p3il",
"https://gdmirrorbot.nl/file/zejqh3k",
"https://gdmirrorbot.nl/file/unpwuu2",
"https://gdmirrorbot.nl/file/w8oqevy",
"https://gdmirrorbot.nl/file/f31g1kb",
"https://gdmirrorbot.nl/file/gamnfj8",
"https://gdmirrorbot.nl/file/vgcyylt",
"https://gdmirrorbot.nl/file/kkbpnsx",
"https://gdmirrorbot.nl/file/g8ox4vv",
"https://gdmirrorbot.nl/file/b5ts4nw",
"https://gdmirrorbot.nl/file/zxv1szn",
"https://gdmirrorbot.nl/file/s1efpks",
"https://gdmirrorbot.nl/file/zzsuvx7",
"https://gdmirrorbot.nl/file/hz9992m",
"https://gdmirrorbot.nl/file/xcm2pkf",
"https://gdmirrorbot.nl/file/ypgoozw",
"https://gdmirrorbot.nl/file/qgfjhmy",
"https://gdmirrorbot.nl/file/eld32lr",
"https://gdmirrorbot.nl/file/p68jtop",
"https://gdmirrorbot.nl/file/b3xhse4",
"https://gdmirrorbot.nl/file/jg8h7u8",
"https://gdmirrorbot.nl/file/n1onncr",
"https://gdmirrorbot.nl/file/x9jxwek",
"https://gdmirrorbot.nl/file/odll3z8",
"https://gdmirrorbot.nl/file/g0c823n",
"https://gdmirrorbot.nl/file/di67ldp",
"https://gdmirrorbot.nl/file/te5403c",
"https://gdmirrorbot.nl/file/rl7ljdp",
"https://gdmirrorbot.nl/file/emnjs4w",
"https://gdmirrorbot.nl/file/e2ne4xr",
"https://gdmirrorbot.nl/file/q0it58i",
"https://gdmirrorbot.nl/file/k6exosp",
"https://gdmirrorbot.nl/file/p7v3o8h",
"https://gdmirrorbot.nl/file/sxphyeq",
"https://gdmirrorbot.nl/file/fbba64k",
"https://gdmirrorbot.nl/file/t9hwsbx",
"https://gdmirrorbot.nl/file/p5qr8ms",
"https://gdmirrorbot.nl/file/src88wk",
"https://gdmirrorbot.nl/file/sioi2yp",
"https://gdmirrorbot.nl/file/w621kfz",
"https://gdmirrorbot.nl/file/zoo28sk",
"https://gdmirrorbot.nl/file/r936fys",
"https://gdmirrorbot.nl/file/dfpg3sj",
"https://gdmirrorbot.nl/file/cw68jdz",
"https://gdmirrorbot.nl/file/kf9b9e2",
"https://gdmirrorbot.nl/file/ca0zc96",
"https://gdmirrorbot.nl/file/hnr61ds",
"https://gdmirrorbot.nl/file/s03nlvn",
"https://gdmirrorbot.nl/file/ywpgcq2",
"https://gdmirrorbot.nl/file/ws8lues",
"https://gdmirrorbot.nl/file/cwogt2r",
"https://gdmirrorbot.nl/file/x04ypdd",
"https://gdmirrorbot.nl/file/va5lwdz",
"https://gdmirrorbot.nl/file/lpkvpxh",
"https://gdmirrorbot.nl/file/grgjq83",
"https://gdmirrorbot.nl/file/hijua0q",
"https://gdmirrorbot.nl/file/nmqftmo",
"https://gdmirrorbot.nl/file/t5vue3p",
"https://gdmirrorbot.nl/file/zvuht9o",
"https://gdmirrorbot.nl/file/wkelz01",
"https://gdmirrorbot.nl/file/rj1cs4l",
"https://gdmirrorbot.nl/file/vyo215z",
"https://gdmirrorbot.nl/file/jd8i1p7",
"https://gdmirrorbot.nl/file/mk4jbna",
"https://gdmirrorbot.nl/file/yfn23ng",
"https://gdmirrorbot.nl/file/alunzkj",
"https://gdmirrorbot.nl/file/a9i22qc",
"https://gdmirrorbot.nl/file/p2qh39u",
"https://gdmirrorbot.nl/file/nqrq9yb",
"https://gdmirrorbot.nl/file/e3xo4e3",
"https://gdmirrorbot.nl/file/v1w8v4b",
"https://gdmirrorbot.nl/file/z5s2yvs",
"https://gdmirrorbot.nl/file/oyf15f6",
"https://gdmirrorbot.nl/file/krevrmx",
"https://gdmirrorbot.nl/file/cqvwmjg",
"https://gdmirrorbot.nl/file/bzw0w7a",
"https://gdmirrorbot.nl/file/eztnu69",
"https://gdmirrorbot.nl/file/bs9iep2",
"https://gdmirrorbot.nl/file/l6zeqo9",
"https://gdmirrorbot.nl/file/qcpdwik",
"https://gdmirrorbot.nl/file/h3l5dm3",
"https://gdmirrorbot.nl/file/j2cjbdh",
"https://gdmirrorbot.nl/file/ixf5zh1",
"https://gdmirrorbot.nl/file/v0gro1x",
"https://gdmirrorbot.nl/file/qktpldb",
"https://gdmirrorbot.nl/file/xwy1rrj",
"https://gdmirrorbot.nl/file/p42bono",
"https://gdmirrorbot.nl/file/z486zti",
"https://gdmirrorbot.nl/file/ny7rehz",
"https://gdmirrorbot.nl/file/kozrzbf",
"https://gdmirrorbot.nl/file/xkbb3gf",
"https://gdmirrorbot.nl/file/cwkwmqm",
"https://gdmirrorbot.nl/file/i7k610f",
"https://gdmirrorbot.nl/file/qj820hs",
"https://gdmirrorbot.nl/file/ixkf4tf",
"https://gdmirrorbot.nl/file/oqyacnv",
"https://gdmirrorbot.nl/file/pying3i",
"https://gdmirrorbot.nl/file/mrp99fm",
"https://gdmirrorbot.nl/file/mxdngc2",
"https://gdmirrorbot.nl/file/p09gur0",
"https://gdmirrorbot.nl/file/t14eg9c",
"https://gdmirrorbot.nl/file/hx8zu43",
"https://gdmirrorbot.nl/file/a90hvkz",
"https://gdmirrorbot.nl/file/g8rysdb",
"https://gdmirrorbot.nl/file/enidems",
"https://gdmirrorbot.nl/file/y0m47qz",
"https://gdmirrorbot.nl/file/df7httq",
"https://gdmirrorbot.nl/file/in0bzmj",
"https://gdmirrorbot.nl/file/nyacwy9",
"https://gdmirrorbot.nl/file/buuj38a",
"https://gdmirrorbot.nl/file/odluvu6",
"https://gdmirrorbot.nl/file/qvm9r7j",
"https://gdmirrorbot.nl/file/w5yvhu5",
"https://gdmirrorbot.nl/file/lseg2f9",
"https://gdmirrorbot.nl/file/qhwybem",
"https://gdmirrorbot.nl/file/g1y0hwd",
"https://gdmirrorbot.nl/file/w2fisql",
"https://gdmirrorbot.nl/file/meuvgbc",
"https://gdmirrorbot.nl/file/j9r56ts",
"https://gdmirrorbot.nl/file/cydl8yd",
"https://gdmirrorbot.nl/file/x6mto9o",
"https://gdmirrorbot.nl/file/yptw0ec",
"https://gdmirrorbot.nl/file/jlr2e8g",
"https://gdmirrorbot.nl/file/cki4i2s",
"https://gdmirrorbot.nl/file/nic4x7w",
"https://gdmirrorbot.nl/file/zsm4jzj",
"https://gdmirrorbot.nl/file/f02zf1z",
"https://gdmirrorbot.nl/file/f70tlqm",
"https://gdmirrorbot.nl/file/fp5l9kf",
"https://gdmirrorbot.nl/file/dwoi1qw",
"https://gdmirrorbot.nl/file/st9r1a4",
"https://gdmirrorbot.nl/file/kv7mlmb",
"https://gdmirrorbot.nl/file/vc40ti8"
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
    print("Waiting for 55 sec before proceeding to the next URL...")
    time.sleep(55)  # Wait for 30 sec

# Close the WebDriver
print("Closing the WebDriver...")
driver.quit()
print("Done.")
