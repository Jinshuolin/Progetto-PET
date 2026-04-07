# Progetto-PET
Progetto PET Metodi Computazionali Fisica

Saranno Presenti nella repository due file : PET.py e pixelf.py

Nel primo file sono presenti il costruttore degli oggetti Pet con i parametri nel seguente ordine: 

 N: numero di rilevatori da distribuire lungo la circonferenza. I rilevatori saranno posizionati uniformemente lungo la circonferenza.
 
 raggio: raggio della circonferenza macchina PET in centimetri [cm]
 
 risoluzione: risoluzione temporale dei rilevatori in nanosecondi [ns]
 
 xsorgente: coordinata x della sorgente di fotoni in centimetri [cm]
 
 ysorgente: coordinata y della sorgente di fotoni in centimetri [cm]
 
 durata: durata di tempo della diagnosi in minuti [min]
 
Sono presenti inoltre, sempre in PET.py i seguenti metodi:

 cn: Modifica il numero di rilevatori

 cr: Modifica raggio macchina PET 
 
 ct: Modifica risoluzione temporale rilevatori
 
 cp: Modifica posizione del punto di emissione di Fotoni

 cd: Modifica durata diagnostica
 
 scan: Inizio diagnosi del paziente
 
L'ultimo metodo permette, insieme alle funzioni presenti nel file pixelf.py, di inziare la diagnosi del paziente e di stimare con precisione la 
posizione dell'organo, che è stato approssimato a punto.

Nei file, per ogni funzione o metodo, sono presenti docstring che descrivono i parametri necessari per il corretto funzionamento di essi.

Nel file main.py è presente un esempio di utilizzo di un oggetto Pet. Si è usato prima di tutto il costruttore con parametri iniziali (1000, 10, 0.5, 0.5, 0.5, 30). Sono stati usati gli altri metodi presenti nella classe per modificare tali parametri e infine si è usato il metodo scan per la diagnostica e la ricerca della posizione dell'organo.

Se si vuole provare autonomamente i metodi della classe in un file a parte, prima di tutto bisogna fare l'import dei moduli PET.py e pixelf.py.


