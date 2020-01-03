from collections import namedtuple
import numpy as np
from numpy import (isscalar, r_, log, around, unique, asarray,
                   zeros, arange, sort, amin, amax, any, atleast_1d,
                   sqrt, ceil, floor, array, compress,
                   pi, exp, ravel, count_nonzero, sin, cos, arctan2, hypot)
from scipy import stats
WilcoxonResult = namedtuple('WilcoxonResult', ('statistic', 'pvalue'))

def wilcoxon_two_sided(x,zero_method="wilcox"):
	# p-value didapat dari variabel prob
	# return min for two-sided test, but r_plus for one-sided test. 
	d = asarray(x)
	d = compress(np.not_equal(d, 0), d, axis=-1)
	
    if zero_method in ["wilcox", "pratt"]:
        n_zero = np.sum(d == 0, axis=0)
        if n_zero == len(d):
            raise ValueError("zero_method 'wilcox' and 'pratt' do not work if "
                             "the x - y is zero for all elements.")

	count  = len(d)

    r = stats.rankdata(abs(d))
    r_plus = np.sum((d > 0) * r, axis=0)
    r_minus = np.sum((d < 0) * r, axis=0)
	# buat perangkingan
	# summary yg d nya +
	# summary yg d nya -

	# two-sided
	T = min(r_plus, r_minus)


	mn = count * (count + 1.) * 0.25
	se = count * (count + 1.) * (2. * count + 1.)

    replist, repnum = stats.find_repeats(r)
    if repnum.size != 0:
        # Correction for repeated elements.
        se -= 0.5 * (repnum * (repnum * repnum - 1)).sum()

    se = sqrt(se / 24)

    # apply continuity correction if applicable
    d = 0
    if correction:
        if alternative == "two-sided":
            d = 0.5 * np.sign(T - mn)
        elif alternative == "less":
            d = -0.5
        else:
            d = 0.5

	# abs : ignore either - or +
	# nilai T didapatkan dari nilai minimal dari ranking (+) vs ranking (-)
	z  = (T - mn - d) / se
	# survival function
	prob = 2. * stats.distributions.norm.sf(abs(z))
	# nilai T nya tidak perlu dilihat
	return WilcoxonResult(T,prob)

d = [6, 8, 14, 16, 23, 24, 28, 29, 41, -48, 49, 56, 60, -67, 75]	
print(wilcoxon_two_sided(d))