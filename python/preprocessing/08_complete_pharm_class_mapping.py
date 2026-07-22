# ==========================================================
# PHARMAOPS AI
# Complete Pharm Class Mapping
# Part 1 - Configuration & Rule Engine Setup
# ==========================================================

from pathlib import Path
import pandas as pd

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "reference" / "Pharm_Class_Mapping.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "reference" / "Pharm_Class_Mapping.csv"
UNMAPPED_FILE = PROJECT_ROOT / "data" / "reference" / "Unmapped_Pharm_Classes.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 70)
print("PHARMAOPS AI - COMPLETE PHARM CLASS MAPPING")
print("=" * 70)

df = pd.read_csv(INPUT_FILE)

df["Category_ID"] = df["Category_ID"].fillna("").astype(str)
df["Category_Name"] = df["Category_Name"].fillna("").astype(str)

print(f"Loaded {len(df):,} Pharm Classes")

# ==========================================================
# CATEGORY MASTER
# ==========================================================

CATEGORY_MASTER = {

    "CAT001": "Antibiotics",
    "CAT002": "Antidiabetic",
    "CAT003": "Cardiovascular",
    "CAT004": "Pain & Inflammation",
    "CAT005": "Neurology & Psychiatry",
    "CAT006": "Allergy & Respiratory",
    "CAT007": "Gastrointestinal",
    "CAT008": "Dermatology",
    "CAT009": "Hormonal",
    "CAT010": "Vaccines & Biologics",
    "CAT011": "Ophthalmology",
    "CAT012": "Oncology",
    "CAT013": "Supplements",
    "CAT014": "Medical Devices / Misc",
    "CAT015": "Others"

}
MANUAL_MAPPING = {

    # =====================================================
    # BATCH 1
    # =====================================================

    "4-Hydroxyphenyl-Pyruvate Dioxygenase Inhibitor [EPC]": ("CAT014", "Medical Devices / Misc"),
    "APOC-III-directed RNA Interaction [EPC]": ("CAT003", "Cardiovascular"),
    "Acetyl Aldehyde Dehydrogenase Inhibitors [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Actinomycin [EPC]": ("CAT012", "Oncology"),
    "Actively Acquired Immunity [PE]": ("CAT010", "Vaccines & Biologics"),
    "Adenosine Receptor Agonist [EPC]": ("CAT003", "Cardiovascular"),
    "Adenosine Receptor Agonists [MoA]": ("CAT003", "Cardiovascular"),
    "Adenosine Triphosphate-Citrate Lyase Inhibitor [EPC]": ("CAT003", "Cardiovascular"),
    "Adrenergic Agonists [MoA]": ("CAT003", "Cardiovascular"),
    "Alkaline Phosphatase [CS]": ("CAT014", "Medical Devices / Misc"),
    "Alkaloid [EPC]": ("CAT012", "Oncology"),
    "Aluminum Complex [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Alveolar Surface Tension Reduction [PE]": ("CAT006", "Allergy & Respiratory"),
    "Aminoketone [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Aminolevulinate Synthase 1-directed RNA Interaction [EPC]": ("CAT012", "Oncology"),
    "Aminosalicylate [EPC]": ("CAT007", "Gastrointestinal"),
    "Ammonium Ion Binding Activity [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Amphetamine Anorectic [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Analogs/Derivatives [Chemical/Ingredient]": ("CAT014", "Medical Devices / Misc"),
    "Angiopoietin-like 3 Inhibitor [EPC]": ("CAT003", "Cardiovascular"),
    "Anti-IgE [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Anti-anginal [EPC]": ("CAT003", "Cardiovascular"),
    "Anti-coagulant [EPC]": ("CAT003", "Cardiovascular"),
    "Anti-epileptic Agent [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Antibodies": ("CAT010", "Vaccines & Biologics"),
    "Antibodies [CS]": ("CAT010", "Vaccines & Biologics"),
    "Antidote [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Antifibrinolytic Agent [EPC]": ("CAT003", "Cardiovascular"),
    "Antihypoglycemic Agent [EPC]": ("CAT002", "Antidiabetic"),
    "Antileishmanial [EPC]": ("CAT001", "Antibiotics"),
    # =====================================================
    # BATCH 2
    # =====================================================

    "Antiprotozoal [EPC]": ("CAT001", "Antibiotics"),
    "Antirheumatic Agent [EPC]": ("CAT004", "Pain & Inflammation"),
    "Antisense Oligonucleotide [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Appetite Suppression [PE]": ("CAT005", "Neurology & Psychiatry"),
    "Aryl Hydrocarbon Receptor Agonist [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Asparaginase [CS]": ("CAT012", "Oncology"),
    "Autonomic Ganglionic Blocker [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "BCL-2 Inhibitor [EPC]": ("CAT012", "Oncology"),
    "Barbiturate [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Benzothiazole [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Bismuth [CS]": ("CAT007", "Gastrointestinal"),
    "Bispecific gp100 Peptide-HLA-directed CD3 T Cell Engager [EPC]": ("CAT012", "Oncology"),
    "Bisphosphonate [EPC]": ("CAT009", "Hormonal"),
    "Blood Viscosity Reducer [EPC]": ("CAT003", "Cardiovascular"),
    "Boron Compounds [CS]": ("CAT014", "Medical Devices / Misc"),
    "Bradykinin B2 Receptor Antagonist [EPC]": ("CAT003", "Cardiovascular"),
    "CCR5 Co-receptor Antagonist [EPC]": ("CAT001", "Antibiotics"),
    "CD123 Interaction [EPC]": ("CAT012", "Oncology"),
    "CD25-directed Cytotoxin [EPC]": ("CAT012", "Oncology"),
    "Calculi Dissolution Agent [EPC]": ("CAT007", "Gastrointestinal"),
    "Cannabinoid [EPC]": ("CAT004", "Pain & Inflammation"),
    "Cannabinoids [CS]": ("CAT004", "Pain & Inflammation"),
    "Carbamoyl Phosphate Synthetase 1 Activator [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Carbonic Anhydrase Inhibitor [EPC]": ("CAT003", "Cardiovascular"),
    "Carboxypeptidase [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Catechol O-Methyltransferase Inhibitors [MoA]": ("CAT005", "Neurology & Psychiatry"),
    "Catecholamine Synthesis Inhibitor [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Catecholamine [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Catecholamines [CS]": ("CAT005", "Neurology & Psychiatry"),
    "Centrally-mediated Muscle Relaxation [PE]": ("CAT005", "Neurology & Psychiatry"),
    # =====================================================
    # BATCH 3
    # =====================================================

    "Chloride Channel Activation Potentiators [MoA]": ("CAT006", "Allergy & Respiratory"),
    "Chloride Channel Activator [EPC]": ("CAT006", "Allergy & Respiratory"),
    "Cholecystokinin Analog [EPC]": ("CAT007", "Gastrointestinal"),
    "Copper Absorption Inhibitor [EPC]": ("CAT007", "Gastrointestinal"),
    "Copper [CS]": ("CAT013", "Supplements"),
    "Cyclic Pyranopterin Monophosphate [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Cystine Depleting Agent [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Cystine Disulfide Reduction [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Cytolytic Agent [EPC]": ("CAT012", "Oncology"),
    "Cytoprotective Agent [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Decreased Cell Wall Integrity [PE]": ("CAT001", "Antibiotics"),
    "Decreased Cell Wall Synthesis & Repair [PE]": ("CAT001", "Antibiotics"),
    "Decreased Diuresis [PE]": ("CAT003", "Cardiovascular"),
    "Decreased GnRH Secretion [PE]": ("CAT009", "Hormonal"),
    "Decreased Mitosis [PE]": ("CAT012", "Oncology"),
    "Decreased RNA Integrity [PE]": ("CAT012", "Oncology"),
    "Decreased Renal K+ Excretion [PE]": ("CAT003", "Cardiovascular"),
    "Decreased Sebaceous Gland Activity [PE]": ("CAT008", "Dermatology"),
    "Decreased Striated Muscle Contraction [PE]": ("CAT005", "Neurology & Psychiatry"),
    "Decreased Tracheobronchial Stretch Receptor Activity [PE]": ("CAT006", "Allergy & Respiratory"),
    "Depigmenting Activity [PE]": ("CAT008", "Dermatology"),
    "Dihydroorotate Dehydrogenase Inhibitors [MoA]": ("CAT012", "Oncology"),
    "Dipeptidyl Peptidase 4 Inhibitor [EPC]": ("CAT002", "Antidiabetic"),
    "Disclosing Agent [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Ectoparasiticide [EPC]": ("CAT001", "Antibiotics"),
    "Endoglycosidase [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Endothelin Receptor Antagonist [EPC]": ("CAT003", "Cardiovascular"),
    "Epoxide Hydrolase Inhibitors [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Ergolines [CS]": ("CAT005", "Neurology & Psychiatry"),
    "Ergotamine Derivative [EPC]": ("CAT005", "Neurology & Psychiatry"),
    # =====================================================
    # BATCH 4
    # =====================================================

    "Erythroid Maturation Agent [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Erythropoiesis-stimulating Agent [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Estradiol Congeners [CS]": ("CAT009", "Hormonal"),
    "Fibric Acids [CS]": ("CAT003", "Cardiovascular"),
    "Folate Analog Metabolic Inhibitor [EPC]": ("CAT012", "Oncology"),
    "Folate Analog [EPC]": ("CAT012", "Oncology"),
    "Fusion Protein Inhibitors [MoA]": ("CAT010", "Vaccines & Biologics"),
    "G-Protein-linked Receptor Interactions [MoA]": ("CAT014", "Medical Devices / Misc"),
    "General Anesthesia [PE]": ("CAT005", "Neurology & Psychiatry"),
    "Glinide [EPC]": ("CAT002", "Antidiabetic"),
    "Glucosylceramidase [CS]": ("CAT014", "Medical Devices / Misc"),
    "Glucosylceramide Synthase Inhibitor [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Glycosaminoglycan [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Guanylate Cyclase Activators [MoA]": ("CAT003", "Cardiovascular"),
    "Guanylate Cyclase Stimulators [MoA]": ("CAT003", "Cardiovascular"),
    "HER2/Neu/cerbB2 Antagonists [MoA]": ("CAT012", "Oncology"),
    "HMG-CoA Reductase Inhibitor [EPC]": ("CAT003", "Cardiovascular"),
    "Hedgehog Pathway Inhibitor [EPC]": ("CAT012", "Oncology"),
    "Hematopoietic Stem Cell Mobilizer [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Heparin": ("CAT003", "Cardiovascular"),
    "Heparin Binding Activity [MoA]": ("CAT003", "Cardiovascular"),
    "Human Immunodeficiency Virus 1 Non-Nucleoside Analog Reverse Transcriptase Inhibitor [EPC]": ("CAT001", "Antibiotics"),
    "Human Immunodeficiency Virus Nucleoside Analog Reverse Transcriptase Inhibitor [EPC]": ("CAT001", "Antibiotics"),
    "Human Serum Albumin [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Hyperpolarization-activated Cyclic Nucleotide-gated Channel Antagonists [MoA]": ("CAT005", "Neurology & Psychiatry"),
    "Hypoxia-Inducible Factor Prolyl Hydroxylase Inhibitors [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Imidazolines [CS]": ("CAT005", "Neurology & Psychiatry"),
    "Increased Diuresis [PE]": ("CAT003", "Cardiovascular"),
    "Increased Diuresis at Loop of Henle [PE]": ("CAT003", "Cardiovascular"),
    "Increased Intravascular Volume [PE]": ("CAT003", "Cardiovascular"),
    # =====================================================
    # BATCH 5
    # =====================================================

    "Increased Megakaryocyte Maturation [PE]": ("CAT010", "Vaccines & Biologics"),
    "Increased Prostaglandin Activity [PE]": ("CAT004", "Pain & Inflammation"),
    "Increased Uterine Smooth Muscle Contraction or Tone [PE]": ("CAT009", "Hormonal"),
    "Inhibit Ovum Fertilization [PE]": ("CAT009", "Hormonal"),
    "Integrin Receptor Antagonist [EPC]": ("CAT003", "Cardiovascular"),
    "Kallikrein Inhibitors [MoA]": ("CAT003", "Cardiovascular"),
    "Local Anesthesia [PE]": ("CAT004", "Pain & Inflammation"),
    "Medium-chain Triglyceride [EPC]": ("CAT013", "Supplements"),
    "Melanocortin 4 Receptor Agonist [EPC]": ("CAT009", "Hormonal"),
    "Melanocortin Receptor Agonist [EPC]": ("CAT009", "Hormonal"),
    "Melatonin Receptor Agonist [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Methylating Activity [MoA]": ("CAT012", "Oncology"),
    "Methyltransferase Inhibitor [EPC]": ("CAT012", "Oncology"),
    "Methylxanthine [EPC]": ("CAT006", "Allergy & Respiratory"),
    "Microtubule Inhibition [PE]": ("CAT012", "Oncology"),
    "Monoamine Oxidase Inhibitor [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Mood Stabilizer [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "N-methyl-D-aspartate Receptor Antagonist [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Neonatal Fc Receptor Blocker [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Nicotinic Acid [EPC]": ("CAT013", "Supplements"),
    "Norepinephrine Reuptake Inhibitor [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Norepinephrine Uptake Inhibitors [MoA]": ("CAT005", "Neurology & Psychiatry"),
    "Nuclear Export Inhibitor [EPC]": ("CAT012", "Oncology"),
    "Nucleic Acid Synthesis Inhibitors [MoA]": ("CAT012", "Oncology"),
    "Oligonucleotide Telomerase Inhibitor [EPC]": ("CAT012", "Oncology"),
    "Orexin Receptor Antagonist [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Organic Anion Transporting Polypeptide 2B1 Inhibitors [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Organic Cation Transporter 2 Inhibitors [MoA]": ("CAT014", "Medical Devices / Misc"),
    "P-Glycoprotein Inhibitors [MoA]": ("CAT014", "Medical Devices / Misc"),
    "PPAR alpha [CS]": ("CAT003", "Cardiovascular"),
    # =====================================================
    # BATCH 6 (FINAL)
    # =====================================================

    "Pediculicide [EPC]": ("CAT001", "Antibiotics"),
    "Peroxisome Proliferator Receptor alpha Agonist [EPC]": ("CAT003", "Cardiovascular"),
    "Phenothiazine [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Phenylalanine Ammonia-Lyase [CS]": ("CAT014", "Medical Devices / Misc"),
    "Platinum-based Drug [EPC]": ("CAT012", "Oncology"),
    "Porphyrin Precursor [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Potassium Channel Antagonists [MoA]": ("CAT003", "Cardiovascular"),
    "Prostaglandin Analog [EPC]": ("CAT004", "Pain & Inflammation"),
    "Prostaglandin E1 Analog [EPC]": ("CAT004", "Pain & Inflammation"),
    "Prostaglandin E2 Receptor Agonist [EPC]": ("CAT004", "Pain & Inflammation"),
    "Pyrethrins [CS]": ("CAT001", "Antibiotics"),
    "Pyridone [EPC]": ("CAT014", "Medical Devices / Misc"),
    "RANK Ligand Blocking Activity [MoA]": ("CAT012", "Oncology"),
    "Retinoid [EPC]": ("CAT008", "Dermatology"),
    "Sclerosing Activity [MoA]": ("CAT014", "Medical Devices / Misc"),
    "Semifluorinated Alkane [EPC]": ("CAT014", "Medical Devices / Misc"),
    "Sigma-1 Agonist [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Sphingosine 1-Phosphate Receptor Modulators [MoA]": ("CAT010", "Vaccines & Biologics"),
    "Sulfone [EPC]": ("CAT001", "Antibiotics"),
    "Thalidomide Analog [EPC]": ("CAT012", "Oncology"),
    "Thymic Stromal Lymphopoietin Blocker [EPC]": ("CAT010", "Vaccines & Biologics"),
    "Tissue Factor Pathway Inhibitor Antagonist [EPC]": ("CAT003", "Cardiovascular"),
    "Tryptophan Hydroxylase Inhibitor [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "UNKNOWN": ("CAT015", "Others"),
    "Urate Oxidase [CS]": ("CAT014", "Medical Devices / Misc"),
    "Vesicular Monoamine Transporter 2 Inhibitor [EPC]": ("CAT005", "Neurology & Psychiatry"),
    "Vinca Alkaloid [EPC]": ("CAT012", "Oncology"),
    "Xanthine Oxidase Inhibitor [EPC]": ("CAT003", "Cardiovascular"),
    "alpha Glucosidase Inhibitors [MoA]": ("CAT002", "Antidiabetic"),
    "gamma-Cyclodextrins [CS]": ("CAT014", "Medical Devices / Misc"),
}

RULES = [

    # ======================================================
    # ANTIBIOTICS
    # ======================================================

    ("aminoglycoside", "CAT001"),
    ("cephalosporin", "CAT001"),
    ("penicillin", "CAT001"),
    ("macrolide", "CAT001"),
    ("quinolone", "CAT001"),
    ("fluoroquinolone", "CAT001"),
    ("carbapenem", "CAT001"),
    ("glycopeptide", "CAT001"),
    ("tetracycline", "CAT001"),
    ("sulfonamide", "CAT001"),
    ("antibacterial", "CAT001"),
    ("antibiotic", "CAT001"),
    ("antimicrobial", "CAT001"),
    ("antiviral", "CAT001"),
    ("antifungal", "CAT001"),
    ("antiparasitic", "CAT001"),
    ("antimalarial", "CAT001"),
    ("anthelmintic", "CAT001"),
    ("antiinfective", "CAT001"),
    ("anti-infective", "CAT001"),
    ("mycobacterial", "CAT001"),

    # ======================================================
    # ANTIDIABETIC
    # ======================================================

    ("antidiabetic", "CAT002"),
    ("insulin", "CAT002"),
    ("biguanide", "CAT002"),
    ("glp", "CAT002"),
    ("dpp", "CAT002"),
    ("sglt", "CAT002"),
    ("sodium-glucose", "CAT002"),
    ("sulfonylurea", "CAT002"),
    ("thiazolidinedione", "CAT002"),
    ("amylin", "CAT002"),

    # ======================================================
    # CARDIOVASCULAR
    # ======================================================

    ("angiotensin", "CAT003"),
    ("ace inhibitor", "CAT003"),
    ("renin", "CAT003"),
    ("aldosterone", "CAT003"),
    ("antiarrhythmic", "CAT003"),
    ("arrhythm", "CAT003"),
    ("vasodilator", "CAT003"),
    ("vasoconstrictor", "CAT003"),
    ("anticoagulant", "CAT003"),
    ("antiplatelet", "CAT003"),
    ("thrombin", "CAT003"),
    ("factor xa", "CAT003"),
    ("statin", "CAT003"),
    ("lipid", "CAT003"),
    ("cholesterol", "CAT003"),
    ("adrenergic alpha", "CAT003"),
    ("adrenergic beta", "CAT003"),
    ("beta blocker", "CAT003"),
    ("beta-blocker", "CAT003"),
    ("calcium channel", "CAT003"),
    ("diuretic", "CAT003"),
    ("hypertension", "CAT003"),
    ("antihypertensive", "CAT003"),
    ("cardiac", "CAT003"),
    ("heart", "CAT003"),

    # ======================================================
    # PAIN & INFLAMMATION
    # ======================================================

    ("anti-inflammatory", "CAT004"),
    ("anti inflammatory", "CAT004"),
    ("analgesic", "CAT004"),
    ("pain", "CAT004"),
    ("opioid", "CAT004"),
    ("cox", "CAT004"),
    ("cyclooxygenase", "CAT004"),
    ("lipoxygenase", "CAT004"),
    ("nsaid", "CAT004"),
    ("local anesthetic", "CAT004"),
    ("anesthetic", "CAT004"),
    ("corticosteroid", "CAT004"),
    ("glucocorticoid", "CAT004"),
        # ======================================================
    # NEUROLOGY & PSYCHIATRY
    # ======================================================

    ("antidepressant", "CAT005"),
    ("antipsychotic", "CAT005"),
    ("antiepileptic", "CAT005"),
    ("anticonvulsant", "CAT005"),
    ("benzodiazepine", "CAT005"),
    ("dopamine", "CAT005"),
    ("serotonin", "CAT005"),
    ("gaba", "CAT005"),
    ("nmda", "CAT005"),
    ("ampa", "CAT005"),
    ("acetylcholine", "CAT005"),
    ("cholinergic", "CAT005"),
    ("cholinesterase", "CAT005"),
    ("cns", "CAT005"),
    ("central nervous", "CAT005"),
    ("neurology", "CAT005"),
    ("psychiatric", "CAT005"),
    ("migraine", "CAT005"),
    ("parkinson", "CAT005"),
    ("alzheimer", "CAT005"),
    ("amyloid", "CAT005"),
    ("neuro", "CAT005"),
    ("sedative", "CAT005"),
    ("hypnotic", "CAT005"),
    ("anxiolytic", "CAT005"),

    # ======================================================
    # ALLERGY & RESPIRATORY
    # ======================================================

    ("histamine", "CAT006"),
    ("h1 receptor", "CAT006"),
    ("h2 receptor", "CAT006"),
    ("antihistamine", "CAT006"),
    ("allergen", "CAT006"),
    ("allergy", "CAT006"),
    ("leukotriene", "CAT006"),
    ("bronchodilator", "CAT006"),
    ("beta2", "CAT006"),
    ("beta-2", "CAT006"),
    ("respiratory", "CAT006"),
    ("asthma", "CAT006"),
    ("pulmonary", "CAT006"),
    ("airway", "CAT006"),
    ("cough", "CAT006"),
    ("antitussive", "CAT006"),
    ("decongestant", "CAT006"),
    ("surfactant", "CAT006"),

    # ======================================================
    # GASTROINTESTINAL
    # ======================================================

    ("gastrointestinal", "CAT007"),
    ("digestive", "CAT007"),
    ("proton pump", "CAT007"),
    ("ppi", "CAT007"),
    ("antacid", "CAT007"),
    ("antiemetic", "CAT007"),
    ("laxative", "CAT007"),
    ("constipation", "CAT007"),
    ("diarrhea", "CAT007"),
    ("antidiarrheal", "CAT007"),
    ("bowel", "CAT007"),
    ("intestinal", "CAT007"),
    ("stomach", "CAT007"),
    ("gastric", "CAT007"),
    ("ulcer", "CAT007"),
    ("hepatic", "CAT007"),
    ("liver", "CAT007"),

    # ======================================================
    # DERMATOLOGY
    # ======================================================

    ("dermatology", "CAT008"),
    ("dermatologic", "CAT008"),
    ("topical", "CAT008"),
    ("skin", "CAT008"),
    ("acne", "CAT008"),
    ("psoriasis", "CAT008"),
    ("eczema", "CAT008"),
    ("keratolytic", "CAT008"),
    ("antiseptic", "CAT008"),
    ("antifungal skin", "CAT008"),
    ("cutaneous", "CAT008"),
    ("scalp", "CAT008"),

    # ======================================================
    # HORMONAL
    # ======================================================

    ("hormone", "CAT009"),
    ("estrogen", "CAT009"),
    ("progesterone", "CAT009"),
    ("androgen", "CAT009"),
    ("testosterone", "CAT009"),
    ("thyroid", "CAT009"),
    ("pituitary", "CAT009"),
    ("adrenal", "CAT009"),
    ("cortisol", "CAT009"),
    ("gonadotropin", "CAT009"),
    ("aromatase", "CAT009"),
    ("5-alpha", "CAT009"),
    ("steroid", "CAT009"),
    ("glucocorticoid", "CAT009"),
    ("mineralocorticoid", "CAT009"),

    # ======================================================
    # VACCINES & BIOLOGICS
    # ======================================================

    ("vaccine", "CAT010"),
    ("toxoid", "CAT010"),
    ("immune globulin", "CAT010"),
    ("immunoglobulin", "CAT010"),
    ("monoclonal antibody", "CAT010"),
    ("antibody", "CAT010"),
    ("biologic", "CAT010"),
    ("immunotherapy", "CAT010"),

    # ======================================================
    # OPHTHALMOLOGY
    # ======================================================

    ("ophthalmic", "CAT011"),
    ("ocular", "CAT011"),
    ("eye", "CAT011"),
    ("glaucoma", "CAT011"),
    ("retina", "CAT011"),
    ("tear", "CAT011"),
    ("lacrimal", "CAT011"),

    # ======================================================
    # ONCOLOGY
    # ======================================================

    ("oncology", "CAT012"),
    ("cancer", "CAT012"),
    ("tumor", "CAT012"),
    ("neoplasm", "CAT012"),
    ("antineoplastic", "CAT012"),
    ("chemotherapy", "CAT012"),
    ("kinase inhibitor", "CAT012"),
    ("tyrosine kinase", "CAT012"),
    ("jak inhibitor", "CAT012"),
    ("braf", "CAT012"),
    ("bcr-abl", "CAT012"),
    ("vegf", "CAT012"),
    ("vegfr", "CAT012"),
    ("egfr", "CAT012"),
    ("pd-1", "CAT012"),
    ("pd-l1", "CAT012"),
    ("cd20", "CAT012"),
    ("cd19", "CAT012"),
    ("checkpoint inhibitor", "CAT012"),
    ("apoptosis", "CAT012"),
    ("anthracycline", "CAT012"),
    ("antimetabolite", "CAT012"),
    ("alkylating", "CAT012"),

    # ======================================================
    # SUPPLEMENTS
    # ======================================================

    ("vitamin", "CAT013"),
    ("mineral", "CAT013"),
    ("electrolyte", "CAT013"),
    ("nutrition", "CAT013"),
    ("nutritional", "CAT013"),
    ("amino acid", "CAT013"),
    ("trace element", "CAT013"),
    ("ascorbic acid", "CAT013"),
    ("folic acid", "CAT013"),
    ("iron", "CAT013"),
    ("calcium", "CAT013"),
    ("zinc", "CAT013"),
    ("magnesium", "CAT013"),

    # ======================================================
    # MEDICAL DEVICES / MISC
    # ======================================================

    ("diagnostic", "CAT014"),
    ("contrast", "CAT014"),
    ("radioactive", "CAT014"),
    ("radiopharmaceutical", "CAT014"),
    ("device", "CAT014"),
    ("scaffold", "CAT014"),
    ("implant", "CAT014"),
    ("acidifying", "CAT014"),
    ("alkalinizing", "CAT014"),
    ("chelating", "CAT014"),
    ("lubricant", "CAT014"),
    ("irrigation", "CAT014"),
    ("dialysis", "CAT014"),
    ("adsorbent", "CAT014"),
        # ======================================================
    # DEFAULT
    # ======================================================
        # ======================================================
    # IMMUNOLOGY / BIOLOGICS
    # ======================================================

    ("interleukin", "CAT010"),
    ("interferon", "CAT010"),
    ("complement", "CAT010"),
    ("cytokine", "CAT010"),
    ("growth factor", "CAT010"),
    ("colony stimulating", "CAT010"),
    ("colony-stimulating", "CAT010"),
    ("lymphocyte", "CAT010"),
    ("immune", "CAT010"),
    ("immunologic", "CAT010"),
    ("immunosuppressant", "CAT010"),
    ("antigen", "CAT010"),
    ("antitoxin", "CAT010"),
    ("antitoxins", "CAT010"),

    # ======================================================
    # ANTIVIRALS / INFECTIOUS DISEASE
    # ======================================================

    ("hiv", "CAT001"),
    ("hepatitis", "CAT001"),
    ("influenza", "CAT001"),
    ("cytomegalovirus", "CAT001"),
    ("sars-cov", "CAT001"),
    ("neuraminidase", "CAT001"),
    ("viral", "CAT001"),

    # ======================================================
    # ONCOLOGY
    # ======================================================

    ("dna polymerase", "CAT012"),
    ("dna replication", "CAT012"),
    ("rna polymerase", "CAT012"),
    ("protein synthesis", "CAT012"),
    ("topoisomerase", "CAT012"),
    ("proteasome", "CAT012"),
    ("parp", "CAT012"),
    ("poly(adp-ribose)", "CAT012"),
    ("histone", "CAT012"),
    ("menin", "CAT012"),
    ("isocitrate", "CAT012"),
    ("cyclin-dependent kinase", "CAT012"),

    # ======================================================
    # CARDIOVASCULAR
    # ======================================================

    ("vasodilation", "CAT003"),
    ("vasoconstriction", "CAT003"),
    ("vasopressin", "CAT003"),
    ("prostacyclin", "CAT003"),
    ("prostacyclin receptor", "CAT003"),
    ("p-selectin", "CAT003"),
    ("blood coagulation", "CAT003"),
    ("factor viii", "CAT003"),
    ("platelet", "CAT003"),
    ("phosphodiesterase", "CAT003"),

    # ======================================================
    # GASTROINTESTINAL
    # ======================================================

    ("bile", "CAT007"),
    ("phosphate binder", "CAT007"),
    ("potassium binder", "CAT007"),
    ("urease", "CAT007"),

    # ======================================================
    # HORMONAL
    # ======================================================

    ("thyroxine", "CAT009"),
    ("triiodothyronine", "CAT009"),
    ("calcitonin", "CAT009"),

    # ======================================================
    # SUPPLEMENTS
    # ======================================================

    ("ergocalciferol", "CAT013"),
    ("cholecalciferol", "CAT013"),
    ("fatty acid", "CAT013"),
    ("carnitine", "CAT013"),

    # ======================================================
    # MEDICAL DEVICES / MISC
    # ======================================================

    ("cytochrome", "CAT014"),
    ("enzyme", "CAT014"),
    ("lysosomal", "CAT014"),
    ("radioligand", "CAT014"),
    ("positron", "CAT014"),
    ("photoabsorption", "CAT014"),
    ("osmotic", "CAT014"),
    ("oxidation-reduction", "CAT014"),

]

# ==========================================================
# APPLY RULE ENGINE
# ==========================================================
mapped = 0
others = 0

for index, row in df.iterrows():

    pharm_class = str(row["Pharm_Class"]).strip()
    pharm_lower = pharm_class.lower()

    category_id = None

    # First check manual mapping
    if pharm_class in MANUAL_MAPPING:

        category_id, category_name = MANUAL_MAPPING[pharm_class]

        df.at[index, "Category_ID"] = category_id
        df.at[index, "Category_Name"] = category_name
        df.at[index, "Matched_Rule"] = "MANUAL"

        if category_id == "CAT015":
         others += 1
        else:
         mapped += 1

    # Otherwise use rule engine
    else:

        for keyword, cat_id in RULES:

            if keyword in pharm_lower:
                category_id = cat_id
                break

        if category_id:

            df.at[index, "Category_ID"] = category_id
            df.at[index, "Category_Name"] = CATEGORY_MASTER[category_id]
            df.at[index, "Matched_Rule"] = keyword

            if category_id == "CAT015":
                others += 1
            else:
                mapped += 1

        else:

            df.at[index, "Category_ID"] = "CAT015"
            df.at[index, "Category_Name"] = CATEGORY_MASTER["CAT015"]
            df.at[index, "Matched_Rule"] = "UNMATCHED"
            others += 1
            mapped += 1
others = (df["Category_ID"] == "CAT015").sum()
mapped = len(df) - others
print(f"Successfully Mapped : {mapped}")
print(f"Mapped to Others    : {others}")
# ==========================================================
# CATEGORY STATISTICS
# ==========================================================

print("\nCategory Distribution")
print("-" * 70)

category_summary = (

    df.groupby(
        ["Category_ID", "Category_Name"]
    )
    .size()
    .reset_index(name="Count")
    .sort_values(
        "Count",
        ascending=False
    )

)

print(category_summary.to_string(index=False))

# ==========================================================
# RULE USAGE
# ==========================================================

print("\nTop Matching Rules")
print("-" * 70)

rule_summary = (

    df["Matched_Rule"]
    .value_counts()
    .head(20)

)

print(rule_summary)

# ==========================================================
# MAPPING SUMMARY
# ==========================================================

print("\nSummary")
print("-" * 70)

print(f"Total Pharm Classes : {len(df):,}")
print(f"Mapped              : {mapped:,}")
print(f"Others              : {others:,}")

coverage = round(((mapped + others) / len(df)) * 100, 2)

print(f"Coverage            : {coverage}%")
# ==========================================================
# SAVE UPDATED MAPPING
# ==========================================================

df.drop(columns=["Matched_Rule"]).to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

print("\nUpdated Pharm_Class_Mapping.csv saved successfully.")

# ==========================================================
# EXPORT UNMAPPED CLASSES
# ==========================================================
# Export only truly unmapped classes
unmapped_df = df[df["Category_ID"].isna()]

if len(unmapped_df) > 0:
    unmapped_df.to_csv(
        UNMAPPED_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    print("Unmapped classes exported to:")
    print(UNMAPPED_FILE)
else:
    print("No unmapped Pharm Classes found.")
# ==========================================================
# VALIDATION
# ==========================================================

print("\n" + "=" * 70)
print("VALIDATION")
print("=" * 70)

required_columns = [
    "Pharm_Class",
    "Category_ID",
    "Category_Name"
]

missing_columns = []

for col in required_columns:

    if col not in df.columns:
        missing_columns.append(col)

if len(missing_columns) == 0:
    print("Required Columns          : PASS")
else:
    print("Required Columns          : FAIL")
    print("Missing:", missing_columns)

duplicate_pharm = df["Pharm_Class"].duplicated().sum()

if duplicate_pharm == 0:
    print("Duplicate Pharm Classes   : PASS")
else:
    print(f"Duplicate Pharm Classes   : FAIL ({duplicate_pharm})")

missing_category = df["Category_ID"].isna().sum()

if missing_category == 0:
    print("Missing Category_ID       : PASS")
else:
    print(f"Missing Category_ID       : FAIL ({missing_category})")

invalid_category = (
    ~df["Category_ID"].isin(CATEGORY_MASTER.keys())
).sum()

if invalid_category == 0:
    print("Invalid Category_ID       : PASS")
else:
    print(f"Invalid Category_ID       : FAIL ({invalid_category})")

# ==========================================================
# FINAL REPORT
# ==========================================================

print("\n" + "=" * 70)
print("PHARMAOPS AI - PHARM CLASS MAPPING COMPLETED")
print("=" * 70)

print(f"Total Pharm Classes      : {len(df):,}")
print(f"Successfully Mapped      : {mapped:,}")
print(f"Mapped to Others         : {others:,}")
print(f"Coverage                : {coverage}%")

print("\nFinal Category Distribution")
print("-" * 70)

final_summary = (
    df.groupby(["Category_ID", "Category_Name"])
      .size()
      .reset_index(name="Count")
      .sort_values("Count", ascending=False)
)

print(final_summary.to_string(index=False))

print("\nFiles Generated")
print("-" * 70)
print(f"✓ {OUTPUT_FILE}")

if not unmapped_df.empty:
    print(f"✓ {UNMAPPED_FILE}")

print("\nProcess Completed Successfully.")
print("=" * 70)