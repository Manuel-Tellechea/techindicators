import numpy as np
#
# Simple Moving Average
# a is an array of prices, b is a period for averaging
def sma(a,b):
    result = np.zeros(len(a)-b+1)
    for i in range(len(a)-b+1):
        result[i] = np.sum(a[i:i+b])/b
    return result
#
# Exponential Moving Average
# a is an array of prices, b is a period for averaging
def ema(a,b):
    result = np.zeros(len(a)-b+1)
    result[0] = np.sum(a[0:b])/b
    for i in range(1,len(result)):
        result[i] = result[i-1]+(a[i+b-1]-result[i-1])*(2/(b+1))
    return result
#
# Kaufman's Adaptive Moving Average
# a is an array of prices, b is the period for the efficiency ratio
# c is the period for the fast EMA, d is the period for the slow EMA
def kama(a,b,c,d):
    fsc = 2/(c+1)# fast smoothing constant
    ssc = 2/(d+1)# slow smoothing constant
    er = np.zeros(len(a))# efficiency ratio
    pv = np.zeros(len(a))# periodic volatility
    pd = np.zeros(len(a))# price direction
    for i in range(1,len(a)):
        pv[i] = np.fabs(a[i]-a[i-1])
    for i in range(b,len(a)):
        pd[i] = np.fabs(a[i]-a[i-b])
    for i in range(b,len(a)):
        er[i] = pd[i]/np.sum(pv[i-b+1:i+1])
    sc = (er*(fsc-ssc)+ssc)**2
    result = np.zeros(len(a))
    result[b-1] = a[b-1]
    for i in range(b,len(a)):
        result[i] = result[i-1]+sc[i]*(a[i]-result[i-1])
    return result[b-1:]
#
# Average True Range
# a is array of high prices, b is array of low prices, 
# c is array of closing prices, d is period for averaging
def atr(a,b,c,d):
    tr = np.zeros(len(a))
    result = np.zeros(len(a)-d+1)
    tr[0] = a[0]-b[0]
    for i in range(1,len(a)):
        hl = a[i]-b[i]
        hpc = np.fabs(a[i]-c[i-1])
        lpc = np.fabs(b[i]-c[i-1])
        tr[i] = np.amax(np.array([hl,hpc,lpc]))
    result[0] = np.sum(tr[0:d])/d
    for i in range(1,len(a)-d+1):
        result[i] = (result[i-1]*(d-1)+tr[i+d-1])/d
    return result
#
# Relative Strength Index
# a is an array of prices, b is the period for averaging
def rsi(a,b):
    change = np.zeros(len(a))
    gain = np.zeros(len(a))
    loss = np.zeros(len(a))
    ag = np.zeros(len(a))
    al = np.zeros(len(a))
    result = np.zeros(len(a))
    for i in range(1,len(a)):
        change[i] = a[i]-a[i-1]
        if change[i] == 0:
            gain[i] = 0
            loss[i] = 0
        if change[i] < 0:
            gain[i] = 0
            loss[i] = np.fabs(change[i])
        if change[i] > 0:
            gain[i] = change[i]
            loss[i] = 0
    ag[b] = np.sum(gain[1:b+1])/b# initial average gain
    al[b] = np.sum(loss[1:b+1])/b# initial average loss
    for i in range(b+1,len(a)):
        ag[i] = (ag[i-1]*(b-1)+gain[i])/b
        al[i] = (al[i-1]*(b-1)+loss[i])/b
    for i in range(b,len(a)):
        result[i] = 100-100/(1+ag[i]/al[i])
    return result[b:]
#
# Commodity Channel Index
# a is array of high prices, b is array of low prices,
# c is array of closing prices, d is the number of periods
def cci(a,b,c,d):
    tp = (a+b+c)/3 # typical price
    atp = np.zeros(len(a)) # average typical price
    md = np.zeros(len(a)) # mean deviation
    result = np.zeros(len(a))
    for i in range(d-1,len(a)):
        atp[i] = np.sum(tp[i-(d-1):i+1])/d
        md[i] = np.sum(np.fabs(atp[i]-tp[i-(d-1):i+1]))/d
        result[i] = (tp[i]-atp[i])/(0.015*md[i])
    return result[d-1:]
