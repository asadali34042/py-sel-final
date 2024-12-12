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
"https://gdmirrorbot.nl/file/txy654b",
"https://gdmirrorbot.nl/file/qbym1hf",
"https://gdmirrorbot.nl/file/zdie2ot",
"https://gdmirrorbot.nl/file/w2ov4sw",
"https://gdmirrorbot.nl/file/uq8iwma",
"https://gdmirrorbot.nl/file/vgoo5bg",
"https://gdmirrorbot.nl/file/jhm9lk4",
"https://gdmirrorbot.nl/file/kofudkv",
"https://gdmirrorbot.nl/file/ixpvsqr",
"https://gdmirrorbot.nl/file/a2rcfu2",
"https://gdmirrorbot.nl/file/s8zagcq",
"https://gdmirrorbot.nl/file/muwy4yg",
"https://gdmirrorbot.nl/file/fojj4y1",
"https://gdmirrorbot.nl/file/i01crr4",
"https://gdmirrorbot.nl/file/gj7qi02",
"https://gdmirrorbot.nl/file/e0j6xrn",
"https://gdmirrorbot.nl/file/m0ig8k7",
"https://gdmirrorbot.nl/file/ehbyc18",
"https://gdmirrorbot.nl/file/odskldp",
"https://gdmirrorbot.nl/file/andsk41",
"https://gdmirrorbot.nl/file/eqwv3uv",
"https://gdmirrorbot.nl/file/wqywls0",
"https://gdmirrorbot.nl/file/p4b3wal",
"https://gdmirrorbot.nl/file/apzkfl8",
"https://gdmirrorbot.nl/file/u987rvq",
"https://gdmirrorbot.nl/file/nhx89tn",
"https://gdmirrorbot.nl/file/g0giju0",
"https://gdmirrorbot.nl/file/d1zgng0",
"https://gdmirrorbot.nl/file/y3b2lq1",
"https://gdmirrorbot.nl/file/exfuqka",
"https://gdmirrorbot.nl/file/b6t840u",
"https://gdmirrorbot.nl/file/sgp9igb",
"https://gdmirrorbot.nl/file/l7j5n8t",
"https://gdmirrorbot.nl/file/us8eqei",
"https://gdmirrorbot.nl/file/nbm0e8j",
"https://gdmirrorbot.nl/file/ixdx1s7",
"https://gdmirrorbot.nl/file/ssri2dk",
"https://gdmirrorbot.nl/file/ky2k7of",
"https://gdmirrorbot.nl/file/puojcx8",
"https://gdmirrorbot.nl/file/kug913v",
"https://gdmirrorbot.nl/file/e37dl5e",
"https://gdmirrorbot.nl/file/zsvtoqy",
"https://gdmirrorbot.nl/file/yaofgje",
"https://gdmirrorbot.nl/file/wrr8jfa",
"https://gdmirrorbot.nl/file/gvk7o9s",
"https://gdmirrorbot.nl/file/its43d1",
"https://gdmirrorbot.nl/file/i7bcp96",
"https://gdmirrorbot.nl/file/g3owuwv",
"https://gdmirrorbot.nl/file/zqzzhhs",
"https://gdmirrorbot.nl/file/f9tk80i",
"https://gdmirrorbot.nl/file/mks04ib",
"https://gdmirrorbot.nl/file/f4tuokn",
"https://gdmirrorbot.nl/file/c3ceguq",
"https://gdmirrorbot.nl/file/npu2je1",
"https://gdmirrorbot.nl/file/i1gdwfk",
"https://gdmirrorbot.nl/file/r8q1d0s",
"https://gdmirrorbot.nl/file/sgu9lmk",
"https://gdmirrorbot.nl/file/b88u14e",
"https://gdmirrorbot.nl/file/eyyb7ps",
"https://gdmirrorbot.nl/file/px4fz2c",
"https://gdmirrorbot.nl/file/d9f567s",
"https://gdmirrorbot.nl/file/l0bl7aj",
"https://gdmirrorbot.nl/file/z7switv",
"https://gdmirrorbot.nl/file/ce0nkrr",
"https://gdmirrorbot.nl/file/hftjdfh",
"https://gdmirrorbot.nl/file/ust8jgr",
"https://gdmirrorbot.nl/file/vi6q1h0",
"https://gdmirrorbot.nl/file/eblzxg1",
"https://gdmirrorbot.nl/file/bz28gh7",
"https://gdmirrorbot.nl/file/uj7fyfu",
"https://gdmirrorbot.nl/file/ca9hika",
"https://gdmirrorbot.nl/file/tmnflnt",
"https://gdmirrorbot.nl/file/goffkkb",
"https://gdmirrorbot.nl/file/utmbvdn",
"https://gdmirrorbot.nl/file/pdyfzvp",
"https://gdmirrorbot.nl/file/wwsj0nn",
"https://gdmirrorbot.nl/file/o4s6j41",
"https://gdmirrorbot.nl/file/rwd0ere",
"https://gdmirrorbot.nl/file/pnmdbku",
"https://gdmirrorbot.nl/file/ff102ke",
"https://gdmirrorbot.nl/file/r4tfe5w",
"https://gdmirrorbot.nl/file/gjab5t7",
"https://gdmirrorbot.nl/file/gtkpbs4",
"https://gdmirrorbot.nl/file/usj30tm",
"https://gdmirrorbot.nl/file/pn8uw0u",
"https://gdmirrorbot.nl/file/utiakel",
"https://gdmirrorbot.nl/file/cfpmt48",
"https://gdmirrorbot.nl/file/oht560v",
"https://gdmirrorbot.nl/file/cj7jlws",
"https://gdmirrorbot.nl/file/bl55ekf",
"https://gdmirrorbot.nl/file/e9o9lkh",
"https://gdmirrorbot.nl/file/e57y2i3",
"https://gdmirrorbot.nl/file/ow2kay8",
"https://gdmirrorbot.nl/file/mblgzoj",
"https://gdmirrorbot.nl/file/fo623w7",
"https://gdmirrorbot.nl/file/bg362u4",
"https://gdmirrorbot.nl/file/wrcwpc1",
"https://gdmirrorbot.nl/file/i2sb0k9",
"https://gdmirrorbot.nl/file/fvlu3yv",
"https://gdmirrorbot.nl/file/y49hd8h",
"https://gdmirrorbot.nl/file/e9o8x5g",
"https://gdmirrorbot.nl/file/zjkob8t",
"https://gdmirrorbot.nl/file/z4t2usf",
"https://gdmirrorbot.nl/file/jdxsn39",
"https://gdmirrorbot.nl/file/vlxibp4",
"https://gdmirrorbot.nl/file/mbi0er7",
"https://gdmirrorbot.nl/file/xjj3y4q",
"https://gdmirrorbot.nl/file/wiolpex",
"https://gdmirrorbot.nl/file/e070krm",
"https://gdmirrorbot.nl/file/ae9uxnh",
"https://gdmirrorbot.nl/file/yuy9ym5",
"https://gdmirrorbot.nl/file/p5ce8jl",
"https://gdmirrorbot.nl/file/f68z2x0",
"https://gdmirrorbot.nl/file/a06dz6a",
"https://gdmirrorbot.nl/file/ege7d69",
"https://gdmirrorbot.nl/file/allq4x2",
"https://gdmirrorbot.nl/file/kxhyy3f",
"https://gdmirrorbot.nl/file/rum9g7d",
"https://gdmirrorbot.nl/file/k4vsczs",
"https://gdmirrorbot.nl/file/n0huxxp",
"https://gdmirrorbot.nl/file/vtx5ok7",
"https://gdmirrorbot.nl/file/c57ugsa",
"https://gdmirrorbot.nl/file/lap5ayr",
"https://gdmirrorbot.nl/file/stvgqxp",
"https://gdmirrorbot.nl/file/wj539py",
"https://gdmirrorbot.nl/file/ugh51cf",
"https://gdmirrorbot.nl/file/xmm1i65",
"https://gdmirrorbot.nl/file/nxdic4v",
"https://gdmirrorbot.nl/file/srzk11f",
"https://gdmirrorbot.nl/file/rd3ich4",
"https://gdmirrorbot.nl/file/arhlrdy",
"https://gdmirrorbot.nl/file/c460d8w",
"https://gdmirrorbot.nl/file/w75kx10",
"https://gdmirrorbot.nl/file/s70jsf6",
"https://gdmirrorbot.nl/file/ynxe2p6",
"https://gdmirrorbot.nl/file/jzh9wr0",
"https://gdmirrorbot.nl/file/sm8jy6o",
"https://gdmirrorbot.nl/file/im2jbpp",
"https://gdmirrorbot.nl/file/egfjdmf",
"https://gdmirrorbot.nl/file/h728wnn",
"https://gdmirrorbot.nl/file/c2p07ez",
"https://gdmirrorbot.nl/file/p68huke",
"https://gdmirrorbot.nl/file/w90unju",
"https://gdmirrorbot.nl/file/yqc7pw2",
"https://gdmirrorbot.nl/file/j49lxgd",
"https://gdmirrorbot.nl/file/dv1krf6",
"https://gdmirrorbot.nl/file/vv4vffj",
"https://gdmirrorbot.nl/file/g07bjp4",
"https://gdmirrorbot.nl/file/v87zpto",
"https://gdmirrorbot.nl/file/xo5nhtg",
"https://gdmirrorbot.nl/file/al8br6k",
"https://gdmirrorbot.nl/file/w1t124e",
"https://gdmirrorbot.nl/file/i5d9uh4",
"https://gdmirrorbot.nl/file/zc1qjw6",
"https://gdmirrorbot.nl/file/k986fh7",
"https://gdmirrorbot.nl/file/yatq3ix",
"https://gdmirrorbot.nl/file/dns1psu",
"https://gdmirrorbot.nl/file/uzrta7m",
"https://gdmirrorbot.nl/file/dsklyfx",
"https://gdmirrorbot.nl/file/pkt6f0k",
"https://gdmirrorbot.nl/file/biq5dwn",
"https://gdmirrorbot.nl/file/qjt83c4",
"https://gdmirrorbot.nl/file/a4m17cc",
"https://gdmirrorbot.nl/file/rtg1rp6",
"https://gdmirrorbot.nl/file/q31lgu9",
"https://gdmirrorbot.nl/file/jdnnyrm",
"https://gdmirrorbot.nl/file/bwwxcw5",
"https://gdmirrorbot.nl/file/eo0dc35",
"https://gdmirrorbot.nl/file/zxdxujm",
"https://gdmirrorbot.nl/file/ankmxt5",
"https://gdmirrorbot.nl/file/q83y3y0",
"https://gdmirrorbot.nl/file/ytta37w",
"https://gdmirrorbot.nl/file/g8lmm4u",
"https://gdmirrorbot.nl/file/tz99nup",
"https://gdmirrorbot.nl/file/x0i9xco",
"https://gdmirrorbot.nl/file/w3z5qyc",
"https://gdmirrorbot.nl/file/iwf726z",
"https://gdmirrorbot.nl/file/meetiih",
"https://gdmirrorbot.nl/file/r1oxvn0",
"https://gdmirrorbot.nl/file/c2l0jzx",
"https://gdmirrorbot.nl/file/md4i059",
"https://gdmirrorbot.nl/file/rfvkbtg",
"https://gdmirrorbot.nl/file/v583brt",
"https://gdmirrorbot.nl/file/ot8o2i0",
"https://gdmirrorbot.nl/file/q8oaoto",
"https://gdmirrorbot.nl/file/xchxrhu",
"https://gdmirrorbot.nl/file/a7v5mhx",
"https://gdmirrorbot.nl/file/z4e7wbi",
"https://gdmirrorbot.nl/file/rhqtewm",
"https://gdmirrorbot.nl/file/wk9r81o",
"https://gdmirrorbot.nl/file/opldo86",
"https://gdmirrorbot.nl/file/k3j9nce",
"https://gdmirrorbot.nl/file/fndo4fe",
"https://gdmirrorbot.nl/file/yf20w3u",
"https://gdmirrorbot.nl/file/r7ngc9w",
"https://gdmirrorbot.nl/file/x4kklhh",
"https://gdmirrorbot.nl/file/yaaa3wj",
"https://gdmirrorbot.nl/file/w1shgfx",
"https://gdmirrorbot.nl/file/yqhtne7",
"https://gdmirrorbot.nl/file/xs7qwpm",
"https://gdmirrorbot.nl/file/t5r55o3",
"https://gdmirrorbot.nl/file/ya8wre3",
"https://gdmirrorbot.nl/file/u73xqra",
"https://gdmirrorbot.nl/file/w66wg5l",
"https://gdmirrorbot.nl/file/ftzxuh4",
"https://gdmirrorbot.nl/file/shj3m9o",
"https://gdmirrorbot.nl/file/u70t21r",
"https://gdmirrorbot.nl/file/bosh0xg",
"https://gdmirrorbot.nl/file/p0ire67",
"https://gdmirrorbot.nl/file/z7ic0im",
"https://gdmirrorbot.nl/file/ucyyux5",
"https://gdmirrorbot.nl/file/hdjf4co",
"https://gdmirrorbot.nl/file/scg1fye",
"https://gdmirrorbot.nl/file/d32dezj",
"https://gdmirrorbot.nl/file/pu8853m",
"https://gdmirrorbot.nl/file/dtka1ha",
"https://gdmirrorbot.nl/file/utkzemv",
"https://gdmirrorbot.nl/file/jug0g84",
"https://gdmirrorbot.nl/file/zlpuc03",
"https://gdmirrorbot.nl/file/w7xtmit",
"https://gdmirrorbot.nl/file/cvm6rog",
"https://gdmirrorbot.nl/file/n5g9qul",
"https://gdmirrorbot.nl/file/i86gvxs",
"https://gdmirrorbot.nl/file/anipsdq",
"https://gdmirrorbot.nl/file/o0ms36n",
"https://gdmirrorbot.nl/file/yfzimta",
"https://gdmirrorbot.nl/file/tycmboe",
"https://gdmirrorbot.nl/file/u9uz3dd",
"https://gdmirrorbot.nl/file/gnw1xeh",
"https://gdmirrorbot.nl/file/b3ckjmc",
"https://gdmirrorbot.nl/file/y2rwpd6",
"https://gdmirrorbot.nl/file/hx2u5cg",
"https://gdmirrorbot.nl/file/fa49e13",
"https://gdmirrorbot.nl/file/mlzdkg9",
"https://gdmirrorbot.nl/file/uog8oe7",
"https://gdmirrorbot.nl/file/ldm1rwm",
"https://gdmirrorbot.nl/file/iyr4b7p",
"https://gdmirrorbot.nl/file/t1qakvt",
"https://gdmirrorbot.nl/file/ujxj7nr",
"https://gdmirrorbot.nl/file/wpywskf",
"https://gdmirrorbot.nl/file/ert673m",
"https://gdmirrorbot.nl/file/ykrrqcf",
"https://gdmirrorbot.nl/file/ccwfggv",
"https://gdmirrorbot.nl/file/w1y8omw",
"https://gdmirrorbot.nl/file/n5eo91o",
"https://gdmirrorbot.nl/file/yxbjjt9",
"https://gdmirrorbot.nl/file/a4tooys",
"https://gdmirrorbot.nl/file/se647so",
"https://gdmirrorbot.nl/file/vws919q",
"https://gdmirrorbot.nl/file/eujdy49",
"https://gdmirrorbot.nl/file/jzu9d4l",
"https://gdmirrorbot.nl/file/k995gdm",
"https://gdmirrorbot.nl/file/ch49gvn",
"https://gdmirrorbot.nl/file/mjtqd9w",
"https://gdmirrorbot.nl/file/vszffnk",
"https://gdmirrorbot.nl/file/e49v8cp",
"https://gdmirrorbot.nl/file/li6ky86",
"https://gdmirrorbot.nl/file/db1z1d5",
"https://gdmirrorbot.nl/file/w9mprgp",
"https://gdmirrorbot.nl/file/eo15gb8",
"https://gdmirrorbot.nl/file/jvd3m6f",
"https://gdmirrorbot.nl/file/fblh7ne",
"https://gdmirrorbot.nl/file/xf7s3rx",
"https://gdmirrorbot.nl/file/s07dcol",
"https://gdmirrorbot.nl/file/rr7k4cn",
"https://gdmirrorbot.nl/file/vtbivus",
"https://gdmirrorbot.nl/file/mjgyuex",
"https://gdmirrorbot.nl/file/z7tbrrm",
"https://gdmirrorbot.nl/file/ehf4pjt",
"https://gdmirrorbot.nl/file/dvnuha0",
"https://gdmirrorbot.nl/file/y4jukmf",
"https://gdmirrorbot.nl/file/s7qjjmn",
"https://gdmirrorbot.nl/file/g1kjtdu",
"https://gdmirrorbot.nl/file/ghs15zc",
"https://gdmirrorbot.nl/file/arprsqq",
"https://gdmirrorbot.nl/file/k80cj8q",
"https://gdmirrorbot.nl/file/p9kmi6m",
"https://gdmirrorbot.nl/file/f8wux40",
"https://gdmirrorbot.nl/file/p1zry21",
"https://gdmirrorbot.nl/file/vmnepkb",
"https://gdmirrorbot.nl/file/cifyw6x",
"https://gdmirrorbot.nl/file/v0jvgw7",
"https://gdmirrorbot.nl/file/u1uduof",
"https://gdmirrorbot.nl/file/peos0r5",
"https://gdmirrorbot.nl/file/b5x2034",
"https://gdmirrorbot.nl/file/bpx0w8u",
"https://gdmirrorbot.nl/file/hwtp4fy",
"https://gdmirrorbot.nl/file/mzcze9m",
"https://gdmirrorbot.nl/file/ukmff8d",
"https://gdmirrorbot.nl/file/ds6phip",
"https://gdmirrorbot.nl/file/wn6znpx",
"https://gdmirrorbot.nl/file/p9r51zd",
"https://gdmirrorbot.nl/file/t7uybhe",
"https://gdmirrorbot.nl/file/acb9a4y",
"https://gdmirrorbot.nl/file/aat008c",
"https://gdmirrorbot.nl/file/rtt1ap5",
"https://gdmirrorbot.nl/file/ko7qirv",
"https://gdmirrorbot.nl/file/nzb4e18",
"https://gdmirrorbot.nl/file/ketwo6g",
"https://gdmirrorbot.nl/file/icujzh2",
"https://gdmirrorbot.nl/file/sdcg2pe",
"https://gdmirrorbot.nl/file/vg716dz",
"https://gdmirrorbot.nl/file/alsfr3o",
"https://gdmirrorbot.nl/file/nydftx5",
"https://gdmirrorbot.nl/file/aciugox",
"https://gdmirrorbot.nl/file/jra4a8a",
"https://gdmirrorbot.nl/file/voy2ds3",
"https://gdmirrorbot.nl/file/rh2hcn3",
"https://gdmirrorbot.nl/file/s24rgqh",
"https://gdmirrorbot.nl/file/zgw51g2",
"https://gdmirrorbot.nl/file/zjppjzt",
"https://gdmirrorbot.nl/file/huv1zey",
"https://gdmirrorbot.nl/file/eawkjxp",
"https://gdmirrorbot.nl/file/wlgkcpy",
"https://gdmirrorbot.nl/file/ibc0owx",
"https://gdmirrorbot.nl/file/r5j8ij7",
"https://gdmirrorbot.nl/file/y0lvps8",
"https://gdmirrorbot.nl/file/hcqnnhr",
"https://gdmirrorbot.nl/file/r5dkdsu",
"https://gdmirrorbot.nl/file/wj6jx7g",
"https://gdmirrorbot.nl/file/hkr7jl0",
"https://gdmirrorbot.nl/file/a7ryk8s",
"https://gdmirrorbot.nl/file/hdxqlsr",
"https://gdmirrorbot.nl/file/wb32av9",
"https://gdmirrorbot.nl/file/k2ioe0c",
"https://gdmirrorbot.nl/file/zgio7p7",
"https://gdmirrorbot.nl/file/zvbtopl",
"https://gdmirrorbot.nl/file/xmrtl03",
"https://gdmirrorbot.nl/file/l4xvusp",
"https://gdmirrorbot.nl/file/z4pzzvr",
"https://gdmirrorbot.nl/file/gpqzvp5",
"https://gdmirrorbot.nl/file/q399lnk",
"https://gdmirrorbot.nl/file/fsk7bwp",
"https://gdmirrorbot.nl/file/k2vcb6w",
"https://gdmirrorbot.nl/file/uew4p3k",
"https://gdmirrorbot.nl/file/f2swbgq",
"https://gdmirrorbot.nl/file/s6ehr5h",
"https://gdmirrorbot.nl/file/o0u7tuk",
"https://gdmirrorbot.nl/file/x1y9a8k",
"https://gdmirrorbot.nl/file/nczcka9",
"https://gdmirrorbot.nl/file/t9lp5cc",
"https://gdmirrorbot.nl/file/belqmga",
"https://gdmirrorbot.nl/file/i5gc4ac",
"https://gdmirrorbot.nl/file/a68hhw6",
"https://gdmirrorbot.nl/file/zs7obnk",
"https://gdmirrorbot.nl/file/j8xyrz7",
"https://gdmirrorbot.nl/file/rhtl01v",
"https://gdmirrorbot.nl/file/dpr1gls",
"https://gdmirrorbot.nl/file/dad30yk",
"https://gdmirrorbot.nl/file/hc8n1ea",
"https://gdmirrorbot.nl/file/mv63v9m",
"https://gdmirrorbot.nl/file/eezk526",
"https://gdmirrorbot.nl/file/luu1hja",
"https://gdmirrorbot.nl/file/rw3h9r8",
"https://gdmirrorbot.nl/file/yjnukyr",
"https://gdmirrorbot.nl/file/r54xnr4",
"https://gdmirrorbot.nl/file/xpk640j",
"https://gdmirrorbot.nl/file/wpdz2o0",
"https://gdmirrorbot.nl/file/bzj2cf0",
"https://gdmirrorbot.nl/file/vhunrpb",
"https://gdmirrorbot.nl/file/d9e1tpa",
"https://gdmirrorbot.nl/file/jzy14xw",
"https://gdmirrorbot.nl/file/p937wso",
"https://gdmirrorbot.nl/file/vv1hbn3",
"https://gdmirrorbot.nl/file/mbimyh6",
"https://gdmirrorbot.nl/file/eqwm4nf",
"https://gdmirrorbot.nl/file/xfn9pzb",
"https://gdmirrorbot.nl/file/bezhi4f",
"https://gdmirrorbot.nl/file/wnr851f",
"https://gdmirrorbot.nl/file/ze9r0lj",
"https://gdmirrorbot.nl/file/kiuyb7n",
"https://gdmirrorbot.nl/file/dyehn50",
"https://gdmirrorbot.nl/file/p7u0toe",
"https://gdmirrorbot.nl/file/gm6r3py",
"https://gdmirrorbot.nl/file/xua3ate",
"https://gdmirrorbot.nl/file/pnqk9hf",
"https://gdmirrorbot.nl/file/htkp33s",
"https://gdmirrorbot.nl/file/bmzgtmr",
"https://gdmirrorbot.nl/file/gl5i96s",
"https://gdmirrorbot.nl/file/lpiv5jq",
"https://gdmirrorbot.nl/file/suwzddt",
"https://gdmirrorbot.nl/file/txc1rfe",
"https://gdmirrorbot.nl/file/yizez0a",
"https://gdmirrorbot.nl/file/ftm9hz2",
"https://gdmirrorbot.nl/file/pp7bti1",
"https://gdmirrorbot.nl/file/wyzzyzp",
"https://gdmirrorbot.nl/file/ddsjr1h",
"https://gdmirrorbot.nl/file/i42ert4",
"https://gdmirrorbot.nl/file/itlz7pz",
"https://gdmirrorbot.nl/file/m2jzvqn",
"https://gdmirrorbot.nl/file/ud8wymg",
"https://gdmirrorbot.nl/file/mz7xll7",
"https://gdmirrorbot.nl/file/mb2deuh",
"https://gdmirrorbot.nl/file/l4gtf0y",
"https://gdmirrorbot.nl/file/oo2udwy",
"https://gdmirrorbot.nl/file/oey7wy5",
"https://gdmirrorbot.nl/file/jqm26eq",
"https://gdmirrorbot.nl/file/f8ouscf",
"https://gdmirrorbot.nl/file/ueor8ej",
"https://gdmirrorbot.nl/file/yngn6c8",
"https://gdmirrorbot.nl/file/ju09f25",
"https://gdmirrorbot.nl/file/af0l9fr",
"https://gdmirrorbot.nl/file/eqkyrsu",
"https://gdmirrorbot.nl/file/qeanguh",
"https://gdmirrorbot.nl/file/xi3pxqk",
"https://gdmirrorbot.nl/file/gwrb4ah",
"https://gdmirrorbot.nl/file/ci6eirp",
"https://gdmirrorbot.nl/file/gkrn31e",
"https://gdmirrorbot.nl/file/jd0mars",
"https://gdmirrorbot.nl/file/vzqmt2t",
"https://gdmirrorbot.nl/file/rkliqcd",
"https://gdmirrorbot.nl/file/mxqitlm",
"https://gdmirrorbot.nl/file/htop6eb",
"https://gdmirrorbot.nl/file/gs0jwq0",
"https://gdmirrorbot.nl/file/v6ota4y",
"https://gdmirrorbot.nl/file/teflacu",
"https://gdmirrorbot.nl/file/s1e23qs",
"https://gdmirrorbot.nl/file/zj52i9d",
"https://gdmirrorbot.nl/file/ncjlr30",
"https://gdmirrorbot.nl/file/vyqhbyf",
"https://gdmirrorbot.nl/file/sp2p688",
"https://gdmirrorbot.nl/file/ykjdkpy",
"https://gdmirrorbot.nl/file/fqzmpiq",
"https://gdmirrorbot.nl/file/y3gvp2b",
"https://gdmirrorbot.nl/file/m1ighrk",
"https://gdmirrorbot.nl/file/qsvizco",
"https://gdmirrorbot.nl/file/q41ogsn",
"https://gdmirrorbot.nl/file/kmfva7s",
"https://gdmirrorbot.nl/file/fz13ici",
"https://gdmirrorbot.nl/file/wyll2dr",
"https://gdmirrorbot.nl/file/wki1vjw",
"https://gdmirrorbot.nl/file/bceudz6",
"https://gdmirrorbot.nl/file/xcz7z4h",
"https://gdmirrorbot.nl/file/e7wep9i",
"https://gdmirrorbot.nl/file/ejmwyh8",
"https://gdmirrorbot.nl/file/nap0l6t",
"https://gdmirrorbot.nl/file/c33pc7j",
"https://gdmirrorbot.nl/file/f56lauu",
"https://gdmirrorbot.nl/file/wmi55f6",
"https://gdmirrorbot.nl/file/klysajx",
"https://gdmirrorbot.nl/file/ug27bua",
"https://gdmirrorbot.nl/file/jgkq4pz",
"https://gdmirrorbot.nl/file/ny8jyej",
"https://gdmirrorbot.nl/file/ggkumjq",
"https://gdmirrorbot.nl/file/xe498tc",
"https://gdmirrorbot.nl/file/npd0i7v",
"https://gdmirrorbot.nl/file/k7e8yol",
"https://gdmirrorbot.nl/file/s40wz1t",
"https://gdmirrorbot.nl/file/uhuudt9",
"https://gdmirrorbot.nl/file/cob8y04",
"https://gdmirrorbot.nl/file/yaw62fh",
"https://gdmirrorbot.nl/file/cck3obu",
"https://gdmirrorbot.nl/file/jmu1tq6",
"https://gdmirrorbot.nl/file/jfydvcr",
"https://gdmirrorbot.nl/file/mrth4o4",
"https://gdmirrorbot.nl/file/bs82c9x",
"https://gdmirrorbot.nl/file/fv6zmi3",
"https://gdmirrorbot.nl/file/yrs3ria",
"https://gdmirrorbot.nl/file/zkyjx5m",
"https://gdmirrorbot.nl/file/t22hl5j",
"https://gdmirrorbot.nl/file/ddb9hyz",
"https://gdmirrorbot.nl/file/onidy5a",
"https://gdmirrorbot.nl/file/mql77gq",
"https://gdmirrorbot.nl/file/wo6eqse",
"https://gdmirrorbot.nl/file/i4pukt7",
"https://gdmirrorbot.nl/file/rbizyza",
"https://gdmirrorbot.nl/file/rcmz55q",
"https://gdmirrorbot.nl/file/wo6ra0g",
"https://gdmirrorbot.nl/file/mo40jkr",
"https://gdmirrorbot.nl/file/hd9pwji",
"https://gdmirrorbot.nl/file/o2pwbsn",
"https://gdmirrorbot.nl/file/gu3n5bt",
"https://gdmirrorbot.nl/file/hm6mxy7",
"https://gdmirrorbot.nl/file/d6ntn6x",
"https://gdmirrorbot.nl/file/jjrdwiq",
"https://gdmirrorbot.nl/file/m3a0lw8",
"https://gdmirrorbot.nl/file/p8izdbp",
"https://gdmirrorbot.nl/file/k4jrap4",
"https://gdmirrorbot.nl/file/rsvhy5n",
"https://gdmirrorbot.nl/file/okmji1w",
"https://gdmirrorbot.nl/file/dur3rpr",
"https://gdmirrorbot.nl/file/m60b7x5",
"https://gdmirrorbot.nl/file/omez22l",
"https://gdmirrorbot.nl/file/v6iftf4",
"https://gdmirrorbot.nl/file/a0eqeio",
"https://gdmirrorbot.nl/file/c8i7oga",
"https://gdmirrorbot.nl/file/c5lanj9",
"https://gdmirrorbot.nl/file/mqqn8b6",
"https://gdmirrorbot.nl/file/tpfcinm",
"https://gdmirrorbot.nl/file/pun2z55",
"https://gdmirrorbot.nl/file/y9awxvg",
"https://gdmirrorbot.nl/file/qbyxxrm",
"https://gdmirrorbot.nl/file/udz7cc2",
"https://gdmirrorbot.nl/file/mdf6t2q",
"https://gdmirrorbot.nl/file/ovb1vg0",
"https://gdmirrorbot.nl/file/e2ko8k4",
"https://gdmirrorbot.nl/file/j1svse4",
"https://gdmirrorbot.nl/file/vo0cgqs",
"https://gdmirrorbot.nl/file/rqgvruz",
"https://gdmirrorbot.nl/file/sw4dqw0",
"https://gdmirrorbot.nl/file/ik7zq8c",
"https://gdmirrorbot.nl/file/o4ot4fl",
"https://gdmirrorbot.nl/file/h3t5woo",
"https://gdmirrorbot.nl/file/wzqagri",
"https://gdmirrorbot.nl/file/vzfw3c9",
"https://gdmirrorbot.nl/file/x2rg37d",
"https://gdmirrorbot.nl/file/wwxrav3",
"https://gdmirrorbot.nl/file/rqqdg1h",
"https://gdmirrorbot.nl/file/rf5sp93",
"https://gdmirrorbot.nl/file/hy8nwvv",
"https://gdmirrorbot.nl/file/l27ne5p",
"https://gdmirrorbot.nl/file/if61yko",
"https://gdmirrorbot.nl/file/q4kx1a9",
"https://gdmirrorbot.nl/file/onj0ati",
"https://gdmirrorbot.nl/file/vkwhuxw",
"https://gdmirrorbot.nl/file/nxm0x1v",
"https://gdmirrorbot.nl/file/aeavfr2",
"https://gdmirrorbot.nl/file/f0gfciz",
"https://gdmirrorbot.nl/file/fec253h",
"https://gdmirrorbot.nl/file/hher9pi",
"https://gdmirrorbot.nl/file/fqjgcre",
"https://gdmirrorbot.nl/file/hw1jx47",
"https://gdmirrorbot.nl/file/rbvyz48",
"https://gdmirrorbot.nl/file/wd1slnb",
"https://gdmirrorbot.nl/file/ibdluvl",
"https://gdmirrorbot.nl/file/w7capkj",
"https://gdmirrorbot.nl/file/vsgdvtr",
"https://gdmirrorbot.nl/file/ljkwsyp",
"https://gdmirrorbot.nl/file/uny0znf",
"https://gdmirrorbot.nl/file/hue2907",
"https://gdmirrorbot.nl/file/ahtdamu",
"https://gdmirrorbot.nl/file/ld0l1ci",
"https://gdmirrorbot.nl/file/zzv3v45",
"https://gdmirrorbot.nl/file/iqlzjak",
"https://gdmirrorbot.nl/file/xfvj9iy",
"https://gdmirrorbot.nl/file/pfz847v",
"https://gdmirrorbot.nl/file/bjk88up",
"https://gdmirrorbot.nl/file/kuvqg9v",
"https://gdmirrorbot.nl/file/s3hir13",
"https://gdmirrorbot.nl/file/gv6doo8",
"https://gdmirrorbot.nl/file/f0mxk8i",
"https://gdmirrorbot.nl/file/l09yzmj",
"https://gdmirrorbot.nl/file/qijqvsg",
"https://gdmirrorbot.nl/file/c48bka0",
"https://gdmirrorbot.nl/file/i17y7y5",
"https://gdmirrorbot.nl/file/jzartz9",
"https://gdmirrorbot.nl/file/ldri1zc",
"https://gdmirrorbot.nl/file/wap3caz",
"https://gdmirrorbot.nl/file/dmxe49g",
"https://gdmirrorbot.nl/file/rag3sgy",
"https://gdmirrorbot.nl/file/j5ppbpd",
"https://gdmirrorbot.nl/file/rj1rlhb",
"https://gdmirrorbot.nl/file/olyoru4",
"https://gdmirrorbot.nl/file/zu3y3z9",
"https://gdmirrorbot.nl/file/st58p7b",
"https://gdmirrorbot.nl/file/e49akae",
"https://gdmirrorbot.nl/file/ozsytbz",
"https://gdmirrorbot.nl/file/xcirjnz",
"https://gdmirrorbot.nl/file/pxe1ubb",
"https://gdmirrorbot.nl/file/jc1c1tn",
"https://gdmirrorbot.nl/file/jom2ug1",
"https://gdmirrorbot.nl/file/yeqrn9e",
"https://gdmirrorbot.nl/file/cl7qpwr",
"https://gdmirrorbot.nl/file/mjjhnbn",
"https://gdmirrorbot.nl/file/g7gr2ly",
"https://gdmirrorbot.nl/file/s2mlfvg",
"https://gdmirrorbot.nl/file/us0krqr",
"https://gdmirrorbot.nl/file/wm6onhx",
"https://gdmirrorbot.nl/file/pmyfoo2",
"https://gdmirrorbot.nl/file/pfta8ah",
"https://gdmirrorbot.nl/file/x00cp12",
"https://gdmirrorbot.nl/file/naml3jy",
"https://gdmirrorbot.nl/file/tg9lsn2",
"https://gdmirrorbot.nl/file/wtueiug",
"https://gdmirrorbot.nl/file/bjx847c",
"https://gdmirrorbot.nl/file/txu3sak",
"https://gdmirrorbot.nl/file/kvf86tj",
"https://gdmirrorbot.nl/file/yaoun38",
"https://gdmirrorbot.nl/file/bhk2bfk",
"https://gdmirrorbot.nl/file/msc8bgt",
"https://gdmirrorbot.nl/file/qst3u43",
"https://gdmirrorbot.nl/file/cfwrppl",
"https://gdmirrorbot.nl/file/itigtn5",
"https://gdmirrorbot.nl/file/q7kj80m",
"https://gdmirrorbot.nl/file/k0ga3lu",
"https://gdmirrorbot.nl/file/mzerqzn",
"https://gdmirrorbot.nl/file/gq4kg6e",
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
