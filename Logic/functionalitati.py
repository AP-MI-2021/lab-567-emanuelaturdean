import Domain.rezervare

def treceRezervariLaClasaSuperioaraPentruNumeCitit(rezervari, nume):
    for rez in rezervari:
        if Domain.rezervare.getNume(rez) == nume:
            if Domain.rezervare.getClasa(rez) == "economy":
                Domain.rezervare.setClasa(rez, "economy plus")
            elif Domain.rezervare.getClasa(rez) == "economy plus":
                Domain.rezervare.setClasa(rez, "bussiness")

def ieftinesteRezervariCuCheckinFacut(rezervari, procentaj):
    for rez in rezervari:
        if Domain.rezervare.getCheckinfacut(rez) == True:
            Domain.rezervare.setPret(rez, Domain.rezervare.getPret(rez) - procentaj/100 * Domain.rezervare.getPret(rez))

def pretMaximFiecareClasa(rezervari):
    pretMaxEconomy = 0
    pretMaxEconomyPlus = 0
    pretMaxBussiness = 0
    for rez in rezervari:
        if Domain.rezervare.getClasa(rez) == "economy" and Domain.rezervare.getPret(rez) > pretMaxEconomy:
            pretMaxEconomy = Domain.rezervare.getPret(rez)
        if Domain.rezervare.getClasa(rez) == "economy plus" and Domain.rezervare.getPret(rez) > pretMaxEconomyPlus:
            pretMaxEconomyPlus = Domain.rezervare.getPret(rez)
        if Domain.rezervare.getClasa(rez) == "bussiness" and Domain.rezervare.getPret(rez) > pretMaxBussiness:
            pretMaxBussiness = Domain.rezervare.getPret(rez)
    return pretMaxEconomy, pretMaxEconomyPlus, pretMaxBussiness