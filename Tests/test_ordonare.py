from Domain.rezevare import creeaza_rezervare, get_pret
from Logic.ord_pret import ord_price


def get_date():
    return [
        creeaza_rezervare(1, "ex1", "economy", 123.4, "da"),
        creeaza_rezervare(2, "ex2", "economy plus", 225, "da"),
        creeaza_rezervare(3, "ex3", "economy", 0, "da"),
        creeaza_rezervare(4, "ex4", "business", 324.9, "nu"),
        creeaza_rezervare(5, "ex5", "economy", 123.4, "nu"),
        creeaza_rezervare(6, "ex6", "economy", 123346.4, "da"),
        creeaza_rezervare(7, "ex7", "economy plus", 225, "nu")
    ]


def test_ord_pret():
    lst_test = get_date()
    lst_ordonata = ord_price(lst_test)
    ultima_rezervare = creeaza_rezervare(6, "ex6", "economy", 123346.4, "da")
    assert lst_test[0] != lst_ordonata[0]
    assert lst_ordonata[6] == ultima_rezervare
    assert get_pret(lst_ordonata[0]) <= get_pret(lst_ordonata[1])
    assert get_pret(lst_ordonata[1]) <= get_pret(lst_ordonata[2])
    assert get_pret(lst_ordonata[2]) <= get_pret(lst_ordonata[3])
    assert get_pret(lst_ordonata[3]) <= get_pret(lst_ordonata[4])
    assert get_pret(lst_ordonata[4]) <= get_pret(lst_ordonata[5])
    assert get_pret(lst_ordonata[5]) <= get_pret(lst_ordonata[6])
