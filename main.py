from Tests.test_crud import test_crud
from UserInterface.interfata import run_ui


def main():
    lst_rezervari=[]
    lst_rezervari=run_ui(lst_rezervari)


if __name__=='__main__':
    test_crud()
    main()
