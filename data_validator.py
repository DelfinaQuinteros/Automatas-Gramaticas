import re
from file_logic import FileDescriptor


class DataFilter:
    file_descriptor = FileDescriptor()

    @staticmethod
    def get_mac_ap(line):
        mac_ap = re.search('(^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):UM$)', line)
        try:
            return mac_ap.group(0)
        except:
            return None

    @staticmethod
    def get_mac(line):
        mac = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
        try:
            return mac.group(0)
        except:
            return None

    @staticmethod
    def get_conection_id(line):
        user_id = re.search('([\w\d]){16}', line)
        try:
            return user_id.group(0)
        except:
            return None

    def get_lines_by_user(self, user_id) -> list:
        lines = self.file_descriptor.read_file()
        list_lines = []
        for line in lines:
            line_splited = self.file_descriptor.show_line(line)
            if user_id == line_splited[1]:
                list_lines.append(line)
        return list_lines

    def get_lines_by_mac_ap(self, mac_ap: str) -> list:
        lines = self.file_descriptor.read_file()
        list_lines = []
        for line in lines:
            if re.findall(mac_ap, line):
                list_lines.append(line)
        return list_lines

    @staticmethod
    def get_line_by_conection_id(conection_id, lines):
        for line in lines:
            if re.findall(conection_id, line):
                return line

    @staticmethod
    def get_date(line) -> tuple:
        dates = re.search('((\d{2}/)+\d{4}) (\d{2}:\d{2})', line)
        try:
            return str(dates.group(0)), str(dates.group(1))
        except:
            return None, None

    @staticmethod
    def get_seconds(line: list) -> int:
        seconds = line[4]
        return int(seconds)

    @staticmethod
    def get_start_date(line: list) -> str:
        start_date = line[2]
        return str(start_date)

    @staticmethod
    def get_end_date(line: list) -> str:
        end_date = line[3]
        return str(end_date)

    @staticmethod
    def get_input_date(input):
        date = re.search('^((\d{2}/)+(\d{2}/)+\d{4}) (\d{2}:\d{2})$', input)
        try:
            return str(date.group(0))
        except:
            return None

    @staticmethod
    def get_input_user(user):
        user = re.search('([a-z])', user)
        try:
            return str(user.group(0))
        except:
            return None
