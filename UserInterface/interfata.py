from Domain.rezevare import creaza_rezervare, get_detalii, get_nume, get_clasa, get_pret, get_checkin
from Logic.crud import adaug_rezervare, modifica_rezervare, sterge_rezervare, citeste_rezervare


def showmenu():
    print("1.Meniu CRUD")
    print("x.Inchidere")


def handle_adaugare(lst_rezervari):
    valid = True
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
    return adaug_rezervare(lst_rezervari,id_rezervare,nume,clasa,pret,checkin)


def handle_modificare(lst_rezervari):
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
    new_rezervare=creaza_rezervare(id_rezervare,nume,clasa,pret,checkin)
    return modifica_rezervare(lst_rezervari,new_rezervare)


def handle_stergere(lst_rezervari):
    id_rezervare = int(input("Dati un id-ul rezervarii care trebuie sterse: "))
    return sterge_rezervare(lst_rezervari,id_rezervare)


def handle_afisare(lst_rezervari):
    for rezervare in lst_rezervari:
        print(get_detalii(rezervare))


def handle_detalii(lst_rezervari):
    id_rezervare=int(input("Dati id-ul rezervarii pentru care vreti detalii: "))
    rezervare=citeste_rezervare(lst_rezervari,id_rezervare)
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
        optiune=input("Alegeti optiunea:")
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


def run_ui(lst_rezervari):
    while True:
        showmenu()
        option = input("Alegeti optiunea: ")
        if option == '1':
            run_CRUDmenu(lst_rezervari)
        elif option == 'x':
            break
        else:
            print("Optiune invalida")
    return lst_rezervari
