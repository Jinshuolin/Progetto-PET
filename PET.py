import numpy as np
from scipy import constants
import pixelf
import matplotlib.pyplot as plt
class Pet:
    
    """
    Macchina del Pet

    Sono disponibili i seguenti metodi:
    cn: Modifica il numero di rilevatori
    cr: Modifica raggio macchina PET 
    ct: Modifica risoluzione temporale rilevatori
    cp: Modifica posizione del punto di emissione di Fotoni
    cd: Modifica durata diagnostica
    scan: Inizio diagnosi del paziente
    """
    def __init__(self, N, raggio, risoluzione, xsorgente, ysorgente, durata):
        """
        Costruttore del PET

        Parametri:
        N: numero di rilevatori da distribuire lungo la circonferenza.I rilevatori saranno posizionati uniformemente lungo la circonferenza.
        raggio: raggio della circonferenza macchina PET in centimetri [cm]
        risoluzione: risoluzione temporale dei rilevatori in nanosecondi [ns]
        xsorgente: coordinata x della sorgente di fotoni in centimetri [cm]
        ysorgente: coordinata y della sorgente di fotoni in centimetri [cm]
        durata: durata di tempo della diagnosi in minuti [min]

        """
        if (N <=1) or (risoluzione <=0 )or (durata <=0) or (raggio <=0):
            print ("Errore: il numero di rilevatori deve essere maggiore di uno. Il raggio, la risoluzione e la durata devono essere positivi")
        elif xsorgente**2 + ysorgente**2 >= raggio**2:
            print("Errore: la sorgente deve essere nell'interno del cerchio")
        else: 
            self.pixel =int(N)
            self.radius = raggio
            self.resolution = risoluzione
            self.xsorgente = xsorgente
            self.ysorgente = ysorgente
            self.time = durata
            print ("PET funzionante")

    def cr (self, rad):
        """
        Modifica raggio macchina PET

        Il valore del raggio deve essere > 0
        Parametro:
        rad: nuovo valore del raggio della macchina PET in centimetri [cm]
        """
        if rad <=0:
            print ("Errore: il raggio deve essere positivo")
        elif self.xsorgente**2 + self.ysorgente**2 >= rad**2:
            print ("Errore: il raggio è tale che il cerchio centrato nell'origine non contenga la sorgente al suo interno. Modificare prima la posizione della sorgente") 
        else:
            self.radius = rad
            print ("Raggio aggiornato:",self.radius, "cm")
    def ct (self, tempo):
        """
        Modifica risoluzione temporale dei rilevatori

        Il valore della risoluzione deve essere > 0
        Parametro:
        tempo: nuovo valore di risoluzione temporale in nanosecondi [ns]
        """
        if tempo <=0:
            print ("Errore: la risoluzione temporale deve essere positiva")
        else:
            self.resolution = tempo
            print ("Risoluzione aggiornata:", self.resolution, "ns")
            
    def cp (self, x,y):
        """
        Modifica la posizione della sorgente

        Assicurarsi che i valori delle coordinate x e y siano tali da appartenere all'interno del cerchio della macchina PET
        Parametri:
        x: coordinata x in centimetri [cm]
        y: coordinata y in centimetri [cm] 
        """
        
        if x**2 + y**2 >= self.radius**2:
            print ("Errore: la sorgente deve essere nell'interno del cerchio")
        else:
            self.xsorgente = x
            self.ysorgente = y
            print ("Posizione della sorgente in cm aggiornata: ({:},{:})".format(self.xsorgente, self.ysorgente))

    def cd (self, time):
        """
        Modifica durata diagnostica

        Il valore della durata diagnostica deve essere > 0
        Parametro:
        time: nuovo valore di durata diagnostica in minuti [min]
        """
        
        if time <=0:
            print ("Errore: la durata diagnostica deve essere un valore positivo")
        else:
            self.time = time
            print ("Durata diagnostica aggiornata:", self.time, "min")

    def cn (self, N):
        """
        Modifica il numero di rilevatori

        Il valore di N deve essere > 1. Se il valore è float allora si considererà solo la sua parte intera
        Parametro:
        N: Numero di rilevatori
        """
        if N <=1:
            print ("Errore: il numero deve essere maggiore di uno")
        else:
            self.pixel = int(N)
            print ("Numero rilevatori aggiornato:", self.pixel)
            
    def scan (self):
        """
        Diagnosi del paziente

        """
        
        lambda_ = int((input("Quale tipo di radionuclide è contenuto nell'iniezione? Fluoro_18 = 18, Carbonio_11 = 11 --> ")))
        if lambda_ == 18:
            lambda_ = 10**6*np.log(2)/110 * self.time # Numero di nuclei, costante di decadimento e durata tempo sarebbe 10**9 ma impossibile per il mio computer
        elif lambda_ == 11:
            lambda_ = 10**6*np.log(2)/20.33 * self.time # Numero di nuclei, costante di decadimento e durata tempo sarebbe 10**12 ma impossibile per il mio computer
        else:
            print ("Errore: non è stato selezionato nessuno dei due radionuclidi disponibili")

        numero_fotoni = np.random.poisson (lambda_)
        angles = np.random.uniform (-np.pi/2, np.pi/2, numero_fotoni)
        # Forma normale ax^2 + bx +c
        mask = angles != -np.pi/2
        tan = np.tan (angles[mask])
        a = 1+tan**2
        b = 2*tan*(self.ysorgente - self.xsorgente*tan)
        c = (self.xsorgente*tan)**2 - 2*self.xsorgente*self.ysorgente*tan - self.radius**2 + self.ysorgente**2
        x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a) # Angolo non -pi greco mezzi 
        x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a) # Angolo non -pi greco mezzi
        x3 = np.full (len(angles[~mask]), self.xsorgente) # Angolo - pi greco mezzi
        x4 = x3
        y1 = self.ysorgente + tan* (x1 - self.xsorgente)
        y2 = self.ysorgente + tan* (x2 - self.xsorgente)
        y3 = np.sqrt(self.radius**2 - x3**2)
        y4 = -y3
        # Ho gli array di soluzioni
        # Ora devo calcolare il tempo in cui raggiungono i rilevatori: tempo = spazio/velocità.
        
        
        sp1 = np.sqrt( (x1 - self.xsorgente)**2 + (y1 - self.ysorgente)**2)
        sp2 = np.sqrt( (x2 - self.xsorgente)**2 + (y2 - self.ysorgente)**2)
        t1 = sp1/(constants.c) * 10**7#[ns]
        t2 = sp2/(constants.c) * 10**7#[ns]
        sp3 = np.sqrt( (x3 - self.xsorgente)**2 + (y3 - self.ysorgente)**2) 
        sp4 = np.sqrt( (x4 - self.xsorgente)**2 + (y4 - self.ysorgente)**2)
        t3 = sp3/(constants.c) *10**7#[ns]
        t4 = sp4/(constants.c) *10**7#[ns]
        # Ora ad ogni misura di tempo deve essere assegnata una fluttuazione Gaussiana
        t1 = np.random.normal (t1, self.resolution)  # Tutti questi valori di tempo sono in nanosecondi!
        t2 = np.random.normal (t2, self.resolution)
        t3 = np.random.normal (t3, self.resolution)
        t4 = np.random.normal (t4, self.resolution)
        
        xp = np.concatenate ((x1,x3)) # I "Primi" fotoni della coppia
        yp = np.concatenate ((y1,y3)) # I "Primi" fotoni della coppia
        xs = np.concatenate ((x2,x4)) # I "Secondi" fotoni della coppia
        ys = np.concatenate ((y2,y4)) # I "Secondi" fotoni della coppia
        tp = np.concatenate ((t1,t3)) # Tempi dei "Primi" fotoni della coppia
        ts = np.concatenate ((t2,t4)) # Tempi dei "Secondi" fotoni della coppia
        maskt = (tp >0) & (ts >0) & (tp < (2*self.radius * 10**7) / constants.c) & (ts <(2*self.radius * 10**7) / constants.c)
        tp = tp[maskt]
        ts = ts[maskt]
        xp = xp[maskt]
        yp = yp[maskt]
        xs = xs[maskt]
        ys = ys[maskt]


        
        angoli_pixel  = pixelf.angle_pix(self.pixel)
        polarep = pixelf.angolatura(xp,yp,self.radius)
        polares = pixelf.angolatura(xs,ys,self.radius)
        indici1 = pixelf.indici(polarep, angoli_pixel)
        indici2 = pixelf.indici(polares, angoli_pixel)
        risultato = pixelf.posizione (self.radius, angoli_pixel, indici1, indici2, tp,ts,self.resolution)

        print ("La posizione dell'organo è ({:} +/- {:},{:}, +/- {:})".format (risultato[0],risultato[1],risultato[2],risultato[3]))
    
        print ("La discrepanza di coordinate è ({:}, {:})".format(np.abs(risultato[0]-self.xsorgente), np.abs(risultato[2]-self.ysorgente)))

 
        spazio = np.linspace (-self.radius, self.radius, 1000)
        circ_sup = np.sqrt(self.radius**2 - spazio**2)
        circ_inf = -circ_sup
        plt.plot (spazio, circ_sup, color = "Slategrey", label = "PET")
        plt.plot (spazio, circ_inf, color = "Slategrey")
        plt.errorbar (risultato[0],risultato[2], xerr = risultato[1],fmt = "*", yerr = risultato[3], label = "Posizione stimata dell'organo")
        plt.plot (self.xsorgente, self.ysorgente,"o", label = "Posizione effettiva dell'organo")
        legend =plt.legend()
        legend._legend_box.width = 45
        plt.title ("Risultati della diagnosi")
        plt.xlabel ("X [cm]")
        plt.ylabel ("Y [cm]")
        plt.show()
    
