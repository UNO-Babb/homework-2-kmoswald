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

def getHours(time): #Take a time in the format HH:MM AM and return hour in 24-hour format
  
  time2 = datetime.datetime.strptime(time, "%H:%M%p")
 
  currentHour = (time2.hour - 6) % 24

  return currentHour

def getMinutes(time): #Given a string in the form "HH:MM AM/PM" will return just the minutes portion.
  time2 = datetime.datetime.strptime(time, "%H:%M%p")
 
  currentMinute = time2.minute
  return currentMinute

def minutesLater(time1, time2): #comparing two time strings to see how many minutes apart they are
  
  hour1 = datetime.datetime.strptime(time1, "%I:%M%p").hour
  minutes1 = getMinutes(time1)
  minutes1 = minutes1 + (hour1 * 60)

  hour2 = datetime.datetime.strptime(time2, "%I:%M%p").hour
  minutes2 = getMinutes(time2)
  minutes2 = minutes2 + (hour2 * 60) 

  minutesDiff = minutes1 - minutes2
  return minutesDiff

def nextBusTime(busTimeList, myTime): #provided the following bus arrival 

  foundTime = ""
  for busTime in busTimeList:
    if minutesLater(myTime, busTime) < 0:
      foundTime = busTime
      break
      
  if foundTime == "":
    foundTime = busTimeList[0]

  return foundTime 

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

  for testLine in busList: #filter out lines from the testPage that were not times
    if (testLine.count(":") == 1) and ((len(testLine) == 6) or (len(testLine) == 7)):
      busTimes.append(testLine)
  
  currentDT = datetime.datetime.now()
  currentLocalTime = datetime.time((currentDT.hour - 5) % 24, currentDT.minute)

  currentLocalTimeStr = currentLocalTime.strftime("%I:%M%p")
  print("Current time: " +  currentLocalTimeStr)
  
  nextBus = nextBusTime(busTimes, currentLocalTimeStr)
  minLater = minutesLater(nextBus, currentLocalTimeStr) 
  print(f"The next bus will arrive in {minLater} minutes.")

  followingBus = "" #give the user the second bus option
  nextBusIndex = busTimes.index(nextBus)

  if (nextBusIndex < len(busTimes) - 1): #if the current bus is at the last time on the list, start the list over
    followingBus = busTimes[nextBusIndex + 1]
  else:
    followingBus = busTimes[0]

  print(f"The following bus will arrive in {str(abs(minutesLater(followingBus, nextBus)))} minutes.")
  
main()
