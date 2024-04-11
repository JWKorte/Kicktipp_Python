import pandas as pd
import matplotlib.pyplot as plt
blt_platzierungen = pd.read_html("https://www.kicktipp.de/xyz/gesamtuebersicht?ansicht=platzierungen&")[0]                      # Statt xyz Tipprunde
tipper = ["x", "y", "z"]                                                                                                        # Statt x,y,z Namen der Tipper 
blt_platzierungen = blt_platzierungen.set_index(blt_platzierungen["Name"]).drop(["Pos","Name","Re","S","G"], axis=1).transpose()
for tipp in tipper:
    blt_platzierungen[tipp].plot(title="Platzierung", legend=True, figsize=(10,10), ylim=(40,0))
plt.show()    
