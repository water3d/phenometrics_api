from collections import defaultdict
import csv

import timeseries
import plotting


def load_appeears_csv(filepath, metric="Median"):
	appeears_results = defaultdict(lambda: dict(inputs=list(), results=None))
	with open(filepath, 'r') as appeears_data:
		reader = csv.DictReader(appeears_data)
		for row in reader:
			row_input = {
				"date": row["Date"],
				"index_value": float(row[metric])
			}
			appeears_results[row["aid"]]["inputs"].append(row_input)

	for area in appeears_results:
		results = timeseries.get_phenometrics_basic(appeears_results[area]["inputs"], index_field="index_value", date_field="date", date_format="%Y-%m-%d %H:%M:%S %Z")
		appeears_results[area]["results"] = results["results"]
		appeears_results[area]["measurements_numpy"] = results["measurements_numpy"]
		appeears_results[area]["measurements_da"] = results["measurements_da"]

	plotting.plot_phenometrics(appeears_results[area]["measurements_numpy"].T, appeears_results[area]["results"])

	return appeears_results["results"]

load_appeears_csv(r"C:\Users\dsx\Downloads\ECO3ETALEXI-001-Statistics.csv")