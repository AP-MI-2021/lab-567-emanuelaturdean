def createRezervare(id, nume, clasa, pret, checkinfacut):
    return {
        "id" : id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkinfacut": checkinfacut
    }

def getId(rezervare):
    return rezervare['nume']

def getNume(rezervare):
    return rezervare['nume']

def getClasa(rezervare):
    return rezervare['clasa']

def getPret(rezervare):
    return rezervare['pret']

def getCheckinfacut(rezervare):
    return rezervare['checkinfacut']

def setId(rezervare, idnou):
    rezervare['id'] = idnou

def setNume(rezervare, numenou):
    rezervare['nume'] = numenou

def setClasa(rezervare, clasanoua):
    rezervare['clasa'] = clasanoua

def setPret(rezervare, pretnou):
    rezervare['pret'] = pretnou

def setCheckinfacut(rezervare, checkinfacutnou):
    rezervare['checkinfacut'] = checkinfacutnou