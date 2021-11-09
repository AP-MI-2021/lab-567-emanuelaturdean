import Logic.crud
import UserInterface.Meniu
import Domain.rezervare

if __name__ == '__main__':
    UserInterface.Meniu.afiseaza()
    rezervari = []
    n = int(input("Alege optiune:"))
    while n != 0:
        if n == 1:
            id = int(input("Id:"))
            nume = input("Nume:")
            clasa = input("Clasa:")
            pret = int(input("Pret:"))
            checkinfacut = bool(int(input("Checkin facut:")))
            Logic.crud.adaugaRezervare(rezervari, id, nume, clasa, pret, checkinfacut)
        if n == 2:
            id = int(input("Id:"))
            nume = input("Nume:")
            Logic.crud.stergeRezervare(rezervari, id, nume)
        if n == 3:
            for rez in rezervari:
                print("--")
                print(Domain.rezervare.getId(rez))
                print(Domain.rezervare.getNume(rez))
                print(Domain.rezervare.getClasa(rez))
                print(Domain.rezervare.getPret(rez))
                print(Domain.rezervare.getCheckinfacut(rez))
                print("--")
        UserInterface.Meniu.afiseaza()
        n = int(input("Alege optiune:"))