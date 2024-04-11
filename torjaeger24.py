print("\n","Vollautomatischer Torjaeger-Tipp-Zwischenstand", "\n")
import pandas as pd
torjaeger = pd.read_html("https://www.sport.de/fussball/deutschland-bundesliga/torjaeger/", encoding=("utf-8"))[0]
Tipps ={"Tipper_a":{"Tipp_a":0, "Tipp_b":0, "Tipp_c":0},                                                              # Statt Tipper_a,b,c Namen der Tippenden
        "Tipper_b":{"Tipp_a":0, "Tipp_b":0, "Tipp_c":0},                                                    # Statt Tipp_a,b,c die Namen exakt wie bei sport.de
       "Tipper_c":{"Tipp_a":0, "Tipp_b":0, "Tipp_c":0}}
for tipper in Tipps.keys():
    for tipp in Tipps[tipper]:
        if tipp in list(torjaeger["Spieler"]):
            Tipps[tipper][tipp]=torjaeger[torjaeger["Spieler"]==tipp].values[0,7]
for tipper,tipper2 in zip(list(Tipps.keys())[:4], list(Tipps.keys())[4:8]):
    print(f'{tipper}\t{sum(Tipps[tipper].values())}\t\t\t{tipper2}\t{sum(Tipps[tipper2].values())}')
    for tipps, tipps2 in zip(Tipps[tipper].items(),Tipps[tipper2].items()): 
            print(f'{tipps}\t\t{tipps2}')
    print("\n")
    