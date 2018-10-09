#!/bin/bash

pdftk $1 output uncompressed.pdf uncompress
LANG=C LC_CTYPE=C sed -n '/^\/Annots/!p' uncompressed.pdf > stripped.pdf
pdftk stripped.pdf output $1 compress
rm uncompressed.pdf stripped.pdf

