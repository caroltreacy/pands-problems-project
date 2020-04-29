# IPython log file


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv")

plt.plot(df["PetalLength"], "r.", df["PetalWidth"], "b.")
plt.title("Petal Length v's Petal Width")
plt.xlabel("Length")
plt.ylabel("Width")
plt.savefig("scatter.png")
plt.clf ()

plt.plot(df["SepalLength"], "r.", df["SepalWidth"], "b.")
plt.title("Sepal Length v's Sepal Width")
plt.xlabel("Length")
plt.ylabel("Width")
plt.savefig("scatter1.png")
plt.clf ()

plt.hist(df["PetalLength"])
plt.title("Petal Length")
plt.savefig("hist.png")
plt.clf ()

plt.hist(df["PetalWidth"])
plt.title("Petal Width")
plt.savefig("hist2.png")
plt.clf ()

plt.hist(df["SepalLength"])
plt.title("Sepal Length")
plt.savefig("hist3.png")
plt.clf ()

plt.hist(df["SepalWidth"])
plt.title("Sepal Width")
plt.savefig("hist4.png")
plt.clf ()


sns.scatterplot('x = mean', 'y = average')
plt.savefig("Scatter2.png")
plt.clf()





