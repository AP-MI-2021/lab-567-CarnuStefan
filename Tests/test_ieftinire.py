from Domain.rezevare import creaza_rezervare
from Logic.ieftinire import ieftinire


def get_date():
    return [
        creaza_rezervare(1, "ex1", "economy", 123.4, "da"),
        creaza_rezervare(2, "ex2", "economy plus", 225, "da"),
        creaza_rezervare(3, "ex3", "economy", 0, "da"),
        creaza_rezervare(4, "ex4", "business", 324.9, "nu"),
        creaza_rezervare(5, "ex5", "economy", 123.4, "nu"),
        creaza_rezervare(6, "ex6", "economy", 123346.4, "da"),
        creaza_rezervare(7, "ex7", "economy plus", 225, "nu")
    ]


def test_ieftinire():
    lst_rezervari = get_date()
    copy_rezervare = creaza_rezervare(2, "ex2", "economy plus", 225, "da")
    copy_rezervare2 = creaza_rezervare(5, "ex5", "economy", 123.4, "nu")
    lst_ieftinita = ieftinire(lst_rezervari, 25)
    lst_ieftinita2 = ieftinire(lst_rezervari, 25.5555)
    lst_ieftinita3 = ieftinire(lst_rezervari, 100)
    assert copy_rezervare not in lst_ieftinita
    assert copy_rezervare not in lst_ieftinita2
    assert copy_rezervare2 in lst_ieftinita
    assert copy_rezervare2 in lst_ieftinita2
    rezervare_ieftinita = creaza_rezervare(2, "ex2", "economy plus", 225 - (25 / 100 * 225), "da")
    rezervare_ieftinita2 = creaza_rezervare(6, "ex6", "economy", 123346.4 - (25 / 100 * 123346.4), "da")
    rezervare_ieftinita3 = creaza_rezervare(6, "ex6", "economy", 123346.4 - (25.5555 / 100 * 123346.4), "da")
    rezervare_ieftinita4 = creaza_rezervare(6, "ex6", "economy", 0, "da")
    assert rezervare_ieftinita in lst_ieftinita
    assert rezervare_ieftinita2 in lst_ieftinita
    assert rezervare_ieftinita3 in lst_ieftinita2
    assert rezervare_ieftinita4 in lst_ieftinita3
    # Test eroare procentaj > 100 si procentaj is None
    try:
        _=ieftinire(lst_rezervari,)
        assert False
    except ValueError:
        assert True

    try:
        _=ieftinire(lst_rezervari,1000)
        _=ieftinire(lst_rezervari,100.1)
        assert False
    except ValueError:
        assert True
