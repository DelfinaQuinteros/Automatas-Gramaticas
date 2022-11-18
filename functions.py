import datetime
from data_validator import DataFilter
from file_logic import FileDescriptor
from user import User


def input_function(*args) -> dict:
    inputs: list = {}
    for arg in args:
        user_input = input(f"Ingrese {arg}: ")
        inputs[arg] = user_input
    return inputs


class FileService:
    get_data = DataFilter()
    file_descriptor = FileDescriptor()

    def get_macs_by_user(self, user_id=None) -> set:
        user_id = str(input("Ingrese el usuario: "))
        macs: list = []
        lines = self.get_data.get_lines_by_user(user_id)
        for line in lines:
            mac = self.get_data.get_mac(line)
            macs.append(mac)
        macs_user = len(set(macs))
        return f"El usuario se ha conectado a {macs_user} dispositivos", set(macs)

    def sesion_time(self):
        user_id = str(input("Ingrese el user: "))
        lines = self.get_data.get_lines_by_user(user_id)
        time = 0
        for line in lines:
            time += self.get_data.get_seconds(self.file_descriptor.show_line(line))
        time = datetime.timedelta(seconds=time)
        return f"El usuario {user_id} estuvo conectado por {time}"

    def get_all_user_sessions(self, user_id=None) -> list:
        user_id = str(input("Ingrese usuario: "))
        user_lines = self.get_data.get_lines_by_user(user_id)
        user_sessions = []
        for line in user_lines:
            try:
                id_conection = self.get_data.get_conection_id(line)
                user_sessions.append(id_conection)
            except:
                pass
        return f'El usuario {user_id} tiene {len(user_sessions)} sesiones', user_sessions

    def get_by_date_range(self, type_get) -> list:
        data_input = input_function("fecha inicio", "fecha fin", "usuario/mac")
        lines = type_get(data_input["usuario/mac"])
        results = []
        for line in lines:
            date = self.get_data.get_date(line)
            date = datetime.datetime.strptime(date[0], "%d/%m/%Y %H:%M")
            start_date = datetime.datetime.strptime(data_input["fecha inicio"], "%d/%m/%Y %H:%M")
            end_date = datetime.datetime.strptime(data_input["fecha fin"], "%d/%m/%Y %H:%M")
            if start_date <= date <= end_date:
                register = User.create_object(line=self.file_descriptor.show_line(line))
                results.append(register)
            if end_date == date:
                break
        return results

    def get_sessions_by_user_and_date(self) -> list:
        user = self.get_data.get_lines_by_user
        objects = self.get_by_date_range(user)
        return f"Inicios de sesion del usuario en un periodo de tiempo son: {len([o.id for o in objects])}", [o.id for o in objects]

    def get_users_by_macap_and_date(self) -> list:
        mac = self.get_data.get_lines_by_mac_ap
        objects = self.get_by_date_range(mac)
        return f"Usuarios que accedieron a la MAC AP en un periodo de tiempo son: {len([o.user for o in objects])}", [o.user for o in objects]
