import random as rand
from tkinter import *
from tkinter import messagebox
def mozliwosciUlozeniaBota(grid):                               #grid2 zlicza liczbe zwycieskich linii bota z danym polem np:
    grid2=[0,0,0,0,0,0,0,0,0]                                   #    123      123
    for i in range(3):                                          #  1  O     1 100
        fits=0                                                  #  2  X     2 201
        for j in range(3):                                      #  3   O    3 200
            if grid[3*i+j]==' ' or grid[3*i+j]=='X':            #
                fits+=1
        if fits==3:
            for j in range(3):
                grid2[3*i+j]+=1
    for i in range(3):
        fits=0
        for j in range(3):
            if grid[3*j+i]==' ' or grid[3*j+i]=='X':
                fits+=1
        if fits==3:
            for j in range(3):
                grid2[3*j+i]+=1
    fits=0
    for i in range(3):
        if grid[4*i]==' ' or grid[4*i]=='X':
            fits+=1
    if fits==3:
        for i in range(3):
            grid2[4*i]+=1
    fits=0
    for i in range(3):
        if grid[2*i+2]==' ' or grid[2*i+2]=='X':
            fits+=1
    if fits==3:
        for i in range(3):
            grid2[2*i+2]+=1
    for i in range(9):
        if grid[i]=='X':
            grid2[i]=0
    return grid2





def zmniejszeniaRuchowGracza(grid):                              #ile mniej wygrywajacych ulozen bedzie dla gracza
    grid4=[0,0,0,0,0,0,0,0,0]                                    #w zalezności od położenia X np:
    for i in range(3):                                           #    123      1  2  3
        fits=0                                                   #  1  O    1 -2  0 -2
        for j in range(3):                                       #  2  X    2 -1  0 -1
            if grid[3*i+j]==' ' or grid[3*i+j]=='O':             #  3   O   3 -2 -1  0
                fits+=1
        if fits==3:
            for j in range(3):
                if grid[3*i+j]==' ':
                    grid4[3*i+j]-=1
    for i in range(3):
        fits=0
        for j in range(3):
            if grid[3*j+i]==' ' or grid[3*j+i]=='O':
                fits+=1
        if fits==3:
            for j in range(3):
                if grid[3*j+i]==' ':
                    grid4[3*j+i]-=1
    fits=0
    for i in range(3):
        if grid[4*i]=='O' or grid[4*i]==' ':
            fits+=1
    if fits==3:
        for i in range(3):
            if grid[4*i]==' ':
                grid4[4*i]-=1
    fits=0
    for i in range(3):
        if grid[2*i+2]=='O' or grid[2*i+2]==' ':
            fits+=1
    if fits==3:
        for i in range(3):
            if grid[2*i+2]==' ':
                grid4[2*i+2]-=1
    return grid4


def najszybszeUlozenie(grid):                                       #liczba ruchów potrzebnych do wykonania by dane pole było w linii wygrywającej np dla:
    grid5=[4,4,4,4,4,4,4,4,4]                                       #    123      123
    for i in range(3):                                              #  1  O     1 342
        ilePustych=0                                                #  2  X     2 242
        fits=0                                                      #  3   O    3 244
        for j in range(3):                                          
            if grid[i*3+j]=='X' or grid[3*i+j]==' ':
                fits+=1
        if fits==3:
            for j in range(3):
                if grid[i*3+j]==' ':
                    ilePustych+=1
            for j in range(3):
                if grid[i*3+j]==' ':
                    if grid5[i*3+j]>ilePustych:
                        grid5[i*3+j]=ilePustych
    for i in range(3):
        ilePustych=0
        fits=0
        for j in range(3):
            if grid[j*3+i]=='X' or grid[3*j+i]==' ':
                fits+=1
        if fits==3:
            for j in range(3):
                if grid[j*3+i]==' ':
                    ilePustych+=1
            for j in range(3):
                if grid[j*3+i]==' ':
                    if grid5[j*3+i]>ilePustych:
                        grid5[j*3+i]=ilePustych
    ilePustych=0
    fits=0
    for i in range(3):
        if grid[4*i]=='X' or grid[4*i]==' ':
            fits+=1
    if fits==3:
        for i in range(3):
            if grid[4*i]==' ':
                ilePustych+=1
        for i in range(3):
            if grid[4*i]==' ':
                if grid5[4*i]>ilePustych:
                    grid5[4*i]=ilePustych
    ilePustych=0
    fits=0
    for i in range(3):
        if grid[2*i+2]=='X' or grid[2*i+2]==' ':
            fits+=1
    if fits==3:
        for i in range(3):
            if grid[2*i+2]==' ':
                ilePustych+=1
        for i in range(3):
            if grid[2*i+2]==' ':
                if grid5[2*i+2]>ilePustych:
                    grid5[2*i+2]=ilePustych
    return grid5


