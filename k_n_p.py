import random

   

    # Vytvorte list moznosti
moznosti = ["kamen", "nuzky", "papir"]
    
    # Vytvorte promennou hrac
while (hrac := input("Zadej volbu:..., nebo ukonči 'q'. ")) != "q":
        # Vytvorte promennou pocitac
    pocitac = random.choice(moznosti)
        # Vytisknete volbu cloveka a pocitace
    print("Hráč:",hrac,"\n"+"Počítač:", pocitac)
        # Vytvorte podminku, zda hrac zvolil platnou volbu
    if hrac in moznosti:
        pass
    else:
        print("Neplatná volba.")
    # Pokud je volba v poradku, muzeme provest zbytek programu


    if hrac == "kamen" and pocitac == "kamen":
            print("!!!Nerozhodně:")
    elif hrac == "nuzky" and pocitac == "nuzky": 
            print("Nerozhodně:")
    elif hrac == "papir" and pocitac == "papir":
            print("Nerozhodně:")
    elif hrac == "kamen" and pocitac == "nuzky":
            print("Prohrál jsi :(")
    elif hrac == "kamen" and pocitac == "papir":
            print("Prohrál jsi :(")
    elif hrac == "nuzky" and pocitac == "papir":
            print("Vyhrál jsi :)")
    elif hrac == "papir" and pocitac == "nuzky":
        print("Vyhrál jsi :)")
    elif hrac == "papir" and pocitac == "kamen":
        print("Vhrál jsi :)")
