from Tests.test_crud import test_crud
from Tests.test_ieftinire import test_ieftinire
from Tests.test_ordonare import test_ord_pret
from Tests.test_pret_maxim import test_maxprice_class
from Tests.test_suma_pret_nume import test_sum_price_name
from Tests.test_undo_redo import test_do_undo_redo
from Tests.test_upgrade_clasa import test_upgrade_clasa
from UserInterface.command_line_console import cmd_line
from UserInterface.interfata import run_ui


def main():
    lst_rezervari = []
    lst_undo = []
    lst_redo = []
    while True:
        print('1. Interfata clasica')
        print('2. Command_line interface')
        print('x. Inchidere')
        opt = input("Alegeti optiunea: ")
        if opt == '1':
            lst_rezervari = run_ui(lst_rezervari,lst_undo,lst_redo)
        elif opt == '2':
            lst_rezervari = cmd_line(lst_rezervari,lst_undo,lst_redo)
        elif opt == 'x':
            break
        else:
            print("Optiune invalida")


if __name__ == '__main__':
    test_do_undo_redo()
    test_ord_pret()
    test_sum_price_name()
    test_maxprice_class()
    test_ieftinire()
    test_crud()
    test_upgrade_clasa()
    main()
