def creaza_rezervare(id_rezervare: int, nume, clasa, pret, checkin):
    """
    Creaza o rezervare
    :param id_rezervare: Identificator numeric pentru rezervare,Unic<trebuie sa fie int
    :param nume: Numele celui care a facut rezervarea
    :param clasa: Tipul de rezervare
    :param pret: Pretul rezervarii
    :param checkin: Daca s-a facut check-in sau nu
    :return: o rezervare
    """
    return [
        id_rezervare,
        nume,
        clasa,
        pret,
        checkin,
    ]


def get_id(rezervare):
    """
    Getter pentru id-ul unei rezervarii
    :param rezervare:
    :return: id-ul unei rezervarii
    """
    return rezervare[0]


def get_nume(rezervare):
    """
    Getter pentru numele unei rezervarii
    :param rezervare:
    :return: numele unei rezervari
    """
    return rezervare[1]


def get_clasa(rezervare):
    """
    Getter pentru clasa unei rezervarii
    :param rezervare:
    :return: lasa unei rezervari
    """
    return rezervare[2]


def get_pret(rezervare):
    """
    Getter pentru pretul unei rezervarii
    :param rezervare:
    :return: pretul unei rezervari
    """
    return rezervare[3]


def get_checkin(rezervare):
    """
    Getter pentru checkin-ul unei rezervarii
    :param rezervare:
    :return: checkin-ul unei rezrevari
    """
    return rezervare[4]


def get_detalii(rezervare):
    return f"Rezervarea cu id-ul {get_id(rezervare)}, facuta pe numele {get_nume(rezervare)}, " \
           f"la clasa {get_clasa(rezervare)}, cu pretul de {get_pret(rezervare)}," \
           f" care are starusul de checkin : {get_checkin(rezervare)}"
