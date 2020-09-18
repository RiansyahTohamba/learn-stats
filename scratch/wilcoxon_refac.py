import warnings
from .stats import find_repeats, _contains_nan
from . import distributions
from collections import namedtuple
import numpy as np
from scipy import stats
from numpy import (isscalar, r_, log, around, unique, asarray,
                   zeros, arange, sort, amin, amax, any, atleast_1d,
                   sqrt, ceil, floor, array, compress,
                   pi, exp, ravel, count_nonzero, sin, cos, arctan2, hypot)

class Wilcoxon:
    def __init__(self):
        pass

    def r_plus(self):
        count_r_plus = 1
        return count_r_plus

    def r_minus(self):
        count_r_plus = 2
        return count_r_plus

    def first_validation(self,zero_method,alternative):
        if zero_method not in ["wilcox", "pratt", "zsplit"]:
            raise ValueError("Zero method should be either 'wilcox' "
                             "or 'pratt' or 'zsplit'")

        if alternative not in ["two-sided", "less", "greater"]:
            raise ValueError("Alternative must be either 'two-sided', "
                             "'greater' or 'less'")


    WilcoxonResult = namedtuple('WilcoxonResult', ('statistic', 'pvalue'))

    def wilcoxon(self,x, y=None, zero_method="wilcox", correction=False,
                 alternative="two-sided"):

        self.first_validation(zero_method, alternative)
        distr = self.check_y(y)

        n_zero = self.zero_wilcox_pratt(distr, zero_method)

        if zero_method == "wilcox":
            # Keep all non-zero differences
            distr = compress(np.not_equal(distr, 0), distr, axis=-1)

        count = len(distr)
        if count < 10:
            warnings.warn("Sample size too small for normal approximation.")

        rankdata = stats.rankdata(abs(distr))
        r_plus = np.sum((distr > 0) * rankdata, axis=0)
        r_minus = np.sum((distr < 0) * rankdata, axis=0)

        if zero_method == "zsplit":
            r_zero = np.sum((distr == 0) * rankdata, axis=0)
            r_plus += r_zero / 2.
            r_minus += r_zero / 2.

        T_val = self.set_t_val(alternative, r_minus, r_plus)

        mn = count * (count + 1.) * 0.25
        se = count * (count + 1.) * (2. * count + 1.)

        mn, rankdata, se = self.zero_method_pratt(distr, mn, n_zero, rankdata, se, zero_method)

        replist, repnum = find_repeats(rankdata)
        if repnum.size != 0:
            # Correction for repeated elements.
            se -= 0.5 * (repnum * (repnum * repnum - 1)).sum()

        se = sqrt(se / 24)

        distr = self.set_distr(T_val, alternative, correction, distr, mn)

        # compute statistic and p-value using normal approximation
        z_stat = (T_val - mn - distr) / se
        prob = self.count_p_val(alternative, z_stat)

        return WilcoxonResult(T_val, prob)

    def set_distr(self, T_val, alternative, correction, distr, mn):
        # apply continuity correction if applicable
        distr = 0
        if correction:
            if alternative == "two-sided":
                distr = 0.5 * np.sign(T_val - mn)
            elif alternative == "less":
                distr = -0.5
            else:
                distr = 0.5
        return distr

    def set_t_val(self, alternative, r_minus, r_plus):
        # return min for two-sided test, but r_plus for one-sided test
        # the literature is not consistent here
        # r_plus is more informative since r_plus + r_minus = count*(count+1)/2,
        # i.e. the sum of the ranks, so r_minus and the min can be inferred
        # (If alternative='pratt', r_plus + r_minus = count*(count+1)/2 - r_zero.)
        # [3] uses the r_plus for the one-sided test, keep min for two-sided test
        # to keep backwards compatibility
        if alternative == "two-sided":
            T_val = min(r_plus, r_minus)
        else:
            T_val = r_plus
        return T_val

    def zero_method_pratt(self, distr, mn, n_zero, rankdata, se, zero_method):
        if zero_method == "pratt":
            rankdata = rankdata[distr != 0]
            # normal approximation needs to be adjusted, see Cureton (1967)
            mn -= n_zero * (n_zero + 1.) * 0.25
            se -= n_zero * (n_zero + 1.) * (2. * n_zero + 1.)
        return mn, rankdata, se

    def count_p_val(self, alternative, z_stat):
        if alternative == "two-sided":
            prob = 2. * distributions.norm.sf(abs(z_stat))
        elif alternative == "greater":
            # large T_val = r_plus indicates x is greater than y; i.e.
            # accept alternative in that case and return small p-value (sf)
            prob = distributions.norm.sf(z_stat)
        else:
            prob = distributions.norm.cdf(z_stat)
        return prob

    def zero_wilcox_pratt(self, distr, zero_method):
        if zero_method in ["wilcox", "pratt"]:
            n_zero = np.sum(distr == 0, axis=0)
            if n_zero == len(distr):
                raise ValueError("zero_method 'wilcox' and 'pratt' do not work if "
                                 "the x - y is zero for all elements.")
        return n_zero

    def check_y(self, y):
        if y is None:
            distr = asarray(x)
            if distr.ndim > 1:
                raise ValueError('Sample x must be one-dimensional.')
        else:
            x, y = map(asarray, (x, y))
            if x.ndim > 1 or y.ndim > 1:
                raise ValueError('Samples x and y must be one-dimensional.')
            if len(x) != len(y):
                raise ValueError('The samples x and y must have the same length.')
            distr = x - y
        return distr
