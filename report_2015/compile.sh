#!/bin/bash

pandoc --bibliography report.bib -o ${1}.pdf *.md -V lang:russian
