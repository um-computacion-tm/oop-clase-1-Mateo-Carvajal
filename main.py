from alumno import Alumno
from profesor import Profesor

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

profe_elio.dame_tu_nombre()
print(profe_gabi.dame_tu_nombre())

alumno_juan = Alumno("Juan")
alumno_Maria = Alumno("Maria")

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())

alumno_Maria.elegir_dieta_especial("vegetariana")
print(alumno_Maria.__dieta__)
alumno_juan.es_vegano()
print(alumno_juan.__dieta__)

alumno_juan.mentoria(profe_elio)
print(alumno_juan.__mentor__.dame_tu_nombre())

