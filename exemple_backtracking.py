"""

Ce programme est une démonstration de résolution de sudoku grâce à un algorithme de backtracking.
Une fonction importe un fichier .txt dans lequel se trouve une grille de sudoku spécialement formatée.
La grille est convertie en tableau puis la classe SudokuSolver la résout et l'affiche dans le terminal 
avec les chiffres de la grille de départ en couleur.


"""

from sudoku_solver import Backtracking

def file_to_array(input_file):    
        """
        Cette fonction importe un fichier.txt et convertit la grille de sudoku qu'elle contient en un tableau
        pour être manipulable par la classe Backtracking.
        
        """
        created_board = []
        
        with open(input_file, "r", encoding='utf-8') as fichier: 
            for line in fichier:
                created_board.append(line.rstrip())
                
        for i in range(len(created_board)):
            created_board[i] = list(created_board[i].replace(u'_',u'0').strip())
            
        for i in range(len(created_board)):
            for j in range(len(created_board[i])):
                created_board[i][j] = int(created_board[i][j])
        return created_board        
        # print(created_board)


#Chargement des fichiers exemple
sudoku = file_to_array("/home/dennis/Dev/PythonDev/Divers/grilles_sudoku/sudoku.txt")
sudoku_2 = file_to_array("/home/dennis/Dev/PythonDev/Divers/grilles_sudoku/sudoku2.txt")
sudoku_3 = file_to_array("/home/dennis/Dev/PythonDev/Divers/grilles_sudoku/sudoku3.txt")
sudoku_4 = file_to_array("/home/dennis/Dev/PythonDev/Divers/grilles_sudoku/sudoku4.txt")
evil_sudoku = file_to_array("/home/dennis/Dev/PythonDev/Divers/grilles_sudoku/evilsudoku.txt")

s = Backtracking(sudoku)
sudoku_solve = s.solve()

