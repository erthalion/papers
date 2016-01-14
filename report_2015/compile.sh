#!/bin/bash

FILES="experimental_facility.md math.md computation.md results.md conclusions.md biblio.md"

pandoc --filter pandoc-crossref --bibliography report.bib -o ${1}.docx ${FILES} -V lang:russian
