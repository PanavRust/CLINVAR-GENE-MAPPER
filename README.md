# 🧬 ClinVar Gene–Disease Mapper

## 📌 Overview
This project maps a list of genes to their associated diseases using the ClinVar VCF dataset.

ClinVar is a variant-centric database, meaning it stores information at the variant level. This pipeline reconstructs gene-level disease associations by parsing variant annotations from the ClinVar VCF file.

---
## 📂 Project Structure

clinvar-gene-mapper/

├── scripts/
│   └── clinvar_vcf_parser.py

├── data/
│   └── gene3.txt

├── output/
│   └── clinvar_gene_disease.csv

├── .gitignore

└── README.md
---

## 📥 Input
Gene list (`gene3.txt`) with one gene per line:

TP53  
BRCA1  
EGFR  
MTHFR  

---

## 📤 Output
CSV file (`clinvar_gene_disease.csv`):

TP53, Li-Fraumeni syndrome; Breast cancer  
BRCA1, Breast ovarian cancer syndrome  
MTHFR, Homocystinuria  
MTOR, NA  

---

## 🚀 Usage

### 1. Download ClinVar VCF
wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz  
gunzip clinvar.vcf.gz  

### 2. Run the Script
python3 scripts/clinvar_vcf_parser.py  

---

## 🧠 Key Concepts
- ClinVar is variant-based, not gene-based  
- Gene–disease mapping is reconstructed from variant annotations  
- Uses:
  - GENEINFO → Gene  
  - CLNDN → Disease  

---

## ⚠️ Limitations
- Some genes may return NA  
- Disease names may be broad  
- Not filtered by pathogenicity  

---

## 🔥 Future Improvements
- Filter pathogenic variants (CLNSIG)  
- Add variant counts  
- Convert to Nextflow pipeline  

---

## 👨‍💻 Author
Panav Rustagi
