# MLiFC_invoice_classifier
Some focus in code for our study group_x in Bletchley Bootcamp...

Contains the baseline notebook by Jannes Klaas @ Bletchley Bootcamp / Turing Society Rotterdam.
https://drive.google.com/file/d/1wjtiXpxRkuN5V57GiK_RSPxy84cFbERO/view?usp=sharing

## Aim of the project and approach
Aim: to provide a proof of concept (working prototype) that is capable of extracting five specific strings from invoices.

Approach: Working from the baseline provided by Jannes, we improve some of the details. Also we attempt to enrich the generated example invoices. The heart of the project will be a stacker algo that can take up to four different (intermediate) results from one to four different exctractor models.

## Random details
* model "regex_iban" is a traditional algorithm based on regular expressions. 
* model "X1" is an improved version of Jannes' baseline model.
* all extractor models need to take input and produce outputs that are consistent in format and content.
  * This proves to be a challenge in itself. Jannes' notebook produces examples on the fly. We must find a way and a format to store the generated examples on disk and a way to share the uniquely identified invoices among team members. Each individual invoice must be accompanied by its "truth values" for training/testing.
* the stacker algo takes in 1 or more sets of strings (identified by the invoice's uuid) and spits out a corrected set of similar strings. It aims to select the strongest inputs or strongest parts of strings and recombine these into better strings.
 * for instance: two models predict the KvK number to be: 12345678 and I2345678 repectively. The first is correct and the stacker should learn to select that one as its output. In order to train the stacker, it needs the truth for the KvK number as a target.
 * different example: two models predict the IBAN to be: NL12 AB#D 3456 7890 12 and NL12 #BCD 3456 7890 12 respectively. Both are mutated by noise, but the correct IBAN can be extracted by a model that learns to separate the signal from the noise. Call it error correction, if you like....

## Data formats
Generated invoice examples look like the character based output from an OCR algorithm.
```
f-torec%
Aan:

ING Bank N.V.
Bijlmerplein 888
1102MG 1102MG

ORTEC Finance B.V.
Boompjes 40
KvK nr:

3011XB Rotterdam

BTW nr:

Bank:
BAN:
BIC:
Tel:
E-mail:
Website:

Factuur

33031431
000019531656
ING NETHERLANDS
NL12INGB0758162765
INGBNL2A
06-90366060
info@ing.nl
https://www.ing.nl

Factuurnummer

Factuurdatum

Uw referentie

XEIQQ9ATAL

9/11/2015

MOU26

DATUM

AANTAL

PRIJS

BTW

SUBTOTAAL

OMSCHRIJVING

Sony XB950B1 Extra Bass Wireless Headphones

4.00

€ 5.75

€ 2.76

€ 23.01


23andMe DNA Test

4.00

€ 557.85

€ 267.77

€ 2231.40


 Instant Pot 7-in-1 Multi-Functional Pressure Cooker

9.00

€ 328.17

€ 354.42

€ 2953.49


Anker Super Bright Tactical Flashlight, Rechargeable

9.00

€ 8.80

€ 9.51

€ 79.24

TOTAAL EXCL. BTW

€ 5287.14
BTW%

OVER

BEDRAG

-

-


TOTAAL BTW

€ 634.46
TE BETALEN

€ 5921.60

Opmerkingen & Voorwaarden
<CONDITIONS>
```
The accompanying truth is generated to be:
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
where each number represents a character in the invoice and is interpreted to mean:
```
0: Ignore
1: Sender Name
2: Sender KVK
3: Sender IBAN
4: Invoice Reference
5: Total
```
# Stacker Algorithm
But what we are really interested in are human readable strings like these:
```
Invoice UUID                         | Sender Name           | Sender KvK    | Sender IBAN             | ref.    | Total
56584c6e-6cd7-49d4-8d7e-1830030fa225 | ING Bank N.V.         | 33031431      | NL12INGB0758162765      | MOU26   | 5921.60
```
Assume our extractor models create strings like above. Strings that are in need of some cleaning up, electing, correcting maybe.
model X1 predicts:
```
56584c6e-6cd7-49d4-8d7e-1830030fa225 | n:ING Bank N.V.B      | r33031431000   | SNL12INGB0758162765I   |  <None>  | € 5921.60
```
while model X2 predicts for the same invoice:
```
56584c6e-6cd7-49d4-8d7e-1830030fa225 | n:ING Bank            | 3303 1431      | NL12 INGB 0758 1627 65 |  <None>  | X 5921,60
```
The stacker algorithm needs to learn to choose which parts of which inputs "to trust" and copy to its output. For some fields it might even learn how to correct the string so that it complies to the expected format (IBAN?). And the stacker also needs to learn to ignore the strings that the models could not predict at all.

## uniformity of inputs and outputs and targets
This is the proposed format for each extractable field:
```
Invoice UUID      : 36 chars (as generated by python module uuid, method .uuid4(): random string)
Sender Name       : 32 chars
Sender KVK        : 16 chars
Sender IBAN       : 32 chars
Invoice Reference : 16 chars
Total             : 16 chars
```
All these are oversized to fit extraneous characters surrounding the string to extract. The idea is that the stacker algo sees some usable info in those. UUID is not a learnable input, so it is not oversized. It is up to the extractor models to "decide" wether to include extra chars or not.
