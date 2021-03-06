# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:56:22 2021

@author: taiga
"""

import random
import tkinter as tk
import math

class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frameCan = tk.Frame(self)
        self.frameCan.pack(side='top')
        self.canvas = tk.Canvas(self.frameCan,width=600,height=480,bg='white')
        self.canvas.bind("<Button-1>",self.onClick_souris) # <Button-1> : Bouton gauche de la souris 
        self.canvas.pack()
        self.canvas.create_line(200,0,200,479)
        self.canvas.create_line(400,0,400,479)
        self.canvas.create_line(0,160,599,160)
        self.canvas.create_line(0,320,599,320)
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(side='bottom')
        self.morpion = Morpion(self)
        self.listButton = []

        self.zoneTexte = tk.Label(self, text='CLICK ON NEW PARTY', background='palegreen')
        self.zoneTexte.pack(side='top', padx=5, pady=5)

        self.frameButton = tk.Frame(self, background='gray')
        self.frameButton.pack(side='top', padx=5, pady=5)
        self.listButton = []

        self.buttonNP = tk.Button(self.frameButton, text='New party', command=self.nouvelle_partie)
        self.buttonNP.pack(side='left', padx=5, pady=5)
        self.listButton.append(self.buttonNP)

        self.buttonNoir = tk.Button(self.frameButton, text='cross', command=self.choixNoir)
        self.buttonNoir.pack(side='left', padx=5, pady=5)
        self.buttonNoir.config(state='disabled')
        self.listButton.append(self.buttonNoir)

        self.buttonBlanc = tk.Button(self.frameButton, text='circle', command=self.choixBlanc)
        self.buttonBlanc.pack(side='left', padx=5, pady=5)
        self.buttonBlanc.config(state='disabled')
        self.listButton.append(self.buttonBlanc)

        self.buttonQuit = tk.Button(self.frameButton, text='Quit', command=self.destroy)
        self.buttonQuit.pack(side='left', padx=5, pady=5)
        self.listButton.append(self.buttonQuit)

        self.humain = False
        self.liste_cases = []
        self.liste_cases_opposee = []
        # Cr??ation de la liste des cases pour y tracer les formes
        for j in range(3):
            for i in range(3):
                self.liste_cases.append([i * 201, j * 161, i * 201 + 198, j * 161 + 158])
                # Permet de tracer les cross facilement
                self.liste_cases_opposee.append([i * 201, j * 161 + 159, i * 201 + 199, j * 161])

        self.zoneCompteur = tk.Label(self, text='Number of turns : ' + str(self.morpion.compteur), background='sandybrown')
        self.zoneCompteur.pack(side='bottom', padx=5, pady=5)
        
        ################################################################################
        self.combinedFrames = tk.Frame(self)
        self.combinedFrames.pack(side="bottom")
        self.frameModes = tk.Frame(self.combinedFrames, background='gray')
        self.frameModes.pack(side='left', padx=5, pady=5)

        self.choixMode = 'aucun'

        self.button2 = tk.Button(self.frameModes, text='IA vs IA', command = self.AIvsAI)
        self.button2.pack(side='left', padx=5, pady=5)
        self.button2.config(state='disabled')
        self.listButton.append(self.button2)

        self.button3 = tk.Button(self.frameModes, text='Human vs IA', command = self.HumanVSAI)
        self.button3.pack(side='left', padx=5, pady=5)
        self.button3.config(state='disabled')
        self.listButton.append(self.button3)

        self.button4 = tk.Button(self.frameModes, text='Human vs Human', command = self.HumanVSHuman)
        self.button4.pack(side='left', padx=5, pady=5)
        self.button4.config(state='disabled')
        self.listButton.append(self.button4)
        

        #################################################################################
        self.frameAI = tk.Frame(self.combinedFrames, background='gray')
        self.frameAI.pack(side='left', padx=5, pady=5)

        self.AI = 'aucune'

        self.button5 = tk.Button(self.frameAI, text='without IA', command = self.noAI)
        self.button5.pack(side='left', padx=5, pady=5)
        self.button5.config(state='disabled')
        self.listButton.append(self.button5)

        self.button6 = tk.Button(self.frameAI, text='Best First', command = self.bestFirst)
        self.button6.pack(side='left', padx=5, pady=5)
        self.button6.config(state='disabled')
        self.listButton.append(self.button6)

        self.button7 = tk.Button(self.frameAI, text='MinMax', command = self.minMax)
        self.button7.pack(side='left', padx=5, pady=5)
        self.button7.config(state='disabled')
        self.listButton.append(self.button7)

                
        self.morpion.reset()
        
    def reset(self):
        self.morpion.reset()

    def nouvelle_partie(self):
        self.morpion.is_active = False
        self.zoneCompteur.config(text='Number of turns: ' + str(self.morpion.compteur))
        self.choixMode = 'aucun'
        self.AI = 'aucune'
        self.morpion.reset()
        self.zoneCompteur.config(text='Number of turns: ' + str(self.morpion.compteur))
        self.button2.config(state='disabled',relief='raised')
        self.button3.config(state='disabled',relief='raised')
        self.button4.config(state='disabled',relief='raised')
        self.button5.config(state='disabled',relief='raised')
        self.button6.config(state='disabled',relief='raised')
        self.button7.config(state='disabled',relief='raised')
        self.buttonBlanc.config(state='normal')
        self.buttonNoir.config(state='normal')
        self.zoneTexte.config(text='Select the piece to play',background='pink')
        self.update()

    def choixNoir(self):
        self.morpion.joueur='cross'
        self.morpion.reset()
        self.buttonNoir.config(state='disabled')
        self.buttonBlanc.config(state='disabled')
        self.button2.config(state='normal')
        self.button3.config(state='normal')
        self.button4.config(state='normal')
        self.zoneTexte.config(text="Select the game mode",background='yellow')
        self.update()

    def choixBlanc(self):
        self.morpion.joueur='circl'
        self.morpion.reset()
        self.buttonNoir.config(state='disabled')
        self.buttonBlanc.config(state='disabled')
        self.button2.config(state='normal')
        self.button3.config(state='normal')
        self.button4.config(state='normal')
        self.zoneTexte.config(text="Select the game mode",background='yellow')
        self.update()

    
    def AIvsAI(self):
        self.button2.config(relief='flat')
        self.button3.config(state='disabled')
        self.button4.config(state='disabled')
        if self.choixMode == 'aucun':
            if self.AI == 'aucune':
                self.choixMode = 'AIVSAI'
                self.choixIA()
        else:
            self.zoneTexte.config(text="The AI plays for you!", background='cyan')
            self.morpion.is_active = True
            self.morpion.AIvsAI()
        
    def HumanVSAI(self):
        self.button2.config(state='disabled')
        self.button3.config(relief='flat')
        self.button4.config(state='disabled')
        if self.choixMode == 'aucun':
            if self.AI == 'aucune':
                self.choixMode = 'HVSAI'
                self.choixIA()
        else:
            self.zoneTexte.config(text="You're fighting against the AI ! Align 3 " + self.morpion.joueur + "es to win!", background='cyan')
            self.morpion.is_active = True
            self.morpion.HumanVSAI()
        
    def HumanVSHuman(self):
        self.button2.config(state='disabled')
        self.button3.config(state='disabled')
        self.button4.config(relief='flat')
        if self.choixMode == 'aucun':
            self.choixMode = 'HVSH'
            self.zoneTexte.config(text='Play alternatively!',background='cyan')
            self.morpion.is_active = True
            self.morpion.HumanVSHuman()

    def choixIA(self):
        if self.choixMode == 'AIVSAI':
            self.button5.config(state='normal')
            self.button6.config(state='normal')
            self.button7.config(state='normal')
            self.zoneTexte.config(text="Choose the intelligente of the AI!", background='yellow')
        elif self.choixMode == 'HVSAI':
            self.button5.config(state='normal')
            self.button6.config(state='normal')
            self.button7.config(state='normal')
            self.zoneTexte.config(text="Choose the intelligente of the AI!", background='yellow')
        
    def noAI(self):
        if self.AI == 'aucune':
            self.AI = 'noAI'
            self.button5.config(relief='flat')
            self.button6.config(state='disabled')
            self.button7.config(state='disabled')
            self.morpion.noAI()
            if self.choixMode == 'AIVSAI':
                self.AIvsAI()
            elif self.choixMode == 'HVSAI':
                self.HumanVSAI()
        
    def bestFirst(self):
        if self.AI == 'aucune':
            self.AI = 'bestFirst'
            self.button5.config(state='disabled')
            self.button6.config(relief='flat')
            self.button7.config(state='disabled')
            self.morpion.bestFirst()
            if self.choixMode == 'AIVSAI':
                self.AIvsAI()
            elif self.choixMode == 'HVSAI':
                self.HumanVSAI()
        
    def minMax(self):
        if self.AI == 'aucune':
            self.AI = 'minMax'
            self.button5.config(state='disabled')
            self.button6.config(state='disabled')
            self.button7.config(relief='flat')
            self.morpion.minMax()
            if self.choixMode == 'AIVSAI':
                self.AIvsAI()
            elif self.choixMode == 'HVSAI':
                self.HumanVSAI()

    def tracer(self, forme, case, color):
        # Trace la forme dans la case, circl ou cross
        try:
            assert self.morpion.is_active, "Choose a form to play"
            if forme == 'circl':
                self.canvas.create_oval(*(self.liste_cases[case]), outline=color)
            else:
                self.canvas.create_line(*(self.liste_cases[case]), fill=color)
                self.canvas.create_line(*(self.liste_cases_opposee[case]), fill=color)
        except AssertionError as e:
            self.zoneTexte.config(text=e, background='#9b1441')
        self.update()
        
    def effacer(self,case):
        #vide la case
        self.canvas.create_rectangle(*(self.liste_cases[case]),fill='white',outline='white')
    
    def onClick_souris(self,event):
        x=event.x
        y=event.y
        for case in self.liste_cases:
            if x>case[0] and x<case[2] and y>case[1] and y<case[3]:
                # self.morpion.dessiner_au_piff_c_est_un_test(self.liste_cases.index(case))
                self.morpion.interfaceClick(self.liste_cases.index(case))
    
    def editNombreTour(self):
        """Permet d'afficher le nombre de tour r??alis??"""
        self.zoneCompteur.config(text='Number of turns: ' + str(self.morpion.compteur))

        
    def editGagnant(self):
        """Permet d'afficher qui a gagn??"""
        v=self.morpion.vainqueur
        if not v is None:
            if self.morpion.joueur==v:
                self.zoneTexte.config(text='You won!',background='lightpink')
            elif v in self.morpion.joueurs:
                self.zoneTexte.config(text='You lost...',background='lightpink')
            else:
                self.zoneTexte.config(text="The game is too long, the winner is "+v,background='lightpink')
                    
