from . import phenolopy
import xarray
import numpy
from datetime import datetime
import copy

import datetime
import arrow


def get_phenometrics_basic(measurements, index_field, date_field, date_format="%Y/%m/%d"):

	# this approach currently doesn't allow for any smoothing or interpolation. That may not be what we want. It could
	# be that this code assumes that work has all been done, but I think we'd want a way to pass in dictionaries of data
	# and have that all done too, so need to think about that.

	# need to get the dates as timestamps first
	measurements_processed = _preprocess_measurements(measurements, index_field, date_field, date_format)

	# then make tuples with the veg index and the timestamps
	measurements_tuples = [(meas[index_field], meas["timestamp"]) for meas in measurements_processed]
	date_objects = [meas[date_field] for meas in measurements_processed]

	# then make it into a numpy array and transpose it
	measurements_numpy = numpy.array(measurements_tuples).T  # note the transpose on the end!!

	# then make the xarray dataset
	da = xarray.DataArray(measurements_numpy, dims=["veg_index", "time"], coords=dict(time=date_objects))

	# then calculate the phenometrics
	results = phenolopy.calc_phenometrics(da)

	return results


def _preprocess_measurements(raw_measurements, index_field, date_field, date_format="%Y/%m/%d"):
	"""
		Makes sure that we have measurements as a dictionary with an index value, a datetime object, and a timestamp
	:param raw_measurements:
	:return:
	"""

	if not hasattr(raw_measurements, "__iter__"):  # it needs to be some kind of iterable of dictionaries - likely freshly loaded JSON, but not always
		raise ValueError("raw_measurements must be an iterable object (list, tuple, etc) containing dictionaries")

	outputs = []
	for measurement in raw_measurements:
		if not index_field in measurement:
			continue
		if not date_field in measurement:
			continue

		output = copy.copy(measurement)
		# check if it's a string, and if so, parse it. Otherwise, check if it's an arrow object and convert to datetime.
		# then confirm that it must be a datetime object if it's not one of those.
		if type(output[date_field]) is str:
			if date_format is None:
				raise ValueError("Date value of measurement is a string, but date_format value to interpret string is None")
			output[date_field] = datetime.datetime.strptime(output[date_field], date_format)
		elif isinstance(output[date_field], arrow.arrow.Arrow):
			output[date_field] = output[date_field].datetime
		elif not isinstance(output[date_field], datetime.datetime):
			raise ValueError("measurement dates must be strings, datetime objects, or Aarow objects")

		# add the timestamp value
		if "timestamp" not in output or output["timestamp"] is None:
			output["timestamp"] = output[date_field].timestamp()

		outputs.append(output)

	return outputs
