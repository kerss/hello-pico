bestandsnaam = "voorbeeld_csv.txt"

# 'w' = write (schrijven nieuw bestand)
with open(bestandsnaam, 'w') as file:
    regel_tekst = 'tijd, temperatuur, luchtvochtigheid\n'
    file.write(regel_tekst)

tijd = 0.1
meetwaarde1 = 240.231
meetwaarde2 = 2

# 'a' = appenden (toevoegen)
with open(bestandsnaam, 'a') as file:
    regel_tekst = str(tijd) + ',' + str(meetwaarde1) + ',' + str(meetwaarde2) + '\n'
    file.write(regel_tekst)
