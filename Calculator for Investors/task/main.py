# write your code here
import CRUD_operations
from CRUD_operations import CRUDMenu
from TopTenMenu_operations import TopTenMenu
from dataBase_oprations import close_access
#import data_import

def open_CRUD_menu():
    CRUDMenu()


def open_TopTen_Menu():
    TopTenMenu()

if __name__ == '__main__':
    init = True
    while True:
        if init:
            print('Welcome to the Investor Program!MAIN MENU')
            init = False
        else:
            print('MAIN MENU')
        print('0 Exit\n1 CRUD operations\n2 Show top ten companies by criteria\nEnter an option:')
        input_code = input()
        match input_code:
            case '0':
                print('Have a nice day!')
                break
            case '1':
                open_CRUD_menu()
            case '2':
                open_TopTen_Menu()
            case _:
                print('Invalid option!')
    close_access()