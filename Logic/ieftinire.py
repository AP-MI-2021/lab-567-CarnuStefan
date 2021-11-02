from Domain.rezevare import get_checkin, get_pret, creaza_rezervare, get_id, get_nume, get_clasa


def ieftinire(lst_rezervari, procentaj: float = None):
    """
    Cauta in lista rezervarile la care checkin-ul este "da" si il ieftineste cu procentajul dat
    :param lst_rezervari: lista cu rezervari
    :param procentaj: procentaj
    :return:O noua lista cu rezervarile ieftinite
    """
    result = []
    if (procentaj is None) or (procentaj > 100):
        raise ValueError(f'Nu se poate ieftini cu un procentaj de {procentaj}%')
    for rezervare in lst_rezervari:
        descazut = (procentaj / 100) * get_pret(rezervare)
        if get_checkin(rezervare) == "da":
            rezervare_ieftinita = creaza_rezervare(get_id(rezervare), get_nume(rezervare), get_clasa(rezervare),
                                                   get_pret(rezervare) - descazut, get_checkin(rezervare))
            result.append(rezervare_ieftinita)
        else:
            result.append(rezervare)
    return result
