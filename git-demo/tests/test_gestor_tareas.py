from src.gestor_tareas import GestorTareas


def test_agregar_y_completar_tarea():
    gestor = GestorTareas()
    tarea = gestor.agregar_tarea("Investigar buenas practicas de Git")
    assert tarea.completada is False

    gestor.completar_tarea(tarea.id_tarea)
    assert gestor.tareas[0].completada is True
