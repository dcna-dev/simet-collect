import csv
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the url
url = 'https://beta.simet.nic.br'

# Set Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--incognito") # Open as incognito window
prefs = {"profile.default_content_setting_values.geolocation" :2} # Set allow to share location
chrome_options.add_experimental_option("prefs",prefs) # Set allow to share location
browser = Chrome(chrome_options=chrome_options) # Pass the options to browser

# Set a timeout
wait = WebDriverWait(browser, 10000)

#Set vars
data = [] # var to store the values
columns = ["down_speed", "down_unit", "up_speed", "up_unit", "ping",
           "ping_unit", "lost_pkts", "jitter", "jitter_unit" "date", "hour"    ] # Headers for csv file

# Selectors to find the elements
ping_selector = "#rttResults > div > p > span"
date_selector = "#rttResults > div > div.mb-1.text-center.text-dark > div"
hour_selector = "#rttResults > div > div.mb-1.text-center.text-dark > span > strong"
download_selector = "#app > div > div > div > div > div.d-flex.flex-row.flex-wrap.justify-content-center.mt-5.mb-3 > div.col-6.col-md-5.order-1.order-md-1.text-left > div > div.pt-0.d-inline-flex.align-items-md-baseline.align-items-center.flex-wrap.flex-md-row.flex-column"
upload_selector = "#app > div > div > div > div > div.d-flex.flex-row.flex-wrap.justify-content-center.mt-5.mb-3 > div.col-6.col-md-5.order-2.order-md-3.text-right > div > div.pt-0.d-inline-flex.align-items-md-baseline.align-items-center.flex-wrap.flex-md-row.flex-column"

# Open the Simet
browser.get(url)

# Wait until ping value appear
element = wait.until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ping_selector), '--'))

# wait more 5 seconds before start get the values
sleep(5)

# Get download data
get_download = browser.find_element_by_css_selector(download_selector)
data.append(get_download.text.split('\n')[0]) # Download value
data.append(get_download.text.split('\n')[1]) # Donwload unit (like Mbps)

# Get upload data
get_upload = browser.find_element_by_css_selector(upload_selector)
data.append(get_upload.text.split('\n')[0]) # upload value
data.append(get_upload.text.split('\n')[1]) # upload unit (like Mbps)

# Get the RTT values
get_rtt_results = browser.find_elements_by_css_selector(ping_selector)
data.append(get_rtt_results[0].text.split(' ')[0]) # ping time
data.append(get_rtt_results[0].text.split(' ')[1]) # ping time unit (like ms)
data.append(get_rtt_results[1].text) # Packet lost
data.append(get_rtt_results[2].text.split(' ')[0]) # jitter time
data.append(get_rtt_results[2].text.split(' ')[1]) # jitter time unit (like ms)

# Get the date
get_date = browser.find_element_by_css_selector(date_selector)
data.append(get_date.text)

# Get the hour
get_hour = browser.find_element_by_css_selector(hour_selector)
data.append(get_hour.text)

# All values were added to data var (a list) and now is saved in a .csv file
with open('measurements.csv', mode='r+') as csv_file:
   # csv_reader = csv.reader(csv_file)
    row = csv_file.readline()
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if row  == "":
      csv_writer.writerow(columns)
      csv_writer.writerow(data)
    else:
      csv_writer.writerow(data)

# Take a screenshot from browser with Simet data
screenshot_name = "screenshot_"+ get_date.text.replace('/','-') + "_" + get_hour.text.replace(':','-').replace(' ', '-') + ".png"
browser.get_screenshot_as_file(screenshot_name)

# Quit the browser
browser.quit()
