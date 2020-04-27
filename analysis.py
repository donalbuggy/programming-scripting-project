import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

df = pd.read_csv("iris.csv")
print(df.head)
print(df)


## Histograms ##

plt.hist(df.sepal_length, bins=20, edgecolor="black")
plt.legend()
plt.title("Sepal Length")
plt.xlabel("Length (mm)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df.sepal_width, bins=20, edgecolor="black")
plt.legend()
plt.title("Sepal Width")
plt.xlabel("Width (mm)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df.petal_length, bins=20, edgecolor="black")
plt.legend()
plt.title("Petal Length")
plt.xlabel("Length (mm)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df.petal_width, bins=20, edgecolor="black")
plt.legend()
plt.title("Petal Width")
plt.xlabel("Width (mm)")
plt.ylabel("Frequency")
plt.show()


## Scatterplots ##

plpw = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
plpw.set(xscale="linear")
plt.savefig("pl_pw.png")
plt.show()

plsl = sns.scatterplot(x="petal_length", y="sepal_length", hue="species", data=df)
plsl.set(xscale="linear")
plt.savefig("pl_sl.png")
plt.show()

plsw = sns.scatterplot(x="petal_length", y="sepal_width", hue="species", data=df)
plsw.set(xscale="linear")
plt.savefig("pl_sw.png")
plt.show()

slpw = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=df)
slpw.set(xscale="linear")
plt.savefig("sl_pw.png")
plt.show()

slsw = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df)
slsw.set(xscale="linear")
plt.savefig("sl_sw.png")
plt.show()

pwsw = sns.scatterplot(x="petal_width", y="sepal_width", hue="species", data=df)
pwsw.set(xscale="linear")
plt.savefig("pw_sw.png")
plt.show()

sns.pairplot(df, hue="species")
plt.savefig("species_matrix.png")
plt.show()
