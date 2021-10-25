from Logic.crud import adaug_rezervare


def showmenu():
    print("1.Meniu CRUD")
    print("x.Inchidere")


def handle_adaugare(lst_rezervari):
    id_rezervare = int(input("Dati un id pentru rezervare"))
    nume = input("Dati un nume pentru rezervare")
    clasa = input("Dati clasa rezervarii")
    pret = float(input("Dati un pret pentru rezervare"))
    checkin = input("Dati un status de checkin pentru rezervare")
    return adaug_rezervare(lst_rezervari,id_rezervare,nume,clasa,pret,checkin)


def handle_modificare(lst_rezervari):
    new_rezervare=int(input("Da"))


def run_CRUDmenu(lst_rezervari):
    while True:
        print("1.Adaugare rezervare")
        print("2.Modificare rezervare")
        print("3.Stergere rezervare")
        print("a.Afisare lista rezervari")
        print("x.Inapoi")
        optiune=input("Alegeti optiunea:")
        if optiune == '1':
            lst_rezervari = handle_adaugare(lst_rezervari)
        elif optiune == '2':
            lst_rezervari = handle_modificare(lst_rezervari)
        elif optiune == '3':
            pass
        elif optiune == 'a':
            pass
        elif optiune == 'x':
            break


def run_ui(lst_rezervari):
    while True:
        showmenu()
        option = input("Alegeti optiunea: ")
        if option == '1':
            run_CRUDmenu(lst_rezervari)
        elif option == 'x':
            break
    return lst_rezervari