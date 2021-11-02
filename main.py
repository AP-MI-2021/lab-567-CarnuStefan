from Tests.test_crud import test_crud
from Tests.test_ieftinire import test_ieftinire
from Tests.test_upgrade_clasa import test_upgrade_clasa
from UserInterface.interfata import run_ui


def main():
    lst_rezervari = []
    lst_rezervari = run_ui(lst_rezervari)


if __name__ == '__main__':
    test_ieftinire()
    test_crud()
    test_upgrade_clasa()
    main()