#
# Accumulation/Distribution Line
# a is array of high prices, b is array of low prices,
# c is array of closing prices, d is the trading volume
def adl(a,b,c,d):
    mfm = ((c-b)-(a-c))/(a-b) # Money flow multiplier
    mfv = mfm*d # Money flow volume
    result = np.zeros(len(a))
    result[0] = mfv[0]
    for i in range(1,len(a)):
        result[i] = np.sum(mfv[0:i+1])
    return result
#
# Moving Average Convergence/Divergence
# a is an array of prices, b is the numer of periods for fast EMA
# c is number of periods for slow EMA, 
# d is number of periods for signal line
def macd(a,b,c,d):
    line = ema(a,b)[c-b:]-ema(a,c)
    signal = ema(line,d)
    return line,signal
#
# Keltner Channels
# a, b, and c are high, low, and close price arrays
# d is numer of periods for center line EMA
# e is multiplier for ATR, and f is period for ATR
def kelt(a,b,c,d,e,f):
    center = ema(c,d)
    if d>f:
        upper = center+e*atr(a,b,c,f)[d-f:]
        lower = center-e*atr(a,b,c,f)[d-f:]
    if f>=d:
        upper = center[f-d:]+e*atr(a,b,c,f)
        lower = center[f-d:]+e*atr(a,b,c,f)
    return lower,center,upper
#
# Rolling standard deviation
# a is an array of prices, b is number of periods
def rstd(a,b):
    result = np.zeros(len(a)-b+1)
    for i in range(len(a)-b+1):
        result[i] = np.std(a[i:i+b],ddof=0)
    return result
#
# Bollinger Bands
# a is an array of prices, b is number of periods used 
# for the SMA calculation, c is the multiplier for the 
# standard deviation, d is the number of periods for
# calculating the standard deviation
def boll(a,b,c,d):
    stdboll = rstd(a,d)
    center = sma(a,b)
    if b>d:
        upper = center+c*stdboll[b-d:]
        lower = center-c*stdboll[b-d:]
    if d>=b:
        upper = center[d-b:]+c*stdboll
        lower = center[d-b:]-c*stdboll
    return lower,center,upper
#
# Percent price oscillator
# a is an array of prices, b is the numer of periods for fast EMA
# c is number of periods for slow EMA, 
# d is number of periods for signal line
def ppo(a,b,c,d):
    line = ((ema(a,b)[c-b:]-ema(a,c))/ema(a,c))*100
    signal = ema(line,d)
    return line,signal
#
# TRIX
# a is an array of prices, b is a period for each EMA in TRIX
# c is a period for the signal line EMA
def trix(a,b,c):
    triema = ema(ema(ema(a,b),b),b)
    line = np.zeros(len(triema)-1)
    for i in range(1,len(triema)):
        line[i-1] = ((triema[i]-triema[i-1])/triema[i-1])*100
    signal = ema(line,c)
    return line,signal
#
# Stochastic oscillator
# a is an array of high prices, b is array of low prices,
# c is an array of closing prices, d is the look back period
# e is number of periods for %K SMA, f is the number of
# periods for %D SMA
def stoch(a,b,c,d,e,f):
    t = np.zeros(len(a))
    for i in range(d-1,len(a)):
        t[i] = ((c[i]-np.amin(b[i-(d-1):i+1]))/(np.amax(a[i-(d-1):i+1])-\
         np.amin(b[i-(d-1):i+1])))*100
    t = t[d-1:]
    pk = sma(t,e)
    pd = sma(pk,f)
    return pk,pd
