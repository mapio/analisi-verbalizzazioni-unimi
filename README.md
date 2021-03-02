# Analisi Verbalizzazioni @ UniMI

Questo *notebook* consente di svolgere alcune semplici analisi a partire dai
verbali estratti tramite la funzione [Archivio verbali ed esiti
finali](https://work.unimi.it/boDocenti/wicket/page?3) dell'applicazione [B.O.
Docent](https://work.unimi.it/boDocenti/) di UniMI; più in generale consente di
svolgere le analisi a partire da un qualunque elenco di verbali d'esame che
registrino, per ciascuna prova, l'*insegnamento* a cui si riferisce, la *data*
in cui è avvenuta, il numero di *matricola* dello studente (o un qualunque
identificatore unico del medesimo) e l'*esito* della prova.

## Installare il software

Per eseguire il notebook, oltre a scaricare l'estratto dall'archivio verbali, è
necessario usare una versione recente di Python (3.x) ed installare le
necessarie dipendenze col comando

    pip install -r requirements.txt

può essere comodo dapprima creare ed attivare un un *virtual environment*
(usando il modulo [venv](https://docs.python.org/3/library/venv.html) della
libreria standard di Python) con i comandi

    python3 -m venv venv
    source ./venv/bin/activate

Una volta installato il software è possibile aprire il notebook con il comando

    jupyter notebook "Analisi Verbalizazioni.ipynb"