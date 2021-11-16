import Domain.rezervare

def adaugaRezervare(rezervari, id, nume, clasa, pret, checkinfacut):
    rez = Domain.rezervare.createRezervare(id, nume, clasa, pret, checkinfacut)
    rezervari.append(rez)

def stergeRezervare(rezervari, id, nume):
    for rez in rezervari:
        if Domain.rezervare.getId(rez) == id and Domain.rezervare.getNume(rez) == nume:
            rezervari.remove(rez)

def modificaRezervare(rezervari, rezervare, idnou, numenou, clasanoua, pretnou, checkinfacutnou):
    for rez in rezervari:
        if rez == rezervare:
            Domain.rezervare.setId(rezervare, idnou)
            Domain.rezervare.setNume(rezervare, numenou)
            Domain.rezervare.setClasa(rezervare, clasanoua)
            Domain.rezervare.setPret(rezervare, pretnou)
            Domain.rezervare.setCheckinfacut(rezervare, checkinfacutnou)
