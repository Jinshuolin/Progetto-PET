import pixelf
import PET
print ("Saranno eseguiti gli scan di 6 pazienti")
print ("Primo paziente")
paziente = PET.Pet (1000, 10, 0.5, 0.5, 0.5, 30) # Creazione oggetto Pet con 1000 pixel, un raggio di 10 cm, una risoluzione temporale di 0.5 ns, in posizione (0.5,0.5) cm e con durata di diagnosi di 30 min
paziente.cr (20) # Cambiamento del raggio a 20 cm
paziente.ct (0.20) # Cambiamento della risoluzione temporale a 0.20 ns
paziente.cp (0.7,1) # Cambiamento della posizione in (0.7,1)
paziente.cd (28) # Cambiamento durata a 28 min
paziente.cn (3000) # Cambiamento numero di pixel a 3000 pixel
paziente.scan() # Diagnosi del paziente

print ("Secondo paziente")
paziente2 = PET.Pet (3000, 20, 1.0, 10, 11, 60)
paziente2.scan()

print ("Terzo paziente")
paziente3 = PET.Pet (4000, 30, 0.5, -0.5, 20, 40)
paziente3.cr (26)
paziente3.cn (50000)
paziente3.ct (0.89)
paziente3.cd (41)
paziente3.scan()

print ("Quarto paziente")

paziente4 = PET.Pet (10000, 25, 0.25, -2.5, -15, 10)
paziente4.cd (39)
paziente4.cr (23)
paziente4.scan()

print ("Quinto paziente")
paziente5 = PET.Pet (500, 40, 0.15, 2.5, 20, 20)
paziente5.cn (30000)
paziente5.cr (30)
paziente5.ct (0.17)
paziente5.cp (20,-12)
paziente5.cd (40)
paziente5.scan()

print ("Ultimo paziente")
paziente6 = PET.Pet (300, 60, 0.15, 30, -22, 20)
paziente6.cn (60000)
paziente6.ct(0.40)
paziente6.cd (23)
paziente6.scan()
