#!/bin/bash

# this deletes all the following extensions from current and sub-dir
# to run the script, $ ./clean_up_tex.sh

# Check if the script is executable
if [[ ! -x "$0" ]]
then
    chmod +x "$0"
fi

# Delete all .pdf, .xml, .aux, .log, .bcf, .bbl, blg, run.xml, fls, synctex.gz, fdb_latexmk files

# find . -type f -name "*.pdf" -delete
find . -type f -name "*.xml" -delete
find . -type f -name "*.aux" -delete
find . -type f -name "*.log" -delete
find . -type f -name "*.bcf" -delete
find . -type f -name "*.bbl" -delete
find . -type f -name "*.blg" -delete
find . -type f -name "*.fls" -delete
find . -type f -name "*.fdb_latexmk" -delete
find . -type f -name "*.synctex.gz" -delete
find . -type f -name "*.run.xml" -delete
