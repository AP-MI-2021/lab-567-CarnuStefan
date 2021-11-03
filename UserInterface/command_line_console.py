from Domain.rezevare import creaza_rezervare
from Logic.crud import adaug_rezervare, modifica_rezervare, sterge_rezervare
from Logic.ieftinire import ieftinire
from Logic.upgrade_clasa import upgrade_clasa
from UserInterface.interfata import handle_afisare, handle_detalii


def help_cmd():
    print("Comenzile posibile sunt:")
    print('Adaugare rezervare : se face folosind "add" urmata de parametri in ordine "id,nume,clasa,pret,'
          'checkin" neaparat separat prin "," ')
    print('Modificare rezervare:se face folosind "modify" urmata de parametri in ordine "id,nume,clasa,pret,'
          'checkin" neaparat separate prin "," ')
    print('Stergere rezervare:se face folosind "delete" urmata de parametrul "id" neaparat separate prin ","')
    print('Afisarea rezervarilor:se face folosind "showall"')
    print('Detaliere rezervare:se face folosind "details" urmata de parametrul "id" neaparat separate prin ","')
    print('Upgrade:se face folosind "upgrade" urmata de parametri in ordine "nume" neaparat separate prin ","')
    print('Ieftinirea rezervare:se face folosind "sale" urmata de parametrul "procentaj" neaparat separate prin ","')
    print('ATENTIE: La finalul unei comenzi,imediat dupa ultiml parametru, se pune ";"')
    print('Folotsiti comanda "exit" pentru a iesi ')
    print('Folositi comanda "help" pentru a reafisa aceste mesaje')


def cmd_line(lst_rezervari):
    help_cmd()
    while True:
        line = input("Introduceti comenzi:")
        comenzi = line.split(";")
        for comanda in comenzi:
            subcomenzi = comanda.split(",")
            try:
                if subcomenzi[0] == "add":
                    lst_rezervari = adaug_rezervare(lst_rezervari, int(subcomenzi[1]), subcomenzi[2], subcomenzi[3],
                                                    subcomenzi[4],
                                                    subcomenzi[5])
                elif subcomenzi[0] == "modify":
                    new_rezervare = creaza_rezervare(int(subcomenzi[1]), subcomenzi[2], subcomenzi[3], subcomenzi[4],
                                                     subcomenzi[5])
                    lst_rezervari = modifica_rezervare(lst_rezervari, new_rezervare)
                elif subcomenzi[0] == "delete":
                    lst_rezervari = sterge_rezervare(lst_rezervari, int(subcomenzi[1]))
                elif subcomenzi[0] == "showall":
                    handle_afisare(lst_rezervari)
                elif subcomenzi[0] == "details":
                    handle_detalii(lst_rezervari)
                elif subcomenzi[0] == "upgrade":
                    lst_rezervari = upgrade_clasa(lst_rezervari, subcomenzi[1])
                elif subcomenzi[0] == "sale":
                    lst_rezervari = ieftinire(lst_rezervari, float(subcomenzi[1]))
                elif subcomenzi[0] == "exit":
                    return lst_rezervari
                elif subcomenzi[0] == "help":
                    help_cmd()
            except ValueError as err:
                print("Eroare: ", err)
