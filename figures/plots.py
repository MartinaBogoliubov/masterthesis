import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#
#
#
def arrowed_spines(ax=None, arrow_length=20, labels=('', ''), arrowprops=None):
	xlabel, ylabel = labels
	if ax is None:
		ax = plt.gca()
	if arrowprops is None:
		arrowprops = dict(arrowstyle='<|-', facecolor='black')

	for i, spine in enumerate(['left', 'bottom']):
		# Set up the annotation parameters
		t = ax.spines[spine].get_transform()
		xy, xycoords = [1, 0], ('axes fraction', t)
		xytext, textcoords = [arrow_length, 0], ('offset points', t)
		ha, va = 'left', 'bottom'

		# If axis is reversed, draw the arrow the other way
		top, bottom = ax.spines[spine].axis.get_view_interval()
		if top < bottom:
			xy[0] = 0
			xytext[0] *= -1
			ha, va = 'right', 'top'

		if spine is 'bottom':
			xarrow = ax.annotate(xlabel, xy, xycoords=xycoords, xytext=xytext, 
                        textcoords=textcoords, ha=ha, va='center',
                        arrowprops=arrowprops)
		else:
			yarrow = ax.annotate(ylabel, xy[::-1], xycoords=xycoords[::-1], xytext=xytext[::-1], textcoords=textcoords[::-1], ha='center', va=va, arrowprops=arrowprops)
	return xarrow, yarrow
#
#
#
def f(x):
	return np.exp(x) / (x * (np.exp(x))**2) * (np.pi - (2 * r * beta / (gamma * x)) / (1 + (r * beta / (gamma * x))**2) - 2 * np.arctan(r * beta / (gamma * x)))
#
#
# Data for plotting x-dependence
x = np.arange(0.0, 6.0, 0.001)

# Setting parameters
beta = 1
gamma = 1
r = 0.1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,f(x),linewidth = 2.0)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

arrowed_spines(ax)

plt.ylim((0,7))

ax.set(xlabel = 'x (arbitrary units)', ylabel = 'f(x)', title = 'x-dependence of the integrand')

fig.savefig("x-dependence.pdf")
