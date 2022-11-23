from constant import *
from functions import FileService
import sys


def read_option():
    file_service = FileService()
    opt = int(input("Ingrese una opción: "))
    options = {
        0: sys.exit,
        1: file_service.get_all_user_sessions,
        2: file_service.get_sessions_by_user_and_date,
        3: file_service.sesion_time,
        4: file_service.get_macs_by_user,
        5: file_service.get_users_by_macap_and_date,
    }
    return options[opt]()

        #return sys.exit()


if __name__ == '__main__':
    while True:
        print(MAIN)
        print(read_option())
