def sf(self, x, *args, **kwds):    
    args, loc, scale = self._parse_args(*args, **kwds)
    _a, _b = self._get_support(*args)
    x, loc, scale = map(asarray, (x, loc, scale))
    args = tuple(map(asarray, args))
    dtyp = np.find_common_type([x.dtype, np.float64], [])
    x = np.asarray((x - loc)/scale, dtype=dtyp)
    cond0 = self._argcheck(*args) & (scale > 0)
    cond1 = self._open_support_mask(x, *args) & (scale > 0)
    cond2 = cond0 & (x <= _a)
    cond = cond0 & cond1
    output = zeros(shape(cond), dtyp)
    place(output, (1-cond0)+np.isnan(x), self.badvalue)
    place(output, cond2, 1.0)
    if np.any(cond):
        goodargs = argsreduce(cond, *((x,)+args))
        place(output, cond, self._sf(*goodargs))
    if output.ndim == 0:
        return output[()]
    return output

"""
        Survival function (1 - `cdf`) at x of the given RV.

        Parameters
        ----------
        x : array_like
            quantiles
        arg1, arg2, arg3,... : array_like
            The shape parameter(s) for the distribution (see docstring of the
            instance object for more information)
        loc : array_like, optional
            location parameter (default=0)
        scale : array_like, optional
            scale parameter (default=1)

        Returns
        -------
        sf : array_like
            Survival function evaluated at x

        """