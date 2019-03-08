# Factiva Parser

## What it does
This small python script converts a collection of files exported from the famous paid-access press database, Factiva

## What file from Factiva are
These files are typically exported by hand from a query on the [Factiva website](https://www.dowjones.com/products/factiva/). Each file contains a batch of a hundred articles. Each article preceded by a small header whose format can slightly vary depending on the source, and followed by a cryptic identifier.

## What this script does
This parser uses regular expression to parse such a collection of files containing articles into a csv file containing, for each article :

- identifier
- title
- number of words
- date
- journal where the article was published
- some cryptic code
- the full text of the article

## Nota bene
Please note that files must be converted from their original Rich Text Format _.rtf_ format before this script can convert them. They should be encoded in UTF-8.

## What this script doesn't do
- Articles whose header does not contain a title won't be parsed.
- Articles where full text isn't avalaible won't be parsed.
- Some other weird header format might be badly parsed or not at all, or the beasts from the underworld might be unleashed to enslave us all.