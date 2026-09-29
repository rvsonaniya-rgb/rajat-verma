# DNA Sequence Analyzer

A small menu-driven Python program that does basic analysis on DNA sequences. I made it as my project for the VITyarthi Python course.

**Author:** Rajat Verma (Integrated M.Tech, AI and Bioinformatics, VIT Bhopal)

---

## What it does

You can give it a DNA sequence, either by typing it in or by loading a `.txt` or FASTA file. Then it can:

- Check that the sequence is valid (only A, T, G and C are allowed). Spaces and newlines are removed and lowercase letters are converted to uppercase, so you don't have to clean the input first.
- Count each base and show its percentage
- Calculate the GC content
- Give the reverse complement
- Transcribe DNA to RNA (T becomes U)
- Translate the sequence into a protein using the standard genetic code
- Search for a motif and show every position where it appears (positions start from 1)
- Save everything into a `report.txt` file

---

## Requirements

Python 3.6 or newer, because I used f-strings. There are no external libraries, only built-in Python.

---

## How to run

```bash
python dna_analyzer.py
```

This menu will show up:

```
===== DNA SEQUENCE ANALYZER =====
1. Enter sequence (type)
2. Load sequence from file
3. Base count and percentage
4. GC content
5. Reverse complement
6. Transcription (DNA -> RNA)
7. Translation (DNA -> Protein)
8. Motif search
9. Save report to file
0. Exit
```

Start with option 1 or 2 to load a sequence. Options 3 to 9 all work on whatever sequence you loaded.

---

## Input file format

Any plain text file or FASTA file works. Lines starting with `>` (the FASTA header) are skipped, and all the other lines are joined into a single sequence. For example:

```
>sample_sequence
ATGGCCATTGTAATGGG
CCGCTGA
```

---

## Example

I tested it with the sequence `ATGGCCATTGTAATGGGCCGCTGA`:

| Analysis           | Result                                  |
|--------------------|-----------------------------------------|
| Length             | 24 bases                                |
| A / T / G / C      | 5 / 6 / 8 / 5                           |
| GC content         | 54.17%                                  |
| Reverse complement | `TCAGCGGCCCATTACAATGGCCAT`              |
| RNA                | `AUGGCCAUUGUAAUGGGCCGCUGA`              |
| Protein            | `MAIVMGR`                               |
| Motif `ATG`        | found 2 times, at positions `[1, 13]`   |

---

## Sample report

This is what `report.txt` looks like for the same sequence:

```
==================================================
        DNA SEQUENCE ANALYSIS REPORT
==================================================
Sequence        : ATGGCCATTGTAATGGGCCGCTGA
Length          : 24 bases

Base composition:
  A :    5  (20.83%)
  T :    6  (25.0%)
  G :    8  (33.33%)
  C :    5  (20.83%)

GC content      : 54.17%
Reverse compl.  : TCAGCGGCCCATTACAATGGCCAT
RNA             : AUGGCCAUUGUAAUGGGCCGCUGA
Protein         : MAIVMGR
==================================================
```

---

## How it works

**Codon table:** Instead of typing out all 64 codons by hand, I generate them with nested loops. The loops use `BASES = "TCAG"` and a 64-letter string of amino acids, where `*` means a STOP codon.

**Translation:** It starts at the first base, reads the sequence three letters at a time, and stops when it hits the first STOP codon.

**Motif search:** It slides a window across the sequence and notes every match. Overlapping matches are counted too.

---

## Files

```
dna_analyzer.py   # the whole program, in one file
README.md         # this file
report.txt        # created when you choose option 9
```

---

## Limitations

- Only A, T, G and C are accepted. Ambiguous bases like `N` are rejected.
- Translation always begins at the first base. It doesn't look for an `ATG` start codon or try other reading frames.
- Only the standard genetic code is supported.
- The report is always saved as `report.txt` in the current folder, and it overwrites any existing file with that name.

---

## Ideas for later

- Translate all 6 reading frames and find ORFs
- Support IUPAC ambiguity codes
- Add molecular weight and melting temperature
- Let the user choose the report file name
