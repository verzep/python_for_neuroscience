import numpy as np
import pandas

def round_to_nearest(val, base=0.5):
    """
    Given a value, or an array of values, round them to the nearest multiple of :arg:base
    """
    if isinstance(val, int) or isinstance(val, float):
        val = [val]
    return np.array([base * round(e/base) for e in val])

def find_local_maxima(array, tolerance=0.5):
    """
    Given an array of voltage traces, find all the local maxima
    This is similar to scipy.signal.find_peaks
    """
    return np.where(
        np.diff(
            np.sign(
                np.gradient(
                    round_to_nearest(array, tolerance)))))[0]

def count_spikes(spike_times, max_interval=15):
    """
    Given an array of spike times, this method clusters them based on a maximum allowed time interval.

    Args:
        spike_times: an array of spike_times
        max_interval: maximum allowed ISI such that spikes within this range are clustered together
    
    Returns:
        spike_counts (dict): a dictionary mapping the onset of the first spike to the amount of spikes that follow with a max interspike interval of :arg:max_interval
    """
    spike_counts = {}
    for i in range(len(spike_times)):
        start_t = spike_times[i]
        n_spikes = 1
        while i < len(spike_times) - 1 and spike_times[i+1] < spike_times[i] + max_interval:
            n_spikes +=1
            i += 1
        spike_counts[start_t] = n_spikes
    return spike_counts