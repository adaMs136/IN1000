import random

#lager en prosedyre som plasserer en bil og to geiter bak 3 "dører", nr. 1, 2 og 3
#prosedyren returnerer variabele bil med tallet til døren med bilen bak
#og listen geit som er en liste med dørene som har geiter bak seg
def lage_dorer():
    dorer = [1, 2, 3]
    bil = random.randint(1,3)
    geit = dorer.copy()
    geit.remove(bil)
    return(bil, geit)

#lager en prosedyre som har inn tre parametre. En for hvilken før bilen befinner seg bak, 
#en for hvilke dører geitene befinner seg bak og en for hvilken dør som er valgt (av en bruker eller automatisk)
#prosedyren "åpner" en dør med geit bak, og returnerer tallet på den åpne døren
def apne_dor(bil, geiter, valg):
    apen = [1,2,3]
    #dersom døren som er valgt ikke er den med bilen bak fjernes bil-døren og den valgte døren 
    #slik at døren som åpnes er den tredje
    if bil != valg:
        apen.remove(bil)
        apen.remove(valg)
        #apen vil her være en liste med et int element som må gjøres om til en int
        apen = int(apen[0])
    #om den valgte døren har bilen bak seg velges en tilfeldig dør blant de med geiter
    else:
        apen = random.choice(geiter)

    return(apen)

#lager en prosedyre som automatisk bytter den valgte døren til den som ikke er valgt og ikke åpnet
def bytte_dor(valg, apen):
    valgbar_dor = [1,2,3]
    valgbar_dor.remove(apen)
    valgbar_dor.remove(valg)
    #valgbar_dor vil her være en liste med et int element som må gjøres om til en int
    valgbar_dor = int(valgbar_dor[0])
    return(valgbar_dor)

#lager en prosedyre som evaluerer om den valgte døren har en bil eller geit bak seg
#dersom det skal ha skjedd noe feil vil den returnere stringen "error"
#jeg har laget denne spesifikt for å lagre den returnerte verdien til en liste, 
# det finns definitivt andre måter å gjøre det på :)
def resultat(bil, geiter, valg):
    if valg in geiter:
        return(False)
    elif valg == bil:
        return(True)
    else:
        return("error")

#definerer tomme lister for å lagre resultatene i     
resultater = []
resultater2 = []

#løkken under kjører spillet 100 ganger hvor døren ikke byttes
#resultatene lagres i en liste, telles opp og printes ut
#jeg la også inn en teller for å sjekke om spillet feilet, 
# men etter å ha kjørt programmet flere ganger fikk jeg konstant 0 error :D
for i in range(1000):
    bil, geiter = lage_dorer()
    valg = 1
    apen = apne_dor(bil, geiter, valg)

    resultater.append(resultat(bil, geiter, valg))
    ant_seiere = resultater.count(True)
    ant_tap = resultater.count(False)
    ant_error = resultater.count("error")

print("Statistikk når døren ikke byttes:")
print(f"Seiere: {ant_seiere}")
print(f"Tap: {ant_tap}")
#print(f"Error: {ant_error}")

#løkken under kjører spillet 100 ganger hvor døren byttes
#resultatene lagres i en liste, telles opp og printes ut
for i in range(1000):
    bil, geiter = lage_dorer()
    valg = 1
    apen = apne_dor(bil, geiter, valg)
    valg2 = bytte_dor(valg, apen)

    resultater2.append(resultat(bil, geiter, valg2))
    ant_seiere = resultater2.count(True)
    ant_tap = resultater2.count(False)
    ant_error = resultater2.count("error")

print("\nStatistikk når døren byttes:")
print(f"Seiere: {ant_seiere}")
print(f"Tap: {ant_tap}")
#print(f"Error: {ant_error}")