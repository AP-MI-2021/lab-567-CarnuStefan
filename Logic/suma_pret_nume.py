from Domain.rezevare import get_nume, get_pret


def sum_price_name(lst_rezervari):
    """
    
    :param lst_rezervari:
    :return:
    """
    sume_nume = {}
    for rez1 in lst_rezervari:
        if get_nume(rez1) not in sume_nume:
            suma = 0
            for rez2 in lst_rezervari:
                if get_nume(rez1) == get_nume(rez2):
                    suma = suma + get_pret(rez2)
            sume_nume[get_nume(rez1)] = suma
    return sume_nume
