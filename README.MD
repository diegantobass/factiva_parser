# Factiva Parser

## What it does
This small python script converts a collection of files exported from the famous paid-access press database, Factiva

## What file from Factiva are
These files are typically exported by hand from a query on the [Factiva website](https://www.dowjones.com/products/factiva/). Each file contains a batch of a hundred articles. Each article preceded by a small header whose format can slightly vary depending on the source, and followed by a cryptic identifier.

## What this script does
This parser uses regular expressions to parse such files containing articles into a csv file containing, for each article :

- identifier
- title
- number of words
- date
- newspaper/website where the article was published
- some cryptic code for the newspapier/website
- the full text of the article

## Nota bene
Please note that files must be converted from their original Rich Text Format _.rtf_ format before this script can parse them. They should be encoded in UTF-8.

You might use a simple bash script in the directory of _.rtf_ files to convert them. The following example uses the macintosh-only bash utility _textutil_

~~~bash 
find ./ -name '*.rtf' -print0 | xargs -0 textutil -inputencoding UTF-8 -convert txt
~~~

Or some other combination of bash tools, like unrtf (untested)

~~~bash
for FILE in $(ls|grep *.rtf); do unrtf --text $FILE; done
~~~

## What this script doesn't do
- An article whose header does not contain a title won't be parsed.
- An article for which the full text isn't avalaible won't be parsed.
- Some other weird header formats might be badly parsed or not parsed at all, or the beasts from the underworld might be unleashed to enslave us all because regexes are actually reg-hexes.