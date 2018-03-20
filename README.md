# Invoice classifier - group_x
this file contains all the documentation of our attempt at Ortec challenge for an invoice field extractor.

## INDEX
1. Content of the repo
2. What we have made
3. Description of our processing pipeline
4. Generation of data
5. Expansion of the project
6. Reflections

## 1. Content of the repo
### TOC notebooks
* Baseline Ortec: Jannes' original (updated via Slack)
* Ortec_jannes_1G: ditto, with improvements
* Ortec_enea_regex_dragon_1G: Enea's model, uses regular expressions to extract fields (IBAN only really)
* Ortec_shaffy_1G: Shaffy's model, like Jannes', experiments with hyper parameters

* invoices_generate_todisk: generates invoices/taregts/truths and saves them to disk
* invoices_from_disk_sample_code: shows how to use the generated invoices in your extractor notebooks
* ortec.py: library used by invoices_from_disk_sample_code; loads batches of invoices

* IBAN_generation: generates IBANs and has multiple ways to introduce noise into strings, for training purposes
* IBAN_stacker: model for IBANs only, stacks multiple outputs to create one good prediction

### Model maturity
1G: model generates invoices on the fly, using create_invoice()
2G: same, but saves output to disk for future stackers to pick up. output must include ground truth in string format
G2: similar, but confused; takes input from disk, but does not save to disk
3G: best of all; reads and writes disk stored invoices, targets and ground truths

## 2. What we have done
### Aim
The aim of the project is to sort text from text-format invoices and correctly output the text related to each category.

### Approach
* Generate our own larger pool of invoices from 21 different invoice templates.
* Use the pool of generated invoices to build models that make predictions for each category and outputs the related text.
* Input the outputs of the models to a stacker, that assigns weights to the predictions and to produce the best possible prediction.

