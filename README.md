Please correct this README.md section from a GitHub repository to make it look prettier. ##**Tail Risk Black-Scholes Option Estimates**
---

The present project aims to calculate option estimates employing the Black-Scholes model to illustrate different scenarios relying on volatility, time of expiry, dividend yield percentage, and percentage basis change.

*It is important to notice that both rates and volatility are annualized*.

####**1. Define Constants**
---

In this section, we define the initial parameters that the model is going to work with.

- Spot Price ($S$)
- Strike Price ($K$)
- Risk-free rate ($r$ - annual, %)
- Dividend yield ($q$ - annual, %)
- Volatility ($\sigma$ - annual, %)
- Time to expiry T (years) -- vector of multiple values


####**2. Calculate intermediates $d_1$ and $d_2$**
---

$$d_1 = \frac{ln(\frac{S}{K}) + ((r-q) + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}}$$
\
$$d_2 = d_1 - \sigma\sqrt{T}$$

####**3. Calculate Outputs (Call Price and Put Price)**
---

$$C_{call} = Se^{-qT}N(d_1) - Ke^{-rT}N(d_2)$$
\
$$P_{put} = Ke^{-rT}N(-d_2) - Se^{-qT}N(-d_1)$$

####**4. Calculate Extras (Greeks)**
---

Key Black-Scholes Greeks and Their Functions:

- Delta ($\Delta$): Measures the change in option price for a  change in the underlying asset. It also indicates the theoretical hedge ratio (number of shares needed for a delta-neutral position).

- Gamma ($\Gamma$): Measures the rate of change in Delta for a change in the underlying price. It indicates how often a portfolio needs to be rebalanced to maintain a delta-neutral hedge.

- Vega ($V$): Measures sensitivity to implied volatility. It shows the expected change in option price for a change in volatility.

- Theta ($\theta$): Measures the rate of time decay, showing how much value the option loses daily as it approaches expiration.

- Rho ($\rho$): Measures sensitivity to the risk-free interest rate, indicating the change in option price for a change in interest rates.

$$\Delta_{call} = e^{-qt}N(d_1)$$
\
$$\Delta_{put} = e^{-qt}N(d_1) - e^{-qt}$$
\
$$\Gamma = \frac{e^{-qt}\phi(d_1)}{S\sigma\sqrt{t}}$$
\
$$\nu_{1\%} = e^{-qt}\phi(d_1)\sqrt{t}\space0.01$$
\
$$\Theta_{call_{year}} = \frac{-Se^{-qt}\phi(d_1)\sigma}{2\sqrt{t}} - rKe^{-rt}N(d_2) + qSe^{-qt}N(d_1)$$
\
$$\Theta_{put_{year}} = \frac{-Se^{-qt}\phi(d_1)\sigma}{2\sqrt{t}} + rKe^{-rt}N(-d_2) - qSe^{-qt}N(-d_1)$$
\
$$\rho_{call}(per\space{1\%}\space{rate}) = Kte^{-rt}N(d_2)\cdot0.01$$
\
$$\rho_{call}(per\space{1\%}\space{rate}) = -Kte^{-rt}N(-d_2)\cdot0.01$$

####**5. Scenarios (with dividend yield)**
---

####**6. Scenarios Visualization**
---
