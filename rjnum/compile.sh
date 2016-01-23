#!/bin/bash

FILES="abstract.md intro.md problem.md solution.md results.md biblio.md"

pandoc -S --filter pandoc-crossref --bibliography paper.bib --csl=gost.csl -o ${1}.docx ${FILES} -V lang:russian
