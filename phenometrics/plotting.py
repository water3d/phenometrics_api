import pandas
import seaborn
from matplotlib import pyplot as plt


def plot_phenometrics(measurements, phenometrics):
	df = pandas.DataFrame(measurements, columns=["veg_index", "date"])
	seaborn.lineplot(data=df, x="date", y="veg_index")
	plt.show()