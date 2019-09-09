# 3D-Antenna-Radiation-Pattern


This code reads a CSV file which has the antenna gain measurements(dBd) for spherical coordinates phi (-90, 90) and theta (-175,175) for
frequency = 26500MHz. This measurement was done using a horn antenna. 

It then converts them to cartesian coordinates using standard mathematical formulae.

The graphic library used for full range 3D plotting is plotly. 

The plot is generated as a local html file displayed in a browser. The color scaling is according to the gain and the gain is in Watts.
