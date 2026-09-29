# DNA Sequence Analyzer

A menu-driven Python program for basic DNA sequence analysis. Built as a **VITyarthi Python Project**.

**Author:** Rajat Verma (Integrated M.Tech, AI and Bioinformatics, VIT Bhopal)

---

## Features

1. **Enter a sequence** by typing it, or **load it from a `.txt` / FASTA file**
2. **Validation**: only `A`, `T`, `G`, `C` are accepted (spaces/newlines are removed and lowercase is converted automatically)
3. **Base count and percentage** for A, T, G, C
4. **GC content** (in %)
5. **Reverse complement** of the strand
6. **Transcription**: DNA → RNA (T becomes U)
7. **Translation**: RNA → Protein using the standard genetic code
8. **Motif search**: finds all 1-based start positions of a motif
9. **Save a full report** to `report.txt`

---

## Requirements

- Python 3.6 or above (uses f-strings)
- No external libraries needed. Only built-in Python is used.

---

## How to Run

```bash
python dna_analyzer.py
```

You will see this menu:

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

First choose option **1** or **2** to load a sequence. After that, options 3 to 9 work on that sequence.

---

## Input File Format

A plain text file or a FASTA file. Lines starting with `>` (FASTA headers) are skipped, and the remaining lines are joined into one sequence.

```
>sample_sequence
ATGGCCATTGTAATGGG
CCGCTGA
```

---

## Example

**Input sequence:** `ATGGCCATTGTAATGGGCCGCTGA`

| Analysis           | Result                     |
|--------------------|----------------------------|
| Length             | 24 bases                   |
| A / T / G / C      | 5 / 6 / 8 / 5              |
| GC content         | 54.17%                     |
| Reverse complement | `TCAGCGGCCCATTACAATGGCCAT` |
| RNA                | `AUGGCCAUUGUAAUGGGCCGCUGA` |
| Protein            | `MAIVMGR`                  |
| Motif `ATG`        | found 2 time(s) at positions `[1, 13]` |

---

## Sample Report (`report.txt`)

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

## How It Works

- **Codon table:** all 64 codons are generated with nested loops from `BASES = "TCAG"` and a 64-letter amino acid string (`*` = STOP codon).
- **Translation:** starts from the first base, reads in triplets, and stops at the first STOP codon.
- **Motif search:** slides a window over the sequence and records every match (overlapping matches are included).

---

## Project Structure

```
dna_analyzer.py   # main program (all code in one file)
README.md         # this file
report.txt        # created when you choose option 9
```

---

## Limitations

- Only `A`, `T`, `G`, `C` are supported (ambiguous bases like `N` are rejected).
- Translation always starts from the first base (no search for the `ATG` start codon and no other reading frames).
- Only the standard genetic code is used.
- The report is always saved as `report.txt` in the current folder (an existing file is overwritten).

---

## Possible Future Improvements

- Translate all 6 reading frames and find ORFs
- Support for IUPAC ambiguity codes
- Molecular weight and melting temperature calculation
- Custom output file name for the report
