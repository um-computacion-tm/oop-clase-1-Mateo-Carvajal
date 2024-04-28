class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def mentoria(self, profesor):
        self.__mentor__ = profesor

    def falta(self):
        self.__inasistencias__ += 1

    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "vegano"

    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"
