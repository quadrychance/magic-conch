import numpy as np
import astropy.units as u
import astropy.constants as c
import kepler

G =c.G.to(u.au ** 3 / u.M_sun / u.day ** 2).value
observing_span = 668
def RadialVelocity(m_1,q,e,i,a,phi,w,t,eps):
    m_2=m_1*q


    period = 2*np.pi*np.sqrt((a)**3/(G*(m_1+m_2)))
    n = 2*np.pi/period
    mean_anomaly = n*(t)+phi
    eccentric_anomaly, cos_true_anomaly, sin_true_anomaly = kepler.kepler(mean_anomaly, e)
    k = np.sqrt(G/(m_1+m_2)*a*(1-e**2))
    b = m_2*np.sin(np.deg2rad(i))*(np.cos(w) * cos_true_anomaly - np.sin(w) * sin_true_anomaly + e * np.cos(w))
    rv = k*b
    RV = (rv*(u.AU/u.day)).to(u.km/u.s).value
    #sigma = np.array(np.random.uniform(low=2, high=3,size=1), dtype=float)
    noisy_RV = RV+(eps*np.random.randn(*RV.shape))

    return noisy_RV,k
