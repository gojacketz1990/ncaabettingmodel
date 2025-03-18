from selenium import webdriver
from selenium.webdriver.common.by import By
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



def kenpom_webscrape():

    driver = webdriver.Chrome()

    driver.get('https://kenpom.com')
    driver.fullscreen_window()
    #driver.maximize_window()

    #put the teams together:



    allkenpomrows = driver.find_elements(By.XPATH,"//tbody/tr")
    rank = []
    team = []
    conference = []
    winloss = []
    AdjEM = []
    AdjO = []
    AdjD = []
    AdjT = []
    Luck = []
    AdjEMSoS = []
    OppO = []
    OppD = []
    AdjEMNCSOS = []

    for stats in allkenpomrows:
        #print(stats.text)
        rank.append(stats.find_element(By.XPATH,'./td[1]').text)



        # Assuming 'stats' is already defined in your Selenium script
        team_name = stats.find_element(By.XPATH, './td[2]/a').text

        # Check if the text ends with 'St.' and replace it
        if team_name.endswith('St.'):
            team_name = team_name.replace('St.', 'State')

        # Append to the list
        team.append(team_name)

        #team.append(stats.find_element(By.XPATH,'./td[2]/a').text)


        conference.append(stats.find_element(By.XPATH,'./td[3]').text)
        winloss.append(stats.find_element(By.XPATH,'./td[4]').text)
        AdjEM.append(float(stats.find_element(By.XPATH,'./td[5]').text))
        AdjO.append(float(stats.find_element(By.XPATH,'./td[6]').text))
        AdjD.append(float(stats.find_element(By.XPATH,'./td[8]').text))
        AdjT.append(float(stats.find_element(By.XPATH,'./td[10]').text))
        Luck.append(float(stats.find_element(By.XPATH,'./td[12]').text))
        AdjEMSoS.append(float(stats.find_element(By.XPATH,'./td[14]').text))
        OppO.append(float(stats.find_element(By.XPATH,'./td[16]').text))
        OppD.append(float(stats.find_element(By.XPATH,'./td[18]').text))
        AdjEMNCSOS.append(float(stats.find_element(By.XPATH,'./td[20]').text))

        #rank = stats.find_element(By.XPATH,'./td[1]').text
        #team = stats.find_element(By.XPATH,'./td[2]').text
        #conference = stats.find_element(By.XPATH,'./td[3]').text
        #winloss = stats.find_element(By.XPATH,'./td[4]').text
        #AdjEM = stats.find_element(By.XPATH,'./td[5]').text

        #print("")
        #print(rank)
        #print(team)
        #print(conference)
        #print(winloss)
        #print(AdjEM)
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
    df = pd.DataFrame({'rank': rank, "team": team, 'conference': conference, "winloss": winloss, "AdjEM":AdjEM, "AdjO":AdjO, "AdjD":AdjD,
                       "AdjT":AdjT, "Luck":Luck, "AdjEMSoS":AdjEMSoS, "OppO":OppO,"OppD":OppD,"AdjEMNCSOS":AdjEMNCSOS})
    df.to_csv('../ModelData/kenpom.csv', index=False)
    # #print(df)
    # hometeam = input("Enter home team: ")
    # roadteam = input("Enter road team: ")
    #
    # hometeamrow = read_csv_row_by_column_value("kenpom.csv", "team", hometeam)
    # if hometeamrow:
    #   print(hometeamrow)
    # else:
    #   print("Row not found.")

kenpom_webscrape()
