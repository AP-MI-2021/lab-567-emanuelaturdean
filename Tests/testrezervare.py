import Domain.rezervare

def testrezervari():
    id = 1
    nume = "emma"
    casa = "business"
    pret = 100
    checkinfacut = True
    rez = Domain.rezervare.createRezervare(id, nume, casa, pret, checkinfacut)
    assert(Domain.rezervare.getId(rez) == 1)
    assert (Domain.rezervare.getNume(rez) == "emma")
    assert (Domain.rezervare.getClasa(rez) == "business")
    assert (Domain.rezervare.getPret(rez) == 100)
    assert (Domain.rezervare.getCheckinfacut(rez) == True)


