import re


class FileDescriptor:

    @staticmethod
    def read_file():
        archivo = open('Usuarios WiFi.txt', "r")
        lines = archivo.readlines()
        lines.pop(0)
        archivo.close()
        return lines

    @staticmethod
    def show_line(line):
        line = list(re.split(r';', line))
        return line