def dobreRuchy(grid2,grid4,grid5,grid7):
    gridRuch=[0,0,0,0,0,0,0,0,0]
   
    checkI=0
    for i in range(9):
        if grid7[i]==1:
            checkI+=1
    if checkI>=2:
        for i in range(9):
            if grid2[i]==max(grid2)  and grid5[i]==min(grid5) and grid7[i]==1:              #najlepszy ruch z pułapką
                gridRuch[i]=1
    else:
        for i in range(9):
            if grid2[i]==max(grid2) and grid4[i]==min(grid4) and grid5[i]==min(grid5):      #najlepszy ruch jeśli nie ma pułapki
                gridRuch[i]=1
    return gridRuch

def ruchPulapkaGracza(grid):                                        #tu jest obliczany grid6 który szuka pułapek, np dla ustawienia:
    for i in range(9):                                              #    123                    123                         123
        grid6=[0,0,0,0,0,0,0,0,0]                                   #  1  O          znajduje 1 1O   bo istnieje pułapka  1  OO
        if grid[i]==' ':                                            #  2  X                   2  X1                       2  X
            tempgrid=[]                                             #  3   O                  3   O                       3   O
            for j in range(9):                                      #jedynki to pola poza polem pułapką, i jak się je uzupełni lub zmusi przeciwnika do ruchu w tamtych miejscach
                tempgrid.append(grid[j])                            #to pułapka przestaje działać
            tempgrid[i]='O'
            for j in range(3):
                IsO=0
                fitsAny=0
                for k in range(3):
                    if tempgrid[3*j+k]=='O':
                        IsO+=1
                    if tempgrid[3*j+k]==' ':
                        fitsAny+=1
                if IsO==2 and fitsAny==1:
                    for k in range(3):
                        if tempgrid[3*j+k]==' ':
                            grid6[3*j+k]=1
            for j in range(3):
                IsO=0
                fitsAny=0
                for k in range(3):
                    if tempgrid[3*k+j]=='O':
                        IsO+=1
                    if tempgrid[3*k+j]==' ':
                        fitsAny+=1
                if IsO==2 and fitsAny==1:
                    for k in range(3):
                        if tempgrid[3*k+j]==' ':
                            grid6[3*k+j]=1
            IsO=0
            fitsAny=0
            for k in range(3):
                if tempgrid[4*k]=='O':
                    IsO+=1
                if tempgrid[4*k]==' ':
                    fitsAny+=1
            if IsO==2 and fitsAny==1:
                for k in range(3):
                    if tempgrid[4*k]==' ':
                        grid6[4*k]=1
            IsO=0
            fitsAny=0
            for k in range(3):
                if tempgrid[2*k+2]=='O':
                    IsO+=1
                if tempgrid[2*k+2]==' ':
                    fitsAny+=1
            if IsO==2 and fitsAny==1:
                for k in range(3):
                    if tempgrid[2*k+2]==' ':
                        grid6[2*k+2]=1
            thereIs1=0
            for k in range(9):
                if grid6[k]==1:
                    thereIs1+=1
            if thereIs1==2:
                return grid6
    return grid6

