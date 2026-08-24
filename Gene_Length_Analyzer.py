import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("." * 30)

print("GENE LENGTH ANALYZER")

print("." * 30)


genes = ["CFTR", "APOE", "INS", "HBB", "VEGFA"]

gene_lenghts = [189000, 3597, 1430, 1606, 14193]


print("\n", "." * 10, "Genes Length", "." * 10)

print("Genes:", genes)

print("Gene Lengths:", gene_lenghts)


# ==========================================
# FUNCTION
# ==========================================

def gene_data():

    print("\nGene Information")

    print("." * 20)

    for gene, length in zip(genes, gene_lenghts):

        print(gene, ":", length)


gene_data()


# ==========================================
# CONDITIONS
# ==========================================

print("\n", "." * 10, "GENE CLASSIFICATION", "." * 10)

for gene, length in zip(genes, gene_lenghts):

    if length > 100000:

        print(gene, "is high in length")

    elif length > 10000:

        print(gene, "is moderate in length")

    else:

        print(gene, "is small in length")


# ==========================================
# NUMPY ANALYSIS
# ==========================================

print("\n", "." * 10, "NUMPY ANALYSIS", "." * 10)

numpy_array = np.array(gene_lenghts)

print("Maximum gene is:", np.max(numpy_array))

print("Minimum gene is:", np.min(numpy_array))

print("Average mean is:", np.mean(numpy_array))


# ==========================================
# DATAFRAME
# ==========================================

data_frame = pd.DataFrame({

    "gene": genes,
    "length": gene_lenghts

})


print("\nGENE DATAFRAME")

print("." * 20)

print(data_frame)


# ==========================================
# SORTING
# ==========================================

sorted_df = data_frame.sort_values(by="length")

print("\nSORTING GENE DATA")

print("." * 20)

print(sorted_df)


# ==========================================
# FILTERING
# ==========================================

long_genes = data_frame[data_frame["length"] > 10000]

print("\nFILTERED DATA")

print("." * 20)

print(long_genes)


# ==========================================
# DESCRIBE
# ==========================================

print("\nNUMPY GENE STATISTICS")

print("." * 20)

print(data_frame["length"].describe())


# ==========================================
# DATA VISUALIZATION
# ==========================================

sns.set_style("whitegrid")


# ==========================================
# 1. BAR PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.barplot(
    x="gene",
    y="length",
    data=data_frame
)

plt.title("Gene Length Comparison")
plt.xlabel("Gene")
plt.ylabel("Gene Length (bp)")

plt.tight_layout()

plt.show()


# ==========================================
# 2. HISTOGRAM
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data_frame["length"],
    bins=5,
    kde=True
)

plt.title("Distribution of Gene Lengths")
plt.xlabel("Gene Length (bp)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.show()


# ==========================================
# 3. PIE CHART
# ==========================================

plt.figure(figsize=(8, 8))

plt.pie(
    gene_lenghts,
    labels=genes,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gene Length Proportion")

plt.tight_layout()

plt.show()
