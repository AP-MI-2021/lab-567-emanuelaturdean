from Logic.crud import *
from Logic.functionalitati import *
from Tests.testfunctionalitati import *
from Tests.testrezervare import *
from UserInterface.Meniu import *
from Domain.rezervare import *
import sys

def printRezervari(agentie):
    rezervari = get_list_curenta(agentie)
    for rez in rezervari:
        print("--")
        print(getId(rez))
        print(getNume(rez))
        print(getClasa(rez))
        print(getPret(rez))
        print(getCheckinfacut(rez))
        print("--")

def mainNormal():
    afiseaza()
    agentie = create_agentie()
    n = 0
    adaugaRezervare(agentie, 1, "Deni", "economy", 100, True)
    adaugaRezervare(agentie, 2, "Emma", "bussiness", 13, False)
    adaugaRezervare(agentie, 3, "Emma", "economy", 50, True)
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
                adaugaRezervare(agentie, id, nume, clasa, pret, checkinfacut)
            except (ValueError):
                print("eroare")
        elif n == 2:
            try:
                id = int(input("Id:"))
                nume = input("Nume:")
                stergeRezervare(agentie, id, nume)
            except (ValueError):
                print("eroare")
        elif n == 3:
            printRezervari(agentie)
        elif n == 4:
            nume = input("Nume rezervare:")
            treceRezervariLaClasaSuperioaraPentruNumeCitit(agentie, nume)
        elif n == 5:
            try:
                procentaj = int(input("Procentaj:"))
                ieftinesteRezervariCuCheckinFacut(agentie, procentaj)
            except ValueError:
                print("Eroare")
        elif n == 6:
            pmaxeconomy, pmaxeconomyplus, pmaxbussiness = pretMaximFiecareClasa(agentie)
            print("Pret max economy:", pmaxeconomy)
            print("Pret max economy plus:", pmaxeconomyplus)
            print("Pret max bussiness:", pmaxbussiness)
        elif n == 7:
            agentiesortate = Ordonarerezervaridescrescatordupapret(agentie)
            printRezervari(agentiesortate)
        elif n==8:
            afisaresumepreturiptfiecarenume(agentie)
        elif n == 9:
            try:
                undo(agentie)
            except Exception as exception:
                print(exception)
        elif n == 10:
            try:
                redo(agentie)
            except Exception as exception:
                print(exception)
        elif n == 11:
            testupgraderezervarepentrunume()
            testrezervari()
            testieftinesterezervaricuprocentaj()
            testpretmaximfiecarezbor()
        else:
            print("Incorect")
        afiseaza()
        try:
            n = int(input("Alege optiune:"))
        except ValueError:
            print("Eroare")
            n = int(input("Alege optiune:"))

def mainLinieComanda():
    agentie = []
    n = 0
    adaugaRezervare(agentie, 1, "Alex", "economy", 100, True)
    adaugaRezervare(agentie, 2, "Emma", "bussiness", 13, False)
    adaugaRezervare(agentie, 3, "Emma", "economy", 50, True)
    argument = sys.argv[1]
    arguments = argument.split(',')
    if arguments[0] == "add":
        if len(arguments) != 6:
            print("eroare")
        else:
            adaugaRezervare(agentie, arguments[1], arguments[2], arguments[3], arguments[4], arguments[5])
        printRezervari(agentie)
    elif arguments[0] == "showall":
        printRezervari(agentie)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mainLinieComanda()
    else:
        mainNormal()
