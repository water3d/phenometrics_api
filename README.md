# Phenometrics API

A Python package and accompanying API that support using phenolopy to calculate
phenometric data for single timeseries. Phenolopy requires a data cube and processes
the imagery data. This package and API will accept an arbitrary timeseries and
return phenolopy's phenometric results as if the timeseries was a single pixel
in a data cube - this can be used for timeseries generated from pixel aggregations,
etc (e.g. field-level aggregations), and also can then support timeseries generated
from multiple sources, including Earth Engine, AppEEARS, OpenET, and more.

More documentation to come - the application works as a proof of concept, but
the package isn't a stable API yet.