# Relazione GPOI
### By Samuele Facenda, Thomas Cetto, Marco Polimeni, Stefano Tosi


Il nostro gruppo si è occupato di creare un programma che permette di, dato in un input una parte non completa di un brano suonato al pianoforte e un certo numero di note, ampliare il brano iniziale aggiungendo la quantità di note richieste, rispettando le tonalità del brano dato in input.

Per realizzarlo abbiamo usato python, tramite alcuni strumenti come PyTorch per la realizzazione della rete neurale, Pandas e Numpy per la gestione dei dati, Music21 per gestire le canzoni e altre librerie varie.
Per il training del modello abbiamo usato un dataset di circa 1300 canzoni, ottenute da Magenta, un progetto di Google. Per gestire queste canzoni abbiamo usato dei file MIDI, che contengono tutte le informazioni di una canzone, nota per nota.

### Spiegazione piu' tecnica

Abbiamo realizzato una rete neurale di tipo LSTM(Long Short Term Memory), particolarmente adatta all'analisi di serie di dati, per il fatto che riesce a fare previsioni tenendo conto
sia del breve periodo che del lungo periodo(come invece non riescono a fare le RNN, recurrent neural network, classiche, di cui le LSTM sono una sottofamiglia.

Con il modello trainato partendo da una corta sequenza di note si riesce a generare una nuova sequenza di note di lunghezza potenzialmente infinita, questa viene poi salvata in
un file midi per poi poter essere riprodotta.
