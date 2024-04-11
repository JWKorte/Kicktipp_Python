import pandas as pd
print("Vollautomatische Tagessieg-Ermittlung\nFür die meisten Punkte unter den relevanten Tippern pro Spieltag gibt es einen Punkt, bei Punktgleicheit 1/Anzahl der Tipper")
blt_platzierungen = pd.read_html("https://www.kicktipp.de/xyz/gesamtuebersicht?ansicht=spieltagspunkte&")[0]                           # Statt xyz Name der Tipprunde
tipper = ["x", "y", "z"]                                                                                                        # Statt x,y,z Namen der Tipper 
print("Tagessiege im Bundesligatipp")                                                                                 # Report der Tagessiege in der Spielrunde 
for tipp in tipper:
    print(tipp+":\t",blt_platzierungen[blt_platzierungen["Name"]==tipp]["S"].values[0]/100)
blt_platzierungen = blt_platzierungen.set_index(blt_platzierungen["Name"]).drop(["Pos","Name","Re","S","G"], axis=1)        
for x in blt_platzierungen.index:
    if x not in tipper:
        blt_platzierungen.drop([x], inplace=True)
tagessiege = {'y':0,'x':0,'z':0}                                                                                                # Statt x,y,z Namen der Tipper
for x in blt_platzierungen:
    if blt_platzierungen[x][1]>0:
        for y in list(range(1,len(blt_platzierungen.index[blt_platzierungen[x]==blt_platzierungen[x].max()])+1)):
            tagessiege[blt_platzierungen.index[blt_platzierungen[x]==blt_platzierungen[x].max()][y-1]]+=1/len(blt_platzierungen.index[blt_platzierungen[x]==blt_platzierungen[x].max()])
print("--Bundesligatipp--")
for x,y in sorted(tagessiege.items(), key=lambda x:x[1],reverse=True):
    print(f'{x}\t\t{y}')
