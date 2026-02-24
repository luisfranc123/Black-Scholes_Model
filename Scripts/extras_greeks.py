def greeks(d1, d2, S, K, r, q, sigma, T):

  """
  This function calculates the Extra Greeks corresponding to
  the Black-Scholes Option estimates model.

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
  float: Greeks (Extras)

  """

#Call delta:
  delta_call = [np.exp(-q*T)*norm.cdf(d1[i]) for i in range(len(d1))]
#Put delta
  delta_put = [np.exp(-q*T)*norm.cdf(d1[i]) - np.exp(-q*T) \
              for i in range(len(d1))]

# Gamma
  gamma = [(np.exp(-q*T)*norm.pdf(d1[i]))/(S[i]*sigma[i]*np.sqrt(T)) \
          for i in range(len(d1))]
# Vega per 1% vol
  vega = [S[i]*np.exp(-q*T)*norm.pdf(d1[i])*np.sqrt(T)*0.01 \
          for i in range(len(S))]

# Theta call per year
  theta_call_year = [-(S[i]*np.exp(-q*T)*norm.pdf(d1[i])*(sigma[i]))/(2*np.sqrt(T)) - \
             r*K*np.exp(-r*T)*norm.cdf(d2[i]) + \
             q*S[i]*np.exp(-q*T)*norm.cdf(d1[i]) for i in range(len(d1))]

# Theta put per year
  theta_put_year = [-(S[i]*np.exp(-q*T)*norm.pdf(d1[i])*(sigma[i]))/(2*np.sqrt(T)) + \
             r*K*np.exp(-r*T)*norm.cdf(-d2[i]) - \
             q*S[i]*np.exp(-q*T)*norm.cdf(-d1[i]) for i in range(len(d1))]

# Theta call per day
  theta_call_day = [(1/days_year)*val for val in theta_call_year]
# Theta put per day
  theta_put_day = [(1/days_year)*val for val in theta_put_year]

#Rho call (per 1% rate)
  rho_call = [K*T*np.exp(-r*T)*norm.cdf(d2[i])*0.01 \
            for i in range(len(d1))]
#Rho put (per 1% rate)
  rho_put = [-K*T*np.exp(-r*T)*norm.cdf(-d2[i])*0.01 \
            for i in range(len(d1))]

  return delta_call, delta_put, gamma, vega, theta_call_year, theta_put_year,\
         theta_call_day, theta_put_day, rho_call, rho_put

# Calculate greeks and extras
greeks_results = []
for i in range(len(spot_price)):
  greek_values = greeks(
            d1_list[i], d2_list[i], spot_price[i], K, r, q, sigma_vector[i], T
        )
  greeks_results.append(greek_values)

  # Unpack greeks results
  call_delta = [g[0] for g in greeks_results]
  put_delta = [g[1] for g in greeks_results]
  gamma = [g[2] for g in greeks_results]
  vega = [g[3] for g in greeks_results]
  call_theta_year = [g[4] for g in greeks_results]
  put_theta_year = [g[5] for g in greeks_results]
  call_theta_day = [g[6] for g in greeks_results]
  put_theta_day = [g[7] for g in greeks_results]
  call_rho = [g[8] for g in greeks_results]
  put_rho = [g[9] for g in greeks_results]
