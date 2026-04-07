# Progetto-PET
Progetto PET Metodi Computazionali Fisica

Saranno Presenti nella repository due file : PET.py e pixelf.py

Nel primo file sono presenti il costruttore degli oggetti Pet con i seguenti parametri: 

 N: numero di rilevatori da distribuire lungo la circonferenza.I rilevatori saranno posizionati uniformemente lungo la circonferenza.
 
 raggio: raggio della circonferenza macchina PET in centimetri [cm]
 
 risoluzione: risoluzione temporale dei rilevatori in nanosecondi [ns]
 
 xsorgente: coordinata x della sorgente di fotoni in centimetri [cm]
 
 ysorgente: coordinata y della sorgente di fotoni in centimetri [cm]
 
 durata: durata di tempo della diagnosi in minuti [min]
 
Sono presenti inoltre i seguenti metodi:

 cn: Modifica il numero di rilevatori

 cr: Modifica raggio macchina PET 
 
 ct: Modifica risoluzione temporale rilevatori
 
 cp: Modifica posizione del punto di emissione di Fotoni

 cd: Modifica durata diagnostica
 
 scan: Inizio diagnosi del paziente
 
L'ultimo metodo permette, insieme alle funzioni presenti nel file pixelf.py, di inziare la diagnosi del paziente e di stimare con precisione la 
posizione dell'organo, che è stato approssimato a punto.
Nei file, per ogni funzione o metodo, sono presenti docstring che descrivono i parametri necessari per il corretto funzionamento di essi.
Si provi a creare un oggetto di tipo Pet, facendo attenzione al fatto che potrebbe non essere creato correttamente in caso vi siano parametri contraddittori o non sensati, quali il numero di pixel che non può certamente essere negativo.
Si provi a usare i metodi che permettono di cambiare i parametri dopo aver creato l'oggetto di tipo Pet.
Infine, se si è soddisfatti con i parametri immessi, usare il metodo scan in modo da poter stimare la posizione dell'organo.
