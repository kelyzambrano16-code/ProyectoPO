# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from typing import List
from servicio import Servicio


class GestorServicios:
    """
    Clase auxiliar/gestor que contiene operaciones polimórficas sobre listas
    de objetos Servicio.
    """

    def _init_(self):
        self._servicios = []

    def agregar_servicio(self, servicio: Servicio):
        if not isinstance(servicio, Servicio):
            raise ValueError("El objeto debe heredar de Servicio")
        self._servicios.append(servicio)

    def listar_servicios(self) -> List[Servicio]:
        return list(self._servicios)

    # Método polimórfico 1
    def sumar_costos(self, servicios: List[Servicio]) -> float:
        """
        Suma los costos de cualquier lista de objetos que hereden de Servicio.
        """
        total = 0.0
        for s in servicios:
            total += s.calcular_costo()
        return round(total, 2)

    # Metodo polimorfico 2
    def generar_reporte(self, servicios: List[Servicio]) -> str:
        """
        Genera un reporte textual con cada servicio y su costo calculado.
        No pregunta el tipo; usa polimorfismo.
        """
        lines = ["--- Reporte de Servicios ---"]
        for s in servicios:
            lines.append(f"{s.mostrar_info()} -> costo: {s.calcular_costo()}")
        lines.append(f"Total servicios: {len(servicios)}")
        lines.append(f"Total acumulado: {self.sumar_costos(servicios)}")
        return "\n".join(lines)