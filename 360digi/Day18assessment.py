""" Perfect 👍

📘 Python Libraries in Data Analytics — Cheat Sheet with Usage
|  |  |  | 
|  |  | pd.read_csv("file.csv")df[df["Age"] > 30]df.groupby("Dept")["Salary"].mean() | 
|  |  | np.array([1,2,3])np.mean(arr)np.dot(a, b) | 
|  |  | plt.plot(x, y)plt.hist(data)plt.scatter(x, y) | 
|  |  | sns.heatmap(df.corr())sns.boxplot(x="Dept", y="Salary", data=df)sns.regplot(x="Age", y="Salary", data=df) | 
|  |  | train_test_split(X, y)LogisticRegression().fit(X_train, y_train)KMeans(n_clusters=3).fit(X) | 
|  |  | sm.OLS(y, X).fit()sm.tsa.ARIMA(data, order=(1,1,1)).fit()sm.stats.ttest_ind(a, b) | 
|  |  | model = Prophet(); model.fit(df)future = model.make_future_dataframe(periods=365)model.plot(forecast) | 
|  |  | word_tokenize(text)PorterStemmer().stem("running")nltk.pos_tag(words) | 
|  |  | soup = BeautifulSoup(html, "html.parser")[a['href'] for a in soup.find_all('a')]soup.get_text() | 



📝 Key Takeaways
- Pandas → Manipulate & clean data
- NumPy → Numerical backbone for arrays & math
- Matplotlib → Flexible plotting (low-level control)
- Seaborn → Quick, polished statistical plots
- Scikit-learn → Machine learning (classification, regression, clustering, evaluation)
- StatsModels → Statistical modeling & hypothesis testing
- Prophet → Forecasting time series with seasonality
- NLTK → NLP tasks (tokenization, stemming, tagging)
- BeautifulSoup → Web scraping & HTML parsing

- Primary purpose of Pandas → Data manipulation and analysis
- Purpose of iloc in Pandas → Data filtering by positions (integer-based indexing)
- Goal of Feature Engineering → To create new data features
- Regression in ML → Predicting a target variable based on input features (continuous values)
- Library for NLP tasks → NLTK (Natural Language Toolkit)
- Library for Time Series Forecasting → Prophet (specialized for forecasting)
- Purpose of K-means → Clustering (grouping data points by similarity)
- EDA stands for → Exploratory Data Analysis
- Outlier definition → A data point significantly different from other data points
- Library for Data Visualization → Seaborn (built on Matplotlib, polished visuals)
- Library for Machine Learning algorithms → Scikit-learn
- Purpose of Matplotlib → Data visualization (flexible plotting library)
- Heatmap usage → Visualizing correlation (and patterns in data matrices)
- Library for Statistical Models → StatsModels (regression, time series, hypothesis testing)

📝 Quick Takeaways
- Pandas → Data manipulation
- Seaborn / Matplotlib → Visualization
- Scikit-learn → Machine learning algorithms
- NLTK → NLP tasks
- Prophet / StatsModels → Time series & statistical modeling
- K-means → Clustering
- EDA → First step in analytics (explore data)
- Outliers → Must detect & handle carefully
"""