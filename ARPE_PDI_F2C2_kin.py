import matplotlib.pyplot as plt
#import matplotlib.style
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


plt.rcParams['figure.figsize'] = [8.0, 6.0]
plt.rcParams['figure.dpi'] = 80
plt.rcParams['savefig.dpi'] = 100

plt.rcParams['font.size'] = 22
plt.rcParams['legend.fontsize'] = 'large'
plt.rcParams['figure.titlesize'] = 'large'

# load data file
data_file = pd.read_csv('ARPE_PDI_F2C2_kin.csv')
s = data_file['f2c2']
ps = np.linspace(0, 10, 7)

vinit = data_file['vo']
sdev = data_file['sd1']
 # pGSNO = data_file['pv']

# define fitting functions
def vo(s, V0, K0):
 return s * V0 / (K0 + s)

#find optimal params
pO = (0.5, 0.67)
p, pov = curve_fit(vo, s, vinit, pO)
# pp, ppov = curve_fit(vo, s, pGSNO, pO)



#calculate predicted curve
vp = vo(ps, *p)

# vpp = vo(ps, *pp) 

#calculate r^2
r2 = r2_score(vinit, vp)
#print (params)
print('best fit Vm. Km')
print(p)
#print(pp)
print('R^2: ')
print(r2)
print (ps)
# print(time)
# print(fluo[0:3])
# a[0], a[1:] = np.loadtxt('PlateReader_Case.csv', delimiter=',', unpack=True)

plt.plot(s, vinit, 'bo', markersize=9, label='FITC-GSNO')
# plt.plot(s, pGSNO, 'ro', label='+ GSNO')
plt.errorbar(s, vinit, yerr=sdev, linestyle=' ', capsize=9)
#plt.annotate('No CMC', xy=(3, 8), xytext=(4, 9,),
             #arrowprops=dict(facecolor='k', shrink=0.01), )
             
plt.plot(ps, vp, 'r--') #label= r'fit: $V_{max}$=%5.3f, K$_M$=%5.3f' % tuple(p))
#plt.plot(ps, vpp, 'r-', label= r'fit: $V_{max}$=%5.3f, K$_M$=%5.3f' % tuple(pp))
    #plt.annotate('CMC (0.1%)', xy=(5, 2.8), xytext=(6, 4,),
             #arrowprops=dict(facecolor='g', shrink=0.01), )
#plt.plot(s, theo, 'r-')

plt.xlabel( '[DTFCys2] (' r'$\mu M$' ')', fontsize=24, fontweight='bold')
plt.ylabel( r'$\nu_o$'' (' r'$\Delta F/min$' ')', fontsize=24, fontweight='bold')
#plt.title('PDI-mediated FITC denitrosation', fontsize=16, fontweight='bold')
plt.grid(True)
#plt.savefig("PlaterReaderCase.png")
#plt.legend()
plt.show()
