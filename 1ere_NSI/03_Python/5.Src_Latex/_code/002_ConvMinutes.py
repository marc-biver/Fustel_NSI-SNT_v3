def conv_minutes(heures, minutes):
    minutes = minutes + heures * 60
    return minutes

resultat = conv_minutes(2, 30)

print("2 heures 30 font: ", resultat, " minutes")