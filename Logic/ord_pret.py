from Domain.rezevare import get_pret


def find_price(rezervare):
    return get_pret(rezervare)


def ord_price(lst_rezervari):
    return sorted(lst_rezervari, key=find_price)
