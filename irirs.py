import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s

df = pd.read_csv('Iris.csv')

#boxplot
s.boxplot(df['SepalLengthCm'],color='green')
plt.title("Boxplot of spies")
plt.xlabel(" Sepallength in cm")
plt.legend()
plt.show()

#scatterplot
species = df['species'].unique()
for sp in species:
    subset = df[df['species'] == sp]
    plt.scatter(subset['PetalLengthCm'], subset['PetalWidthCm'], label=sp)

plt.title('Petal Length vs petal width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.show()


#barplot
species_counts = df['species'].value_counts()

plt.bar(species_counts.index, species_counts.values)
plt.title('Number of Samples per Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

#piechart
df = pd.read_csv('Iris.csv')

species_counts = df['species'].value_counts()

plt.pie(species_counts.values, labels=species_counts.index)
plt.title('Distribution of Iris species')
plt.show()
