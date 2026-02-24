from scipy.stats import norm
def call_put_prices(d1, d2, S, K, r, q, sigma, T):

  """
  Function that calculates call and put prices.
  Args:
    - d1: intermediate d1
    - d2: intermediate d2
    - S_values: vector containing spot prices depending on percentage basis
    - K: Strike price (USD)
    - r: risk free rate r
    - q: Dividend yield q
    - sigma_inputs = vector containing volatility increments
    - T: time to expiry

  Returns:
    call_prices and put_prices
  """

  call_price = [(S[i]*np.exp(-q*T)*norm.cdf(d1[i]) - \
                   K*np.exp(-r*T)*norm.cdf(d2[i])) for i in range(len(d1))]

  put_price = [(K*np.exp(-r*T)*norm.cdf(-d2[i]) - \
                S[i]*np.exp(-q*T)*norm.cdf(-d1[i])) for i in range(len(d1))]

  return call_price, put_price

call_price = call_put_prices(d1, d2, spot_price, K, r, q, sigma_inc, T)[0]
put_price = call_put_prices(d1, d2, spot_price, K, r, q, sigma_inc, T)[1]
