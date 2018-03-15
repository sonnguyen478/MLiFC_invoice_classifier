# MLiFC_invoice_classifier
Some focus in code for our study group_x in Bletchley Bootcamp...

Contains the baseline notebook by Jannes Klaas @ Bletchley Bootcamp / Turing Society Rotterdam.
https://drive.google.com/file/d/1wjtiXpxRkuN5V57GiK_RSPxy84cFbERO/view?usp=sharing

## Aim of the project and approach
Aim: to provide a proof of concept (working prototype) that is capable of extracting five specific strings from invoices.

Approach: Working from the baseline provided by Jannes, we improve some of the details. Also we attempt to enrich the generated example invoices. The heart of the project will be a stacker model that can take up to four different (intermediate) results from one to four different exctractor models.

## Random details
* model "regex_iban" is a traditional algorithm based on regular expressions. 
* model "X1" is an improved version of Jannes' baseline model.
* all extractor models need to take input and produce outputs that are consistent in format and content.
  * This proves to be a challenge in itself. Jannes' notebook produces examples on the fly. We must find a way and a format to store the generated examples on disk and a way to share the uniquely identified invoices among team members. Each individual invoice must be accompanied by its "truth values" for training/testing.
