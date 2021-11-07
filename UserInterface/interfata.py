from Domain.rezevare import creaza_rezervare, get_detalii, get_nume, get_clasa, get_pret, get_checkin
from Logic.crud import adaug_rezervare, modifica_rezervare, sterge_rezervare, citeste_rezervare
from Logic.ieftinire import ieftinire
from Logic.ord_pret import ord_price
from Logic.pret_maxim_per_clasa import maxprice_class
from Logic.suma_pret_nume import sum_price_name
from Logic.upgrade_clasa import upgrade_clasa


def showmenu():
    print("1.Meniu CRUD")
    print("2.Upgrade clasa")
    print("3.Ieftinire")
    print("4.Determinare pret maxim pe clasa")
    print("5.Afisarea pretului total pentru fiecare nume cu rezervari")
    print("6.Ordonare crescatoare dupa pret")
    print("x.Inchidere")


def handle_adaugare(lst_rezervari):
    try:
        id_rezervare = int(input("Dati un id pentru rezervare: "))
        nume = input("Dati un nume pentru rezervare: ")
        clasa = input("Dati clasa rezervarii: ")
        while (clasa != "economy") & (clasa != "economy plus") & (clasa != "business"):
            print('Clasa invalida\nClasa poate fi doar: "economy"; "economy plus"; "business"\n')
            clasa = input("Dati clasa rezervarii: ")
            print(clasa)
        pret = float(input("Dati un pret pentru rezervare: "))
        checkin = input("Dati un status de checkin pentru rezervare: ")
        while (checkin != "da") & (checkin != "nu"):
            print('Checkin status invalid\nCheckin status poate fi doar : "da" sau "nu"\n')
            checkin = input("Dati un status de checkin pentru rezervare: ")
        return adaug_rezervare(lst_rezervari, id_rezervare, nume, clasa, pret, checkin)
    except ValueError as err:
        print('Eroare: ', err)
    return lst_rezervari


def handle_modificare(lst_rezervari):
    try:
        id_rezervare = int(input("Dati un id-ul rezervarii care trebuie schimbate: "))
        nume = input("Dati un nou nume pentru rezervare: ")
        clasa = input("Dati o noua clasa rezervarii: ")
        while (clasa != "economy") & (clasa != "economy plus") & (clasa != "business"):
            print('Clasa invalida\nClasa poate fi doar: "economy"; "economy plus"; "business"\n')
            clasa = input("Dati clasa rezervarii: ")
        pret = float(input("Dati un nou pret pentru rezervare: "))
        checkin = input("Dati un nou status de checkin pentru rezervare: ")
        while (checkin != "da") & (checkin != "nu"):
            print('Checkin status invalid\nCheckin status poate fi doar : "da" sau "nu"\n')
            checkin = input("Dati un status de checkin pentru rezervare: ")
        new_rezervare = creaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
        return modifica_rezervare(lst_rezervari, new_rezervare)
    except ValueError as err:
        print("Eroare: ", err)
    return lst_rezervari


def handle_stergere(lst_rezervari):
    try:
        id_rezervare = int(input("Dati un id-ul rezervarii care trebuie sterse: "))
        return sterge_rezervare(lst_rezervari, id_rezervare)
    except ValueError as err:
        print("Eroare: ", err)
    return lst_rezervari


def handle_afisare(lst_rezervari):
    for rezervare in lst_rezervari:
        print(get_detalii(rezervare))


def handle_detalii(lst_rezervari):
    id_rezervare = int(input("Dati id-ul rezervarii pentru care vreti detalii: "))
    rezervare = citeste_rezervare(lst_rezervari, id_rezervare)
    print(f'Nume:{get_nume(rezervare)}')
    print(f'Clasa:{get_clasa(rezervare)}')
    print(f'Pret:{get_pret(rezervare)}')
    print(f'Checkin facut:{get_checkin(rezervare)}')


def run_CRUDmenu(lst_rezervari):
    while True:
        print("1.Adaugare rezervare")
        print("2.Modificare rezervare")
        print("3.Stergere rezervare")
        print("a.Afisare lista rezervari")
        print("d.Afisare detalii rezervare")
        print("x.Inapoi")
        optiune = input("Alegeti optiunea:")
        if optiune == '1':
            lst_rezervari = handle_adaugare(lst_rezervari)
        elif optiune == '2':
            lst_rezervari = handle_modificare(lst_rezervari)
        elif optiune == '3':
            lst_rezervari = handle_stergere(lst_rezervari)
        elif optiune == 'a':
            handle_afisare(lst_rezervari)
        elif optiune == 'd':
            handle_detalii(lst_rezervari)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida")
    return lst_rezervari


def handle_upgrade(lst_rezervari):
    nume = input("Dati numele persoanei pentru care vreti sa faceti upgrade: ")
    while nume is None:
        nume = input("Dati numele persoanei pentru care vreti sa faceti upgrade: ")

    lst_rezervari = upgrade_clasa(lst_rezervari, nume)
    return lst_rezervari


def handle_ieftinire(lst_rezervari):
    try:
        procentaj = float(input("Introduceti procentajul cu care doriti sa ieftiniti: "))
        return ieftinire(lst_rezervari, procentaj)
    except ValueError as err:
        print("Eroare: ", err)
    return lst_rezervari


def handle_maxpret(lst_rezervari):
    max_pret = maxprice_class(lst_rezervari)
    for clasa in max_pret:
        print(clasa, ':', max_pret[clasa])


def run_ui(lst_rezervari):
    while True:
        showmenu()
        option = input("Alegeti optiunea: ")
        if option == '1':
            lst_rezervari = run_CRUDmenu(lst_rezervari)
        elif option == '2':
            lst_rezervari = handle_upgrade(lst_rezervari)
        elif option == '3':
            lst_rezervari = handle_ieftinire(lst_rezervari)
        elif option == '4':
            handle_maxpret(lst_rezervari)
        elif option == '5':
            print(sum_price_name(lst_rezervari))
        elif option == '6':
            lst_rezervari = ord_price(lst_rezervari)
        elif option == 'x':
            break
        else:
            print("Optiune invalida")
    return lst_rezervari
