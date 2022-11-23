
class User:

    def __init__(self, id, user, start_conection, end_conection, session_time, octetcs_in, octets_out, mac_ap, mac_client) -> None:
        self.id = id
        self.user = user
        self.start_conection = start_conection
        self.end_conection = end_conection
        self.session_time = session_time
        self.octects_in = octetcs_in
        self.octetcs_out = octets_out
        self.mac_ap = mac_ap
        self.mac_client = mac_client
    
    def __repr__(self):
            return f"ID: {self.id} USUARIO: {self.user} INICIO CONEXION: {self.start_conection} FIN CONEXCION:{self.end_conection} TIEMPO SESION: {self.session_time} OCTETOS INT: {self.octects_in} OCTETOS OUT: {self.octetcs_out} MAC AP: {self.mac_ap} MAC CLIENTE: {self.mac_client}"

    @staticmethod
    def create_object(line):
        id = line[0]
        user = line[1]
        start_conection = line[2]
        end_conection = line[3]
        session_time = line[4]
        octets_in = line[5]
        octets_out = line[6]
        mac_ap = line[7]
        mac_client = line[8]
        info_user = User(id, user, start_conection, end_conection, session_time, octets_in, octets_out, mac_ap, mac_client)
        return info_user
