#!/usr/bin/env python


from . import butter
from . import wavelet


__all__ = ['butter', 'wavelet']


def filt_from_kwargs(**kwargs):
    method = kwargs.pop('method')
    if method == 'butter':
        flow = kwargs['low']
        fhigh = kwargs['high']
        sr = kwargs['samprate']
        order = kwargs['order']
        return lambda x: butter.filt(x, flow, fhigh, sr, order)
    elif method == 'wavelet':
        minlvl = kwargs['minlvl']
        maxlvl = kwargs['maxlvl']
        wtype = kwargs['wavelet']
        mode = kwargs['mode']
        return lambda x: wavelet.filt(x, maxlvl, wtype, mode, minlvl)
    else:
        raise ValueError('Unknown filt method: %s' % method)


def filt_from_config(config, section='filter'):
    kwargs = {}
    for k in ('method', 'low', 'high', 'samprate', 'order',
              'minlvl', 'maxlvl', 'wavelet', 'mode'):
        if config.has_option(section, k):
            kwargs[k] = config.get(section, k)
    return filt_from_kwargs(**kwargs)
