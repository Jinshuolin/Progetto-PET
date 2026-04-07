import pixelf
import PET

paziente = PET.Pet (1000, 10, 0.5, 0.5, 0.5, 30) # Creazione oggetto Pet con 1000 pixel, un raggio di 10 cm, una risoluzione temporale di 0.5 ns, in posizione (0.5,0.5) cm e con durata di diagnosi di 30 min
paziente.cr (20) # Cambiamento del raggio a 20 cm
paziente.ct (0.20) # Cambiamento della risoluzione temporale a 0.20 ns
paziente.cp (0.7,1) # Cambiamento della posizione in (0.7,1)
paziente.cd (28) # Cambiamento durata a 28 min
paziente.cn (3000) # Cambiamento numero di pixel a 3000 pixel
paziente.scan() # Diagnosi del paziente

