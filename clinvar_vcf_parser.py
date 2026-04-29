#!/usr/bin/env python3

import csv

INPUT_GENES = "gene3.txt"
VCF_FILE = "clinvar.vcf"
OUTPUT_FILE = "clinvar_gene_disease.csv"

# -----------------------------
# Load gene list
# -----------------------------
with open(INPUT_GENES) as f:
    genes = set(line.strip() for line in f if line.strip())

print(f"Loaded {len(genes)} genes")

# Initialize dictionary
gene_disease = {g: set() for g in genes}


# -----------------------------
# Parse VCF
# -----------------------------
with open(VCF_FILE) as vcf:
    for line in vcf:
        if line.startswith("#"):
            continue

        parts = line.strip().split("\t")
        info = parts[7]

        # Parse INFO field into dictionary
        info_dict = {}
        for item in info.split(";"):
            if "=" in item:
                key, value = item.split("=", 1)
                info_dict[key] = value

        # -----------------------------
        # Extract gene
        # -----------------------------
        gene_info = info_dict.get("GENEINFO", "")
        if ":" not in gene_info:
            continue

        gene = gene_info.split(":")[0]

        if gene not in genes:
            continue

        # -----------------------------
        # Extract disease
        # -----------------------------
        disease_field = info_dict.get("CLNDN", "")

        if not disease_field:
            continue

        # Clean + split diseases
        disease_field = disease_field.replace("_", " ")

        for disease in disease_field.split("|"):
            disease = disease.strip()

            # Filter junk
            if disease.lower() in [
                "not provided",
                "not specified",
                "not specified, disease",
                "phenotype not specified"
            ]:
                continue

            gene_disease[gene].add(disease)


# -----------------------------
# Write output CSV
# -----------------------------
with open(OUTPUT_FILE, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["Gene", "Diseases"])

    for gene in sorted(genes):
        diseases = gene_disease[gene]

        if diseases:
            writer.writerow([gene, "; ".join(sorted(diseases))])
        else:
            writer.writerow([gene, "NA"])

print(f"\n✅ Done! Output written to {OUTPUT_FILE}")
