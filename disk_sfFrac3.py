from __future__ import print_function
import scipy.stats.distributions as dist
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstwobign
import math

execfile('/1/home/idroberts/prog.py')

f0 = open('bins_pass_w_lx_mh13.dat', 'w')
f1 = open('bins_pass_w_lx_mh13.5.dat', 'w')
f2 = open('bins_pass_w_lx_mh14.dat', 'w')
f3 = open('bins_pass_w_lx_mh14.5.dat', 'w')

m0, ssfr0, n0, w0 = np.loadtxt('sloanX_lxw_mh13.dat', usecols=(0,2,3,8), unpack=True)
m1, ssfr1, n1, w1 = np.loadtxt('sloanX_lxs_mh13.dat', usecols=(0,2,3,8), unpack=True)

m2, ssfr2, n2, w2 = np.loadtxt('sloanX_lxw_mh13.5.dat', usecols=(0,2,3,8), unpack=True)
m3, ssfr3, n3, w3 = np.loadtxt('sloanX_lxs_mh13.5.dat', usecols=(0,2,3,8), unpack=True)

m4, ssfr4, n4, w4 = np.loadtxt('sloanX_lxw_mh14.dat', usecols=(0,2,3,8), unpack=True)
m5, ssfr5, n5, w5 = np.loadtxt('sloanX_lxs_mh14.dat', usecols=(0,2,3,8), unpack=True)

m6, ssfr6, n6, w6 = np.loadtxt('sloanX_lxw_mh14.5.dat', usecols=(0,2,3,8), unpack=True)
m7, ssfr7, n7, w7 = np.loadtxt('sloanX_lxs_mh14.5.dat', usecols=(0,2,3,8), unpack=True)

c = 0.683
cut = -11
ncut = 1.5
bins1 = [9,9.75,10.2,10.5,20]
bins_ = np.arange(9, 11, 0.3)
bins = np.append(bins_, 20)
#bins = [9,9.5,9.8,10.1,10.4,10.7,20]

x0, y0, eu0, el0, W0 = sfFrac_w(m0, ssfr0, w0, bins, cut, c, f0)
x1, y1, eu1, el1, W1 = sfFrac_w(m1, ssfr1, w1, bins, cut, c, f0)

x2, y2, eu2, el2, W2 = sfFrac_w(m2, ssfr2, w2, bins, cut, c, f1)
x3, y3, eu3, el3, W3 = sfFrac_w(m3, ssfr3, w3, bins, cut, c, f1)

x4, y4, eu4, el4, W4 = sfFrac_w(m4, ssfr4, w4, bins, cut, c, f2)
x5, y5, eu5, el5, W5 = sfFrac_w(m5, ssfr5, w5, bins, cut, c, f2)

x6, y6, eu6, el6, W6 = sfFrac_w(m6, ssfr6, w6, bins, cut, c, f3)
x7, y7, eu7, el7, W7 = sfFrac_w(m7, ssfr7, w7, bins, cut, c, f3)

x00, y00, eu00, el00, W00 = diskFrac_w(m0, n0, w0, bins, ncut, c, f0)
x11, y11, eu11, el11, W11 = diskFrac_w(m1, n1, w1, bins, ncut, c, f0)

x22, y22, eu22, el22, W22 = diskFrac_w(m2, n2, w2, bins, ncut, c, f1)
x33, y33, eu33, el33, W33 = diskFrac_w(m3, n3, w3, bins, ncut, c, f1)

x44, y44, eu44, el44, W44 = diskFrac_w(m4, n4, w4, bins, ncut, c, f2)
x55, y55, eu55, el55, W55 = diskFrac_w(m5, n5, w5, bins, ncut, c, f2)

x66, y66, eu66, el66, W66 = diskFrac_w(m6, n6, w6, bins, ncut, c, f3)
x77, y77, eu77, el77, W77 = diskFrac_w(m7, n7, w7, bins, ncut, c, f3)

f4 = open('sf_lx2_mh13_vals.dat', 'w')
for i in range(0, len(x0)):
    print(x0[i], y0[i], eu0[i], el0[i], y1[i], eu1[i], el1[i], file = f4)
f5 = open('sf_lx2_mh13.5_vals.dat', 'w')
for i in range(0, len(x2)):
    print(x2[i], y2[i], eu2[i], el2[i], y3[i], eu3[i], el3[i], file = f5)