def kontratak(grid,grid6):                                                      #jeżeli linia grid6 i grid ma w sobie ' ','X',1 to wstawia X w puste pole
    grid7=[0,0,0,0,0,0,0,0,0]                                                   #1 pochodzi z grid 6, które szukało pułapek
    for i in range(3):                                                          #grid 7 ich nie uzupełnia, a wskazuje na pole, które zmusza gracza do ruchu w niewygodne miejsce
        isX=0
        for j in range(3):
            if grid[3*i+j]=='X':
                isX+=1
        fits=0
        for j in range(3):
            if grid[3*i+j]=='X' or grid[3*i+j]==' ':
                fits+=1
        possibleTrap=0
        for j in range(3):
            if grid6[3*i+j]==1:
                possibleTrap=1
        for j in range(3):
            if grid[3*i+j]==' ' and possibleTrap==1 and fits==3 and isX==1:
                grid7[3*i+j]=1
    for i in range(3):
        isX=0
        for j in range(3):
            if grid[3*j+i]=='X':
                isX+=1
        fits=0
        for j in range(3):
            if grid[3*j+i]=='X' or grid[3*j+i]==' ':
                fits+=1
        possibleTrap=0
        for j in range(3):
            if grid6[3*j+i]==1:
                possibleTrap=1
        for j in range(3):
            if grid[3*j+i]==' ' and possibleTrap==1 and fits==3 and isX==1:
                grid7[3*j+i]=1
   
    isX=0
    for j in range(3):
        if grid[4*j]=='X':
            isX+=1
    fits=0
    for j in range(3):
        if grid[4*j]=='X' or grid[4*j]==' ':
            fits+=1
    possibleTrap=0
    for j in range(3):
        if grid6[4*j]==1:
            possibleTrap=1
    for j in range(3):
        if grid[4*j]==' ' and possibleTrap==1 and fits==3 and isX==1:
            grid7[4*j]=1
   
    isX=0
    for j in range(3):
        if grid[2*j+2]=='X':
            isX+=1
    fits=0
    for j in range(3):
        if grid[2*j+2]=='X' or grid[2*j+2]==' ':
            fits+=1
    possibleTrap=0
    for j in range(3):
        if grid6[2*j+2]==1:
            possibleTrap=1
    for j in range(3):
        if grid[2*j+2]==' ' and possibleTrap==1 and fits==3 and isX==1:
            grid7[2*j+2]=1
    return grid7

