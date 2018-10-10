#!/bin/bash

function remove_annotation {
    echo "Removing annotations from $1"
    pdftk $1 output $1.uncompressed uncompress
    LANG=C LC_CTYPE=C sed -n '/^\/Annots/!p' $1.uncompressed > $1.stripped
    pdftk $1.stripped output $1 compress
    rm $1.uncompressed $1.stripped
}

input=$1

if [[ -d $input ]]; then
    # from https://stackoverflow.com/questions/6481005/how-to-obtain-the-number-of-cpus-cores-in-linux-from-the-command-line
    cpu_count=`getconf _NPROCESSORS_ONLN`
    ls $input/*.pdf | parallel -j ${cpu_count} "./remove-pdf-annotations.sh {}"
#    for pdf in $input/*.pdf
#    do
#        remove_annotation $pdf
#    done
elif [[ -f $input && ${input: -4} == ".pdf" ]]; then
    remove_annotation $input
else
    echo "Please provide a directory containing pdfs or a pdf"
    exit 1
fi



