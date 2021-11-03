from Tests.test_crud import test_crud
from Tests.test_ieftinire import test_ieftinire
from Tests.test_upgrade_clasa import test_upgrade_clasa
from UserInterface.command_line_console import cmd_line
from UserInterface.interfata import run_ui


def main():
    lst_rezervari = []
    while True:
        print('1. Interfata clasica')
        print('2. Command_line interface')
        print('x. Inchidere')
        opt = input("Alegeti optiunea: ")
        if opt == '1':
            lst_rezervari = run_ui(lst_rezervari)
        elif opt == '2':
            lst_rezervari = cmd_line(lst_rezervari)
        elif opt == 'x':
            break
        else:
            print("Optiune invalida")


if __name__ == '__main__':
    test_ieftinire()
    test_crud()
    test_upgrade_clasa()
    main()
