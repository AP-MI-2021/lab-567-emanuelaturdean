from copy import deepcopy


def create_agentie():
    return {
        'listaCurenta': [],
        'listaUndo' : [[]],
        'listaRedo' : [[]]
    }

def get_list_curenta(agentie):
    return agentie['listaCurenta']

def get_list_undo(agentie):
    return agentie['listaUndo']

def get_list_redo(agentie):
    return agentie['listaRedo']

def set_lista_curenta(agentie, lista_noua):
    agentie['listaCurenta'] = lista_noua

def adaugare_lista_undo(agentie):
    get_list_undo(agentie).append(deepcopy(get_list_curenta(agentie)))

def adaugare_lista_redo(agentie):
    get_list_redo(agentie).append(deepcopy(get_list_curenta(agentie)))

def goleste_list_redo(agentie):
    agentie['listaRedo'] = [[]]

