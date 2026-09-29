

BASES = "TCAG"
AMINO_ACIDS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

CODON_TABLE = {}
index = 0
for first in BASES:
    for second in BASES:
        for third in BASES:
            CODON_TABLE[first + second + third] = AMINO_ACIDS[index]
            index += 1

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def validate(seq):
    seq = "".join(seq.split()).upper()
    if seq == "":
        raise ValueError("Sequence is empty.")
    for base in seq:
        if base not in "ATGC":
            raise ValueError(f"Invalid base '{base}'. Only A, T, G, C are allowed.")
    return seq


def load_from_file(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(">"):
                lines.append(line)
    return "".join(lines)


def base_count(seq):
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in seq:
        counts[base] += 1
    return counts


def base_percentage(seq):
    counts = base_count(seq)
    percentages = {}
    for base in counts:
        percentages[base] = round(counts[base] / len(seq) * 100, 2)
    return percentages


def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return round(gc / len(seq) * 100, 2)


def reverse_complement(seq):
    result = ""
    for base in reversed(seq):
        result += COMPLEMENT[base]
    return result


def transcribe(seq):
    """DNA -> RNA (T becomes U)."""
    return seq.replace("T", "U")


def translate(seq):
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        amino_acid = CODON_TABLE[codon]
        if amino_acid == "*":
            break
        protein += amino_acid
    return protein


def find_motif(seq, motif):
    positions = []
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i + len(motif)] == motif:
            positions.append(i + 1)
    return positions

def build_report(seq):
    counts = base_count(seq)
    perc = base_percentage(seq)
    lines = []
    lines.append("=" * 50)
    lines.append("        DNA SEQUENCE ANALYSIS REPORT")
    lines.append("=" * 50)
    lines.append(f"Sequence        : {seq}")
    lines.append(f"Length          : {len(seq)} bases")
    lines.append("")
    lines.append("Base composition:")
    for base in counts:
        lines.append(f"  {base} : {counts[base]:>4}  ({perc[base]}%)")
    lines.append("")
    lines.append(f"GC content      : {gc_content(seq)}%")
    lines.append(f"Reverse compl.  : {reverse_complement(seq)}")
    lines.append(f"RNA             : {transcribe(seq)}")
    lines.append(f"Protein         : {translate(seq) or '(none)'}")
    lines.append("=" * 50)
    return "\n".join(lines)


def save_report(seq, filename="report.txt"):
    with open(filename, "w") as f:
        f.write(build_report(seq))


def show_menu():
    print("\n===== DNA SEQUENCE ANALYZER =====")
    print("1. Enter sequence (type)")
    print("2. Load sequence from file")
    print("3. Base count and percentage")
    print("4. GC content")
    print("5. Reverse complement")
    print("6. Transcription (DNA -> RNA)")
    print("7. Translation (DNA -> Protein)")
    print("8. Motif search")
    print("9. Save report to file")
    print("0. Exit")


def main():
    seq = None

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using DNA Sequence Analyzer!")
            break

        elif choice == "1":
            try:
                seq = validate(input("Enter DNA sequence: "))
                print(f"Sequence saved ({len(seq)} bases).")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            filename = input("Enter file name (e.g. sample.txt): ").strip()
            try:
                seq = validate(load_from_file(filename))
                print(f"Sequence loaded from file ({len(seq)} bases).")
            except FileNotFoundError:
                print("Error: file not found.")
            except ValueError as e:
                print("Error:", e)

        elif choice in ("3", "4", "5", "6", "7", "8", "9"):
            if seq is None:
                print("Please enter or load a sequence first (option 1 or 2).")
                continue

            if choice == "3":
                counts = base_count(seq)
                perc = base_percentage(seq)
                for base in counts:
                    print(f"{base}: {counts[base]} ({perc[base]}%)")

            elif choice == "4":
                print("GC content:", gc_content(seq), "%")

            elif choice == "5":
                print("Reverse complement:", reverse_complement(seq))

            elif choice == "6":
                print("RNA:", transcribe(seq))

            elif choice == "7":
                protein = translate(seq)
                print("Protein:", protein if protein else "(no protein produced)")

            elif choice == "8":
                motif = input("Enter motif to search (e.g. ATG): ").strip().upper()
                if motif == "" or any(b not in "ATGC" for b in motif):
                    print("Error: motif must contain only A, T, G, C.")
                else:
                    positions = find_motif(seq, motif)
                    if positions:
                        print(f"'{motif}' found {len(positions)} time(s) at positions: {positions}")
                    else:
                        print(f"'{motif}' not found.")

            elif choice == "9":
                save_report(seq)
                print("Report saved to report.txt")

        else:
            print("Invalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
    main()
