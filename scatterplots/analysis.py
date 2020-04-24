# IPython log file

import pandas as pd
get_ipython().run_line_magic('logstart', '')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv")
df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv")

df
df["SepalLength"]
df["SepalWidth"]
df["PetalLength"]
df["PetalWidth"]
df["Name"]
plt.plot(df["PetalLength"], df["PetalWidth"], "b.")
plt.savefig("hist.png")
plt.title("PetalLength")
plt.clf


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     plt.plot(df["PetalLength"], "r.", df["PetalWidth"], "b.")

plt.legend("Iris Petal Length and Width")
plt.title("Iris Petal Length and Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.savefig("hist.png")
plt.clf

plt.legend("Iris Sepal Length and Width")
plt.title("Iris Sepal Length and Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.savefig("hist.png")
plt.clf

plt.hist(df["SeptalLength"])
plt.savefig("hist.png)")
plt.clf 

plt.hist(df["SeptalWidth"])
plt.savefig("hist.png)")
plt.clf 

plt.hist(df["PetalLength"])
plt.savefig("hist.png)")
plt.clf 

plt.hist(df["PetalWidth"])
plt.savefig("hist.png)")
plt.clf 

