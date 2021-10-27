from Domain.rezevare import creaza_rezervare, get_id
from Logic.crud import adaug_rezervare, citeste_rezervare, modifica_rezervare, sterge_rezervare


def get_date():
    return [
        creaza_rezervare(1,"ex1","economy",123.4,"da"),
        creaza_rezervare(2,"ex2","economy plus",225,"da"),
        creaza_rezervare(3,"ex3","economy",123.4,"da"),
        creaza_rezervare(4,"ex4","business",324.9,"nu"),
        creaza_rezervare(5,"ex5","economy",123.4,"nu"),
        creaza_rezervare(6,"ex6","economy",123.4,"da"),
        creaza_rezervare(7,"ex7","economy plus",225,"nu")
            ]


def test_adaug():
    lst_rezervari=get_date()
    params = (8, 'ex8-nou', "economy", 125, "nu")
    new_rezervare=creaza_rezervare(*params)
    new_lst_rezervari=adaug_rezervare(lst_rezervari,*params)
    assert new_rezervare in new_lst_rezervari


def test_citire():
    lst_rezervari=get_date()
    rezervare_de_gasit=lst_rezervari[3]
    assert citeste_rezervare(lst_rezervari,get_id(rezervare_de_gasit)) == rezervare_de_gasit
    assert citeste_rezervare(lst_rezervari,None) == lst_rezervari


def test_modificare():
    lst_rezervari=get_date()
    rezervare_modificata=creaza_rezervare(1, 'ex1-modificat', "business", 325, "da")
    modificat=modifica_rezervare(lst_rezervari, rezervare_modificata)
    assert rezervare_modificata in modificat
    assert rezervare_modificata not in lst_rezervari
    assert len(modificat) == len(lst_rezervari)


def test_stergere():
    lst_rezervari = get_date()
    de_sters = 5
    este_sters = citeste_rezervare(lst_rezervari, de_sters)
    lst_sters = sterge_rezervare(lst_rezervari, de_sters)
    assert este_sters not in lst_sters
    assert este_sters in lst_rezervari
    assert len(lst_rezervari)-1 == len(lst_sters)


def test_crud():
    test_adaug()
    test_modificare()
    test_citire()
    test_stergere()
