# Project Statement - DNA Sequence Analyzer

## Problem statement

DNA sequences show up a lot in biology and bioinformatics classes, but doing things like finding the GC content or translating a sequence into a protein by hand is slow and easy to get wrong. I wanted to build a small tool that does these basic DNA analysis steps automatically, using core Python concepts like dictionaries, loops and string handling, without relying on a bioinformatics library like Biopython.

## Scope

This is a terminal program that works on one DNA sequence at a time. You can type a sequence in directly or load it from a file. Once a sequence is loaded, you can run different kinds of analysis on it through a menu, and save a report to a text file.

It doesn't handle multiple sequences at once, doesn't have a GUI, and doesn't support RNA or protein sequences as input, only DNA.

## Target users

- My course faculty checking the project
- Students learning basic bioinformatics or Python who want to see base counting, transcription and translation done with plain code
- Anyone who wants a quick way to check GC content or translate a short DNA sequence without installing a bioinformatics library

## Main features

- Enter a sequence by typing or by loading a FASTA-style file
- Checks the sequence only contains A, T, G, C
- Base count and percentage
- GC content
- Reverse complement
- Transcription (DNA to RNA)
- Translation (DNA to protein) using a codon table
- Motif search with position numbers
- Save a full report to a text file
