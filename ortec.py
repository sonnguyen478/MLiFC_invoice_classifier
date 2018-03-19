"""
ortec.py
simple library by Rik for loading invoices batch wise into a classifier or extractor model
"""

import glob
import pandas as pd

def select_batch(start=0, batch_size=32, stop=32):
    while start < stop:
        yield [start, min(stop, start + batch_size)]
        start += batch_size
#

def select_filebatch(filenames=[], start=0, batch_size=32, total=32):
    stop = min(len(filenames)+1, total)
    for (first_idx, last_idx) in select_batch(start=0, batch_size=batch_size, stop=stop):
        yield filenames[first_idx:last_idx]
#

def select_invoicebatch(filenames=[], batch_size=32, total=32):
    """yields list of invoices, list of targets, list of truths"""
    for file_batch in select_filebatch(filenames=filenames, batch_size=batch_size, total=total):
        invoices = []
        targets = []
        truths = []

        for file in file_batch:
            mysample = pd.read_csv(file)
            # each file only contains one row, that's why we get away with the 0 in .loc[0,'invoice']
            # else we needed to start another level of iteration
            invoice  = mysample.loc[0,'invoice']
            target   = eval(mysample.loc[0,'target'])
            truth    = eval(mysample.loc[0,'truth'])
            invoices.append(invoice)
            targets.append(target)
            truths.append(truth)
        #
        yield invoices, targets, truths
    #
#