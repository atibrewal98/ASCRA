import pandas as pd
import numpy as np
import seaborn as sns
from numpy import mean
from numpy import std
from numpy import isnan
from sklearn.ensemble import RandomForestClassifier
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.pipeline import Pipeline
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error


def getImputorAnalysis(dataframe):
    # split into input and output elements
    data = dataframe.values
    ix = [i for i in range(data.shape[1]) if i != 46]
    X, y = data[:, ix], data[:, 46:47]
    # evaluate each strategy on the dataset
    results = list()
    # strategies = ['ascending', 'descending', 'roman', 'arabic', 'random']
    strategies = [str(i) for i in range(1, 21)]
    for s in strategies:
    	# create the modeling pipeline
    	pipeline = Pipeline(steps=[('i', IterativeImputer(max_iter = int(s))), ('m', RandomForestClassifier())])
    	# evaluate the model
    	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    	scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=cv, n_jobs = 1)
    	# store results
    	results.append(scores)
    	print('>%s %.3f (%.3f)' % (s, mean(scores), std(scores)))
    # plot model performance for comparison
    pyplot.boxplot(results, labels=strategies, showmeans=True)
    pyplot.xticks(rotation=45)
    pyplot.show()
    
    
def imputeData(dataframe):
    # split into input and output elements
    data = dataframe.values
    ix = [i for i in range(data.shape[1]) if i != 47]
    X, y = data[:, ix], data[:, 47:]
    
    imputer = IterativeImputer(max_iter = 16, imputation_order = 'random')
    imputer.fit(X)
    
    Xtrans = imputer.transform(X)
    
    print('Missing: %d' % sum(isnan(Xtrans).flatten()))
    
def getPlots(df):
    cont_feats = [col for col in df.columns if df[col].dtype != object]
    
    # Mean Imputation
    mean_imputer = SimpleImputer(strategy='mean')
    mean_imputed = mean_imputer.fit_transform(df[cont_feats])
    df_mean_imputed = pd.DataFrame(mean_imputed, columns=cont_feats)
    
    # Median Imputation
    median_imputer = SimpleImputer(strategy='median')
    median_imputed = median_imputer.fit_transform(df[cont_feats])
    df_median_imputed = pd.DataFrame(median_imputed, columns=cont_feats)
    
    # Iterative Imputation
    iter_imputer = IterativeImputer(random_state=42)
    iter_imputed = iter_imputer.fit_transform(df[cont_feats])
    df_iter_imputed = pd.DataFrame(iter_imputed, columns=cont_feats)
    
    # Plotting a comparison between the different strategies
    fig, axes = pyplot.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 10))
    axes = np.reshape(axes, -1)
    
    dfs = [df_mean_imputed, df_median_imputed, df_iter_imputed]
    titles = ['Mean Imputation', 'Median Imputation', 'Iterative Imputation']
    
    for i, df in enumerate(dfs):
        # Plotting the data
        x = df.gov_spend
        y = df.gov_debt
        sns.scatterplot(x, y, ax=axes[i], color='green')
        
        # Fitting and plotting a linear regression line
        m, b = np.polyfit(x, y, 1)
        linreg = m*x + b
        axes[i].plot(x, linreg, color='black')
        
        # Setting the titles and including the RMSE values
        axes[i].set_title(titles[i], fontsize=16, fontweight='bold')
        rmse = round(mean_squared_error(y, linreg, squared=False), 3)
        axes[i].text(45, 35, f'RMSE: {rmse}', fontsize=14, fontweight='bold')
        
    pyplot.show()