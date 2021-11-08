from Domain.rezevare import creeaza_rezervare
from Logic.upgrade_clasa import upgrade_clasa


def get_date():
    return [
        creeaza_rezervare(1, "ex1", "economy", 123.4, "da"),
        creeaza_rezervare(2, "ex2", "economy plus", 225, "da"),
        creeaza_rezervare(3, "ex3", "economy", 123.4, "da"),
        creeaza_rezervare(4, "ex1", "business", 324.9, "nu"),
        creeaza_rezervare(5, "ex5", "economy", 123.4, "nu"),
        creeaza_rezervare(6, "ex3", "economy", 123.4, "da"),
        creeaza_rezervare(7, "ex7", "economy plus", 225, "nu")
    ]


def test_upgrade_clasa():
    lst_rezervari = get_date()
    rezervare = creeaza_rezervare(3, "ex3", "economy", 123.4, "da")
    rezervare_cu_upgrade = creeaza_rezervare(3, "ex3", "economy plus", 123.4, "da")
    rezervare_business = creeaza_rezervare(4, "ex1", "business", 324.9, "nu")
    lst_rezervari = upgrade_clasa(lst_rezervari, "ex1")
    lst_rezervari = upgrade_clasa(lst_rezervari, "ex3")
    assert rezervare not in lst_rezervari
    assert rezervare_cu_upgrade in lst_rezervari
    assert rezervare_business in lst_rezervari
