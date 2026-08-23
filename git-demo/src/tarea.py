class Tarea:
    """Representa una tarea dentro del sistema de gestión de tareas."""

    def __init__(self, id_tarea, titulo, completada=False):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.completada = completada

    def __repr__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"[{self.id_tarea}] {self.titulo} - {estado}"
