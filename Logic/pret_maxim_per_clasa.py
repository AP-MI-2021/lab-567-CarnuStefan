from Domain.rezevare import get_clasa, get_pret


def maxprice_class(lst_rezervari):
    """
    Functia ia toate clasele rezervarilor din lst rezervari si le pune intr-un dictionar drept chei. Pentru fiecare
    clasa se determina pretul maxim si se salveaza la cheia corespunzatoare
    :param lst_rezervari: lista cu rezervari
    :return: Un dictionar cu clasele drept chei si preturile maximime drept valori
    """
    max_pret = {}
    for rezervare in lst_rezervari:
        if get_clasa(rezervare) not in max_pret:
            max_pret[get_clasa(rezervare)] = get_pret(rezervare)
        elif get_pret(rezervare) > max_pret[get_clasa(rezervare)]:
            max_pret[get_clasa(rezervare)] = get_pret(rezervare)
    return max_pret
