# Stock Predictor


## Techniques to be Applied

**1. Statistical Models:**

1. Gaussian Process Regression (GPR): Popularity (High), Ease of Use (Medium), Availability (Scikit-learn)
2. Skewed Student-T Distribution (ST) Models: Popularity (Medium), Ease of Use (Hard), Availability (Scipy)
3. Dynamic Linear Models (DLMs): Popularity (Medium), Ease of Use (Hard), Availability (Scipy)
4. Bayesian Structural Time Series (BSTS) models: Popularity (Low), Ease of Use (Hard), Availability (Scipy)
5. Local Linear Trend (LLT) Models: Popularity (Low), Ease of Use (Easy), Availability (Scipy)

**2. Machine Learning Models:**

1. Decision Trees: Popularity (High), Ease of Use (Easy), Availability (Scikit-learn)
2. K-Nearest Neighbors (K-NN): Popularity (Medium), Ease of Use (Medium), Availability (Scikit-learn)
3. Extreme Gradient Boosting (XGBoost): Popularity (Medium), Ease of Use (Hard), Availability (Scikit-learn)
4. Gradient Descent: Popularity (Low), Ease of Use (Medium), Availability (Scikit-learn)
5. Long Short-Term Memory (LSTM) Networks: Popularity (Low), Ease of Use (Hard), Availability (Keras)

**3. Deep Learning Models:**

1. Convolutional Neural Networks (CNNs): Popularity (High), Ease of Use (Medium), Availability (Keras)
2. Recurrent Neural Networks (RNNs): Popularity (Medium), Ease of Use (Medium), Availability (Keras)
3. Autoencoder Networks: Popularity (Medium), Ease of Use (Hard), Availability (Keras)
4. Variational Autoencoders (VAEs): Popularity (Low), Ease of Use (Hard), Availability (Keras)
5. Generative Adversarial Networks (GANs): Popularity (Low), Ease of Use (Hard), Availability (Keras)

## Recommended Approaches

**1. For Statistical Models:**
1. Since GPR can model the correlation between financial variables, it can capture the patterns in stock prices over time and predict future values accordingly.
2. ST models can incorporate time-series data for variable relationships and use estimation techniques like maximum likelihood estimation (MLE) to predict future stock prices.
3. DLMs are well-suited for analyzing and predicting the time dynamics of stock prices and related financial indicators, such as trading volumes and bid-ask spread.
4. Like DLMs, BSTS models can incorporate various time-related factors to predict future stock prices, such as seasonality, cyclical behavior, and periodicity.
5. LLT models are particularly useful when the stock price series exhibits linear trend and seasonality patterns.

**2. For Machine Learning Models:**
1. Decision trees can be used to select variables and evaluate their importance for predicting stock prices over a given time horizon, as well as pattern recognition for forecasting.
2. K-NN can help to identify similar patterns of the stock price from the past and predict their potential future change.
3. XGBoost can be used for boosting other time series models to improve prediction accuracy through proper hyper-parameter tuning.
4. Gradient descent can be used to train a range of linear models (ARIMA, etc.) to identify correlation patterns between the past and current stock prices and make relevant predictions.
5. LSTMs are especially useful for encoding important historical patterns in the stock price and trading volumes data for specific time intervals, and using this information to make predictions for future intervals.

**3. For Deep Learning Models:**
1. CNNs can capture and process time-varying inputs, making them suitable for analyzing the stock price data using convolutional filters that extract meaningful features.
2. With a memory that can update retrospectively, RNNs use the sequential data of the stock prices to recognize important temporal patterns and hence make accurate predictions.
3. Autoencoders can discover meaningful patterns in complex time-series data like stock prices and extract the relevant subsets for making predictions that reflect the broader trend.
4. VAEs can be trained on stock price time-series data and generate new plausible scenarios, providing a diversified set of potential outcomes from which we can infer future changes in stock prices.
5. GANs are capable of improving the quality of the data they generate; hence, they can help to reduce noise and capture more pronounced trends from the stock price series.

## Data

The stock data includes several key attributes that can provide useful information for investors and traders. These attributes include:

- Date: The date of each trading day.
- Open: The opening price of the stock at the beginning of the trading day.
- High: The highest price reached by the stock during the trading day.
- Low: The lowest price reached by the stock during the trading day.
- Close: The closing price of the stock at the end of the trading day.
- Volume: The total number of shares traded during the trading day.
- OpenInt: The open interest, which is the number of outstanding derivative contracts, at the end of the trading day.

Using these attributes, investors can derive several key indicators that can aid in their investment decisions, such as:

- Moving Averages: Investors can calculate moving averages by taking the average of a certain number of periods, such as 5, 10, or 20 days. The values for open, high, low, and close prices over these periods can be averaged to provide a more smooth and consistent view of the stock price over time. Moving averages can help identify trends and potential turning points in the stock price.
- Relative Strength Index (RSI): The RSI is calculated by comparing the average gains of a stock's prices with the average losses over a certain period, typically 14 days. The RSI provides an indication of whether the stock is overbought or oversold, which can help investors identify potential buy and sell opportunities.
- Bollinger Bands: Bollinger Bands are calculated by plotting two standard deviations away from the stock's moving average price. The bands widen or tighten depending on the volatility of the stock. They can give an indication of whether the stock is overbought or oversold and can help investors make better trading decisions.
- Volume Weighted Average Price (VWAP): VWAP is a measure of the true average price paid for a stock over a given period, weighted by the volume of shares traded. It provides a more accurate picture of the price movement throughout the day and can help investors assess their trading performance.
- Price-to-Earnings Ratio (P/E Ratio): The P/E ratio is calculated by dividing the stock price by its earnings per share. This metric is used to measure the earnings of the stock relative to its price and can help investors determine if the stock is undervalued or overvalued compared to its peers.

The file name consists of the ticker symbol and country code for the stock. In this case, "csbk" is the ticker symbol for the stock of Clifton Bancorp Inc. and ".us" is the country code for the United States. Therefore, the file name "csbk.us" tells you that the stock data pertains to Clifton Bancorp Inc. traded in the United States.