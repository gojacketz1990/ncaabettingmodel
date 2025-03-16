
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import Select
import csv

def read_csv_row_by_column_value(filename, column_name, column_value):
  """Reads a specific row from a CSV file based on a column value.

  Args:
    filename: The name of the CSV file.
    column_name: The name of the column to search.
    column_value: The value to search for in the column.

  Returns:
    A list containing the values in the row, or None if the row is not found.
  """

  with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[column_name] == column_value:
        return row

  return None
def Average(lst):
    return sum(lst) / len(lst)



def vegasInsider_webscrape():


    chrome_options = Options()
    chrome_options.add_argument("--enable-javascript")

    service = Service("/opt/homebrew/bin/chromedriver")  # Replace with actual path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://www.vegasinsider.com/college-basketball/odds/las-vegas/')
    driver.fullscreen_window()
    driver.maximize_window()

    #put the teams together:



    allhometeams = driver.find_elements(By.XPATH,"//tbody[contains(@id,'spread')]/tr[@class='footer']")
    allroadteams = driver.find_elements(By.XPATH,"//tbody[contains(@id,'spread')]/tr[@class='divided']")

    homeTeam = []
    awayTeam = []
    openingLine = []
    openingTotal = []

    teamcount = 0
    for allhometeamsandlines in allhometeams:
        #print(allhometeamsandlines.text)
        homeTeam.append(allhometeamsandlines.find_element(By.XPATH,"./td/div/span/a").text)
        openingLine.append(allhometeamsandlines.find_element(By.XPATH,"./td[@class='game-odds'][1]/span/span").text)
        #openingLine.append(allhometeamsandlines.find_element(By.XPATH,"./td[@class='game-odds'][4]/a/span").text)

    for roadteams in allroadteams:
        try:
            # Attempt to find the element and append its text
            awayTeam.append(roadteams.find_element(By.XPATH, "./td/div/span/a").text)
        except:
            # If the element is not found, append 'N/A'
            awayTeam.append('N/A')


    totalTab = driver.find_element(By.XPATH, '//li/span[contains(@data-content,"total")]')
    totalTab.click()

    alltotals = driver.find_elements(By.XPATH,"//tbody[contains(@id,'total')]/tr[@class='footer']")



    for totals in alltotals:

        openingTotal.append(totals.find_element(By.XPATH,"./td[@class='game-odds'][1]/span/span").text)
        print(totals.find_element(By.XPATH,"./td[@class='game-odds'][4]/a/span").text)

    driver.quit()

    # print("The AdjEM average is", Average(AdjEM))
    # print("The AdjO average is", Average(AdjO))
    # print("The AdjD average is", Average(AdjD))
    # print("The AdjT average is", Average(AdjT))
    # print("The Luck average is", Average(Luck))
    # print("The AdjEMSoS average is", Average(AdjEMSoS))
    # print("The OppO average is", Average(OppO))
    # print("The OppD average is", Average(OppD))
    # print("The AdjEMNCSOS average is", Average(AdjEMNCSOS))
    #
    # #create data frame with Pandas
    # #With dictionaries:
    df = pd.DataFrame({'Home Team': homeTeam, "Away Team": awayTeam, 'Opening Line': openingLine, 'Opening Total' : openingTotal})
    df.to_csv('../ModelData/todays_matchups.csv', index=False)
    # #print(df)
    # hometeam = input("Enter home team: ")
    # roadteam = input("Enter road team: ")
    #
    # hometeamrow = read_csv_row_by_column_value("kenpom.csv", "team", hometeam)
    # if hometeamrow:
    #   print(hometeamrow)
    # else:
    #   print("Row not found.")

vegasInsider_webscrape()
