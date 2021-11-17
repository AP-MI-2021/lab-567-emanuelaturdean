import Logic.crud
import Logic.functionalitati
import Tests.testfunctionalitati
import Tests.testrezervare
import UserInterface.Meniu
import Domain.rezervare
import sys

def printRezervari(rezervari):
    for rez in rezervari:
        print("--")
        print(Domain.rezervare.getId(rez))
        print(Domain.rezervare.getNume(rez))
        print(Domain.rezervare.getClasa(rez))
        print(Domain.rezervare.getPret(rez))
        print(Domain.rezervare.getCheckinfacut(rez))
        print("--")

def mainNormal():
    UserInterface.Meniu.afiseaza()
    rezervari = []
    n = 0
    Logic.crud.adaugaRezervare(rezervari, 1, "Alex", "economy", 100, True)
    Logic.crud.adaugaRezervare(rezervari, 2, "Emma", "bussiness", 13, False)
    Logic.crud.adaugaRezervare(rezervari, 3, "Emma", "economy", 50, True)
    try:
        n = int(input("Alege optiune:"))
    except ValueError:
        print("Eroare")
        n = int(input("Alege optiune:"))
    while n != 0:
        if n == 1:
            try:
                id = int(input("Id:"))
                nume = input("Nume:")
                clasa = input("Clasa:")
                pret = int(input("Pret:"))
                checkinfacut = bool(int(input("Checkin facut:")))
                Logic.crud.adaugaRezervare(rezervari, id, nume, clasa, pret, checkinfacut)
            except (ValueError):
                print("eroare")
        elif n == 2:
            try:
                id = int(input("Id:"))
                nume = input("Nume:")
                Logic.crud.stergeRezervare(rezervari, id, nume)
            except (ValueError):
                print("eroare")
        elif n == 3:
            printRezervari(rezervari)
        elif n == 4:
            nume = input("Nume rezervare:")
            Logic.functionalitati.treceRezervariLaClasaSuperioaraPentruNumeCitit(rezervari, nume)
        elif n == 5:
            try:
                procentaj = int(input("Procentaj:"))
                Logic.functionalitati.ieftinesteRezervariCuCheckinFacut(rezervari, procentaj)
            except ValueError:
                print("Eroare")
        elif n == 6:
            pmaxeconomy, pmaxeconomyplus, pmaxbussiness = Logic.functionalitati.pretMaximFiecareClasa(rezervari)
            print("Pret max economy:", pmaxeconomy)
            print("Pret max economy plus:", pmaxeconomyplus)
            print("Pret max bussiness:", pmaxbussiness)
        elif n == 7:
            Tests.testfunctionalitati.testupgraderezervarepentrunume()
            Tests.testrezervare.testrezervari()
            Tests.testfunctionalitati.testieftinesterezervaricuprocentaj()
            Tests.testfunctionalitati.testpretmaximfiecarezbor()
        else:
            print("Incorect")
        UserInterface.Meniu.afiseaza()
        try:
            n = int(input("Alege optiune:"))
        except ValueError:
            print("Eroare")
            n = int(input("Alege optiune:"))

def mainLinieComanda():
    rezervari = []
    n = 0
    Logic.crud.adaugaRezervare(rezervari, 1, "Alex", "economy", 100, True)
    Logic.crud.adaugaRezervare(rezervari, 2, "Emma", "bussiness", 13, False)
    Logic.crud.adaugaRezervare(rezervari, 3, "Emma", "economy", 50, True)
    argument = sys.argv[1]
    arguments = argument.split(',')
    if arguments[0] == "add":
        if len(arguments) != 6:
            print("eroare")
        else:
            Logic.crud.adaugaRezervare(rezervari, arguments[1], arguments[2], arguments[3], arguments[4], arguments[5])
        printRezervari(rezervari)
    elif arguments[0] == "showall":
        printRezervari(rezervari)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mainLinieComanda()
    else:
        mainNormal()
