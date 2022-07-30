import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import graphviz
from Models.Common.sqlconnection import getResult
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
import sklearn.metrics as metrics

query = '''
    SELECT region_id
      ,[population]
      ,[population_growth]
      ,[life_expectancy]
      ,[globalization_index]
      ,[economic_gi]
      ,[political_gi]
      ,[social_gi]
      ,[gdp_gov_spend]
      ,[gov_spend]
      ,[gov_debt]
      ,[tax_revenue]
      ,[foreign_aid_assistance]
      ,[economic_growth_forecast]
      ,[investment_forecast]
      ,[inflation_forecast]
      ,[liability_liquid]
      ,[assets_bank]
      ,[credit_bank_to_gov]
      ,[gdp_growth_rate]
      ,[gdp]
      ,[gdp_per_capita]
      ,[capital_investment]
      ,[household_consumption]
      ,[inflation]
      ,[exports]
      ,[imports]
      ,[foreign_investments]
      ,[net_equity_inflow]
      ,[current_account_balance]
      ,[trade_balance]
      ,[foreign_exchange_reserves]
      ,[net_payment_error_balance]
      ,[energy]
      ,[income_natural_resources]
      ,[electricity_access]
      ,[renewable_pg]
      ,[fossil_pg]
      ,[wind_pg]
      ,[solar_pg]
      ,[hydro_pg]
      ,[nuclear_pg]
      ,[geo_pg]
      ,[labour_force]
      ,[unemplyment_rate]
      ,[yield]
      ,[s&p]
  FROM [dbo].[vw_credit_esg_data]
	Where country_id not in (120, 140, 88, 182, 166, 118, 80, 89, 2, 18, 45, 56, 69, 143, 161)

'''

testQuery = '''
    SELECT region_id
      ,[population]
      ,[population_growth]
      ,[life_expectancy]
      ,[globalization_index]
      ,[economic_gi]
      ,[political_gi]
      ,[social_gi]
      ,[gdp_gov_spend]
      ,[gov_spend]
      ,[gov_debt]
      ,[tax_revenue]
      ,[foreign_aid_assistance]
      ,[economic_growth_forecast]
      ,[investment_forecast]
      ,[inflation_forecast]
      ,[liability_liquid]
      ,[assets_bank]
      ,[credit_bank_to_gov]
      ,[gdp_growth_rate]
      ,[gdp]
      ,[gdp_per_capita]
      ,[capital_investment]
      ,[household_consumption]
      ,[inflation]
      ,[exports]
      ,[imports]
      ,[foreign_investments]
      ,[net_equity_inflow]
      ,[current_account_balance]
      ,[trade_balance]
      ,[foreign_exchange_reserves]
      ,[net_payment_error_balance]
      ,[energy]
      ,[income_natural_resources]
      ,[electricity_access]
      ,[renewable_pg]
      ,[fossil_pg]
      ,[wind_pg]
      ,[solar_pg]
      ,[hydro_pg]
      ,[nuclear_pg]
      ,[geo_pg]
      ,[labour_force]
      ,[unemplyment_rate]
      ,[yield]
      ,[s&p]
  FROM [dbo].[vw_credit_esg_data]
	Where country_id in (120, 140, 88, 182, 166, 118, 80, 89, 2, 18, 45, 56, 69, 143, 161)

'''

query2 = '''
    Select [region_id], [population], [population_growth], [life_expectancy], 
    [globalization_index], [economic_gi], [political_gi], [social_gi], [gdp_gov_spend], 
    [gov_spend], [gov_debt], [tax_revenue], [foreign_aid_assistance], 
    [economic_growth_forecast], [investment_forecast], [inflation_forecast], [s&p] 
    From [vw_credit_esg_data] 
    Where country_id not in (120, 140, 88, 182, 166, 118, 80, 89, 2, 18, 45, 56, 69, 143, 161)
'''

testQuery2 = '''
    Select [region_id], [population], [population_growth], [life_expectancy], 
    [globalization_index], [economic_gi], [political_gi], [social_gi], [gdp_gov_spend], 
    [gov_spend], [gov_debt], [tax_revenue], [foreign_aid_assistance], 
    [economic_growth_forecast], [investment_forecast], [inflation_forecast], [s&p] 
    From [vw_credit_esg_data] 
    Where country_id in (120, 140, 88, 182, 166, 118, 80, 89, 2, 18, 45, 56, 69, 143, 161)
'''

def getTrainTestFiltered():
    df_new = getResult(query2)
    data = df_new.values
    
    X, y = data[:, 0:16], data[:, 16:]
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=69)
    
    return X_train, X_test, y_train, y_test

