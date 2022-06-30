class Timeseries(object):
	"""
		Handles storage of a single timeseries, date values, any naming of the index used, and plotting.
		Doesn't care what it's associated with, just represents a timeseries. PhenometricsManager holds
		multiple timeseries and keeps them grouped into an object.
	"""
	pass

class PhenometricsManager(object):
	"""
		Manages Timeseries and phenometrics pairs for a single observable object
	"""