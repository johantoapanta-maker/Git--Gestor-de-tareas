from src.tarea import Tarea


class GestorTareas:
    """Administra la coleccion de tareas del sistema."""

    def __init__(self):
        self.tareas = []
        self._siguiente_id = 1

    def agregar_tarea(self, titulo):
        tarea = Tarea(self._siguiente_id, titulo)
        self.tareas.append(tarea)
        self._siguiente_id += 1
        return tarea

    def listar_tareas(self):
        for tarea in self.tareas:
            print(tarea)
        return self.tareas

    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                tarea.completada = True
                return tarea
        raise ValueError(f"No se encontro la tarea con id {id_tarea}")
        print("Hola soy johan")
