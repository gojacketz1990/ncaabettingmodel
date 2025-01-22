import csv
import pandas as pd



def test_hoopswinners():
    print("")
    #df1 = pd.read_csv("/Users/gojacketz/PycharmProjects/NCAABasketballModel/ModelData/scraping_matchups.csv")
    #df2 = pd.read_csv("/Users/gojacketz/PycharmProjects/NCAABasketballModel/ModelData/kenpom.csv")
    df1 = pd.read_csv("../ModelData/Model_Projections.csv")

    homeTeam = []
    awayTeam = []
    openingHomeLine = []
    modelFavorite = []
    modelLine = []
    pick = []
    pointdifference = []
    confidence = []



    for index, row in df1.iterrows():
        #print(row['Home Team'], row['Away Team'], row['Opening Line'])
        hometeam = row['Home Team']
        awayteam = row['Away Team']
        openinghomeline = row['Opening Home Team Line']
        modelfavorite = row['Model Favorite']
        modelline = row['Model Line']


        homeTeam.append(hometeam)
        awayTeam.append(awayteam)
        openingHomeLine.append(openinghomeline)
        modelFavorite.append(modelfavorite)
        modelLine.append(modelline)

        pointdiff = 0

        if openinghomeline < 0 and modelfavorite == hometeam:#both negative
            if abs(modelline) - abs(openinghomeline) > 0:
                pick.append(hometeam)
                pointdiff = round(abs(modelline) - abs(openinghomeline))
                pointdifference.append(str(pointdiff))
            else:
                pick.append(awayteam)
                pointdiff = round(abs(openinghomeline) - abs(modelline))
                pointdifference.append(str(pointdiff))


        elif openinghomeline < 0 and modelfavorite == awayteam:#home line negative, home model line positive
            #Home team favored, Road Team Favored by Model
            pick.append(awayteam)
            pointdiff = round(abs(modelline) + abs(openinghomeline))
            pointdifference.append(str(pointdiff))

        elif openinghomeline > 0 and modelfavorite == hometeam:#HOME LINE positive, home model line negative
            #Road team favored, Home Team Favored by Model
            pick.append(hometeam)
            pointdiff = round(abs(modelline) + abs(openinghomeline))
            pointdifference.append(str(pointdiff))

        elif openinghomeline > 0 and modelfavorite == awayteam:#home line positive, home model line positive
            if abs(modelline) - abs(openinghomeline) > 0:
                pick.append(awayteam)
                pointdiff = round(abs(modelline) - abs(openinghomeline))
                pointdifference.append(str(pointdiff))
            else:
                pick.append(hometeam)
                pointdiff = round(abs(openinghomeline) - abs(modelline))
                pointdifference.append(str(pointdiff))

        if 0 <= abs(pointdiff) <= 1:
            confidence.append("Very Low")
        if 1 < abs(pointdiff) <= 2:
            confidence.append("Low")
        if 2 < abs(pointdiff) <= 3:
            confidence.append("Medium")
        if 3 < abs(pointdiff) < 5:
            confidence.append("High")
        if abs(pointdiff) >= 5:
            confidence.append("Very High")


    df2 = pd.DataFrame({'Home Team': homeTeam,  "Away Team": awayTeam,
                       'Opening Home Line' : openingHomeLine,
                        'Model Favorite': modelFavorite,
                        'Model Line': modelLine,
                        'Pick':pick,
                        'Point Difference':pointdifference,
                        'Confidence':confidence
                        })

    df2 = df2.sort_values(by='Point Difference', ascending=False)


    df2.to_csv('../ModelData/Line_Model_Picks.csv', index=False)
