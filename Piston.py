# -*- coding: utf-8 -*-
"""
Bienvenue dans la partie commentaire.

Celle ci est dédiée à l'explication des différents calculs réalisés pour
ce code. Si vous avez quelque difficulté à lire quelque information, vous 
pouvez nous contacter par email.


Partie I : mise en contexte:
    
    Pourquoi il n'est pas nécéssaire de prendre en compte les collisions entre
    les molécules de gaz?
    
    Les collisions entres les molécules de gaz sont elastiques donc aucune énergie
    n'est perdue (concervation de l'énergie), et cela entraine que la collision
    entre les molécules n'est pas importante, puisqu'elle n'a aucune 
    répercussion sur le système.

Partie II : Travail demandé, cahier des charges:
    
    La relativité Galiléenne et de Newton fait que les balles qui représentent
    les molécules perdent leur vitesse (et eur energie) quand elles heurtent 
    les bords et le paroi du piston qui bouge à vitesse constante. 
    On utilise ce calcul pour déterminer les conditions limites des mouvements
    des balles.

3) Partie III : Interprétation physique:
    a:
        La relation donnée entre a température et le volume ne s'appliquent que
        dans les conditions suivantes:
    
        1- La vitesse des molécules est bien plus grande par rapport à celle du
        piston.
        2- Le nombre de balles est très grand
    
        Nous avons fait un graphique, avec la condition if. Il trace la 
        température et l'autre le volume juste pour voir s'il seront les mêmes
        ou différents. Nous avons constaté que lorsqu'il y avait peu de balles
        ou lorsque la différence entre la vitesse du piston et celle des balles
        est faible, les deux graphiques ne seront pas les mêmes. Ces graphiques
        sont du coté droit lorsque le programme est lancé.
    b:
       Pour le calcul de gamma, nous avons fait une seconde figure et écrit les
       calculs dedans. Nous avons trouvé: gamma = 5/3
        
Bonne chance pour lire le script

kebsibadr@gmail.com
poncet.oc55@gmail.com
"""

import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani

#On définit une fonction pour calculer v^2 = vx^2 + vy^2

vit = lambda x,y: x**2+y**2

#Définition de variables multiples: itteration_speed(BoundarySpeed)
#Valeur maximum des axes x et y (sx,sy), vitesse Maximum (V)
#le nombre d'itérations(stop), Volume du piston(volume)
#nombre de balles(B) et le temps ticks1 (dt) pour mieux
#observer le déroulement de l'opération


sx=1000
sy=200
V= 10000
dt=sy/2./V

print("Bienvenue à la simulation de piston.\n\
Ce code à été écrit pour le CC3.\n\n\
Vous pouvez changer n'importe quelle variable du code\n\
mais gardez en tête qu'elle détermine \n\
beaucoup de paramètres différents \n\
Il est conseillé par exemple, d'augmenter la vitesse des balles\n\
si vous voulez augmenter la vitesse du piston\n\n\
SVP prenez en compte que chaque frame number correspond\n\
à %.3f seconds.Par example, écrire que la vitesse du piston \n\
est = X, le piston bougera à X*%.3f unité par frame"%(dt,dt))

error = "Vous n'avez pas écrit des bonnes valeurs."
try:
    conditions=input("SVP, écrire le nombre de balles/molécules de gaz,\n\
dans le piston, la vitesse du piston et le nombre \n\
d'itérations (frames) séparés par une virgule (balls,moving wall,frames)\n\n")

    B=int(conditions.split(sep=",")[0])
    BoundarySpeed=float(conditions.split(sep=",")[1])
    stop=float(conditions.split(sep=",")[2])
except:
    print(error)
    try:
        B=int(input("Veuillez tapper les nombre des balles: "))
    except:
        B=int(input("Le nombre des balles doit être un nombre entier,\n\
Veuillez tapper les nombre des balles:  "))
    BoundarySpeed=float(input("Veuillez tapper la vitesse d'expantion: "))
    stop=float(input("Veuillez tapper le nombre d'itteration (frames): "))





volume=sx*(sy)
volumeInit=volume

#Different listes pour grapher les graphs
xdata,ydata,volist,tempist,det=[],[],[],[],[]
#assigner les vecteurs aux balles
#et mettre leurs coordonnées et vitesses à 0 pour le moment

balls = np.zeros(B, dtype=[('position', float, 2),
                           ('velocity', float, 2)])


#leur assigner des vitesses et coordonnées au hasard

balls['position'] = np.random.uniform(0, 1, (B, 2))
balls['position'][:,0]*=sx
balls['position'][:,1]*=sy
balls['velocity'] = np.random.uniform(-1*V, V, (B, 2))

ballsInit = balls

#Calculer la vitesse initiale de chaque balle
#La vitesse de chaque balles est calculer comme V = sqrt(V_x**2+V_y**2)
#Puis, on prend la somme des toutes les vitesses en utilisant cumsum et[-1]
#et on divise par le nombre de balles(B)

