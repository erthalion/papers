#!/bin/bash

pandoc --filter pandoc-crossref --bibliography report.bib -M "eqnPrefix: " -o ${1}.docx *.md -V lang:russian
