from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import basedatos as bd


class Tarea(BaseModel):
    texto: str


app = FastAPI()


@app.get("/tareas")
def listar():
    return bd.listar()


@app.get("/tareas/{id}")
def obtener(id: int):
    tarea = bd.obtener(id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@app.post("/tareas")
def crear(tarea: Tarea):
    nuevo_id = bd.añadir(tarea.texto)
    return {"id": nuevo_id, "texto": tarea.texto}


@app.delete("/tareas/{id}")
def borrar(id: int):
    if not bd.borrar(id):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"borrada": id}


@app.put("/tareas/{id}")
def actualizar(id: int, tarea: Tarea):
    if not bd.actualizar(id, tarea.texto):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"id": id, "texto": tarea.texto}
