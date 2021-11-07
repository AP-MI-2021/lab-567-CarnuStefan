from Domain.rezevare import creaza_rezervare
from Logic.crud import adaug_rezervare, modifica_rezervare, sterge_rezervare
from Logic.ieftinire import ieftinire
from Logic.ord_pret import ord_price
from Logic.suma_pret_nume import sum_price_name
from Logic.upgrade_clasa import upgrade_clasa
from UserInterface.interfata import handle_afisare, handle_detalii, handle_maxpret


def help_cmd():
    print("Comenzile posibile sunt:")
    print('Adaugare rezervare :\n -se face folosind "add" urmata de parametri in ordine "id,nume,clasa,pret,'
          'checkin" neaparat separat prin "," ')
    print('Modificare rezervare:\n -se face folosind "modify" urmata de parametri in ordine "id,nume,clasa,pret,'
          'checkin" neaparat separate prin "," ')
    print('Stergere rezervare:\n -se face folosind "delete" urmata de parametrul "id" neaparat separate prin ","')
    print('Afisarea rezervarilor:\n -se face folosind "showall"')
    print('Detaliere rezervare:\n -se face folosind "details" urmata de parametrul "id" neaparat separate prin ","')
    print('Upgrade:\n -se face folosind "upgrade" urmata de parametri in ordine "nume" neaparat separate prin ","')
    print('Ieftinirea rezervare:\n -se face folosind "sale" urmata de parametrul "procent" neaparat separate prin ","')
    print('Determinarea pretului maxim pentru fiecare clasa:\n -se face folosind "maxprice"')
    print('Afisarea sumei preturilor pentru toate rezervarile facute pe un nume:\n -se face folosind "total"')
    print('Ordonarea listei dupa preturile rezervarilor:\n -se face folosind "orderprice"')
    print('ATENTIE:\n -La finalul unei comenzi,imediat dupa ultiml parametru, se pune ";"')
    print(' -Folotsiti comanda "exit" pentru a iesi ')
    print(' -Folositi comanda "help" pentru a reafisa acest mesaj')


def cmd_line(lst_rezervari):
    help_cmd()
    while True:
        line = input("Introduceti comenzi:")
        comenzi = line.split(";")
        for comanda in comenzi:
            subcomenzi = comanda.split(",")
            try:
                if subcomenzi[0] == "add":
                    if len(subcomenzi) == 6:
                        lst_rezervari = adaug_rezervare(lst_rezervari, int(subcomenzi[1]), subcomenzi[2], subcomenzi[3],
                                                        float(subcomenzi[4]),
                                                        subcomenzi[5])
                    else:
                        print('Comanda "add" necesita 5 parametri')
                elif subcomenzi[0] == "modify":
                    if len(subcomenzi) == 6:
                        new_rezervare = creaza_rezervare(int(subcomenzi[1]), subcomenzi[2], subcomenzi[3],
                                                         float(subcomenzi[4]),
                                                         subcomenzi[5])
                        lst_rezervari = modifica_rezervare(lst_rezervari, new_rezervare)
                    else:
                        print('Comanda "modify" necesita 5 parametri')
                elif subcomenzi[0] == "delete":
                    if len(subcomenzi) == 2:
                        lst_rezervari = sterge_rezervare(lst_rezervari, int(subcomenzi[1]))
                    else:
                        print('Comanda "delete" necesita un parametru')
                elif subcomenzi[0] == "showall":
                    handle_afisare(lst_rezervari)
                elif subcomenzi[0] == "details":
                    handle_detalii(lst_rezervari)
                elif subcomenzi[0] == "upgrade":
                    if len(subcomenzi) == 2:
                        lst_rezervari = upgrade_clasa(lst_rezervari, subcomenzi[1])
                    else:
                        print('Comanda "upgrade" necesita un parametru')
                elif subcomenzi[0] == "sale":
                    if len(subcomenzi) == 2:
                        lst_rezervari = ieftinire(lst_rezervari, float(subcomenzi[1]))
                    else:
                        print('Comanda "sale" necesita un parametru')
                elif subcomenzi[0] == "maxprice":
                    handle_maxpret(lst_rezervari)
                elif subcomenzi[0] == "total":
                    print(sum_price_name(lst_rezervari))
                elif subcomenzi[0] == "orderprice":
                    lst_rezervari = ord_price(lst_rezervari)
                elif subcomenzi[0] == "exit":
                    return lst_rezervari
                elif subcomenzi[0] == "help":
                    help_cmd()
                elif subcomenzi[0] != '':
                    print(f'Comanda {subcomenzi[0]} este invalida')
            except ValueError as err:
                print("Eroare: ", err)
