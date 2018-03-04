
## List of functions

### sma

The sma function is the [simple moving average](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages).  Two parameters are required: a Numpy array of prices, and the number of time periods for averaging.  The function returns the simple moving average as a numpy array.  Note that the length of the moving average will be shorter than the price series by N-1, where N is the period for averaging.

### ema

The ema function is the [exponential moving average](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages).  Two parameters are required: a Numpy array of prices, and the number of time periods for averaging.  The function returns the simple moving average as a numpy array.  Note that the length of the moving average will be shorter than the price series by N-1, where N is the period for averaging.

### kama

The kama function is the [Kaufman adaptive moving average](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:kaufman_s_adaptive_moving_average).  Four parameters are required: a Numpy array of prices, the number of periods for the efficiency ratio calculation, the number of periods for the fastest exponential moving average constant, and the number of periods for the slowest exponential moving average constant.  The time periods are adjustable, but Kaufman originally suggested time periods of 10, 2, and 30 for the efficiency ration, fastest EMA, and slowest EMA, respectively.  The kama function returns the average as a Numpy array whose length is shorter than the price array by N-1, where N is the number of periods used for the efficiency ratio.

### atr

The atr function is [average true range](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_true_range_atr)  The function requires four parameters: an array of high prices, an array of low prices, and array of closing prices, and a time period for averaging.  The time period is adjustable, but 14 is typically used.  The average true range is returned as an array shorter than the price array by N-1, where N is the time period used for averaging.

### rsi

The rsi function calculates the [Relative Strength Index](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:relative_strength_index_rsi).  The function requires two parameters: an array of prices, and a number of time periods for averaging.  The number of time periods is adjustable, but 14 is typically used.  The RSI is returned as an array that is shorter than the price array by N, where N is the number of periods used for averaging.

### cci

The cci function calculates the [Commodity Channel Index](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:commodity_channel_index_cci).  The function requires four parameters: an array of high prices, and array of low prices, and array of closing prices, and a number of time periods for averaging.  The number of time periods is adjustable, but a value of 20 is typically used.  The function returns the calculated cci values in an array that is shorter than the length of the price array by N-1, where N is the number of periods used for averaging.

### adl

The adl function calculates the [Accumulation/Distribution Line](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:accumulation_distribution_line).  The function requires four parameters: an array of high prices, and array of low prices, and array of closing prices, and a trading volume.  The function returns the adl values as an array whose length is equal to the length of the price arrays.

### macd

The macd function calculates the [Moving Average Convergence/Divergence](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_convergence_divergence_macd).  The function requires four parameters: an array of prices, a number of periods for the fast EMA, a number of periods for the slow EMA, and a number of periods for the signal line.  The function returns two arrays: the MACD Line and Signal Line.  The difference between the MACD Line and Signal Line can be used to calculate the MACD histogram.

### ppo

The macd function calculates the [Percent Price Oscillator](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:price_oscillators_ppo).  The function requires four parameters: an array of prices, a number of periods for the fast EMA, a number of periods for the slow EMA, and a number of periods for the signal line.  The function returns two arrays: the PPO Line and Signal Line.  The difference between the PPO Line and Signal Line can be used to calculate the PPO histogram.

### kelt

The kelt function calculates [Keltner Channels](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:keltner_channels).  The function requires six parameters, arrays of high prices, low prices, and closing prices, the number of periods for calculating the center line EMA, the multiple for the ATR, and the number of periods for calculating the ATR.  The function returns the lower, center, and upper lines of the Keltner Channels.

### rstd

The rstd function calculates a rolling [standard deviation](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:standard_deviation_volatility).  The function requires two parameters: an array of prices, and a number of periods used for calculating the standard deviation.  The function returns an array of the rolling standard deviation.

### boll

The boll function calculates the [Bollinger Bands<html>&reg;</html>](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:bollinger_bands).  The function requires four parameters: an array of prices, number of periods for calculating the center line SMA, multiplier for the standard deviation, and the number of periods used for calculating the rolling standard deviation.  The function returns the lower, center, and upper lines of the Bollinger Bands<html>&reg;</html>.

### trix

The trix function calculates the [TRIX indicator](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix).  The function requires three parameters: an array of prices, and a number of periods used for calculating the trimple EMA line, and the number of periods used for calculating the EMA of the signal.  The function returns the TRIX line and signal.

### stoch

The stoch function calculates the [Stochastic Oscillator](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:stochastic_oscillator_fast_slow_and_full).  The function requires six parameters: an array of high prices, an array of low prices, an array of closing prices, a look back period, a number of periods for calculating the %K moving average, and the number of periods for calculating the %D moving average.  The standard slow stochastic oscillator is calculated using the parameters (high,low,close,14,3,3).  The standard fast stochastic oscillator is calculated with the parameters (high,low,close,14,1,3).  Other look back and moving average periods may be selected to create a custom stochastic oscillator.

### vortex

The vortex function calculates the [Vortex Indicator](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:vortex_indicator).  The function requires four parameters: an array of high prices, and array of low prices, an array of closing prices, and a number of periods used for calculation.  The function returns the +VM and -VM indicators. 

### adx

The adx function calculates the [Average Directional Index (ADX)](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx). The function requires four parameters: an array of high prices, and array of low prices, an array of closing prices, and a number of periods used for calculation.  The function returns the positive directional indicator (+DI), negative directional indicator (-DI), and the ADX line. 
