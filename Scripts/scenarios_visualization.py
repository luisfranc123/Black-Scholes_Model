# 1. we create a dictionary to store all scenario tables
all_scenarios = {}

# 2. Loop through all 11 scenarios (0 to 10)
for scenario_number in range(len(scenarios_list)):
  # Get the volatility vector for each scenario
  sigma_vector = scenarios_list[scenario_number]

  # 3. Calculate intermediates function (d1, d2) for the current scenario
  # Pass the entire spot_price list and the current sigma_vector list to the functions
  d1_scenario, d2_scenario = intermediates(spot_price, K, r, q, sigma_vector, T)

  # 4. Calculate call/put prices for the current scenario
  call_price_scenario, put_price_scenario = call_put_prices(d1_scenario, d2_scenario, spot_price, K, r, q, sigma_vector, T)

  # Store the calculated values for the current scenario in the all_scenarios dictionary
  all_scenarios[f'Scenario_{scenario_number}'] = {
      'd1': d1_scenario,
      'd2': d2_scenario,
      'call_prices': call_price_scenario,
      'put_prices': put_price_scenario
  }

# All put prices from each scenario
put_prices_dict = {scenario: all_scenarios[scenario]['put_prices']\
                   for scenario in all_scenarios}
Table_1_df = pd.DataFrame(put_prices_dict)
idx0 = 0
idx1 = 1
Table_1_df.insert(loc = idx0, column = "Spot_Price", value = spot_price)
new_col = Table_1_df['Spot_Price']/spot_price[0] - 1
Table_1_df.insert(loc = idx1, column = 'Percentage', value = new_col)
print(Table_1_df)

# Constants
fund_input = input("Enter the fund quantity (USD): ")
fund = float(fund_input)
constant_1 = fund/spot_price[0]/100
constant_2 = 0.20
constant_3 = constant_1*constant_2

# Table 2:
# Get all scenario columns
scenario_columns = [col for col in Table_1_df.columns if \
                    col.startswith('Scenario_')]
Table_2_df = Table_1_df[['Spot_Price', 'Percentage']].copy()
Table_2_df[scenario_columns] = Table_1_df[scenario_columns]*constant_3*100
print(Table_2_df)

# Table 3:
scenario_columns = [col for col in Table_2_df.columns if \
                    col.startswith('Scenario_')]
Market_Decline = Table_2_df[['Spot_Price', 'Percentage']].copy()
Market_Decline[scenario_columns] = Table_2_df[scenario_columns]/fund
print(Market_Decline)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
Market_Decline_reversed = Market_Decline.iloc[::-1].reset_index(drop = True)
# reshape the data from wide to long format for seaborn
df_melted = Market_Decline_reversed.melt(
    id_vars = ['Spot_Price', 'Percentage'],  # Keep these columns as identifiers
    value_vars = [col for col in Market_Decline_reversed.columns if \
                  col.startswith('Scenario_')],  # Scenario columns to melt
    var_name = 'Scenario',
    value_name = 'Probability'
)

# Create the lineplot
plt.figure(figsize=(12, 8))
sns.lineplot(
    data = df_melted,
    x = 'Percentage',
    y = 'Probability',
    hue = 'Scenario',
    marker = 'o',
    palette = 'colorblind'
)


# Customize the plot
plt.title('Hypothetical Increases from the OTM Puts\nwith\nDifferent Volatility Increases')
plt.xlabel('Market Decline Percentage')
plt.ylabel('Probability')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)

# Adjust layout to prevent legend cutoff
plt.tight_layout()
plt.show()
