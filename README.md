# simet-collect
Python script that uses Selenium to get  results from Simet (simet.nic.br) connection tests

## What this script do

- open the Chrome browser 
- open the url https://beta.simet.nic.br/
- wait for the results
- collect the results
- take a screenshot of the page with the results
- close the browser


### How to use

- git clone https://github.com/dcna-io/simet-collect.git
- cd simet-collect
- python3 -m venv .venv
- . .venv/bin/activate
- pip install -r requirements.txt
- touch measurements.csv
- download and install the Chrome driver:
  - wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
    - Please, choose the correct version of you browser in https://chromedriver.chromium.org/downloads
  - unzip -d .venv/bin/ chromedriver_linux64.zip
    - This command will install the drive in virtualenv, if you want to make this acessible to everyone, change .venv/bin/ to another folder that is present in your $PATH environment variable
- python simet-collect.py

## To do

- Make the script create the file measurements.csv fle if not exists
- Test with Firefox
  - Need to replace the webdriver
  - Comment or replace the Chrome options
- Configure an option to run in background (headless)
- Create oprions to run multiple times (like a cron)

