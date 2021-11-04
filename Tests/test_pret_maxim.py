from Domain.rezevare import creaza_rezervare
from Logic.pret_maxim_per_clasa import maxprice_class


def get_date():
    return [
        creaza_rezervare(1, "ex1", "economy", 123.4, "da"),
        creaza_rezervare(2, "ex2", "economy plus", 2.123141232141232, "da"),
        creaza_rezervare(3, "ex3", "economy", 0, "da"),
        creaza_rezervare(4, "ex4", "business", 324.9, "nu"),
        creaza_rezervare(5, "ex5", "economy", -123.4, "nu"),
        creaza_rezervare(6, "ex6", "economy", 123346.4, "da"),
        creaza_rezervare(7, "ex7", "economy plus", 2.2, "nu")
    ]


def test_maxprice_class():
    lst_rest = get_date()
    preturi_maxime = maxprice_class(lst_rest)
    assert preturi_maxime['economy'] == 123346.4
    assert preturi_maxime['business'] == 324.9
    assert preturi_maxime['economy plus'] == 2.2
    assert len(preturi_maxime) == 3