f6 = open('sf_lx2_mh14_vals.dat', 'w')
for i in range(0, len(x4)):
    print(x4[i], y4[i], eu4[i], el4[i], y5[i], eu5[i], el5[i], file = f6)
f7 = open('sf_lx2_mh14.5_vals.dat', 'w')
for i in range(0, len(x6)):
    print(x6[i], y6[i], eu6[i], el6[i], y7[i], eu7[i], el7[i], file = f7)

f8 = open('df_lx2_mh13_vals.dat', 'w')
for i in range(0, len(x00)):
    print(x00[i], y00[i], eu00[i], el00[i], y11[i], eu11[i], el11[i], file = f8)
f9 = open('df_lx2_mh13.5_vals.dat', 'w')
for i in range(0, len(x22)):
    print(x22[i], y22[i], eu22[i], el22[i], y33[i], eu33[i], el33[i], file = f9)
f10 = open('df_lx2_mh14_vals.dat', 'w')
for i in range(0, len(x44)):
    print(x44[i], y44[i], eu44[i], el44[i], y55[i], eu55[i], el55[i], file = f10)
f11 = open('df_lx2_mh14.5_vals.dat', 'w')
for i in range(0, len(x66)):
    print(x66[i], y66[i], eu66[i], el66[i], y77[i], eu77[i], el77[i], file = f11)

Xmax = 11
Xmin = 9
Ymax = 1
Ymin = 0

##################################################

plt.rc('font', family='serif')
fig = plt.figure()
fig.subplots_adjust(top=0.85, wspace=0.05, hspace=0.05)

lw = 2
ms = 7
mew = 1.5
elw = 1.5

#fig.text(0.515, 0, 'log M$_{\star}$/M$_{\odot}$', ha='center', va='center', fontsize=28)
#fig.text(0.035, 0.5, 'Fraction', ha='center', va='center', fontsize=28, rotation='vertical')

ax = fig.add_subplot(111)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
ax.set_xlabel('log M$_\star$/M$_\odot$', fontsize=18, labelpad=12)
ax.set_ylabel('Fraction', fontsize=18, labelpad=12)

#f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True, sharex=True)
ax1 = fig.add_subplot(221)

ax1.set_xticks([9,9.5,10,10.5])
ax1.set_yticks([0.1, 0.3, 0.5, 0.7, 0.9])
ax1.set_ylim([Ymin, Ymax])
ax1.set_xlim([Xmin, Xmax])
#plt.tick_params(axis='both', which='major', labelsize=18)

#ax1.errorbar(x0, y0, yerr=[el0,eu0], marker='o', ls='-', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='#2B4F81', lw=lw, ms=ms)

#ax1.errorbar(x1, y1, yerr=[el1,eu1], marker='s', ls='-', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='#A52A2A', lw=lw, ms=ms)

#ax1.errorbar(x00, y00, yerr=[el00,eu00], marker='o', ls='--', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='none', mew=mew, lw=lw, ms=ms)

ax1.errorbar(x11, y11, yerr=[el11,eu11], marker='s', ls='--', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='none', mew=mew, lw=lw, ms=ms)

#ax1.text(9.94, 0.7, 'L$_{\mathbf{X}}$ weak:', color='#2B4F81', fontsize=12, weight='semibold')
#ax1.plot(10.67, 0.72, marker='o', color='#2B4F81', ms=ms, mfc='none', mew=mew, mec='#2B4F81')
#ax1.plot([10.52,10.82], [0.72,0.72], ls='--', color='#2B4F81', lw=lw)
#ax1.text(10.84, 0.7, 'f$_{\mathbf{D}}$', color='#2B4F81', fontsize=12, weight='semibold')
#ax1.plot(10.45, 0.939, marker='o', mfc='none', mec='#2B4F81', mew=mew, ms=ms)
#ax1.plot([10.3,10.6], [0.939,0.939], ls='--', color='#2B4F81', lw=lw)
#ax1.text(10.68, 0.91, 'f$_{\mathbf{D}}$', color='#2B4F81', fontsize=12, weight='semibold')

