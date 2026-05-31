from pathlib import Path
from collections import Counter

FASTA = Path("input_dataset/Delsuc-CurrBiol-2019_dataset.fasta")
PHYLIP = Path("input_dataset/Delsuc-CurrBiol-2019_dataset.phylip")
NEXUS = Path("model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex")

OUT_QC = Path("results/qc")

OUT_QC.mkdir(exist_ok=True, parents=True)


def read_fasta(path):
    records = []
    name = None
    seq_parts = []

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith(">"):
            if name is not None:
                records.append((name, "".join(seq_parts).upper()))
            name = line[1:].strip()
            seq_parts = []
        else:
            seq_parts.append(line)

    if name is not None:
        records.append((name, "".join(seq_parts).upper()))

    return records


def read_phylip_names(path):
    names = []
    with path.open() as f:
        header = f.readline().split()
        for line in f:
            line = line.strip()
            if line:
                names.append(line.split()[0])
    return header, names


def read_nexus_matrix_names(path):
    names = []
    in_matrix = False

    for line in path.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("["):
            continue

        if s.lower() == "matrix":
            in_matrix = True
            continue

        if in_matrix and s == ";":
            break

        if in_matrix:
            names.append(s.split()[0])

    return names


def main():
    records = read_fasta(FASTA)
    fasta_names = [name for name, _ in records]
    fasta_set = set(fasta_names)

    phylip_header, phylip_names = read_phylip_names(PHYLIP)
    phylip_set = set(phylip_names)

    nexus_names = read_nexus_matrix_names(NEXUS)
    nexus_set = set(nexus_names)

    lengths = Counter(len(seq) for _, seq in records)

    valid_bases = set("ACGT")
    ambiguous_codes = set("RYSWKMBDHV")

    with (OUT_QC / "alignment_summary.tsv").open("w") as out:
        out.write(
            "taxon\tlength\tgap_count\tN_count\tmissing_count\t"
            "ambiguous_count\tother_count\tgap_fraction\tN_fraction\t"
            "missing_fraction\tambiguous_fraction\tother_fraction\n"
        )

        for name, seq in records:
            length = len(seq)
            gap_count = seq.count("-")
            n_count = seq.count("N")
            missing_count = seq.count("?")
            ambiguous_count = sum(1 for c in seq if c in ambiguous_codes)
            other_count = sum(
                1 for c in seq
                if c not in valid_bases
                and c not in ambiguous_codes
                and c not in {"-", "N", "?"}
            )

            out.write(
                f"{name}\t{length}\t{gap_count}\t{n_count}\t{missing_count}\t"
                f"{ambiguous_count}\t{other_count}\t"
                f"{gap_count / length:.6f}\t"
                f"{n_count / length:.6f}\t"
                f"{missing_count / length:.6f}\t"
                f"{ambiguous_count / length:.6f}\t"
                f"{other_count / length:.6f}\n"
            )

    with (OUT_QC / "dataset_qc_summary.tsv").open("w") as out:
        out.write("metric\tvalue\n")
        out.write(f"fasta_sequence_count\t{len(records)}\n")
        out.write(f"fasta_unique_taxon_labels\t{len(fasta_set)}\n")
        out.write(f"fasta_length_values\t{dict(sorted(lengths.items()))}\n")
        out.write(f"phylip_header_ntax\t{phylip_header[0] if len(phylip_header) > 0 else 'NA'}\n")
        out.write(f"phylip_header_nchar\t{phylip_header[1] if len(phylip_header) > 1 else 'NA'}\n")
        out.write(f"phylip_unique_taxon_labels\t{len(phylip_set)}\n")
        out.write(f"nexus_unique_taxon_labels\t{len(nexus_set)}\n")
        out.write(f"fasta_vs_phylip_same_taxa\t{fasta_set == phylip_set}\n")
        out.write(f"fasta_vs_nexus_same_taxa\t{fasta_set == nexus_set}\n")

    print("QC finished.")
    print("Wrote:")
    print("  results/qc/alignment_summary.tsv")
    print("  results/qc/dataset_qc_summary.tsv")


if __name__ == "__main__":
    main()
