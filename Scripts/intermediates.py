import numpy as np
# define empty vectors to store d1 and d2 computations.
def intermediates(S, K, r, q, sigma, T):
  """
  Function that calculates intermediates.
  Args:
    - S_values: vector containing spot prices depending on percentage basis
    - K: Strike price (USD)
    - r: risk free rate r
    - q: Dividend yield q
    - sigma_inputs = vector containing volatility increments
    - T: time to expiry

  Returns:
    d1 and d2
  """
  d1 = [(np.log(S[i]/K) + (r - q + 0.5*sigma[i]**2)*T) / \
               (sigma[i]*np.sqrt(T)) for i in range(len(S))]

  d2 = [d1[i] - sigma[i]*np.sqrt(T) for i in range(len(d1))]

  return d1, d2
