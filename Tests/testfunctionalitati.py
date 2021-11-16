import Domain.rezervare
import Logic.functionalitati
import Logic.crud

def testupgraderezervarepentrunume():
    rezervari = []
    Logic.crud.adaugaRezervare(rezervari, 1, "Deni", "economy", 100, True)
    Logic.crud.adaugaRezervare(rezervari, 2, "Emma", "bussiness", 13, False)
    Logic.crud.adaugaRezervare(rezervari, 3, "Emma", "economy", 50, True)
    numedetrecut = "Emma"
    Logic.functionalitati.treceRezervariLaClasaSuperioaraPentruNumeCitit(rezervari, numedetrecut)
    assert (Domain.rezervare.getClasa(rezervari[0]) == "economy")
    assert (Domain.rezervare.getClasa(rezervari[1]) == "bussiness")
    assert (Domain.rezervare.getClasa(rezervari[2]) == "economy plus")

def testieftinesterezervaricuprocentaj():
    rezervari = []
    Logic.crud.adaugaRezervare(rezervari, 1, "Deni", "economy", 100, True)
    Logic.crud.adaugaRezervare(rezervari, 2, "Emma", "bussiness", 13, False)
    Logic.crud.adaugaRezervare(rezervari, 3, "Emma", "economy", 50, True)
    procentaj = 20
    Logic.functionalitati.ieftinesteRezervariCuCheckinFacut(rezervari, procentaj)
    assert (Domain.rezervare.getPret(rezervari[0]) == 80)
    assert (Domain.rezervare.getPret(rezervari[1]) == 13)
    assert (Domain.rezervare.getPret(rezervari[2]) == 40)

def testpretmaximfiecarezbor():
    rezervari = []
    Logic.crud.adaugaRezervare(rezervari, 1, "Deni", "economy", 100, True)
    Logic.crud.adaugaRezervare(rezervari, 2, "Emma", "bussiness", 13, False)
    Logic.crud.adaugaRezervare(rezervari, 3, "Emma", "economy", 50, True)
    Logic.crud.adaugaRezervare(rezervari, 4, "Emma", "economy plus", 65, True)
    peconmy, peconomyplus, pbussiness = Logic.functionalitati.pretMaximFiecareClasa(rezervari)
    assert (peconmy == 100)
    assert (peconomyplus == 65)
    assert (pbussiness == 13)



