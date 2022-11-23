import datetime
from data_validator import DataFilter
from file_logic import FileDescriptor
from user import User
from input import Input


class FileService:
    get_data = DataFilter()
    file_descriptor = FileDescriptor()
    input = Input()

    def get_macs_by_user(self):
        lines = self.input.input_user()
        macs: list = []
        for line in lines[0]:
            mac = self.get_data.get_mac(line)
            macs.append(mac)
        macs_user = len(set(macs))
        if macs_user == 0:
            return f"El usuario no existe."
        return f"El usuario {lines[1]} se ha conectado desde {macs_user} dispositivos", set(macs)

    def sesion_time(self):
        lines = self.input.input_user()
        time = 0
        for line in lines[0]:
            time += self.get_data.get_seconds(self.file_descriptor.show_line(line))
        time = datetime.timedelta(seconds=time)
        return f"El usuario {lines[1]} estuvo conectado por {time}"

    def get_all_user_sessions(self):
        user_lines = self.input.input_user()
        user_sessions = []
        for line in user_lines[0]:
            id_conection = self.get_data.get_conection_id(line)
            user_sessions.append(id_conection)
        if len(user_sessions) == 0:
            return f'No existe el usuario {user_lines[1]}'
        else:
            return f'El usuario {user_lines[1]} tiene {len(user_sessions)} sesiones', user_sessions

    def get_by_date_range(self, type_get, type_str):
        if type_str == 'user':
            data_input = self.input.input_user_dates()
            lines = type_get(data_input["user"])
        else:
            data_input = self.input.input_mac_dates()
            lines = type_get(data_input["mac"])
        results = []
        for line in lines:
            date = self.get_data.get_date(line)
            #Este if es para corregir un error, ya que a veces la tupla fecha tiene el primer elemento como None, y eso provoca error
            if date[0] is not None:
                date = datetime.datetime.strptime(date[0], "%d/%m/%Y %H:%M")
                start_date = datetime.datetime.strptime(data_input["fecha inicio"], "%d/%m/%Y %H:%M")
                end_date = datetime.datetime.strptime(data_input["fecha fin"], "%d/%m/%Y %H:%M")
                if start_date <= date <= end_date:
                    register = User.create_object(line=self.file_descriptor.show_line(line))
                    results.append(register)
                if end_date == date:
                    break
        return results, lines

    def get_sessions_by_user_and_date(self):
        user = self.get_data.get_lines_by_user
        objects = self.get_by_date_range(user, 'user')
        if len(objects[1]) == 0:
            return f"El usuario no existe."
        if len(objects[0]) == 0:
            return f"El usuario no posee sesiones entre las fechas especificadas."
        return f"Inicios de sesion del usuario en un periodo de tiempo son: {len([o.id for o in objects[0]])}", [o.id for o in objects[0]]

    def get_users_by_macap_and_date(self):
        mac = self.get_data.get_lines_by_mac_ap
        objects = self.get_by_date_range(mac, 'mac')
        return f"Usuarios que accedieron a la MAC AP en un periodo de tiempo son: {len([o.user for o in objects[0]])}", [o.user for o in objects[0]]
