from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# import time
# import sys


def send_email(message_dict):
    pd.set_option('display.max_colwidth', -1)  # Set this so that the message values are not truncate
    df = pd.DataFrame(data=message_dict)  # Convert the message_dict variable into a dataframe
    df = df.fillna(' ').T  # Transpose the data so we have rows as steps

    message_html = df.to_html()  # Convert the dataframe into HTML

    smtp_address = '###@email_server.com' # smtp server email details - use gmail one
    smtp_pw = 'xxx' # password details for smtp server
    to_names = ['Joe Bloggs']
    to_emails = ['joe.bloggs@email_server.com']

    # set up the SMTP server
    s = SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(smtp_address, smtp_pw)

    # For each contact, send the email:
    for name, email in zip(to_names, to_emails):
        msg = MIMEMultipart('alternative')  # create a message

        # setup the parameters of the message
        msg['From'] = smtp_address
        msg['To'] = email
        msg['Subject'] = "RateSetter Scrape - Automated Email"

        msg_contents = MIMEText(message_html, 'html')

        msg.attach(msg_contents)

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


log_msg = {}

url = 'https://members.ratesetter.com/login.aspx'
chrome_driver_path = u'C:\\Users\\ABaker\\Documents\\GitHub\\python_learning\\scraping\\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
)

webdriver.set_window_size(1440, 900)

with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # retrieve url in headless browser
    driver.get(url)

    try:
        # find email field and enter details
        wait.until(presence_of_element_located((By.ID, "txtEmailNew")))
        email_input = driver.find_element_by_id("txtEmailNew")
        email_input.send_keys("xxx@email_provider.com") # my email address

        # find password field and enter details
        wait.until(presence_of_element_located((By.ID, "ctl00_cphContentArea_cphForm_txtPasswordNew")))
        pw_input = driver.find_element_by_id("ctl00_cphContentArea_cphForm_txtPasswordNew")
        pw_input.send_keys("xxx123") # password to be sent in form

        driver.find_element_by_class_name("login-btn").click()
    except:
        print("Could not log in")
        driver.quit()

    try:
        # Find the 'ISA Account' details and click on relevant button
        wait.until(presence_of_element_located((By.ID, "ctl00_cphContentArea_rptAccounts_ctl01_btnView")))
        driver.find_element_by_id("ctl00_cphContentArea_rptAccounts_ctl01_btnView").click()

        # Find the 'Withdraw' button and click on it
        wait.until(presence_of_element_located((By.LINK_TEXT, "Withdraw")))
        driver.find_element_by_link_text("Withdraw").click()

        # Find the 'Withdraw to Bank Account' button and click on it
        wait.until(presence_of_element_located((By.ID, "ctl00_cphContentArea_cphForm_btnNextOneOff")))
        driver.find_element_by_id("ctl00_cphContentArea_cphForm_btnNextOneOff").click()
    except:
        print("Could not access the 'Withdraw to Bank Account' screen")
        driver.quit()

    try:
        # Now try to find out if there are any values in either 'Holding Account' or 'On Market'
        wait.until(presence_of_element_located((By.CLASS_NAME, "novo-table-content")))
        table_id = driver.find_element(By.CLASS_NAME, "novo-table-content")
        rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        holding_account_val = rows[1].find_elements(By.TAG_NAME, "td")[1]
        on_market_val = rows[2].find_elements(By.TAG_NAME, "td")[1]
        holding_account_val = float(holding_account_val.text[1:])
        on_market_val = float(on_market_val.text[1:])
    except:
        print("Could not evaluate possible withdrawal amounts")
        driver.quit()

    try:
        # We now test whether either of the Holding Account/On Market values are > 0 and withdraw
        if holding_account_val > 1 or on_market_val > 1:
            withdraw_entry = driver.find_element_by_id("ctl00_cphContentArea_cphForm_tbAmount")
            withdraw_entry.send_keys(str(holding_account_val + on_market_val))  # this is how we should do it
            # withdraw_entry.send_keys(str(1.00)) # for now test with £1.00

            # Confirm the withdrawal amount
            wait.until(presence_of_element_located((By.ID, "ctl00_cphContentArea_cphForm_btnNext")))
            next_element = driver.find_element_by_id("ctl00_cphContentArea_cphForm_btnNext")
            driver.execute_script("arguments[0].click();", next_element)

            # Confirm the final withdrawal
            wait.until(presence_of_element_located((By.ID, "ctl00_cphContentArea_cphForm_btnConfirm")))
            confirm_element = driver.find_element_by_id("ctl00_cphContentArea_cphForm_btnConfirm")
            driver.execute_script("arguments[0].click();", confirm_element)

            # Send an email with the amount withdrawn
            log_msg['Amount Withdrawn'] = {'Value': str(holding_account_val + on_market_val)}
            send_email(log_msg)

    except:
        print("Could not withdraw any values")
    finally:
        # must close the driver after task finished
        log_msg['Amount Withdrawn'] = {'Value': 'nowt'}
        send_email(log_msg)

        driver.quit()