def obronaLubWygrana(grid,poziomTrudnosci):                 #Bot szuka dwóch X lub O w jednej linii i wstawia X do pola pustego
    for i in range(3):                                      #jest 8 pętli 4 na X (pionowo, poziomo, przekątna1 i przekątna2) i 4 na O
        fits=0
        pkt=0
        for j in range(3):
            if grid[3*i+j]=='X' or grid[3*i+j]==' ':
                fits+=1
            if grid[3*i+j]=='X':
                pkt+=1
        if fits==3 and pkt==2:
            for j in range(3):
                if grid[3*i+j]==' ':
                    grid[3*i+j]='X'
                    print("ruch2")
                    return grid
    for i in range(3):
        fits=0
        pkt=0
        for j in range(3):
            if grid[3*i+j]=='O' or grid[3*i+j]==' ':
                fits+=1
            if grid[3*i+j]=='O':
                pkt+=1
        if fits==3 and pkt==2:
            for j in range(3):
                if grid[3*i+j]==' ':
                    grid[3*i+j]='X'
                    return grid
    for i in range(3):
        fits=0
        pkt=0
        for j in range(3):
            if grid[3*j+i]=='X' or grid[3*j+i]==' ':
                fits+=1
            if grid[3*j+i]=='X':
                pkt+=1
        if fits==3 and pkt==2:
            for j in range(3):
                if grid[3*j+i]==' ':
                    grid[3*j+i]='X'
                    return grid
    for i in range(3):
        fits=0
        pkt=0
        for j in range(3):
            if grid[3*j+i]=='O' or grid[3*j+i]==' ':
                fits+=1
            if grid[3*j+i]=='O':
                pkt+=1
        if fits==3 and pkt==2:
            for j in range(3):
                if grid[3*j+i]==' ':
                    grid[3*j+i]='X'
                    return grid
    fits=0
    pkt=0
    for j in range(3):
        if grid[4*j]=='X' or grid[4*j]==' ':
            fits+=1
        if grid[4*j]=='X':
            pkt+=1
    if fits==3 and pkt==2:
        for j in range(3):
            if grid[4*j]==' ':
                grid[4*j]='X'
                return grid
    fits=0
    pkt=0
    for j in range(3):
        if grid[4*j]=='O' or grid[4*j]==' ':
            fits+=1
        if grid[4*j]=='O':
            pkt+=1
    if fits==3 and pkt==2:
        for j in range(3):
            if grid[4*j]==' ':
                grid[4*j]='X'
                return grid
    fits=0
    pkt=0
    for j in range(3):
        if grid[2*j+2]=='X' or grid[2*j+2]==' ':
            fits+=1
        if grid[2*j+2]=='X':
            pkt+=1
    if fits==3 and pkt==2:
        for j in range(3):
            if grid[2*j+2]==' ':
                grid[2*j+2]='X'
                return grid
    fits=0
    pkt=0
    for j in range(3):
        if grid[2*j+2]=='O' or grid[2*j+2]==' ':
            fits+=1
        if grid[2*j+2]=='O':
            pkt+=1
    if fits==3 and pkt==2:
        for j in range(3):
            if grid[2*j+2]==' ':
                grid[2*j+2]='X'
                return grid
    if poziomTrudnosci==2:
        while True:                                    
            a=rand.randint(0,8)                            
            if grid[a]==' ':
                grid[a]='X'
                return grid
    return "Skomplikowany ruch"                     #zwraca informację że nie ma takiego ruchu który albo zwycięży albo zablokuje
                                                    #zwraca do linii 432

#===========================================================================================================================================#
#KONIEC FUNKCJI POMOCNICZYCH
#===========================================================================================================================================#

def ruchBota(grid,poziomTrudnosci):
    if poziomTrudnosci==1:                              
        while True:
            a=rand.randint(0,8)
            if grid[a]==' ':
                grid[a]='X'
                return grid
    elif poziomTrudnosci==2:
        return obronaLubWygrana(grid,poziomTrudnosci)  
    elif poziomTrudnosci==3:
        if grid==['X',' ',' ',' ','O',' ',' ',' ','O']:
            grid[2]='X'
            return grid
        checkIfOK=obronaLubWygrana(grid,poziomTrudnosci)
        if checkIfOK=="Skomplikowany ruch":
            grid6=ruchPulapkaGracza(grid)                           #grid 6 sprawdza czy jest ruch wprowadzajacy bota w pulapke, potem zwraca liste, na ktorej zaznaczone sa ruchy gracza psujace pulapke i jednoczesnie sa czescia dobrych ruchow bota
            grid7=kontratak(grid,grid6)                             #grid 7 wykorzystuje grid 6 zeby wyznaczyc odpowiednie ruchy bota
            grid2=mozliwosciUlozeniaBota(grid)                      #grid 2 liczy ile mozliwych wygranych daje ruch na kazdym z wolnych pol
            grid4=zmniejszeniaRuchowGracza(grid)                    #grid 4 liczy o ile zmniejszy wygrywajace ulozenia gracza dla kazdego pola
            grid5=najszybszeUlozenie(grid)                          #grid 5 wyznacza najmniejsza liczbe potrzebnych ruchow bota, zeby wygral z kazdego z pol
            gridDobrychRuchow=dobreRuchy(grid2,grid4,grid5,grid7)
            checkIfExists=0
            for i in range(9):
                if gridDobrychRuchow[i]==1:
                    grid[i]='X'
                    checkIfExists=1
                    return grid
            if checkIfExists==0:
                for i in range(9):
                    if grid7[i]==1:
                        grid[i]='X'
                        return grid
        else:
            return checkIfOK


