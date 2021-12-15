from Domain.rezervare import *
from Domain.agentie import *
from Logic.crud import *

import itertools
def treceRezervariLaClasaSuperioaraPentruNumeCitit(agentie, nume):
    rezervari = get_list_curenta(agentie)
    for rez in rezervari:
        if getNume(rez) == nume:
            if getClasa(rez) == "economy":
                modificaRezervare(agentie, rez, getId(rez), getNume(rez), "economy plus", getPret(rez), getCheckinfacut(rez))
            elif getClasa(rez) == "economy plus":
                modificaRezervare(agentie, rez, getId(rez), getNume(rez), "business", getPret(rez), getCheckinfacut(rez))

def ieftinesteRezervariCuCheckinFacut(agentie, procentaj):
    rezervari = get_list_curenta(agentie)
    for rez in rezervari:
        if getCheckinfacut(rez) == True:
            modificaRezervare(agentie, rez, getId(rez), getNume(rez), getClasa(rez), getPret(rez) - procentaj/100 * getPret(rez), getCheckinfacut(rez))


def pretMaximFiecareClasa(agentie):
    rezervari = get_list_curenta(agentie)
    pretMaxEconomy = 0
    pretMaxEconomyPlus = 0
    pretMaxBussiness = 0
    for rez in rezervari:
        if getClasa(rez) == "economy" and getPret(rez) > pretMaxEconomy:
            pretMaxEconomy = getPret(rez)
        if getClasa(rez) == "economy plus" and getPret(rez) > pretMaxEconomyPlus:
            pretMaxEconomyPlus = getPret(rez)
        if getClasa(rez) == "bussiness" and getPret(rez) > pretMaxBussiness:
            pretMaxBussiness = getPret(rez)
    return pretMaxEconomy, pretMaxEconomyPlus, pretMaxBussiness

def Ordonarerezervaridescrescatordupapret(agentie):
    rezervari = get_list_curenta(agentie)
    copierezervari = rezervari
    copierezervari.sort(key =  lambda rezervare : rezervare['pret'])
    return copierezervari

def afisaresumepreturiptfiecarenume(agentie):
    rezervari = get_list_curenta(agentie)
    key_func = lambda rezervare: rezervare["nume"]
    for key, lista in itertools.groupby(rezervari, key_func):
        rezervariPerPersoana = list(lista)
        listaPreturi = list(map( lambda rezervare: rezervare['pret'],rezervariPerPersoana))
        print(key + " :" + str(sum(listaPreturi)))

def undo(agentie):
    lista_curenta = get_list_curenta(agentie)
    lista_undo = get_list_undo(agentie)
    if len(lista_undo) > 1:
        new_lista_curenta = lista_undo.pop()
        adaugare_lista_redo(agentie)
        set_lista_curenta(agentie, new_lista_curenta)
    else:
        raise Exception("No undo to do!")

def redo(agentie):
    lista_curenta = get_list_curenta(agentie)
    lista_redo = get_list_redo(agentie)
    if len(lista_redo) > 1:
        new_lista_curenta = lista_redo.pop()
        adaugare_lista_undo(agentie)
        set_lista_curenta(agentie, new_lista_curenta)
    else:
        raise Exception("No redo to do!")


