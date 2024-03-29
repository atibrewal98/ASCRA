
export const countrySummary = [{
    "Name": "Sri Lanka",
    "S&P Rating": "CC",
    "Moodys Rating": "Caa2",
    "Fitch Rating": "CC",
    "Our Rating": "C"
},
{
    "Name": "United Kingdom",
    "S&P Rating": "AA",
    "Moodys Rating": "Aa3",
    "Fitch Rating": "AA-",
    "Our Rating": "AA"
},
{
    "Name": "Azerbaijan",
    "S&P Rating": "BB+",
    "Moodys Rating": "Ba2",
    "Fitch Rating": "BB+",
    "Our Rating": "BBB"
}]

export const defaultSummary = {
    "Name": "Default",
    "S&P Rating": "BB+",
    "Moodys Rating": "Ba2",
    "Fitch Rating": "BB+",
    "Our Rating": "BBB"
}

export const columns = [
    {id: 'year', label: 'Year', minWidth: 150},
    {id: 'population', label: 'Population (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'population_growth', label: 'Population Growth (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'life_expectancy', label: 'Life Expectancy (Years)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'globalization_index', label: 'Globalization Index (0-100)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'economic_gi', label: 'Economic Growth Index (0-100)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'political_gi', label: 'Political Growth Index (0-100)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'social_gi', label: 'Social Growth Index (0-100)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'gdp_gov_spend', label: 'GDP Govt. Spend (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'gov_spend', label: 'Govt. Spend (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'gov_debt', label: 'Govt. Debt (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'tax_revenue', label: 'Tax Revenue (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'foreign_aid_assistance', label: 'Foreign Aid Assitance (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'economic_growth_forecast', label: 'Economic Growth Forecast (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'investment_forecast', label: 'Investment Forecast (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'inflation_forecast', label: 'Inflation Forecast (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'liability_liquid', label: 'Liability Liquid (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'assets_bank', label: 'Assets Bank (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'credit_bank_to_gov', label: 'Credit Bank To Govt. (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'gdp_growth_rate', label: 'GDP Growth Rate (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'gdp', label: 'GDP (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'gdp_per_capita', label: 'GDP Per Capita (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'capital_investment', label: 'Capital Investment (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'household_consumption', label: 'Household Consumption (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'inflation', label: 'Inflation (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'exports', label: 'Exports (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'imports', label: 'Import (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'foreign_investments', label: 'Foreign Investments (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'net_equity_inflow', label: 'Net Equity Inflow (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'current_account_balance', label: 'Current Account Balance (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'trade_balance', label: 'Trade Balance (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'foreign_exchange_reserves', label: 'Foreign Exchange Reserves (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'net_payment_error_balance', label: 'Net Payment Error Balance (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'energy', label: 'Energy (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'income_natural_resources', label: 'Income Natural Resources (Millions)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'electricity_access', label: 'Electricity Access (% of Population)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'renewable_pg', label: 'Renewable Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'fossil_pg', label: 'Fossil Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'wind_pg', label: 'Wind Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'solar_pg', label: 'Solar Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'hydro_pg', label: 'Hydro Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'nuclear_pg', label: 'Nuclear Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'geo_pg', label: 'Geo Power Generation (Billions KWH)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'unemplyment_rate', label: 'Unemployment Rate (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 'yield', label: 'Yield (%)', minWidth: 150, format: (value) => value.toFixed(2)},
    {id: 's&p', label: 'S&P', minWidth: 150},
    {id: 'moody', label: 'Moody', minWidth: 150},
    {id: 'fitch', label: 'Fitch', minWidth: 150}
  ];