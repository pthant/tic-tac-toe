from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from board import Board

app = FastAPI()
board = Board(3)

@app.get("/board")
def get_board() -> list[list[str]]:
    return board.data

class Move(BaseModel):
    row: int
    col: int
    player: str

@app.post("/board:move")
def set_move(move: Move):
    try:
        board.mark(move.row, move.col, move.player)
        return {"status": "Ok"}
    except:
        return {"status": "Invalid move"}

@app.get("/board:isdraw")
def is_draw() -> bool:
    return board.is_draw()

@app.get("/board:findwinner")
def find_winner():
    return board.find_winner()

@app.post("/board:reset")
def reset():
    board.reset()

app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
