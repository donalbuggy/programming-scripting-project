import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("iris.csv")

plt.scatter(df["petal_length"], df["petal_width"])
plt.title("Petal length vs Petal width")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.savefig("pl_pw.png")
plt.show()

plt.scatter(df["petal_length"], df["sepal_length"])
plt.title("Petal length vs Sepal length")
plt.xlabel("Petal length")
plt.ylabel("Sepal length")
plt.savefig("pl_sl.png")
plt.show()

plt.scatter(df["petal_length"], df["sepal_width"])
plt.title("Petal length vs Sepal width")
plt.xlabel("Petal length")
plt.ylabel("Sepal width")
plt.savefig("pl_sl.png")
plt.show()

plt.scatter(df["sepal_length"], df["petal_width"])
plt.title("Sepal length vs Petal width")
plt.xlabel("Sepal length")
plt.ylabel("Petal width")
plt.savefig("sl_pw.png")
plt.show()

plt.scatter(df["sepal_length"], df["sepal_width"])
plt.title("Sepal length vs Sepal width")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.savefig("sl_sw.png")
plt.show()

plt.scatter(df["petal_width"], df["sepal_width"])
plt.title("Petal width vs Sepal width")
plt.xlabel("Petal Width")
plt.ylabel("Sepal width")
plt.savefig("pw_sw.png")
plt.show()

sns.pairplot(df, hue="species")
plt.savefig("species_matrix.png")
plt.show()