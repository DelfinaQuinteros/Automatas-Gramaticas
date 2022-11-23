from data_validator import DataFilter


class Input:
    get_data = DataFilter()

    def input_user_dates(self) -> dict:
        inputs: dict = {}
        counter = 0
        while counter == 0:
            user_input = input(f"Ingrese fecha inicio: ")
            if self.get_data.get_input_date(user_input):
                inputs['fecha inicio'] = user_input
                counter = 1
            else:
                print('Formato de fecha inválido (dd/mm/aaaa hh:mm).')
        counter = 0
        while counter == 0:
            user_input = input(f"Ingrese fecha finalización: ")
            if self.get_data.get_input_date(user_input):
                inputs['fecha fin'] = user_input
                counter = 1
            else:
                print('Formato de fecha inválido (dd/mm/aaaa hh:mm).')
        counter = 0
        while counter == 0:
            user_input = input(f"Ingrese usuario: ")
            if self.get_data.get_input_user(user_input):
                inputs['user'] = user_input
                counter = 1
            else:
                print('El nombre de usuario debe contener alguna letra minúscula.')
        return inputs

    def input_mac_dates(self) -> dict:
        inputs: dict = {}
        counter = 0
        while counter == 0:
            user_input = input(f"Ingrese fecha inicio: ")
            if self.get_data.get_input_date(user_input):
                inputs['fecha inicio'] = user_input
                counter = 1
            else:
                print('Formato de fecha inválido (dd/mm/aaaa hh:mm).')
        counter = 0
        while counter == 0:
            user_input = input(f"Ingrese fecha finalización: ")
            if self.get_data.get_input_date(user_input):
                inputs['fecha fin'] = user_input
                counter = 1
            else:
                print('Formato de fecha inválido (dd/mm/aaaa hh:mm).')
        counter = 0
        while counter == 0:
            mac_input = input(f"Ingrese la dirección MAC de un AP: ")
            if self.get_data.get_mac_ap(mac_input):
                inputs['mac'] = mac_input
                counter = 1
            else:
                print('El formato de la dirección MAC del AP es incorrecto (XX:XX:XX:XX:XX:XX:UM).')
        return inputs

    def input_user(self):
        counter = 0
        while counter == 0:
            user_id = str(input("Ingrese usuario: "))
            if self.get_data.get_input_user(user_id):
                user_lines = self.get_data.get_lines_by_user(user_id)
                counter = 1
            else:
                print('El nombre de usuario debe contener alguna letra minúscula.')
        return user_lines, user_id

    def input_mac_of_user(self):
        counter = 0
        while counter == 0:
            user_id = str(input("Ingrese usuario: "))
            if self.get_data.get_input_user(user_id):
                user_lines = self.get_data.get_lines_by_user(user_id)
                counter = 1
            else:
                print('El nombre de usuario debe contener alguna letra minúscula.')
        return user_lines, user_id
