### First Plot ###

# Read in data
from astropy.io import ascii

data_A = ascii.read('flux_vs_time_A.dat', names=['Time', 'Flux_pcnt_diff', 'Flux_err', 'Flux_linear_fit'])
data_C = ascii.read('flux_vs_time_C.dat', names=['Time', 'Flux_pcnt_diff', 'Flux_err', 'Flux_linear_fit'])

import matplotlib.pyplot as pyplot
#import numpy

# Scatter plots
figure, ax = pyplot.subplots()
ax.scatter(data_A['Time'], data_A['Flux_pcnt_diff'], c='blue')
ax.scatter(data_C['Time'], data_C['Flux_pcnt_diff'], c='red')
figure.show()

# Add axis labels
ax.set_xlabel('Time [MJD]', fontsize=20)
ax.set_ylabel('Flux Diff [%]', fontsize=20)
figure.show()

# Save the figure

figure.savefig('flux_vs_time_1.pdf')


### Markers, Lines, and Legends ###

# Change shapes and sizes and transparency
ax.clear()
ax.scatter(data_A['Time'], data_A['Flux_pcnt_diff'], c='blue', marker='x', s=30, alpha=0.75)
ax.scatter(data_C['Time'], data_C['Flux_pcnt_diff'], c='red', marker='d', s=30, alpha=0.75)
ax.set_xlabel('Time [MJD]', fontsize=20)
ax.set_ylabel('Flux Diff [%]', fontsize=20)
figure.show()

# Add legend
ax.scatter(data_A['Time'], data_A['Flux_pcnt_diff'], c='blue', marker='x', s=30, alpha=0.75, label='Amp A')
ax.scatter(data_C['Time'], data_C['Flux_pcnt_diff'], c='red', marker='d', s=30, alpha=0.75, label='Amp C')
ax.legend(loc='best', scatterpoints=1)
figure.show()

# Over plot line
ax.plot(data_A['Time'], data_A['Flux_linear_fit'], c='blue', ls='-.', linewidth=2, label='Amp A Fit')
ax.plot(data_C['Time'], data_C['Flux_linear_fit'], c='red', ls=':', linewidth=2, label='Amp C Fit')
ax.legend(loc='best', scatterpoints=1)
figure.show()

# Add vertical and horizonal lines
ax.axhline(0.0, color='k', ls='--', linewidth=1)  #horizonal line at 0.0
ax.axvline(56250.0, color='green', ls='-', linewidth=2)  #vertical line at 55800.0
figure.show()

# Save the figure

figure.savefig('flux_vs_time_2.pdf')


### Error Bars ###
ax.clear()
ax.scatter(data_A['Time'], data_A['Flux_pcnt_diff'], c='blue', s=10)
ax.errorbar(data_A['Time'], data_A['Flux_pcnt_diff'], yerr=data_A['Flux_err'], c='k', marker=None, ls='None')
figure.show()


### Change MJD to day-month-year###
from astropy.time import Time
time_MJD = [float(item.get_text()) for item in ax.get_xticklabels()]
time_convert = Time(time_MJD, format='mjd', scale='utc')
time_ymd_long = time_convert.iso
time_ymd_short = []
for date in time_ymd_long:
    time_ymd_short.append(date.split(' ')[0])

ax.set_xticklabels(time_ymd_short)
ax.set_xlabel('Time', fontsize=20)
ax.set_ylabel('Flux Diff [%]', fontsize=20)
figure.show()

# Save the figure

figure.savefig('flux_vs_time_3.pdf')


### Side-by-Side Plots ###

figure = pyplot.figure(figsize = (10,10))

ax1 = pyplot.subplot(211, title='Amp A')
ax1.scatter(data_A['Time'], data_A['Flux_pcnt_diff'], c='blue')

# Make top plot's axis invisible
pyplot.setp(ax1.get_xticklabels(), visible=False)

# Force second plot's axis to be identical to first plot's
ax2 = pyplot.subplot(212, title='Amp C', sharex=ax1, sharey=ax1)
ax2.scatter(data_C['Time'], data_C['Flux_pcnt_diff'], c='red')

# Set labels
ax1.set_ylabel('Flux Diff [%]', fontsize=15)
ax2.set_ylabel('Flux Diff [%]', fontsize=15)
ax2.set_xlabel('Time [MJD]', fontsize=15)

figure.show()

figure.savefig('flux_vs_time_4.pdf')


### Image Plot of FITS file ###

import astropy.io.fits as fits

image = fits.open('ibsa01fpq_flt.fits')

sci_data = image['sci'].data

pyplot.clf()
pyplot.gray()

pyplot.imshow(sci_data, vmin=0, vmax=60)
image.close()

pyplot.title('M51', fontsize=20)
pyplot.xlabel('x pixels', fontsize=15)
pyplot.ylabel('y pixels', fontsize=15)

image.close()

pyplot.annotate('star', xy=(640,810),  xytext=(520,770), color='white', arrowprops=dict(facecolor='white', width=3.5))

pyplot.savefig('M51.pdf')



'''
# using pylab
    
import pylab
    
fig = pylab.figure()

#Scatter plots
plot = pylab.scatter(data['Time'], data['Flux_pcnt_diff_A'], c='blue')
plot = pylab.scatter(data['Time'], data['Flux_pcnt_diff_C'], c='red')

#Over plot line
plot = pylab.plot(data['Time'], data['Flux_linear_fit_A'], c='blue')
plot = pylab.plot(data['Time'], data['Flux_linear_fit_C'], c='red')

#Add labels
plot = pylab.xlabel('Time (MJD)')
plot = pylab.ylabel('Flux Diff (%)')

'''