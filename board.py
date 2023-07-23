# from player import Player

class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.__data = self.__new_board()

    def display(self):
        for row in self.__data:
            print("\t".join(row))

    def __str__(self) -> str:
        res = ""
        for row in self.__data:
            res += "\t".join(row) + "\n"
        return res
    
    @property
    def data(self) -> list[list[str]]:
        return self.__data
    
    def reset(self):
        self.__data = self.__new_board()
    
    def __new_board(self) -> list[list[str]]:
        out = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append("")
            
            out.append(row)
        return out
    
    def mark(self, row: int, col: int, player: str) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError
        if self.__data[row][col] != "":
            raise ValueError
        self.__data[row][col] = player


    def is_draw(self) -> bool:
        for row in self.__data:
            for cell in row:
                if cell == "":
                    return False   
        return True

    def find_winner(self) -> list[list[int]]:
        ROW = len(self.__data)
        COL = len(self.__data[0])
        
        for r,row in enumerate(self.__data):
            if row[0] != "" and all([ v == row[0] for v in row ]):
                ans = []
                for c in range(COL):
                    ans.append([r, c])
                return ans
        
        for c in range(COL):
            col = [ self.__data[r][c] for r in range(ROW) ]
            if col[0] != "" and all([ v == col[0] for v in col ]):
                ans = []
                for r in range(ROW):
                    ans.append([r, c])
                return ans
    
            
        main_diag = [ self.__data[i][i] for i in range(ROW) ]
        if main_diag[0] != "" and all([ v == main_diag[0] for v in main_diag ]):
            ans = []
            for i in range(self.size):
                ans.append([i, i])
            return ans
        
        off_diag = [ self.__data[i][-i-1] for i in range(ROW) ]
        if off_diag[0] != "" and all([ v == off_diag[0] for v in off_diag ]):
            ans = []
            for i in range(self.size):
                ans.append([i, self.size-1-i])
            return ans
        
        return []
