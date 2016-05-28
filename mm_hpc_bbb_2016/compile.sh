#!/bin/bash

FILES="abstract.md"

pandoc -S --filter pandoc-crossref --csl=gost.csl -o ${1}.docx ${FILES} -V lang:russian
