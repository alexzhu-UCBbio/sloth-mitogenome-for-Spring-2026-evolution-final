from pathlib import Path
import re

NEXUS = Path("model_partition/Delsuc-CurrBiol-2019_dataset_partitions.nex")
OUT = Path("model_partition/Delsuc-CurrBiol-2019_iqtree_42partitions.partitions")

PROTEIN_CODING_GENES = [
    "ATP6",
    "ATP8",
    "COX1",
    "COX2",
    "COX3",
    "CYTB",
    "ND1",
    "ND2",
    "ND3",
    "ND4L",
    "ND4",
    "ND5",
    "ND6",
]

RRNA_GENES = ["12S", "16S"]


def parse_charsets(nexus_path):
    pattern = re.compile(
        r"charset\s+ancient40mitos_(?P<name>.+?)_mafft_gb\s*=\s*"
        r"(?P<start>\d+)\s*-\s*(?P<end>\d+)\s*;",
        re.IGNORECASE,
    )

    charsets = {}
    for line in nexus_path.read_text().splitlines():
        match = pattern.search(line)
        if match:
            name = match.group("name")
            start = int(match.group("start"))
            end = int(match.group("end"))
            charsets[name] = (start, end)

    return charsets


def sites_from_spec(start, end, offset=0, step=1):
    return set(range(start + offset, end + 1, step))


def main():
    charsets = parse_charsets(NEXUS)

    partitions = []
    covered_sites = set()

    # Original initial scheme: 12S rRNA and 16S rRNA are separate partitions.
    for gene in RRNA_GENES:
        start, end = charsets[gene]
        spec = f"{start}-{end}"
        partitions.append((gene, spec))
        covered_sites.update(sites_from_spec(start, end))

    # Original initial scheme: 13 protein-coding genes split by codon position.
    for gene in PROTEIN_CODING_GENES:
        start, end = charsets[gene]
        length = end - start + 1

        if length % 3 != 0:
            raise ValueError(f"{gene} length is not divisible by 3: {start}-{end}")

        for codon_pos in [1, 2, 3]:
            offset = codon_pos - 1
            name = f"{gene}_p{codon_pos}"
            spec = f"{start + offset}-{end}\\3"
            partitions.append((name, spec))
            covered_sites.update(sites_from_spec(start, end, offset=offset, step=3))

    # Original initial scheme: all tRNAs are combined into one partition.
    trna_specs = []
    for gene, (start, end) in sorted(charsets.items(), key=lambda item: item[1][0]):
        if gene.startswith("tRNA-"):
            trna_specs.append(f"{start}-{end}")
            covered_sites.update(sites_from_spec(start, end))

    partitions.append(("tRNAs", ", ".join(trna_specs)))

    expected_sites = set(range(1, 15157 + 1))

    if len(partitions) != 42:
        raise ValueError(f"Expected 42 partitions, got {len(partitions)}")

    if covered_sites != expected_sites:
        missing = sorted(expected_sites - covered_sites)
        extra = sorted(covered_sites - expected_sites)
        raise ValueError(
            f"Site coverage failed. Missing={len(missing)}, extra={len(extra)}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with OUT.open("w") as f:
        for name, spec in partitions:
            f.write(f"DNA, {name} = {spec}\n")

    print(f"Wrote: {OUT}")
    print(f"Partitions: {len(partitions)}")
    print(f"Covered sites: {len(covered_sites)}")


if __name__ == "__main__":
    main()
