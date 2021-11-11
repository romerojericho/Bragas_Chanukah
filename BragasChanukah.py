print("BRAGAS, EILA REIGN \n")

days = input("Enter number of days: ")
days = int(days)

shammas = days*(days+1)/2
shammas = int(shammas)

total = shammas+days
total = int(total)

print("Number of days/ordinary candles lit: " + str(days))
print("Number of shammas candles: " + str(shammas))
print("TOTAL NUMBER OF CANDLES LIT (ordinary candles + shammas): "+ str(total))