def GraczWinCheck(grid):                                            #sprawdza czy gracz wygrał i jeśli tak, to koloruje zwycięskie pola na zielono
    global buttonList
    if ((grid[0]=='O' and grid[1]=='O' and grid[2]=='O') or 
          (grid[3]=='O' and grid[4]=='O' and grid[5]=='O') or 
          (grid[6]=='O' and grid[7]=='O' and grid[8]=='O') or 
          (grid[0]=='O' and grid[3]=='O' and grid[6]=='O') or 
          (grid[1]=='O' and grid[4]=='O' and grid[7]=='O') or 
          (grid[2]=='O' and grid[5]=='O' and grid[8]=='O') or 
          (grid[0]=='O' and grid[4]=='O' and grid[8]=='O') or 
          (grid[2]=='O' and grid[4]=='O' and grid[6]=='O')):
        #KOLOROWANIE NA ZIELONO #jesli znajdzie 3 w linii (fits==3) to koloruje wszystkie w linii
        for i in range(3):
            fits=0
            for j in range(3):
                if grid[3*i+j]=='O':
                    fits+=1
            if fits==3:
                for j in range(3):
                    buttonList[3*i+j].config(bg='#abffaf')
                return 1
        for i in range(3):
            fits=0
            for j in range(3):
                if grid[3*j+i]=='O':
                    fits+=1
            if fits==3:
                for j in range(3):
                    buttonList[3*j+i].config(bg='#abffaf')
                return 1
        fits=0
        for j in range(3):
            if grid[4*j]=='O':
                fits+=1
        if fits==3:
            for j in range(3):
                buttonList[4*j].config(bg='#abffaf')
            return 1
        fits=0
        for j in range(3):
            if grid[2*j+2]=='O':
                fits+=1
        if fits==3:
            for j in range(3):
                buttonList[2*j+2].config(bg='#abffaf')
            return 1
    else:
        return 0
def BotWinCheck(grid):                                                       #sprawdza czy bot wygrał i jeśli tak, to koloruje zwycięskie pola na czerwono
    global buttonList
    if ((grid[0]=='X' and grid[1]=='X' and grid[2]=='X') or 
          (grid[3]=='X' and grid[4]=='X' and grid[5]=='X') or 
          (grid[6]=='X' and grid[7]=='X' and grid[8]=='X') or 
          (grid[0]=='X' and grid[3]=='X' and grid[6]=='X') or 
          (grid[1]=='X' and grid[4]=='X' and grid[7]=='X') or 
          (grid[2]=='X' and grid[5]=='X' and grid[8]=='X') or 
          (grid[0]=='X' and grid[4]=='X' and grid[8]=='X') or 
          (grid[2]=='X' and grid[4]=='X' and grid[6]=='X')):
        #KOLOROWANIE NA CZERWONO #jesli znajdzie 3 w linii (fits==3) to koloruje wszystkie w linii
        for i in range(3):
            fits=0
            for j in range(3):
                if grid[3*i+j]=='X':
                    fits+=1
            if fits==3:
                for j in range(3):
                    buttonList[3*i+j].config(bg='#ff6363')
        for i in range(3):
            fits=0
            for j in range(3):
                if grid[3*j+i]=='X':
                    fits+=1
            if fits==3:
                for j in range(3):
                    buttonList[3*j+i].config(bg='#ff6363')
        fits=0
        for j in range(3):
            if grid[4*j]=='X':
                fits+=1
        if fits==3:
            for j in range(3):
                buttonList[4*j].config(bg='#ff6363')
        fits=0
        for j in range(3):
            if grid[2*j+2]=='X':
                fits+=1
        if fits==3:
            for j in range(3):
                buttonList[2*j+2].config(bg='#ff6363')
        return 1
    else:
        return 0

