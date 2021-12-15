from Domain.rezervare import *
from Domain.agentie import *

def adaugaRezervare(agentie, id, nume, clasa, pret, checkinfacut):
    rezervari = get_list_curenta(agentie)
    rez = createRezervare(id, nume, clasa, pret, checkinfacut)
    adaugare_lista_undo(agentie)
    goleste_list_redo(agentie)
    rezervari.append(rez)

def stergeRezervare(agentie, id, nume):
    rezervari = get_list_curenta(agentie)
    for rez in rezervari:
        if getId(rez) == id and getNume(rez) == nume:
            adaugare_lista_undo(agentie)
            goleste_list_redo(agentie)
            rezervari.remove(rez)

def modificaRezervare(agentie, rezervare, idnou, numenou, clasanoua, pretnou, checkinfacutnou):
    rezervari = get_list_curenta(agentie)
    for rez in rezervari:
        if rez == rezervare:
            adaugare_lista_undo(agentie)
            goleste_list_redo(agentie)
            setId(rezervare, idnou)
            setNume(rezervare, numenou)
            setClasa(rezervare, clasanoua)
            setPret(rezervare, pretnou)
            setCheckinfacut(rezervare, checkinfacutnou)
