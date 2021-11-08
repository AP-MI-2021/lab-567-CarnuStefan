def do_undo(lst_rezervari: list, lst_undo: list, lst_redo: list, ):
    """
    Face operatia de undo. Aduce lista la ultima stare inainte de orice operatie care modifica lista
    :param lst_rezervari: lista cu rezervari
    :param lst_undo: lista cu starile precedente
    :param lst_redo: lista cu starile inainte de undo
    :return: lista in starea in care se afla inainte de orice operatia care a modificat-o
    """
    if lst_undo:
        lst_redo.append(lst_rezervari)
        return lst_undo.pop()

    return None


def do_redo(lst_rezervari: list, lst_undo: list, lst_redo: list, ):
    """
    Face operatia de redo. Readuce lista la ultima stare inainte de undo.
    :param lst_rezervari: lista cu rezervari
    :param lst_undo:lista cu starile precedente
    :param lst_redo:lista cu starile inainte de undo
    :return: lista in starea in care se afla inainte de undo
    """
    if lst_redo:
        lst_undo.append(lst_rezervari)
        return lst_redo.pop()

    return None