ax1.text(9.85, 0.8, 'L$_{\mathbf{X}}$ strong:', color='#A52A2A', fontsize=12, weight='semibold')
ax1.plot(10.67, 0.82, marker='s', color='#A52A2A', ms=ms, mfc='none', mew=mew, mec='#A52A2A')
ax1.plot([10.52,10.82], [0.82,0.82], ls='--', color='#A52A2A', lw=lw)
ax1.text(10.84, 0.8, 'f$_{\mathbf{D}}$', color='#A52A2A', fontsize=12, weight='semibold')
#ax1.plot(10.45, 0.839, marker='s', mfc='none', mec='#A52A2A', mew=mew, ms=ms)
#ax1.plot([10.3,10.6], [0.839,0.839], ls='--', color='#A52A2A', lw=lw)
#ax1.text(10.68, 0.81, 'f$_{\mathbf{D}}$', color='#A52A2A', fontsize=12, weight='semibold')

ax1.text(9.1, 0.9, '13 < log M$_{\mathbf{H}}$ < 13.5', color='k', fontsize=12, weight='semibold')
ax1.text(9.1, 0.07, '(a)', fontsize=12, weight='semibold')

ax2 = fig.add_subplot(222, sharex=ax1, sharey=ax1)

ax2.set_ylim([Ymin, Ymax])
ax2.set_xlim([Xmin, Xmax])
#plt.tick_params(axis='both', which='major', labelsize=18)

#ax2.errorbar(x2, y2, yerr=[el2,eu2], marker='o', linestyle='solid', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='#2B4F81', lw=lw, ms=ms)

#ax2.errorbar(x3, y3, yerr=[el3,eu3], marker='s', linestyle='solid', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='#A52A2A', lw=lw, ms=ms)

#ax2.errorbar(x22, y22, yerr=[el22,eu22], marker='o', linestyle='dashed', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='none', mew=mew, lw=lw, ms=ms)

ax2.errorbar(x33, y33, yerr=[el33,eu33], marker='s', linestyle='dashed', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='none', mew=mew, lw=lw, ms=ms)

ax2.text(9.1, 0.9, '13.5 < log M$_{\mathbf{H}}$ < 14', color='k', fontsize=12, weight='semibold')
ax2.text(9.1, 0.07, '(b)', fontsize=12, weight='semibold')

ax3 = fig.add_subplot(223, sharex=ax1, sharey=ax1)

ax3.set_ylim([Ymin, Ymax])
ax3.set_xlim([Xmin, Xmax])
#plt.tick_params(axis='both', which='major', labelsize=18)

#ax3.errorbar(x4, y4, yerr=[el4,eu4], marker='o', linestyle='solid', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='#2B4F81', lw=lw, ms=ms)

#ax3.errorbar(x5, y5, yerr=[el5,eu5], marker='s', linestyle='solid', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='#A52A2A', lw=lw, ms=ms)

#ax3.errorbar(x44, y44, yerr=[el44,eu44], marker='o', linestyle='dashed', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='none', mew=mew, lw=lw, ms=ms)

ax3.errorbar(x55, y55, yerr=[el55,eu55], marker='s', linestyle='dashed', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='none', mew=mew, lw=lw, ms=ms)

ax3.text(9.1, 0.9, '14 < log M$_{\mathbf{H}}$ < 14.5', color='k', fontsize=12, weight='semibold')
plt.text(9.1, 0.07, '(c)', fontsize=12, weight='semibold')

ax4 = fig.add_subplot(224, sharex=ax1, sharey=ax1)

ax4.set_ylim([Ymin, Ymax])
ax4.set_xlim([Xmin, Xmax])
#plt.tick_params(axis='both', which='major', labelsize=18)

#ax4.errorbar(x6, y6, yerr=[el6,eu6], marker='o', linestyle='solid', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='#2B4F81', lw=lw, ms=ms)

#ax4.errorbar(x7, y7, yerr=[el7,eu7], marker='s', linestyle='solid', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='#A52A2A', lw=lw, ms=ms)

#ax4.errorbar(x66, y66, yerr=[el66,eu66], marker='o', linestyle='dashed', color='#2B4F81', elinewidth=elw, capsize=0, mec='#2B4F81', mfc='none', mew=mew, lw=lw, ms=ms)

ax4.errorbar(x77, y77, yerr=[el77,eu77], marker='s', linestyle='dashed', color='#A52A2A', elinewidth=elw, capsize=0, mec='#A52A2A', mfc='none', mew=mew, lw=lw, ms=ms)

ax4.text(9.1, 0.9, '14.5 < log M$_{\mathbf{H}}$ < 15', color='k', fontsize=12, weight='semibold')
ax4.text(9.1, 0.07, '(d)', fontsize=12, weight='semibold')

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

fig.savefig('disk_sfFrac3.png', dpi=600, bbox_inches='tight')
#plt.show()
