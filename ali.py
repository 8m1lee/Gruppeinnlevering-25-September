# Innleveringsoppave 2 - IS-118 - del 2
# konflikt håndtering i prosjekt


def les_valg(spm): 
    """ Leser A eller B fra brukeren (case-insensitive) """
    while True:
        S = input (spm + " (A/B): ").strip().upper()
        if S in ['A', 'B']:
            return S
        print ("skriv A eller B.")


def hoved ():
    print ("Du er Erling. Ta tre valg.\n")  

    # valg 1
    print ("1) konflikt mellom Silje og Sivert:")
    print (" A: Ta det åpent")
    print (" B: Ta det privat")
    v1 = les_valg ("velg")

    # valg 2
    print ("\n2) Hamdi og Jabir:")
    print (" A: Møte begge to")
    print (" B: La dem prøve selv")
    v2 = les_valg ("velg")

    # valg 3
    print ("\n3) Motivere teamet:")
    print (" A: Sosiale aktiviteter")
    print (" B: FOkus på arbeid")
    v3 = les_valg ("velg")


    # oppsummering
    print ("\nDine valg", v1, v2, v3, "\nResultat:")

    # minst tre utfall
    if v1 == 'A' and v2 == 'A' and v3 == 'A':
        print ("BEste utfall: Teamet blir bedre kjent og jobber godt sammen.")
    elif v3 == 'B' and ( v1 == 'B' or v2 == "B"):
        print ("Fremdrift, men noen samarbeidsproblemer kan bli værende.")
    elif v1 == 'A' and v2 == 'B' and v3 == 'A':
        print (" Delvis løsning: Åpenhet hjelper, men noen ting trenger mer tid.")
    elif v1 == 'B' and v2 == 'B' and v3 == 'B':
        print (" verst: Problemer holdes skjult og teamet kan miste motivasjon.")
    else: 
        print ("Blandet resultatet: Noe går godt, noe må følges opp senere.")

    print ("\nTakk for at du spilte!")

if __name__ == "__main__":
    hoved()
    

