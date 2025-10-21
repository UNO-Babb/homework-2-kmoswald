#BusSchedule.py
#Name:Kaitlyn Oswald
#Date:10/5/25
#Assignment:Homework 2

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents

def getHours(time):
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute)
  #if hour 

  #hour = hour + 12


  "Take a time in the format HH:MM AM and return hour in 24-hour format"

  return 21

#def getMinutes(time):
#Given a string in the form "HH:MM AM/PM" will return just the minutes portion.


#def isLater(time1, time2):
#Provide True or False if time 1 is later than time 2
#hour1 = getHours(time1)
#minutes1 = getMinutes(time1)
#hour2 = getHours(time2)
#minutes2 = getMinutes(time2)
#if hour1 > hour2
  #return True
#elif hour1 < hour2
  #return False
#else
  #if minute1 > minute2:
    #return True
   #else
    #return False 

def main():
  direction = "EAST"

  #url = "https://myride.ometro.com/Schedule?stopCode=2269&routeNumber=11&directionName=" + direction
  url = "https://myride.ometro.com/Schedule?stopCode=3060&date=2025-10-20&routeNumber=18&directionName="+ direction
  c1 = loadURL(url) #loads the web page
  #c1 = loadTestPage() #loads the test page
  print(c1)
  time = "9:49 PM"

  #print("Current time:" + )
  #print("The next bus will arrive in" +)
  #print("The following bus will arrive in " + )
  
main()
