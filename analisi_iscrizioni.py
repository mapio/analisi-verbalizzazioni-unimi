#!/usr/bin/env python

# Versione a linea di comando di https://github.com/mapio/analisi-verbalizzazioni-unimi/

from pathlib import Path
from sys import argv, exit

import pandas as pd
from tabulate import tabulate

*file_verbali, file_iscrizioni, nome_insegnamento = argv[1:]

def vse2e(voto, stato_esito):
    if stato_esito == 'Rifiutato': return '~' + voto
    if voto == 'Respinto': return 'RE'
    if voto == 'Ritirato': return 'RI'
    if voto == '30 e lode': return '33'
    return voto

verbali = []
for fv in file_verbali:
  verbali.append(pd.read_excel(fv, dtype = {'Matricola': object}).apply(lambda _: pd.Series({
      'Insegnamento': _['Descrizione insegnamento'],
      'Appello': _['Data appello'],
      'Matricola': _['Matricola'],
      'Esito': vse2e(_['Voto'], _['Stato Esito'])
  }), axis = 1).sort_values('Appello'))
verbali = pd.concat(verbali)

iscrizioni = pd.read_excel(file_iscrizioni, dtype = {'Matricola': object})[['Matricola', 'Cognome', 'Nome']].set_index('Matricola')

storia = ( verbali[verbali.Insegnamento == nome_insegnamento]
            .merge(iscrizioni, on = 'Matricola', how = 'right')
            .fillna('').groupby('Matricola').Esito
            .agg(lambda _: ', '.join(_)) )
storia.name = 'Storia'

if ( storia.shape[0] != iscrizioni.shape[0]): exit(-1)

print(tabulate(iscrizioni.join(storia).sort_values('Matricola'), headers = 'keys', tablefmt = 'psql'))