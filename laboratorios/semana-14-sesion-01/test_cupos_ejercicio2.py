"""Pruebas del Ejercicio 2. La primera ya esta escrita. Escribe las demas
una a la vez, en este orden, y antes de cada una haz pasar la anterior:

1. Un estudiante sin reservas puede reservar.
2. Con 2 reservas en la semana, todavia puede.
3. Con 3 reservas en la semana, ya no puede.
4. Las reservas de otra semana no cuentan (2026-11-16 y 2026-11-23 son
   lunes de semanas distintas; 2026-11-22 es el domingo de la semana del 16).
5. Cancelar una reserva libera su lugar.
6. Un equipo oficial puede tener 6 reservas en la semana, pero no 7.
7. Registrar la cuarta reserva lanza ValueError (usa pytest.raises), y
   despues de intentarlo el estudiante sigue con 3.

Anota en la bitacora del README, por cada prueba: con que mensaje fallo,
que cambiaste para que pase, y que refactorizaste.
"""
import pytest
from cupos_ejercicio2 import CupoSemanal


def test_sin_reservas_puede_reservar():
    cupo = CupoSemanal()
    assert cupo.puede_reservar("ana", "2026-11-16")

def test_dos_reservas_puede_reservar():
   cupo = CupoSemanal()
   cupo.registrar("1", "Ana", "2026-11-16")
   cupo.registrar("2", "Ana", "2026-11-17")
   assert cupo.puede_reservar("Ana", "2026-11-18")

def test_tres_reservas_no_puede_reservar():
   cupo = CupoSemanal()
   cupo.registrar("1", "Charlie", "2026-11-16")
   cupo.registrar("2", "Charlie", "2026-11-17")
   cupo.registrar("3", "Charlie", "2026-11-18")

   assert cupo.puede_reservar("Charlie", "2026-11-19") == False

def test_reservas_otra_semana_no_cuentan():
   cupo = CupoSemanal()
   cupo.registrar("1", "Dani", "2026-11-16")
   cupo.registrar("2", "Dani", "2026-11-17")
   cupo.registrar("3", "Dani", "2026-11-23")
   
   assert cupo.puede_reservar("Dani", "2026-11-19") 

def test_cancelar_reserva_liberar_lugar():
   cupo = CupoSemanal()
   cupo.registrar("1", "Eli", "2026-11-16")
   cupo.registrar("2", "Eli", "2026-11-17")
   cupo.registrar("3", "Eli", "2026-11-18")
   cupo.registrar("4", "Eli", "2026-11-23")

   cupo.cancelar("4")
   assert not cupo.puede_reservar("Eli", "2026-11-19")

   cupo.cancelar("2")
   assert cupo.puede_reservar("Eli", "2026-11-19")

def test_equipo_oficial_seis_reservas():
   cupo = CupoSemanal()
   cupo.registrar_equipo_oficial("EquipoOficial")
   for i in range(6):
      cupo.registrar(f"EquipoOficial-{i}", "EquipoOficial", f"2026-11-{16+i}")
   
   assert cupo.puede_reservar("EquipoOficial", "2026-11-22") == False

def test_cuarta_reserva_lanza_valueerror():
   cupo = CupoSemanal()
   cupo.registrar("1", "Frank", "2026-11-16")
   cupo.registrar("2", "Frank", "2026-11-17")
   cupo.registrar("3", "Frank", "2026-11-18")

 
   with pytest.raises(ValueError, match="cupo semanal agotado"):
      cupo.registrar("4", "Frank", "2026-11-19")

   assert not cupo.puede_reservar("Frank", "2026-11-19")
   cupo.cancelar("1")
   assert cupo.puede_reservar("Frank", "2026-11-19")