class Morpion():
    def __init__(self,interface):
        self.interface = interface
        self.winPossibilities = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # Liste de toutes les combinaisons permettant de gagner
        self.joueurs = ['circl','cross']
        self.joueur = '' # 'circl' ou 'cross'
        self.AI = None
        self.is_active = False
        self.profondeur = 6
        self.compteur=0
        
    def reset(self):
        """Permet de r??initialiser les variables avant de d??buter une nouvelle partie"""
        self.Vo = [] # Vecteur des circls
        self.Vx = [] # Vecteur des cross
        self.VV = [i for i in range(9)] # Vecteur des cases vides
        self.case_a_vider = None
        self.repaint()
        self.joueur_start = random.randint(0,1) # 1 si c'est le joueur humain qui doit jouer en premier, 0 sinon
        if self.joueur_start == 1:
            self.tile = self.joueur # self.tile correspond au pion qui doit ??tre jou?? au prochain tour
        else:
            self.tile = 'cross' if self.joueur == 'circl' else 'circl'
        self.compteur = 0
        self.case = None
        self.vainqueur = None
        self.playMode = None # soit AIVSAI, soit HVSAI
        self.historique = [] # historique de placement des pions
        
    def noAI(self):
        """Joue sans IA"""
        self.AI = None
        
    def bestFirst(self):
        """Joue avec l'algorithme bestFirst"""
        self.AI = 'bestFirst'
        
    def minMax(self):
        """Joue avec l'algorithme minMax"""
        self.AI = 'minMax'
        
    def playerTile(self,tile):
        """Permet de choisir si on joue en tant que circl ou cross"""
        if tile in self.joueurs:
            self.joueur = tile
            
    def AIvsAI(self):
        """Mode de jeu IA vs IA"""
        self.playMode = "AIVSAI"
        i = self.joueur_start
        self.tile = self.joueurs[i]
        while self.vainqueur == None and self.playMode=="AIVSAI": # Boucle tant que le jeu n'est pas r??initialis?? (self.reset()) ou s'il n'y a pas de gagnant
            self.place_tile()
            
    def HumanVSAI(self):
        """Mode de jeu Humain vs IA"""
        self.playMode = "HVSAI"
        if self.joueur_start == 0: #La machine commence
            self.place_tile()
            
    def HumanVSHuman(self):
        """Mode de jeu Humain vs Humain"""
        if self.playMode == None:
            self.playMode = "HVSH"
    
            
    def updateHistorique(self):
        """Actualise l'historique"""
        if self.tile == 'circl':
            self.Vo.sort()
            self.historique.append(self.Vo.copy()) # m??morise la liste qui vient d'??tre modifi??e
        else:
            self.Vx.sort()
            self.historique.append(self.Vx.copy()) # m??morise la liste qui vient d'^tre modifi??e
            
    def interfaceClick(self,case):
        """Fonction appel??e ?? chaque clic r??alis?? dans l'interface graphique"""
        if self.vainqueur == None and ((self.playMode =="HVSAI" and self.tile==self.joueur) or self.playMode=="HVSH"): # V??rifie si c'est au tour d'un humain de jouer
            self.case = case
            if self.case_a_vider == None:
                # S'il n'y a pas de case ?? vider, alors on peut directement placer un nouveau pion (au lieu d'en d??placer un)
                self.place_tile()
                if self.case != None:
                    # place_tile() permute la valeur de self.tile
                    # Mais si la case n'a pas ??t?? jou??e (i.e. self.case != None), alors il faut repermuter self.tile
                    self.tile = 'circl' if self.tile == 'cross' else 'cross'
            elif self.case in self.VV:
                # Si self.case_a_vider != None, alors il faut supprimer le pion de cette case pour la replacer dans self.case, en v??rifiant que self.case soit libre
                self.remove_tile() # Supprime le pion dans self.case_a_vider
                self.place_tile() # Rajoute un pion dans self.case, ou s??lectionne une nouvelle valeur pour self.case_a_vider
                if self.case_a_vider != None:
                    # Si une nouvelle case_a_vider a ??t?? s??lectionn??, il faut permuter la valeur de self.tile
                    self.tile = 'circl' if self.tile == 'cross' else 'cross'
            elif self.case == self.case_a_vider: # Permet de d??selectionner la case ?? vider en recliquant dessus
                self.interface.tracer(self.tile, self.case_a_vider, 'black')
                if self.tile == 'circl' and self.case in self.Vo or self.tile == "cross" and self.case in self.Vx:
                    self.case_a_vider = None
                    
            if self.playMode == "HVSAI" and self.case == None and self.vainqueur == None: # La machine joue si le joueur humain a plac??/d??plac?? un pion
                self.place_tile()
                
    def place_tile(self):
        """Place un pion"""
        if self.case != None : # C'est au joueur humain de jouer
            self.human_place_tile()
        else: # Aucune case selectionne par le joueur humain, donc la machine joue
            # Choisit quel algorithme utiliser
            if self.AI == "bestFirst":
                self.use_bestFirst()
            elif self.AI == "minMax":
                self.use_minMax()
            else:
                self.use_idleMachine()
            self.compteur += 1
            self.interface.editNombreTour()
            self.updateHistorique()
                
        # Permute la valeur de self.tile pour que le prochain tour corresponde ?? celui de l'adversaire
        if self.winner():
            self.interface.editGagnant()
        self.tile = 'circl' if self.tile == 'cross' else 'cross' # Change la cross en circl et vice-versa
            
    def remove_tile(self):
        """Supprime le pion pr??sent dans self.case_a_vider"""
        if self.case_a_vider in self.Vo:
            self.Vo.remove(self.case_a_vider)
        else:
            self.Vx.remove(self.case_a_vider)
        self.VV.append(self.case_a_vider)
        self.case_a_vider = None
      
    def human_place_tile(self):
        """Appel?? lorsqu'un humain veut placer un pion"""
        if self.tile == 'circl': # S??lectionne la couleur du pion ?? jouer
            if len(self.Vo)>2:
                # Cas o?? on selectionne un pion ?? d??placer (si on a 3 pions plac??s)
                if self.case in self.Vo:
                    self.case_a_vider = self.case
                    self.interface.tracer(self.tile, self.case_a_vider, 'red')
            elif self.case in self.VV:
                # Cas o?? on n'a pas encore 3 pions sur la table
                self.VV.remove(self.case)
                self.Vo.append(self.case)
                self.case = None # Permet de v??rifier que le pion a ??t?? jou?? (pour d??terminer si on peut passer au prochain tour)
                self.updateHistorique()
                self.compteur += 1
                self.interface.editNombreTour()
                self.repaint()
        else:
            if len(self.Vx)>2:
                if self.case in self.Vx:
                    self.case_a_vider = self.case
                    self.interface.tracer(self.tile, self.case_a_vider, 'red')
            elif self.case in self.VV:
                self.VV.remove(self.case)
                self.Vx.append(self.case)
                self.case = None # Permet de v??rifier que le pion a ??t?? jou?? (pour d??terminer si on peut passer au prochain tour)
                self.updateHistorique()
                self.compteur += 1
                self.interface.editNombreTour()
                self.repaint()
          
    def use_idleMachine(self):
        case = self.VV[random.randint(0,len(self.VV))-1] # On choisit al??atoirement une case libre
        if self.tile == 'cross':
            if len(self.Vx)>2:
                self.case_a_vider = self.Vx[random.randint(0,2)] # On choisit de d??truire al??atoirement une cross parmi les 3 d??j?? plac??s
                self.remove_tile()
            self.VV.remove(case) # On place un pion dans la case qui avait ??t?? choisit au d??but de la fonction (forc??mment diff??rente de self.case_a_vider)
            self.Vx.append(case)
        else:
            if len(self.Vo)>2:
                self.case_a_vider = self.Vo[random.randint(0,2)] # On choisit de d??truire al??atoirement une cross parmi les 3 d??j?? plac??s
                self.remove_tile()
            self.VV.remove(case) # On place un pion dans la case qui avait ??t?? choisit au d??but de la fonction (forc??mment diff??rente de self.case_a_vider)
            self.Vo.append(case)
        self.repaint()
    
    
    def use_bestFirst(self):
        case = self.VV[0] # Case choisit par d??faut
        g = self.calculate_singleG(case)
        
        if self.tile == 'circl' and len(self.Vo)>2 or self.tile == 'cross' and len(self.Vx)>2:
            for i in range(3): # On essaye de voir quel pion parmi les 3 d??j?? pos??s il est judicieux de d??placer
                if self.tile == 'circl':
                    self.Vo.sort() # Ordonne la liste pour ??viter de changer l'indice des elements de la liste
                    self.case_a_vider = self.Vo[i]
                    self.Vo.remove(self.case_a_vider) # Simule la suppression d'un des pions d??j?? plac??s
                else:
                    self.Vx.sort() # Ordonne la liste pour ??viter de changer l'indice des elements de la liste
                    self.case_a_vider = self.Vx[i]
                    self.Vx.remove(self.case_a_vider) # Simule la suppression d'un des pions d??j?? plac??s
                
                g,case = self.bestFirst_calculateG(g,case) # Calcule la meilleur case ?? jouer
                
                if self.tile == 'circl':
                    self.Vo.append(self.case_a_vider) # Remet en place le pion dont ??a suppression avait ??t?? simul??e (sera r??ellement supprim??e une fois qu'on est s??r de sa suppression)
                else:
                    self.Vx.append(self.case_a_vider) # Remet en place le pion dont ??a suppression avait ??t?? simul??e (sera r??ellement supprim??e une fois qu'on est s??r de sa suppression)
                    
            self.remove_tile() # On a trouv?? le meilleur pion a supprimer, donc on le supprime d??finitivement
        
        else:
            g,case = self.bestFirst_calculateG(g,case) # On a pas de pion a supprimer car il y a moins de 3 pions dans le plateau
            
        self.VV.remove(case) # Rend la case choisie occup??e
        if self.tile == 'circl':
            self.Vo.append(case)
        else:
            self.Vx.append(case)
        self.repaint()
        
    def calculate_singleG(self,caseLibre):
        """Calcule la valeur de g correspondant ?? la case libre"""
        if self.tile == 'circl':
            self.Vo.append(caseLibre)
        else:
            self.Vx.append(caseLibre)

        NL1,NL2,NC1,NC2,ND11,ND12,ND21,ND22 = 0,0,0,0,0,0,0,0
        case_x,case_y = caseLibre//3, caseLibre%3 # Num??ro de la ligne et de la colonne de la case libre
        # On part du principe que self.tile == 'circl'. Si ce n'est pas le cas, on intervertit NL1 et NL2, NC1 et NC2, ND1 et ND2
        for i in self.Vo:
            i_x,i_y = i//3, i%3 # Num??ro de la ligne et de la colonne du pion
            if i_x == case_x:
                NL1 += 1 # la case libre poss??de un pion alli?? dans sa ligne
            if i_y == case_y:
                NC1 += 1 # La case libre poss??de un pion alli?? dans sa colonne
            if i in [0,4,8] and caseLibre in [0,4,8]:
                ND11 += 1 # La case libre poss??de un pion alli?? dans sa diagonale
            if i in [2,4,6] and caseLibre in [2,4,6]:
                ND21 += 1 # LA case libre poss??de un pion alli?? dans sa deuxi??me diagonale
        for j in self.Vx:
            j_x,j_y = j//3, j%3 # Num??ro de la ligne et de la colonne du pion
            if j_x == case_x:
                NL2 += 1 # la case libre poss??de un pion ennemi dans sa ligne
            if j_y == case_y:
                NC2 += 1 # La case libre poss??de un pion ennemi dans sa colonne
            if j in [0,4,8] and caseLibre in [0,4,8]:
                ND12 += 1 # La case libre poss??de un pion ennemi dans sa diagonale
            if j in [2,4,6] and caseLibre in [2,4,6]:
                ND22 += 1 # La case libre poss??de un pion ennemi dans sa deuxi??me diagonale
        
        if self.tile == 'circl':
            self.Vo.remove(caseLibre)
        else:
            self.Vx.remove(caseLibre)
            
        if not self.tile == 'circl':
            # On intervertit les indices, parce qu'on ??tait partit du principe que les pions alli??s ??taient les circls       
            NL1,NL2 = NL2,NL1
            NC1,NC2 = NC2,NC1
            ND11,ND12 = ND12,ND11
            ND21,ND22 = ND22,ND21

        ### FONCTION G ###
        # g = (NL1-NL2)**3 + (NC1-NC2)**3 + (ND11-ND12)**3 + (ND21-ND22)**3

        ### VERSION QUADRATIQUE ###            
        facteur_NL = -1 if NL2>NL1 else 1
        facteur_NC = -1 if NC2>NC1 else 1
        facteur_ND1 = -1 if ND12>ND11 else 1
        facteur_ND2 = -1 if ND22>ND21 else 1
        g = facteur_NL*(NL1-NL2)**2 + facteur_NC*(NC1-NC2)**2 + facteur_ND1*(ND11-ND12)**2 + facteur_ND2*(ND21-ND22)**2
            
        facteur_NL = 2 if NL2>1 else 1
        facteur_NC = 2 if NC2>1 else 1
        facteur_ND = 2 if ND22+ND12>1 else 1
        g *= facteur_NL * facteur_NC * facteur_ND
        
        return g    
        
        
    def bestFirst_calculateG(self,g,case):
        """ Renvoie la meilleure case libre ?? choisir ainsi que la valeur de la fonction g associ??e"""
        for case_candidat in self.VV:
                
            g_candidat = self.calculate_singleG(case_candidat)
            
            if case_candidat == 4: # Priorise syst??matiquement le d??placement du pion vers le centre
                if g_candidat > g or g_candidat == g and (case != 4 or random.randint(0,1)==1):
                    g = g_candidat
                    case = case_candidat
                else:
                    continue # la case est d??j?? au centre, et son g est optimal, donc on sort de la boucle
                
            elif g_candidat > g or g_candidat == g and case_candidat%2==0 and (case%2!=0 or random.randint(0,1)==1 and case!=4):
                # si g_candidat > g, on prend la nouvelle case
                # si les deux g sont ??gaux mais que case_candidat est dans un diagonale (c-??-d case_candidat%2==0), alors on prend la nouvelle case
                # si les deux g sont ??gaux et case_candidat et case sont toutes deux sur une diagonale, on choisit al??atoirement l'une des deux cases (random.randint(0,1)==1)
                g = g_candidat
                case = case_candidat
                
        return (g,case)
    
    def use_minMax(self):
        if self.profondeur == 0 or self.profondeur > 6: # Probl??me de profondeur, on arr??te donc l'utilisation de minMax
            print("Probl??me de profondeur lors du choix de l'utilisation de l'algorithme minMax")
            return
        plateau = {"cross":self.Vx,"circl":self.Vo,"vide":self.VV} # Regrouppement des 3 listes en un dictionnaire
        plateauAJouer, valeur = self.executeMinMax(plateau, self.profondeur, "max", self.tile) # Appel r??cursif pour ??tudier la meilleur case ?? jouer en profondeur
        
        # Remplace les anciennes listes Vx,Vo,VV par celles renvoy??es par l'algotithme minMax
        self.Vx = plateauAJouer['cross']
        self.Vo = plateauAJouer['circl']
        self.VV = plateauAJouer['vide']
        self.repaint()
        
    def executeMinMax(self, plateau, profondeur, mode, color):
        """Partie r??cursive de l'algorithme minMax"""
        inverseColor = 'circl' if color == 'cross' else 'cross'        
        inverseMode = 'max' if mode == 'min' else 'min'
        if len(plateau["vide"]) < 8: #Si le plateau n'est pas vierge:
            if profondeur == 0 or self.gagne(inverseColor, plateau):
                # Condition d'arr??t de la r??cursion
                valeur = self.score_plateau(plateau, self.tile) # Calcule le score du dernier plateau visit??
                return (plateau,valeur)
        maxScore = -1*math.inf # Valeur minimale par d??faut
        minScore = math.inf # Valeur maximale par d??faut
        listePlateauxSuccesseurs = [] # Liste des plateaux ?? visiter
        if len(plateau[color])<3: # Si la couleur ?? jouer poss??de moins de 3 pions dans le tableau
            listePlateauxSuccesseurs = self.succ_plateau_moins_de_3_pions(plateau, color)
        else:
            listePlateauxSuccesseurs = self.succ_plateau_deja_3_pions(plateau, color)
            
        bestScore = None # Pas de meilleur choix par d??faut
        
        for plateauBis in listePlateauxSuccesseurs:
            plateau1, score = self.executeMinMax(plateauBis, profondeur-1, inverseMode, inverseColor) # Appel r??cursif
            if mode == 'max':
                if score >= maxScore or (score==maxScore and random.randint(0,1)==1): # Actualise le meilleur score. S'il existe deux plateaux avec le m??me score, l'un des deux sera choisit al??atoirement.
                    bestScore = score
                    bestPlateau = plateau1
                    maxScore = bestScore
                    if bestScore == math.inf: # Pas la peine de faire d'avantage d'appel r??cursif, car on ne peut pas faire de meilleur score
                        break
            else:
                if score <= minScore or (score==maxScore and random.randint(0,1)==1): # Actualise le meilleur score. S'il existe deux plateaux avec le m??me score, l'un des deux sera choisit al??atoirement.
                    bestScore = score # Actualise le meilleu score
                    bestPlateau = plateau1
                    minScore = bestScore
                    if bestScore == -1*math.inf: # Pas la peine de faire d'avantage d'appel r??cursif, car on ne peut pas faire de pire score
                        break
                    
        if bestScore == None: # Ce cas arrive lorsque tous les scores sont ??gaux ?? plus ou moins l'infini
            plateauBis = listePlateauxSuccesseurs[0]
            bestPlateau, score = self.executeMinMax(plateauBis, profondeur-1, inverseMode, inverseColor)
            bestScore = score

        if profondeur == self.profondeur: # Si on est au premier appel, on renvoie le meilleur plateau qui succ??de au plateau original
            return (bestPlateau,bestScore)
        else:
            return (plateau,bestScore) # Sinon, on renvoie simplement le plateau actuel avec le meilleur score qui peut ??tre obtenu
                    
    def gagne(self, color, plateau):
        plateau[color].sort()
        return (plateau[color] in self.winPossibilities)
        
    def score_plateau(self, plateau,color):
        """Calcule le score d'un plateau dont la couleur qui vient d'??tre jou??e correspond ?? color"""
        inverseColor = 'circl' if color == 'cross' else 'cross'
        if self.gagne(color, plateau):
            return math.inf
        elif self.gagne(inverseColor, plateau):
            return -1*math.inf
        else:
            return self.gagnantsPossibles(plateau,color) - self.gagnantsPossibles(plateau,inverseColor)
        
    def gagnantsPossibles(self, plateau, color):
        """Indique le nombre de lignes/colonnes/diagonales que color bloque pour son adversaire"""
        valeur = 0
        for i in [0,1,2]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [3,4,5]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [6,7,8]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [0,3,6]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [1,4,7]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [2,5,8]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [0,4,8]:
            if i in plateau[color]:
                valeur+=1
                break
        for i in [2,4,6]:
            if i in plateau[color]:
                valeur+=1
                break
        return valeur
        
    def succ_plateau_moins_de_3_pions(self,plateau, color):
        """Renvoie la liste des plateaux possibles d'obtenir apr??s avoir plac?? un pion de la couleur 'color' """
        liste = []
        Vx,Vo,VV = plateau.values()
        for caseVide in plateau["vide"]:
            newPlateau = {"cross":Vx.copy(),"circl":Vo.copy(),"vide":VV.copy()}
            newPlateau[color].append(caseVide)
            newPlateau["vide"].remove(caseVide)
            liste.append(newPlateau)
        return liste
    
    def succ_plateau_deja_3_pions(self, plateau, color):
        """Renvoie la liste des plateaux possibles d'obtenir apr??s avoir d??plac?? un pion de la couleur 'color' """
        liste = []
        Vx,Vo,VV = plateau.values()
        for caseOccup_indice in range(3): # Essaie de d??placer tous pions
            plateau[color].sort() # Ordonne la liste pour ne pas modifier l'indice des ??l??ments
            caseOccup = plateau[color][caseOccup_indice]
            if color == 'circl':
                Vo.remove(caseOccup)
            else:
                Vx.remove(caseOccup)
            VV.append(caseOccup)
            for caseVide in plateau["vide"]:
                if caseVide != caseOccup: # V??rifie qu'on ne cr??e pas le m??me plateau que celui de base
                    newPlateau = {"cross":Vx.copy(),"circl":Vo.copy(),"vide":VV.copy()}
                    newPlateau[color].append(caseVide)
                    newPlateau["vide"].remove(caseVide)
                    liste.append(newPlateau)
            VV.remove(caseOccup)
            if color == 'circl':
                Vo.append(caseOccup)
            else:
                Vx.append(caseOccup)
        return liste
    
    def repaint(self):
        # Actualise l'interface graphique
        for case in range(9):
            self.interface.effacer(case)
            if case in self.Vx:
                self.interface.tracer('cross', case, 'black')
            elif case in self.Vo:
                self.interface.tracer('circl', case, 'black')
            
    def winner(self):
        """V??rifie s'il y a un gagnant dans la configuration actuelle des listes"""
        self.Vo.sort() # Ordonne la liste pour la comparer avec les listes contenues dans self.winPossibilities
        if self.Vo in self.winPossibilities:
            self.vainqueur = "circl"
            return True
        self.Vx.sort()
        if self.Vx in self.winPossibilities: # Ordonne la liste pour la comparer avec les listes contenues dans self.winPossibilities
            self.vainqueur = "cross"
            return True
        if self.etatRedondant(): # Cas o?? il y a ??galit?? (on retombe toujours dans la m??me configuration)
                self.endGame()
                return True
        return False
        
    def etatRedondant(self):
        if self.compteur > 20:
            n = len(self.historique)
            d,ad,aad,aaad = self.historique[n-1],self.historique[n-2],self.historique[n-3],self.historique[n-4] # dernier,avant-dernier,avant-avant-dernier et avant-avant-avant-dernier jeu
            for i in range(n-4):
                if aaad == self.historique[i] and aad == self.historique[i+1] and ad == self.historique[i+2] and d == self.historique[i+3]:
                    return True
        return False
    
    def endGame(self):
        plateau = {"cross":self.Vx,"circl":self.Vo,"vide":self.VV} # Regrouppement des 3 listes en un dictionnaire
        pointscross = 8-self.gagnantsPossibles(plateau,"cross") # Il y a 8 fa??ons de gagner moins les lignes/colonnes/diagonales bloqu??es par l'ennemi
        pointscircl = 8-self.gagnantsPossibles(plateau,"circl")
        if pointscross > pointscircl:
            self.vainqueur = "circl ("+str(pointscross)+" points vs "+str(pointscircl)+" points)."
        else:
            self.vainqueur = "cross ("+str(pointscircl)+" points vs "+str(pointscross)+" points)."
        
if __name__ == "__main__" :
    jeu = Interface()
    jeu.mainloop()
