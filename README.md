Tail Risk Black-Scholes Option Estimates

This project calculates option estimates using the Black-Scholes model to illustrate different scenarios based on volatility, time to expiry, dividend yield, and percentage basis changes.

    Note: Both interest rates and volatility are annualized.

1. Define Constants

Initialize the model with the following parameters:

    Spot Price ($S$)

    Strike Price ($K$)

    Risk-free rate ($r$ - annual, %)

    Dividend yield ($q$ - annual, %)

    Volatility ($\sigma$ - annual, %)

    Time to expiry ($T$) — vector of multiple values (in years)

2. Calculate Intermediates $d_1$ and $d_2$
d1=ln⁡(SK)+((r−q)+σ22)TσT
d1​=σT
​ln(KS​)+((r−q)+2σ2​)T​
d2=d1−σT
d2​=d1​−σT
​
3. Calculate Outputs (Call and Put Prices)
Ccall=Se−qTN(d1)−Ke−rTN(d2)
Ccall​=Se−qTN(d1​)−Ke−rTN(d2​)
Pput=Ke−rTN(−d2)−Se−qTN(−d1)
Pput​=Ke−rTN(−d2​)−Se−qTN(−d1​)
4. Calculate Extras (Greeks)

Key Black-Scholes Greeks and their interpretations:
Greek	Symbol	Description
Delta	$\Delta$	Measures change in option price per $1 change in underlying asset. Also indicates the theoretical hedge ratio for a delta-neutral position.
Gamma	$\Gamma$	Measures rate of change in Delta per $1 change in underlying price. Indicates how often a delta-neutral portfolio needs rebalancing.
Vega	$\nu$	Measures sensitivity to a 1% change in implied volatility.
Theta	$\Theta$	Measures time decay — how much value the option loses per day as expiration approaches.
Rho	$\rho$	Measures sensitivity to a 1% change in the risk-free interest rate.
Greeks Formulas
Δcall=e−qtN(d1)
Δcall​=e−qtN(d1​)
Δput=e−qtN(d1)−e−qt
Δput​=e−qtN(d1​)−e−qt
Γ=e−qtϕ(d1)Sσt
Γ=Sσt
​e−qtϕ(d1​)​
ν1%=e−qtϕ(d1)t×0.01
ν1%​=e−qtϕ(d1​)t
​×0.01
Θcall(year)=−Se−qtϕ(d1)σ2t−rKe−rtN(d2)+qSe−qtN(d1)
Θcall(year)​=−2t
​Se−qtϕ(d1​)σ​−rKe−rtN(d2​)+qSe−qtN(d1​)
Θput(year)=−Se−qtϕ(d1)σ2t+rKe−rtN(−d2)−qSe−qtN(−d1)
Θput(year)​=−2t
​Se−qtϕ(d1​)σ​+rKe−rtN(−d2​)−qSe−qtN(−d1​)\rho_{\text{call}}^{\text{(per 1% rate)}} = Kte^{-rt}N(d_2) \times 0.01\rho_{\text{put}}^{\text{(per 1% rate)}} = -Kte^{-rt}N(-d_2) \times 0.01
5. Scenarios (with Dividend Yield)

[Content to be added — describe the scenarios explored, e.g., varying volatility, time to expiry, or dividend yield impacts.]
6. Scenario Visualization

[Content to be added — include plots showing option price behavior under different scenarios, heatmaps of Greeks, or 3D surfaces.]

####**6. Scenarios Visualization**
---
