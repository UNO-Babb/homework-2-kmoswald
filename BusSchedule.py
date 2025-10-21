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
  
  #now = datetime.datetime.now()
  time2 = datetime.datetime.strptime(time, "%H:%M%p")
 
  currentHour = (time2.hour - 6) % 24


  "Take a time in the format HH:MM AM and return hour in 24-hour format"

  return currentHour

def getMinutes(time):
#Given a string in the form "HH:MM AM/PM" will return just the minutes portion.
#want to ignore HH and "":"
#currentMinute = now.minute
  time2 = datetime.datetime.strptime(time, "%H:%M%p")
 
  currentMinute = time2.minute
  return currentMinute


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
  routeNo = "11"
  stopNo = "2269"


  url = "https://myride.ometro.com/Schedule?stopCode=" + stopNo + "&routeNumber=" + routeNo + "&directionName=" + direction
  #c1 = loadURL(url) #loads the web page
  c1 = loadTestPage() #loads the test page
  #print(c1)
  busList = c1.split("\n")
  busTimes = []

  for testLine in busList:
    #print(f"{testLine}  {testLine.count(":")}")
    if (testLine.count(":") == 1) and ((len(testLine) == 6) or (len(testLine) == 7)):
      #print("append:" + testLine)
      busTimes.append(testLine)
  
  #print("busTimes")
  #for busTime in busTimes:
  #  print(busTime)



  #time = "9:49PM"
  #time = busTimes[4]
  #print(getHours(time))
  #print(getMinutes(time))
  
  #print(datetime.datetime.astimezone)
  currentDT = datetime.datetime.now()
  if currentDT.hour >= 12:
    time = str((currentDT.hour - 5) % 12) + ":" + str(currentDT.minute) + "PM"
  else:
    time = str((currentDT.hour - 5) % 12) + ":" + str(currentDT.minute) + "AM"

  print("Current time:" +  time)
  #print("The next bus will arrive in" + getMinutes(time))
  #print("The following bus will arrive in " + getMinutes(time))
  
main()
