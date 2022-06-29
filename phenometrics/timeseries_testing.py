import phenolopy
import xarray
import numpy
from datetime import datetime

import timeseries

def raw_test():
	data_list = [0.15,0.15,0.15,0.2,0.22,0.25,0.3,0.4,0.45,0.5,0.48,0.53,0.58,0.55,0.62,0.64,0.63,0.65,0.6,0.5,0.35,0.25,0.2,0.15,0.15,0.15,0.15,0.15,0.15]
	dates = [datetime.strptime("01/01/2022", "%m/%d/%Y"),datetime.strptime("01/14/2022", "%m/%d/%Y"),datetime.strptime("01/27/2022", "%m/%d/%Y"),datetime.strptime("02/09/2022", "%m/%d/%Y"),datetime.strptime("02/22/2022", "%m/%d/%Y"),datetime.strptime("03/07/2022", "%m/%d/%Y"),datetime.strptime("03/20/2022", "%m/%d/%Y"),datetime.strptime("04/02/2022", "%m/%d/%Y"),datetime.strptime("04/15/2022", "%m/%d/%Y"),datetime.strptime("04/28/2022", "%m/%d/%Y"),datetime.strptime("05/11/2022", "%m/%d/%Y"),datetime.strptime("05/24/2022", "%m/%d/%Y"),datetime.strptime("06/06/2022", "%m/%d/%Y"),datetime.strptime("06/19/2022", "%m/%d/%Y"),datetime.strptime("07/02/2022", "%m/%d/%Y"),datetime.strptime("07/15/2022", "%m/%d/%Y"),datetime.strptime("07/28/2022", "%m/%d/%Y"),datetime.strptime("08/10/2022", "%m/%d/%Y"),datetime.strptime("08/23/2022", "%m/%d/%Y"),datetime.strptime("09/05/2022", "%m/%d/%Y"),datetime.strptime("09/18/2022", "%m/%d/%Y"),datetime.strptime("10/01/2022", "%m/%d/%Y"),datetime.strptime("10/14/2022", "%m/%d/%Y"),datetime.strptime("10/27/2022", "%m/%d/%Y"),datetime.strptime("11/09/2022", "%m/%d/%Y"),datetime.strptime("11/22/2022", "%m/%d/%Y"),datetime.strptime("12/05/2022", "%m/%d/%Y"),datetime.strptime("12/18/2022", "%m/%d/%Y"),datetime.strptime("12/31/2022", "%m/%d/%Y")]
	timestamps = [date.timestamp() for date in dates]

	data_array = numpy.array((data_list, timestamps))  # use timstamps in array, but add dates as the time coord
	da = xarray.DataArray(data_array, dims=["veg_index", "time"], coords=dict(time=dates))

	results = phenolopy.calc_phenometrics(da)
	print(results)
	print(f"Start of Season Value: {results['sos_values'][0]}")
	print(f"Start of Season Time: {results['sos_times'][0]}")
	print(f"End of Season Value: {results['eos_values'][0]}")
	print(f"End of Season Time: {results['eos_times'][0]}")
	print(f"Middle of Season: {results['mos_values'][0]}")
	print(f"Length of Season: {results['eos_times'][0] - results['sos_times'][0]}")
	print(f"Amplitude of Season: {results['aos_values'][0]}")
	print(f"Productivity (Long Integral) of Season: {results['lios_values'][0]}")
	print(f"Productivity (Short Integral - likely cropping) of Season: {results['sios_values'][0]}")
	#print(f"Number of Seasons: {results['nos'][0]}")


def test_function():
	data_list = [0.15,0.15,0.15,0.2,0.22,0.25,0.3,0.4,0.45,0.5,0.48,0.53,0.58,0.55,0.62,0.64,0.63,0.65,0.6,0.5,0.35,0.25,0.2,0.15,0.15,0.15,0.15,0.15,0.15]
	dates = [datetime.strptime("01/01/2022", "%m/%d/%Y"),datetime.strptime("01/14/2022", "%m/%d/%Y"),datetime.strptime("01/27/2022", "%m/%d/%Y"),datetime.strptime("02/09/2022", "%m/%d/%Y"),datetime.strptime("02/22/2022", "%m/%d/%Y"),datetime.strptime("03/07/2022", "%m/%d/%Y"),datetime.strptime("03/20/2022", "%m/%d/%Y"),datetime.strptime("04/02/2022", "%m/%d/%Y"),datetime.strptime("04/15/2022", "%m/%d/%Y"),datetime.strptime("04/28/2022", "%m/%d/%Y"),datetime.strptime("05/11/2022", "%m/%d/%Y"),datetime.strptime("05/24/2022", "%m/%d/%Y"),datetime.strptime("06/06/2022", "%m/%d/%Y"),datetime.strptime("06/19/2022", "%m/%d/%Y"),datetime.strptime("07/02/2022", "%m/%d/%Y"),datetime.strptime("07/15/2022", "%m/%d/%Y"),datetime.strptime("07/28/2022", "%m/%d/%Y"),datetime.strptime("08/10/2022", "%m/%d/%Y"),datetime.strptime("08/23/2022", "%m/%d/%Y"),datetime.strptime("09/05/2022", "%m/%d/%Y"),datetime.strptime("09/18/2022", "%m/%d/%Y"),datetime.strptime("10/01/2022", "%m/%d/%Y"),datetime.strptime("10/14/2022", "%m/%d/%Y"),datetime.strptime("10/27/2022", "%m/%d/%Y"),datetime.strptime("11/09/2022", "%m/%d/%Y"),datetime.strptime("11/22/2022", "%m/%d/%Y"),datetime.strptime("12/05/2022", "%m/%d/%Y"),datetime.strptime("12/18/2022", "%m/%d/%Y"),datetime.strptime("12/31/2022", "%m/%d/%Y")]

	measurements = []
	for i in range(len(data_list)):
		measurements.append({'index_value': data_list[i], 'date_value': dates[i]})
	print(measurements)

	timeseries.get_phenometrics_basic(measurements, 'index_value', 'date_value', None)

test_function()