velAVG=np.cumsum(vit(balls['velocity'][:,0],\
                       balls['velocity'][:,1]))[-1]/B
#velInit=np.cumsum(vit(balls['velocity'][:,0],balls['velocity'][:,1]))[-1]/B

SecretEnding = "Il y a une deuxieme figure qui contient les calcules \
mathematiques"
#Maintentant vient la partie graphique


explain = "\n\nL'équation mathématique pour un gaz parfait subissant \
un processis (i.e., no entropy generation) adiabatic reversible peut \
être représenté par l'équationde processus polytropique:\n\
P * V^gamma = constant \n\
SOurce: wikipédia.\n\n"

print(explain)

if 1:
    fig2 = plt.figure(2)
    textax = plt.axes(xlim=(0,100), ylim=(0,200))
    textax.set_title("Mathematical Calculations")



    textax.text(0,190,r'$PV^\gamma = constant$' ,fontsize=12.5)
    textax.text(0,170,r'$P = \frac{\frac{2}{3}Nk_bT}{V}$' ,fontsize=12.5)
    textax.text(0,154,r'$\Longleftrightarrow (\frac{\frac{2}{3}Nk_bT}{V})*V^\gamma=constant$' ,fontsize=12.5)
    textax.text(0,142,r'$\Longleftrightarrow V^{\gamma-1}*T=constant\longrightarrow(1)$' ,fontsize=12.5)
    textax.text(0,130,"PAr nos calcules, on a:",fontsize=12.5,style='italic')
    textax.text(0,118,r'$\frac{T}{T_0}=(\frac{V}{V_0})^{-\frac{2}{3}}$' ,fontsize=12.5)
    textax.text(0,100,r'$\Longleftrightarrow T*V^{\frac{2}{3}}=T_0*V_0^{\frac{2}{3}}$' ,fontsize=12.5)
    textax.text(0,88,r'$\Longleftrightarrow T*V^{\frac{2}{3}}=constant\longrightarrow(2)$' ,fontsize=12.5)
    textax.text(0,76,"combining 1 & 2 we get:",fontsize=12.5,style='italic')
    textax.text(0,64,r'$\gamma-1=\frac{2}{3}$',fontsize=12.5)
    textax.text(0,48,r'$\Longleftrightarrow\gamma=\frac{5}{3}$',fontsize=12.5)



fig = plt.figure(1)

#Definition de la taille de notre écran


#Cette partie est pour définir le périmètre en relation avec la vitesse du
#piston (BoundarySpeed)et du nombre d'itérations (stop).
if BoundarySpeed*dt*stop <= sy:
    LIM = 600
else:
    LIM = 200+BoundarySpeed*dt*stop*1.5
    

ax = plt.axes(xlim=(0,sx), ylim=(0,LIM))
ax.set_title('Piston', fontsize=20)

#Mettre les positions randoms initiales dans le piston
balle = ax.scatter(balls['position'][:, 0], balls['position'][:, 1],\
                   c='magenta', s=10)

#cette ligne représente le paroi qui bouge


limit, = plt.plot([0, sx], [sy, sy],'r--')

#Tracer la vitesse comme fonction dans le volume du piston
if 1:
    ax1= fig.add_axes([0.21875, 0.5, 0.25, 0.25],\
                  xlabel='Volume $m^3$',\
                  ylabel=r'Average Velocity $(\frac{m^2}{s^2})$')
    ax1.grid()
    ax1.set_ylim(bottom=velAVG-1000, top=velAVG)

    volBoundary = int(volumeInit+sx*stop*BoundarySpeed*dt)

    ax1.set_xlim(left=volume, right=volBoundary)
    ax1.set_title('Vitesse moyenne au carré\nen fonction du volume')
    vvgraph, = ax1.plot([], [], lw=1)

if 1:
    
    ax2=fig.add_axes([0.6, 0.5, 0.25, 0.25],\
                      xlabel=r'Time(Frames)($10^{-2}*s$)',\
                      ylabel=r'$\frac{T}{T_0}$ & $(\frac{V}{V_0})^{-\frac{2}{3}}$')
    ax2.grid()
    ax2.set_xlim(left=0,right=stop)
    ax2.set_ylim(bottom=0.9,top=1.1)
    ax2.set_title("Temperature(green)\Volume(red)")
    Temp, = ax2.plot([], [],'g', lw=1)
    Vol, = ax2.plot([], [],'r', lw=1)
    red_patch = mpatches.Patch(color='red', label='Volume')
    green_patch = mpatches.Patch(color='green', label='Temprature')
    ax2.legend(handles=[red_patch,green_patch])
    

sec = fig.text(0.155,0.025,SecretEnding)
#Maintenant le meilleur: definir la fonction magique