#
# Vortex indicator
# a is array of high prices, b is array of low prices
# c is array of close prices, d is number of periods
def vortex(a,b,c,d):
    tr = np.zeros(len(a))
    vp = np.zeros(len(a))
    vm = np.zeros(len(a))
    trd = np.zeros(len(a))
    vpd = np.zeros(len(a))
    vmd = np.zeros(len(a))
    tr[0] = a[0]-b[0]
    for i in range(1,len(a)):
        hl = a[i]-b[i]
        hpc = np.fabs(a[i]-c[i-1])
        lpc = np.fabs(b[i]-c[i-1])
        tr[i] = np.amax(np.array([hl,hpc,lpc]))
        vp[i] = np.fabs(a[i]-b[i-1])
        vm[i] = np.fabs(b[i]-a[i-1])
    for j in range(len(a)-d+1):
        trd[d-1+j] = np.sum(tr[j:j+d])
        vpd[d-1+j] = np.sum(vp[j:j+d])
        vmd[d-1+j] = np.sum(vm[j:j+d])
    trd = trd[d-1:]
    vpd = vpd[d-1:]
    vmd = vmd[d-1:]
    vpn = vpd/trd
    vmn = vmd/trd
    return vpn,vmn
#
# Average Directional Index (ADX)
# a is array of high prices, b is array of low prices
# c is array of close prices, d is number of periods
def adx(a,b,c,d):
    tr = np.zeros(len(a))
    hph = np.zeros(len(a))
    pll = np.zeros(len(a))
    trd = np.zeros(len(a))
    pdm = np.zeros(len(a))
    ndm = np.zeros(len(a))
    pdmd = np.zeros(len(a))
    ndmd = np.zeros(len(a))
    for i in range(1,len(a)):
        hl = a[i]-b[i]
        hpc = np.fabs(a[i]-c[i-1])
        lpc = np.fabs(b[i]-c[i-1])
        tr[i] = np.amax(np.array([hl,hpc,lpc]))
        hph[i] = a[i]-a[i-1]
        pll[i] = b[i-1]-b[i]
    for j in range(1,len(a)):
        if hph[j]>pll[j]:
            if hph[j]>0:
                pdm[j]=hph[j]
        if pll[j]>hph[j]:
            if pll[j]>0:
                ndm[j]=pll[j]
    trd[d]=np.sum(tr[1:d+1])
    pdmd[d]=np.sum(pdm[1:d+1])
    ndmd[d]=np.sum(ndm[1:d+1])
    for k in range(d+1,len(a)):
        trd[k]=trd[k-1]-trd[k-1]/d+tr[k]
        pdmd[k]=pdmd[k-1]-pdmd[k-1]/d+pdm[k]
        ndmd[k]=ndmd[k-1]-ndmd[k-1]/d+ndm[k]
    trd = trd[d:]
    pdmd = pdmd[d:]
    ndmd = ndmd[d:]
    p = (pdmd/trd)*100
    n = (ndmd/trd)*100
    diff = np.fabs(p-n)
    summ = p+n
    dx = 100*(diff/summ)
    adx = np.zeros(len(dx))
    adx[d-1] = np.mean(dx[0:d])
    for l in range(d,len(dx)):
        adx[l] = (adx[l-1]*(d-1)+dx[l])/d
    adx = adx[d-1:]
    return p,n,adx
#
# Aroon Oscillator
# a is array of high prices, b is array of low prices
# c is number of periods for calculation
def aroon(a,b,c):
    up = np.zeros(len(a))
    down = np.zeros(len(a))
    for i in range(c,len(a)):
        up[i] = 100*(1-(i-np.amax(np.where(a[0:i+1]==np.amax(a[i-c:i+1]))))/c)
        down[i] = 100*(1-(i-np.amax(np.where(b[0:i+1]==np.amin(b[i-c:i+1]))))/c)
    up = up[c:]
    down = down[c:]
    return up,down,(up-down)