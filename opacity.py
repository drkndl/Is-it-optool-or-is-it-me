# Trying to figure out what is wrong with optool

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from astropy import units as u 

filename = 'for_8to13um_dustkappa.dat' 			# Optool output file
a = 0.1 * u.micron								# Grain size in microns
rho = 3.27 * u.g / u.cm**3 						# Material density of forsterite in g/cm^3
mf = 1.0 										# Mass fraction of the grain

### Opening the usual way, but checking if there is a delimiter issue
op_curve = pd.read_csv(filename, delimiter='\s+', skiprows = 23, names = ['wavelength', 'Kabs', 'Ksca', 'g_asymm'])
# op_curve = pd.read_csv(filename, delimiter='\t', skiprows = 23, names = ['wavelength', 'Kabs', 'Ksca', 'g_asymm'])
 
### Trying with and without the astropy units
lamda = u.Quantity(op_curve['wavelength'].to_numpy(), u.micron)
kappa = op_curve['Kabs'].to_numpy() * u.cm**2 / u.g 
# wavelength = Q_curve['wavelength']
# print(wavelength)
# Kabs = Q_curve['Kabs']

### Calculating the absorption efficiency from the opacity
Q = 4.0 * a.to(u.cm) * kappa * mf * rho / 3.0
print(Q.unit)

plt.plot(lamda, Q)
plt.savefig("optool_forsterite_8to13um_Q.png")

### Opening the output file the primitive way like a barbarian
# wavelength = []
# Kabs = []
# Ksca = []
# g_asymm = []
# count = 0

# with open(filename, 'r') as f:
# 	lines = f.readlines()
# 	for line in lines:

# 		line = line.strip().split()
# 		print(line)
# 		count += 1

# 		if count <= 23:
# 			continue
# 		else:
# 			wavelength.append(float(line[0]))
# 			Kabs.append(float(line[1]))
# 			Ksca.append(float(line[2]))
# 			g_asymm.append(float(line[3]))

# plt.plot(wavelength, Kabs)
# plt.savefig("optool_fors_direct_8to13um_opacity.png")

### Plotting only the first 20 microns
# index = np.where(lamda <= 20 * u.micron)[0][-1]
# ldict_plot = lamda[:index+1]
# kdict_plot = kappa[:index+1]
# plt.plot(ldict_plot, kdict_plot)

# plt.plot(lamda, kappa)
# plt.savefig("optool_fors_Ksca_8to13um_opacity.png")