def getTestFiltered():
    df_new = getResult(testQuery2)
    data = df_new.values
    
    X, y = data[:, 0:16], data[:, 16:]
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y

def getTrainTest():
    df_new = getResult(query)
    data = df_new.values
    
    X, y = data[:, 0:46], data[:, 46:]
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=69)
    
    return X_train, X_test, y_train, y_test

def getTest():
    df_new = getResult(testQuery)
    data = df_new.values
    
    X, y = data[:, 0:46], data[:, 46:]
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y

def getCorrelationMatrix(df):
    corr = df.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))
    
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    

def getDecisionTreeFiltered():
    X_train, X_val, y_train, y_val = getTrainTestFiltered()
    X_test, y_test = getTestFiltered()
    
    decision_tree = tree.DecisionTreeClassifier(random_state = 69)
    decision_tree = decision_tree.fit(X_train, y_train)
    
    tree.plot_tree(decision_tree)
    
    feature_importance = decision_tree.feature_importances_
    
    y_pred = decision_tree.predict(X_val)
    score = accuracy_score(y_val, y_pred)
    
    print("Validation Accuracy: ", score)
    
    y_pred = decision_tree.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    
    print("Testing Accuracy: ", score)
 
def getDecisionTree():
    X_train, X_val, y_train, y_val = getTrainTest()
    X_test, y_test = getTest()
    
    decision_tree = tree.DecisionTreeClassifier(random_state = 69)
    decision_tree = decision_tree.fit(X_train, y_train)
    
    tree.plot_tree(decision_tree)
    
    feature_importance = decision_tree.feature_importances_
    
    y_pred = decision_tree.predict(X_val)
    score = accuracy_score(y_val, y_pred)
    
    print("Validation Accuracy: ", score)
    
    y_pred = decision_tree.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    
    print("Testing Accuracy: ", score)
    
def getRegressor():
    X_train, X_val, y_train, y_val = getTrainTest()
    X_test, y_test = getTest()
    
    regressor = DecisionTreeRegressor() 
    b_regressor = BaggingRegressor(regressor, n_estimators = 100, max_features=3, max_samples=.5)  # get Boostrap aggregation ensemble regressor 
    
    regressor.fit(X_train, y_train)  
    y_pred = regressor.predict(X_val) 
    
    b_regressor.fit(X_train, y_train)  
    y_b_pred = b_regressor.predict(X_val) 
    
    # df = pd.DataFrame({'Actual Value': y_val, 'Predicted Values': y_pred, 'Bagging Predicted Values': y_b_pred})  
    # print(df)
    
    print('Mean Absolute Error (Regular):', metrics.mean_absolute_error(y_val, y_pred))
    print('Mean Squared Error (Regular):', metrics.mean_squared_error(y_val, y_pred))
    print('Root Mean Squared Error (Regular):', np.sqrt(metrics.mean_squared_error(y_val, y_pred)))
    
    print('Mean Absolute Error (Bagging):', metrics.mean_absolute_error(y_val, y_b_pred))
    print('Mean Squared Error (Bagging):', metrics.mean_squared_error(y_val, y_b_pred))
    print('Root Mean Squared Error (Bagging):', np.sqrt(metrics.mean_squared_error(y_val, y_b_pred)))
    
    score = accuracy_score(y_val, y_pred)
    # b_score = accuracy_score(y_val, y_b_pred)
    
    print("Validation Accuracy DT: ", score)
    # print("Validation Accuracy Bagging: ", b_score)
    
    print("\n\n")
    
    y_pred = regressor.predict(X_test)     
    y_b_pred = b_regressor.predict(X_test) 
    
    # df = pd.DataFrame({'Actual Value': y_val, 'Predicted Values': y_pred, 'Bagging Predicted Values': y_b_pred})  
    # print(df)
    
    print('Mean Absolute Error (Regular):', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error (Regular):', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error (Regular):', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    
    print('Mean Absolute Error (Bagging):', metrics.mean_absolute_error(y_test, y_b_pred))
    print('Mean Squared Error (Bagging):', metrics.mean_squared_error(y_test, y_b_pred))
    print('Root Mean Squared Error (Bagging):', np.sqrt(metrics.mean_squared_error(y_test, y_b_pred)))
    
    score = accuracy_score(y_test, y_pred)
    # b_score = accuracy_score(y_val, y_b_pred)
    
    print("Testing Accuracy DT: ", score)
    # print("Validation Accuracy Bagging: ", b_score)