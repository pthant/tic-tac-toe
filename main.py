from typing import Optional
from board import Board
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

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

