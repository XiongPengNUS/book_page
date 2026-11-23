import numpy as np


def estimate_return(data):
    """
    The estimate_return function estimate the mean and covariance
    matrix of the year rate of return based on the given weekly
    prices of stocks.
    
    Parameters
    ----------
    data : Pandas data frame
        It is a dataset of weekly stock prices. 
    
    Returns
    -------
    mean : Pandas series
        The mean values of the yearly rates of returns.
    cov : Pandas data frame
        The covariance matrix of the year rates of returns. 
        
    Notes:
    ------
    It is assumed that there are 52 weeks in a week. 
    """
    
    factor = 52
    
    wk_log = np.log(data).diff()
    
    mu_log = wk_log.mean() * factor
    Sigma_log = wk_log.cov() * factor
    
    ratio = np.exp(mu_log + (1/2)*np.diag(Sigma_log))
    mean = ratio - 1
    cov = np.outer(ratio, ratio) * (np.exp(Sigma_log) - 1)
    
    return mean, cov
