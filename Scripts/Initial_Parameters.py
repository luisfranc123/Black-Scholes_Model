import yfinance as yf
import pandas as pd

def get_spx_level():
    """Get current S&P 500 level using Yahoo Finance"""
    spx = yf.Ticker("^GSPC")  # Yahoo uses ^GSPC for S&P 500
    data = spx.history(period = "1d")
    return data['Close'].iloc[-1]

# Get S&P 500 level
spx_level = get_spx_level()
print(f"The current S&P 500 Index is: {spx_level:.4f}")

# Define the initial parameters:
time_to_expiry = input("Enter the time to expiry T (days) you want to explore: ")
strike_price = input("Enter the Strike Price K (USD): ")
risk_free_rate = input("Enter the annual risk free rate r (%): ")
dividend_yield = input("Enter the annual dividend yield q (%): ")
volatility = float(input("Enter the annual volatility sigma (%) you want to explore: "))

S = spx_level
K = float(strike_price)
r = (1/100)*float(risk_free_rate)
q = (1/100)*float(dividend_yield)
#sigma = (1/100)*float(volatility)
days_year = 365
T = (1/days_year)*int(time_to_expiry)

sigma_inc = [volatility/100]*10
# Create percentage basis vector
perc = [1, .90, .80, .70, .60, .50, .40, .30, .20, .10]
# Multiply the Spot proce times the percentage basis vector
spot_price = [S*val for val in perc]
