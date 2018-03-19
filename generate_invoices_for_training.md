# Data generation when "real" data is not available
One of the challenges in this project was to improve on the training data.

The original Baseline produces invoices (and training targets) on the fly. We are proposing a pipeline where all data is on disk for different collaborators to load it from.

We wrote a notebook that generates invoices with corresponding targets and truth strings. The notebook fills a subdir with csv files and creates a zipfile for distribution.
The original generator was limited to two templates. We added 19 more templates based on real life examples. Personal details were altered and the parts of interest were changed into placeholders for the algorithm.

The main challenge in our pipeline is to make sure all collaborating parties work on the same collection of invoices and know how to identify each invoice. That is why we added a globally unique identifier to every invoice.

For the benefit of the stacker model, we store the "truth strings" of the invoice with the invoice in the same file. To accomplish that, we had to change the generation algorithm to return those strings in an array.

For a further explanation, read the invoices_generate_todisk.ipynb.
