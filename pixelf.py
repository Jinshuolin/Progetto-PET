import numpy as np
from scipy import constants
import pixelf


"""Funzioni riguardanti i rilevatori PET"""

def angle_pix (N):
    """
    Definisce la posizione angolare dei rilevatori lungo la circonferenza

    Parametro:
    N: numero pixel
    Restituisce:
    angles: array di N angoli distribuiti uniformemente lungo la circonferenza
    """
    angles = 2*np.pi/N *np.arange (N) + np.pi/N
    return angles
def angolatura (x,y,raggio):
    """
    Funzione che restituisce la posizione angolare del punto

    Parametri:
    x: coordinata x del punto
    y: coordinata y del punto
    raggio: raggio della macchina PET
    Restituisce:
    angolo: array di angoli formati con semiasse positivo delle ascisse che il punto forma rispetto all'origine
    """
    mask1 = (x>0) & (y>=0)
    mask2 = y == raggio
    mask3 = x<0
    mask4 =  y==- raggio
    mask5 = (x > 0) & (y<0)

    angolo = np.ones (len(x))
    angolo[mask4] = 3*np.pi/2
    angolo[mask2] = np.pi*2
    angolo[mask1] = np.arctan (y[mask1]/x[mask1])
    angolo[mask3] = np.arctan (y[mask3]/x[mask3]) + np.pi
    angolo[mask5] = np.arctan (y[mask5]/x[mask5]) + 2*np.pi
    return angolo

def indici (theta, angles):
    """
    Funzione che, dati le posizioni angolari dei punti restituisce gli indici corrispondenti ai rilevatori, posizionati agli angoli angles
    Parametri:
    theta: posizione angolare dei punti
    angles: posizione angolare dei rilevatori
    Restituisce:
    marchi: array di indici corrispondenti ognuno al rilevatore nel quale si trova ogni punto
    """
    range1 = angles - np.pi /(len(angles))
    marchi = np.zeros(len(theta), dtype = int)
    for i in range (len(theta)):
        delta_angolo = np.full(len(range1),theta[i])
        delta_angolo = delta_angolo - range1
        mask = delta_angolo <0
        delta_angolo[mask] = 10
        indice_minimo = np.argmin (delta_angolo)
        marchi[i] = int(indice_minimo)

    return marchi

def posizione (raggio,angles,marchio1,marchio2,tempo1,tempo2,resolution):
    """
    Funzione che restituisce la posizione della sorgente forniti i seguenti parametri
    Parametri:
    raggio: raggio della circonferenza in centimetri [cm]
    angles: angoli dei pixel
    marchio1: indici corrispondenti ai pixel colpiti da un fotone di ogni coppia
    marchio2: indici corrispondenti ai pixel colpiti dall'altro fotone della coppia
    tempo1: tempi in nanosecondi [ns] che i fotoni corrispondenti a marchio1 colpiscono il rilevatore
    tempo2: tempi in nanosecondi [ns] che i fotoni corrispondenti a marchio2 colpiscono il rilevatore
    resolution: risoluzione della macchina PET in nanosecondi [ns]
    Restituisce array contenente i seguenti valori:
    x_medio: miglior valore statistico coordinata x della sorgente di radiazioni
    sigma_x: incertezza sul valore x
    y_medio: miglior valore statistico coordinata y della sorgente di radiazioni
    sigma_y: incertezza sul valore y
    """
    x_c = raggio * np.cos(angles)
    y_c = raggio * np.sin(angles)
    xp1 = x_c[marchio1]
    yp1 = y_c[marchio1] 
    xp2 = x_c[marchio2]
    yp2 = y_c[marchio2]
    delta_raggio = 1
    delta_angles = np.pi/len(angles)

    delta_xp1 = np.sqrt((raggio*np.sin(angles[marchio1])*delta_angles)**2 + (np.cos(angles[marchio1])*delta_raggio)**2)
    delta_yp1 = np.sqrt((raggio*np.cos(angles[marchio1])*delta_angles)**2 + (np.sin(angles[marchio1])*delta_raggio)**2)
    delta_xp2 = np.sqrt((raggio*np.sin(angles[marchio2])*delta_angles)**2 + (np.cos(angles[marchio2])*delta_raggio)**2)
    delta_yp2 = np.sqrt((raggio*np.cos(angles[marchio2])*delta_angles)**2 + (np.sin(angles[marchio2])*delta_raggio)**2)
    

    
    sp1 = constants.c * tempo1 * 10**(-7)
    sp2 = constants.c * tempo2 * 10**(-7)
    distanze = np.sqrt((xp1-xp2)**2 + (yp1-yp2)**2)
    param1 = sp1 / distanze
    param2 = sp2 / distanze
    x1 = xp1 + param1*(xp2 - xp1)
    y1 = yp1 + param1*(yp2 - yp1)
    x2 = xp2 + param2*(xp1 - xp2)
    y2 = yp2 + param2*(yp1 - yp2)

    
    
    const1 = constants.c * 10**(-7) / distanze
    delta_x1 = np.sqrt(((1-const1*tempo1*(1-((xp2-xp1)/distanze)**2))*delta_xp1)**2 +(const1*tempo1 * (1- ((xp2-xp1)/distanze)**2)* delta_xp2)**2 + (const1*tempo1/ (distanze**2) * (yp1-yp2)*(xp2-xp1))**2 * (delta_yp1**2 + delta_yp2**2) + (const1*(xp2-xp1) * resolution)**2)
    delta_y1 = np.sqrt(((1-const1*tempo1*(1-((yp2-yp1)/distanze)**2))*delta_yp1)**2 +(const1*tempo1 * (1- ((yp2-yp1)/distanze)**2)* delta_yp2)**2 + (const1*tempo1/ (distanze**2) * (yp1-yp2)*(xp2-xp1))**2 * (delta_xp1**2 + delta_xp2**2) + (const1*(yp2-yp1) * resolution)**2)
    delta_x2 = np.sqrt(((1-const1*tempo2*(1-((xp1-xp2)/distanze)**2))*delta_xp2)**2 +(const1*tempo2 * (1- ((xp1-xp2)/distanze)**2)* delta_xp1)**2 + (const1*tempo2/ (distanze**2) * (yp1-yp2)*(xp1-xp2))**2 * (delta_yp1**2 + delta_yp2**2) + (const1*(xp1-xp2) * resolution)**2)
    delta_y2 = np.sqrt(((1-const1*tempo2*(1-((yp1-yp2)/distanze)**2))*delta_yp2)**2 +(const1*tempo2 * (1- ((yp1-yp2)/distanze)**2)* delta_yp1)**2 + (const1*tempo2/ (distanze**2) * (yp2-yp1)*(xp2-xp1))**2 * (delta_xp1**2 + delta_xp2**2) + (const1*(yp1-yp2) * resolution)**2)
  
    
    x = np.concatenate((x1,x2))
    y = np.concatenate((y1,y2))    
    sigma_x = np.concatenate ((delta_x1,delta_x2))
    sigma_y = np.concatenate ((delta_y1,delta_y2))
    w_x = 1/(sigma_x ** 2)
    w_y = 1/(sigma_y ** 2)
    x_medio = np.average (x,weights = w_x)
    y_medio = np.average (y,weights = w_y)
    sigma_x = 1 / np.sqrt(np.sum (w_x))
    sigma_y = 1 / np.sqrt(np.sum (w_y))
    
    
    return np.array([x_medio,sigma_x,y_medio,sigma_y])




    
    
