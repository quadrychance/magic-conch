import numpy as np
from scipy import (special, stats)

from astropy.io import fits

def get_j_rv(dataframe):
    jv = []
    for i in range(len(dataframe)):
        jv.append(np.sqrt((2/np.pi) * dataframe["t"].iloc[i] * (dataframe["RV jitter"].iloc[i]**2 - 0.11**2)))
    jv_data = np.array(jv)
    return jv_data




#y =binaries['RV jitter'][:N]#get_j_rv(binaries)[:N]
# Where j_rv is defined as:
#   j_rv = np.sqrt((2/np.pi) * gaia["rv_nb_transits"][()] * (gaia["radial_velocity_error"][()]**2 - 0.11**2))


def ln_likelihood_single(params, y):
    theta, mu_single, sigma_single, sigma_multiple = params
    lpdf_single = stats.norm.logpdf(
        y,
        loc=mu_single,
        scale=sigma_single
    )
    return np.log(theta) + lpdf_single


def get_mu_multiple(mu_single, sigma_single, sigma_multiple):
    SCALAR = 1 # MAGIC
    return np.log(np.array(mu_single) + SCALAR * np.array(sigma_single)) + np.array(sigma_multiple)**2


def ln_likelihood_multiple(params, y):
    theta, mu_single, sigma_single, sigma_multiple = params

    mu_multiple = get_mu_multiple(mu_single, sigma_single, sigma_multiple)

    lpdf_multiple = stats.lognorm.logpdf(
        y,
        loc=0,
        scale=np.exp(mu_multiple),
        s=sigma_multiple
    )

    lpdf = np.log(1 - theta) + lpdf_multiple

    # Truncated log normal distribution.
    M = 2 # MAGIC
    weight = (1/sigma_single) * np.log(np.sqrt(2 * np.pi * sigma_single) * np.exp(0.5 * M**2) - 1)
    sigmoid = 1/(1 + np.exp(-weight * (y - mu_single)))
    return lpdf + np.log(sigmoid)


def calculate_rv_p_single(p_theta, p_mu_single, p_sigma_single, p_sigma_multiple, y):

    params = (p_theta, p_mu_single, p_sigma_single, p_sigma_multiple)
    lpdf_single = ln_likelihood_single(params, y)
    lpdf_multiple = ln_likelihood_multiple(params, y)

    lpdf = np.array([lpdf_single, lpdf_multiple])

    p_single = np.exp(lpdf - special.logsumexp(lpdf, axis=0))[0]

    return p_single
