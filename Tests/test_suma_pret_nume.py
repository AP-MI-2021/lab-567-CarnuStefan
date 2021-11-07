from Domain.rezevare import creaza_rezervare
from Logic.suma_pret_nume import sum_price_name


def get_date():
    return [
        creaza_rezervare(1, "ex1", "economy", 123.4, "da"),
        creaza_rezervare(1, "ex1", "economy", 123.4, "da"),
        creaza_rezervare(2, "ex2", "economy plus", 225, "da"),
        creaza_rezervare(2, "ex2", "economy plus", 225, "da"),
        creaza_rezervare(2, "ex2", "economy plus", 225, "da"),
        creaza_rezervare(3, "ex3", "economy", 0, "da"),
        creaza_rezervare(3, "ex3", "economy", 0, "da"),
        creaza_rezervare(3, "ex3", "economy", 0, "da"),
        creaza_rezervare(4, "ex4", "business", 324.9, "nu"),
        creaza_rezervare(4, "ex4", "business", 32453656.9, "nu"),
        creaza_rezervare(4, "ex4", "business", 32412413.9, "nu"),
        creaza_rezervare(5, "ex5", "economy", 123.4, "nu"),
        creaza_rezervare(5, "ex5", "economy", -123.4, "nu"),
        creaza_rezervare(6, "ex6", "economy", 123.4, "da"),
        creaza_rezervare(7, "ex7", "economy plus", 225, "nu")
    ]


def test_sum_price_name():
    test_lst = get_date()
    result = sum_price_name(test_lst)
    assert result['ex1'] == 123.4+123.4
    assert result['ex2'] == 225+225+225
    assert result['ex3'] == 0
    assert result['ex4'] == 324.9+32453656.9+32412413.9
    assert result['ex5'] == 123.4-123.4
