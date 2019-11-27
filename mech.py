import mechanicalsoup
from creds import *
from random import randint
from time import sleep
import datetime
from send_sms import sms_sender
from bs4 import BeautifulSoup
import os.path

#Todo: Bot nur während Arbeitszeit des Prüfungsbüros laufen lassen
# Mehr Zufall
# SMS senden integrieren

# while datetime.datetime.today().weekday() < 5:
#     #run script
#     # else wait for weekday
#     pass

# Initiate browser with common user_agent
browser = mechanicalsoup.StatefulBrowser(
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"
)
sleep(randint(1,5))

# Open Agnes and wait a random time between 1 to 5 seconds
browser.open("https://agnes.hu-berlin.de/")
sleep(randint(1,5))

# Find login link using regex, klick link and wait
login_link = browser.find_link(url_regex="wlogin")
browser.follow_link(login_link)
sleep(randint(1,5))

# Select form, enter credentials and submit login form
browser.select_form('form[name="loginform"]')
browser["username"] = user
browser["password"] = password
resp = browser.submit_selected()
sleep(randint(1,7))

# Find link to student record, follow and wait
student_record_link = browser.find_link(url_regex="notenspiegelStudent")
browser.follow_link(student_record_link)
sleep(randint(1,5))

# Get the student record's html, find tablerows
page = browser.get_current_page()
new_table_rows = page.table.find_all("tr")


if not os.path.isfile('inital_table.html'):
    with open("inital_table.html", "w") as f:
      f.write(str(new_table_rows))

else:
    with open("inital_table.html") as f:
        old_table_rows = BeautifulSoup(f, features="lxml")
    diff = list(set(new_table_rows).difference(old_table_rows))
    if diff:
        grade = diff[0].select("td", {"class": "lspiegel_center lspiegelBottomBorder"})[4].get_text(strip=True)
        type = diff[0].select("td", {"class": "lspiegel_center lspiegelBottomBorder"})[1].get_text(strip=True)
        sms_sender(number, type, grade)


# Perform logout and close browser
logout_link = browser.find_link(url_regex="auth.logout")
browser.follow_link(logout_link)
browser.close()
