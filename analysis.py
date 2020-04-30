# Donal Buggy
# This project provides a statistical analysis of the Fisher iris dataset.
# It first generates a text file containing a summary of the data, e.g., mean, median, standard deviation, etc. This data is then saved to the user's drive as PNG files
# It then generates histograms for each of the four variables: sepal length, sepal width, petal length, and petal width. These plots are also saved to the user's drive as PNG files
# It then generates scatterplots for each pairing of variables with the three iris species designated by colour. A matrix consisting of all twelve scatterplots is also generated.

# packages to be imported
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
import statistics
import os

# reads the contents of the CSV file into a variable and prints a sample of the data
df = pd.read_csv("irisdataset.csv")
print(df)

## Summary ##

# This is where the summary text file is generated

# The describe function is run on the df varaible to generate most of the data breakdown, and this is saved as a string to a variable to be used later
describeStats = str(df.describe())

# because the describe() function does not generate median or mode from the data, it is done manually for each variable and given the proper formatting here
medianStats = str("median     " + str(statistics.median(df.sepal_length)) + "00000" + "     " + str(statistics.median(df.sepal_width)) + "00000" + "      " + str(statistics.median(df.petal_length)) + "0000" + "     " + str(statistics.median(df.petal_width)) + "00000")

modeStats = str("mode       " + str(statistics.mode(df.sepal_length)) + "00000" + "     " + str(statistics.mode(df.sepal_width)) + "00000" + "      " + str(statistics.mode(df.petal_length)) + "00000" + "     " + str(statistics.mode(df.petal_width)) + "00000")

# opening the text file and setting mode to "write"
summaryText = open("summary.txt", "w")

# contents of the text file including heading
summaryText.write("Summary of statistical information on Fisher's iris data set:" + "\n" + "\n")
summaryText.write(describeStats + "\n" + medianStats + "\n" + modeStats)
summaryText.close()

# for usability, the location of the current working directory (where the generated files will be saved) is read with the os.getcwd function and passed into a variable
# the files will be saved to the directory where the user has installed Python.


print("The summary text file has been added to " + os.getcwd())


## Histograms ##

# The method for each histogram is the same
# matplotlib's pyplot package is passed the variable containing the CSV data for each of the four variables in the data
# the number of bins, title and axis labels are defined also
# the generated PNGs are saved to the same location as the summary text file using the savefig() function

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

print("The histogram images have been added to " + os.getcwd())


## Scatterplots ##

# the seaborn package is passed the df variable in the "data" attribute using the scatterplot() function
# the generated plots are saved to the same directory as the text file and histograms

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

print("The scatterplot images have been added to " + os.getcwd())
