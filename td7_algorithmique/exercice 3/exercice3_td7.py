import chaines

mot = input("Entrez un mot: ").upper()
freq = chaines.frequences(mot)

for lettre, nb_apparitions in freq.items():
    print(f"'{lettre}' apparaît {nb_apparitions} fois")