![proposed pipeline for extraction of info from invoices](https://github.com/riklmr/MLiFC_invoice_classifier/blob/master/ortec_invoice_pipeline_group_X.png "proposed pipeline for extraction of info from invoices")


### Random details
* model "RegExDragon" is a traditional algorithm based on regular expressions. It only extracts IBAN successfully.
* all extractor models need to take input and produce outputs that are consistent in format and content.
  * This proves to be a challenge in itself. Jannes' notebook produces examples on the fly. We must find a way and a format to store the generated examples on disk and a way to share the uniquely identified invoices among team members. Each individual invoice must be accompanied by its "truth values" for training/testing.
* the stacker algo takes in 1 or more sets of strings (identified by the invoice's uuid) and spits out a corrected set of similar strings. It aims to select the strongest inputs or strongest parts of strings and recombine these into better strings.
 * for instance: two models predict the KvK number to be: 12345678 and I2345678 repectively. The first is correct and the stacker should learn to select that one as its output. In order to train the stacker, it needs the truth for the KvK number as a target.
 * different example: two models predict the IBAN to be: NL12 AB#D 3456 7890 12 and NL12 #BCD 3456 7890 12 respectively. Both are mutated by noise, but the correct IBAN can be extracted by a model that learns to separate the signal from the noise. Call it error correction, if you like....
 
## 3. What we would like to happen..

We first defined a data generator that generates 47000 different invoices from 21 different templates. This data is then saved to a disk to be used by the different models. 
Next we would like to create 4 models which read in the different invoices and return an output of 5 strings which represent each of the five categories i.e. sender name, sender KVK, sender IBAN, invoice reference and the total amount due. 
The objective is for each model to use a different method to derive the 5 strings. 
At this time the models are:
* baseline provided in the course
* our own improvement on the baseline
* a string extractor via regexes.
After which we put these outputs in a NN which we call the Stacker. 

We want the Stacker model to do 2 things, first of we want the model to choose the best output out of the 4 models and secondly we want the model to learn which errors each model makes and correct these errors.
By combining our models, we intend to create a voting system. Each model would output zero or more predictions, where zero would be the case where the classifier does not find a string in the invoice which matches our categories. The predictions are compiled and used as inputs into a neural netEwork. This neural network would then be able to identify if a classifier makes systematic errors, producing an improved overall result by weighting each prediction appropriately. A sci-fi model we still have not figured out how to build would be able to take different "imperfect" predictions, separate signsal from noise and produce the correct prediction.

## 4. Data generation when "real" data is not available
One of the challenges in this project was to improve on the training data.

The original Baseline produces invoices (and training targets) on the fly. We are proposing a pipeline where all data is on disk for different collaborators to load it from.

We wrote a notebook that generates invoices with corresponding targets and truth strings. The notebook fills a subdir with csv files and creates a zipfile for distribution.
The original generator was limited to two templates. We added 19 more templates based on real life examples. Personal details were altered and the parts of interest were changed into placeholders for the algorithm.

The main challenge in our pipeline is to make sure all collaborating parties work on the same collection of invoices and know how to identify each invoice. That is why we added a globally unique identifier to every invoice.

For the benefit of the stacker model, we store the "truth strings" of the invoice with the invoice in the same file. To accomplish that, we had to change the generation algorithm to return those strings in an array.

For a further explanation, read the invoices_generate_todisk.ipynb.
The notebook invoices_from_disk_demo.ipynb gives a demonstration on how to use the saved data.

## 5. Expansion of the project

Two weeks were not enough to implement all the ideas we think are valuable in solving the problem at hand.
In this section the goal is to outline the possibilities that didn't end up in our submission but which could make for a useful addition.

### 5.1 KvK API
The KvK API provides data about companies. It can be called providing name and/or KvK nummer and returns a JSON with the information about the company.
The API is paid for commercial use.

since the KvK number has a fixed structure and we are convinced a model could become quite good at recognizing it, it could become the unique Key. In the end, difficult-to-predict fields such as company name or address could be obtained via KvK database instead of a neural network.
Since the KvK number itself is an uncertain result in out approach, exceptions should be raised if no result is obtained via this method.

### 5.2 Caching of past results
A company has a stable set of suppliers from which it receives invoices. Once a field such as company name has been predicted correctly once it gets inserted in a database, with all other known attrivutes of the supplier. When the model outputs a set of results it can try to match them to the database of known companies (no need for exact match, something like fuzzy search) and retrieve results from there.
In this way the probabilistic and error-prone results of our models lead to certain results stored in the database. 

With time the database would become more and more complete, leading to more matches and less guesses

### 5.3 IBAN check via schwifty
IBAN codes can be validated via an algorythm as shown [here](https://en.wikipedia.org/wiki/International_Bank_Account_Number#Algorithms).
there is a nice python library that does automatic checks on IBANs. Documentation can be found [here](https://pypi.python.org/pypi/schwifty/1.0.0).

The idea is to write a function that checks IBANs and insert it in the pipeline. If an IBAN passes the test it can be flagged as a high-probability prediction. With time the check could become a confirmation of a perfect match.

## 6. Reflection

As a group we ran into numerous challenges when trying to tackle the problem of accurately identifying invoices. An initial problem that we had was that we were running models based on alterations of those few templates, which meant that our model would highly overfit, and not necessarily be applicable to other files. In real life for example, IBAN numbers can be grouped by four, or they can be written as one long string of 22 characters. Our group attempted to work around this limitation, by adding 19 extra invoices that one group member could provide. Now our group was able to generate invoices, which are more than 1000% more diverse than the initial two templates, which is highly effective in combatting overfitting. Most problems that we faced were technical in nature. By creating thousands of new invoices, we saved them to a disk. Importing and training on this data, proved to be a technical challenge, which cost time. We expect that the combined stacking model could be effective, had there been a bit more time to work out the technical kinks of building such a model. Dividing up work and working remotely is also not highly effective, and we imagine that an internal team at a company such as Ortec would have less of these communication problems, meaning all ideas are aligned quicker.
