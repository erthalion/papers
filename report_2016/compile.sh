#!/bin/bash

FILES="application.md"

#pandoc --filter pandoc-crossref --bibliography report.bib -o ${1}.docx ${FILES} -V lang:russian
pandoc --filter pandoc-crossref -o ${1}.docx ${FILES} -V lang:russian
