import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
import statistics

df = pd.read_csv("irisdataset.csv")
print(df.head)
print(df)

## Summary ##

describeStats = str(df.describe())
medianStats = str("median     " + str(statistics.median(df.sepal_length)) + "00000" + "     " + str(statistics.median(df.sepal_width)) + "00000" + "      " + str(statistics.median(df.petal_length)) + "0000" + "     " + str(statistics.median(df.petal_width)) + "00000")

modeStats = str("mode       " + str(statistics.mode(df.sepal_length)) + "00000" + "     " + str(statistics.mode(df.sepal_width)) + "00000" + "      " + str(statistics.mode(df.petal_length)) + "00000" + "     " + str(statistics.mode(df.petal_width)) + "00000")

summaryText = open("summary.txt", "w")

summaryText.write("Summary of statistical information on Fisher's iris data set:" + "\n" + "\n")
summaryText.write(describeStats + "\n" + medianStats + "\n" + modeStats)
summaryText.close()


## Histograms ##

plt.hist(df.sepal_length, bins=20, edgecolor="black")
plt.title("Sepal Length")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.savefig("sl_hist.png")
plt.show()

plt.hist(df.sepal_width, bins=20, edgecolor="black")
plt.title("Sepal Width")
plt.xlabel("Width (cm)")
plt.ylabel("Frequency")
plt.savefig("sw_hist.png")
plt.show()

plt.hist(df.petal_length, bins=20, edgecolor="black")
plt.title("Petal Length")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.savefig("pl_hist.png")
plt.show()

plt.hist(df.petal_width, bins=20, edgecolor="black")
plt.title("Petal Width")
plt.xlabel("Width (cm)")
plt.ylabel("Frequency")
plt.savefig("pw_hist.png")
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
