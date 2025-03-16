import csv
import pandas as pd



def hoopswinners():
    print("")
    #df1 = pd.read_csv("/Users/gojacketz/PycharmProjects/NCAABasketballModel/ModelData/scraping_matchups.csv")
    #df2 = pd.read_csv("/Users/gojacketz/PycharmProjects/NCAABasketballModel/ModelData/kenpom.csv")
    df1 = pd.read_csv("../ModelData/todays_matchups.csv")
    df2 = pd.read_csv("../ModelData/kenpom.csv")
    homeTeam = []
    awayTeam = []
    openingLine = []
    openingTotal = []
    projectedTotal = []
    homeMoneyLine = []
    roadMoneyLine = []
    modelPredictedLine = []
    modelFavorite = []
    modelLine = []


    for index, row in df1.iterrows():
        #print(row['Home Team'], row['Away Team'], row['Opening Line'])
        hometeam = row['Home Team']
        roadteam = row['Away Team']
        openingline = row['Opening Line']
        openingtotal = row['Opening Total'][1:]



        homerow = df2[df2["team"] == hometeam]

        #print(homerow)

        #print("Filtered Row(s):\n", homerow)

        roadrow = df2[df2["team"] == roadteam]
        #print(roadrow)
        #print("Filtered Row(s):\n", roadrow)

        if not homerow.empty:
            pass
        else:
            continue
            #print(f"No data found for home team: {hometeam}")

        if not roadrow.empty:
            homeTeam.append(hometeam)
            awayTeam.append(roadteam)
            openingLine.append(openingline)
            openingTotal.append(openingtotal)
        else:
            continue

        homeadjoffense = homerow.iloc[0]["AdjO"]
        #print("AdjO: "+str(homeadjoffense))
        homeadjdefense = homerow.iloc[0]["AdjD"]
        #print("AdjD: "+str(homeadjdefense))

        roadadjoffense = roadrow.iloc[0]["AdjO"]
        #print("roadadjoffense: "+str(roadadjoffense))
        roadadjdefense = roadrow.iloc[0]["AdjD"]
        #print("roadadjdefense: "+str(roadadjdefense))

        HomeCourtAA = 0.00 #zero if nuetral court
        #HomeCourtAA = 3.02 #zero if nuetral court

        avgAdjT = df2["AdjT"].mean()
        #print("avgAdjT: "+str(avgAdjT))

        avgAdjO = df2["AdjO"].mean()
        #print("avgAdjO: " +str(avgAdjO))

        avgAdjD = df2["AdjD"].mean()
        #print("avgAdjD: "+str(avgAdjD))

        homecourdAdj = HomeCourtAA/2/avgAdjO
        roadcourdAdj = -1*HomeCourtAA/2/avgAdjO

        #print("homecourtAdj: " + str(homecourdAdj))
        #print("roadcourdAdj: " + str(roadcourdAdj))

        homeoffense = homeadjoffense*(1 + homecourdAdj)
        #print("homeoffense: " + str(homeoffense))
        homedefense = homeadjdefense*(1 - homecourdAdj)
        #print("homedefense: " + str(homedefense))


        roadoffense = roadadjoffense*(1 + roadcourdAdj)
        #print("roadoffense: " + str(roadoffense))
        roaddefense = roadadjdefense*(1 - roadcourdAdj)
        #print("roaddefense: " + str(roaddefense))
        #Expected WIN % Calcs
        #Need AdjO, AdjD

        #Offense = AdjO*(1+HomeCourt)
        #Defense = AdjD*(1-HomeCourt)
        #E(W%) = Offense*10.25(Offense^10.25 + Defense^10.25)



        homeewpercentage = homeoffense**10.25/(homeoffense**10.25 + homedefense**10.25)
        #print("homeewpercentage: " + str(homeewpercentage))

        roadewpercentage = roadoffense**10.25/(roadoffense**10.25 + roaddefense**10.25)
        #print("roadewpercentage: " + str(roadewpercentage))

        #Win% = (E(W%)-E(W%)*opponentsE(W%))/E(W%)+Opponents E(W%)-2*E(W%)*opponents E(W%)

        homewinpercentage = (homeewpercentage-homeewpercentage*roadewpercentage)/(homeewpercentage+roadewpercentage-2*homeewpercentage*roadewpercentage)
        #print(hometeam +" Win Percentage: " + str(homewinpercentage))
        roadwinpercentage = (roadewpercentage-roadewpercentage*homeewpercentage)/(roadewpercentage+homeewpercentage-2*roadewpercentage*homeewpercentage)
        #print(roadteam +" Win Percentage: " + str(roadwinpercentage))

        if homewinpercentage > .5000:
            homemoneyline = -100*(homewinpercentage/(1-homewinpercentage))
            print(hometeam+ " Moneyline: " + str(homemoneyline))
        elif homewinpercentage < .5000:
            homemoneyline = 100*((1-homewinpercentage)/homewinpercentage)
            print(hometeam+ " Moneyline: " + str(homemoneyline))
        elif homewinpercentage == .5000:
            homemoneyline = 'Even'
            print(hometeam+ " Moneyline: Even")
        homeMoneyLine.append(round(homemoneyline,2))

        if roadwinpercentage > .5000:
            roadmoneyline = -100*(roadwinpercentage/(1-roadwinpercentage))
            print(roadteam+" Moneyline: " + str(roadmoneyline))
        elif roadwinpercentage < .5000:
            roadmoneyline = 100*((1-roadwinpercentage)/roadwinpercentage)
            print(roadteam+" Moneyline: " + str(roadmoneyline))
        elif roadwinpercentage == .5000:
            roadmoneyline = 'Even'
            print(roadteam+" Moneyline:  Even")
        roadMoneyLine.append(round(roadmoneyline,2))
        #Score Predictors:
        #AdjT
        #Tempo % = AdjT/Average NCAA Tempo
        #E(Tempo) = Tempo % of opponent*Teams Tempo%/Average Tempo
        #Output O% = Offense/Average AdjO for all
        #output D% = Opponents Defense/Averge AdjO for all
        #E(Output) = Output O x Output D x Average Adj O
        #Final Points - E(Output)(E(Tempo)/100)

        homeadjtempo = homerow.iloc[0]["AdjT"]
        #print("homeadjtempo: "+str(homeadjtempo))

        roadadjtempo = roadrow.iloc[0]["AdjT"]
        #print("roadadjtempo: "+str(roadadjtempo))

        hometempopercentage = (homeadjtempo)/avgAdjT
        #print("hometempopercentage: "+str(hometempopercentage))

        roadtempopercentage = (roadadjtempo)/avgAdjT
        #print("roadtempopercentage: "+str(roadtempopercentage))
        #print("avgAdjT: "+str(avgAdjT))

        etempo = hometempopercentage*roadtempopercentage*avgAdjT
        #print("etempo: "+str(etempo))

        homeoutputOpercentage = homeoffense/avgAdjO
        #print("homeoutputOpercentage: " + str(homeoutputOpercentage))

        roadoutputOpercentage = roadoffense/avgAdjO
        #rint("roadoutputOpercentage: " + str(roadoutputOpercentage))

        homeoutputDpercentage = roaddefense/avgAdjD
        #print("homeoutputDpercentage: " + str(homeoutputDpercentage))

        roadoutputDpercentage = homedefense/avgAdjD
        #print("roadoutputDpercentage: " + str(roadoutputDpercentage))

        homeeoutput = homeoutputOpercentage*homeoutputDpercentage*avgAdjO
        #print("homeeoutput: " + str(homeeoutput))


        roadeoutput = roadoutputOpercentage*roadoutputDpercentage*avgAdjO
        #print("roadeoutput: " + str(roadeoutput))

        homefinalpoints = homeeoutput*(etempo/100)
        #print("homefinalpoints: " + str(homefinalpoints))

        roadfinalpoints = roadeoutput*(etempo/100)
        #print("roadfinalpoints: " + str(roadfinalpoints))

        if homefinalpoints > roadfinalpoints:
            print(hometeam+" projected favorite -"+ str(homefinalpoints-roadfinalpoints))
            modelFavorite.append(hometeam)
            modelPredictedLine.append(hometeam+" projected favorite -"+ str(round((homefinalpoints-roadfinalpoints),2)))
            modelLine.append(round(-1*(homefinalpoints-roadfinalpoints),2))

        if roadfinalpoints > homefinalpoints:
            print(roadteam+" projected favorite -"+ str(roadfinalpoints-homefinalpoints))
            modelFavorite.append(roadteam)
            modelPredictedLine.append(roadteam+" projected favorite -"+ str(round((roadfinalpoints-homefinalpoints),2)))
            modelLine.append(round(-1*(roadfinalpoints-homefinalpoints),2))
        over_under = homefinalpoints + roadfinalpoints
        print("Projected Total: ", str(over_under))
        projectedTotal.append(round(over_under,2))





    df3 = pd.DataFrame({'Home Team': homeTeam, 'Opening Home Team Line':openingLine, "Away Team": awayTeam,
                        'Model Favorite':modelFavorite,'Model Line':modelLine,'Opening Total' : openingTotal,
                        'Projected Total': projectedTotal, 'Home MoneyLine':homeMoneyLine,
                        'Road Moneyline':roadMoneyLine, 'Model Prediction':modelPredictedLine
                        })
    df3.to_csv('../ModelData/Model_Projections.csv', index=False)

hoopswinners()
