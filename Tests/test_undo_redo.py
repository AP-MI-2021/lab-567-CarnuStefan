from Domain.rezevare import creeaza_rezervare, get_pret
from Logic.crud import adaug_rezervare, modifica_rezervare, sterge_rezervare
from Logic.ieftinire import ieftinire
from Logic.ord_pret import ord_price
from Logic.undo_redo import do_undo, do_redo
from Logic.upgrade_clasa import upgrade_clasa


def test_do_undo_redo():
    lst_test = []
    lst_undo_test = []
    lst_redo_test = []
    lst_test = adaug_rezervare(lst_test, 1, "ex1", 'economy', 1, 'da', lst_undo_test, lst_redo_test)
    lst_test = adaug_rezervare(lst_test, 2, "ex2", 'economy', 12, 'da', lst_undo_test, lst_redo_test)
    lst_test = adaug_rezervare(lst_test, 3, "ex3", 'economy', 123, 'da', lst_undo_test, lst_redo_test)
    lst_test = adaug_rezervare(lst_test, 4, "ex4", 'economy', 1234, 'da', lst_undo_test, lst_redo_test)
    # adaugare
    rezervare_id4 = creeaza_rezervare(4, "ex4", 'economy', 1234, 'da')
    assert rezervare_id4 in lst_test
    lst_test = do_undo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_id4 not in lst_test
    lst_test = do_redo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_id4 in lst_test
    # modificare
    rezervare_modificata = creeaza_rezervare(4, 'modificat', 'business', 1234, 'da')
    lst_test = modifica_rezervare(lst_test, rezervare_modificata, lst_undo_test, lst_redo_test)
    assert rezervare_modificata in lst_test
    assert rezervare_id4 not in lst_test
    lst_test = do_undo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_modificata not in lst_test
    assert rezervare_id4 in lst_test
    lst_test = do_redo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_modificata in lst_test
    assert rezervare_id4 not in lst_test
    # stergere
    rezervare_id1 = creeaza_rezervare(1, 'ex1', 'economy', 1, 'da')
    lst_test = sterge_rezervare(lst_test, 1, lst_undo_test, lst_redo_test)
    assert rezervare_id1 not in lst_test
    lst_test = do_undo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_id1 in lst_test
    lst_test = do_redo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_id1 not in lst_test
    # ieftinire
    rezervare_ieftinita = creeaza_rezervare(4, 'modificat', 'business', (1234 - (10 / 100) * 1234), 'da')
    lst_test = ieftinire(lst_test, 10, lst_undo_test, lst_redo_test)
    assert rezervare_ieftinita in lst_test
    lst_test = do_undo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_ieftinita not in lst_test
    assert rezervare_modificata in lst_test
    lst_test = do_redo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_ieftinita in lst_test
    assert rezervare_modificata not in lst_test
    # upgrade clasa
    lst_test = adaug_rezervare(lst_test, 5, "forupgrade", 'economy', 150, 'da', lst_undo_test, lst_redo_test)
    rezervare_faraupgrade = creeaza_rezervare(5, "forupgrade", 'economy', 150, 'da')
    rezervare_cuupgrade = creeaza_rezervare(5, "forupgrade", 'economy plus', 150, 'da')
    lst_test = upgrade_clasa(lst_test, "forupgrade", lst_undo_test, lst_redo_test)
    assert rezervare_faraupgrade not in lst_test
    assert rezervare_cuupgrade in lst_test
    lst_test = do_undo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_faraupgrade in lst_test
    assert rezervare_cuupgrade not in lst_test
    lst_test = do_redo(lst_test, lst_undo_test, lst_redo_test)
    assert rezervare_faraupgrade not in lst_test
    assert rezervare_cuupgrade in lst_test
    # ordonare dupa pret
    lst_test = adaug_rezervare(lst_test, 6, "prim", 'economy', 0, 'da', lst_undo_test, lst_redo_test)
    lst_test = ord_price(lst_test, lst_undo_test, lst_redo_test)
    assert get_pret(lst_test[0]) == 0
    lst_test = do_undo(lst_test, lst_undo_test, lst_redo_test)
    assert get_pret(lst_test[0]) != 0
    lst_test = do_redo(lst_test, lst_undo_test, lst_redo_test)
    assert get_pret(lst_test[0]) == 0
    # Teste dupa exemplul din laborator
    lista_de_rezervari = []
    lista_undo = []
    lista_redo = []
    o1 = creeaza_rezervare(1, "o1", "economy", 102, "da")
    o2 = creeaza_rezervare(2, "o2", "economy plus", 212, "da")
    o3 = creeaza_rezervare(3, "o3", "business", 98, "nu")
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 1, "o1", "economy", 102, "da", lista_undo, lista_redo)
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 2, "o2", "economy plus", 212, "da", lista_undo, lista_redo)
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 3, "o3", "business", 98, "nu", lista_undo, lista_redo)
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 not in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 not in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 1, "o1", "economy", 102, "da", lista_undo, lista_redo)
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 2, "o2", "economy plus", 212, "da", lista_undo, lista_redo)
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 3, "o3", "business", 98, "nu", lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    o4 = creeaza_rezervare(4, "o4", "business", 9.8, "da")
    lista_de_rezervari = adaug_rezervare(lista_de_rezervari, 4, "o4", "business", 9.8, "da", lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 not in lista_de_rezervari
    lista_de_rezervari = do_undo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 not in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 not in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 not in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 in lista_de_rezervari
    lista_de_rezervari = do_redo(lista_de_rezervari, lista_undo, lista_redo)
    assert o1 in lista_de_rezervari
    assert o2 not in lista_de_rezervari
    assert o3 not in lista_de_rezervari
    assert o4 in lista_de_rezervari