#################################################################################################################
#-----START-----#
#################################################################################################################

def main():
    #definiuje okno i zmienne fundamentalne
    grid=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    root=Tk()
    root.config(bg="#9ef0ff")
    root.geometry("342x490")
    root.resizable(width=0,height=0)
    root.title("Kółko i Krzyżyk")
    #by zacząć trzeba wybrać poziom trudności
    global checkToStart
    checkToStart=False
    #jeśli się zacznie, to nie można zmienić poziomu trudności
    global checkIfStart
    checkIfStart=False
    #kolor pól
    baseColour='#d1f8ff'
    #kolor pól po najechaniu
    baseColourActive='#e4f8ff'
   
    #pokazuje wybrany poziom trudności
    StatusTrudnosci=Label(root,text="Wybierz poziom\ntrudnosci",height=2,width=16,bg="#9ef0ff")
   
    def poziomTrudnosciFunction(i):
        global checkToStart
        global checkIfStart
        if checkIfStart==False:
            global poziomTrudnosci
            poziomTrudnosci=i
            checkToStart=True
            #tylko kolor jednego poziomu trudnosci sie wyróżnia
            if poziomTrudnosci==1:
                bImpossible.config(bg='#c7f7ff',fg='black',activebackground='#d4f8ff',activeforeground='black')
                bMedium.config(bg='#c7f7ff',fg='black',activebackground='#d4f8ff',activeforeground='black')
                bEasy.config(bg='#45a9ba',fg='#2eff66',activebackground='#4eb9cc',activeforeground='#2eff66')
                StatusTrudnosci["text"]="Poziom trudności:\nŁatwy"
            elif poziomTrudnosci==2:
                bImpossible.config(bg='#c7f7ff',fg='black',activebackground='#d4f8ff',activeforeground='black')
                bMedium.config(bg='#45a9ba',fg='#fdff80',activebackground='#4eb9cc',activeforeground='#fdff80')
                bEasy.config(bg='#c7f7ff',fg='black',activebackground='#d4f8ff',activeforeground='black')
                StatusTrudnosci["text"]="Poziom trudności:\nŚredni"
            elif poziomTrudnosci==3:
                bImpossible.config(bg='#45a9ba',fg='#ff3838',activebackground='#4eb9cc',activeforeground='#ff3838')
                bMedium.config(bg='#c7f7ff',fg='black',activebackground='#d4f8ff',activeforeground='black')
                bEasy.config(bg='#c7f7ff',fg='black',activebackground='#d4f8ff',activeforeground='black')
                StatusTrudnosci["text"]="Poziom trudności:\nNiemożliwy"

   
    def b_click(i,grid):
        if checkToStart==True:
            global checkIfStart
            checkIfStart=True
            #jeśli gracz kliknie na puste pole, w przeciwnym przypadku nic sie nie dzieje
            if grid[i]==' ':
                grid[i]='O'
                #update tekstu na polach
                for j in range(9):
                    buttonList[j]["text"]=grid[j]
                #test czy gracz wygrał
                if GraczWinCheck(grid)==1:
                    #kiedy gracz wygrywał to kursor dalej byl na polu, przez co kolor zwycieskiego pola nie byl zielony. Petla ponizej zmienia kolor na zielony
                    for button in buttonList:
                        interakcjaZKursorem(button,'#abffaf','#abffaf')
                    messagebox.showerror("Wynik", "Wygrał Gracz")
                    root.destroy()
                    return 0
                #jeśli jest remis. Remis występuje tylko po ruchu gracza
                if ' ' not in grid:
                    messagebox.showerror("Wynik", "Remis")
                    root.destroy()
                    return 0
                grid=ruchBota(grid,poziomTrudnosci)
                #update tekstu na polach
                for j in range(9):
                    buttonList[j]["text"]=grid[j]
                if BotWinCheck(grid)==1:
                    messagebox.showerror("Wynik", "Wygrał Bot")
                    root.destroy()
                    return 0
    #funkcja zmieniajaca kolor pól po najezdzeniu
    def interakcjaZKursorem(button, kolorNa, kolorPoza):
        button.bind("<Enter>", func=lambda e: button.config(background=kolorNa))
        button.bind("<Leave>", func=lambda e: button.config(background=kolorPoza))
           
    #przyciski poziomu trudnosci
    bEasy=Button(root,borderwidth=0, text='Łatwy', font=('Helvetica',10),height=2,width=8,bg='#c7f7ff',activebackground='#d4f8ff',command=lambda:poziomTrudnosciFunction(1))
    bMedium=Button(root,borderwidth=0, text='Średni', font=('Helvetica',10),height=2,width=8,bg='#c7f7ff',activebackground='#d4f8ff',command=lambda:poziomTrudnosciFunction(2))  
    bImpossible=Button(root,borderwidth=0, text='Niemożliwy', font=('Helvetica',10),height=2,width=8,bg='#c7f7ff',activebackground='#d4f8ff',command=lambda:poziomTrudnosciFunction(3))  
   
    #przyciski pól 1-9
    b1=Button(root,borderwidth=0, text=grid[0], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(0,grid))
    #funkcja koloru dla najeżdżania
    interakcjaZKursorem(b1,baseColourActive,baseColour)
    b2=Button(root,borderwidth=0, text=grid[1], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(1,grid))
    interakcjaZKursorem(b2,baseColourActive,baseColour)
    b3=Button(root,borderwidth=0, text=grid[2], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(2,grid))
    interakcjaZKursorem(b3,baseColourActive,baseColour)

    b5=Button(root,borderwidth=0, text=grid[3], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(4,grid))
    interakcjaZKursorem(b5,baseColourActive,baseColour)
    b6=Button(root,borderwidth=0, text=grid[4], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(5,grid))
    interakcjaZKursorem(b6,baseColourActive,baseColour)
    b4=Button(root,borderwidth=0, text=grid[5], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(3,grid))
    interakcjaZKursorem(b4,baseColourActive,baseColour)

    b7=Button(root,borderwidth=0, text=grid[6], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(6,grid))
    interakcjaZKursorem(b7,baseColourActive,baseColour)
    b8=Button(root,borderwidth=0, text=grid[7], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(7,grid))
    interakcjaZKursorem(b8,baseColourActive,baseColour)
    b9=Button(root,borderwidth=0, text=grid[8], font=('Helvetica',20),height=3,width=6,bg=baseColour ,command=lambda:b_click(8,grid))
    interakcjaZKursorem(b9,baseColourActive,baseColour)
   
   
    global buttonList
    buttonList=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
   
    #definuje rozmiar i grid przycisków
    bEasy.grid(row=0,column=0,pady=10)
    bMedium.grid(row=0,column=1,pady=10)
    bImpossible.grid(row=0,column=2,pady=10)
    StatusTrudnosci.grid(row=1,column=1)
   
    b1.grid(row=2,column=0,padx=5,pady=10)
    b2.grid(row=2,column=1,pady=10)
    b3.grid(row=2,column=2,padx=5,pady=10)

    b4.grid(row=3,column=0,pady=5,padx=5)
    b5.grid(row=3,column=1,pady=5)
    b6.grid(row=3,column=2,pady=5,padx=5)

    b7.grid(row=4,column=0,padx=5,pady=10)
    b8.grid(row=4,column=1,pady=10)
    b9.grid(row=4,column=2,padx=5,pady=10)
   
    root.mainloop()    
main()