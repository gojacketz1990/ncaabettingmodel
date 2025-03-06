import csv
import pandas as pd



def model_picks():
    print("")
    #df1 = pd.read_csv("/Users/gojacketz/PycharmProjects/NCAABasketballModel/ModelData/scraping_matchups.csv")
    #df2 = pd.read_csv("/Users/gojacketz/PycharmProjects/NCAABasketballModel/ModelData/kenpom.csv")
    df1 = pd.read_csv("../ModelData/Model_Projections.csv")

    homeTeam = []
    awayTeam = []
    projectedTotal = []
    openingTotal = []
    pick = []
    pointdifference = []
    confidence = []



    for index, row in df1.iterrows():
        #print(row['Home Team'], row['Away Team'], row['Opening Line'])
        hometeam = row['Home Team']
        awayteam = row['Away Team']
        openingtotal = row['Opening Total']
        projectedtotal = row['Projected Total']

        homeTeam.append(hometeam)
        awayTeam.append(awayteam)
        openingTotal.append(openingtotal)
        projectedTotal.append(projectedtotal)

        if projectedtotal > openingtotal:
            pick.append("OVER")
            pointdifference.append(str(round(projectedtotal-openingtotal)))


        if openingtotal > projectedtotal:
            pick.append("UNDER")
            pointdifference.append(str(round(openingtotal-projectedtotal)))

        if openingtotal == projectedtotal:
            pick.append("Total Matches")
            pointdifference.append(str(0))

        if 0 <= abs(projectedtotal-openingtotal) <= 1:
            confidence.append("Very Low")

        if 1 < abs(projectedtotal-openingtotal) <= 2:
            confidence.append("Low")

        if 2 < abs(projectedtotal-openingtotal) <= 3:
            confidence.append("Medium")

        if 3 < abs(projectedtotal-openingtotal) <= 5:
            confidence.append("High")

        if abs(projectedtotal-openingtotal) > 5:
            confidence.append("Very High")

    df2 = pd.DataFrame({'Home Team': homeTeam,  "Away Team": awayTeam,
                       'Opening Total' : openingTotal,
                        'Projected Total': projectedTotal,
                        'Total Pick': pick,
                        'Point Difference':pointdifference,
                        'Confidence':confidence

                        })

    df2 = df2.sort_values(by='Point Difference', ascending=False)


    df2.to_csv('../ModelData/Total_Model_Picks.csv', index=False)

model_picks()
