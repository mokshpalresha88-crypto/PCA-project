import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

                    
data = pd.read_csv("data/filtered.tsv.gz", sep="\t")
data.columns = data.columns.str.strip()
labels = pd.read_csv("data/class.tsv", sep="\t", header=None)


xbp1_id = "4404"
gata3_id = "2625"


if xbp1_id not in data.columns or gata3_id not in data.columns:
    print("Gene IDs not found in dataset")
    print("Available columns sample:", data.columns[:20])
    exit()

xbp1 = data[xbp1_id]
gata3 = data[gata3_id]

plt.figure()

for i in range(len(labels)):
    if labels.iloc[i, 0] == 1:
        plt.scatter(gata3[i], xbp1[i], color='red', label='ER+' if i == 0 else "")
    else:
        plt.scatter(gata3[i], xbp1[i], color='blue', label='ER-' if i == 0 else "")

plt.xlabel("GATA3 Expression")
plt.ylabel("XBP1 Expression")
plt.title("Gene Expression Scatter Plot (Figure 1a)")
plt.legend()
plt.show()

pca = PCA(n_components=1)
X_pca = pca.fit_transform(data)

plt.figure()

for i in range(len(labels)):
    if labels.iloc[i, 0] == 1:
        plt.scatter(X_pca[i], 0, color='red')
    else:
        plt.scatter(X_pca[i], 0, color='blue')

plt.title("PCA Projection on PC1 (Figure 1c)")
plt.xlabel("PC1")
plt.yticks([])
plt.show()
