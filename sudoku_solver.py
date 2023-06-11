import copy
from termcolor import colored



class Backtracking:
    
    """
    
    Cette classe résout une grille de sudoku et l'affiche dans le terminal
    avec les chiffres de la grille initiale en couleur
    
    """
    
    
    def __init__(self,input_array):
        
        self.input_array = input_array
        self.unsolved = copy.deepcopy(input_array)
        self.compteur = 0

    def print_grille(self,x,y):
        
        """
        La méthode print_board se charge de l'affichage de la solution.
        En vert les chiffres de la grille initiale, en blanc les chiffres trouvés pour la solution.
        """  
        
        print("L'algorithme de backtracking a résolu la grille de sudoku en", y,"essais.")
        print("\n")
        print("Voici le sudoku résolu avec en vert les chiffres de la grille de départ:")
        print("\n")
        
        for i in range(0, 9):
            for j in range(0, 9):
                print(str(x[i][j]) if self.unsolved[i][j] == 0 else colored(str(self.unsolved[i][j]), 'green'), end=" ")
            print()    

    
    def chiffre_unique(self,grille, ligne, col, val):
        
        """
        La méthode booléenne chiffre_unique() vérifie si un chiffre apparaît plus d'une fois dans chaque ligne, colonne
        et bloc 3x3 modulo 3, auquel cas elle renvoit False.
        """
        
        for j in range(0, 9):
            if grille[ligne][j] == val:
                return False

        for i in range(0, 9):
            if grille[i][col] == val:
                return False

        startLigne = (ligne // 3) * 3
        startCol = (col // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if grille[startLigne+i][startCol+j] == val:
                    return False

        return True      
          
    def solve(self):
        
        """
        La méthode solve() applique l'algorithme du backtracking. Elle rempli progressivement
        la grille de sudoku en essayant tous les chiffres de 1 à 9. 
        """
        self.compteur += 1
        self.grille = self.input_array
        
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grille[i][j] == 0:
                    for val in range(1, 10):
                        if self.chiffre_unique(self.grille, i, j, val):
                            self.grille[i][j] = val
                    
                            self.solve()
                    
                            # La solution ne fonctionne pas, on continue d'essayer avec une nouvelle grille.
                            self.grille[i][j] = 0  
                    return self.grille
        # On envoie la grille résolue et le compteurs du nombre d'essais à la méthode print_grille
        # pour l'affichage            
        self.print_grille(self.grille, self.compteur)


                
