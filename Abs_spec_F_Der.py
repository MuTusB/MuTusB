import matplotlib.pyplot as plt
#import matplotlib.style
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


plt.rcParams['figure.figsize'] = [8.0, 6.0]
plt.rcParams['figure.dpi'] = 80
plt.rcParams['savefig.dpi'] = 100

plt.rcParams['font.size'] = 16

plt.rcParams['legend.fontsize'] = 'large'
plt.rcParams['figure.titlesize'] = 'large'

# load data file
data_file = pd.read_csv('Abs_F2C2_F2HC2_FSNOG.csv')
Wl = data_file['w']
f2c2 = data_file['F2C2']
f2hc2 = data_file['F2HC2']
fgsno = data_file['FGSNO']
#f2hc2d = data_file['F2HC2d']

plt.plot(Wl, f2c2, 'r--', label='DTFCys2')
plt.plot(Wl, f2hc2, 'b--', label='DTFHCys2')
plt.plot(Wl, fgsno, 'k--', label='TFSNOG')
#plt.plot(Wl, f2hc2d, 'b-', label='F2HC2 -DTT')

plt.xlabel( 'Wavelength (nm)', fontsize=24, fontweight='bold')
plt.ylabel( 'Absorbance', fontsize=24, fontweight='bold')

plt.grid(True)
plt.legend()
plt.show()
