print("Volatility Increase % (Scenarios):\n")
print("-"*70)
# Generate all lists
all_lists = [sigma_inc] + [
    [0.20 if j == 0 else 0.20 + (i * .05 * j) for j in range(10)]
    for i in range(1, 11)]

# Assign to individual variables
sigma_inc, sigma_inc2, sigma_inc3, sigma_inc4, sigma_inc5, sigma_inc6,\
sigma_inc7, sigma_inc8, sigma_inc9, sigma_inc10, sigma_inc11 = all_lists

# Create different scenarios vector
scenarios = [1.00 + i* .05 for i in range(11)]

# Convert list to numpy arrays
scenarios_arr = np.array(scenarios)
all_lists_arr = np.array(all_lists)

# Perform the multiplication scenarios * all_lists
result_array = all_lists_arr*scenarios_arr[:, np.newaxis]
scenarios_list = result_array.round(2).tolist()
# Print to verify
for idx, lst in enumerate(scenarios_list):
    print(f"Scenario_{idx}: {lst}")

import pandas as pd
scenario_input = input("Please enter the scenario you want to explore (0 - 10): ")

try:
    scenario_number = int(scenario_input)
    d1 = intermediates(spot_price, K, r, q, scenarios_list[scenario_number], T)[0]
    d2 = intermediates(spot_price, K, r, q, scenarios_list[scenario_number], T)[1]
    callput_price = call_put_prices(d1, d2, spot_price, K, r, q, \
                               scenarios_list[scenario_number], T)
    greeks_extras = greeks(d1, d2, spot_price, K, r, q, \
                                     scenarios_list[scenario_number], T)
    scenario = {'Percentage_Basis': [100*val for val in perc],
                'd1': d1,
                'd2': d2,
                'Call_price': callput_price[0],
                'Put_price': callput_price[1],
                'Call_Delta': greeks_extras[0],
                'Put_Delta': greeks_extras[1],
                'Gamma': greeks_extras[2],
                'Vega_per_1%_vol': greeks_extras[3],
                'Call_Theta_year': greeks_extras[4],
                'Put_Theta_year': greeks_extras[5],
                'Call_Theta_day': greeks_extras[6],
                'Put_Theta_day': greeks_extras[7],
                'Call_Rho_1%_rate': greeks_extras[8],
                'Put_Rho_1%_rate': greeks_extras[9]}

    print(f"You entered scenario number: {scenario_number}")
    print(pd.DataFrame(scenario))

except ValueError:
    print(f"Invalid input. Please enter a valid integer for the scenario.\
     You entered: {scenario_input}")