def setData():
    #Les variables suivantes sont nécessaires dans la fonction
    global sy,volume,velAVG,xdata,ydata
    
    xdata, ydata = [], []
    sy=200
    balls = ballsInit
    velAVG = np.cumsum(vit(balls['velocity'][:,0],\
                             balls['velocity'][:,1]))[-1]/B
    N = 0
    while N <= stop:
        #Régler les conditions limites en gardant à l'esprit que l'energie 
        #est concervée
        balls['position'][:,0] += balls['velocity'][:,0] * dt
        balls['position'][:,1] += balls['velocity'][:,1] * dt
        for i in range(B):
            #Noter ici que dt = 1 et ça ne change pas le résultat
            #calculer qui va X = X0 + Vdt
            #avec X0: postion initiale
            #X: position à n'importe quel temps
            #V: vitesse de la balle
            #dt: time frame or time difference prise comme 1 dans ce 
            #programme.
            if balls['position'][i,0] >= sx :
                balls['position'][i,0]=sx-(balls['position'][i,0]-sx)
                balls['velocity'][i,0] *= -1
            elif  balls['position'][i,0] <= 0:
                balls['position'][i,0]=-balls['position'][i,0]
                balls['velocity'][i,0] *= -1        
            
            if balls['position'][i,1] >= sy :
                balls['position'][i,1]=sy-(balls['position'][i,1]-sy)
                balls['velocity'][i,1] = -balls['velocity'][i,1]+BoundarySpeed
            #Notons l'ajout des vitesses limites pour que les balles
            #perdents de la vitesse lorsqu'elles heurtent le piston
            #Ce calcul est fait en respectant la relativité galiléennese 
            #Les molécules vont perdre de l'énergie tant qu'elles heurtent le 
            #piston qui ne verra pas son energie augmenter car sa masse est bien
            #supérieure M(wall) >> M(molecule)
            elif balls['position'][i,1] <= 0:
                balls['position'][i,1]=-balls['position'][i,1]
                balls['velocity'][i,1] *= -1
        volume=sx*(sy)
        velAVG=np.cumsum(vit(balls['velocity'][:,0]\
                            ,balls['velocity'][:,1]))[-1]/B 
                              
        #Cette partie est le piston en mouvement
        sy+=BoundarySpeed*dt
        

        yield sy,volume,velAVG,balls,N
        N+=1
        

        

def update(setData):

    
    balle.set_offsets(setData[3]['position'])
    limit.set_ydata([setData[0],setData[0]])
#et finallement, le piston est une ligne qui monte
        #xdata and ydata va tracer la vitesse moyenne comme une fonction
        #du volume total.
        
    xdata.append(setData[1])
    ydata.append(setData[2])
    vvgraph.set_data(xdata, ydata)
    
    
    ymin, ymax = ax1.get_ylim()
    if velAVG <= ymin:
            ax1.set_ylim(ydata[-1], ymax)
            ax1.figure.canvas.draw()
        
    #Ce sont les données des balles de chaqueframe tick.
    


    if 1:
        tempist.append((ydata[-1]/ydata[0]))
        volist.append((xdata[-1]/xdata[0])**-(2./3.))
        det.append(setData[4])
        Temp.set_data(det, tempist)
        Vol.set_data(det, volist)
        Ymin, Ymax = ax2.get_ylim()
        if (ydata[-1]/ydata[0])<=Ymin\
        or (xdata[-1]/xdata[0])**-(2./3.)<=Ymin:
            ax2.set_ylim(Ymin-0.1, Ymax)
            ax2.figure.canvas.draw()
        
    
    if setData[4]==stop:
        TempFac = (ydata[-1]/ydata[0])
        VolFac = (xdata[-1]/xdata[0])**-(2./3.)
        diff=np.abs(TempFac-VolFac)
        print('Facteur de la Temprature est: %f\nFacteur du Volume est: %f\n\
et la différence entre eux est: %f' %(TempFac,VolFac,diff))
        if diff > 0.1:
            print("On voit ici que la différence entre les deux\
 facteurs est grand et cela est dû à la vitesse de la paroi mobile\
 qui est rapide par rapport à la réalité. Je pense que %i par rapport\
 à %i est un peu accablante, n'est-ce pas?\n\
 Le rapport entre la vitesse des molécules et celle d'expansion est\
 ce qui est un peu irréaliste"\
 %(BoundarySpeed,V,V/BoundarySpeed))
        else:
            print("La différence entre les deux facteur est minime\
 donc on peut dire que les deux facteurs sont egales.")


    return balle,limit,vvgraph,Temp,Vol,

#On laisse maitenant la magie opérer
animation = FuncAnimation(fig,update,setData,interval=20,\
                          blit=False,repeat=False)
#animation.save('animation.mp4', fps = 5)
plt.show(animation)
