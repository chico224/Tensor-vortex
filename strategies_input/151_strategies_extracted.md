# 151 Trading Strategies - Extracted Data

Source: 151 Trading Strategies论文版.pdf
Total Pages: 361

---

## Page 1

151 Trading Strategies
Zura Kakushadze§†1 and Juan Andr´ es Serur♯2
§ Quantigic® Solutions LLC
1127 High Ridge Road #135, Stamford, CT 06905 3
† Free University of Tbilisi, Business School & School of Physics
240, David Agmashenebeli Alley, Tbilisi, 0159, Georgia
♯ Universidad del CEMA
Av. C´ ordoba 374, C1054AAP, Ciudad de Buenos Aires, Argentina
(August 17, 2018)
ZK: To my mother Mila and my children Mirabelle and Maximilien
JAS: To my parents, Claudio and Andrea, and my brother Emiliano
Abstract
We provide detailed descriptions, including over 550 mathematical formu-
las, for over 150 trading strategies across a host of asset classes (and trading
styles). This includes stocks, options, ﬁxed income, futures, ETFs, indexes,
commodities, foreign exchange, convertibles, structured assets, volatility (as
an asset class), real estate, distressed assets, cash, cryptocurrencies, miscel-
lany (such as weather, energy, inﬂation), global macro, infrastructure, and tax
arbitrage. Some strategies are based on machine learning algorithms (such as
artiﬁcial neural networks, Bayes, k-nearest neighbors). We also give: source
code for illustrating out-of-sample backtesting with explanatory notes; around
2,000 bibliographic references; and over 900 glossary, acronym and math def-
initions. The presentation is intended to be descriptive and pedagogical.
Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights Reserved.
1 Zura Kakushadze, Ph.D., is the President and CEO of Quantigic ® Solutions LLC, and a Full
Professor at Free University of Tbilisi. Email: zura@quantigic.com
2 Juan Andr´ es Serur, M.Fin., is an Assistant Professor at University of CEMA. Email:
jaserur15@ucema.edu.ar
3 DISCLAIMER: This address is used by the corresponding author for no purpose other than
to indicate his professional aﬃliation as is customary in publications. In particular, the contents
of this paper are not intended as an investment, legal, tax or any other such advice, and in no
way represent views of Quantigic® Solutions LLC, the website www.quantigic.com or any of their
other aﬃliates.
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 2

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Contents
Praises of 151 Trading Strategies 7
Author Biographies 9
Preface (by Zura Kakushadze) 10
1 Introduction and Summary 15
2 Options 17
2.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2 Strategy: Covered call . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3 Strategy: Covered put . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.4 Strategy: Protective put . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.5 Strategy: Protective call . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.6 Strategy: Bull call spread . . . . . . . . . . . . . . . . . . . . . . . . 19
2.7 Strategy: Bull put spread . . . . . . . . . . . . . . . . . . . . . . . . 20
2.8 Strategy: Bear call spread . . . . . . . . . . . . . . . . . . . . . . . . 20
2.9 Strategy: Bear put spread . . . . . . . . . . . . . . . . . . . . . . . . 20
2.10 Strategy: Long synthetic forward . . . . . . . . . . . . . . . . . . . . 21
2.11 Strategy: Short synthetic forward . . . . . . . . . . . . . . . . . . . . 21
2.12 Strategy: Long combo . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.13 Strategy: Short combo . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.14 Strategy: Bull call ladder . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.15 Strategy: Bull put ladder . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.16 Strategy: Bear call ladder . . . . . . . . . . . . . . . . . . . . . . . . 23
2.17 Strategy: Bear put ladder . . . . . . . . . . . . . . . . . . . . . . . . 23
2.18 Strategy: Calendar call spread . . . . . . . . . . . . . . . . . . . . . . 24
2.19 Strategy: Calendar put spread . . . . . . . . . . . . . . . . . . . . . . 24
2.20 Strategy: Diagonal call spread . . . . . . . . . . . . . . . . . . . . . . 25
2.21 Strategy: Diagonal put spread . . . . . . . . . . . . . . . . . . . . . . 25
2.22 Strategy: Long straddle . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.23 Strategy: Long strangle . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.24 Strategy: Long guts . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.25 Strategy: Short straddle . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.26 Strategy: Short strangle . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.27 Strategy: Short guts . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.28 Strategy: Long call synthetic straddle . . . . . . . . . . . . . . . . . . 28
2.29 Strategy: Long put synthetic straddle . . . . . . . . . . . . . . . . . . 28
2.30 Strategy: Short call synthetic straddle . . . . . . . . . . . . . . . . . 28
2.31 Strategy: Short put synthetic straddle . . . . . . . . . . . . . . . . . 29
2.32 Strategy: Covered short straddle . . . . . . . . . . . . . . . . . . . . 29
2.33 Strategy: Covered short strangle . . . . . . . . . . . . . . . . . . . . . 29
1
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 3

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.34 Strategy: Strap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2.35 Strategy: Strip . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2.36 Strategy: Call ratio backspread . . . . . . . . . . . . . . . . . . . . . 30
2.37 Strategy: Put ratio backspread . . . . . . . . . . . . . . . . . . . . . 31
2.38 Strategy: Ratio call spread . . . . . . . . . . . . . . . . . . . . . . . . 31
2.39 Strategy: Ratio put spread . . . . . . . . . . . . . . . . . . . . . . . . 31
2.40 Strategy: Long call butterﬂy . . . . . . . . . . . . . . . . . . . . . . . 32
2.40.1 Strategy: Modiﬁed call butterﬂy . . . . . . . . . . . . . . . . . 32
2.41 Strategy: Long put butterﬂy . . . . . . . . . . . . . . . . . . . . . . . 32
2.41.1 Strategy: Modiﬁed put butterﬂy . . . . . . . . . . . . . . . . . 33
2.42 Strategy: Short call butterﬂy . . . . . . . . . . . . . . . . . . . . . . 33
2.43 Strategy: Short put butterﬂy . . . . . . . . . . . . . . . . . . . . . . 33
2.44 Strategy: “Long” iron butterﬂy . . . . . . . . . . . . . . . . . . . . . 34
2.45 Strategy: “Short” iron butterﬂy . . . . . . . . . . . . . . . . . . . . . 34
2.46 Strategy: Long call condor . . . . . . . . . . . . . . . . . . . . . . . . 34
2.47 Strategy: Long put condor . . . . . . . . . . . . . . . . . . . . . . . . 35
2.48 Strategy: Short call condor . . . . . . . . . . . . . . . . . . . . . . . . 35
2.49 Strategy: Short put condor . . . . . . . . . . . . . . . . . . . . . . . . 35
2.50 Strategy: Long iron condor . . . . . . . . . . . . . . . . . . . . . . . . 36
2.51 Strategy: Short iron condor . . . . . . . . . . . . . . . . . . . . . . . 36
2.52 Strategy: Long box . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2.53 Strategy: Collar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2.54 Strategy: Bullish short seagull spread . . . . . . . . . . . . . . . . . . 37
2.55 Strategy: Bearish long seagull spread . . . . . . . . . . . . . . . . . . 38
2.56 Strategy: Bearish short seagull spread . . . . . . . . . . . . . . . . . 38
2.57 Strategy: Bullish long seagull spread . . . . . . . . . . . . . . . . . . 39
3 Stocks 40
3.1 Strategy: Price-momentum . . . . . . . . . . . . . . . . . . . . . . . . 40
3.2 Strategy: Earnings-momentum . . . . . . . . . . . . . . . . . . . . . . 41
3.3 Strategy: Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.4 Strategy: Low-volatility anomaly . . . . . . . . . . . . . . . . . . . . 42
3.5 Strategy: Implied volatility . . . . . . . . . . . . . . . . . . . . . . . . 43
3.6 Strategy: Multifactor portfolio . . . . . . . . . . . . . . . . . . . . . . 43
3.7 Strategy: Residual momentum . . . . . . . . . . . . . . . . . . . . . . 44
3.8 Strategy: Pairs trading . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.9 Strategy: Mean-reversion – single cluster . . . . . . . . . . . . . . . . 46
3.9.1 Strategy: Mean-reversion – multiple clusters . . . . . . . . . . 47
3.10 Mean-reversion – weighted regression . . . . . . . . . . . . . . . . . . 49
3.11 Strategy: Single moving average . . . . . . . . . . . . . . . . . . . . . 49
3.12 Strategy: Two moving averages . . . . . . . . . . . . . . . . . . . . . 50
3.13 Strategy: Three moving averages . . . . . . . . . . . . . . . . . . . . 51
3.14 Strategy: Support and resistance . . . . . . . . . . . . . . . . . . . . 51
2
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 4

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3.15 Strategy: Channel . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.16 Strategy: Event-driven – M&A . . . . . . . . . . . . . . . . . . . . . 52
3.17 Strategy: Machine learning – single-stock KNN . . . . . . . . . . . . 53
3.18 Strategy: Statistical arbitrage – optimization . . . . . . . . . . . . . . 55
3.18.1 Dollar-neutrality . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.19 Strategy: Market-making . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.20 Strategy: Alpha combos . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.21 A few comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4 Exchange-traded funds (ETFs) 61
4.1 Strategy: Sector momentum rotation . . . . . . . . . . . . . . . . . . 61
4.1.1 Strategy: Sector momentum rotation with MA ﬁlter . . . . . . 62
4.1.2 Strategy: Dual-momentum sector rotation . . . . . . . . . . . 62
4.2 Strategy: Alpha rotation . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.3 Strategy: R-squared . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.4 Strategy: Mean-reversion . . . . . . . . . . . . . . . . . . . . . . . . . 64
4.5 Strategy: Leveraged ETFs (LETFs) . . . . . . . . . . . . . . . . . . . 64
4.6 Strategy: Multi-asset trend following . . . . . . . . . . . . . . . . . . 65
5 Fixed Income 66
5.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5.1.1 Zero-coupon bonds . . . . . . . . . . . . . . . . . . . . . . . . 66
5.1.2 Bonds with coupons . . . . . . . . . . . . . . . . . . . . . . . 66
5.1.3 Floating rate bonds . . . . . . . . . . . . . . . . . . . . . . . . 67
5.1.4 Swaps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.1.5 Duration and convexity . . . . . . . . . . . . . . . . . . . . . . 68
5.2 Strategy: Bullets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.3 Strategy: Barbells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.4 Strategy: Ladders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
5.5 Strategy: Bond immunization . . . . . . . . . . . . . . . . . . . . . . 70
5.6 Strategy: Dollar-duration-neutral butterﬂy . . . . . . . . . . . . . . . 71
5.7 Strategy: Fifty-ﬁfty butterﬂy . . . . . . . . . . . . . . . . . . . . . . 72
5.8 Strategy: Regression-weighted butterﬂy . . . . . . . . . . . . . . . . . 72
5.8.1 Strategy: Maturity-weighted butterﬂy . . . . . . . . . . . . . . 73
5.9 Strategy: Low-risk factor . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.10 Strategy: Value factor . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.11 Strategy: Carry factor . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.12 Strategy: Rolling down the yield curve . . . . . . . . . . . . . . . . . 74
5.13 Strategy: Yield curve spread (ﬂatteners & steepeners) . . . . . . . . . 75
5.14 Strategy: CDS basis arbitrage . . . . . . . . . . . . . . . . . . . . . . 75
5.15 Strategy: Swap-spread arbitrage . . . . . . . . . . . . . . . . . . . . . 76
3
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 5

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
6 Indexes 76
6.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
6.2 Strategy: Cash-and-carry arbitrage . . . . . . . . . . . . . . . . . . . 77
6.3 Strategy: Dispersion trading in equity indexes . . . . . . . . . . . . . 77
6.3.1 Strategy: Dispersion trading – subset portfolio . . . . . . . . . 78
6.4 Strategy: Intraday arbitrage between index ETFs . . . . . . . . . . . 79
6.5 Strategy: Index volatility targeting with risk-free asset . . . . . . . . 80
7 Volatility 80
7.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
7.2 Strategy: VIX futures basis trading . . . . . . . . . . . . . . . . . . . 81
7.3 Strategy: Volatility carry with two ETNs . . . . . . . . . . . . . . . . 82
7.3.1 Strategy: Hedging short VXX with VIX futures . . . . . . . . 82
7.4 Strategy: Volatility risk premium . . . . . . . . . . . . . . . . . . . . 83
7.4.1 Strategy: Volatility risk premium with Gamma hedging . . . . 83
7.5 Strategy: Volatility skew – long risk reversal . . . . . . . . . . . . . . 84
7.6 Strategy: Volatility trading with variance swaps . . . . . . . . . . . . 84
8 Foreign Exchange (FX) 85
8.1 Strategy: Moving averages with HP ﬁlter . . . . . . . . . . . . . . . . 85
8.2 Strategy: Carry trade . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
8.2.1 Strategy: High-minus-low carry . . . . . . . . . . . . . . . . . 87
8.3 Strategy: Dollar carry trade . . . . . . . . . . . . . . . . . . . . . . . 88
8.4 Strategy: Momentum & carry combo . . . . . . . . . . . . . . . . . . 88
8.5 Strategy: FX triangular arbitrage . . . . . . . . . . . . . . . . . . . . 89
9 Commodities 89
9.1 Strategy: Roll yields . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
9.2 Strategy: Trading based on hedging pressure . . . . . . . . . . . . . . 90
9.3 Strategy: Portfolio diversiﬁcation with commodities . . . . . . . . . . 90
9.4 Strategy: Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
9.5 Strategy: Skewness premium . . . . . . . . . . . . . . . . . . . . . . . 91
9.6 Strategy: Trading with pricing models . . . . . . . . . . . . . . . . . 91
10 Futures 92
10.1 Strategy: Hedging risk with futures . . . . . . . . . . . . . . . . . . . 92
10.1.1 Strategy: Cross-hedging . . . . . . . . . . . . . . . . . . . . . 93
10.1.2 Strategy: Interest rate risk hedging . . . . . . . . . . . . . . . 93
10.2 Strategy: Calendar spread . . . . . . . . . . . . . . . . . . . . . . . . 94
10.3 Strategy: Contrarian trading (mean-reversion) . . . . . . . . . . . . . 95
10.3.1 Strategy: Contrarian trading – market activity . . . . . . . . . 95
10.4 Strategy: Trend following (momentum) . . . . . . . . . . . . . . . . . 96
4
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 6

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
11 Structured Assets 97
11.1 Generalities: Collateralized Debt Obligations (CDOs) . . . . . . . . . 97
11.2 Strategy: Carry, equity tranche – index hedging . . . . . . . . . . . . 99
11.3 Strategy: Carry, senior/mezzanine – index hedging . . . . . . . . . . 99
11.4 Strategy: Carry – tranche hedging . . . . . . . . . . . . . . . . . . . . 99
11.5 Strategy: Carry – CDS hedging . . . . . . . . . . . . . . . . . . . . . 100
11.6 Strategy: CDOs – curve trades . . . . . . . . . . . . . . . . . . . . . 100
11.7 Strategy: Mortgage-backed security (MBS) trading . . . . . . . . . . 100
12 Convertibles 101
12.1 Strategy: Convertible arbitrage . . . . . . . . . . . . . . . . . . . . . 101
12.2 Strategy: Convertible option-adjusted spread . . . . . . . . . . . . . . 102
13 Tax Arbitrage 102
13.1 Strategy: Municipal bond tax arbitrage . . . . . . . . . . . . . . . . . 102
13.2 Strategy: Cross-border tax arbitrage . . . . . . . . . . . . . . . . . . 103
13.2.1 Strategy: Cross-border tax arbitrage with options . . . . . . . 104
14 Miscellaneous Assets 104
14.1 Strategy: Inﬂation hedging – inﬂation swaps . . . . . . . . . . . . . . 104
14.2 Strategy: TIPS-Treasury arbitrage . . . . . . . . . . . . . . . . . . . 105
14.3 Strategy: Weather risk – demand hedging . . . . . . . . . . . . . . . 106
14.4 Strategy: Energy – spark spread . . . . . . . . . . . . . . . . . . . . . 108
15 Distressed Assets 108
15.1 Strategy: Buying and holding distressed debt . . . . . . . . . . . . . 108
15.2 Strategy: Active distressed investing . . . . . . . . . . . . . . . . . . 109
15.2.1 Strategy: Planning a reorganization . . . . . . . . . . . . . . . 109
15.2.2 Strategy: Buying outstanding debt . . . . . . . . . . . . . . . 109
15.2.3 Strategy: Loan-to-own . . . . . . . . . . . . . . . . . . . . . . 110
15.3 Strategy: Distress risk puzzle . . . . . . . . . . . . . . . . . . . . . . 110
15.3.1 Strategy: Distress risk puzzle – risk management . . . . . . . 110
16 Real Estate 111
16.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
16.2 Strategy: Mixed-asset diversiﬁcation with real estate . . . . . . . . . 111
16.3 Strategy: Intra-asset diversiﬁcation within real estate . . . . . . . . . 112
16.3.1 Strategy: Property type diversiﬁcation . . . . . . . . . . . . . 112
16.3.2 Strategy: Economic diversiﬁcation . . . . . . . . . . . . . . . . 112
16.3.3 Strategy: Property type and geographic diversiﬁcation . . . . 113
16.4 Strategy: Real estate momentum – regional approach . . . . . . . . . 113
16.5 Strategy: Inﬂation hedging with real estate . . . . . . . . . . . . . . . 113
16.6 Strategy: Fix-and-ﬂip . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
5
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 7

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
17 Cash 114
17.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
17.2 Strategy: Money laundering – the dark side of cash . . . . . . . . . . 114
17.3 Strategy: Liquidity management . . . . . . . . . . . . . . . . . . . . . 115
17.4 Strategy: Repurchase agreement (REPO) . . . . . . . . . . . . . . . . 115
17.5 Strategy: Pawnbroking . . . . . . . . . . . . . . . . . . . . . . . . . . 115
17.6 Strategy: Loan sharking . . . . . . . . . . . . . . . . . . . . . . . . . 116
18 Cryptocurrencies 116
18.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
18.2 Strategy: Artiﬁcial neural network (ANN) . . . . . . . . . . . . . . . 116
18.3 Strategy: Sentiment analysis – na¨ ıve Bayes Bernoulli . . . . . . . . . 120
19 Global Macro 121
19.1 Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
19.2 Strategy: Fundamental macro momentum . . . . . . . . . . . . . . . 122
19.3 Strategy: Global macro inﬂation hedge . . . . . . . . . . . . . . . . . 122
19.4 Strategy: Global ﬁxed-income strategy . . . . . . . . . . . . . . . . . 123
19.5 Strategy: Trading on economic announcements . . . . . . . . . . . . . 123
20 Infrastructure 123
Acknowledgments 124
A R Source Code for Backtesting 125
B DISCLAIMERS 132
References 134
Glossary 279
Acronyms 336
Some Math Notations 340
Explanatory Comments for Index 341
Index 342
6
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 8

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Praises of 151 Trading Strategies
“If you want to work as a trader or quant on Wall Street, you have to walk the
walk and talk the talk. This unique book is a comprehensive introduction to a wide
variety of tried and tested trading strategies. I highly recommend a 152nd trading
strategy called buy this book!”
–Peter Carr , Professor and Chair of Finance and Risk Engineering Depart-
ment, NYU’s Tandon School of Engineering; and 2010 Financial Engineer of the
Year, International Association for Quantitative Finance & Sungard
“This book is an encyclopedic guided tour of “quant” investment strategies, from
the simplest ones (like trend following) to much more exotic ones using sophisticated
derivative contracts. No claim is made about the proﬁtability of these strategies: one
knows all too well how much implementation details and transaction costs matter.
But no quant trader can aﬀord ignoring what’s out there, as a source of inspiration
or as a benchmark for new ideas.”
–Jean-Philippe Bouchaud, Chairman and Chief Scientist, Capital Fund Man-
agement; Professor, ´Ecole Normale Sup´ erieure; Member, French Academy of Sci-
ences; and Co-Director, CFM-Imperial Institute of Quantitative Finance
“Zura Kakushadze and Juan Andr´ es Serur have created a masterful encyclopedia
of quantitative trading strategies. The authors oﬀer us a rigorous but accessible
treatment of the mathematical foundations of these strategies. The coverage is
comprehensive, starting with simple and well-known strategies such as covered call
and then moving naturally to strategies involving cryptocurrencies. The supporting
material such as a detailed glossary and an extensive list of references will make this
book an essential reference for ﬁnancial economists and investment professionals.”
–Hossein Kazemi , Michael & Cheryl Philipp Endowed Professor of Finance,
University of Massachusetts at Amherst; and Editor-in-Chief, The Journal of Alter-
native Investments
“The successful trading of ﬁnancial instruments is both a science and an art, just as
the eﬀorts of a chef reﬂect both gastronomic artistry and the underlying chemical
and thermal processes of cooking. In 151 Trading Strategies ﬁnancial traders are
provided with a compendium of sound recipes, spanning the broad range of meth-
ods that can be applied to modern investment practice. The exposition of both the
mathematics and intuition of each described trade is clear and concise. Readers will
appreciate the inclusion of extensive computer code so as to reduce eﬀort needed to
implement any required calculations.”
–Dan diBartolomeo, President, Northﬁeld Information Services; and Editor,
Journal of Asset Management
“A real tour de force– 151 Trading Strategies provides the most comprehensive un-
7
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 9

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
covering of popular hedge fund strategies. By revealing all the hedge funds’ secret
sauce, Kakushadze and Serur have now rendered everything as beta-strategies. Time
to lower ’em fees!”
–Jim Kyung-Soo Liew, Assistant Professor of Finance, Carey Business School,
Johns Hopkins University; Advisory Board Member, The Journal of Portfolio Man-
agement; and Co-Founder, SoKat
“This book is an impressive concentration of strategies and formulas to expand
knowledge in quantitative ﬁnance; it’s a must-read for anyone who wants to drasti-
cally improve his or her expertise in ﬁnancial markets dynamics.”
–Daniele Bernardi , CEO, DIAMAN Capital; and Chairman of the Board,
INVESTORS’ Magazine Italia
8
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 10

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Author Biographies
Zura Kakushadze received his Ph.D. in theoretical physics from Cornell Univer-
sity, USA at 23, was a Postdoctoral Fellow at Harvard University, USA and an
Assistant Professor at C.N. Yang Institute for Theoretical Physics at Stony Brook
University, USA. He received an Alfred P. Sloan Foundation Fellowship in 2001.
After expanding into quantitative ﬁnance, he was a Director at RBC Capital Mar-
kets, Managing Director at WorldQuant, Executive Vice President and substantial
shareholder at Revere Data (now part of FactSet), and Adjunct Professor at the Uni-
versity of Connecticut, USA. Currently he is the President and CEO of Quantigic ®
Solutions and a Full Professor at Free University of Tbilisi, Georgia. He has over
17 years of hands-on experience in quantitative trading and ﬁnance, 130+ publi-
cations in physics, ﬁnance, cancer research and other ﬁelds, 3,400+ citations and
h-index 30+, 170,000+ downloads on SSRN, and over a quarter million followers on
LinkedIn.
Juan Andr´ es Serurholds a Master’s Degree in Finance from the University of
CEMA, Argentina. With more than 6 years of experience in trading in the stock
market, he currently works as a quantitative analyst and strategist in an Argentine
quantitative asset management ﬁrm and as a ﬁnancial consultant for large corpo-
rations. In addition, he serves as the Academic Secretary of the Master of Finance
Program at the University of CEMA, where he teaches undergraduate and postgrad-
uate computational ﬁnance courses as an Assistant Professor. In 2016 he won the
First Prize in an Argentine Capital Markets Simulation Challenge for Universities
and Professional Institutions.
9
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 11

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Preface (by Zura Kakushadze)
The purpose of this “post-factum” Preface is to give some history, which sheds light
on why we (the authors) have decided to make this book, which has been published
in hardcover (and as an e-book), 4 into a freely downloadable PDF e-book on SSRN.
In December of 2015 I posted the paper “101 Formulaic Alphas” on SSRN
[Kakushadze, 2016], which provides explicit formulas (that are also computer source
code) for 101 real-life formulaic quantitative trading alphas. That paper was a hit
– in hindsight, perhaps unsurprisingly, considering how secretive quant trading is.
So, at some point down the road, a light bulb went on in my head and I got this
seemingly “crazy” idea to write a paper entitled “101 Trading Strategies”, except
that this time these 101 strategies would be spread across all asset classes (as opposed
to equities (StatArb) quant trading alphas as in “101 Formulaic Alphas”). I did not
envision this as a book, just as a paper, maybe 100+ pages long, 1 page per strategy
on average, plus overhead (introduction, references, etc.), something publishable in
a journal (at least online). I also thought it would be both fun and eﬃcient to get
around 10-12 coauthors together, each would contribute about 10 strategies in one
or two asset classes according to their ﬁelds of expertise, so the project would go
faster. So, I pinged my contacts by email and posted several posts in the LinkedIn
feed and groups saying that I was looking for collaborators for this project. I got a
rather decent number of responses, some evidently were not serious, but some were.
However, once I outlined in more detail what I had in mind for this project – I
had a written plan – apparently people realized that this would not be a cakewalk,
and most disappeared. As it turned out, the only person who was truly serious
about this project was Juan Andr´ es Serur, a young professor from Buenos Aires,
Argentina, whom I had never even met in person. There were a lot of challenges
along the way (including that Juan had never worked on a project of this magnitude
and was learning on the job, so to speak). But at the end we got through it. Except
that we did not have just 100+ pages with 101 strategies but over 350 pages with
around 160-170 strategies (depending on how one counts). This was not publishable
in any journal, by any stretch. This project basically had taken on a life of its own
and turned into... a book. So, we discussed it and decided to publish it as such.
Publishing a quant trading/ﬁnance book such as “151 Trading Strategies” is not
a very rewarding business (at least ﬁnancially), for several reasons. First, the target
audience is rather limited because of the highly technical nature of the material.
In my original exploratory call with them, the publisher mentioned that books like
this sell around 1,000 copies total. This was consistent with what I was told by
someone who is well-known in the ﬁeld and had published 5 quant trading/ﬁnance
books over the years, which had sold around 5,000 copies altogether. Second, if the
book is published by a major publisher, the authors get dismal royalties, usually
in the 8-12% range, which can go to around 20% if the book sells better than
4 Z. Kakushadze and J.A. Serur. 151 Trading Strategies. Cham, Switzerland: Palgrave Macmil-
lan, an imprint of Springer Nature, 1st Edition (2018), XX, 480 pp; ISBN 978-3-030-02791-9.
10
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 12

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
expected. At $60-$70 for a hardcover, your book has to sell 100,000+ copies for
you to make any decent money so it is a least somewhat commensurate with the
time you spend on writing the book – this book took about 9 months to write,
not including the time I spent on it before drafting started (conceiving it, looking
for coauthors, etc.) or the time spent dealing with the publisher, advertising it,
etc. Third, this particular publisher does not publish paperbacks as a matter of
some policy I do not comprehend, and when the price is set around $60-$70 for
a hardcover, the pool of potential buyers is dramatically reduced compared with
a $20-$30 price point a paperback would have. Fourth, there are plenty of people
working in quant trading/ﬁnance who can easily aﬀord $60-$70, but many of these
people – not to oﬀend anyone – would rather download a pirated PDF copy from the
internet... Fifth, the publisher’s business model appears to be immune to the fact
that they cannot make much money from hardcover sales. Instead, their business
model appears to hinge on e-book downloads through their existing (institutional)
subscriptions: a subscriber, who pays a subscription fee, can freely download any
book from the publisher’s portfolio. So, the success of a book is measured by e-book
downloads by subscribers, not by hardcover sales, and the authors do not get paid
per download, they only get paid a very symbolic (mildly put) ﬂat fee irrespective
of the number of such downloads. The bottom line is that there is no money to be
made in this business for the authors. We were well-aware of this from the get-go.
We did not publish this book for money – originally, it was going to be a paper.
What is worse though is that, unlike in the olden days when editors would read
every word of your manuscript and mark it up so it could be improved, etc., nowadays
there appears to be little to no editorial support. We wrote the manuscript in LaTeX
(as there are over 550 elevated equations in the book, not counting inline math), we
created the index ourselves (which is a major pain and very time-consuming, if done
right; in fact, it is probably the single worst part of writing a book), and proofread
the manuscript several times to the point where upon the ﬁnal proofreading right
before printing we found only 5 minor typos attributable to our original manuscript.
The bottom line is that we spent a lot of time perfecting our manuscript and it was
very much print-ready. However, things got really messy on the publisher’s end.
The nightmare started with the book cover. The publisher ask me if I had any
concrete ideas for how I wanted the cover designed, and if I had a speciﬁc cover
image in mind and to feel free to send along some images from Getty and Alamy
(the image providers the publisher uses). I was taken aback. They keep almost
all the proﬁts and they ask me for the cover design? If we have to design our
own cover, then we might as self-well publish and keep most royalties. I told them
to design the cover professionally, as this was their responsibility. Their so-called
“designs” they forwarded were highly unimpressive (just really super-minimalist –
mildly put). So, I ended up designing the cover myself, including picking the cover
image from the library of thousands of available images, placing the title and author
names on the cover, etc. Their “design team” used my cover design and the only
“substantial” change they made was changing the color of the title fonts to (in my
11
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 13

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
humble opinion) suboptimal white – the publisher said they could not accommodate
the color I suggested. So, imagine how appalled and taken aback I was when in the
ready-to-publish ﬁnal book version, on the copyright page, they put some name for
the cover design credit, and did not even mention mine. They said the cover design
“is theirs”, apparently referring to their “design team”. This was just factually false.
But we did not wish to appear “diﬃcult” or “unaccommodating”, so we let this go.
However, the nightmare continued with author biographies on an inside ﬂap of
the dust jacket. They asked us to provide our headshots. We did. At least three
times they produced the author biographies with one of the headshots sizably larger
than the other, even though we provided identically sized headshots. Worse yet,
they claimed that the headshots on the dust jacket were the same size when they
clearly were not. So, again, not to appear “diﬃcult” or “unaccommodating”, having
wasted an inordinate amount of time on this, we let them leave our headshots out of
the inside ﬂap as their “design team” either could not or would not get them right.
Little did we know that this was only the tip of the iceberg. When we ﬁnally
(and belatedly) received the proofs from the publisher, we found over 100 typos
introduced by the publisher’s typesetters in most incomprehensible ways. Worse yet,
the one inadvertent grammar typo we did have in our original manuscript (along
with four other, more subtle, non-grammar typos) was not ﬁxed. It was painfully
evident that they did not proofread the manuscript very carefully – them creating
100+ unfathomable typos speaks volumes. So, we spent countless additional hours
ﬁxing their typos, and it took more than one round of revisions for them to get it
right. In hindsight, this should come as no surprise: as many other publishers, they
apparently outsource typesetting, copyediting, cover design, etc., to a developing
country, and I highly doubt that, e.g., the English proﬁciency on the other end of
this outsourcing process is top-notch. It is the all-familiar and prevalent sad story:
English-language books are produced by people whose ﬁrst language is not English.
Finally, the book was online. However, the nightmare continued. There is an
appendix in the book with computer source code and a lengthy discussion. This
appendix was just another chapter in the book and was not supposed to be a part
of the free preview of the book, which we expressly discussed and agreed on with
the publisher in writing to be limited to the ﬁrst two chapters. Yet, they included
the appendix in the back matter of the book, which is freely downloadable from
the publisher’s website along with the front matter. When I pointed this out to the
publisher, their reply was that, for them to redo the ﬁles, it would delay the release of
the book accordingly (and, based on prior history, that meant weeks, if not longer).
This was already after multiple delays on the publisher’s end. So, once again, not to
appear “diﬃcult” or “unaccommodating”, we let this go and the appendix stayed
in the freely-downloadable back matter. Speaking of which, while in our original
manuscript all references were in one place, at the end, in the published version the
references were cited at the end of each chapter. However, the publisher – for the
reasons we do not comprehend – also kept the full list of references in the freely-
downloadable back matter. While in the modular (where all chapters, front matter
12
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 14

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
and back matter have separate PDF ﬁles) electronic e-book version this is not a big
deal, they actually also included these duplicate references in the back matter in the
printed version, which substantially (and artiﬁcially) increased its number of pages.
But there is more. One would imagine that their production team would do some
basic quality control post-production. Months later we found out that the Kindle
version on Amazon was all messed up, with equations not displaying properly, etc.
The publisher claimed that they provided correct ﬁles to Amazon and that the
problem was on Amazon’s end. It took them several weeks to ﬁx this issue, and
the ﬁx was a “hack”: they replaced the Kindle version with the so-called “replica”
version, which is just a replica of the PDF. Anyone can easily create a “replica”
version from a PDF using Kindle Create – this does not take a leading publisher.
Furthermore, the Kindle preview version displays material substantially outside of
the preview material we agreed on. But then again, who cares about the authors?
Nor did the publisher seem to care much about the apparent pirated versions
of the book PDF appearing on various websites. Basically, it was unclear what, if
anything, the publisher was doing for the book. Their entire marketing eﬀort was
apparently limited to whopping two tweets they sent when the book was published.
Essentially all the marketing eﬀorts came from me promoting the book on LinkedIn
(where I have over quarter million followers) by posting links to the preview version
then-available on SSRN and the full version/hardcover on the publisher’s websites.
Perhaps most unfathomably, not only did the publisher apparently did not do
much to protect the book from pirated copies being available on the internet, or
to promote the book, they outright refused to refute a factually false and defama-
tory “review” an anonymous purchaser placed on Amazon. E.g., that review falsely
claims that “there is only a tiny paragraph (no more than 10 lines), very general,
on each strategy and then close to 10 pages of book references after each strategy.”
This is factually false: there are not “10 pages of book references after each strat-
egy”. There are references after each chapter (not strategy or section) pursuant
to the publisher’s own formatting (see above). The review also falsely claims that
“A 10 line description of a very general strategy, no math, no backrest, no opti-
mization.” Again, this is factually false: as the reader can readily see, the book
has over 550 elevated equations (not counting lots of math embedded in the text),
the source code for backtesting in Appendix A, strategies involving optimization,
900+ glossary terms, acronyms and math deﬁnitions, etc. Furthermore, simpler
strategies have concise (but precise) descriptions, while others span pages, not “10
lines”, contrary to what the review falsely claims. The review also complains about
the number of references in the book. The book description on Amazon (as well as
the publisher’s websites) expressly states that there are around 2,000 bibliographic
references in the book, one of whose aims is to serve as a reference guide into (and
essentially an encyclopedia of) trading strategies (which is also stated in the Edi-
torial Reviews of the book). Therefore, the anonymous reviewer was well aware of
this before purchasing the book. The review further falsely claims: “And then, as
if it were not enough, at the end of the book the author recaps all the references
13
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 15

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
one more time.” The review is expressly attacking “the author” of the book, even
though, as mentioned above, the speciﬁc formatting of the references (whereby the
references pertinent to each chapter are included after each chapter, and all refer-
ences are also included in the back matter, which is freely downloadable from the
publisher’s website) was performed by the publisher, not by the authors. Our origi-
nal manuscript has references only at the end. Again, as mentioned above, why the
publisher duplicated the references both after the chapters and in the back matter
is not something we understand, and it is not something we did or had control over,
contrary to the anonymous reviewer’s factually false and defamatory statements.
When we discovered the aforesaid factually false and defamatory review on Ama-
zon, we contacted the publisher and asked them, at the minimum to put a comment
on the review refuting its factually false statements, and also to contact Amazon to
remove the review (as under Amazon’s policies, defamatory reviews are not allowed).
To our bewilderment, the publisher suggested that we use our contacts to generate
positive reviews on Amazon to counteract that negative review. Incredible, isn’t it?
To be clear, having over a quarter million followers on LinkedIn and putting lots
of content out there on social media, I have had my share of haters. And one thing
I have learned is that there is some truth to the common expression “haters make
us famous”. When you write a paper or a book or anything else you stick your neck
out with, it comes with the territory: some will love it, some will hate it, and some
will not care. I write things for the “some-will-love-it” demographic and I do not
care about the rest. However, there is a big diﬀerence between someone expressing
a negative opinion about what you have written – this is perfectly acceptable, we
live in a free country with freedom of speech – and someone making factually false
and defamatory statements, which is not acceptable. And when you write a book
and grant the publisher all kinds of rights for the book, it falls onto the publisher to
protect its integrity and reputation, as the publisher owns the rights to the book.
There is a lesson to be learned from all this. That a large publisher will do
little to nothing to protect the integrity and reputation of the book or its authors
(especially if it involves a potential headache with Amazon) or to promote the book.
So, as an author, you do all the hard work, and your publisher just takes over your
sweat-and-blood creation, makes money from it, while you do all the work promoting
the book, with little to no support from the publisher, including protecting the book
from, e.g., being pirated on the internet, defamed, etc. Is this fair? Absolutely not!
So, we have terminated the publishing agreement and are making our work free
for everyone to download and beneﬁt from the knowledge we have compiled in this
now-free e-book. We hope you enjoy it and thanks for reading our book and our
story, which hopefully will also be useful to other authors contemplating publishing
a book. Consider this. Without real editorial support, when you have to design the
book cover, deal with a large number of typos introduced by the typesetters, etc.,
is publishing with a big-name publisher all that diﬀerent from “vanity publishing”?
Finally, I will let you read the book. Innovate. Disrupt. Spread the knowledge.
14
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 16

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
1 Introduction and Summary
A trading strategy can be deﬁned as a set of instructions to achieve certain asset
holdings by some predeﬁned times t1, t2, . . ., which holdings can (but need not) be
null at one or more of these times. In many cases, the main objective of a trading
strategy is to make a proﬁt, i.e., to generate a positive return on its investment.
However, some viable trading strategies are not always outright proﬁtable as stand-
alone strategies. E.g., a hedging strategy can be a part of a bigger plan, which itself
can but need not be a trading strategy. Thus, an airline hedging against rising fuel
costs with commodity futures is a trading strategy, which is a risk-management step
in executing the airline’s business strategy of generating proﬁts through its services.
In the case of trading strategies that are intended to be outright proﬁtable as
stand-alone strategies, one may argue that the phrase “buy low, sell high” captures
their essence. However this viewpoint is somewhat superﬂuous and, while it applies
to trading strategies that buy and sell a single asset (e.g., a single stock), it would
exclude a whole host of viable strategies that do not work quite like that. E.g., a
trading strategy that uses a hedging sub-strategy for risk management may not al-
ways “buy low, sell high” when it comes to a particular asset in its portfolio. This is
because hedging risk – or, essentially, transferring some risk to other market partic-
ipants – is not free, and often a trader will pay a premium for hedging some risks in
a trading strategy to achieve its objectives. Another example would be the so-called
statistical arbitrage, wherein the trading portfolio can consist of, e.g., thousands of
stocks and proﬁtability is typically not achieved by buying low and selling high each
stock or even any discernable groups of stocks, but statistically, across all stocks,
with some trades making money and some losing it. It gets complicated quickly.
The purpose of these notes is to collect a variety of trading strategies in the
context of ﬁnance (as opposed to trading baseball cards, classic cars, etc.) across
essentially all (or at least most frequently encountered) asset classes. Here we delib-
erately use the term “asset class” somewhat loosely and include what can be referred
to as “asset sub-classes”. Thus, a narrower deﬁnition would include stocks, bonds,
cash, currencies, real estate, commodities and infrastructure. However, this deﬁni-
tion would be too narrow for our purposes here. We also consider: derivatives such
as options and futures; exchange-traded funds (ETFs); indexes (which are usually
traded through vehicles such as ETFs and futures); volatility, which can be treated
as an asset class (and traded via, among other things, exchange-traded notes); struc-
tured assets (such as collateralized debt obligations and mortgage-backed securities);
convertible bonds (which represent a hybrid between bonds and stocks); distressed
assets (which are not a separate asset class per se, but the corresponding trading
strategies are rather distinct); cryptocurrencies; miscellaneous assets such as weather
and energy (derivatives); and also trading strategies such as tax arbitrage and global
macro (which use some assets mentioned above as tradables). Some strategies are
relatively simple and can be described in words, while many (in fact, most) require
a much more detailed mathematical description, which we provide formulaically.
15
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 17

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
It is important to bear in mind that, unlike the laws of nature (physics), which
(apparently) are set in stone and do not change in time, ﬁnancial markets are man-
made and change essentially continuously, and at times quite dramatically. One of
the consequences of this transiency is that trading strategies that may have worked
well for some time, may die, sometimes quite abruptly. E.g., when the New York
Stock Exchange (NYSE) started switching away from its human-operated “special-
ist” system to electronic trading beginning late 2006, 5 many statistical arbitrage
strategies that were proﬁtable for years prior to that, pretty much died overnight
as volatility increased and what used to do the trick before no longer did. Eventu-
ally the market was ﬂooded with high frequency trading (HFT) 6 strategies further
diminishing proﬁt margins of many “good old” trading strategies and killing them.
However, technological advances gave rise to new types of trading, including
ubiquitous trading strategies based on data mining and machine learning, which
seek to identify – typically quite ephemeral – signals or trends by analyzing large
volumes of diverse types of data. Many of these trading signals are so faint that
they cannot be traded on their own, so one combines thousands, in fact, tens or
even hundreds of thousands if not millions of such signals with nontrivial weights
to amplify and enhance the overall signal such that it becomes tradable on its own
and proﬁtable after trading costs and slippage, including that inﬂicted by HFT. 7
Considering the intrinsically ephemeral nature of the ﬁnancial markets and trad-
ing strategies designed to make a proﬁt therefrom, the purpose of these notes is not
to convey to the reader how to make money using any trading strategy but simply to
provide information on and give some ﬂavor of what kind of trading strategies peo-
ple have considered across a broad cross-section of asset classes and trading styles.
In light of the foregoing, we make the following DISCLAIMER: Any information or
opinions provided herein are for informational purposes only and are not intended,
and shall not be construed, as an investment, legal, tax or any other such advice,
or an oﬀer, solicitation, recommendation or endorsement of any trading strategy,
security, product or service. For further legal disclaimers, see Appendix B hereof.
We hope these notes will be useful to academics, practitioners, students and
aspiring researchers/traders for years to come. These notes intentionally – not to
duplicate prior literature and to avoid this manuscript spanning thousands of pages –
do not contain any numeric simulations, backtests, empirical studies, etc. However,
we do provide an eclectic cornucopia of references, including those with detailed
empirical analyses. Our purpose here is to describe, in many cases in sizable detail,
various trading strategies. Also, Appendix A provides source code for illustrating
out-of-sample backtesting (see Appendix B for legalese). 8 So, we hope you enjoy!
5 NYSE ﬁrst started with its “Hybrid Market” (see, e.g., [Hendershott and Moulton, 2011]).
However, the writing had been on the wall for the ultimate demise of the specialist system for
quite some time. For a timeline, see, e.g., [Pisani, 2010].
6 See, e.g., [Aldridge, 2013], [Lewis, 2014].
7 See, e.g., [Kakushadze and Tulchinsky, 2016], [Kakushadze and Yu, 2017b].
8 The code in Appendix A is not written to be “fancy” or optimized for speed or otherwise.
16
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 18

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2 Options
2.1 Generalities
An option is a form of a ﬁnancial derivative. It is a contract sold by the option writer
to the option holder. Typically, an option gives the option holder the right, but not
the obligation, to buy or sell an underlying security or ﬁnancial asset (e.g., a share
of common stock) at an agreed-upon price (referred to as the strike price) during a
certain period of time or on a speciﬁc date (referred to as the exercise date). A buyer
pays a premium to the seller for the option. For option pricing, see, e.g., [Harrison
and Pliska, 1981], [Baxter and Rennie, 1996], [Hull, 2012], [Kakushadze, 2015a].
A European call option is a right (but not an obligation) to buy a stock at the
maturity time T for the strike price k agreed on at time t = 0. The claim for the call
option fcall(ST , k) = (ST− k)+. Here ( x)+ = x if x > 0, and ( x)+ = 0 if x≤ 0. By
the “claim” we mean how much the option is worth at maturityT . If the stock price
at maturity ST > k, then the option holder gains ST− k (excluding the cost paid for
the option at t = 0). If the price at maturity ST≤ k, then there is no proﬁt to be
made from the option as it makes no sense to exercise it if ST < k (as it is cheaper
to buy the stock in the market) and it makes no diﬀerence if ST = k – all this is
assuming no transaction costs. Similarly, a European put option is a right (but not
an obligation) to sell a stock at the maturity time T for the strike price k agreed on
at time t = 0. The claim for the put option is given by fput(ST , k) = (k− ST )+.
Options can be issued on a variety of underlying assets, e.g., equities (single-
stock options), bonds, futures, indexes, commodities, currencies, etc. For the sake of
terminological convenience and deﬁniteness, in the following we will frequently refer
to the underlying asset as “stock”, even though in many cases the discussion can be
readily generalized to other assets. Furthermore, there is a variety of option styles
(beyond European options – for European options, see, e.g., [Black and Scholes,
1973]), e.g., American options (that can be exercised on any trading day on or
before expiration – see, e.g., [Kim, 1990]), Bermudan options (that can be exercised
only on speciﬁed dates on or before expiration – see, e.g., [Andersen, 1999]), Canary
options (that can be exercised, say, quarterly, but not before a determined time
period, say, 1 year, has elapsed – see, e.g., [Henrard, 2006]), Asian options (whose
payoﬀ is determined by the average underlying price over some preset time period
– see, e.g., [Rogers and Shi, 1995]), barrier options (which can be exercised only if
the underlying security’s price passes a certain level or “barrier” – see, e.g., [Haug,
2001]), other exotic options (a broad category of options that typically are complexly
structured – see, e.g., [Fabozzi, 2002]), etc. Let us also mention binary (a.k.a. all-
or-nothing or digital) options (that pay a preset amount, say, $1, if the underlying
security meets a predeﬁned condition on expiration, otherwise they simply expire
without paying anything to the holder – see, e.g., [Breeden and Litzenberger, 1978]).
Some trading strategies can be built using, e.g., combinations of options. Such
trading strategies can be divided into two groups: directional and non-directional.
17
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 19

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Directional strategies imply an expectation on the direction of the future stock price
movements. Non-directional (a.k.a. neutral) strategies are not based on the future
direction: the trader is oblivious to whether the stock price goes up or down.
Directional strategies can be divided into two subgroups: (i) bullish strategies,
where the trader proﬁts if the stock price goes up; and (ii) bearish strategies, where
the trader proﬁts if the stock price goes down. Non-directional strategies can be
divided into two subgroups: (a) volatility strategies that proﬁt if the stock has large
price movements (high volatility environment); and (b) sideways strategies that
proﬁt if the stock price remains stable (low volatility environment). Also, one can
distinguish income, capital gain, hedging strategies, etc. (see, e.g., [Cohen, 2005]).
In the remainder of this section, unless stated otherwise, all options are for the
same stock and have the same time-to-maturity (TTM). The moneyness abbrevia-
tions are: ATM = at-the-money, ITM = in-the-money, OTM = out-of-the-money.
Also: fT is the payoﬀ at maturity T ; S0 is the stock price at the time t = 0 of
entering the trade (i.e., establishing the initial position); ST is the stock price at
maturity; C is the net credit received at t = 0, and D is the net debit required at
t = 0, as applicable; H = D (for a net debit trade) or H =−C (for a net credit
trade);9 S∗up and S∗down are the higher and lower break-even (i.e., for which fT = 0)
stock prices at maturity; if there is only one break-even price, it is denoted by S∗;
Pmax is the maximum proﬁt at maturity; Lmax is the maximum loss at maturity.
2.2 Strategy: Covered call
This strategy (a.k.a. “buy-write” strategy) amounts to buying stock and writing a
call option with a strike price K against the stock position. The trader’s outlook on
the stock price is neutral to bullish. The covered call strategy has the same payoﬀ as
writing a put option (short/naked put).10 While maintaining the long stock position,
the trader can generate income by periodically selling OTM call options. We have:11
fT = ST− S0− (ST− K)+ + C = K− S0− (K− ST )+ + C (1)
S∗ = S0− C (2)
Pmax = K− S0 + C (3)
Lmax = S0− C (4)
2.3 Strategy: Covered put
This strategy (a.k.a. “sell-write” strategy) amounts to shorting stock and writing a
put option with a strike price K against the stock position. The trader’s outlook is
9 H is the net debit for all bought option premia less the net credit for all sold option premia.
10 This is related to put-call parity (see, e.g., [Stoll, 1969], [Hull, 2012]).
11 For some literature on covered call strategies, see, e.g., [Pounds, 1978], [Whaley, 2002], [Feld-
man and Roy, 2004], [Hillet al, 2006], [Kapadia and Szado, 2007], [Che and Fung, 2011], [Mugwagwa
et al , 2012], [Israelov and Nielsen, 2014], [Israelov and Nielsen, 2015a], [Hemler and Miller, 2015].
18
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 20

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
neutral to bearish. The covered put strategy has the same payoﬀ as writing a call
option (short/naked call). While maintaining the short stock position, the trader
can generate income by periodically selling OTM put options. We have: 12
fT = S0− ST− (K− ST )+ + C = S0− K− (ST− K)+ + C (5)
S∗ = S0 + C (6)
Pmax = S0− K + C (7)
Lmax = unlimited (8)
2.4 Strategy: Protective put
This strategy (a.k.a. “married put” or “synthetic call”) amounts to buying stock
and an ATM or OTM put option with a strike price K≤ S0. The trader’s outlook
is bullish. This is a hedging strategy: the put option hedges the risk of the stock
price falling. We have: 13
fT = ST− S0 + (K− ST )+− D = K− S0 + (ST− K)+− D (9)
S∗ = S0 + D (10)
Pmax = unlimited (11)
Lmax = S0− K + D (12)
2.5 Strategy: Protective call
This strategy (a.k.a. “married call” or “synthetic put”) amounts to shorting stock
and buying an ATM or OTM call option with a strike price K≥ S0. The trader’s
outlook is bearish. This is a hedging strategy: the call option hedges the risk of the
stock price rising. We have: 14
fT = S0− ST + (ST− K)+− D = S0− K + (K− ST )+− D (13)
S∗ = S0− D (14)
Pmax = S0− D (15)
Lmax = K− S0 + D (16)
2.6 Strategy: Bull call spread
This is a vertical spread consisting of a long position in a close to ATM call option
with a strike price K1, and a short position in an OTM call option with a higher
12 The covered put option strategy is symmetrical to the covered call option strategy. Academic
literature on the covered put option strategy appears to be scarce. See, e.g., [Che, 2016].
13 For some literature on protective put strategies, see, e.g., [Figlewski, Chidambaran and Ka-
plan, 1993], [Israelov and Nielsen, 2015b], [Israelov, Nielsen and Villalon, 2017], [Israelov, 2017].
14 The protective call option strategy is symmetrical to the protective put option strategy.
Academic literature on the protective call option strategy appears to be scarce. See, e.g., [Jabbour
and Budwick, 2010], [Tokic, 2013].
19
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 21

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
strike price K2. This is a net debit trade. The trader’s outlook is bullish: the
strategy proﬁts if the stock price rises. This is a capital gain strategy. We have: 15
fT = (ST− K1)+− (ST− K2)+− D (17)
S∗ = K1 + D (18)
Pmax = K2− K1− D (19)
Lmax = D (20)
2.7 Strategy: Bull put spread
This is a vertical spread consisting of a long position in an OTM put option with
a strike price K1, and a short position in another OTM put option with a higher
strike price K2. This is a net credit trade. The trader’s outlook is bullish. This is
an income strategy. We have:
fT = (K1− ST )+− (K2− ST )+ + C (21)
S∗ = K2− C (22)
Pmax = C (23)
Lmax = K2− K1− C (24)
2.8 Strategy: Bear call spread
This is a vertical spread consisting of a long position in an OTM call option with a
strike price K1, and a short position in another OTM call option with a lower strike
price K2. This is a net credit trade. The trader’s outlook is bearish. This is an
income strategy. We have:
fT = (ST− K1)+− (ST− K2)+ + C (25)
S∗ = K2 + C (26)
Pmax = C (27)
Lmax = K1− K2− C (28)
2.9 Strategy: Bear put spread
This is a vertical spread consisting of a long position in a close to ATM put option
with a strike price K1, and a short position in an OTM put option with a lower
15 For some literature on bull/bear call/put vertical spreads, see, e.g., [Cartea and Pedraz,
2012], [Chaput and Ederington, 2003], [Chaput and Ederington, 2005], [Chen, Chen and Howell,
1999], [Cong, Tan and Weng, 2013], [Cong, Tan and Weng, 2014], [Matsypura and Timkovsky,
2010], [Shah, 2017], [Wong, Thompson and Teh, 2011], [Zhang, 2015]. Also see [Clarke, de Silva
and Thorley, 2013], [Cohen, 2005], [Jabbour and Budwick, 2010], [McMillan, 2002], [The Options
Institute, 1995].
20
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 22

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
strike price K2. This is a net debit trade. The trader’s outlook is bearish: this
strategy proﬁts if the stock price falls. This is a capital gain strategy. We have:
fT = (K1− ST )+− (K2− ST )+− D (29)
S∗ = K1− D (30)
Pmax = K1− K2− D (31)
Lmax = D (32)
2.10 Strategy: Long synthetic forward
This strategy amounts to buying an ATM call option and selling an ATM put option
with a strike price K = S0. This can be a net debit or net credit trade. Typically,
|H|≪ S0. The trader’s outlook is bullish: this strategy mimics a long stock or
futures position; it replicates a long forward contract with the delivery price K and
the same maturity as the options. This is a capital gain strategy. We have: 16
fT = (ST− K)+− (K− ST )+− H = ST− K− H (33)
S∗ = K + H (34)
Pmax = unlimited (35)
Lmax = K + H (36)
2.11 Strategy: Short synthetic forward
This strategy amounts to buying an ATM put option and selling an ATM call option
with a strike price K = S0. This can be a net debit or net credit trade. Typically,
|H|≪ S0. The trader’s outlook is bearish: this strategy mimics a short stock or
futures position; it replicates a short forward contract with the delivery price K and
the same maturity as the options. This is a capital gain strategy. We have:
fT = (K− ST )+− (ST− K)+− H = K− ST− H (37)
S∗ = K− H (38)
Pmax = K− H (39)
Lmax = unlimited (40)
2.12 Strategy: Long combo
This strategy (a.k.a. “long risk reversal”) amounts to buying an OTM call option
with a strike price K1 and selling an OTM put option with a strike price K2. The
16 For some literature on long/short synthetic forward contracts (a.k.a. synthetic futures), see,
e.g., [Benavides, 2009], [Bozic and Fortenbery, 2012], [DeMaskey, 1995], [Ebrahim and Rahman,
2005], [Nandy and Chattopadhyay, 2016].
21
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 23

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
trader’s outlook is bullish. This is a capital gain strategy. 17 We have (K1 > K2):
fT = (ST− K1)+− (K2− ST )+− H (41)
S∗ = K1 + H, H > 0 (42)
S∗ = K2 + H, H < 0 (43)
K2≤ S∗≤ K1, H = 0 (44)
Pmax = unlimited (45)
Lmax = K2 + H (46)
2.13 Strategy: Short combo
This strategy (a.k.a. “short risk reversal”) amounts to buying an OTM put option
with a strike price K1 and selling an OTM call option with a strike price K2. The
trader’s outlook is bearish. This is a capital gain strategy. We have ( K2 > K1):
fT = (K1− ST )+− (ST− K2)+− H (47)
S∗ = K1− H, H > 0 (48)
S∗ = K2− H, H < 0 (49)
K1≤ S∗≤ K2, H = 0 (50)
Pmax = K1− H (51)
Lmax = unlimited (52)
2.14 Strategy: Bull call ladder
This is a vertical spread consisting of a long position in (usually) a close to ATM
call option with a strike price K1, a short position in an OTM call option with
a strike price K2, and a short position in another OTM call option with a higher
strike price K3. A bull call ladder is a bull call spread ﬁnanced by selling another
OTM call option (with the strike price K3).18 This adjusts the trader’s outlook from
bullish (bull call spread) to conservatively bullish or even non-directional (with an
expectation of low volatility). We have:
fT = (ST− K1)+− (ST− K2)+− (ST− K3)+− H (53)
S∗down = K1 + H, H > 0 (54)
S∗up = K3 + K2− K1− H (55)
Pmax = K2− K1− H (56)
Lmax = unlimited (57)
17 For some literature on long/short combo strategies, see, e.g., [Rusn´ akov´ a,ˇSolt´ es and Szabo,
2015], [ˇSolt´ es, 2011], [ˇSolt´ es and Rusn´ akov´ a, 2012]. Also see, e.g., [Chaput and Ederington, 2003].
18 In this sense, this is an “income” strategy.
22
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 24

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.15 Strategy: Bull put ladder
This is a vertical spread consisting of a short position in (usually) a close to ATM
put option with a strike price K1, a long position in an OTM put option with a strike
price K2, and a long position in another OTM put option with a lower strike price
K3. A bull put ladder typically arises when a bull put spread (a bullish strategy)
goes wrong (the stock trades lower), so the trader buys another OTM put option
(with the strike price K3) to adjust the position to bearish. We have: 19
fT = (K3− ST )+ + (K2− ST )+− (K1− ST )+− H (58)
S∗up = K1 + H, H < 0 (59)
S∗down = K3 + K2− K1− H (60)
Pmax = K3 + K2− K1− H (61)
Lmax = K1− K2 + H (62)
2.16 Strategy: Bear call ladder
This is a vertical spread consisting of a short position in (usually) a close to ATM
call option with a strike price K1, a long position in an OTM call option with a strike
price K2, and a long position in another OTM call option with a higher strike price
K3. A bear call ladder typically arises when a bear call spread (a bearish strategy)
goes wrong (the stock trades higher), so the trader buys another OTM call option
(with the strike price K3) to adjust the position to bullish. We have:
fT = (ST− K3)+ + (ST− K2)+− (ST− K1)+− H (63)
S∗down = K1− H, H < 0 (64)
S∗up = K3 + K2− K1 + H (65)
Pmax = unlimited (66)
Lmax = K2− K1 + H (67)
2.17 Strategy: Bear put ladder
This is a vertical spread consisting of a long position in (usually) a close to ATM
put option with a strike price K1, a short position in an OTM put option with
a strike price K2, and a short position in another OTM put option with a lower
strike price K3. A bear put ladder is a bear put spread ﬁnanced by selling another
OTM put option (with the strike price K3).20 This adjusts the trader’s outlook from
bearish (bear put spread) to conservatively bearish or even non-directional (with an
19 For some literature on ladder strategies, see, e.g., [Amaitiek, B´ alint and Reˇ sovsk´ y, 2010],
[Harˇ carikov´ a andˇSolt´ es, 2016], [He, Tang and Zhang, 2016], [ˇSolt´ es and Amaitiek, 2010a].
20 In this sense, as for the bull call ladder, this is an “income” strategy.
23
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 25

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
expectation of low volatility). We have (assuming K3 + K2− K1 + H > max(H, 0)):
fT = (K1− ST )+− (K2− ST )+− (K3− ST )+− H (68)
S∗up = K1− H, H > 0 (69)
S∗down = K3 + K2− K1 + H (70)
Pmax = K1− K2− H (71)
Lmax = K3 + K2− K1 + H (72)
2.18 Strategy: Calendar call spread
This is a horizontal spread consisting of a long position in a close to ATM call option
with TTM T′ and a short position in another call option with the same strike price
K but shorter TTM T < T ′. This is a net debit trade. The trader’s outlook is
neutral to bullish. At the expiration of the short call option ( t = T ), the best case
scenario is if the stock price is right at the strike price ( ST = K). At t = T let V be
the value of the long call option (expiring at t = T′) assuming ST = K. We have:21
Pmax = V− D (73)
Lmax = D (74)
If at the expiration of the short call option the stock price Sstop−loss≤ ST ≤ K,
where Sstop−loss is the stop-loss price below which the trader would unwind the
entire position, then the trader can write another call option with the strike price
K and TTM T1 < T′. While maintaining the long position in the call option with
TTM T′, the trader can generate income by periodically selling call options with
shorter maturities. In this regard, this strategy resembles the covered call strategy.
2.19 Strategy: Calendar put spread
This is a horizontal spread consisting of a long position in a close to ATM put option
with TTM T′ and a short position in another put option with the same strike price
K but shorter TTM T < T ′. This is a net debit trade. The trader’s outlook is
neutral to bearish. At the expiration of the short put option ( t = T ), the best case
scenario is if the stock price is right at the strike price ( ST = K). At t = T let V be
the value of the long put option (expiring at t = T′) assuming ST = K. We have:
Pmax = V− D (75)
Lmax = D (76)
If at the expiration of the short put option the stock price K≤ ST ≤ Sstop−loss,
where Sstop−loss is the stop-loss price above which the trader would unwind the
21 For some literature on calendar/diagonal call/put spreads, see, e.g., [Carmona and Durrleman,
2003], [Carr and Javaheri, 2005], [Dale and Currie, 2015], [Gatheral and Jacquier, 2014], [Kawaller,
Koch and Ludan, 2002], [Liu and Tang, 2010], [Manoliu, 2004], [Pirrong, 2017], [Till, 2008].
24
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 26

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
entire position, then the trader can write another put option with the strike price
K and TTM T1 < T′. While maintaining the long position in the put option with
TTM T′, the trader can generate income by periodically selling put options with
shorter maturities. In this regard, this strategy resembles the covered put strategy.
2.20 Strategy: Diagonal call spread
This is a diagonal spread consisting of a long position in a deep ITM call option with
a strike price K1 and TTM T′, and a short position in an OTM call option with a
strike price K2 and shorter TTM T < T ′. This is a net debit trade. The trader’s
outlook is bullish. At t = T let V be the value of the long call option (expiring at
t = T′) assuming ST = K. We have:
Pmax = V− D (77)
Lmax = D (78)
If at the expiration of the short call option the stock price Sstop−loss≤ ST ≤ K2,
where Sstop−loss is the stop-loss price below which the trader would unwind the entire
position, then the trader can write another OTM call option with TTM T1 < T′.
While maintaining the long position in the call option with TTM T′, the trader can
generate income by periodically selling OTM call options with shorter maturities. In
this regard, this strategy is similar to the calendar call spread. The main diﬀerence
is that, in the diagonal call spread the deep ITM call option (unlike the close to
ATM call option in the calendar call spread) more closely mimics the underlying
stock, so the position is more protected against a sharp rise in the stock price.
2.21 Strategy: Diagonal put spread
This is a diagonal spread consisting of a long position in a deep ITM put option with
a strike price K1 and TTM T′, and a short position in an OTM put option with a
strike price K2 and shorter TTM T < T ′. This is a net debit trade. The trader’s
outlook is bearish. At t = T let V be the value of the long put option (expiring at
t = T′) assuming ST = K. We have:
Pmax = V− D (79)
Lmax = D (80)
If at the expiration of the short put option the stock price K2≤ ST ≤ Sstop−loss,
where Sstop−loss is the stop-loss price above which the trader would unwind the entire
position, then the trader can write another OTM put option with TTM T1 < T′.
While maintaining the long position in the put option with TTM T′, the trader can
generate income by periodically selling OTM put options with shorter maturities. In
this regard, this strategy is similar to the calendar put spread. The main diﬀerence
is that, in the diagonal put spread the deep ITM put option (unlike the close to
25
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 27

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ATM put option in the calendar put spread) more closely mimics the underlying
stock, so the position is more protected against a sharp drop in the stock price.
2.22 Strategy: Long straddle
This is a volatility strategy consisting of a long position in an ATM call option, and
a long position in an ATM put option with a strike price K. This is a net debit
trade. The trader’s outlook is neutral. This is a capital gain strategy. We have 22:
fT = (ST− K)+ + (K− ST )+− D (81)
S∗up = K + D (82)
S∗down = K− D (83)
Pmax = unlimited (84)
Lmax = D (85)
2.23 Strategy: Long strangle
This is a volatility strategy consisting of a long position in an OTM call option with
a strike price K1, and a long position in an OTM put option with a strike price K2.
This is a net debit trade. However, because both call and put options are OTM,
this strategy is less costly to establish than a long straddle position. The ﬂipside
is that the movement in the stock price required to reach one of the break-even
points is also more signiﬁcant. The trader’s outlook is neutral. This is a capital
gain strategy. We have:
fT = (ST− K1)+ + (K2− ST )+− D (86)
S∗up = K1 + D (87)
S∗down = K2− D (88)
Pmax = unlimited (89)
Lmax = D (90)
2.24 Strategy: Long guts
This is a volatility strategy consisting of a long position in an ITM call option with
a strike price K1, and a long position in an ITM put option with a strike price K2.
This is a net debit trade. Since both call and put options are ITM, this strategy
22 For some literature on straddle/strangle strategies, see, e.g., [Copeland and Galai, 1983],
[Coval and Shumway, 2001], [Engle and Rosenberg, 2000], [Gao, Xing and Zhang, 2017], [Goltz
and Lai, 2009], [Guo, 2000], [Hansch, Naik and Viswanathan, 1998], [Noh, Engle and Kane, 1994],
[Rusn´ akov´ a andˇSolt´ es, 2012], [Suresh, 2015]. Academic literature speciﬁcally on long/short guts
strategies (which can be thought of as variations on straddles) appears to be more scarce. For a
book reference, see, e.g., [Cohen, 2005]. For covered straddles, see, e.g., [Johnson, 1979].
26
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 28

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
is more costly to establish than a long straddle position. The trader’s outlook is
neutral. This is a capital gain strategy. We have (assuming D > K 2− K1):23
fT = (ST− K1)+ + (K2− ST )+− D (91)
S∗up = K1 + D (92)
S∗down = K2− D (93)
Pmax = unlimited (94)
Lmax = D− (K2− K1) (95)
2.25 Strategy: Short straddle
This a is sideways strategy consisting of a short position in an ATM call option, and
a short position in an ATM put option with a strike price K. This is a net credit
trade. The trader’s outlook is neutral. This is an income strategy. We have:
fT =−(ST− K)+− (K− ST )+ + C (96)
S∗up = K + C (97)
S∗down = K− C (98)
Pmax = C (99)
Lmax = unlimited (100)
2.26 Strategy: Short strangle
This is a sideways strategy consisting of a short position in an OTM call option with
a strike price K1, and a short position in an OTM put option with a strike price K2.
This is a net credit trade. Since both call and put options are OTM, this strategy
is less risky than a short straddle position. The ﬂipside is that the initial credit is
also lower. The trader’s outlook is neutral. This is an income strategy. We have:
fT =−(ST− K1)+− (K2− ST )+ + C (101)
S∗up = K1 + C (102)
S∗down = K2− C (103)
Pmax = C (104)
Lmax = unlimited (105)
2.27 Strategy: Short guts
This is a sideways strategy consisting of a short position in an ITM call option with
a strike price K1, and a short position in an ITM put option with a strike price
K2. This is a net credit trade. Since both call and put options are ITM, the initial
23 Otherwise this strategy would generate risk-free proﬁts.
27
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 29

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
credit is higher than in a short straddle position. The ﬂipside is that the risk is also
higher. The trader’s outlook is neutral. This is an income strategy. We have: 24
fT =−(ST− K1)+− (K2− ST )+ + C (106)
S∗up = K1 + C (107)
S∗down = K2− C (108)
Pmax = C− (K2− K1) (109)
Lmax = unlimited (110)
2.28 Strategy: Long call synthetic straddle
This volatility strategy (which is the same as a long straddle with the put replaced
by a synthetic put) amounts to shorting stock and buying two ATM (or the nearest
ITM) call options with a strike price K. The trader’s outlook is neutral. This is a
capital gain strategy. 25 We have (assuming S0≥ K and D > S 0− K):
fT = S0− ST + 2× (ST− K)+− D (111)
S∗up = 2× K− S0 + D (112)
S∗down = S0− D (113)
Pmax = unlimited (114)
Lmax = D− (S0− K) (115)
2.29 Strategy: Long put synthetic straddle
This volatility strategy (which is the same as a long straddle with the call replaced
by a synthetic call) amounts to buying stock and buying two ATM (or the nearest
ITM) put options with a strike price K. The trader’s outlook is neutral. This is a
capital gain strategy. We have (assuming S0≤ K and D > K− S0):
fT = ST− S0 + 2× (K− ST )+− D (116)
S∗up = S0 + D (117)
S∗down = 2× K− S0− D (118)
Pmax = unlimited (119)
Lmax = D− (K− S0) (120)
2.30 Strategy: Short call synthetic straddle
This sideways strategy (which is the same as a short straddle with the put replaced
by a synthetic put) amounts to buying stock and selling two ATM (or the nearest
24 Similarly to long guts, here we assume that C >K2−K1.
25 Academic literature on synthetic straddles appears to be scarce. See, e.g., [Trifonov et al ,
2011], [Trifonov et al , 2014].
28
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 30

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
OTM) call options with a strike price K. The trader’s outlook is neutral. This is a
capital gain strategy. We have (assuming S0≤ K):
fT = ST− S0− 2× (ST− K)+ + C (121)
S∗up = 2× K− S0 + C (122)
S∗down = S0− C (123)
Pmax = K− S0 + C (124)
Lmax = unlimited (125)
2.31 Strategy: Short put synthetic straddle
This sideways strategy (which is the same as a short straddle with the call replaced
by a synthetic call) amounts to shorting stock and selling two ATM (or the nearest
OTM) put options with a strike price K. The trader’s outlook is neutral. This is a
capital gain strategy. We have (assuming S0≥ K):
fT = S0− ST− 2× (K− ST )+ + C (126)
S∗up = S0 + C (127)
S∗down = 2× K− S0− C (128)
Pmax = S0− K + C (129)
Lmax = unlimited (130)
2.32 Strategy: Covered short straddle
This strategy amounts to augmenting a covered call by writing a put option with
the same strike price K and TTM as the sold call option and thereby increasing the
income. The trader’s outlook is bullish. We have:
fT = ST− S0− (ST− K)+− (K− ST )+ + C (131)
S∗ = 1
2 (S0 + K− C) (132)
Pmax = K− S0 + C (133)
Lmax = S0 + K− C (134)
2.33 Strategy: Covered short strangle
This strategy amounts to augmenting a covered call by writing an OTM put option
with a strike price K′ and the same TTM as the sold call option (whose strike price
is K) and thereby increasing the income. The trader’s outlook is bullish. We have:
fT = ST− S0− (ST− K)+− (K′− ST )+ + C (135)
Pmax = K− S0 + C (136)
Lmax = S0 + K′− C (137)
29
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 31

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.34 Strategy: Strap
This is a volatility strategy consisting of a long position in two ATM call options,
and a long position in an ATM put option with a strike price K. This is a net debit
trade. The trader’s outlook is bullish. This is a capital gain strategy. We have: 26
fT = 2× (ST− K)+ + (K− ST )+− D (138)
S∗up = K + D
2 (139)
S∗down = K− D (140)
Pmax = unlimited (141)
Lmax = D (142)
2.35 Strategy: Strip
This is a volatility strategy consisting of a long position in an ATM call option, and
a long position in two ATM put options with a strike price K. This is a net debit
trade. The trader’s outlook is bearish. This is a capital gain strategy. We have:
fT = (ST− K)+ + 2× (K− ST )+− D (143)
S∗up = K + D (144)
S∗down = K− D
2 (145)
Pmax = unlimited (146)
Lmax = D (147)
2.36 Strategy: Call ratio backspread
This strategy consists of a short position in NS close to ATM call options with a
strike price K1, and a long position in NL OTM call options with a strike price K2,
where NL > NS. Typically, NL = 2 and NS = 1, or NL = 3 and NS = 2. The
trader’s outlook is strongly bullish. This is a capital gain strategy. We have: 27
fT = NL× (ST− K2)+− NS× (ST− K1)+− H (148)
S∗down = K1− H/NS, H < 0 (149)
S∗up = (NL× K2− NS× K1 + H)/(NL− NS) (150)
Pmax = unlimited (151)
Lmax = NS× (K2− K1) + H (152)
26 For some literature on strip and strap strategies, see, e.g., [Jha and Kalimipal, 2010],
[Topaloglou, Vladimirou and Zenios, 2011].
27 For some literature on call/put ratio (back)spreads, see, e.g., [Augustin, Brenner and Subrah-
manyam, 2015], [Chaput and Ederington, 2008], [ˇSolt´ es, 2010], [ˇSolt´ es and Amaitiek, 2010b], [ˇSolt´ es
and Rusn´ akov´ a, 2013].
30
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 32

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.37 Strategy: Put ratio backspread
This strategy consists of a short position in NS close to ATM put options with a
strike price K1, and a long position in NL OTM put options with a strike price K2,
where NL > NS. Typically, NL = 2 and NS = 1, or NL = 3 and NS = 2. The
trader’s outlook is strongly bearish. This is a capital gain strategy. We have:
fT = NL× (K2− ST )+− NS× (K1− ST )+− H (153)
S∗up = K1 + H/NS, H < 0 (154)
S∗down = (NL× K2− NS× K1− H)/(NL− NS) (155)
Pmax = NL× K2− NS× K1− H (156)
Lmax = NS× (K1− K2) + H (157)
2.38 Strategy: Ratio call spread
This strategy consists of a short position in NS close to ATM call options with a
strike price K1, and a long position in NL ITM call options with a strike price K2,
where NL < NS. Typically, NL = 1 and NS = 2, or NL = 2 and NS = 3. This is
an income strategy if it is structured as a net credit trade. The trader’s outlook is
neutral to bearish. We have: 28
fT = NL× (ST− K2)+− NS× (ST− K1)+− H (158)
S∗down = K2 + H/NL, H > 0 (159)
S∗up = (NS× K1− NL× K2− H)/(NS− NL) (160)
Pmax = NL× (K1− K2)− H (161)
Lmax = unlimited (162)
2.39 Strategy: Ratio put spread
This strategy consists of a short position in NS close to ATM put options with a
strike price K1, and a long position in NL ITM put options with a strike price K2,
where NL < NS. Typically, NL = 1 and NS = 2, or NL = 2 and NS = 3. This is
an income strategy if it is structured as a net credit trade. The trader’s outlook is
neutral to bullish. We have:
fT = NL× (K2− ST )+− NS× (K1− ST )+− H (163)
S∗up = K2− H/NL, H > 0 (164)
S∗down = (NS× K1− NL× K2 + H)/(NS− NL) (165)
Pmax = NL× (K2− K1)− H (166)
Lmax = NS× K1− NL× K2 + H (167)
28 So, the diﬀerence between call/put ratio backspreads and ratio call/put spreads is that in the
former NL >N S, while in the latter NL <N S.
31
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 33

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.40 Strategy: Long call butterﬂy
This is a sideways strategy consisting of a long position in an OTM call option with
a strike price K1, a short position in two ATM call options with a strike price K2,
and a long position in an ITM call option with a strike price K3. The strikes are
equidistant: K2− K3 = K1− K2 = κ. This is a relatively low cost net debit trade.
The trader’s outlook is neutral. This is a capital gain strategy. We have: 29
fT = (ST− K1)+ + (ST− K3)+− 2× (ST− K2)+− D (168)
S∗down = K3 + D (169)
S∗up = K1− D (170)
Pmax = κ− D (171)
Lmax = D (172)
2.40.1 Strategy: Modiﬁed call butterﬂy
This is a variation of the long call butterﬂy strategy where the strikes are no longer
equidistant; instead we have K1− K2 < K2− K3. This results in a sideways strategy
with a bullish bias. We have:
fT = (ST− K1)+ + (ST− K3)+− 2× (ST− K2)+− D (173)
S∗ = K3 + D (174)
Pmax = K2− K3− D (175)
Lmax = D (176)
2.41 Strategy: Long put butterﬂy
This is a sideways strategy consisting of a long position in an OTM put option with
a strike price K1, a short position in two ATM put options with a strike price K2,
and a long position in an ITM put option with a strike price K3. The strikes are
equidistant: K3− K2 = K2− K1 = κ. This is a relatively low cost net debit trade.
The trader’s outlook is neutral. This is a capital gain strategy. We have:
fT = (K1− ST )+ + (K3− ST )+− 2× (K2− ST )+− D (177)
S∗up = K3− D (178)
S∗down = K1 + D (179)
Pmax = κ− D (180)
Lmax = D (181)
29 For some literature on butterﬂy spreads (including iron butterﬂies), see, e.g., [Balb´ as, Lon-
garela and Lucia, 1999], [Howison, Reisinger and Witte, 2013], [Jongadsayakul, 2017], [Matsypura
and Timkovsky, 2010], [Youbi, Pindza and Mar´ e, 2017], [Wolf, 2014], [Wystup, 2017]. Academic
literature on condor strategies (which can be thought of as variations on butterﬂies) appears to be
more scarce. See, e.g., [Niblock, 2017].
32
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 34

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.41.1 Strategy: Modiﬁed put butterﬂy
This is a variation of the long put butterﬂy strategy where the strikes are no longer
equidistant; instead we have K3− K2 < K2− K1. This results in a sideways strategy
with a bullish bias. We have (for H > 0 there is also S∗up = K3− H):30
fT = (K1− ST )+ + (K3− ST )+− 2× (K2− ST )+− H (182)
S∗down = 2× K2− K3 + H (183)
Pmax = K3− K2− H (184)
Lmax = 2× K2− K1− K3 + H (185)
2.42 Strategy: Short call butterﬂy
This is a volatility strategy consisting of a short position in an ITM call option with
a strike price K1, a long position in two ATM call options with a strike price K2,
and a short position in an OTM call option with a strike price K3. The strikes are
equidistant: K3− K2 = K2− K1 = κ. This is a net credit trade. In this sense, this
is an income strategy. However, the potential reward is sizably smaller than with a
short straddle or a short strangle (albeit with a lower risk). The trader’s outlook is
neutral. We have:
fT = 2× (ST− K2)+− (ST− K1)+− (ST− K3)+ + C (186)
S∗up = K3− C (187)
S∗down = K1 + C (188)
Pmax = C (189)
Lmax = κ− C (190)
2.43 Strategy: Short put butterﬂy
This is a volatility strategy consisting of a short position in an ITM put option with
a strike price K1, a long position in two ATM put options with a strike price K2,
and a short position in an OTM put option with a strike price K3. The strikes are
equidistant: K2− K3 = K1− K2 = κ. This is a net credit trade. In this sense, this
is an income strategy. However, the potential reward is sizably smaller than with a
short straddle or a short strangle (albeit with a lower risk). The trader’s outlook is
neutral. We have:
fT = 2× (K2− ST )+− (K1− ST )+− (K3− ST )+ + C (191)
S∗down = K3 + C (192)
S∗up = K1− C (193)
Pmax = C (194)
Lmax = κ− C (195)
30 Ideally, this should be structured as a net credit trade, albeit this may not always be possible.
33
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 35

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.44 Strategy: “Long” iron butterﬂy
This sideways strategy is a combination of a bull put spread and a bear call spread
and consists of a long position in an OTM put option with a strike price K1, a
short position in an ATM put option and an ATM call option with a strike price
K2, and a long position in an OTM call option with a strike price K3. The strikes
are equidistant: K2− K1 = K3− K2 = κ. This is a net credit trade. The trader’s
outlook is neutral. This is an income strategy. We have:
fT = (K1− ST )+− (K2− ST )+− (ST− K2)+ + (ST− K3)+ + C (196)
S∗up = K2 + C (197)
S∗down = K2− C (198)
Pmax = C (199)
Lmax = κ− C (200)
2.45 Strategy: “Short” iron butterﬂy
This volatility strategy is a combination of a bear put spread and a bull call spread
and consists of a short position in an OTM put option with a strike price K1, a
long position in an ATM put option and an ATM call option with a strike price
K2, and a short position in an OTM call option with a strike price K3. The strikes
are equidistant: K2− K1 = K3− K2 = κ. This is a net debit trade. The trader’s
outlook is neutral. This is a capital gain strategy. We have:
fT = (K2− ST )+ + (ST− K2)+− (K1− ST )+− (ST− K3)+− D (201)
S∗up = K2 + D (202)
S∗down = K2− D (203)
Pmax = κ− D (204)
Lmax = D (205)
2.46 Strategy: Long call condor
This is a sideways strategy consisting of a long position in an ITM call option with a
strike price K1, a short position in an ITM call option with a higher strike price K2,
a short position in an OTM call option with a strike price K3, and a long position
in an OTM call option with a higher strike price K4. All strikes are equidistant:
K4− K3 = K3− K2 = K2− K1 = κ. This is a relatively low cost net debit trade.
The trader’s outlook is neutral. This is a capital gain strategy. We have:
fT = (ST− K1)+− (ST− K2)+− (ST− K3)+ + (ST− K4)+− D (206)
S∗up = K4− D (207)
S∗down = K1 + D (208)
34
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 36

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Pmax = κ− D (209)
Lmax = D (210)
2.47 Strategy: Long put condor
This is a sideways strategy consisting of a long position in an OTM put option with a
strike price K1, a short position in an OTM put option with a higher strike price K2,
a short position in an ITM put option with a strike price K3, and a long position
in an ITM put option with a higher strike price K4. All strikes are equidistant:
K4− K3 = K3− K2 = K2− K1 = κ. This is a relatively low cost net debit trade.
The trader’s outlook is neutral. This is a capital gain strategy. We have:
fT = (K1− ST )+− (K2− ST )+− (K3− ST )+ + (K4− ST )+− D (211)
S∗up = K4− D (212)
S∗down = K1 + D (213)
Pmax = κ− D (214)
Lmax = D (215)
2.48 Strategy: Short call condor
This is a volatility strategy consisting of a short position in an ITM call option with
a strike price K1, a long position in an ITM call option with a higher strike price K2,
a long position in an OTM call option with a strike price K3, and a short position
in an OTM call option with a higher strike price K4. All strikes are equidistant:
K4− K3 = K3− K2 = K2− K1 = κ. This is a relatively low net credit trade.
As with a short call butterﬂy, the potential reward is sizably smaller than with a
short straddle or a short strangle (albeit with a lower risk). So, this is a capital gain
(rather than an income) strategy. The trader’s outlook is neutral. We have:
fT = (ST− K2)+ + (ST− K3)+− (ST− K1)+− (ST− K4)+ + C (216)
S∗up = K4− C (217)
S∗down = K1 + C (218)
Pmax = C (219)
Lmax = κ− C (220)
2.49 Strategy: Short put condor
This is a volatility strategy consisting of a short position in an OTM put option with
a strike price K1, a long position in an OTM put option with a higher strike priceK2,
a long position in an ITM put option with a strike price K3, and a short position
in an ITM put option with a higher strike price K4. All strikes are equidistant:
K4− K3 = K3− K2 = K2− K1 = κ. This is a relatively low net credit trade.
35
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 37

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
As with a short put butterﬂy, the potential reward is sizably smaller than with a
short straddle or a short strangle (albeit with a lower risk). So, this is a capital gain
(rather than an income) strategy. The trader’s outlook is neutral. We have:
fT = (K2− ST )+ + (K3− ST )+− (K1− ST )+− (K4− ST )+ + C (221)
S∗up = K4− C (222)
S∗down = K1 + C (223)
Pmax = C (224)
Lmax = κ− C (225)
2.50 Strategy: Long iron condor
This sideways strategy is a combination of a bull put spread and a bear call spread
and consists of a long position in an OTM put option with a strike price K1, a short
position in an OTM put option with a higher strike price K2, a short position in an
OTM call option with a strike price K3, and a long position in an OTM call option
with a higher strike price K4. The strikes are equidistant: K4− K3 = K3− K2 =
K2− K1 = κ. This is a net credit trade. The trader’s outlook is neutral. This is an
income strategy. We have:
fT = (K1− ST )+ + (ST− K4)+− (K2− ST )+− (ST− K3)+ + C (226)
S∗up = K3 + C (227)
S∗down = K2− C (228)
Pmax = C (229)
Lmax = κ− C (230)
2.51 Strategy: Short iron condor
This volatility strategy is a combination of a bear put spread and a bull call spread
and consists of a short position in an OTM put option with a strike price K1, a long
position in an OTM put option with a higher strike price K2, a long position in an
OTM call option with a strike price K3, and a short position in an OTM call option
with a higher strike price K4. The strikes are equidistant: K4− K3 = K3− K2 =
K2− K1 = κ. This is a net debit trade. The trader’s outlook is neutral. This is a
capital gain strategy. We have:
fT = (K2− ST )+ + (ST− K3)+− (K1− ST )+− (ST− K4)+− D (231)
S∗up = K3 + D (232)
S∗down = K2− D (233)
Pmax = κ− D (234)
Lmax = D (235)
36
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 38

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.52 Strategy: Long box
This volatility strategy can be viewed as a combination of a long synthetic forward
and a short synthetic forward, or as a combination of a bull call spread and a bear
put spread, and consists of a long position in an ITM put option with a strike price
K1, a short position in an OTM put option with a lower strike price K2, a long
position in an ITM call option with the strike price K2, and a short position in an
OTM call option with the strike price K1. The trader’s outlook is neutral. This is
a capital gain strategy. 31 We have (assuming K1≥ K2 + D):
fT = ( K1− ST )+− (K2− ST )+ + (ST− K2)+− (ST− K1)+− D
= K1− K2− D (236)
Pmax = ( K1− K2)− D (237)
2.53 Strategy: Collar
This strategy (a.k.a. “fence”) is a covered call augmented by a long put option as
insurance against the stock price falling. 32 It amounts to buying stock, buying an
OTM put option with a strike price K1, and selling an OTM call option with a
higher strike price K2. The trader’s outlook is moderately bullish. This is a capital
gain strategy. We have: 33
fT = ST− S0 + (K1− ST )+− (ST− K2)+− H (238)
S∗ = S0 + H (239)
Pmax = K2− S0− H (240)
Lmax = S0− K1 + H (241)
2.54 Strategy: Bullish short seagull spread
This option trading strategy is a bull call spread ﬁnanced with a sale of an OTM
put option. It amounts to a short position in an OTM put option with a strike
price K1, a long position in an ATM call option with a strike price K2, and a short
position in an OTM call option with a strike price K3. Ideally, the trade should be
structured to have zero cost. The trader’s outlook is bullish. This is a capital gain
31 In some cases it can be used as a tax strategy – see, e.g., [Cohen, 2005]. For some literature
on box option strategies, see, e.g., [BenZion, Anan and Yagil, 2005], [Bharadwaj and Wiggins,
2001], [Billingsley and Chance, 1985], [Clarke, de Silva and Thorley, 2013], [Fung, Mok and Wong,
2004], [Hemler and Miller, 1997], [Jongadsayakul, 2016], [Ronn and Ronn, 1989], [Vipul, 2009].
32 Similarly, a short collar is a covered put augmented by a long call option.
33 For some literature on collar strategies, see, e.g., [Bartonov´ a, 2012], [Burnside et al , 2011],
[D’Antonio, 2008], [Israelov and Klein, 2016], [Li and Yang, 2017], [Oﬃcer, 2004], [Oﬃcer, 2006],
[Shan, Garvin and Kumar, 2010], [Szado and Schneeweis, 2010], [Szado and Schneeweis, 2011],
[Timmermans, Schumacher and Ponds, 2017], [Yim et al , 2011].
37
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 39

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
strategy. We have:34
fT =−(K1− ST )+ + (ST− K2)+− (ST− K3)+− H (242)
S∗ = K2 + H, H > 0 (243)
S∗ = K1 + H, H < 0 (244)
K1≤ S∗≤ K2, H = 0 (245)
Pmax = K3− K2− H (246)
Lmax = K1 + H (247)
2.55 Strategy: Bearish long seagull spread
This option trading strategy is a short combo (short risk reversal) hedged against
the stock price rising by buying an OTM call option. It amounts to a long position
in an OTM put option with a strike price K1, a short position in an ATM call option
with a strike price K2, and a long position in an OTM call option with a strike price
K3. Ideally, the trade should be structured to have zero cost. The trader’s outlook
is bearish. This is a capital gain strategy. We have:
fT = (K1− ST )+− (ST− K2)+ + (ST− K3)+− H (248)
S∗ = K1− H, H > 0 (249)
S∗ = K2− H, H < 0 (250)
K1≤ S∗≤ K2, H = 0 (251)
Pmax = K1− H (252)
Lmax = K3− K2 + H (253)
2.56 Strategy: Bearish short seagull spread
This option trading strategy is a bear put spread ﬁnanced with a sale of an OTM
call option. It amounts to a short position in an OTM put option with a strike
price K1, a long position in an ATM put option with a strike price K2, and a short
position in an OTM call option with a strike price K3. Ideally, the trade should be
structured to have zero cost. The trader’s outlook is bearish. This is a capital gain
strategy. We have:
fT =−(K1− ST )+ + (K2− ST )+− (ST− K3)+− H (254)
S∗ = K2− H, H > 0 (255)
S∗ = K3− H, H < 0 (256)
K2≤ S∗≤ K3, H = 0 (257)
Pmax = K2− K1− H (258)
Lmax = unlimited (259)
34 Academic literature on seagull spreads appears to be scarce. For a book reference, see,
e.g., [Wystup, 2017].
38
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 40

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
2.57 Strategy: Bullish long seagull spread
This option trading strategy is a long combo (long risk reversal) hedged against the
stock price falling by buying an OTM put option. It amounts to a long position in
an OTM put option with a strike price K1, a short position in an ATM put option
with a strike price K2, and a long position in an OTM call option with a strike price
K3. Ideally, the trade should be structured to have zero cost. The trader’s outlook
is bullish. This is a capital gain strategy. We have:
fT = (K1− ST )+− (K2− ST )+ + (ST− K3)+− H (260)
S∗ = K3 + H, H > 0 (261)
S∗ = K2 + H, H < 0 (262)
K2≤ S∗≤ K3, H = 0 (263)
Pmax = unlimited (264)
Lmax = K2− K1 + H (265)
39
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 41

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3 Stocks
3.1 Strategy: Price-momentum
Empirically, there appears to be certain “inertia” in stock returns known as the
momentum eﬀect, whereby future returns are positively correlated with past returns
(see, e.g., [Asness, 1994], [Asness et al , 2014], [Asness, Moskowitz and Pedersen,
2013], [Grinblatt and Moskowitz, 2004], [Jegadeesh and Titman, 1993]). Lett denote
time measured in the units of 1 month, with t = 0 corresponding to the most recent
time. Let Pi(t) be the time series of prices (fully adjusted for splits and dividends)
for the stock labeled by i (i = 1 , . . . , N, where N is the number of stocks in the
trading universe). Let
Ri(t) = Pi(t)
Pi(t + 1)− 1 (266)
Rcum
i = Pi(S)
Pi(S + T )− 1 (267)
Rmean
i = 1
T
S+T−1∑
t=S
Ri(t) (268)
Rrisk.adj
i = Rmean
i
σi
(269)
σ2
i = 1
T− 1
S+T−1∑
t=S
(Ri(t)− Rmean
i )2 (270)
Here: Ri(t) is the monthly return; Rcum
i is the cumulative return computed over the
T -month “formation period” (usually T = 12) skipping the most recent S-month
“skip period” (usually S = 1);35 Rmean
i is the mean monthly return computed over
the formation period; Rrisk.adj
i is the risk-adjusted mean return over the formation
period; and σi is the monthly volatility calculated over the formation period.
The price-momentum strategy amounts to buying the best performing stocks
and selling the worst performing stocks, where the “performance” is measured by a
selection criterion based on Rcum
i , Rmean
i , Rrisk.adj
i or some other criterion. E.g., after
the stocks are sorted by Rcum
i (in the decreasing order), the trader can, e.g., buy
stocks in the top decile (winners) and short stocks in the bottom decile (losers). 36
This can be a zero-cost strategy, i.e., the corresponding portfolio is dollar-neutral.
Alternatively, a long-only portfolio can be constructed by buying stocks in, e.g.,
the top decile. Once a portfolio is established at t = 0, it is kept unaltered during
35 Usually, the most recent month is skipped due to an empirically observed mean-reversion
(a.k.a. contrarian) eﬀect in monthly returns possibly rooted in liquidity/microstructure issues –
see, e.g., [Asness, 1994], [Boudoukh, Richardson and Whitelaw, 1994], [Grinblatt and Moskowitz,
2004], [Jegadeesh, 1990], [Lo and MacKinlay, 1990].
36 There is some degree of arbitrariness in deﬁning winners and losers.
40
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 42

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
a predeﬁned “holding period”, 37 which can be 1 month or longer (longer holding
period portfolios typically have diminishing returns before trading costs as the mo-
mentum eﬀect fades with time). Multi-month-holding portfolios can be constructed
by overlapping 1-month-holding portfolios (see, e.g., [Jegadeesh and Titman, 1993]).
The above prescription does not ﬁx the relative weights wi of the stocks in the
portfolio. For a long-only portfolio we have wi≥ 0 and
N∑
i=1
wi = 1 (271)
So, if the total investment level is I, then the stock labeled by i has I× wi dollars
invested in it. This, up to rounding, translates into Qi = I× wi/Pi(0) shares.38 One
can simply take uniform weights, wi = 1 /N for all stocks, albeit other weighting
schemes are possible. E.g., we can have nonuniform wi∝ 1/σi, or wi∝ 1/σ2
i , etc.
For a dollar-neutral portfolio we can have negative wi and
N∑
i=1
|wi| = 1 (272)
N∑
i=1
wi = 0 (273)
So, if the total investment level is I = IL + IS, where IL is the total long investment,
and IS is the absolute value of the total short investment, 39 then the stock labeled
by i has I× wi dollars invested in it, where wi > 0 for long stocks, and wi < 0
for short stocks. One can simply take modulus-uniform weights, where wi = 1/2NL
for all NL long stocks, and wi =−1/2NS for all NS short stocks. However, other
weighting schemes are possible, e.g., as above, weights suppressed by σi, σ2
i , etc.40
3.2 Strategy: Earnings-momentum
This strategy amounts to buying winners and selling losers as in the price-momentum
strategy, but the selection criterion is based on earnings. One way to deﬁne such a
37 Albeit, e.g., a long-only portfolio may have to be liquidated before the end of this holding
period due to unforeseen events, such as market crashes.
38 That is, assuming the stock is bought at the price Pi(0), which does not account for slippage.
39 For dollar-neutral portfolios IL =IS and I = 2×IL.
40 For some additional literature on momentum strategies, see, e.g., [Antonacci, 2017], [Asem
and Tian, 2010], [Barroso and Santa-Clara, 2014], [Bhojraj and Swaminathan, 2006], [Chordia and
Shivakumar, 2002], [Chuang and Ho, 2014], [Cooper, Gutierrez and Hameed, 2004], [Daniel and
Moskowitz, 2016], [G´ eczy and Samonov, 2016], [Griﬃn, Ji and Martin, 2003], [Grundy and Martin,
2001], [Hwang and George, 2004], [Jegadeesh and Titman, 2001], [Karolyi and Kho, 2004], [Kora-
jczyk and Sadka, 2004], [Liu and Zhang, 2008], [Moskowitz and Grinblatt, 1999], [Rouwenhorst,
1998], [Sadka, 2002], [Siganos and Chelley-Steeley, 2006], [Stivers and Sun, 2010].
41
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 43

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
selection criterion is via standardized unexpected earnings (SUE) [Chan, Jegadeesh
and Lakonishok, 1996]:41
SUEi = Ei− E′
i
σi
(274)
Here: Ei is the most recently announced quarterly earnings per share of the stock
labeled by i; E′
i is the earnings per share announced 4 quarters ago;σi is the standard
deviation of the unexpected earnings Ei−E′
i over the last 8 quarters. Similarly to the
price-momentum strategy, the trader can, e.g., construct a dollar-neutral portfolio
by buying stocks in the top decile by SUE, and shorting stocks in the bottom decile.42
3.3 Strategy: Value
This strategy amounts to buying winners and selling losers as in the price-momentum
and earnings-momentum strategies, but the selection criterion is based on value.
Value can be deﬁned as the Book-to-Price (B/P) ratio (see, e.g., [Rosenberg, Reid
and Lanstein, 1985]). Here “Book” is the company’s book value per share outstand-
ing (so the B/P ratio is the same as the Book-to-Market ratio, where now “Book”
stands for its total book value,not per share outstanding, and “Market” is its market
capitalization). The trader can, e.g., construct a zero-cost portfolio by buying stocks
in the top decile by the B/P ratio, and shorting stocks in the bottom decile. There
can be variations in the deﬁnition of the B/P ratio. Thus, e.g., [Asness, Moskowitz
and Pedersen, 2013] uses current (i.e., most up-to-date) prices, while [Fama and
French, 1992] and some others use prices contemporaneous with the book value. 43
3.4 Strategy: Low-volatility anomaly
This strategy is based on the empirical observation that future returns of previously
low-return-volatility portfolios outperform those of previously high-return-volatility
portfolios,44 which goes counter to the “na¨ ıve” expectation that higher risk assets
41 Also see, e.g., [Bartov, Radhakrishnan and Krinsky, 2005], [Battalio and Mendenhall, 2007],
[Bernard and Thomas, 1989], [Bernard and Thomas, 1990], [Bhushan, 1994], [Chordia et al, 2009],
[Chordia and Shivakumar, 2006], [Czaja, Kaufmann and Scholz, 2013], [Doyle, Lundholm and
Soliman, 2006], [Foster, Olsen and Shevlin, 1984], [Hew et al , 1996], [Hirshleifer, Lim and Teoh,
2009], [Jansen and Nikiforov, 2016], [Livnat and Mendenhall, 2006], [Loh and Warachka, 2012],
[Mendenhall, 2004], [Ng, Rusticus and Verdi, 2008], [Rendleman, Jones and Latan´ e, 1982], [Stickel,
1991], [Watts, 1978].
42 Typically, the holding period is 6 months, with diminishing returns for longer holding periods.
43 The holding period typically is 1-6 months. For some additional literature on value strategies,
see, e.g., [Erb and Harvey, 2006], [Fama and French, 1993], [Fama and French, 1996], [Fama and
French, 1998], [Fama and French, 2012], [Fisher, Shah and Titman, 2016], [Gerakos and Linnain-
maa, 2012], [Novy-Marx, 2013], [Piotroski, 2000], [Piotroski and So, 2012], [Stattman, 1980], [Suho-
nen, Lennkh and Perez, 2017], [Zhang, 2005].
44 See, e.g., [Ang et al , 2006], [Ang et al , 2009], [Baker, Bradley and Wurgler, 2011], [Black,
1972], [Blitz and van Vliet, 2007], [Clarke, de Silva and Thorley, 2006], [Clarke, de Silva and
42
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 44

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
should yield proportionately higher returns. Thus, if σi is deﬁned as the histori-
cal volatility (computed over a time series of historical returns, as in Eq. (270)),
the trader can, e.g., construct a dollar-neutral portfolio by buying stocks in the
bottom decile by σi (low-volatility stocks), and shorting stocks in the top decile
(high-volatility stocks). The length of the sample used for computing the historical
volatility can, e.g., be 6 months (126 trading days) to a year (252 trading days),
with a similar duration for the holding period (with no “skip period” required).
3.5 Strategy: Implied volatility
This strategy is based on the empirical observation that stocks with larger increases
in call implied volatilities over the previous month on average have higher future re-
turns, while stocks with larger increases in put implied volatilities over the previous
month on average have lower future returns (see, e.g., [Anet al, 2014], [Chen, Chung
and Tsai, 2016]).45 Therefore, the trader can, e.g., construct a dollar-neutral portfo-
lio by buying stocks in the top decile by the increase in call implied volatilities, and
shorting stocks in the top decile by the increase in put implied volatilities. One can
also consider variations, e.g., buying stocks in the top decile by the diﬀerence twixt
the change in call implied volatilities and the change in put implied volatilities.
3.6 Strategy: Multifactor portfolio
This strategy amounts to buying and shorting stocks based on multiple factors such
as value, momentum, etc. For instance, usually value and momentum are negatively
correlated and combining them can add value (see, e.g., [Asness, Moskowitz and
Pedersen, 2013]). There is a variety of ways in which F > 1 factors can be com-
bined.46 The simplest way is to diversify the exposure to the F factors with some
weights wA, where A = 1, . . . , F labels the factors. That is, if I is the total invest-
ment level, then the F portfolios (each built as above based on the corresponding
factor) are allocated the investment levels IA = wA×I, where (assuming all wA > 0)
F∑
A=1
wA = 1 (275)
Thus, one can simply take uniform weights wA = 1/F , albeit this may not be the
most optimal weighting scheme. E.g., similarly to Subsection 3.1, there are weighting
Thorley, 2010], [Frazzini and Pedersen, 2014], [Fu, 2009], [Garcia-Feij´ ooet al , 2015], [Li, Sullivan
and Garcia-Feij´ oo, 2014], [Li, Sullivan and Garcia-Feij´ oo, 2016], [Merton, 1987].
45 Also see, e.g., [Bali and Hovakimian, 2009], [Bollen and Whaley, 2004], [Busch, Christensen
and Nielsen, 2011], [Chakravarty, Gulen and Mayhew, 2004], [Conrad, Dittmar and Ghysels, 2013],
[Cremers and Weinbaum, 2010], [Pan and Poteshman, 2006], [Xing, Zhang and Zhao, 2010].
46 And the holding period depends on which factors are combined.
43
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 45

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
schemes with wA∝ 1/σA, wA∝ 1/σ2
A, etc., where σA is the historical volatility for
the corresponding factor portfolio (uniformly normalized, e.g., per dollar invested).47
Alternatively, consider F rankings of stocks based on the F factors. One can
now combine these rankings in various ways to blend the factors. E.g., in the case
of two factors, momentum and value, one can take the top (winners) and bottom
(losers) quintiles by momentum and further split them into top half and bottom
half, respectively, by value. Or one can take the top and bottom quintiles by value
and split them by momentum. 48 Yet another way is to deﬁne demeaned ranks
sAi = rank(fAi)− 1
N
N∑
j=1
rank(fAj) (276)
where fAi is the numeric value of the factor labeled by A (e.g., momentum) for the
stock labeled by i (i = 1, . . . , N). One can then simply average the ranks:
si = 1
F
F∑
A=1
sAi (277)
The combined “score” si can have ties, which, if need be (e.g., if there is an ambiguity
at the border of the top decile) can be resolved, e.g., simply by giving preference to
one of the factor rankings. Averaging over sAi simply minimizes the sum of squares
of the Euclidean distances between the N-vector si and the K N -vectors sAi. One
can introduce nonuniform weights into this sum (which would amount to a weighted
average in Eq. (277)), or even use a diﬀerent deﬁnition of the distance (e.g., the
Manhattan distance), which would complicate the problem computationally. Etc. 49
3.7 Strategy: Residual momentum
This is the same as the price-momentum strategy with the stock returns Ri(t) re-
placed by the residuals ϵi(t) of a serial regression of the stock returns Ri(t) over,
e.g., the 3 Fama-French factors MKT(t), SMB(t), HML(t),50 with the intercept (see,
47 Another approach is to ﬁx the weightswA by optimizing a portfolio of theF expected returns
corresponding to the F factors (using an invertible F×F covariance matrix for these returns).
48 These two ways generally do not produce the same resultant portfolios.
49 For additional literature on multifactor strategies, see, e.g., [Amenc et al , 2016], [Amenc et
al, 2015], [Arnott et al , 2013], [Asness, 1997], [Barber, Bennett and Gvozdeva, 2015], [Cochrane,
1999], [Fama, 1996], [Grinold and Kahn, 2000], [Hsu, Lin and Vincent, 2018], [Kahn and Lemmon,
2015], [Kahn and Lemmon, 2016], [Kozlov and Petajisto, 2013], [Malkiel, 2014], [Wang, 2005].
50 The stock returns Ri are deﬁned in excess of the risk-free rate (the one-month Treasury bill
rate); MKT is the excess return of the market portfolio; SMB is the excess return of the Small
minus Big (by market capitalization) portfolio; HML is the excess return of the High minus Low
(by book-to-market) portfolio. See, e.g., [Carhart, 1997], [Fama and French, 1993] for details.
44
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 46

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
e.g., [Blitz, Huij and Martens, 2011]): 51
Ri(t) = αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + ϵi(t) (278)
The regression is run over a 36-month period [Blitz, Huij and Martens, 2011] (with
the 1-month skip period) to estimate the regression coeﬃcients αi, β1,i, β2,i, β3,i.
Once the coeﬃcients are estimated, the residuals can be computed for the 12-month
formation period (again, with the 1-month skip period):
ϵi(t) = Ri(t)− β1,i MKT(t)− β2,i SMB(t)− β3,i HML(t) (279)
Note that αi is not included in this computation of the residuals for the 12-month
formation period as αi was computed for the 36-month period. These residuals
ϵi(t) are then used to compute, e.g., the risk-adjusted residual returns ˜Rrisk.adj
i (here
S = 1 and T = 12; the holding period typically is 1 month, but can be longer):
ϵmean
i = 1
T
S+T−1∑
t=S
ϵi(t) (280)
˜Rrisk.adj
i = ϵmean
i
˜σi
(281)
˜σ2
i = 1
T− 1
S+T−1∑
t=S
(ϵi(t)− ϵmean
i )2 (282)
E.g., a dollar-neutral portfolio can be constructed by buying stocks in the top decile
by ˜Rrisk.adj
i , and shorting stocks in the bottom decile (with (non)uniform weights).
3.8 Strategy: Pairs trading
This dollar-neutral strategy amounts to identifying a pair of historically highly corre-
lated stocks (call them stock A and stock B) and, when a mispricing (i.e., a deviation
from the high historical correlation) occurs, shorting the “rich” stock and buying
the “cheap” stock. This is an example of a mean-reversion strategy. Let PA(t1) and
PB(t1) be the prices of stock A and stock B at time t1, and let PA(t2) and PB(t2)
be the prices of stock A and stock B at a later time t2. All prices are fully adjusted
for any splits and dividends. The corresponding returns (from t1 to t2) are
RA = PA(t2)
PA(t1)− 1 (283)
RB = PB(t2)
PB(t1)− 1 (284)
51 For some additional literature related to the residual momentum strategy, see, e.g., [Blitzet al,
2013], [Chang et al , 2016], [Chaves, 2012], [Chuang, 2015], [Grundy and Martin, 2001], [Gutierrez
and Prinsky, 2007], [H¨ uhn and Scholz, 2017], [Huij and Lansdorp, 2017], [Van Oord, 2016].
45
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 47

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Since typically these returns are small, we can use an alternative deﬁnition:
RA = ln
( PA(t2)
PA(t1)
)
(285)
RB = ln
( PB(t2)
PB(t1)
)
(286)
Next, let ˜RA and ˜RB be the demeaned returns:
R = 1
2 (RA + RB) (287)
˜RA = RA− R (288)
˜RB = RB− R (289)
where R is the mean return. A stock is “rich” if its demeaned return is positive,
and it is “cheap” if its demeaned return is negative. The numbers of shares QA, QB
to short/buy are ﬁxed by the total desired dollar investment I (Eq. (290)) and the
requirement of dollar-neutrality (Eq. (291)):
PA |QA| + PB |QB| = I (290)
PA QA + PB QB = 0 (291)
where PA, PB are the stock prices at the timet∗ the position is established (t∗≥ t2).52
3.9 Strategy: Mean-reversion – single cluster
This is a generalization of the pairs trading strategy to N > 2 stocks that are
historically highly correlated (e.g., stocks belonging to the same industry or sector).
Let Ri, i = 1, . . . , N, be the returns for these N stocks:
Ri = ln
( Pi(t2)
Pi(t1)
)
(292)
R = 1
N
N∑
i=1
Ri (293)
˜Ri = Ri− R (294)
52 For some literature on pairs trading, see, e.g., [Bogomolov, 2013], [Bowen and Hutchinson,
2016], [Bowen, Hutchinson and O’Sullivan, 2010], [Caldeira and Moura, 2013], [Chen et al , 2017],
[Do and Faﬀ, 2010], [Do and Faﬀ, 2012], [Elliott, Van Der Hoek and Malcolm, 2005], [Engle and
Granger, 1987], [Gatev, Goetzmann and Rouwenhorst, 2006], [Huck, 2009], [Huck, 2015], [Huck
and Afawubo, 2014], [Jacobs and Weber, 2015], [Kakushadze, 2015b], [Kim, 2011], [Kishore, 2012],
[Krauss, 2017], [Krauss and St¨ ubinger, 2017], [Liew and Wu, 2013], [Lin, McCrae and Gulati,
2006], [Liu, Chang and Geman, 2017], [Miao, 2014], [Perlin, 2009], [Pizzutilo, 2013], [Rad, Low
and Faﬀ, 2016], [St¨ ubinger and Bredthauer, 2017], [St¨ ubinger and Endres, 2017], [Vaitonis and
Masteika, 2016], [Vidyamurthy, 2004], [Xie et al , 2014], [Yoshikawa, 2017], [Zeng and Lee, 2014].
46
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 48

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Following the pairs trading intuition, we can short stocks with positive ˜Ri and buy
stocks with negative ˜Ri. We have the following conditions:
N∑
i=1
Pi |Qi| = I (295)
N∑
i=1
Pi Qi = 0 (296)
Here: I is the total desired dollar investment; Eq. (296) is the dollar-neutrality
constraint; Qi < 0 for short-sales; Qi > 0 for buys; Pi are the prices at the time
the position is established. We have 2 equations and N > 2 unknowns. A simple
prescription (which is one out of myriad possibilities) for specifying Qi is to have
the dollar positions Di = Pi Qi proportional to the demeaned returns:
Di =−γ ˜Ri (297)
where γ > 0 (recall that we short ˜Ri > 0 stocks and buy ˜Ri < 0 stocks). Then Eq.
(296) is automatically satisﬁed, while Eq. (295) ﬁxes γ:
γ = I
∑N
i=1
⏐⏐⏐˜Ri
⏐⏐⏐
(298)
3.9.1 Strategy: Mean-reversion – multiple clusters
The mean-reversion strategy of Subsection 3.9 can be readily generalized to the case
where we have K > 1 clusters such that stocks within each cluster are historically
highly correlated.53 We can simply treat clusters independently from each other and
construct a mean-reversion strategy following the above procedure in each cluster.
Then, e.g., we can allocate investments to these K independent strategies uniformly.
There is a neat way of treating all clusters in a “uniﬁed” fashion using a linear
regression. Let the K clusters be labeled by A = 1, . . . , K. Let Λ iA be an N× K
matrix such that if the stock labeled by i (i = 1 , . . . , N) belongs to the cluster
labeled by A, then Λ iA = 1; otherwise, Λ iA = 0. We will assume that each and
every stock belongs to one and only one cluster (so there are no empty clusters):
NA =
N∑
i=1
ΛiA > 0 (299)
N =
K∑
A=1
NA (300)
53 E.g., these clusters can correspond to sectors, such as energy, technology, healthcare, etc.
47
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 49

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
We have
ΛiA = δG(i),A (301)
G :{1, . . . , N}↦→{ 1, . . . , K} (302)
Here: G is the map between stocks and clusters; and Λ iA is the loadings matrix.
Now consider a linear regression of the stock returns Ri over ΛiA (without the
intercept and with unit weights):
Ri =
K∑
A=1
ΛiA fA + εi (303)
where fA are the regression coeﬃcients given by (in matrix notation, where R is the
N-vector Ri, f is the K-vector fA, and Λ is the N× K matrix ΛiA)
f = Q−1 ΛT R (304)
Q = ΛT Λ (305)
and εi are the regression residuals. For binary ΛiA given by Eq. (301), these residuals
are nothing but the returns Ri demeaned w.r.t. to the corresponding cluster:
ε = R− Λ Q−1 ΛT R (306)
QAB = NA δAB (307)
RA = 1
NA
∑
j∈JA
Rj (308)
εi = Ri− RG(i) = ˜Ri (309)
where RA is the mean return for the cluster labeled by A, and ˜Ri is the demeaned
return obtained by subtracting from Ri the mean return for the cluster labeled by
A = G(i) to which the stock labeled by i belongs: JA ={i|G(i) = A}⊂{ 1, . . . , N}.
The demeaned returns are cluster-neutral, i.e.,
N∑
i=1
˜Ri ΛiA = 0, A = 1, . . . , K (310)
Also, note that we automatically have (so Di given by Eq. (297) satisfy Eq. (296))
N∑
i=1
˜Ri νi = 0 (311)
where νi≡ 1, i = 1, . . . , N, i.e., the N-vector ν is the unit vector. In the regression
language, ν is the intercept. We did not have to add the intercept to the loadings
matrix Λ as it is already subsumed in it:
K∑
A=1
ΛiA = νi (312)
48
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 50

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3.10 Mean-reversion – weighted regression
The conditions (310) satisﬁed by the demeaned returns when the loadings matrix is
binary simply mean that these returns are cluster-neutral, i.e., orthogonal to the K
N-vectors v(A) comprising the columns of Λ iA. Such orthogonality can be deﬁned
for any loadings matrix, not just a binary one. So, we can consider a generalization
where the loadings matrix, call it ΩiA, may have some binary columns, but generally
it need not. The binary columns, if any, can, e.g., be industry (or sector) based risk
factors; the non-binary columns are interpreted as some non-industry based risk
factors; and the orthogonality condition
N∑
i=1
˜Ri ΩiA, A = 1, . . . , K (313)
can be satisﬁed if the twiddled returns ˜Ri are related to the residuals εi of the
regression of Ri over ΩiA with some (generally nonuniform) regression weights zi via
˜R = Z ε (314)
ε = R− Ω Q−1 ΩT Z R (315)
Z = diag(zi) (316)
Q = ΩT Z Ω (317)
If the intercept is included in Ω iA (i.e., a linear combination of the columns of Ω iA
equals the unit N-vector ν), then we automatically have
N∑
i=1
˜Ri = 0 (318)
The weights zi can, e.g., be taken as zi = 1/σ2
i , where σi are historical volatilities.54
3.11 Strategy: Single moving average
This strategy is based on the stock price crossing a moving average. One can use
diﬀerent types of moving averages (MAs), such as a simple moving average (SMA),
54 For some literature on mean-reversion (a.k.a. contrarian) strategies, see, e.g., [Avellaneda
and Lee, 2010], [Black and Litterman, 1991], [Black and Litterman, 1992], [Cheung, 2010], [Chin,
Prevost and Gottesman, 2002], [Conrad and Kaul, 1998], [Daniel, 2001], [Da Silva, Lee and Porn-
rojnangkool, 2009], [Doan, Alexeev and Brooks, 2014], [Drobetz, 2001], [Hodges and Carverhill,
1993], [Idzorek, 2007], [Jansen and Nikiforov, 2016], [Jegadeesh and Titman, 1995], [Kakushadze,
2015b], [Kang, Liu and Ni, 2002], [Kudryavtsev, 2012], [Lakonishok, Shleifer and Vishny, 1994],
[Lehmann, 1990], [Li et al, 2012], [Liew and Roberts, 2013], [Lo and MacKinlay, 1990], [Mun, Vas-
concellos and Kish, 2000], [O’Tool, 2013], [Pole, 2007], [Poterba and Summers, 1988], [Satchell and
Scowcroft, 2000], [Schiereck, Bondt and Weber, 1999], [Shi, Jiang and Zhou, 2015], [Yao, 2012].
49
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 51

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
or an exponential moving average (EMA): 55
SMA(T ) = 1
T
T∑
t=1
P (t) (319)
EMA(T, λ) =
∑T
t=1 λt−1 P (t)∑T
t=1 λt−1
= 1− λ
1− λT
T∑
t=1
λt−1 P (t) (320)
Here: t = 1 corresponds to the most recent time in the time series of historical stock
prices P (t); T is the length of the MA ( t and T are usually measured in trading
days); and λ < 1 is the factor which suppresses past contributions. Below MA will
refer to SMA or EMA. A simple strategy is deﬁned as follows ( P is the price at
t = 0, on the trading day immediately following the most recent trading day t = 1
in the time series P (t)):
Signal =
{
Establish long/liquidate short position if P > MA(T )
Establish short/liquidate long position if P < MA(T ) (321)
This strategy can be run as, e.g., long-only, short-only, or both long and short. It
can be straightforwardly applied to multiple stocks (on a single-stock basis, with no
cross-sectional interaction between the signals for individual stocks). With a large
number of stocks, it may be possible to construct (near-)dollar-neutral portfolios.
3.12 Strategy: Two moving averages
The simplest variant of this strategy replaces the stock price P in Eq. (321) by
another moving average. That is, we have 2 moving averages with lengths T′ and
T , where T′ < T (e.g., T′ = 10 and T = 30), and the signal is given by:
Signal =
{
Establish long/liquidate short position if MA( T′) > MA(T )
Establish short/liquidate long position if MA( T′) < MA(T ) (322)
This signal can be augmented with additional “stop-loss” rules to protect realized
proﬁts. E.g., if a long position has been established, the trader can deﬁne a threshold
55 For T ≫ 1 we have λT ≪ 1 and EMA( T,λ )≈ (1−λ) P (1) +λ EMA(T− 1,λ ), where
EMA(T−1,λ ) is based onP (2),P (3),...,P (T ). Also, for some literature on moving average based
strategies, see, e.g., [BenZion et al, 2003], [Brock, Lakonishock and LeBaron, 1992], [Dzikeviˇ cius and
ˇSaranda, 2010], [Edwards and Magee, 1992], [Faber, 2007], [F´ elix and Rodr´ ıguez, 2008], [Fiﬁeld,
Power and Knipe, 2008], [Fong and Yong, 2005], [Gen¸ cay, 1996], [Gen¸ cay, 1998], [Gen¸ cay and
Stengos, 1998], [Glabadanidis, 2015], [Gunasekarage and Power, 2001], [Hung, 2016], [James, 1968],
[Jasemi and Kimiagari, 2012], [Kilgallen, 2012], [Li et al , 2015], [Lo, Mamaysky and Wang, 2000],
[Metghalchi, Marcucci and Chang, 2012], [P¨ at¨ ari and Vilska, 2014], [Taylor and Allen, 1992],
[Weller, Friesen and Dunham, 2009], [Zakamulin, 2014a], [Zakamulin, 2015].
50
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 52

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
to liquidate the long position if the stock begins to fall (even if the shorter moving
average has not crossed the longer moving average yet):
Signal =



Establish long position if MA( T′) > MA(T )
Liquidate long position if P < (1− ∆)× P1
Establish short position if MA( T′) < MA(T )
Liquidate short position if P > (1 + ∆)× P1
(323)
Here ∆ is some predeﬁned percentage, e.g., ∆ = 2%. So, a long position is liquidated
if the current price P falls over 2% below the previous day’s price P1; and a short
position is liquidated if P rises over 2% above P1. Other variations can be used.
3.13 Strategy: Three moving averages
In some cases, using 3 moving averages with lengths T1 < T 2 < T 3 (e.g., T1 = 3,
T2 = 10, T3 = 21) can help ﬁlter false signals:
Signal =



Establish long position if MA( T1) > MA(T2) > MA(T3)
Liquidate long position if MA( T1)≤ MA(T2)
Establish short position if MA( T1) < MA(T2) < MA(T3)
Liquidate short position if MA( T1)≥ MA(T2)
(324)
3.14 Strategy: Support and resistance
This strategy uses “support” S and “resistance” R levels, which can be computed
using the “pivot point” (a.k.a. the “center”) C as follows:56
C = PH + PL + PC
3 (325)
R = 2× C− PL (326)
S = 2× C− PH (327)
Here PH, PL and PC are the previous day’s high, low and closing prices. One way
to deﬁne a trading signal is as follows (as above, P is the current price):
Signal =



Establish long position if P > C
Liquidate long position if P≥ R
Establish short position if P < C
Liquidate short position if P≤ S
(328)
56 Other deﬁnitions of the pivot point (e.g., using the current trading day’s open price) and
higher/lower support/resistance levels exist. For some literature on support and resistance strate-
gies, see, e.g., [Amiri et al, 2010], [Brock, Lakonishock and LeBaron, 1992], [Garzarelli et al, 2014],
[Hardy, 1978], [Kahneman and Tversky, 1979], [Murphy, 1986], [Osler, 2000], [Osler, 2003], [Person,
2007], [Pring, 1985], [Shiu and Lu, 2011], [Thomsett, 2003], [Zapranis and Tsinaslanidis, 2012].
51
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 53

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3.15 Strategy: Channel
This strategy amounts to buying and selling a stock when it reaches the ﬂoor and
the ceiling of a channel, respectively. A channel is a range/band, bounded by a
ceiling and a ﬂoor, within which the stock price ﬂuctuates. The trader’s expectation
may be that if the ﬂoor or the ceiling is reached, the stock price will bounce in the
opposite direction. On the other hand, if the stock price breaks through the ceiling
or the ﬂoor, the trader may conclude that a new trend has emerged and follow this
new trend instead. A simple and common deﬁnition of a channel is the Donchian
Channel [Donchian, 1960], where the ceiling Bup and the ﬂoor Bdown are deﬁned as
follows (with the same notations as above): 57
Bup = max(P (1), P(2), . . . , P(T )) (329)
Bdown = min(P (1), P(2), . . . , P(T )) (330)
A simple trading strategy then is as follows:
Signal =
{
Establish long/liquidate short position if P = Bdown
Establish short/liquidate long position if P = Bup
(331)
The wider the channel, the higher the volatility. Usually, the channel indicator is
used together with other indicators. E.g., the signal can be more robust when a
price reversal (or a channel break) occurs with an increase in the traded volume.
3.16 Strategy: Event-driven – M&A
This strategy, referred to as “merger arbitrage” or “risk arbitrage”, attempts to cap-
ture excess returns generated via corporate actions such as mergers and acquisitions
(M&A). A merger arbitrage opportunity arises when one publicly traded company
intends to acquire another publicly traded company at a price that diﬀers from the
latter’s market price. In this regard, there are two main types of transactions: cash
mergers and stock mergers. In the case of a cash merger, the trader establishes a
long position in the target company stock. In the case of a stock merger, the trader
establishes a long position in the target company stock (call it A) and a short posi-
tion in the acquirer company stock (call it B). For instance, if the current price of A
is $67, the current price of B is $35, and under the proposed stock merger deal each
share of A is swapped for 2 shares of B, then the trader buys one share of A and
shorts 2 shares of B generating an initial net credit of $3 = 2 × $35− $67, which is
the proﬁt per each share of A bought if the deal goes through. The trader’s risk is
in that, if the deal falls through, the trader will likely lose money on this trade. 58
57 For some additional literature on channel trading strategies, see, e.g., [Batten and Ellis, 1996],
[Birari and Rode, 2014], [Dempster and Jones, 2002], [De Zwartet al, 2009], [Elder, 2014], [Sullivan,
Timmermann and White, 1999].
58 For some literature on merger arbitrage, see, e.g., [Andrade, Mitchell and Staﬀord, 2001],
[Andrie¸ s and Vˆ ırlan, 2017], [Baker, Pan and Wurgler, 2012], [Baker and Sava¸ soglu, 2002], [Bester,
52
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 54

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3.17 Strategy: Machine learning – single-stock KNN
Some strategies rely on machine learning techniques, such as the k-nearest neighbor
(KNN) algorithm (see, e.g., [Altman, 1992], [Samworth, 2012]), to predict future
stock returns (the target variable) based on a set of predictor (feature) variables,
which can be based on technical, fundamental and/or some other data. The strategy
we describe here is a single-stock strategy, i.e., for each stock the target variable is
predicted using the price and volume data only for this stock (but no cross-sectional
data, i.e., no data for other stocks). The target variable Y (t) is deﬁned as the
cumulative return over the next T trading days (as above, the ascending integer
values of t, which is measured in trading days, correspond to going back in time):
Y (t) = P (t− T )
P (t) − 1 (332)
The predictor variables Xa(t), a = 1 , . . . , m, are deﬁned using prices P (t′) and
volumes V (t′) at times t′ before t (i.e., t′ > t), so they are out-of-sample. Examples
of such variables are moving averages of the price and volume of varying lengths:
X1(t) = 1
T1
T1∑
s=1
V (t + s) (333)
X2(t) = 1
T2
T2∑
s=1
P (t + s) (334)
X3(t) = 1
T3
T3∑
s=1
P (t + s) (335)
. . . (336)
The predictor variables are further normalized to lie between 0 and 1:
˜Xa(t) = Xa(t)− X−
a
X+
a − X−
a
(337)
where X+
a and X−
a are the maximum and minimum values of Xa(t) over the training
period. The ﬁnal ingredient is the number k of the nearest neighbors (see below).
For a given value of t we can take k nearest neighbors of the m-vector ˜Xa(t) among
the m-vectors ˜Xa(t′), t′ = t + 1, t + 2, . . . , t+ T∗, using the KNN algorithm (here
Martinez and Rosu, 2017], [Brown and Raymond, 1986], [Cao et al , 2016], [Cornelli and Li, 2002],
[Dukes, Frolich and Ma, 1992], [Hall, Pinnuck and Thorne, 2013], [Harford, 2005], [Hsieh and
Walkling, 2005], [Huston, 2000], [Jetley and Ji, 2010], [Karolyi and Shannon, 1999], [Khan, 2002],
[Larker and Lys, 1987], [Lin, Lan and Chuang, 2013], [Maheswaran and Yeoh, 2005], [Mitchell and
Pulvino, 2001], [Oﬃcer, 2004], [Oﬃcer, 2006], [Samuelson and Rosenthal, 1986], [Subramanian,
2004], [Van Tassel, 2016], [Walkling, 1985].
53
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 55

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
T∗ is the sample size). For KNN we can use the Euclidean distance D(t, t′) between
˜Xa(t) and ˜Xa(t′) deﬁned as
[D(t, t′)]2 =
m∑
a=1
(˜Xa(t)− ˜Xa(t′))2 (338)
However, we can use some other distance (e.g., the Manhattan distance). Let the k
nearest neighbors of ˜Xa(t) be ˜Xa(t′
α(t)), α = 1, . . . , k. (Note that the k values t′
α(t)
depend on t.) Then we can deﬁne the predicted valueY(t) simply as an average of
the corresponding realized values Y (t′
α(t)):
Y(t) = 1
k
k∑
α=1
Y (t′
α(t)) (339)
Alternatively, we can, e.g., consider a linear model
Y(t) =
k∑
α=1
Y (t′
α(t)) wα + v (340)
and ﬁx the coeﬃcients wα and v by running a regression 59 of the realized values
Y (t) over Y (t′
α(t)) for some number – call it M – of values of t. I.e., we pull Y (t)
for these values of t into an M-vector and regress it over the M× k matrix of the
corresponding values Y (t′
α(t)). The coeﬃcients of this regression are wα and v.
The advantage of using Eq. (339) is simplicity – there are no parameters to train
in this case. We still have to backtest the strategy (see below) out-of-sample. The
disadvantage is that equally weighting contributions of all k nearest neighbors could
be suboptimal. In this regard, there are various (e.g., distance-based) weighting
schemes one may consider. Nontrivial weighting is precisely what Eq. (340) intends
to capture. However, this requires training and cross-validation (using metrics such
as root mean square error), and the ﬁtted parameters wα and v can be (and often
are) out-of-sample unstable. The data can be split, e.g., 60% for training and 40%
for cross-validation. Ultimately, the strategy must backtest well out-of-sample.
The signal at t = 0 can be deﬁned using the predicted value Y =Y(0), which is
the expected return for the next T days. For single-stock trading 60 one can simply
deﬁne thresholds for establishing long and short trades, and liquidating existing
59 We can run this regression without the intercept, in which case we only have the coeﬃcients
wα, or with the intercept, in which case we also have the coeﬃcient v.
60 Alternatively, one can use expected returns Yi computed for N stocks (where N≫ 1) using
a machine learning algorithm as above and then use these expected returns in multi-stock cross-
sectional strategies such as mean-reversion/statistical arbitrage.
54
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 56

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
positions, e.g., as follows: 61
Signal =



Establish long position if Y > z1
Liquidate long position if Y≤ z2
Establish short position if Y <−z1
Liquidate short position if Y≥− z2
(341)
Here, z1 and z2 are trader-deﬁned thresholds. This signal must be backtested out-
of-sample. The number k of nearest neighbors can be optimized using a backtest
(by trying a set of values of k). Alternatively, one can use a common heuristic, e.g.,
k = ﬂoor(√T∗) or k = ceiling(√T∗). Also see, e.g., [Hall, Park and Samworth, 2008].
3.18 Strategy: Statistical arbitrage – optimization
Let Cij be the sample or model covariance matrix for the N stock returns in a
portfolio.62 Let Di be the dollar holdings in our portfolio. The expected portfolio
P&L P , volatility V and Sharpe ratio S are given by
P =
N∑
i=1
Ei Di (342)
V 2 =
N∑
i,j=1
Cij Di Dj (343)
S = P/V (344)
Here Ei are the expected stock returns. Instead of the dollar holdings Di, it is more
convenient to work with dimensionless holding weights (which are positive/negative
for long/short positions)
wi = Di/I (345)
61 For some literature on using machine learning for predicting stock returns, see, e.g., [Adam
and Lin, 2001], [Ang and Quek, 2006], [Chen, 2014], [Chen, Leung and Daouk, 2003], [Creamer
and Freund, 2007], [Creamer and Freund, 2010], [Gestel et al , 2001], [Grudnitski and Osborn,
1993], [Huang, Nakamori and Wang, 2005], [Huang and Tsai, 2009], [Huerta, Elkan and Corbacho,
2013], [Kablan, 2009], [Kakushadze and Yu, 2016b], [Kakushadze and Yu, 2017c], [Kakushadze
and Yu, 2018a], [Kara, Boyacioglu and Baykan, 2011], [Kim, 2003], [Kim, 2006], [Kim and Han,
2000], [Kordos and Cwiok, 2011], [Kryzanowski, Galler and Wright, 1993], [Kumar and Thenmozhi,
2001], [Liew and Mayster, 2018], [Lu, Lee and Chiu, 2009], [Milosevic, 2016], [Novak and Veluˇ s¸ cek,
2016], [Ou and Wang, 2009], [Refenes, Zapranis and Francis, 1994], [Rodr´ ıguez-Gonz´ alez et al ,
2011], [Saad, Prokhorov and Wunsch, 1998], [Schumaker and Chen, 2010], [Subha and Nambi,
2012], [Tay and Cao, 2001], [Teixeira and de Oliveira, 2010], [Tsai and Hsiao, 2010], [Vanstone and
Finnie, 2009], [Yao and Tan, 2000], [Yao, Tan and Poh, 1999], [Yu, Wang and Lai, 2005].
62 The sample covariance matrix based on a time series of historical returns is singular if T≤
N + 1, where T is the number of observations in the time series. Even if it is nonsingular, unless
T≫N, which is rarely (if ever) the case, the oﬀ-diagonal elements of the sample covariance matrix
typically are unstable out-of-sample. Therefore, in practice, typically a model covariance matrix
(which is positive-deﬁnite and should be suﬃciently stable out-of-sample) is used (see below).
55
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 57

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
where I is the total investment level. The holding weights satisfy the condition
N∑
i=1
|wi| = 1 (346)
We have P = I× ˜P , V = I×˜V and S = ˜P /˜V , where
˜P =
N∑
i=1
Ei wi (347)
˜V 2 =
N∑
i,j=1
Cij wi wj (348)
To determine the portfolio weights wi, often one requires that the Sharpe ratio
[Sharpe, 1966], [Sharpe, 1994] be maximized:
S→ max (349)
Assuming no additional conditions on wi (e.g., upper or lower bounds), the solution
to Eq. (349) in the absence of trading costs is given by
wi = γ
N∑
j=1
C−1
ij Ej (350)
where C−1 is the inverse of C, and the normalization coeﬃcient γ is determined
from Eq. (346) (and γ > 0 so ˜P > 0). The weights given by Eq. (350) generically
do not correspond to a dollar-neutral portfolio. To have a dollar-neutral portfolio,
we need to maximize the Sharpe ratio subject to the dollar-neutrality constraint.
3.18.1 Dollar-neutrality
We can achieve dollar-neutrality as follows. In the absence of bounds, trading costs,
etc., the Sharpe ratio is invariant under simultaneous rescalings of all holding weights
wi→ ζ wi, where ζ > 0. Due to this scale invariance, the Sharpe ratio maximization
problem can be recast in terms of minimizing a quadratic objective function:
g(w, λ) = λ
2
N∑
i,j=1
Cij wi wj−
N∑
i=1
Ei wi (351)
g(w, λ)→ min (352)
where λ > 0 is a parameter, and minimization is w.r.t. wi. The solution is given by
wi = 1
λ
N∑
j=1
C−1
ij Ej (353)
56
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 58

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
and λ is ﬁxed via Eq. (346). The objective function approach – which is the mean-
variance optimization [Markowitz, 1952] – is convenient if we wish to impose linear
homogeneous constraints (which do not spoil the aforesaid scale invariance) on wi,
e.g., the dollar-neutrality constraint. We introduce a Lagrange multiplier µ:63
g(w, µ, λ) = λ
2
N∑
i,j=1
Cij wi wj−
N∑
i=1
Ei wi− µ
N∑
i=1
wi (354)
g(w, µ, λ)→ min (355)
Minimization w.r.t. wi and µ now gives the following equations:
λ
N∑
j=1
Cij wj = Ei + µ (356)
N∑
i=1
wi = 0 (357)
So we have dollar-neutrality. The solution to Eqs. (356) and (357) is given by:
wi = 1
λ
[ N∑
j=1
C−1
ij Ej−
N∑
j=1
C−1
ij
∑N
k,l=1 C−1
kl El
∑N
k,l=1 C−1
kl
]
(358)
By construction, wi satisfy the dollar-neutrality constraint (357), and λ is ﬁxed via
Eq. (346). The expected returns Ei can be based on mean-reversion, momentum,
machine learning or other signals. Eq. (358) constructs a dollar-neutral portfolio
with “risk management” built in. E.g., the weights wi (roughly) are suppressed by
stock volatilities σi (where σ2
i = Cii) assuming that on average|Ei| are of order σi.64
The above implementation of the dollar-neutrality constraint via minimizing
the quadratic objective function (354) is equivalent to imposing this constraint
in Sharpe ratio maximization as no trading costs, position/trading bounds, non-
linear/inhomogeneous constraints, etc., are present. More generally Sharpe ratio
maximization is not equivalent to minimizing a quadratic objective function (see,
e.g., [Kakushadze, 2015b]), albeit in practice usually the latter approach is used.
63 By introducing multiple Lagrange multipliers, we can have multiple linear homogeneous
constraints (see, e.g., [Kakushadze, 2015b]).
64 Typically,Cij is a multifactor risk model covariance matrix. For a general discussion, see,
e.g., [Grinold and Kahn, 2000]. For explicit implementations (including source code), see, e.g.,
[Kakushadze, 2015e], [Kakushadze and Yu, 2016a], [Kakushadze and Yu, 2017a]. For multifactor
models, the weights are approximately neutral w.r.t. the columns of the factor loadings matrix.
The exact neutrality is attained in the zero speciﬁc risk limit, where optimization reduces to a
weighted regression (see, e.g., [Kakushadze, 2015b]).
57
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 59

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3.19 Strategy: Market-making
Over-simplistically, this strategy amounts to capturing the bid-ask spread for a given
stock and can be (again, over-simplistically) summarized as follows:
Rule =
{
Buy at the bid
Sell at the ask (359)
In a market where most order ﬂow is “dumb” (or uninformed), this strategy on
average would work very well. However, in a market where most order ﬂow is
“smart” (or informed, i.e., “toxic”), this strategy, as stated, would lose money. This
is because of adverse selection, where, precisely because most order ﬂow is smart,
most ﬁlls at the bid (ask) would be when the market is trading through it downward
(upward), so these trades would lose money. Furthermore, most limit orders to buy
(sell) at the bid (ask) would never be ﬁlled as the price would run away from them,
i.e., increase (decrease). So, ideally, this strategy should be structured such that it
captures dumb order ﬂow and avoids smart order ﬂow, which is not that simple.
One approach is, at any given time, within a short time horizon, to stay on
the “right” side of the market, i.e., to have a short-horizon signal indicating the
direction of the market and place limit orders accordingly (to buy at the bid if the
signal indicates a price increase, and to sell at the ask if the signal indicates a price
decrease). If the signal were (magically) 100% correct, this would capture the dumb
order ﬂow assuming that the orders get ﬁlled. This is a big assumption as for this
to be guaranteed, the trader would have to be #1 in the queue among many other
market participants placing limit orders at the same price point. This is where high
frequency trading comes in – it is essentially all about speed with which orders are
placed, canceled, and cancel-replaced. Infrastructure and technology are key in this.
Another possibility is to modulate the short-horizon signal with a longer-horizon
signal (which can still be an intraday signal). The longer-horizon signal typically
will have a higher cents-per-share 65 than the shorter-horizon signal. Now certain
trades can be proﬁtable even with adverse selection, because they are established
based on the longer-horizon signal. I.e., they “lose money” in the short term due to
adverse selection (as the market trades through the corresponding limit orders), but
they make money in a longer term. The market-making aspect of this is valuable
as placing a passive limit order as opposed to an aggressive market or limit order
saves money. On the other hand, in some cases, if the longer-horizon signal is strong
enough and the shorter-horizon signal is in the same direction, a passive limit order
would likely not get ﬁlled and it may make more sense to place an aggressive order.
Such aggressive order ﬂow is not dumb but smart, as it is based on nontrivial short-
and long-horizon signals with a positive expected return. 66 And speed still matters.
65 “Cents-per-share” is deﬁned as the realized P&L in cents (as opposed to dollars) divided by
the total shares traded (which includes both establishing and liquidating trades). Note that the
longer-horizon signal generally has a lower Sharpe ratio than the shorter-horizon signal.
66 Dumb order ﬂow can come from, e.g., uninformed retail traders. It can also come from ultra-
58
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 60

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
3.20 Strategy: Alpha combos
With technological advances – hardware becoming cheaper and more powerful – it
is now possible to data mine hundreds of thousands and even millions of alphas
using machine learning methods. Here the term “alpha” – following common trader
lingo – generally means any reasonable “expected return” that one may wish to
trade on and is not necessarily the same as the “academic” alpha. 67 In practice,
often the detailed information about how alphas are constructed may not even be
available, e.g., the only data available could be the position data, so “alpha” then is
a set of instructions to achieve certain stock (or some other instrument) holdings by
some times t1, t2, . . . Also, “machine learning” here refers to sophisticated methods
that go beyond single-stock methods such as those discussed in Subsection 3.17
and involve cross-sectional analyses based on price-volume as well as other types
of data (e.g., market cap, some other fundamental data such as earnings, industry
classiﬁcation data, sentiment data, etc.) for a large number of stocks (typically, a
few thousand and up). 101 explicit examples of such quantitative trading alphas
are given in [Kakushadze, 2016]. 68 The ﬂipside is that these ubiquitous alphas are
faint, ephemeral and cannot be traded on their own as any proﬁt on paper would be
eaten away by trading costs. To mitigate this, one combines a large number of such
alphas and trades the so-combined “mega-alpha”. Hence “alpha combo” strategies.
This is not critical, but for deﬁniteness let us assume that all alphas trade the
same underlying instruments, even more concretely, the same universe of (say, 2,500)
most liquid U.S. stocks. Each alpha produces desired holdings for this trading
universe. What we need is the weights with which to combine individual alphas,
whose number N can be large (in hundreds of thousands or even millions). 69 Here
long-horizon institutional traders (mutual funds, pension funds, etc.), whose outlook can be months
or years and who are not concerned about a few pennies’ worth of diﬀerence in the execution price on
short horizons (i.e., this is only “short-term dumb” order ﬂow). For a more detailed discussion, see,
e.g., [Kakushadze, 2015d], [Lo, 2008]. For some literature on high frequency trading and market-
making, see, e.g., [Aldridge, 2013], [Anand and Venkataraman, 2016], [Avellaneda and Stoikov,
2008], [Baron et al , 2014], [Benos et al , 2017], [Benos and Sagade, 2016], [Biais and Foucault,
2014], [Biais, Foucault and Moinas, 2014], [Bowen, Hutchinson and O’Sullivan, 2010], [Bozdoget al,
2011], [Brogaard and Garriott, 2018], [Brogaard et al, 2015], [Brogaard, Hendershott and Riordan,
2014], [Budish, Cramton and Shim, 2015], [Carrion, 2013], [Carrion and Kolay, 2017], [Easley,
L´ opez de Prado and O’Hara, 2011], [Easley, L´ opez de Prado and O’Hara, 2012], [Egginton, Van
Ness and Van Ness, 2016], [Hagstr¨ omer and Nord´ en, 2013], [Hagstr¨ omer, Nord´ en and Zhang,
2014], [Harris and Namvar, 2016], [Hasbrouck and Saar, 2013], [Hendershott, Jones and Menkveld,
2011], [Hendershott, Jones and Menkveld, 2013], [Hendershott and Riordan, 2013], [Hirschey, 2018],
[Holden and Jacobsen, 2014], [Jarrow and Protter, 2012], [Khandani and Lo, 2011], [Kirilenko et
al, 2017], [Korajczyk and Murphy, 2017], [Kozhan and Tham, 2012], [Li et al , 2014], [Madhavan,
2012], [Menkveld, 2013], [Menkveld, 2016], [Muthuswamy et al , 2011], [O’Hara, 2015], [Pagnotta
and Philippon, 2012], [Riordan and Storkenmaier, 2012], [Van Kervel and Menkveld, 2017].
67 By “academic” alpha we mean Jensen’s alpha [Jensen, 1968] or a similar performance index.
68 This is a secretive ﬁeld, so literature on this subject is very scarce. Also see, e.g., [Kakushadze
and Tulchinsky, 2016], [Tulchinsky et al , 2015].
69 Note that N here refers to the number of alphas, not the number of underlying stocks.
59
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 61

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
is a procedure for ﬁxing the alpha weights wi, i = 1 , . . . , N [Kakushadze and Yu,
2017b] (also see [Kakushadze and Yu, 2018a]):
• 1) Start with a time series of realized alpha returns70 Ris, i = 1, . . . , N, s =
1, . . . , M + 1.
• 2) Calculate the serially demeaned returns Xis = Ris− 1
M+1
∑M+1
s=1 Ris.
• 3) Calculate sample variances of alpha returns 71 σ2
i = 1
M
∑M+1
s=1 X2
is.
• 4) Calculate the normalized demeaned returns Yis = Xis/σi.
• 5) Keep only the ﬁrst M columns in Yis: s = 1, . . . , M.
• 6) Cross-sectionally demean Yis: Λis = Yis− 1
N
∑N
j=1 Yjs.
• 7) Keep only the ﬁrst M− 1 columns in Λis: s = 1, . . . , M− 1.
• 8) Take the expected alpha returns Ei and normalize them: ˜Ei = Ei/σi. One
(but by far not the only) way of computing expected alpha returns is via d-day
moving averages (note that d need not be the same as T ):
Ei = 1
d
d∑
s=1
Ris (360)
• 9) Calculate the residuals ˜εi of the regression (without the intercept and with
unit weights) of ˜Ei over Λis.
• 10) Set the alpha portfolio weights to wi = η˜εi/σi.
• 11) Set the normalization coeﬃcient η such that∑N
i=1|wi| = 1.
3.21 A few comments
We end this section with a few comments on some of the stock trading strategies dis-
cussed above. First, single-stock technical analysis strategies (i.e., those based solely
on single-stock as opposed to cross-sectional data) such as those based on moving
averages, support and resistance, channel and even single-stock KNN, are deemed
“unscientiﬁc” by many professionals and academics. On the face of it, “fundamen-
tally” speaking (not to be confused with fundamental analysis), there is no reason
why, say, a short moving average crossing a long moving average should have any
forecasting power.72 This is not to say that moving averages are “unscientiﬁc” or
that they should not be used. After all, e.g., trend following/momentum strategies
are based on moving averages, i.e., the expected returns are computed via moving
averages. However, looking at a large cross-section of stocks brings in a statistical
element into the game. Mean-reversion is expected to work because stocks are ex-
pected to be correlated if they belong to the same industries, etc. This relates back
70 Here s = 1,...,T =M + 1 labels the times ts, where, as before, t1 corresponds to the most
recent time (albeit the time direction is not crucial below), and the alpha returns are Ris =Ri(ts).
Typically, the alpha returns are computed daily, from close to close.
71 Their normalization is immaterial in what follows.
72 Arguendo, the momentum eﬀect may appear to provide a basis for such forecasting power in
some cases. However, then one could argue, e.g., that these are momentum strategies in disguise.
60
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 62

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
to fundamental analysis and – even more importantly – to the investors’ perception
of how stock prices/returns “should” behave based on the companies’ fundamentals.
However, here too it is important to keep in mind that the stock market – an imper-
fect man-made construct – is not governed by laws of nature the same way as, say,
the motion of planets in the solar system is governed by fundamental laws of gravity
(see, e.g., [Kakushadze, 2015d]). The markets behave the way they do because their
participants behave in certain ways, which are sometimes irrational and certainly
not always eﬃcient. In this regard, the key diﬀerence between technical analysis
strategies and statistical arbitrage strategies is that the latter are based on certain
perceptions trickled down from longer holding horizons (fundamental analysis based
strategies) to shorter horizons (statistical arbitrage) further enhanced by statistics,
i.e., the fact that these strategies are based on a large number of stocks whose
properties are further “stratiﬁed” according to some statistical and other features.
This brings us to the second point relating to precisely these “stratiﬁcations” in
the context of statistical arbitrage. Thus, in Subsection 3.10 we can use a binary
industry classiﬁcation matrix as the loadings matrix Ω iA. Such industry classi-
ﬁcations are based on pertinent fundamental/economic data, such as companies’
products and services, revenue sources, suppliers, competitors, partners, etc. They
are essentially independent of the pricing data and, if well-built, tend to be rather
stable out-of-sample as companies seldom jump industries. However, binary classi-
ﬁcations can also be built based purely on pricing data, via clustering algorithms
(see, e.g., [Kakushadze and Yu, 2016b]). Alternatively, the matrix Ω iA can be non-
binary and built using, say, principal components (see, e.g., [Kakushadze and Yu,
2017a]). Some of the columns of Ω iA can be based on longer-horizon style risk fac-
tors such as value, growth, size, momentum, liquidity and volatility (see, e.g., [Ang
et al, 2006], [Anson, 2013], [Asness, 1995], [Asness et al, 2001], [Asness, Porter and
Stevens, 2000], [Banz, 1981], [Basu, 1977], [Fama and French, 1992], [Fama and
French, 1993], [Haugen, 1995], [Jegadeesh and Titman, 1993], [Lakonishok, Shleifer
and Vishny, 1994], [Liew and Vassalou, 2000], [P´ astor and Stambaugh, 2003], [Sc-
holes and Williams, 1977]), 73 or shorter-horizon style factors [Kakushadze, 2015c].
4 Exchange-traded funds (ETFs)
4.1 Strategy: Sector momentum rotation
Empirical evidence suggests that the momentum eﬀect exists not only for individual
stocks but also for sectors and industries.74 A sector momentum rotation strategy is
73 For (il)liquidity related considerations, also see, e.g., [Amihud, 2002].
74 For some pertinent literature, see, e.g., [Cavaglia and Vadim, 2002], [Conover et al , 2008],
[Doeswijk and Vliet, 2011], [Dolvin and Kirby, 2011], [Gao and Ren, 2015], [Hong, Torous and
Valkanov, 2007], [Levis and Liodakis, 1999], [Moskowitz and Grinblatt, 1999], [O’Neal, 2000],
[Sefton and Scowcroft, 2005], [Simpson and Grossman, 2016], [Sorensen and Burke, 1986], [Stoval,
1996], [Swinkels, 2002], [Szakmary and Zhou, 2015], [Wang et al , 2017].
61
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 63

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
based on overweighing holdings in outperforming sectors and underweighing holdings
in underperforming sectors, where the “outperformance” and “underperformance”
are based on momentum during the past T -month formation period (which typically
ranges from 6 to 12 months). ETFs concentrated in speciﬁc sectors/industries oﬀer
a simple way to implement sector/industry rotation without having to buy or sell
a large number of underlying stocks. Similarly to Subsection 3.1, as a measure of
sector/industry momentum, we can use the corresponding ETF’s cumulative return:
Rcum
i (t) = Pi(t)
Pi(t + T )− 1 (361)
Here Pi(t) is the price of the ETF labeled by i. (As above, t + T is T months in the
past w.r.t. t.) Right after time t, the trader can, e.g., buy the ETFs in the top decile
by Rcum
i (t) and hold the portfolio for a holding period (typically 1 to 3 months).
Dollar-neutral strategies can also be constructed by, e.g., buying ETFs in the top
decile and shorting ETFs in the bottom decile (as stocks, ETFs can be shorted). 75
4.1.1 Strategy: Sector momentum rotation with MA ﬁlter
This is a variation/reﬁnement of the sector momentum rotation strategy. An ETF
in the top (bottom) decile is bought (sold) only if it passes an additional ﬁlter based
on a moving average MA( T′) of this ETF’s price:
Rule =
{
Buy top-decile ETFs only if P > MA(T′)
Short bottom-decile ETFs only if P < MA(T′) (362)
Here P is the ETF’s price at the time of the transaction, and MA( T′) is computed
using daily prices (T′ can but need not be equal T ; e.g., T′ can be 100 to 200 days).
4.1.2 Strategy: Dual-momentum sector rotation
In long-only strategies, to mitigate the risk of buying ETFs when the broad market
is trending down, relative (i.e., cross-sectional) momentum of sector ETFs can be
augmented by the absolute (i.e., time-series) momentum of, e.g., a broad market
index ETF (see, e.g., [Antonacci, 2014], [Antonacci, 2017]). 76 So, a long position
based on the sector rotation signal (discussed above) is established only if the broad
75 For some literature on ETFs, see, e.g., [Agapova, 2011a], [Aldridge, 2016], [Ben-David,
Franzoni and Moussawi, 2017], [Bhattacharya et al , 2017], [Buetow and Henderson, 2012], [Clif-
ford, Fulkerson and Jordan, 2014], [Hill, Nadig and Hougan, 2015], [Krause, Ehsani and Lien,
2014], [Madhavan, 2016], [Madura and Ngo, 2008], [Nyaradi, 2010], [Oztekin et al , 2017].
76 For some additional literature on relative momentum, absolute momentum and related topics,
see, e.g., [Ahn, Conrad and Dittmar, 2003], [Bandarchuk and Hilscher, 2013], [Berk, Green and
Naik, 1999], [Cooper, Gutierrez and Hameed, 2004], [Fama and French, 2008], [Hurst, Ooi and
Pedersen, 2017], [Johnson, 2002], [Liu and Zhang, 2008], [Moskowitz, Ooi and Pedersen, 2012], [Sagi
and Seasholes, 2007], [Schwert, 2003], [Zhang, 2006].
62
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 64

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
market index has an upward trend; otherwise, the total available funds are invested
into an ETF (e.g., gold or Treasury ETF) uncorrelated with the broad market index:
Rule =
{
Buy top-decile ETFs if P > MA(T′)
Buy an uncorrelated ETF if P≤ MA(T′) (363)
Here P is the broad market index ETF’s price at the time of the transaction, and
MA(T′) is the moving average of this ETF’s price. Typically, T′ is 100 to 200 days.
4.2 Strategy: Alpha rotation
This is the same as the sector momentum rotation strategy with the cumulative
ETF returns Rcum
i replaced by ETF alphas αi, which are the regression coeﬃcients
corresponding to the intercept in a serial regression of the ETF returns77 Ri(t) over,
e.g., the 3 Fama-French factors MKT(t), SMB(t), HML(t) (see fn. 50): 78
Ri(t) = αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + ϵi(t) (364)
4.3 Strategy: R-squared
Empirical studies for mutual funds (see, e.g., [Amihud and Goyenko, 2013], [Fer-
son and Mo, 2016]) and ETFs (see, e.g., [Garyn-Tal, 2014a], [Garyn-Tal, 2014b])
suggest that augmenting alpha by an indicator based on R2 of a serial regression
of the returns Ri(t) over multiple factors, e.g., the 3 Fama-French factors MKT( t),
SMB(t), HML(t) plus Carhart’s momentum factor MOM( t) (see fn. 50), adds value
in forecasting future returns. Thus, from the serial regression
Ri(t) = αi + β1,i MKT(t) +β2,i SMB(t) +β3,i HML(t) +β4,i MOM(t) +ϵi(t) (365)
we can estimate αi (the regression coeﬃcients corresponding to the intercept) and
the regression R2, which is deﬁned as (“SS” stands for “sum of squares”):
R2 = 1− SSres
SStot
(366)
SSres =
N∑
i=1
ϵ2
i (t) (367)
SStot =
N∑
i=1
(Ri(t)− R(t))2 (368)
R(t) = 1
N
N∑
i=1
Ri(t) (369)
77 Typically, the estimation period is 1 year, and Ri(t) are daily or weekly returns.
78 Alpha here is Jensen’s alpha deﬁned for ETF returns as opposed to mutual fund returns
as in [Jensen, 1968]. For some additional literature related to Jensen’s alpha, see, e.g., [Bollen
and Busse, 2005], [Droms and Walker, 2001], [Elton, Gruber and Blake, 1996a], [Goetzmann and
Ibbotson, 1994], [Grinblatt and Titman, 1992], [Jan and Hung, 2004].
63
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 65

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
An R-squared strategy then amounts to overweighing ETFs with higher “selectivity”
(deﬁned as 1−R2 [Amihud and Goyenko, 2013]) and underweighing ETFs with lower
“selectivity”. E.g., one can ﬁrst sort ETFs into quintiles by R2, and then sort ETFs
in each such quintile into further sub-quintiles by alpha (resulting in 25 groups of
ETFs). One can then, e.g., buy ETFs in the group corresponding to the lowest R2
quintile and its highest alpha sub-quintile and sell ETFs in the group corresponding
to the highest R2 quintile and its lowest alpha sub-quintile. Other variations are
possible. Finally, the estimation period and the returns for R2 can be the same
as in the alpha rotation strategy (see Subsection 4.2 and fn. 77). However, longer
estimation periods can be considered, especially if Ri(t) are monthly returns. 79
4.4 Strategy: Mean-reversion
One way (among myriad others) to construct a mean-reversion strategy for ETFs is
to use the Internal Bar Strength (IBS) based on the previous day’s close PC, high
PH and low PL prices:80
IBS = PC− PL
PH− PL
(370)
Note that IBS ranges from 0 to 1. 81 An ETF can be thought of as being “rich” if its
IBS is close to 1, and as “cheap” if its IBS is close to 0. Upon sorting a universe of
ETFs cross-sectionally by IBS, a dollar-neutral strategy can, e.g., be constructed by
selling ETFs in the top decile and buying ETFs in the bottom decile. As with stock
strategies discussed above, weights can be uniform for all long and all short ETFs,
respectively, or nonuniform, e.g., based on historical ETF volatilities. Furthermore,
mean-reversion strategies we discussed above for stocks can also be adapted to ETFs.
4.5 Strategy: Leveraged ETFs (LETFs)
A leveraged (inverse) ETF seeks to double or triple (the inverse of) the daily return of
its underlying index.82 To maintain a daily leverage of 2× or 3×, LETFs rebalance
79 Also, note that in [Amihud and Goyenko, 2013] R2 is a measure of active management of a
mutual fund. In [Garyn-Tal, 2014a], [Garyn-Tal, 2014b] R2 is applied to actively managed ETFs.
For some additional literature on actively managed ETFs, see, e.g., [Mackintosh, 2017], [Meziani,
2015], [Rompotis, 2011a], [Rompotis, 2011b], [Schizas, 2014], [Sherrill and Upton, 2018].
80 See, e.g., [Pagonidis, 2014]. For some additional related literature, see, e.g., [Brown, Davies
and Ringgenberg, 2018], [Caginalp, DeSantis and Sayrak, 2014], [Chan, 2013], [Dunis, Laws and
Rudy, 2013], [Lai, Tseng and Huang, 2016], [Levy and Lieberman, 2013], [Marshall, Nguyen and
Visaltanachoti], [Rudy, Dunis and Laws, 2010], [Schizas, Thomakos and Wang, 2011], [Smith and
Pantilei, 2015], [Yu and Webb, 2014].
81 An equivalent but more symmetrical measure is Y = IBS− 1/2 = (PC−P∗)/(PH−PL),
where P∗ = (PH +PL)/2. Note that Y ranges from 1/2 for PC =PH to−1/2 for PC =PL.
82 For some literature on leveraged ETFs, see e.g., [Avellaneda and Zhang, 2010], [Bai, Bond
and Hatch, 2015], [Charupat and Miu, 2011], [Cheng and Madhavan, 2010], [Ivanov and Lenkey,
2014], [Jarrow, 2010], [Jiang and Peterburgsky, 2017], [Lu, Wang and Zhang, 2012], [Shum et al ,
2016], [Tang and Xu, 2013], [Trainor, 2010], [Tuzun, 2013].
64
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 66

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
every day, which requires buying on the days when the market is up and selling
when the market is down. This can result in a negative drift in the long term, which
can be exploited by shorting both a leveraged ETF and a leveraged inverse ETF
(both with the same leverage and for the same underlying index) and investing the
proceeds into, e.g., a Treasury ETF. This strategy can have a signiﬁcant downside
risk in the short term if one of the short ETF legs has a sizable positive return.
4.6 Strategy: Multi-asset trend following
One allure of ETFs is their diversiﬁcation power: ETFs allow to gain exposure
to diﬀerent sectors, countries, asset classes, factors, etc., by taking positions in a
relatively small number of ETFs (as opposed to taking positions in a large number
of underlying instruments, e.g., thousands of stocks). Here we focus on long-only
trend-following portfolios. One needs to determine the weight wi of each ETF.
One (but by far not the only) way to ﬁx these weights is as follows. First, as
in the sector momentum rotation strategy, we compute cumulative returns Rcum
i
(over some period T , e.g., 6-12 months). We only take ETFs with positive Rcum
i .
If desired, optionally, we can further ﬁlter out ETFs as in the sector momentum
rotation strategy with an MA ﬁlter, by keeping only the ETFs whose last closing
prices Pi are higher than their corresponding long-term moving averages MA i(T′)
(typically, the MA length T′ is 100 to 200 days). Now, instead of taking ETFs in
the top decile by Rcum
i (as in the sector momentum rotation strategy), we can assign
nonzero weights wi to all remaining ETFs, whose number in this context is relatively
small to begin with by design. The weights can, e.g., be assigned as follows:
wi = γ1 Rcum
i (371)
wi = γ2 Rcum
i /σi (372)
wi = γ3 Rcum
i /σ2
i (373)
Here: σi is the historical volatility; and the overall normalization coeﬃcientsγ1, γ2, γ3
in each case are computed based on the requirement that ∑N
i=1 wi = 1 (where N
is the number of ETFs in our portfolio after all ﬁlters are applied, i.e., those with
nonzero weights). Thus, the weights in Eq. (371) are simply proportional to the
past cumulative returns Rcum
i , which are taken as the measure of momentum, so
the expected returns are also given by (or, more precisely, proportional to) Rcum
i .
The issue with this weighting scheme is that it overweighs volatile ETFs as on
average Rcum
i ∝ σi. The weights in Eq. (372) mitigate this, while the weights
in Eq. (373) actually optimize the Sharpe ratio of the ETF portfolio assuming a
diagonal covariance matrix Cij = diag( σ2
i ) for the ETF returns, i.e., by ignoring
their correlations.83 Imposing bounds wi≤ wmax
i can further mitigate overweighing.
83 For some literature on multi-asset portfolios, dynamic asset allocation and related topics, see,
e.g., [Bekkers, Doeswijk and Lam, 2009], [Black and Litterman, 1992], [Detemple and Rindisbacher,
2010], [Doeswijk, Lam and Swinkels, 2014], [Faber, 2015], [Faber, 2016], [Mladina, 2014], [Petre,
65
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 67

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
5 Fixed Income
5.1 Generalities
5.1.1 Zero-coupon bonds
A promise of being paid $1 at the maturity timeT can be regarded as an asset, which
has some worth at time t before T . This asset is called a (zero-coupon) discount
bond. Let its price at time 0 ≤ t≤ T be P (t, T). Then P (T, T ) = 1. The yield of a
discount bond is deﬁned as 84
R(t, T) =−ln(P (t, T))
T− t (374)
and has the meaning of an average interest rate over the period of time T− t. The
higher the bond price at time t, the lower the yield R(t, T) and vice versa. Below
we refer to a zero-coupon bond with a $1 principal and maturity T as a T -bond.
5.1.2 Bonds with coupons
In practice, a bond usually pays not only its principal at maturity T , but also
makes smaller coupon payments before maturity. Consider a bond that makes n
regular coupon payments at a ﬁxed uncompounded rate k at times Ti = T0 + iδ,
i = 1, 2, . . . , n, and also pays $1 principal at maturityT . The amount of each coupon
payment is kδ, where δ is the payment period. This income stream is equivalent to
owning one T -bond plus kδ units of each Ti-bond, i = 1 , . . . , n. The price of the
coupon bond at time t then is
Pc(t, T) = P (t, T) + kδ
n∑
i=I(t)
P (t, Ti) (375)
where I(t) = min(i : t < Ti). At time t = T0 we have
Pc(T0, T) = P (T0, T) + kδ
n∑
i=1
P (T0, Ti) (376)
If we desire the coupon bond to start with its face value ( Pc(T0, T) = 1), then the
corresponding coupon rate is given by
k = 1− P (T0, T)
δ∑n
i=1 P (T0, Ti) (377)
2015], [Sassetti and Tani, 2006], [Sharpe, 2009], [Sharpe and Perold, 2009], [Sørensen, 1999], [Tri-
pathi and Garg, 2016], [Wu, 2003], [Zakamulin, 2014b].
84 More precisely, this deﬁnition assumes continuous compounding. For periodic compounding
at n discrete times Ti = T0 +iδ, i = 1,...,n , the yield between t = T0 and t = Tn is given by
R(T0,Tn) =δ−1(
[P (T0,Tn)]−1/n− 1
)
assumingP (Tn,Tn) = 1, i.e., Tn is the maturity. Eq. (374)
is recovered in the limit where n→∞ , δ→ 0, nδ = ﬁxed (and equal to T−t in Eq. (374)).
66
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 68

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
5.1.3 Floating rate bonds
A bond might also have ﬂoating coupon payments. Thus, consider a bond that
pays $1 at maturity T , and also makes coupon payments at times Ti = T0 + iδ,
i = 1 , 2, . . . , n, with amounts based on the variable rate (usually LIBOR – see
Subsection 5.15)
L(Ti−1) = 1
δ
[ 1
P (Ti−1, Ti)− 1
]
(378)
The actual coupon payment at time Ti is
Xi = L(Ti−1)δ = 1
P (Ti−1, Ti)− 1 (379)
which is the amount of interest we would get by buying $1’s worth of a Ti-bond
at time Ti−1. Indeed, a Ti-bond is worth P (Ti−1, Ti) at t = Ti−1, so $1’s worth a
Ti-bond at t = Ti−1 is worth 1 /P (Ti−1, Ti) at t = Ti, so the interest earned is given
by Eq. (379). The total value of the variable coupon bond at t = T0 is given by:
V0 = 1− [P (T0, Tn)− P (T0, T)] (380)
If T = Tn, then we have V0 = 1. This is because this bond is equivalent to the
following sequence of trades. At time t = T0 take $1 and buy T1-bonds with it. At
time t = T1 take the interest from the T1-bonds as the T1-coupon, and buy T2-bonds
with the leftover $1 principal. Repeat until we are left with $1 at time Tn. This has
exactly the same cash ﬂow as the variable coupon bond, so the initial prices must
match. If T > T n, then V0 < 1 and can be determined as follows. First, note that
V0 = P (T0, T) + Vcoupons
0 (381)
where Vcoupons
0 is the total value of all n coupon payments at t = T0. This value is
independent of T and is determined from
P (T0, Tn) + Vcoupons
0 = 1 (382)
which is the value of the variable coupon bond with maturity Tn. Hence Eq. (380).
5.1.4 Swaps
Swaps are contracts that exchange a stream of ﬂoating rate payments for a stream
of ﬁxed rate payments or vice versa. A swap where we receive a stream of ﬁxed rate
payments in exchange for ﬂoating rate payments is simply a portfolio which is long
a ﬁxed coupon bond and short a variable coupon bond. The price of the former at
t = T0 is given by Eq. (376), while that of the latter is given by Eq. (380). The
ﬁxed rate that gives the swap initial null value is independent of maturity T and
given by
k = 1− P (T0, Tn)
δ∑n
i=1 P (T0, Ti) (383)
67
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 69

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
5.1.5 Duration and convexity
Macaulay duration of a bond is a weighted average maturity of its cash ﬂows, where
the weights are the present values of said cash ﬂows. E.g., for a ﬁxed rate coupon
bond we have (see Eq. (376))
MacD(t, T) = 1
Pc(t, T)

(T− t) P (t, T) + kδ
n∑
i=I(t)
(Ti− t) P (t, Ti)

 (384)
Modiﬁed duration is deﬁned as (assuming parallel shifts in the yield curve) 85
ModD(t, T) =− ∂ ln (Pc(t, T))
∂R(t, T) (385)
For continuous compounding, Macaulay duration and modiﬁed duration are the
same (see Eq. (374)). For periodic compounding, they diﬀer. For a constant yield
R(t, τ) = Y = const. (for all t < τ < T ), they are related via (see fn. 84):
ModD(t, T) = MacD(t, T)/(1 + Y δ) (386)
Modiﬁed duration is a measure of the relative bond price sensitivity to changes in
the interest rates: ∆ Pc(t, T)/Pc(t, T)≈− ModD(t, T) ∆ R(t, T) (for parallel shifts
∆R(t, τ) = ∆R = const., for all t < τ < T ). Similarly, dollar duration deﬁned as
DD(t, T) =− ∂Pc(t, T)
∂R(t, T) = ModD(t, T) Pc(t, T) (387)
is a measure of the absolute bond price sensitivity to changes in the interest rates.
Convexity of a bond is deﬁned as (again, assuming parallel shifts) 86
C(t, T) =− 1
Pc(t, T)
∂2Pc(t, T)
∂R(t, T)2 (388)
and corresponds to nonlinear eﬀects in the response of the bond price to interest
rate changes:
∆Pc(t, T)/Pc(t, T)≈− ModD(t, T) ∆R(t, T) + 1
2 C(t, T) [∆R(t, T)]2 (389)
85 I.e., ∂R(t,τ )/∂R(t,T ) = 1 for all t<τ <T . For nonuniform shifts things get complicated.
86 For some literature on various properties of bonds, see, e.g., [Baxter and Rennie, 1996],
[Bessembinder and Maxwell, 2008], [ ˇCerovi´ cet al , 2014], [Chance and Jordan, 1996], [Chen,
Lesmond and Wei, 2007], [Chen, Mao and Wang, 2010], [Christensen, 1999], [Cole and Young,
1995], [Fabozzi, 2006a], [Fabozzi, 2012a], [Fabozzi, 2012b], [Fabozzi and Mann, 2010], [Hen-
derson, 2003], [Horvath, 1998], [Hotchkiss and Ronen, 2002], [Hull, 2012], [Hull, Predescu and
White, 2005], [Jostova et al , 2013], [Kakushadze, 2015a], [Leland and Panos, 1997], [Litterman
and Scheinkman, 1991], [Macaulay, 1938], [Martellini, Priaulet and Priaulet, 2003], [Osborne,
2005], [Samuelson, 1945], [Stulz, 2010], [Tuckman and Serrat, 2015].
68
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 70

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
5.2 Strategy: Bullets
In a bullet portfolio, all bonds have the same maturity date T thereby targeting a
speciﬁc segment of the yield curve. The maturity can be picked based on the trader’s
outlook on the future interest rates: if the interest rates are expected to fall (i.e.,
the bond prices to rise), then picking a longer maturity would make more sense; if
the interest rates are expected to rise (i.e., the bond prices to fall), then a shorter
maturity would be more warranted; however, if the trader is uncertain about the
future interest rates, a more diversiﬁed portfolio (e.g., a barbell/ladder portfolio –
see below) is in order (as opposed to a bullet portfolio). Typically, the bonds in a
bullet portfolio are purchased over time, which mitigates the interest rate risk to
some extent: if the interest rates rise, the later bond purchases will be at higher
rates; if the interest rates fall, the earlier bond purchases will have higher yields. 87
5.3 Strategy: Barbells
In this strategy all purchased bonds are concentrated in two maturities T1 (short
maturity) and T2 (long maturity), so this portfolio is a combination of two bullet
strategies. This strategy takes advantage of the higher yields from the long-maturity
bonds while hedging the interest rate risk with the short-maturity bonds: if the
interest rates rise, the long-maturity bonds will lose value, but the proceeds from
the short-maturity bonds can be reinvested at higher rates.88 The modiﬁed duration
(call it D) of the barbell strategy is the same as the modiﬁed duration (call it
D∗) of a bullet strategy with a mid-range maturity (call it T∗, T1 < T∗ < T 2).
However, the convexity (call itC) of the barbell strategy is higher than the convexity
(call it C∗) of this bullet strategy. Intuitively this can be understood by noting
that modiﬁed duration scales approximately linearly with maturity, while convexity
scales approximately quadratically with maturity. For illustrative purposes and
simplicity, let us consider a barbell strategy consisting of w1 dollars’ worth of zero-
coupon bonds with short maturity T1 and w2 dollars’ worth of zero-coupon bonds
with long maturity T2 (each bond has $1 face value). Furthermore, let us assume
continuous compounding and a constant yield Y . We then have
D = ˜w1 T1 +˜w2 T2
˜w1 +˜w2
(390)
T∗ = D∗ = D (391)
C = ˜w1 T 2
1 +˜w2 T 2
2
˜w1 +˜w2
(392)
C∗ = T 2
∗ (393)
87 For some literature on bullet and barbell (see below) strategies, see, e.g., [Fabozzi, Martellini
and Priaulet, 2006], [Grantier, 1988], [Jones, 1991], [Mann and Ramanlal, 1997], [Pascalau and
Poirier, 2015], [Su and Knowles, 2010], [Wilner, 1996], [Yamada, 1999].
88 Flattening/steepening of the yield curve (the spread between the short-term and long-term
interest rates decreases/increases) has a positive/negative impact on the value of the portfolio.
69
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 71

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
where ˜w1 = w1 exp(−T1 Y ) and ˜w2 = w2 exp(−T2 Y ). Straightforward algebra
gives
C− C∗ = ˜w1˜w2
(˜w1 +˜w2)2 (T2− T1)2 > 0 (394)
Higher convexity of the barbell portfolio provides a better protection against parallel
shifts in the yield curve. However, this comes at the expense of a lower overall yield.
5.4 Strategy: Ladders
A ladder is a bond portfolio with (roughly) equal capital allocations into bonds
of n diﬀerent maturities Ti, i = 1 , . . . , n (where the number of rungs n is sizable,
e.g., n = 10). The maturities are equidistant: Ti+1 = Ti + δ. This is a duration-
targeting strategy,89 which maintains an approximately constant duration by selling
shorter-maturity bonds as they approach maturity and replacing them with new
longer-maturity bonds. A ladder portfolio aims to diversify the interest rate and
reinvestment risks90 by avoiding exposure to only a few maturities (as in bullets and
barbells). It also generates a regular revenue stream from the coupons of each bond.
The maturity of a ladder portfolio can be deﬁned as the average maturity:
T = 1
n
n∑
i=1
Ti (395)
The income is higher for higher values of T ; however, so is the interest rate risk.
5.5 Strategy: Bond immunization
Bond immunization is used in cases such as a predetermined future cash obligation.
A simple solution would be to purchase a zero-coupon bond with the required ma-
turity (and desirable/acceptable yield). However, such a bond may not always be
available in the market, so a portfolio of bonds with varying maturities must be used
instead. Such a portfolio is subject to the interest rate and reinvestment risks. One
way to mitigate these risks is to build a portfolio whose duration matches the matu-
rity of the future cash obligation (thereby “immunizing” the bond portfolio against
parallel shifts in the yield curve). Consider a portfolio of bonds with 2 diﬀerent
maturities T1, T2 and the corresponding durations D1, D2 (where “duration” means
modiﬁed duration). Let: the dollar amounts invested in these bonds be P1, P2; the
total amount to be invested be P ; the desired duration of the portfolio be D (which
89 For some literature on ladder and duration-targeting strategies, see, e.g., [Bierwag and Kauf-
man, 1978], [Bohlin and Strickland, 2004], [Cheung, Kwan and Sarkar, 2010], [Dyl and Martin,
1986], [Fridson and Xu, 2014], [Judd, Kubler and Schmedders, 2011], [Langetieg, Leibowitz and
Kogelman, 1990], [Leibowitz and Bova, 2013], [Leibowitz, Bova and Kogelman, 2014], [Leibowitz,
Bova and Kogelman, 2015].
90 The reinvestment risk is the risk that the proceeds (from coupon payments and/or principal)
would be reinvested at a lower rate than the original investment.
70
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 72

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
is related to the maturity T∗ of the future cash obligation – see below); and the
constant yield (which is assumed to be the same for all bonds – see below) be Y .
Then P is ﬁxed using Y and the amount of the future obligation F :
P = F/(1 + Y δ)T∗/δ (396)
where we are assuming periodic compounding and δ is the length of each compound-
ing period (e.g., 1 year). 91 Then we have:
P1 + P2 = P (397)
P1 D1 + P2 D2 = P D (398)
where
D = T∗/(1 + Y δ) (399)
With 3 bonds, we can also match the convexity:
P1 + P2 + P3 = P (400)
P1 D1 + P2 D2 + P3 D3 = P D (401)
P1 C1 + P2 C2 + P3 C3 = P C (402)
where C1, C2, C3 are the convexities of the 3 bonds and
C = T∗(T∗ + δ)/(1 + Y δ)2 (403)
In practice, the yield curve changes over time, which (among other things) requires
that the portfolio be periodically rebalanced. This introduces nontrivial transaction
costs, which must also be accounted for. Furthermore, the yields are not the same for
all bonds in the portfolio, which introduces additional complexity into the problem.92
5.6 Strategy: Dollar-duration-neutral butterﬂy
This is a zero-cost combination of a long barbell portfolio (with short T1 and long
T3 maturities) and a short bullet portfolio (with a medium maturity T2, where
T1 < T 2 < T 3). Let: the dollar amounts invested in the 3 bonds be P1, P2, P3; and
91 For the sake of simplicity, in Eq. (396) the number n = T∗/δ of compounding periods is
assumed to be a whole number. Extension to non-integer T∗/δ is straightforward.
92 For some literature on bond immunization, including more sophisticated optimization tech-
niques, see, e.g., [Albrecht, 1985], [Alexander and Resnick, 1985], [Bierwag, 1979], [Bodie, Kane and
Marcus, 1996], [Boyle, 1978], [Christensen and Fabozzi, 1985], [De La Pe˜ na, Garayeta and Iturricas-
tillo, 2017], [Fisher and Weil, 1971], [Fong and Vasicek, 1983], [Fong and Vasicek, 1984], [H¨ urlimann,
2002], [H¨ urlimann, 2012], [Iturricastillo and De La Pe˜ na, 2010], [Khang, 1983], [Kocherlakota,
Rosenbloom and Shiu, 1988], [Kocherlakota, Rosenbloom and Shiu, 1990], [Montrucchio and Pec-
cati, 1991], [Nawalkha and Chambers, 1996], [Reddington, 1952], [Reitano, 1996], [Shiu, 1987],
[Shiu, 1988], [Zheng, Thomas and Allen, 2003].
71
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 73

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
the corresponding modiﬁed durations be D1, D2, D3. Then zero cost (i.e., dollar-
neutrality) and the dollar-duration-neutrality (the latter protects the portfolio from
parallel shifts in the yield curve) imply that
P1 + P3 = P2 (404)
P1 D1 + P3 D3 = P2 D2 (405)
This ﬁxes P1, P3 via P2. While the portfolio is immune to parallel shifts in the yield
curve, it is not immune to changes in the slope or the curvature of the yield curve. 93
5.7 Strategy: Fifty-ﬁfty butterﬂy
This is a variation of the standard butterﬂy. In the above notations for the dollar-
duration-neutral butterﬂy, we have
P1 D1 = P3 D3 = 1
2 P2 D2 (406)
So, the ﬁfty-ﬁfty butterﬂy is still dollar-duration-neutral, but it is no longer dollar-
neutral (i.e., it is not a zero-cost strategy). Instead, dollar durations of the wings are
the same (hence the term “ﬁfty-ﬁfty”). As a result, the strategy is (approximately)
neutral to small steepening and ﬂattening of the yield curve, to wit, if the interest
rate spread change between the body and the short-maturity wing is equal to the
spread change between the long-maturity wing and the body. That is why this
strategy is a.k.a. “neutral curve butterﬂy” (whose cost is non-dollar-neutrality).
5.8 Strategy: Regression-weighted butterﬂy
Empirically, short-term interest rates are sizably more volatile than long-term in-
terest rates.94 Therefore, the interest rate spread change between the body and the
short-maturity wing (of the butterﬂy – see above) can be expected to be greater by
some factor – call it β – than the spread change between the long-maturity wing
and the body (so, typically β > 1). This factor can be obtained from historical
data via, e.g., running a regression of the spread change between the body and the
short-maturity wing over the spread change between the long-maturity wing and the
body. Then, instead of Eq. (406), we have the following dollar-duration-neutrality
and “curve-neutrality” conditions:
P1 D1 + P3 D3 = P2 D2 (407)
P1 D1 = β P 3 D3 (408)
93 For some literature on various butterﬂy bond strategies, see, e.g., [Bedendo, Cathcart and
El-Jahel, 2007], [Brooks and Moskowitz, 2017], [Christiansen and Lund, 2005], [Fontaine and Nolin,
2017], [Gibson and Pritsker, 2000], [Grieves, 1999], [Heidari and Wu, 2003], [Martellini, Priaulet
and Priaulet, 2002].
94 See, e.g., [Edwards and Susmel, 2003], [Joslin and Konchitchki, 2018], [Mankiw and Summers,
1984], [Shiller, 1979], [Sill, 1996], [Turnovsky, 1989].
72
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 74

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
5.8.1 Strategy: Maturity-weighted butterﬂy
This is a variation of the regression-weighted butterﬂy, where instead of ﬁxing β in
Eq. (408) via a regression based on historical data, this coeﬃcient is based on the
3 bond maturities:
β = T2− T1
T3− T2
(409)
5.9 Strategy: Low-risk factor
As in stocks, empirical evidence suggests that lower-risk bonds tend to outperform
higher-risk bonds on the risk-adjusted basis (“low-risk anomaly”). 95 One can deﬁne
“riskiness” of a bond using diﬀerent metrics, e.g., bond credit rating and maturity.
For instance, a long portfolio can be built (see, e.g., [Houweling and van Vundert,
2017]) by taking Investment Grade bonds with credit ratings AAA through A-, and
then taking the bottom decile by maturity. Similarly, one can take High Yield bonds
with credit ratings BB+ through B-, and then take the bottom decile by maturity.
5.10 Strategy: Value factor
“Value” for bonds (see, e.g., [Correia, Richardson and Tuna, 2012], [Houweling and
van Vundert, 2017], [L’Hoir and Boulhabel, 2010]) is trickier to deﬁne than for stocks.
One way is to compare the observed credit spread 96 to a theoretical prediction
therefor. One way to estimate the latter is, e.g., via a linear cross-sectional (across
N bonds labeled by i = 1, . . . , N) regression [Houweling and van Vundert, 2017]:
Si =
K∑
r=1
βr Iir + γ Ti + ϵi (410)
S∗
i = Si− ϵi (411)
Here: Si is the credit spread; Iir is a dummy variable ( Iir = 1 if the bond labeled
by i has credit rating r; otherwise, Iir = 0) for bond credit rating r (which labels
K credit ratings present among the N bonds, which can be one of the 21 credit
ratings);97 Ti are bond maturities; βr, γ are the regression coeﬃcients; ϵi are the
regression residuals; and S∗
i is the ﬁtted (theoretical) value of the credit spread.
The N× K matrix Iir has no columns with all zeros (so K can be less than 21).
Note that by deﬁnition, since each bond has one and only one credit rating, we have
K∑
r=1
Iir = 1 (412)
95 For some literature, see, e.g., [De Carvalho et al , 2014], [Derwall, Huij and De Zwart, 2009],
[Frazzini and Pedersen, 2014], [Houweling and van Vundert, 2017], [Ilmanen, 2011], [Ilmanen et al,
2004], [Kozhemiakin, 2007], [Ng and Phelps, 2015].
96 Credit spread is the diﬀerence between the bond yield and the risk-free rate.
97 These credit ratings are AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB,
BB-, B+, B, B-, CCC+, CCC, CCC-, CC, C.
73
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 75

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
so the intercept is subsumed in Iir (which is why there is no separate regression
coeﬃcient for the intercept). Next, value is deﬁned asVi = ln(Si/S∗
i ) or Vi = ϵi/S∗
i =
Si/S∗
i− 1, and the bonds in the top decile by Vi are selected for the portfolio.
5.11 Strategy: Carry factor
Carry is deﬁned as the return from the appreciation of the bond value as the bond
rolls down the yield curve (see, e.g., [Beekhuizen et al , 2016], [Koijen, Moskowitz,
Pedersen and Vrugt, 2018]):98
C(t, t + ∆t, T) = P (t + ∆t, T)− P (t, T)
P (t, T) (413)
Here ∆ t is the period over which carry is computed. A simpliﬁcation arises if we
assume that the entire term structure of the interest rates stays constant, i.e., the
yield R(t, T) = f(T− t) is a function of only T− t (i.e., time to maturity). Then,
at time t + ∆t the yield is R(t + ∆t, T) = R(t, T− ∆t). So, we have 99
C(t, t + ∆t, T) =
P (t + ∆t, T)|R(t+∆t,T )− P (t, T)|R(t,T )
P (t, T)|R(t,T )
=
= R(t, T) ∆t + Croll(t, t + ∆t, T) (414)
where (taking into account the deﬁnition of the modiﬁed duration, Eq. (385))
Croll(t, t + ∆t, T) =
P (t + ∆t, T)|R(t,T−∆t)− P (t + ∆t, T)|R(t,T )
P (t, T)|R(t,T )
≈
≈ −ModD(t, T) [R(t, T− ∆t)− R(t, T)] (415)
So, if the term structure of the interest rates is constant, then carry C(t, t + ∆t, T)
receives two contributions: i) R(t, T) ∆t from the bond yield; and ii)Croll(t, t+∆t, T)
from the bond rolling down the yield curve. A zero-cost strategy can be built, e.g.,
by buying bonds in the top decile by carry and selling bonds in the bottom decile.
5.12 Strategy: Rolling down the yield curve
The objective of this strategy is to capture the “roll-down” component Croll(t, t +
∆t, T) of bond yields. These returns are maximized in the steepest segments of the
yield curve. Therefore, the trader can, e.g., buy long- or medium-term bonds from
98 Here, for the sake of simplicity, we consider zero-coupon bonds. The end-result below is also
valid for coupon bonds.
99 For ﬁnanced portfolios, R(t,T ) in the second line of Eq. (414) is replaced by R(t,T )−rf,
whererf is the risk-free rate. However, this overall shift does not aﬀect the actual holdings in the
carry strategy below.
74
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 76

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
such segments and hold them while they are “rolling down the curve”.100 The bonds
must be sold as they approach maturity and the proceeds can be used to buy new
long/medium-term bonds from the steepest segment of the yield curve at that time.
5.13 Strategy: Yield curve spread (ﬂatteners & steepeners)
This strategy consists of buying or selling the yield curve spread. 101 The yield curve
spread is deﬁned as the diﬀerence between the yields of two bonds of the same issuer
with diﬀerent maturities. If the interest rates are expected to fall, the yield curve
is expected to steepen. If the interest rates are expected to rise, the yield curve
is expected to ﬂatten. The yield curve spread strategy can be summarized via the
following rule:
Rule =
{
Flattener: Short spread if interest rates are expected to rise
Steepener: Buy spread if interest rates are expected to fall (416)
Shorting the spread amounts to selling shorter-maturity bonds (a.k.a. the front leg)
and buying longer-maturity bonds (a.k.a. the back leg). Buying the spread is the
opposite trade: buying the front leg and selling the back leg. If the yield curve has
parallel shifts, this strategy can generate losses. Matching dollar durations of the
front and back legs immunizes the portfolio to small parallel shifts in the yield curve.
5.14 Strategy: CDS basis arbitrage
A credit default swap (CDS) is insurance against default on a bond. 102 The CDS
price, known as the CDS spread, is a periodic (e.g., annual) premium per dollar
of the insured debt. The CDS essentially makes the bond a risk-free instrument.
Therefore, the CDS spread should equal the bond yield spread, i.e., the spread
between the bond yield and the risk-free rate. The diﬀerence between the CDS
spread and the bond spread is known as the CDS basis:
CDS basis = CDS spread− bond spread (417)
100 For some literature on the “rolling down the yield curve” strategies, see, e.g., [Ang, Alles
and Allen, 1998], [Bieri and Chincarini, 2004], [Bieri and Chincarini, 2005], [Dyl and Joehnk,
1981], [Grieves et al, 1999], [Grieves and Marcus, 1992], [Osteryoung, McCarty and Roberts, 1981],
[Pantalone and Platt, 1984], [Pelaez, 1997].
101 For some literature on yield curve spread strategies, the yield curve dynamics and related
topics, see, e.g., [Bernadell, Coche and Nyholm, 2005], [Boyd and Mercer, 2010], [Chua, Koh
and Ramaswamy, 2006], [Diebold and Li, 2002], [Diebold, Rudebusch and Aruoba, 2006], [Dolan,
1999], [Evans and Marshall, 2007], [F¨ uss and Nikitina, 2011], [Jones, 1991], [Kalev and Inder,
2006], [Krishnamurthy, 2002], [Shiller and Modigliani, 1979].
102 For some literature on CDS basis arbitrage and related topics, see, e.g., [Bai and Collin-
Dufresne, 2013], [Choudhry, 2004], [Choudhry, 2006], [Choudhry, 2007], [De Wit, 2006], [Fontana,
2010], [Fontana and Scheicher, 2016], [Kim, Li and Zhang, 2016], [Kim, Li and Zhang, 2017],
[Nashikkar, Mahanti, 2011], [Rajan, McDermott and Roy, 2007], [Wang, 2014], [Zhu, 2006].
75
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 77

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Negative basis indicates that the bond spread is too high relative to the CDS spread,
i.e., the bond is relatively cheap. The CDS arbitrage trade then amounts to buying
the bond and insuring it with the CDS 103 thereby generating a risk-free proﬁt. 104
5.15 Strategy: Swap-spread arbitrage
This dollar-neutral strategy consists of a long (short) position in an interest rate
swap (see Subsection 5.1.4) and a short (long) position in a Treasury bond (with the
constant yield YTreasury ) with the same maturity as the swap. A long (short) swap
involves receiving (making) ﬁxed raterswap coupon payments in exchange for making
(receiving) variable rate coupon payments at LIBOR (the London Interbank Oﬀer
Rate) L(t). The short (long) position in the Treasury bond generates (is ﬁnanced at)
the “repo rate” (the discount rate at which the central bank repurchases government
securities from commercial banks) r(t) in a margin account. The per-dollar-invested
rate C(t) at which this strategy generates P&L is given by
C(t) =±[C1− C2(t)] (418)
C1 = rswap− YTreasury (419)
C2(t) = L(t)− r(t) (420)
where the plus (minus) sign corresponds to the long (short) swap strategy. The long
(short) swap strategy is proﬁtable if LIBOR falls (rises). So, this is a LIBOR bet. 105
6 Indexes
6.1 Generalities
An index is a diversiﬁed portfolio of assets combined with some weights. The under-
lying assets are often stocks, e.g., in indexes such as DJIA, S&P 500, Russell 3000,
etc. DJIA weights are based on price, while S&P 500 and Russell 3000 weights are
based on market capitalization. Investment vehicles such as index futures, index-
based ETFs, etc., allow gaining exposure to a broad index with a single trade. 106
103 Note that the CDS is equivalent to a synthetic short bond position.
104 In the case of positive basis, theoretically one would enter into the opposite trade, i.e., selling
the bond and selling the CDS. However, in practice this would usually imply that the trader already
owns the bond and the CDS, i.e., this would amount to unwinding an existing position.
105 For some literature on swap spreads and related topics, see, e.g., [Asgharian and Karlsson,
2008], [Aussenegg, G¨ otz and Jelic, 2014], [Chen and Selender, 1994], [Collin-Dufresne and Solnik,
2001], [Duarte, Longstaﬀ and Yu, 2006], [Dubil, 2011], [Duﬃe, 1996], [Duﬃe and Singleton, 1997b],
[Feldh¨ utter and Lando, 2008], [Fisher, 2002], [Jermann, 2016], [Jordan and Jordan, 1997], [Kambhu,
2006], [Keane, 1996], [Klingler and Sundaresan, 2016], [Kobor, Shi and Zelenko, 2005], [Lang,
Litzenberger and Liu, 1998], [Liu, Longstaﬀ and Mandell, 2006)], [Minton, 1997].
106 For some literature on indexes, see, e.g., [Antoniou and Holmes, 1995], [Beneish and Whaley,
1996], [Bologna and Cavallo, 2002], [Bos, 2000], [Chang, Cheng and Pinegar, 1999], [Chiang and
76
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 78

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
6.2 Strategy: Cash-and-carry arbitrage
This strategy (a.k.a. “index arbitrage”) aims to exploit price ineﬃciencies between
the index spot 107 price and index futures price. 108 Theoretically, the price of the
index futures must equal the spot price accounting for the cost of carry during the
life of the futures contract:
F∗(t, T) = [S(t)− D(t, T)] exp (r (T− t)) (421)
Here: F∗(t, T) is the theoretical (“fair”) price, at time t, of the futures contract
with the delivery time T ; S(t) is the spot value at time t; D(t, T) is the sum of
(discounted values of) the dividends paid by the underlying stocks between the time
t and delivery; and r is the risk-free rate, which for the sake of simplicity is assumed
to be constant from t to delivery.109 The basis is deﬁned as
B(t, T) = F (t, T)− F∗(t, T)
S(t) (422)
where F (t, T) is the current price of the futures contract with the delivery time T .
If B(t, T)̸= 0, more precisely, if|B(t, T)| exceeds the pertinent transaction costs of
executing the arbitrage trade, then there is an arbitrage opportunity. If the basis is
positive (negative), the futures price is rich (cheap) compared with the spot price,
so the arbitrage trade amounts to selling (buying) the futures and buying (selling)
the cash (i.e., the index basket). 110 The position is closed when the basis goes to
zero, i.e., the futures price converges to its fair value. Such arbitrage opportunities
are short-lived and with the advent of high frequency trading require extremely fast
execution. In many cases, the slippage can be prohibitive to execute the trade. 111
6.3 Strategy: Dispersion trading in equity indexes
This strategy takes long positions on volatilities of the index constituents and a
short position on index volatility. It is rooted in an empirical observation that, for
Wang, 2002], [Edwards, 1988], [Frino et al , 2004], [Graham and Pirie, 1994], [Hautcoeur, 2006],
[Illueca and Lafuente, 2003], [Kenett et al , 2013], [Lamoureux and Wansley, 1987], [Larsen and
Resnick, 1998], [Lo, 2016], [Schwartz and Laatsch, 1991], [Spyrou, 2005], [Yo, 2001].
107 “Spot” refers to the current value of the index based on the current prices of its constituents.
“Cash” refers to the underlying index portfolio. This is common trader lingo.
108 See, e.g., [Brenner, Subrahmanyam and Uno, 1989], [B¨ uhler and Kempf, 1995], [Butterworth
and Holmes, 2010], [Chan and Chung, 1993], [Cornell and French, 1983], [Dwyer, Locke and Yu,
1996], [Fassas, 2011], [Puttonen, 1993], [Richie, Daigler and Gleason, 2008], [Yadav and Pope,
1990], [Yadav and Pope, 1994].
109 Eq. (421) further ignores some other pertinent aspects such as taxes, asymmetry of interest
rates (for long and short holdings), transaction costs, etc.
110 Selling the futures poses no issues. However, selling the cash can be problematic with short-
selling issues such as hard-to-borrow securities, etc. Continuously maintaining a sizable dollar-
neutral book which is long cash and short futures can help circumvent such issues.
111 In some cases incomplete baskets approximating the index can be executed to reduce the
transaction costs, e.g., in market cap weighted indexes, by omitting lower cap (and thus less
liquid) stocks. However, such mishedges also increase the risk of losing money on the trade.
77
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 79

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
the most part,112 the implied volatility˜σI from index options is sizably higher than
the theoretical index volatility σI given by
σ2
I =
N∑
i,j=1
wiwjσiσjρij (423)
where wi are the weights of the stocks in the index, σi are their implied volatilities
from single-stock options, and ρij is the sample correlation matrix ( ρii = 1) 113
computed based on a time series of historical returns. 114 Put diﬀerently, the index
options are priced higher than the price corresponding to the aforesaid theoretical
volatility. So, a basic strategy can be structured as follows. For each stock in the
index we have a long position in ni (near-ATM) single-stock option straddles (whose
payoﬀs are based on the stock prices Pi), and we have a short position in a (near-
ATM) option straddle for the index (whose payoﬀ is based on the index level PI –
see below), where
ni = SiPI
∑N
i=1 SiPi
(424)
Here: Si is shares outstanding for stock i (we are assuming the index is market
cap weighted); and PI is the index level. With this deﬁnition of ni, we have PI =∑N
i=1 niPi, so the index option straddle payoﬀ matches the individual single-stock
option straddle payoﬀs as closely as possible. 115 All options have approximately 1
month until the expiration, and all positions remain open until the expiration. 116
6.3.1 Strategy: Dispersion trading – subset portfolio
For some indexes, some component stocks may not have single-stock options. Often
these would be less liquid, lower market cap stocks. They would have to be excluded
112 But not always – see below. For some literature on index vs. constituent volatilities and
dispersion and correlation trading, see, e.g., [Carrasco, 2007], [Deng, 2008], [Lozovaia and Hizhni-
akova, 2005], [Marshall, 2008], [Marshall, 2009], [Maze, 2012], [Meissner, 2016], [Nelken, 2006].
113 Note that the pair-wise correlations ρij, i̸= j, typically are unstable out-of-sample, which
can introduce a sizable error into this computation.
114 For some pertinent literature, see, e.g., [Bakshi and Kapadia, 2003a], [Bakshi and Kapadia,
2003b], [Bakshi, Kapadia and Madan, 2003], [Bollen and Whaley, 2004], [Branger and Schlag, 2004],
[Coval and Shumway, 2001], [Dennis and Mayhew, 2002], [Dennis, Mayhew and Stivers, 2006],
[Driessen, Maenhout and Vilkov, 2009], [Gˆ arleanu, Pedersen and Poteshman, 2009], [Lakonishok
et al , 2007].
115 If ATM options are not available for a given stock, OTM options (close to ATM) can be used.
116 This strategy can be argued to be a volatility strategy. However, it can also be argued
to be correlation trading as the volatility of the portfolio depends on the correlations between
its components (see Eq. (423)). Thus, when the implied index volatility ˜σI is higher than the
theoretical valueσI, this can be (arguably) interpreted as the implied average pair-wise correlation
being higher than the average pair-wise correlation based on ρij. In this regard, at times the index
implied volatility can be lower than its theoretical value, so the dispersion strategy that is short
index volatility would lose money and the reverse trade might be in order. See, e.g., [Deng, 2008].
78
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 80

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
from the bought portfolio. Reducing the number of bought underlying single-stock
options is also desirable to reduce transaction costs. Furthermore, the sample cor-
relation matrix ρij is singular for a typical lookback period (e.g., daily close-to-close
returns, going back 1 year, which is about 252 trading days) as the number of assets
is large (500 for S&P 500 and even larger for other indexes). As mentioned above,
the pair-wise correlations are unstable out-of-sample, which increases errors in the
theoretical value σI computed via Eq. (423). This can be mitigated as follows. 117
The singular and unstable correlation matrix can be made nonsingular and more
stable by replacing it with a statistical risk model [Kakushadze and Yu, 2017a]. Let
V (A)
i be the principal components of ρij with the eigenvalues λ(A) in the decreasing
order, λ(1) > λ (2) > λ (r), where r is the rank of ρij (if r < N , the other eigenvalues
are null: λ(A) = 0, A > r ). The statistical risk model correlation matrix is given by
ψij = ξ2
i δij +
K∑
A=1
λ(A) V (A)
i V (A)
j (425)
ξ2
i = 1−
K∑
A=1
λ(A)
[
V (A)
i
]2
(426)
where K < r is the number of risk factors based on the ﬁrst K principal components
that are chosen to explain systematic risk, and ξi is the speciﬁc (a.k.a. idiosyncratic)
risk. The simplest way to ﬁx K is via eRank (eﬀective rank) [Roy and Vetterli,
2007] – see [Kakushadze and Yu, 2017a] for details and complete source code for
constructing ψij and ﬁxing K. So, now we can use ψij (instead of ρij) to compute
the theoretical volatility σI:
σ2
I =
N∑
i,j=1
wiwjσiσjψij =
N∑
i=1
w2
i σ2
i ξ2
i +
K∑
A=1
[ N∑
i=1
λ(A)V (A)
i wiσi
] 2
(427)
The ﬁrst term on the r.h.s. of Eq. (427) is due to the speciﬁc risk. The long portfolio
then contains only the straddles corresponding to the ﬁrst N∗ single-stock options
with the lowest N∗ values of w2
i σ2
i ξ2
i . E.g., for S&P 500 we can take N∗ = 100.
6.4 Strategy: Intraday arbitrage between index ETFs
This strategy amounts to exploiting short-term mispricings between two ETFs (call
them ETF1 and ETF2) on the same underlying index. 118 It can be summarized as
117 The variation of the dispersion trading strategy we discuss here is similar but not identical
to the PCA (principal component analysis) based strategy discussed in [Deng, 2008], [Larsson and
Flohr, 2011], [Su, 2006]. The statistical risk model construction (see below) is more streamlined.
118 E.g., S&P 500 ETFs, SPDR Trust (ticker SPY) and iShares (ticker IVV). See, e.g., [Marshall,
Nguyen and Visaltanachoti]. For some additional literature on ETF arbitrage and related topics,
see, e.g., [Abreu and Brunnermeier, 2002], [Ackert and Tian, 2000], [Ben-David, Franzoni and
Moussawi, 2012], [Brown, Davies and Ringgenberg, 2018], [Cherry, 2004], [Dolvin, 2009], [Garvey
and Wu, 2009], [Hendershott and Moulton, 2011], [Johnson, 2008], [Maluf and Albuquerque, 2013].
79
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 81

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
follows:
Rule =



Buy ETF2, short ETF1 if PBid
1 ≥ PAsk
2 × κ
Liquidate position if PBid
2 ≥ PAsk
1
Buy ETF1, short ETF2 if PBid
2 ≥ PAsk
1 × κ
Liquidate position if PBid
1 ≥ PAsk
2
(428)
Here: κ is a predeﬁned threshold, which is close to 1, e.g., κ = 1 .002 (see, e.g.,
[Marshall, Nguyen and Visaltanachoti]); PBid
1 and PBid
2 are the bid prices for ETF1
and ETF2, and PAsk
1 and PAsk
2 are the ask prices. Marketable “ﬁll or kill” limit
orders can be used to execute the trades. Such arbitrage opportunities are ephemeral
and require a fast order execution system or else slippage will eat away the proﬁts.
6.5 Strategy: Index volatility targeting with risk-free asset
A volatility targeting strategy aims to maintain a constant volatility level, which can
be achieved by a periodic (weekly, monthly, etc.) rebalancing between a risky asset
– in this case an index – and a riskless asset (e.g., U.S. Treasury bills). 119 If σ is
the volatility of the risky asset 120 and the volatility target is σ∗, then the allocation
weight for the risky asset is given by 121 w = σ∗/σ, and the allocation weight for
the risk-free asset is 1 − w. To avoid overtrading and reduce transaction costs,
rebalancing (instead of periodically) can be done based, e.g., on a preset threshold
κ, say, only if the percentage change |∆w|/w since the last rebalancing exceeds κ.
7 Volatility
7.1 Generalities
Some option trading strategies discussed in Section 2 are volatility strategies, in the
sense that they make bets on high or low future volatility. 122 There are various
ways to make volatility bets, and volatility can be viewed as an asset class of its
own. Historical volatility is based on a time series of past returns. In contrast,
implied volatility extracted from options is considered a forward-looking measure
of volatility.123 VIX (CBOE Volatility Index, a.k.a. the “uncertainty index” or the
119 For some pertinent literature, see, e.g., [Albeverio, Steblovskaya and Wallbaum, 2013], [An-
derson, Bianchi and Goldberg, 2014], [Cirelli et al, 2017], [Cooper, 2010], [Giese, 2012], [Khuzwayo
and Mar´ e, 2014], [Kim and Enke, 2016], [Kirby and Ostdiek, 2012], [Papageorgiou, Reeves and
Sherris, 2017], [Perchet, de Carvalho and Moulin, 2014], [Torricelli, 2018], [Zakamulin, 2014b].
120 Usually, this is implied volatility as opposed to historical volatility as the former is considered
to be forward-looking. Alternatively, it can be based on various volatility-forecasting techniques.
121 If there is a preset maximum leverage L, then w is capped at L.
122 E.g., long (short) straddles bet on increasing (decreasing) volatility.
123 See, e.g., [Abken and Nandi, 1996], [An´ e and Labidi, 2001], [Canina and Figlewski, 1993],
[Christensen and Prabhala, 1998], [Derman and Kani, 1994], [Dumas, Fleming and Whaley, 1998],
80
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 82

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
“fear gauge index”) 124 and other volatility indexes 125 and derivatives (options and
futures) on volatility indexes such as VIX provide avenues for volatility trading.
7.2 Strategy: VIX futures basis trading
This is essentially a mean-reversion strategy. It is rooted in empirical observations
(see, e.g., [Mixon, 2007], [Nossman and Wilhelmsson, 2009], [Simon and Campasano,
2014])126 that the VIX futures basis (deﬁned below) has essentially no forecasting
power for subsequent VIX changes but has substantial forecasting power for sub-
sequent VIX futures price changes. The VIX futures basis BVIX (for our purposes
here) is deﬁned as
BVIX = PUX 1− PVIX (429)
D = BVIX
T (430)
Here: PUX 1 is the price of the ﬁrst-month contract VIX futures; 127 PVIX is the
VIX price; D is the daily roll value; and T is the number of business days until
the settlement (which is assumed to be at least 10). Empirically, the futures prices
tend to fall for positive basis and rise for negative basis (mean-reversion). So, the
strategy amounts to shorting VIX futures when the VIX futures curve is upward-
sloping (a.k.a. “contango”, so the basis is positive), and buying VIX futures when
the VIX futures curve is downward-sloping (a.k.a. “backwardation”, so the basis is
negative). Here is a simple trading rule (see, e.g., [Simon and Campasano, 2014]):
Rule =



Open long UX1 position if D <−0.10
Close long UX1 position if D >−0.05
Open short UX1 position if D > 0.10
Close short UX1 position if D < 0.05
(431)
A short (long) UX1 position is exposed to a risk of a sudden increase (decrease) in
the volatility, which typically occurs during equity market sell-oﬀs (rallies), so this
risk can be hedged by, e.g., shorting (buying) mini-S&P 500 futures. 128 The hedge
[Dupire, 1994], [Glasserman and Wu, 2010], [He, Hsu and Rue, 2015], [Lamoureux and Lastrapes,
1993], [Mayhew, 1995], [Skiadopoulos, Hodges and Clewlow, 1999].
124 See, e.g., [ ¨Aij¨ o, 2008], [Corrado and Miller, 2005], [Fleming, Ostdiek and Whaley, 1995],
[Maghrebi, Kim and Nishina, 2007], [Shaikh and Padhi, 2015], [Siriopoulos and Fassas, 2009],
[Skiadopoulos, 2004], [Whaley, 2000], [Whaley, 2009].
125 E.g., RVX (CBOE Russell 2000 Volatility Index), VXEEM (CBOE Emerging Markets ETF
Volatility Index), TYVIX (CBOE/CBOT 10-year U.S. Treasury Note Volatility Index), GVZ
(CBOE Gold ETF Volatility Index), EUVIX (CBOE/CME FX Euro Volatility Index), VXGOG
(CBOE Equity VIX on Google), VVIX (CBOE VIX of VIX Index), etc.
126 For some additional literature on VIX futures basis and related topics, see, e.g., [Buetow
and Henderson, 2016], [Donninger, 2014], [Fu, Sandri and Shackleton, 2016], [Lee, Liao and Tung,
2017], [Zhang, Shu and Brenner, 2010], [Zhang and Zhu, 2006].
127 UX1 has approximately 1 month to maturity, UX2 has approximately 2 months, etc.
128 Typically, VIX and the equity markets are anti-correlated.
81
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 83

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ratio can be estimated, e.g., based on a historical serial regression of the VIX futures
price changes over the front-month mini-S&P 500 futures contract returns. 129
7.3 Strategy: Volatility carry with two ETNs
VXX is an exchange-traded note (ETN) that tracks VIX via a portfolio of short-
maturity (months 1 and 2) VIX futures contracts. To maintain a constant maturity,
at the close of each day, a portion of the shorter-maturity futures is sold and replaced
with the longer-maturity futures bought with the proceeds. Since the VIX futures
curve is in contango most of the time, the longer-maturity futures are priced higher
than the shorter-maturity futures, so this rebalancing amounts to a decay in the
value of VXX over time, which is known as the roll (or contango) loss. Further, as
time passes, the futures converge to the spot (VIX), so VXX loses value so long as
the VIX futures curve is in contango. VXZ is yet another ETN that tracks VIX via
a portfolio of medium-maturity (months 4 through 7) VIX futures. VXZ also suﬀers
roll loss, but to a lesser degree than VXX as the slope of the VIX futures curve in
contango decreases with maturity. 130 The basic strategy then is to short VXX and
buy VXZ with the hedge ratio that can be determined via a serial regression. 131
This strategy is not without risks, however. There can be short-term spikes in VXX
(the corresponding spikes in VXZ usually are sizably smaller), which can lead to
substantial short-term P&L drawdowns, even if the strategy is overall proﬁtable.
7.3.1 Strategy: Hedging short VXX with VIX futures
Instead of using a long position in VXZ to hedge the short position in VXX, one
can directly use a basket of, e.g., medium-maturity VIX futures. 132 The N VIX
futures have some weights wi. These weights can be ﬁxed in a variety of ways,
e.g., by minimizing the tracking error, i.e., by running a serial regression (with the
intercept) of VXX returns over the N futures returns. Then we have:
wi = σX
N∑
j=1
C−1
ij σjρj (432)
129 See, e.g., [Simon and Campasano, 2014] for details.
130 For some literature on volatility ETNs and related topics, see, e.g., [Alexander and Korovilas,
2012], [Avellaneda and Papanicolaou, 2018], [DeLisle, Doran and Krieger, 2014], [Deng, McCann
and Wang, 2012], [Eraker and Wu, 2014], [Gehricke and Zhang, 2018], [Grasselli and Wagalath,
2018], [Hancock, 2013], [Husson and McCann, 2011], [Liu and Dash, 2012], [Liu, Pantelous and
von Mettenheim, 2018], [Moran and Dash, 2007].
131 We have h = β = ρσX/σZ, where: h (known as the optimal hedge ratio) is the number
of VXZ to buy for each VXX shorted; β is the coeﬃcient (for the VXZ returns) of the serial
regression (with the intercept) of the VXX returns over the VXZ returns; σX and σZ are the
historical volatilities of VXX and VXZ, respectively; and ρ is the pair-wise historical correlation
between VXX and VXZ.
132 These can have maturities of, e.g., 4 through 7 months (thus mimicking the VXZ composition).
82
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 84

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Here: ρi is the pair-wise historical correlation between the futures labeled by i and
VXX; Cij is the N× N sample covariance matrix for the N futures (σ2
i = Cii is the
historical variance for the futures labeled by i); and σX is the historical volatility of
VXX. Some wi may turn out to be negative. This is not necessarily an issue, but
one may wish to impose the bounds wi≥ 0. Further, one may wish the strategy to
be dollar-neutral, which would amount to imposing the constraint
N∑
i=1
wi = 1 (433)
which the optimal hedge ratios (432) generally do not satisfy. Also, instead of
minimizing the tracking error, one may wish to minimize the variance of the entire
portfolio. And so on. The portfolio can be rebalanced monthly or more frequently.
7.4 Strategy: Volatility risk premium
Empirical evidence indicates that implied volatility tends to be higher than realized
volatility most of the time, which is known as the “volatility risk premium”. 133
Simply put, most of the time options are priced higher than the prices one would
expect based on realized volatility, so the idea is to sell volatility. E.g., the trader
can sell straddles based on S&P 500 options. As a possible proxy for volatility risk
premium, the trader can, e.g., use the diﬀerence between VIX at the beginning of
the current month and the realized volatility (in %, as VIX is quoted in %) of S&P
500 daily returns since the beginning of the current month. If the spread is positive,
the trader sells the straddle. If the volatility spikes (which usually happens if the
market sells of), the strategy will lose money. It is proﬁtable in sideways markets.134
7.4.1 Strategy: Volatility risk premium with Gamma hedging
The ATM straddles in the above strategy are Delta-neutral. 135 So, this is a “Vega
play”, i.e., the trader is shorting Vega. If the underlying (S&P 500) moves, the
short straddle is no longer Delta-neutral: if the underlying goes up (down), Delta
becomes negative (positive). So a variation of this strategy is to use Gamma hedging
to keep the strategy close to Delta-neutral, which is achieved by buying (selling) the
underlying if it moves up (down). Then this becomes a “Theta play”, i.e., the
133 For some pertinent literature, see, e.g., [Bakshi and Kapadia, 2003a], [Bollerslev, Gibson and
Zhou, 2011], [Carr and Wu, 2009], [Carr and Wu, 2016], [Christensen and Prabhala, 1998], [Eraker,
2009], [Ge, 2016], [Miao, Wei and Zhou 2012], [Prokopczuk and Simen, 2014], [Saretto and Goyal,
2009], [Todorov, 2010].
134 Also, index options are better suited for this strategy than single-stock options as index
options typically have higher volatility risk premia (see Subsection 6.3).
135 Some of the Greeks for options are: Θ = ∂V/∂t (Theta), ∆ = ∂V/∂S (Delta), Γ = ∂2V/∂S 2
(Gamma), ν =∂V/∂σ (Vega). Here: V is the value of the option; t is time; S is the price of the
underlying; σ is the implied volatility.
83
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 85

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
strategy now aims to capitalize on the Theta-decay of the value of the sold options.
So, the price of this is the cost of the Gamma hedging, which reduces the P&L. As
the underlying moves more and more away from the strike of the sold put and call
options, the Gamma hedge becomes more and more expensive and eventually will
exceed the collected option premia, at which point the strategy starts losing money.
7.5 Strategy: Volatility skew – long risk reversal
OTM put options with the underlying at S0 = K + κ tend to be priced higher than
OTM call options with the underlying at S0 = K− κ (here K is the strike price,
and κ > 0 is the distance from the strike). I.e., with all else being equal, the implied
volatility for puts is higher than for calls. 136 The long risk reversal strategy (see
Subsection 2.12), where the trader buys an OTM call option and sells an OTM put
option, captures this skew. However, this is a directional strategy – it loses money
if the price of the underlying drops below Kput− C, where Kput is the strike price
of the put, and C > 0 is the premium of the put minus the premium of the call.
7.6 Strategy: Volatility trading with variance swaps
One issue with trading volatility using options is the need to (almost continuously)
Delta-hedge the position to avoid directional exposure, 137 which practically can be
both cumbersome and costly. To avoid the need for Delta-hedging, one can make
volatility bets using variance swaps. A variance swap is a derivative contract whose
payoﬀ P (T ) at maturity T is proportional to the diﬀerence between the realized
variance v(T ) of the underlying and the preset variance strike K:
P (T ) = N× (v(T )− K) (434)
v(T ) = F
T
T∑
t=1
R2(t) (435)
R(t) = ln
[ S(t)
S(t− 1)
]
(436)
Here: t = 0, 1, . . . , T labels sample points (e.g., trading days); S(t) is the price of
the underlying at time t; R(t) is the log-return from t−1 to t; F is the annualization
factor (thus, if t labels trading days, thenF = 252); and N is the “variance notional”,
which is preset. Note that in Eq. (435) the mean of R(t) over the period t = 1 to
t = T is not subtracted, hence T in the denominator.138 Long (short) variance swap
136 For some pertinent literature, see, e.g., [Bondarenko, 2014], [Chambers et al , 2014], [Corrado
and Su, 1997], [Damghani and Kos, 2013], [DeMiguel et al , 2013], [Doran and Krieger, 2010],
[Doran, Peterson and Tarrant, 2007], [Fengler, Herwartz and Werner, 2012], [Flint and Mar´ e,
2017], [Jackwerth, 2000], [Kozhan, Neuberger and Schneider, 2013], [Liu and van der Heijden,
2016], [Mixon, 2011], [Zhang and Xiang, 2008].
137 See Subsection 7.4.1 for a Delta-hedging strategy (a.k.a. “Gamma scalping”).
138 If the mean is subtracted, then the denominator would be T− 1 instead.
84
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 86

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
is a bet that the future realized volatility will be higher (lower) than the current
implied volatility. Long (short) variance swaps can therefore be used instead of,
e.g., long (short) straddles to go long (short) volatility. For instance, the dispersion
strategy of Subsection 6.3 can be executed by selling a variance swap on an index and
buying variance swaps on the index constituents (cf. selling and buying straddles).139
8 Foreign Exchange (FX)
8.1 Strategy: Moving averages with HP ﬁlter
In Subsection 3.12 we discussed a trading strategy for stocks wherein the trading
signal is based on 2 intersecting (shorter and longer) moving averages. A similar
approach can be applied to FX as well. However, FX spot rate time series tend
to be rather noisy, which can lead to false signals based on moving averages. To
mitigate this, before computing the moving averages, the higher-frequency noise can
ﬁrst be ﬁltered out, e.g., using the so-called Hodrick-Prescott (HP) ﬁlter. 140 Then,
the remaining lower-frequency trend component (as opposed to the raw spot rate)
can be used to compute the moving averages and generate the trading signal (see,
e.g., [Harris and Yilmaz, 2009]). The HP ﬁlter is given by:
S(t) = S∗(t) + ν(t) (437)
g =
T∑
t=1
[S(t)− S∗(t)]2 + λ
T−1∑
t=2
[S∗(t + 1)− 2S∗(t) + S∗(t− 1)]2 (438)
g→ min (439)
Here: the objective function g is minimized w.r.t. the set of T values of S∗(t), t =
1, . . . , T; S(t) is the FX spot rate at time t; S∗(t) is the lower-frequency (“regular”)
component; ν(t) is the higher-frequency (“irregular”) component, which is treated as
noise; the ﬁrst term in Eq. (438) minimizes the noise, while the second term (based
on the discretized second derivative of S∗(t)) penalizes the variation in S∗(t); and λ
is the smoothing parameter. There is no “fundamental” method to ﬁx λ. Sometimes
(but not always) it is set to λ = 100×n2, where n is the data frequency measured on
139 For some literature on variance swaps, see, e.g., [A¨ ıt-Sahalia, Karaman and Mancini, 2015],
[Bernard, Cui and Mcleish, 2014], [Broadie and Jain, 2008], [Bossu, 2006], [Carr and Lee, 2007],
[Carr and Lee, 2009], [Carr, Lee and Wu, 2012], [Demeterﬁ et al , 1999], [Elliott, Siu and Chan,
2007], [Filipovi´ c, Gourier and Mancini, 2016], [Hafner and Wallmeier, 2007], [H¨ ardle and Silyakova,
2010], [Jarrow et al , 2013], [Konstantinidi and Skiadopoulos, 2016], [Leontsinis and Alexander,
2016], [Liverance, 2010], [Martin, 2011], [Rujivan and Zhu, 2012], [Schoutens, 2005], [Wystup and
Zhou, 2014], [Zhang, 2014], [Zheng and Kwok, 2014].
140 A.k.a. the Whittaker-Henderson method in actuarial sciences. For some pertinent literature,
see, e.g., [Baxter and King, 1999], [Bruder et al , 2013], [Dao, 2014], [Ehlgen, 1998], [Harris and
Yilmaz, 2009], [Harvey and Trimbur, 2008], [Henderson, 1924], [Henderson, 1925], [Henderson,
1938], [Hodrick and Prescott, 1997], [Joseph, 1952], [Lahmiri, 2014], [Mcelroy, 2008], [Weinert,
2007], [Whittaker, 1923], [Whittaker, 1924].
85
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 87

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
an annual basis (see, e.g., [Baxter and King, 1999] for more detail). So, for monthly
data, which is what is usually used in this context, n = 12. The estimation period
usually spans several years (of monthly data). Once S∗(t) is determined, two moving
averages MA(T1) and MA( T2), T1 < T 2, are calculated based on S∗(t). Then, as
before, MA(T1) > MA(T2) is a buy signal, and MA( T1) < MA(T2) is a sell signal.
8.2 Strategy: Carry trade
Pursuant to “Uncovered Interest Rate Parity” (UIRP), excess interest earned in
one country compared with another country due to a diﬀerential between risk-free
interest rates in these countries would be precisely oﬀset by depreciation in the FX
rate between their currencies:
(1 + rd) = Et(S(t + T ))
S(t) (1 + rf) (440)
Here: rd is the domestic interest rate; rf is the foreign interest rate; both rd and rf
are assumed to be constant over the compounding period T ; S(t) is the spot FX rate
at time t, which is the worth of 1 unit of the foreign currency in units of the domestic
currency; and Et(S(t + T )) is the future (at time t + T ) spot FX rate expected at
time t.141 UIRP does not always hold, giving rise to trading opportunities – which
are not risk-free arbitrage opportunities (see below). Thus, UIRP implies that high
interest rate currencies should depreciate w.r.t. low interest rate currencies, whereas
empirically on average the opposite tends to transpire, i.e., such currencies tend to
appreciate (somewhat). 142 So, the basic carry strategy amounts to writing (i.e.,
selling) forwards on currencies that are at a forward premium, i.e., the forward FX
rate F (t, T) exceeds the spot FX rate S(t), and buying forwards on currencies that
are at a forward discount, i.e., the forward FX rate F (t, T) is lower than the spot
FX rate S(t).143 The forward FX rate is given by 144
F (t, T) = S(t) 1 + rd
1 + rf
(441)
141 Thus, 1 USD invested at timet in a risk-free asset in the U.S. would be forth (1 +rd) USD at
timet +T . Alternatively, 1 USD would buy 1/S(t) JPY at time t, which sum could be invested in
a risk-free asset in Japan at time t, which would be worth (1/S(t))× (1 +rf) JPY at time t +T ,
which in turn could be expected to be exchanged for ( Et(S(t +T ))/S(t))× (1 +rf) USD at time
t +T . Requiring that the U.S. and Japan investments yield the same return gives Eq. (440).
142 This is known as “forward premium/discount anomaly/puzzle” or “Fama puzzle”. For some
literature on UIRP and related topics, see, e.g., [Anker, 1999], [Ayuso and Restoy, 1996], [Bac-
chetta and van Wincoop, 2006], [Bacchetta and van Wincoop, 2010], [Baillie and Osterberg,
2000], [Bekaert, Wei and Xing, 2007], [Beyaert, Garc´ ıa-Solanes, and P´ erez-Castej´ on, 2007], [Bil-
son, 1981], [Chaboud and Wright, 2005], [Engel, 1996], [Fama, 1984], [Frachot, 1996], [Froot and
Thaler, 1990], [Hansen and Hodrick, 1980], [Harvey, 2015], [Hodrick, 1987], [Ilut, 2012], [Lewis,
1995], [Lustig and Verdelhan, 2007], [Mark and Wu, 2001], [Roll and Yan, 2008].
143 Ignoring transaction costs, this is equivalent to borrowing (lending) low (high) interest rate
currencies without hedging the FX rate risk.
144 This is known as “Covered Interest Rate Parity” (CIRP). Note that, assuming Eq. (441)
holds (see below), when UIRP (i.e., Eq. (440)) does not hold, F (t,T )̸=Et(S(t +T )).
86
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 88

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
As mentioned above, the carry strategy 145 is not without risks: this trade can gen-
erate losses if the borrowed (lent) currency suddenly appreciates (depreciates) w.r.t.
its counterpart, i.e., it is exposed to the FX rate risk. On the other hand, if we borrow
the low interest rate currency with the maturity date T , invest the funds in the high
interest rate currency, and hedge this position with a forward contract to exchange
the high interest rate currency for the low interest rate currency at maturity T (so
we can cover the loan), ignoring the transaction costs (and other subtleties such as
taxes, etc.), this is a risk-free position and any gains therefrom would amount to
risk-free arbitrage. Hence Eq. (441), which is a no-risk-free-arbitrage condition. 146
8.2.1 Strategy: High-minus-low carry
The carry strategy discussed above can be applied to individual foreign currencies.
It can also be applied cross-sectionally, to multiple foreign currencies. Let s(t) =
ln(S(t)) (log spot FX rate) and f(t, T) = ln( F (t, T)) (log forward FX rate). The
forward discount D(t, T) is deﬁned as
D(t, T) = s(t)− f(t, T) (442)
Pursuant to CIRP, Eq. (441), we have
D(t, T) = ln
(1 + rf
1 + rd
)
≈ rf− rd (443)
For a positive forward discount, we buy a forward (i.e., borrow the domestic cur-
rency and invest in the foreign currency), and the higher the forward discount,
the more proﬁtable the strategy. For a negative forward discount, we sell a for-
ward (i.e., borrow the foreign currency and invest in the domestic currency), and
the lower the forward discount, the more proﬁtable the strategy. So, we can con-
struct a cross-sectional trade (including a zero-cost, i.e., dollar-neutral trade – see,
e.g., [Lustig, Roussanov and Verdelhan, 2011]) by buying forwards on currencies in
some top quantile 147 by forward discount and selling forwards on currencies in the
corresponding bottom quantile. The forwards can, e.g., be one-month forwards.
145 For some literature on currency carry trades and related topics, see, e.g., [Bakshi and Panay-
otov, 2013], [Brunnermeier, Nagel and Pedersen, 2008], [Burnside et al , 2011], [Burnside, Eichen-
baum and Rebelo, 2007], [Burnside, Eichenbaum and Rebelo, 2008], [Clarida, Davis and Pedersen,
2009], [Deardorﬀ, 1979], [Doskov and Swinkels, 2015], [Hau, 2014], [Jurek, 2014], [Lustig, Roussanov
and Verdelhan, 2011], [Lustig, Roussanov and Verdelhan, 2014], [Olmo and Pilbeam, 2009], [Ready,
Roussanov and Ward, 2017], [Rhee and Chang, 1992].
146 Nonetheless, deviations from CIRP (i.e., Eq. (441)) do occur, which gives rise to covered
interest arbitrage. See, e.g., [Akram, Rime and Sarno, 2008], [Avdjiev et al , 2016], [Baba and
Packer, 2009], [Boulos and Swanson, 1994], [Clinton, 1988], [Coﬀey, Hrung and Sarkar, 2009],
[Cosandier and Lang, 1981], [Du, Tepper and Verdelhan, 2018], [Duﬃe, 2017], [Frenkel and Levich,
1975], [Frenkel and Levich, 1981], [Liao, 2016], [Mancini-Griﬀoli and Ranaldo, 2011], [Popper,
1993], [Rime, Schrimpf and Syrstad, 2017].
147 Unlike stocks, that number in thousands, there is a limited number of currencies to play with.
Therefore, one does not necessarily have the luxury of taking top and bottom deciles by forward
discount. So, this quantile can be a half, a third, etc., depending on the number of currencies.
87
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 89

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
8.3 Strategy: Dollar carry trade
This strategy is based on the average cross-sectional forward discount D(t, T) (see,
e.g., [Lustig, Roussanov and Verdelhan, 2014]) for a basket of N foreign currencies:
D(t, T) = 1
N
N∑
i=1
Di(t, T) (444)
where Di(t, T) is the forward discount for the currency labeled byi = 1, . . . , N. This
strategy then goes long (short), with equal weights, all N foreign currency forwards
when D(t, T) is positive (negative), where T can be 1 , 2, 3, 6, 12 months. Empirical
evidence suggests that this strategy relates to the state of the U.S. economy, to wit,
when the U.S. economy is weak, the average forward discount tends to be positive.148
8.4 Strategy: Momentum & carry combo
This is a combination of the momentum strategy (Subsection 8.1) 149 and the carry
strategy (Subsection 8.2), or their variations. There is a variety of ways these
strategies can be combined (including an equally weighted combo, or some ideas
discussed in, e.g., Subsection 3.6 and Subsection 4.6). A simple combination is based
on minimizing the variance of the combo strategy using the sample covariance matrix
of historical returns R1(ts) and R2(ts) of the two strategies (see, e.g., [Olszweski and
Zhou, 2013]). Let (here Var and Cor are serial variance and correlation, respectively)
σ2
1 = Var(R1(ts)) (445)
σ2
2 = Var(R2(ts)) (446)
ρ = Cor(R1(ts), R2(ts)) (447)
Then minimizing the historical variance of the combined returnR(ts) ﬁxes the strat-
egy weights w1 and w2:
R(ts) = w1 R1(ts) + w2 R2(ts) (448)
w1 + w2 = 1 (449)
Var(R(ts))→ min (450)
w1 = σ2
2− σ1σ2ρ
σ2
1 + σ2
2− 2σ1σ2ρ (451)
w2 = σ2
1− σ1σ2ρ
σ2
1 + σ2
2− 2σ1σ2ρ (452)
148 See, e.g., [Cooper and Priestley, 2008], [Joslin and Konchitchki, 2018], [Joslin, Priebsch and
Singleton, 2014], [Lustig, Roussanov and Verdelhan, 2014], [Stambaugh, 1988], [Tille, Stoﬀels and
Gorbachev, 2001].
149 For additional literature on FX momentum strategies and related topics, see, e.g., [Ac-
cominotti and Chambers, 2014], [Ahmerkamp and Grant, 2013], [Burnside, Eichenbaum and
Rebelo, 2011], [Chiang and Jiang, 1995], [Grobys, Heinonen and Kolari, 2016], [Menkhoﬀ et al ,
2012], [Okunev and White, 2003], [Serban, 2010].
88
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 90

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
8.5 Strategy: FX triangular arbitrage
This strategy is based on 3 currency pairs. 150 Let these currencies be A, B and C.
Then we have 2 chains: i) exchange A for B, exchange B for C, and exchange C for A;
and ii) exchange A for C, exchange C for B, and exchange B for A. We will focus on
the ﬁrst chain as the second one is obtained by swapping B for C. Each currency pair
has the bid and the ask; e.g., Bid(A→ B) and Ask(B→ A) for the A-B pair. So,
the rate at which A is exchanged into B is Bid(A→ B), while the rate at which B
is exchanged into A is 1 /Ask(B→ A). Therefore, Bid(B→ A) = 1/Ask(B→ A),
and Ask(A→ B) = 1/Bid(A→ B). In the chain i) above, the trader starts with A
and loops back to A with the overall exchange rate
R(A→ B→ C→ A) = Bid(A→ B)× Bid(B→ C)× 1
Ask(C→ A) (453)
If this quantity is greater than 1, then the trader makes a proﬁt. Such opportunities
are ephemeral, so fast market data and trade execution systems are critical here. 151
9 Commodities
9.1 Strategy: Roll yields
When commodity futures are in backwardation (contango), i.e., when the term struc-
ture of futures prices is downward (upward) sloping, long (short) futures positions
on average generate positive returns due to the roll yield. Roll yields come from re-
balancing futures positions: when the current long (short) futures contract is about
to expire, it is sold (covered) and another futures contract with longer expiration is
bought (sold). Let
φ = P1/P2 (454)
where P1 is the front-month futures price, and P2 is the second-month futures price.
The ratio φ is a measure of backwardation ( φ > 1) and contango ( φ < 1). A zero-
cost long-short portfolio can then be built based on φ, e.g., by buying commodity
futures with higher values of φ and selling futures with lower values thereof. 152
150 Albeit one can also consider more than 3 pairs, which is known as multi-currency arbitrage
(see, e.g., [Moosa, 2003a]).
151 For some literature on triangular arbitrage and related topics, see, e.g., [Aiba and Hatano,
2006], [Aiba et al , 2002], [Aiba et al , 2003], [Akram, Rime and Sarno, 2008], [Choi, 2011], [Cross
and Kozyakin, 2015], [Fenn et al , 2009], [Goldstein, 1964], [Gradojevic, Gen¸ cay and Erdemlioglu,
2017], [Ito et al , 2012], [Moosa, 2001], [Morisawa, 2009], [Mwangi and Duncan, 2012], [Osu, 2010].
152 For some pertinent literature, see, e.g., [Anson, 1998], [Arnott et al , 2014], [Erb and Harvey,
2006], [Fama and French, 1987], [Fama and French, 1988], [Feldman and Till, 2006], [Fuertes, Miﬀre
and Fernandez-Perez, 2015], [Gorton, Hayashi and Rouwenhorst, 2013], [Gorton and Rouwenhorst,
2006], [Greer, 2000], [Leung et al , 2016], [Ma, Mercer and Walker, 1992], [Mou, 2010], [Mouakhar
and Roberge, 2010], [Symeonidis et al , 2012], [Taylor, 2016], [Telser, 1958].
89
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 91

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
9.2 Strategy: Trading based on hedging pressure
This strategy is based on hedgers’ and speculators’ position data provided (weekly)
by the U.S. Commodity Futures Trading Commission (CFTC) in the Commitments
of Traders (COT) reports. For each commodity, the “hedging pressure” (HP), sep-
arately for hedgers and speculators, is calculated as the number of long contracts
divided by the total number of contracts (long plus short). So, HP is between 0
and 1. High (low) hedgers’ HP is indicative of contango (backwardation), while
high (low) speculators’ HP is indicative of backwardation (contango). A zero-cost
portfolio can be constructed, e.g., as follows. First, the cross-section of commodities
is divided into the upper half and the lower half by the speculators’ HP. Then, the
upper half commodity futures are bought if they are in the bottom quintile by the
hedgers’ HP, and the lower half commodity futures are sold if they are in the top
quintile by the hedger’s HP. Typical formation and holding periods are 6 months.153
9.3 Strategy: Portfolio diversiﬁcation with commodities
Commodity markets typically have a low correlation with equity markets, which can
be used to improve performance characteristics of equity portfolios by combining eq-
uity and commodity investments. There are diﬀerent ways to do this. A “passive
approach” would amount to buying commodities with a preset portion of the avail-
able funds, holding them, and rebalancing the portfolio with some periodicity (e.g.,
monthly or annually). An “active approach” would amount to a tactical asset allo-
cation approach via increasing/decreasing the exposure to commodities based on an
increase/decrease in the Fed discount rate (empirically, commodity returns tend to
be sizably correlated with the Fed monetary policy) or some other methodology. 154
9.4 Strategy: Value
This strategy is similar to the value strategy for stocks (see Subsection 3.3). Value
for commodities can be deﬁned as, e.g., the ratio (see, e.g., [Asness, Moskowitz and
153 For some literature on trading strategies based on such data and related topics, see, e.g., [Basu
and Miﬀre, 2013], [Bessembinder, 1992], [Carter, Rausser and Schmitz, 1983], [Cheng and Xiong,
2013], [de Roon, Nijman and Veld, 2000], [Dewally, Ederington and Fernando, 2013], [Fernandez-
Perez, Fuertes and Miﬀre, 2016], [Fishe, Janzen and Smith, 2014], [Fuertes, Miﬀre and Fernandez-
Perez, 2015], [Hirshleifer, 1990], [Lehecka, 2013], [Miﬀre, 2012], [Switzer and Jiang, 2010].
154 For some literature on diversiﬁcation strategies using commodities and related topics, see,
e.g., [Adams and Gl¨ uck, 2015], [Bernardi, Leippold and Lohre, 2018], [Bjornson and Carter, 1997],
[Blitz and Van Vliet, 2008], [Bodie, 1983], [Bodie and Rosansky, 1980], [Chan et al, 2011], [Chance,
1994], [Chong and Miﬀre, 2010], [Conover et al , 2010], [Creti, Jo¨ ets and Mignon, 2013], [Daumas,
2017], [Draper, Faﬀ and Hillier, 2006], [Edwards and Park, 1996], [Elton, Gruber and Rentzler,
1987], [Frankel, 2006], [Gorton and Rouwenhorst, 2006], [Greer, 1978], [Greer, 2007], [Hess, Huang
and Niessen, 2008], [Jensen, Johnson and Mercer, 2000], [Jensen, Johnson and Mercer, 2002],
[Kaplan and Lummer, 1998], [Lummer and Siegel, 1993], [Marshall, Cahan and Cahan, 2008],
[Miﬀre and Rallis, 2007], [Nguyen and Sercu, 2010], [Taylor, 2004], [Vrugt et al , 2007], [Wang and
Yu, 2004], [Weiser, 2003].
90
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 92

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Pedersen, 2013])
v = P5/P0 (455)
where P5 is the spot price 5 years ago, 155 and P0 is the current spot price. Then one
can build a zero-cost portfolio by, e.g., buying the commodities in the top tercile by
value, and selling those in the bottom tercile. The portfolio is rebalanced monthly.
9.5 Strategy: Skewness premium
This strategy is based on the empirically observed negative correlation between the
skewness of historical returns and future expected returns of the commodity futures.
The skewness Si is deﬁned as ( i = 1, . . . , N labels diﬀerent commodities):
Si = 1
σ3
i T
T∑
s=1
[
Ris− Ri
]3
(456)
Ri = 1
T
T∑
s=1
Ris (457)
σ2
i = 1
T− 1
T∑
s=1
[
Ris− Ri
]2
(458)
where Ris are the time series of historical returns (with T observations in each time
series). A zero-cost strategy can be built by, e.g., buying the commodity futures in
the bottom quintile by skewness, and selling the futures in the top quintile. 156
9.6 Strategy: Trading with pricing models
Commodity futures term structure is nontrivial. One way to model it is via stochas-
tic processes. Let S(t) be the spot price, and let X(t) = ln( S(t)). Then X(t)
can be modeled using, e.g., a mean-reverting Brownian motion (i.e., the Ornstein-
Uhlenbeck process [Uhlenbeck and Ornstein, 1930]): 157
dX(t) = κ [a− X(t)] dt + σ dW (t) (459)
155 Or the average spot price between 5.5 and 4.5 years ago.
156 See, e.g., [Fernandez-Perez et al , 2018]. For some additional pertinent literature, see, e.g.,
[Barberis and Huang, 2008], [Christie-David and Chaudry, 2001], [Eastman and Lucey, 2008],
[Gilbert, Jones and Morris 2006], [Junkus, 1991], [Kumar, 2009], [Lien, 2010], [Lien and Wang,
2015], [Mitton and Vorkink, 2007], [Stulz, 1996], [Tversky and Kahneman, 1992].
157 This is a one-factor model. More complex models including multifactor models, noncon-
stant/stochastic volatility models, etc., can be considered instead. For some literature on model-
ing futures prices via stochastic processes and related topics, see, e.g., [Andersen, 2010], [Bessem-
binder et al, 1995], [Borovkova and Geman, 2006], [Casassus and Collin-Dufresne, 2005], [Chaiyapo
and Phewchean, 2017], [Choi et al , 2014], [Geman and Roncoroni, 2006], [Gibson and Schwartz,
1990], [Hilliard and Reis, 1998], [Jankowitsch and Nettekoven, 2008], [Litzenberger and Rabinowitz,
1995], [Liu and Tang, 2011], [Milonas, 1991], [Miltersen and Schwartz, 1998], [Ng and Pirrong,
1994], [Nielsen and Schwartz, 2004], [Paschke and Prokopczuk, 2012], [Pindyck, 2001], [Routledge,
Seppi and Spatt, 2000], [Schwartz, 1997], [Schwartz, 1998], [Schwartz and Smith, 2000].
91
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 93

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Here the parameters κ (mean-reversion parameter), a (the long-run mean) and σ
(log-volatility) are assumed to be constant; and W (t) is a Q-Brownian motion,
where Q is a risk-free probability measure.158 The standard claim pricing argument
(see, e.g., [Baxter and Rennie, 1996], [Hull, 2012], [Kakushadze, 2015a]) gives for
the futures price F (t, T) (which is the price at time t of the futures contract with
the delivery date T )
F (t, T) = Et(S(T )) (460)
ln(F (t, T)) = Et(X(T )) + 1
2 Vt(X(T )) (461)
Here Et(·) and Vt(·) are the conditional expectation and variance, respectively, at
time t. This gives:
ln(F (t, T)) = exp ( −κ(T− t)) X(t) + a [1− exp (−κ(T− t))] +
+ σ2
4κ [1− exp (−2κ(T− t))] (462)
The parameters κ, a, σ can be ﬁtted using historical data (e.g., using nonlinear least
squares). Then the current market price can be compared to the model price to
identify the futures that are rich (sell signal) and cheap (buy signal) compared with
the model prediction. Here two cautionary remarks are in order. First, the model ﬁt
could work in-sample but have no predictive power out-of-sample, so the forecasting
power needs to be ascertained (see, e.g., [Paschke and Prokopczuk, 2012]). Second, a
priori we could write down any reasonable term structure model with desirable qual-
itative properties (e.g., mean-reversion) and ﬁt the parameters using historical data
without any reference to an underlying stochastic dynamics whatsoever, including
using, e.g., “black-box” machine learning techniques. So long as the model works
out-of-sample, there is no magic bullet here and “fancy” does not equal “better”.
10 Futures
10.1 Strategy: Hedging risk with futures
Exposures to certain risks can be mitigated by hedging with futures. E.g., a grain
trader who at time t anticipates that he or she will need to buy (sell) X tons of soy
at a later time T can hedge the risk of soy prices increasing (decreasing) between t
and T by buying (selling) at time t a futures contract with the delivery date T for
the desired amount of soy. This simple strategy can have tweaks and variations. 159
158 Note that this model reduces to the Black-Scholes model [Black and Scholes, 1973] in the
limit κ→ 0, a→∞ , κ a= ﬁxed.
159 For some literature on hedging with futures, see, e.g., [Ahmadi, Sharp and Walther, 1986],
[Cheung, Kwan and Yip, 1990], [Ederington, 1979], [G´ eczy, Minton and Schrand, 1997], [Ghosh,
1993], [Grant, 2016], [Hanly, Morales and Cassells, 2018], [Lebeck, 1978], [Lien and Tse, 2000],
[Mun, 2016], [Wolf, 1987], [Working, 1953].
92
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 94

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
10.1.1 Strategy: Cross-hedging
Sometimes a futures contract for the asset to be hedged may not be available. In
such cases, the trader may be able to hedge using a futures contract for another
asset with similar characteristics. 160 At maturity T , the payoﬀ of the cross-hedged
position established at time t (assuming the short futures position with the unit
hedge ratio) is given by:
S(T )− F (T, T ) + F (t, T) =
[S∗(T )− F (T, T )] + [S(T )− S∗(T )] + F (t, T) (463)
Here: the subscript ∗ indicates that the underlying asset of the futures contract is
diﬀerent from the hedged asset; S(t) is the spot price; F (t, T) is the futures price;
the ﬁrst term on the r.h.s. represents the basis risk stemming from the diﬀerence at
delivery between the futures and the spot prices; and the second term represents the
diﬀerence twixt the two underlying prices. In practice, the optimal hedge ratio may
not be 1 and can be estimated via, e.g., a serial regression or some other method. 161
10.1.2 Strategy: Interest rate risk hedging
Fixed-income assets are sensitive to interest rate variations (see Section 5) and
futures contracts can be used to hedge the interest rate risk. A long (short) hedge
position amounts to buying (selling) interest rate futures in order to hedge against
an increase (decrease) in the price of the underlying asset, i.e., a decrease (increase)
in the interest rates. 162 The corresponding P&L ( PL(t, T) for the long hedge and
PS(t, T) for the short hedge, assuming the position is established at t = 0 with the
unit hedge ratio and the maturity is T ) is given by:
PL(t, T) = B(0, T)− B(t, T) (464)
PS(t, T) = B(t, T)− B(0, T) (465)
B(t, T) = S(t)− F (t, T) (466)
160 For some literature on cross-hedging with futures, see, e.g., [Anderson and Danthine, 1981],
[Ankirchner et al , 2012], [Ankirchner and Heyne, 2012], [Benet, 1990], [Blake and Catlett, 1984],
[Blank, 1984], [Brooks, Davies and Kim, 2007], [Chen and Sutcliﬀe, 2007], [Dahlgran, 2000], [De-
Maskey, 1997], [DeMaskey and Pearce, 1998], [Foster and Whiteman, 2002], [Franken and Parcell,
2003], [Hartzog, 1982], [Lafuente, 2013], [McEnally and Rice, 1979], [Mun and Morgan, 1997].
161 For various optimal hedge ratio techniques, see, e.g., [Baillie and Myers, 1991], [Brooks and
Chong, 2001], [Brooks, Henry and Persand, 2002], [Cecchetti, Cumby and Figlewski, 1988], [Davis,
2006], [Holmes, 1996], [Lien, 1992], [Lien, 2004], [Lien and Luo, 1993], [Lindahl, 1992], [Low et al ,
2002], [Kroner and Sultan, 1993], [Monoyios, 2004], [Moosa, 2003b], [Myers, 1991].
162 For some literature on hedging the interest rate risk with futures, see, e.g., [Booth, Smith and
Stolz, 1984], [Briys and Solnik, 1992], [ ˇCerovi´ c and Pepi´ c, 2011], [Clare, Ioannides and Skinner,
2000], [Fortin and Khoury, 1984], [Gay, Kolb and Chiang, 1983], [Hilliard, 1984], [Hilliard and
Jordan, 1989], [Ho and Saunders, 1983], [Kolb and Chiang, 1982], [Lee and Oh, 1993], [Pepi´ c,
2014], [Picou, 1981], [Trainer, 1983], [Yawitz and Marshall, 1985], [Yeutter and Dew, 1982].
93
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 95

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
where B(t, T) is the futures basis. In practice, the hedge ratio may not be 1. If a
hedge is against a bond in the futures delivery basket, 163 then the conversion factor
model164 is commonly used to compute the hedge ratio hC:
hC = C MB
MF
(467)
where MB is the nominal value of the bond, MF is the nominal value of the futures,
and C is the conversion factor. Unlike the conversion factor model, the modiﬁed
duration hedge ratio hD can be used for both deliverable and non-deliverable bonds:
hD = β DB
DF
(468)
where DB is the dollar duration 165 of the bond, DF is the dollar duration of the
futures, and β (which is often set to 1) is the change in the bond yield relative to
the change in the futures yield, both taken for a given change in the risk-free rate.166
10.2 Strategy: Calendar spread
A bull (bear) futures spread amounts to buying (selling) a near-month futures and
selling (buying) a deferred-month futures. This reduces exposure to the overall mar-
ket volatility and allows to focus more on the fundamentals. Thus, for commodity
futures, for the most part, near-month contracts react to supply and demand more
than deferred-month contracts. Therefore, if the trader expects low (high) supply
and high (low) demand, then the trader can make a bet with a bull (bear) spread.167
163 Typically, an interest rate futures contract allows not just one bond but any bond from a
predeﬁned array of bonds (with varying maturities, coupons, etc.) to be delivered. Hence the use
of the conversion factor (see below) deﬁned as follows [Hull, 2012]: “The conversion factor for a
bond is set equal to the quoted price the bond would have per dollar of principal on the ﬁrst day
of the delivery month on the assumption that the interest rate for all maturities equals 6% per
annum (with semiannual compounding).”
164 The conversion factor model applies only to futures contracts that use conversion factors,
such as T-bond and T-note futures.
165 Recall that the dollar duration equals the price times the modiﬁed duration.
166 The factorβ can be estimated based on the historical data. For some literature on interest rate
futures hedge ratios and related topics, see, e.g., [Chang and Fang, 1990], [Chen, Kang and Yang,
2005], [Daigler and Copper, 1998], [Falkenstein and Hanweck, 1996], [Fisher and Weil, 1971], [Gay
and Kolb, 1983], [Geske and Pieptea, 1987], [Grieves and Mann, 2004], [Grieves and Marcus,
2005], [Hegde, 1982], [Kolb and Chiang, 1981], [Kuberek and Peﬂey, 1983], [Landes, Stoﬀels and
Seifert, 1985], [Pitts, 1985], [Rendleman, 1999], [Toevs and Jacob, 1986], [Viswanath, 1993].
167 For some literature on futures calendar spreads and related topics, see, e.g., [Abken, 1989],
[Adrangi et al , 2006], [Barrett and Kolb, 1995], [Bernstein, 1990], [Bessembinder, 1992], [Bessem-
binder, 1993], [Bessembinder and Chan, 1992], [Billingsley and Chance, 1988], [Castelino and Vora,
1984], [Cole et al , 1999], [Daigler, 2007], [de Roon, Nijman and Veld, 1998], [de Roon, Nijman and
Veld, 2000], [Dunis, Laws and Evans, 2006], [Dunis, Laws and Evans, 2010], [Duttet al, 1997], [Frino
and McKenzie, 2002], [Girma and Paulson, 1998], [Hou and Nord´ en, 2018], [Kawaller, Koch and
94
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 96

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
10.3 Strategy: Contrarian trading (mean-reversion)
This strategy is similar to the mean-reversion strategy discussed in Subsection 3.9.
Within a given universe of futures labeled by i = 1 , . . . , N, the “market index”
return is calculated as an equally weighted average:
Rm = 1
N
N∑
i=1
Ri (469)
where Ri are the individual futures returns (typically over the last one week). The
capital allocation weights wi then are given by
wi =−γ [Ri− Rm] (470)
where γ > 0 is ﬁxed via the normalization condition
N∑
i=1
|wi| = 1 (471)
Note that the strategy is automatically dollar-neutral. It amounts to buying losers
and selling winners w.r.t. the market index (see, e.g., [Wang and Yu, 2004]). 168 As
in the case of equities, the simple weighting scheme given by Eq. (470) is prone to
overinvesting in volatile futures, which can be mitigated by suppressing wi by 1/σi
or 1/σ2
i , where σi are the historical volatilities. The portfolio is rebalanced weekly.
10.3.1 Strategy: Contrarian trading – market activity
Bells and whistles can be added to the above “basic” mean-reversion strategy by
incorporating volume and open interest ﬁlters. Let Vi be the total volume for the
futures labeled by i over the last week (i.e., the sum of daily volumes over the
last week), and V′
i be the total volume over the prior week. Let Ui and U′
i be the
analogous quantities for the open interest. Let
vi = ln(Vi/V′
i ) (472)
ui = ln(Ui/U′
i) (473)
Then the strategy can be built, e.g., by taking the upper half of the futures by the
volume factor vi, taking the lower half of these futures by the open interest factor
ui, and applying the strategy deﬁned by Eq. (470) to this subset of the futures. 169
Ludan, 2002], [Kim and Leuthold, 1997], [McComas, 2003], [Moore, Toepke and Colley, 2006], [Ng
and Pirrong, 1994], [Perchanok, 2012], [Perchanok and Kakabadse, 2013], [Poitras, 1990], [Ross,
2006], [Salcedo, 2004], [Schap, 2005], [Shimko, 1994], [Till and Eagleeye, 2017], [van den Goorbergh,
2004].
168 For some additional pertinent literature, see, e.g., [Bali and Demirtas, 2008], [Bessembinder
et al , 1995], [Bianchi, Drew and Fan, 2015], [Chaves and Viswanathan, 2016], [Fuertes, Miﬀre and
Fernandez-Perez, 2015], [Irwin, Zulauf and Jackson, 1996], [Julio, Hassan and Ngene, 2013], [Leung
et al , 2016], [Monoyios and Sarno, 2002], [Rao, 2011], [Rosales and McMillan, 2017], [Tse, 2017].
169 The rationale behind this is that: i) larger volume changes are likely indicative of greater
overreaction (see, e.g., [Bloom, Easley and O’Hara, 1994], [Conrad, Hameed and Niden, 2013],
95
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 97

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
10.4 Strategy: Trend following (momentum)
Various momentum strategies for futures can be constructed similarly to those for
stocks. Here is a simple example (see, e.g., [Balta and Kosowski, 2013], [Moskowitz,
Ooi and Pedersen, 2012]). 170 Let Ri be the returns for the futures labeled by i =
1, . . . , N over the past period T (which can be measured in, e.g., days, weeks, or
months). Then the weights wi of the trading portfolio are given by
wi = γ ηi
σi
(474)
ηi = sign(Ri) (475)
where σi are the historical volatilities (computed over the period T or some other
period), and γ > 0 is ﬁxed via the normalization condition
N∑
i=1
|wi| = 1 (476)
Note that this strategy is equivalent to the optimization strategy (see Subsection
3.18, Eq. (350)) with a diagonal covariance matrix Cij = σ2
i δij (i.e., the correlations
between diﬀerent futures are ignored) and the expected returns Ei = ηiσi. This is
to be contrasted with the expected returns based on the cumulative returns (Eq.
(267)), which in this case equal Ri. One issue with using Ei = ηiσi as opposed to
Ei = Ri is that, for small |Ri| (e.g., compared with σi), ηi can ﬂip even though the
change in Ri is small. This results in an undesirable instability in the strategy. There
are ways to mitigate this, e.g., by smoothing via ηi = tanh(Ri/κ), where κ is some
parameter, e.g., the cross-sectional standard deviation of Ri (see, e.g., [Kakushadze,
2015b]). Alternatively, one may simply take Ei = Ri (and further use a non-diagonal
Cij). Also, note that the weights deﬁned by Eq. (474) are not dollar-neutral. This
can be rectiﬁed by demeaning them:
wi = γ
[
ηi
σi
− 1
N
N∑
j=1
ηj
σj
]
(477)
One shortcoming of this is that now some futures with ηi > 0 may be sold, and some
futures with ηi < 0 may be bought. To avoid this, if the number N+ =|H+| of the
[DeBondt and Thaler, 1985], [Gervais and Odean, 2001], [Odean, 2002], [Statman, Thorley and
Vorkink, 2006]), so a greater “snap-back” (i.e., mean-reversion) eﬀect can be expected; and ii) open
interest is related to trading by hedgers and is a proxy for market depth (see, e.g., [Bessembinder
and Seguin, 1993]), so an increase in open interest is indicative of a deeper market where volume
increases have smaller eﬀects on prices as compared with when there is a decrease in open interest.
170 For some additional pertinent literature, see, e.g., [Ahn et al , 2002], [Bianchi, Drew and
Fan, 2015], [Dusak, 1973], [Fuertes, Miﬀre and Fernandez-Perez, 2015], [Fuertes, Miﬀre and Rallis,
2010], [Hayes, 2011], [Kazemi and Li, 2009], [Miﬀre and Rallis, 2007], [Pirrong, 2005], [Reynauld
and Tessier, 1984], [Schneeweis and Gupta, 2006], [Szakmary, Shen and Sharma, 2010].
96
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 98

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
futures with ηi > 0 is not dramatically diﬀerent from the number N− =|H−| of the
futures with ηi < 0 (here H± ={i|± ηi > 0}), we can take the weights to be
wi = γ+
ηi
σi
, i ∈ H+ (478)
wi = γ−
ηi
σi
, i ∈ H− (479)
So, now we have two parameters γ±, which can be ﬁxed to satisfy Eq. (476) and
the dollar-neutrality condition
N∑
i=1
wi = 0 (480)
However, if most ηi are positive (negative), i.e., we have skewed returns, then long
(short) positions will be well-diversiﬁed, while the short (long) positions will not
be. This can happen, e.g., if the broad market is rallying (selling oﬀ). Eq. (477)
mitigates this to some extent. However, ηi can still be skewed in this case. A simple
way to avoid this altogether is to use the demeaned returns ˜Ri instead of Ri, where
˜Ri = Ri− Rm, and the “market index” return Rm is deﬁned by Eq. (469). 171 Then
ηi = sign(˜Ri) are no longer skewed and dollar-neutrality can be achieved as above.172
11 Structured Assets
11.1 Generalities: Collateralized Debt Obligations (CDOs)
A CDO is an asset-backed security (ABS) consisting of a basket of assets such
as bonds, credit default swaps, etc. It is divided into multiple tranches, which
consist of assets with diﬀerent credit ratings and interest rates. Each tranche has
an attachment point a and a detachment point d. E.g., a 3-8% tranche (for which
a = 3% and d = 8%) means that it begins to lose value when the underlying
portfolio loss exceeds 3%; and when the underlying portfolio loss exceeds 8%, the
tranche value is completely wiped out.173 A buyer (long position) of a CDO tranche
is a protection seller: in return for receiving periodic premium payments, in the
171 I.e., in this case the momentum, winners and losers are deﬁned w.r.t. the market index, and
the so-deﬁned winners are bought, while the losers are sold.
172 Further, instead of using cumulative returns Ri, one can use exponential moving averages
(to suppress past contributions – see Section 3), the Hodrick-Prescott ﬁlter (to remove the noise
and identify the trend – see Section 8), the Kalman ﬁlter (see, e.g., [Babbs and Nowman, 1999],
[Benhamou, 2016], [Bruder et al , 2013], [DeMoura, Pizzinga and Zubelli, 2016], [Elliott, Van Der
Hoek and Malcolm, 2005], [Engle and Watson, 1987], [Harvey, 1984], [Harvey, 1990], [Hatemi-J,
and Roca, 2006], [Kalman, 1960], [Lautier and Galli, 2004], [Levine and Pedersen, 2016], [Martinelli
and Rhoads, 2010], [Vidyamurthy, 2004]), or some other time-series ﬁlters.
173 Examples of tranches are (in the decreasing order of default risk and periodic premium
payment rate): equity 0-3% tranche; junior mezzanine 3-7% tranche; senior mezzanine 7-10%
tranche; senior 10-15% tranche; and super senior 15-30% tranche.
97
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 99

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
event of a default, the buyer has the obligation to cover the default up to the size
of the tranche. A seller (short position) of a CDO tranche is a protection buyer:
in return for making periodic premium payments, the seller receives a payment in
the event of a default. Synthetic CDOs are “synthesized” through credit derivatives
such as CDS (credit default swaps – see Subsection 5.14) on a pool of reference
entities (e.g., bonds, loans, names of companies or countries). Reference pools for
exchange-traded single-tranche CDOs are CDS indexes such as CDX and iTraxx.174
Let ti, i = 1, . . . , n, denote the times at which the periodic premium payments
are made. 175 Let H(t) denote the set of possible defaults ℓα, α = 1 , . . . , K, that
can occur by time t, and let pα(t) denote the corresponding probabilities (which are
model-dependent). Here ℓα are the dollar amounts of the defaults. 176 The expected
loss L(t) can be computed as
L(t) =
K∑
α=1
pα(t) max(min(ℓα, Ld)− La, 0) (481)
where La = a MCDO, Ld = d MCDO, and MCDO is the CDO notional in dollars. 177
From the long tranche investor’s perspective, the mark-to-market (MTM) value of
the tranche, call itM, is given by
M = P− C (482)
P = S
n∑
i=1
Di ∆i [Mtr− L(ti)] (483)
C =
n∑
i=1
Di [L(ti)− L(ti−1)] (484)
Here: P is the premium leg; C is the contingent (default) leg; S is the spread;
∆i = ti− ti−1; Di is the risk-free discount factor for the payment date ti; and
174 For some literature on CDOs and related topics, see, e.g., [Altman et al , 2005], [Amato
and Gyntelberg, 2005], [Amato and Remolona, 2003], [Andersen and Sidenius, 2005], [Ander-
sen, Sidenius and Basu, 2003], [Belkin, Suchover and Forest, 1998], [Bielecki, Brigo and Patras,
2011], [Bol, Rachev and W¨ urth, 2009], [Boscher and Ward, 2002], [Cousin and Laurent, 2012], [Das,
2005], [Davis and Lo, 2001], [Ding and Sherris, 2011], [Douglas, 2007], [Duﬃe, 2004], [Duﬃe and
Gˆ arleanu, 2001], [Duﬃe and Huang, 1996], [Duﬃe and Singleton, 1997a], [Duﬃe and Singleton,
1997b], [Fabozzi, 2006a], [Finger, 1999], [Frey, McNeil and Nyfeler, 2001], [Gibson, 2004], [Good-
man, 2002], [Goodman and Lucas, 2002], [Houdain and Guegan, 2006], [Hull and White, 2006], [Hull
and White, 2010], [Jarrow, Lando and Turnbull, 1997], [Jarrow and Turnbull, 1995], [Jobst,
2005], [Jobst, 2006a], [Jobst, 2006b], [Jobst, 2006c], [Jobst, 2007], [Laurent and Gregory, 2005], [Li,
2000], [Lucas, Goodman and Fabozzi, 2006], [Meissner, 2008], [Packer and Zhu, 2005], [Prince,
2005], [Schmidt and Ward, 2002], [Sch¨ onbucher, 2003], [Tavakoli, 1998], [Vasicek, 2015].
175 For simplicity, we can also assume that any default payments are also made at those times.
176 If the notional amount of the defaulted credit labeled by α is Mα, then ℓα = Mα(1−Rα),
where Rα is the recovery rate (which may be nonzero) of said credit.
177 Recall that the attachment a and the detachment d are measured in %.
98
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 100

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Mtr = Ld− La is the tranche notional. (Also, t is measured in years, t0 is the initial
time, and L(t0) = 0). Setting the MTMM = 0 ﬁxes the value of the spread S = S∗.
We can further deﬁne the “risky duration”D of the tranche as the ﬁrst derivative
of the MTM w.r.t. the spread:
M(S) = (S− S∗)
n∑
i=1
Di ∆i [Mtr− L(ti)] (485)
D = ∂M/∂S =
n∑
i=1
Di ∆i [Mtr− L(ti)] (486)
The risky durationDix can also be deﬁned in a similar fashion for a CDS index.
11.2 Strategy: Carry, equity tranche – index hedging
This strategy amounts to buying the equity (lowest quality) tranche and Delta-
hedging it by selling the index. The Delta (i.e., the hedge ratio) is given by 178
∆ix = D
Dix
(487)
The premiums received from the equity tranche are higher than the premiums paid
on the short index position. The risk is the exposure to equity tranche credit events.
11.3 Strategy: Carry, senior/mezzanine – index hedging
This strategy amounts to selling a high quality tranche (e.g., senior/mezzanine) and
Delta-hedging the position by buying the index.179 The Delta is given by Eq. (487).
11.4 Strategy: Carry – tranche hedging
This strategy amounts to buying a low quality tranche and Delta-hedging the posi-
tion by selling a high quality tranche. The hedge ratio is given by:
∆high = Dlow
Dhigh
(488)
HereDlow andDhigh are the risky durations of the low and high quality tranches.
178 For some literature on CDO tranche hedging and related topics, see, e.g., [Arnsdorf and
Halperin, 2007], [Bielecki, Jeanblanc and Rutkowski, 2007], [Bielecki, Vidozzi and Vidozzi, 2008],
[Carmona and Cr´ epey, 2010], [Cont and Minca, 2013], [Frey and Backhaus, 2008], [Frey and Back-
haus, 2010], [Giesecke and Weber, 2006], [Herbertsson, 2008], [Houdain and Guegan, 2006], [Lau-
rent, Cousin and Fermanian, 2011], [Walker, 2008].
179 The premiums received from the index are higher than the premiums paid on the short tranche
position. So, this trade is “opposite” to the long equity tranche trade hedged with the index.
99
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 101

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
11.5 Strategy: Carry – CDS hedging
This strategy amounts to buying a low quality tranche and Delta-hedging the po-
sition by selling a single-name CDS with lower premium payments than the long
tranche (instead of the index or a higher quality tranche). The hedge ratio is given
by Eq. (487) with Dix replaced by the risky duration DCDS of the CDS:
∆CDS = D
DCDS
(489)
11.6 Strategy: CDOs – curve trades
As in the case of bonds (see Subsection 5.13), a ﬂattener (steepener) curve trade
involves a simultaneous sale (purchase) of a short-term tranche and a purchase (sale)
of a long-term tranche. Put diﬀerently, with a ﬂattener (steepener), the trader is
buying (selling) short-term protection and selling (buying) long-term protection,
i.e., the trader expects the spread curve to ﬂatten (steepen), whereby the spread
between the long-term and short-term tranches decreases (increases). The carry of
the curve trade over the period from time t to time t + ∆t can be deﬁned as follows
C(t, t + ∆t) = (Mlong Slong− Mshort Sshort) ∆t (490)
where Mlong and Mshort are the long and short tranche notionals, andSlong and Sshort
are the corresponding spreads. The trade can be structured to be dollar-neutral (i.e.,
notional-neutral, Mlong = Mshort),180 risky-duration-neutral (Dlong =Dshort, see Eq.
(486)), carry-neutral (MlongSlong = MshortSshort), etc.181 The P&L of the strategy is
given by (Mlong andMshort are the long and short tranche MTMs, see Eq. (485)):
P&L =Mlong−Mshort (491)
11.7 Strategy: Mortgage-backed security (MBS) trading
This strategy amounts to buying MBS passthroughs 182 and duration-hedging their
interest rate exposure with interest rate swaps. Thus, the main risk of a passthrough
MBS is the prepayment risk, whereby homeowners have an option to prepay their
mortgages. Homeowners reﬁnance their mortgages as the interest rates drop, which
results in negative convexity in the MBS price as a function of the interest rates
180 In this case, for an upward-sloping curve, a ﬂattener (steepener) has positive (negative) carry
as Slong >S short (Slong <S short).
181 For some literature on curve trades and related topics, see, e.g., [Bobey, 2010], [Burtshell,
Gregory and Laurent, 2009)], [Choro´ s-Tomczyk, H¨ ardle and Okhrin, 2016], [Crabbe and Fabozzi,
2002], [Detlefsen and H¨ ardle, 2013], [Hagenstein, Mertz and Seifert, 2004], [Hamerle, Igl and Plank,
2012], [Hull and White, 2004], [Kakodkar et al , 2006], [Koopman, Lucas and Schwaab, 2012], [Lin
and Shyy, 2008], [Rajan, McDermott and Roy, 2007].
182 An MBS is an asset backed by a pool of mortgages. In a passthrough MBS, which is the most
common MBS type, cash ﬂows are passed from debtors to investors through an intermediary.
100
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 102

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
(e.g., the 5-year swap rate). The hedge ratios are model-dependent and a variety of
prepayment models can be constructed. Alternatively one can follow a nonparamet-
ric approach whereby using historical data one estimates the ﬁrst derivative of the
passthrough MBS price P w.r.t. the 5-year swap rate R with the constraint that
P is a non-increasing function of R (see, e.g., [Duarte, Longstaﬀ and Yu, 2006]), 183
employing, e.g., a constrained regression (see, e.g., [A¨ ıt-Sahalia and Duarte, 2003]).
12 Convertibles
12.1 Strategy: Convertible arbitrage
A convertible bond is a hybrid security with an embedded option to convert the bond
(a ﬁxed-income instrument) to a preset number (knows as the conversion ratio) of
the issuer’s stock (an equity instrument) when, e.g., the stock price reaches a preset
level (known as the conversion price). Empirically, convertibles at the issuance
tend to be undervalued relative to their “fair” value. 184 This gives rise to arbitrage
opportunities. A convertible arbitrage strategy amounts to buying a convertible
bond and simultaneously shorting h units of the underlying stock, where the hedge
ratio is given by
h = ∆× C (492)
∆ = ∂V /∂S (493)
Here: C is the conversion ratio; V is the value of the conversion option (which is
model-dependent); S is the underlying stock price; and ∆ is the (model-dependent)
183 For some additional pertinent literature, see, e.g., [Ambrose, LaCour-Little and Sanders,
2004], [Biby, Modukuri and Hargrave, 2001], [Bielecki, Brigo and Patras, 2011], [Boudoukh et
al, 1997], [Brazil, 1988], [Brennan and Schwartz, 1985], [Carron and Hogan, 1988], [Chinloy,
1989], [Davidson, Herskovitz and Van Drunen, 1988], [Dechario et al , 2010], [Downing, Jaﬀee
and Wallace, 2009], [Dunn and McConnell, 1981a], [Dunn and McConnell, 1981b], [Dynkin et
al, 2001], [Fabozzi, 2006b], [Gabaix, Krishnamurthy and Vigneron, 2007], [Glaeser and Kallal,
1997], [Hu, 2001], [Longstaﬀ, 2005], [Kau et al , 1995], [McConnell and Buser, 2011], [McKenzie,
2002], [Nothaft, Lekkas and Wang, 1995], [Passmore, Sherlund and Burgess, 2005], [Richard and
Roll, 1989], [Schultz, 2016], [Schwartz and Torous, 1989], [Schwartz and Torous, 1992], [Stanton,
1995], [Thibodeau and Giliberto, 1989], [Vickery and Wright, 2010].
184 For some literature on convertible bonds and related topics, see, e.g., [Agarwal et al , 2011],
[Ammann, Kind and Seiz, 2010], [Ammann, Kind and Wilde, 2003], [Batta, Chacko and Dharan,
2010], [Brennan and Schwartz, 1988], [Brown et al, 2012], [Calamos, 2003], [Chan and Chen, 2007],
[Choi et al , 2010], [Choi, Getmansky and Tookes, 2009], [De Jong, Dutordoir and Verwijmeren,
2011], [Duca et al , 2012], [Dutordoir et al , 2014], [Grundy and Verwijmeren, 2016], [Henderson,
2005], [Henderson and Tookes, 2012], [Ingersoll, 1977], [Kang and Lee, 1996], [King, 1986], [King
and Mauer, 2014], [Korkeamaki and Michael, 2013], [Lewis, Rogalski and Seward, 1999], [Lewis
and Verwijmeren, 2011], [Loncarski, ter Horst and Veld, 2006], [Loncarski, ter Horst and Veld,
2009], [Mayers, 1998], [Ryabkov, 2015], [Stein, 1992], [Tsiveriotis and Fernandes, 1998], [van Marle
and Verwijmeren, 2017], [Zabolotnyuk, Jones and Veld, 2010].
101
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 103

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Delta of the conversion option. 185 Typically, the position is held for 6-12 months
starting at the issuance date of the convertible and the hedge ratio is updated daily.
12.2 Strategy: Convertible option-adjusted spread
This strategy amounts to simultaneously buying and selling two diﬀerent convertible
bonds of the same issuer. The long position is in a bond with a higher option-
adjusted spread (OAS), and the short position is in a bond with a lower OAS (see,
e.g., [Calamos, 2003]). Then the trade is proﬁtable if these two spreads converge.
The OAS can be calculated as follows (see, e.g., [Hull, 2012]). 186 A straightfor-
ward (but not the only) 187 way to compute the price PC of the convertible bond is
to assume that
PC = PB + V (494)
where PB is the price of the straight bond (without the embedded option), and V
is the value of the conversion option, which is a call option. PB is computed via the
standard discounting of the future cash ﬂows of the bond. On the other hand, V
depends on the risk-free interest rate curve. At the initial iteration, V is computed
(using a pricing model for the call option) assuming the zero-coupon government
Treasury curve as the risk-free interest rate curve. This initial iteration V (0) may
not coincide with Pmkt
C − PB, where Pmkt
C is the market price of the convertible
bond. Then one iteratively (e.g., using the bisection method) parallel-shifts the
input Treasury curve until V computed using the so-shifted curve is such that V =
Pmkt
C − PB. The curve parallel shift obtained via this iterative procedure is the OAS.
13 Tax Arbitrage
13.1 Strategy: Municipal bond tax arbitrage
This strategy is one of the most common and simple forms of tax arbitrage. It
amounts to borrowing money and buying tax-exempt municipal bonds.188 The strat-
185 The Delta itself changes with the stock price S. To account for this, the option Gamma can
be used as in Subsection 7.4.1 (Gamma hedging).
186 For some additional literature related to OAS (mostly focused on applications to MBS), see,
e.g., [Boyarchenko, Fuster and Lucca, 2014], [Brazil, 1988], [Brown, 1999], [Cerrato and Djennad,
2008], [Dong et al, 2009], [Hayre, 1990], [Huang and Kong, 2003], [Levin and Davidson, 2005], [Liu
and Xu, 1998], [Stroebel and Taylor 2012], [Windas, 2007].
187 For some literature on convertible bond pricing, see, e.g., [Ayache, Forsyth and Vetzal, 2003],
[Batten, Khaw and Young, 2014], [Brennan and Schwartz, 1977], [Finnerty and Tu, 2017], [Ingersoll,
1977], [Kang and Lee, 1996], [King, 1986], [Kwok, 2014], [McConnell and Schwartz, 1986], [Milanov
et al, 2013], [Park, Jung and Lee, 2018], [S¨ orensson, 1993], [Tsiveriotis and Fernandes, 1998], [Xiao,
2013], [Zabolotnyuk, Jones and Veld, 2010].
188 For some literature on municipal bond tax arbitrage and related topics, see, e.g., [Ang et al ,
2017], [Buser and Hess, 1986], [Chalmers, 1998], [Erickson, Goolsbee and Maydew, 2003], [Heaton,
1988], [Kochin and Parks, 1988], [Longstaﬀ, 2011], [Miller, 1977], [Poterba, 1986], [Poterba, 1989],
102
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 104

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
egy return is given by
R = rlong− rshort (1− τ) (495)
Here: rlong is the interest rate of the bought municipal bonds, rshort is the interest
rate of the loan, and τ is the corporate tax rate. This strategy is attractive to
companies in jurisdictions where tax rules allow them to buy tax-exempt municipal
bonds and deduct interest expenses from their taxable income (a.k.a. “tax shield”).
13.2 Strategy: Cross-border tax arbitrage
The U.S. double-taxes corporate income. The corporate income is ﬁrst taxed at
the corporate level. Then, it is taxed again when dividends are received by the
shareholders. In some other countries the taxation systems are designed to relieve
the tax burden, e.g., by not taxing dividends (as, e.g., in Singapore), or by giving
shareholders tax credits attached to dividend payments (as, e.g., in Australia). In the
case where this “dividend imputation” corporate tax system gives the full tax credit
to shareholders, it can be schematically described as follows (see, e.g., [McDonald,
2001]):189



Corporate tax rate = τc
Cash dividend paid = D
Dividend tax credit = C = D τc
1−τc
Taxable income = It = D + C = D
1−τc
Personal tax rate = τp
Personal income tax = T = It τp
Dividend income after credit and tax = I = D + C− T = D 1−τp
1−τc
(496)
So, if the corporate income is P and the corporation pays all its income after taxes as
dividends, then D = P (1− τc) and I = P (1− τp), so there is no double-taxation.190
While in countries with imputation systems domestic investors enjoy tax credits,
generally foreign investors do not. If there were no tax credits, the price drop
between cum-dividend and ex-dividend 191 is expected to reﬂect the dividend. In
the presence of tax credits, the drop is expected to be higher: if it fully reﬂects
the tax credit, then it is D (1 + κ), where κ is the tax credit rate. (In the above
nomenclature, 1 + κ = 1/(1 + τc).) So, a foreign investor is eﬀectively penalized for
[Skelton, 1983], [Trzcinka, 1982], [Yawitz, Maloney and Ederington, 1985].
189 However, there can be limitations on the tax credit and other subtleties present depending
on the jurisdiction, various circumstances, etc.
190 In contrast, in the double-taxation system we would instead have: D = P (1−τc), It = D,
T =It τp, I =It−T =P (1−τc) (1−τp).
191 Cum-dividend means the stock buyer is entitled to receive a dividend that has been declared
but not paid. Ex-dividend means the stock seller is entitled to the dividend, not the buyer.
103
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 105

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
holding the stock. To avoid this, the foreign investor can sell the stock cum-dividend
and buy it back ex-dividend.192 Alternatively, the foreign investor can loan the stock
to a domestic investor cum-dividend and receive the stock back ex-dividend along
with (some preset portion of) the tax credit – assuming no restrictions on such cross-
border tax arbitrage. A swap agreement would also achieve the same result. 193
13.2.1 Strategy: Cross-border tax arbitrage with options
Absent a tax credit, there is a theoretical upper bound on the value of an American
put option (see, e.g., [Hull, 2012]):
Vput(K, T)≤ Vcall(K, T)− S0 + K + D (497)
Here: Vput (Vcall) is the price of the put (call) option at time t = 0; K is the
strike price; S0 is the stock price at t = 0; T is the time to maturity; and D is
the present value of the dividends during the life of the option. Put options are
optimally exercised ex-dividend. Therefore, in the presence of a tax credit, it is
expected that put prices should reﬂect the tax credit, i.e., they should be higher
than in the absence of the tax credit (see, e.g., [McDonald, 2001]). So the foreign
investor can sell the stock cum-dividend (at price S0) and write a deep ITM put
option, whose value close to expiration approximately is (here κ is the tax credit
rate deﬁned above)
Vput(K, T) = K− [S0− D (1 + κ)] (498)
The P&L, once the put is exercised ex-dividend at the strike price K, is the same
as with the stock loan/swap strategy discussed above:
P&L = S0 + Vput(K, T)− K = D (1 + κ) (499)
14 Miscellaneous Assets
14.1 Strategy: Inﬂation hedging – inﬂation swaps
This strategy amounts to buying (selling) inﬂation swaps in order to exchange a ﬁxed
(ﬂoating) rate of inﬂation for a ﬂoating (ﬁxed) rate. Inﬂation swaps conceptually are
similar to interest rate swaps (see Subsection 5.1.4). A buyer (seller) of an inﬂation
swap is long (short) the inﬂation and receives the ﬂoating (ﬁxed) rate. The buyer
has a positive return if the inﬂation exceeds the expected inﬂation (i.e., the swap
192 Assuming transaction costs are not prohibitively high.
193 For some literature on cross-border tax arbitrage and related topics, see, e.g., [Allen and
Michaely, 1995], [Amihud and Murgia, 1997], [Bellamy, 1994], [Booth, 1987], [Booth and Johnston,
1984], [Brown and Clarke, 1993], [Bundgaard, 2013], [Callaghan and Barry, 2003], [Christoﬀersen
et al , 2005], [Christoﬀersen et al , 2003], [Eun and Sabherwal, 2003], [Green and Rydqvist, 1999],
[Harris, Hubbard and Kemsley, 2001], [Lakonishok and Vermaelen, 1986], [Lasfer, 1995], [Lessambo,
2016], [McDonald, 2001], [Monkhouse, 1993], [Shaviro, 2002], [Wells, 2016], [Wood, 1997].
104
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 106

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ﬁxed rate, a.k.a. the “breakeven rate”). The ﬁxed rate typically is calculated as the
interest rate spread between the Treasury notes/bonds (as applicable) and Treasury
Inﬂation-Protected Securities (TIPS) with the same maturity as that of the swap.
The ﬂoating rate usually is based on an inﬂation index such as the Consumer Price
Index (CPI). The most common type of inﬂation swap is the zero-coupon inﬂation
swap (ZC), which has only one cash ﬂow at maturity T (measured in years). This
cash ﬂow is the diﬀerence between the ﬁxed rate cash ﬂow Cfixed and the ﬂoating
rate cash ﬂow Cfloating . These cash ﬂows, per $1 notational, are given by:
Cfixed = (1 + K)T− 1 (500)
Cfloating = I(T )/I(0)− 1 (501)
Here: K is the ﬁxed rate; and I(t) is the CPI value at time t (t = 0 is the time
at which the swap contract is entered into). Another type of inﬂation swaps is the
year-on-year inﬂation swap (YoY), which references annual inﬂation (as opposed to
the cumulative inﬂation referenced by the zero-coupon swap). Thus, assuming for
simplicity annual payments, we have (here t = 1, . . . , T is measured in years): 194
Cfixed(t) = K (502)
Cfloating (t) = I(t)/I(t− 1)− 1 (503)
14.2 Strategy: TIPS-Treasury arbitrage
This strategy is based on the empirical observation that Treasury bonds tend to be
overvalued relative to TIPS195 almost all the time (see, e.g., [Campbell, Shiller and
Viceira, 2009], [Driessen, Nijman and Simon, 2017], [Fleckenstein, 2012], [Haubrich,
194 For some literature on inﬂation swaps and related topics, see, e.g., [Belgrade and Benhamou,
2004], [Belgrade, Benhamou and Koehler, 2004], [Bouzoubaa and Osseiran, 2010], [Christensen,
Lopez and Rudebusch, 2010], [Deacon, Derry and Mirfendereski, 2004], [Fleming and Sporn, 2013],
[Haubrich, Pennacchi and Ritchken, 2012], [Hinnerich, 2008], [Jarrow and Yildirim, 2003], [Kenyon,
2008], [Lioui and Poncet, 2005], [Martellini, Milhau and Tarelli, 2015], [Mercurio, 2005], [Mercurio
and Moreni, 2006], [Mercurio and Moreni, 2009], [Mercurio and Yildirim, 2008].
195 TIPS pay semiannual ﬁxed coupons at a ﬁxed rate, but the coupon payments (and principal)
are adjusted based on inﬂation. For some literature on TIPS, inﬂation-indexed products and related
topics, see, e.g., [Adrian and Wu, 2010], [Ang, Bekaert and Wei, 2008], [Bardong and Lehnert,
2004], [Barnes et al , 2010], [Barr and Campbell, 1997], [Bekaert and Wang, 2010], [Buraschi and
Jiltsov, 2005], [Campbell, Sunderam and Viceira, 2017], [Chen, Liu and Cheng, 2010], [Chernov and
Mueller, 2012], [Christensen and Gillan, 2012], [D’Amico, Kim and Wei, 2018], [Deacon, Derry and
Mirfendereski, 2004], [Dudley, Roush and Steinberg, 2009], [Evans, 1998], [Fleckenstein, Longstaﬀ
and Lustig, 2017], [Fleming and Krishnan, 2012], [Grishchenko and Huang, 2013], [Grishchenko,
Vanden and Zhang, 2016], [G¨ urkaynak, Sack and Wright, 2010], [H¨ ordahl and Tristani, 2012],
[H¨ ordahl and Tristani, 2014], [Hunter and Simon, 2005], [Jacoby and Shiller, 2008], [Joyce, Lildholdt
and Sorensen, 2010], [Kandel, Ofer and Sarig, 1996], [Kitsul and Wright, 2013], [Kozicki and Tinsley,
2012], [Mehra, 2002], [Pennacchi, 1991], [Pﬂueger and Viceira, 2011], [Remolona, Wickens and
Gong, 1998], [Roll, 1996], [Roll, 2004], [Sack and Elsasser, 2004], [Sepp¨ al¨ a, 2004], [Shen, 2006], [Shen
and Corning, 2001], [Woodward, 1990], [Yared and Veronesi, 1999].
105
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 107

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Pennacchi and Ritchken, 2012]). The strategy amounts to selling a Treasury bond
(whose price is PTreasury , ﬁxed coupon rate is rTreasury , and maturity is T ) and
oﬀsetting this short position with a synthetic portfolio, which precisely replicates
the Treasury bond coupon and principal payments, but costs less than the Treasury
bond. This synthetic portfolio is constructed by buying TIPS (whose price is PTIPS
and maturity T is the same as that of the Treasury bond) with a ﬁxed coupon rate r
and n coupon payments at times ti, i = 1, . . . , n (with tn = T ), and simultaneously
selling n zero-coupon inﬂation swaps with maturities ti, the ﬁxed rate K, and the
notionals Ni = r + δti,T per $1 of the TIPS principal. The cash ﬂows (per $1
notional) at t = ti are given by (as above, I(t) is the CPI value at time t; also, time
is measured in the units of the (typically, semiannual) compounding periods):
CTIPS (ti) = Ni I(ti)/I(0) (504)
Cswap(ti) = Ni
[
(1 + K)ti− I(ti)/I(0)
]
(505)
Ctotal(ti) = Cswap(ti) + CTIPS (ti) = Ni (1 + K)ti (506)
So, the synthetic portfolio converts the indexed payments from TIPS into ﬁxed
payments with the eﬀective coupon rates reff (ti) = r (1 + K)ti. These synthetic
coupon payments almost replicate the Treasury bond coupons rTreasury . The exact
matching involves small long or short positions in STRIPS 196, which are given by
(see, e.g., [Fleckenstein, Longstaﬀ and Lustig, 2013] for details)
S(ti) = D(ti)
{
[rTreasury− reff (ti)] + δti,T
[
1− (1 + K)ti
]}
(507)
where D(τ) is the value of the STRIPS with maturity τ at time t = 0 (i.e., D(τ)
is a discount factor). In Eq. (507) the second term in the curly brackets (which is
proportional to δti,T and is nonzero only for i = n, i.e., at maturity T ) is included
as we must also match the principals at maturity. Note that the STRIPS positions
are established at t = 0. The net cash ﬂow C(0) at t = 0 is given by (note that the
net cash ﬂows at t > 0 are all null by replication)
C(0) = PTreasury− PTIPS −
n∑
i=1
S(ti) (508)
Empirically C(0) tends to be positive (even after transaction costs). Hence arbitrage.
14.3 Strategy: Weather risk – demand hedging
Various businesses and sectors of the economy can be aﬀected by weather conditions,
both directly and indirectly. Weather risk is hedged using weather derivatives. There
are no “tradable” weather indexes, so various synthetic indexes have been created.
196 STRIPS = “Separate Trading of Registered Interest and Principal of Securities”. Essentially,
STRIPS are zero-coupon discount bonds.
106
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 108

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
The most common ones are based on temperature. The cooling-degree-days (CDD)
and heating-degree-days (HDD) measure extreme high temperatures and extreme
low temperatures, respectively: 197
ICDD =
n∑
i=1
max(0, Ti− Tbase) (509)
IHDD =
n∑
i=1
max(0, Tbase− Ti) (510)
Ti = Tmin
i + Tmax
i
2 (511)
Here: i = 1 , . . . , n labels days; n is the life of the contract (a week, a month
or a season) measured in days; Tmin
i and Tmax
i are the minimum and maximum
temperatures recorded on the day labeled by i; and Tbase = 65◦F. Then, the demand
risk for heating days can, e.g., be hedged by a short futures position or a long put
option position with the hedge ratios given by (here (Cov) Var is serial (co)variance):
hHDD
futures = Cov(qw, IHDD)/Var(IHDD) (512)
hHDD
put =−Cov (qw, max(K− IHDD , 0)) /Var (max(K− IHDD , 0)) (513)
Here: qw is the portion of the demand aﬀected by weather conditions (as there might
be other, exogenous, non-weather-related components to the demand); and K is the
strike price. Similarly, the demand risk for cooling days can, e.g., be hedged by a
long futures position or a long call option position with the hedge ratios given by:
hCDD
futures = Cov(qw, ICDD)/Var(ICDD) (514)
hCDD
call = Cov (qw, max(ICDD− K, 0)) /Var (max(ICDD− K, 0)) (515)
197 For some literature on weather derivatives, weather indexes and related topics, see, e.g., [Ala-
ton, Djehiche and Stillberger, 2010], [Barrieu and El Karoui, 2002], [Barrieu and Scaillet, 2010],
[Benth, 2003], [Benth and Saltyte-Benth, 2005], [Benth and Saltyte-Benth, 2007], [Benth, Saltyte-
Benth and Koekebakker, 2007], [Bloesch and Gourio, 2015], [Brockett et al, 2010], [Brockett, Wang
and Yang, 2005], [Brody, Syroka and Zervos, 2002], [Campbell and Diebold, 2005], [Cao and Wei,
2000], [Cao and Wei, 2004], [Cartea and Figueroa, 2005], [Chaumont, Imkeller and M¨ uller, 2006],
[Chen, Roberts and Thraen, 2006], [Corbally and Dang, 2002], [Davis, 2001], [Dischel, 1998a], [Dis-
chel, 1998b], [Dischel, 1999], [Dorﬂeitner and Wimmer, 2010], [Dornier and Queruel, 2000], [Eder-
ington, 1979], [Geman, 1998], [Geman and Leonardi, 2005], [Ghiulnara and Viegas, 2010], [Golden,
Wang and Yang, 2007], [G¨ onc¨ u, 2012], [Hamisultane, 2009], [Hanley, 1999], [H¨ ardle and L´ opez Cabr-
era, 2011], [Huang, Shiu and Lin, 2008], [Huault and Rainelli-Weis, 2011], [Hunter, 1999], [Jain
and Baile, 2000], [Jewson, 2004a], [Jewson, 2004b], [Jewson, Brix and Ziehmann, 2005], [Jewson
and Caballero, 2003], [Lazo et al , 2011], [Lee and Oren, 2009], [Leggio and Lien, 2002], [Mraoua,
2007], [M¨ uller and Grandi, 2000], [Oetomo and Stevenson, 2005], [Parnaudeau and Bertrand,
2018], [Perez-Gonzalez and Yun, 2010], [Richards, Manfredo and Sanders, 2004], [Saltyte-Benth
and Benth, 2012], [Schiller, Seidler and Wimmer, 2010], [Svec and Stevenson, 2007], [Swishchuk
and Cui, 2013], [Tang and Jang, 2011], [Thornes, 2006], [Vedenov and Barnett, 2004], [Wilson,
2016], [Woodard and Garcia, 2008], [Yang, Brockett and Wen, 2009], [Zapranis and Alexandridis,
2008], [Zapranis and Alexandridis, 2009], [Zeng, 2000].
107
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 109

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
14.4 Strategy: Energy – spark spread
The spark spread is the diﬀerence between the wholesale price of electricity and the
price of natural gas required to produce it. 198 A spark spread can be built by, e.g.,
taking a short position in electricity futures and a long position in the corresponding
number of fuel futures. Such positions are used by electricity producers to hedge
against changes in the electricity price or in the cost of fuel, as well as by traders or
speculators who want to make a bet on a power plant. The number of fuel futures is
determined by the so-called heat rate H, which measures the eﬃciency with which
the plant converts fuel into electricity:
H = QF /QE (516)
Here: QF is the amount of fuel used to produce the amount of electricity QE; QF
is measured in MMBtu; Btu = British thermal unit, which is approximately 1,055
Joules; MBtu = 1,000 Btu; MMBtu = 1,000,000 Btu; QE is measured in Mwh =
Megawatt hour; the heat rate H is measured in MMBtu/Mwh. The spark spread is
measured in $/Mwh. So, if the price of electricity is PE (measured in $/Mwh) and
the price of fuel is PF (measured in $/MMBtu), then the spark spread is given by
S = PE− H PF (517)
The hedge ratio for the futures is aﬀected by the available futures contract sizes.
Thus, an electricity futures contract is FE = 736 Mwh, and a gas futures contract
is FF = 10, 000 MMBtu. So, the hedge ratio is given by
h = H FE/FF (518)
which generally is not a whole number. Therefore, it is (approximately, within
the desired precision) represented as a ratio h≈ NF /NE with the lowest possible
denominator NE, where NF and NE are whole numbers. Then the hedge consists of
buying NF gas futures contracts for every NE sold electricity futures contracts.
15 Distressed Assets
15.1 Strategy: Buying and holding distressed debt
Distressed securities are those whose issuers are undergoing ﬁnancial/operational
distress, default or bankruptcy. One deﬁnition of distressed debt is if the spread
198 So, the spark spread measures a gross margin of a gas-ﬁred power plant excluding all other
costs for operation, maintenance, capital, etc. Also, if the power plant uses fuel other than natural
gas, then the corresponding spread has a diﬀerent name. For coal it is called “dark spread”; for
nuclear power it is called “quark spread”; etc. For some literature on energy spreads, energy
hedging and related topics, see, e.g., [Benth and Kettler, 2010], [Benth, Kholodnyi and Laurence,
2014], [Carmona and Durrleman, 2003], [Cassano and Sick, 2013], [Deng, Johnson and Sogomonian,
2001], [Edwards, 2009], [Elias, Wahab and Fang, 2016], [Emery and Liu, 2002], [Fiorenzani, 2006],
[Fusaro and James, 2005], [Hsu, 1998], [James, 2003], [Kaminski, 2004], [Li and Kleindorfer, 2009],
[Maribu, Galli and Armstrong, 2007], [Mart´ ınez and Torr´ o, 2018], [Wang and Min, 2013].
108
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 110

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
between the yields of Treasury bonds and those of the issuer is greater than some
preset number, e.g., 1,000 basis points (see, e.g., [Harner, 2008]). A common and
simple distressed debt passive trading strategy amounts to buying debt of a dis-
tressed company at a steep discount, 199 expecting (hoping) that the company will
repay its debt. Typically, a distressed debt portfolio is diversiﬁed across industries,
entities and debt seniority level. It is anticipated that only a small fraction of the
held assets will have positive returns, but those that do, will provide high rates of
return (see, e.g., [Greenhaus, 1991]). There are two broad categories of passive dis-
tressed debt strategies (see, e.g., [Altman and Hotchkiss, 2006]). First, using various
models (see Subsection 15.3) one can attempt to predict whether a company will
declare bankruptcy. Second, some strategies focus on assets of companies in default
or bankruptcy, a successful reorganization being the driver of returns. Typically,
positions are established at key dates, such as at the end of the default month or at
the end of the bankruptcy-ﬁling month, with the view of exploiting overreaction in
the distressed debt market (see, e.g., [Eberhart and Sweeney, 1992], [Gilson, 1995]).
15.2 Strategy: Active distressed investing
This strategy amounts to buying distressed assets with the view (unlike the passive
strategy discussed above) to acquire some degree of control of the management and
direction of the company. When facing a distress situation, a company has various
options in its reorganization process. It can ﬁle for bankruptcy protection under
Chapter 11 of the U.S. Bankruptcy Code to reorganize. Or it can work directly
with its creditors out of Court. 200 Below are some scenarios for active investing.
15.2.1 Strategy: Planning a reorganization
An investor can submit a reorganization plan to Court with an objective to obtain
participation in the management of the company, attempt to increase its value and
generate proﬁts. Plans by signiﬁcant debt holders tend to be more competitive.
15.2.2 Strategy: Buying outstanding debt
This strategy amounts to buying outstanding debt of a distressed ﬁrm at a discount
with the view that, after reorganization, part of this debt will be converted into the
ﬁrm’s equity thereby giving the investor a certain level of control of the company.
199 For some pertinent literature, see, e.g., [Altman, 1998], [Clark and Weinstein, 1983], [Eberhart,
Altman and Aggarwal, 1999], [Friewald, Jankowitsch and Subrahmanyam, 2012], [Gande, Altman
and Saunders, 2010], [Gilson, 2010], [Gilson, 2012], [Harner, 2011], [Hotchkiss and Mooradian,
1997], [Jiang, Li and Wang, 2012], [Lhabitant, 2002], [Morse and Shaw, 1988], [Moyer, Martin and
Martin, 2012], [Putnam, 1991], [Quintero, 1989], [Reiss and Phelps, 1991], [Volpert, 1991].
200 For some literature, see, e.g., [Altman and Hotchkiss, 2006], [Chatterjee, Dhillon and Ram´ ırez,
1996], [Gilson, 1995], [Gilson, John and Lang, 1990], [Jostarndt and Sautner, 2010], [Levy, 1991],
[Markwardt, Lopez and DeVol, 2016], [Peri´ c, 2015], [Rosenberg, 1992], [Swank and Root, 1995],
[Ward and Griepentrog, 1993].
109
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 111

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
15.2.3 Strategy: Loan-to-own
This strategy amounts to ﬁnancing (via secured loans) a distressed ﬁrm that is not
bankrupt with the view that it i) overcomes the distress situation, avoids bankruptcy
and increases its equity value, or ii) ﬁles for Chapter 11 protection and, upon reor-
ganization, the secured loan is converted into the ﬁrm’s equity with control rights.
15.3 Strategy: Distress risk puzzle
Some studies suggest that companies more prone to bankruptcy oﬀer higher returns,
which is a form of a risk premium (see, e.g., [Chan and Chen, 1991], [Fama and
French, 1992], [Fama and French, 1996], [Vassalou and Xing, 2004]). However, more
recent studies suggest the opposite, i.e., that such companies do not outperform
healthier ones, and that the latter actually oﬀer higher returns. This is the so-called
“distress risk puzzle” (see, e.g., [George and Hwang, 2010], [Godfrey and Brooks,
2015], [Griﬃn and Lemmon, 2002], [Ozdagli, 2010]). So, this strategy amounts to
buying the safest companies and selling the riskiest ones. As a proxy, one can use the
probability of bankruptcy Pi, i = 1, . . . , N (N is the number of stocks), which can,
e.g., be modeled via a logistic regression (see, e.g., [Campbell, Hilscher and Sziglayi,
2008]).201 A zero-cost portfolio can be constructed by, e.g., selling the stocks in the
top decile by Pi, and buying the stocks in the bottom decile. Typically, the portfolio
is rebalanced monthly, but annual rebalancing is also possible (with similar returns).
15.3.1 Strategy: Distress risk puzzle – risk management
This strategy is a variation of the distress risk puzzle strategy in Subsection 15.3.
Empirical studies suggest that zero-cost healthy-minus-distressed (HMD) strategies
tend to have a high time-varying market beta, which turns signiﬁcantly negative
following market downturns (usually associated with increased volatility), which
can cause large losses if the market bounces abruptly (see, e.g., [Garlappi and Yan,
2011], [O’Doherty, 2012], [Opp, 2017]). This is similar to what happens in other
201 For some literature on models for estimating bankruptcy probabilities, explanatory variables
and related topics, see, e.g., [Alaminos, del Castillo and Fern´ andez, 2016], [Altman, 1968], [Altman,
1993], [Aretz and Pope, 2013], [Beaver, 1966], [Beaver, McNichols and Rhie, 2005], [Bellovary,
Giacomino and Akers, 2007], [Brezigar-Masten and Masten, 2012], [Callej´ onet al, 2013], [Chaudhuri
and De, 2011], [Chava and Jarrow, 2004], [Chen et al, 2011], [Cultrera and Br´ edart, 2015], [Dichev,
1998], [Duﬃe, Saita and Wang, 2007], [DuJardin, 2015], [El Kalak and Hudson, 2016], [Fedorova,
Gilenko and Dovzhenko, 2013], [Ferreira, Grammatikos and Michala, 2016], [Gordini, 2014], [Griﬃn
and Lemmon, 2002], [Hensher and Jones, 2007], [Hillegeist et al , 2004], [Jo, Han and Lee, 1997],
[Jonsson and Fridson, 1996], [Korol, 2013], [Laitinen and Laitinen, 2000], [McKee and Lensberg,
2002], [Min, Lee and Han, 2006], [Mossman et al, 1998], [Odom and Sharda, 1990], [Ohlson, 1980],
[Philosophov and Philosophov, 2005], [Pindado, Rodrigues and de la Torre, 2008], [Podobnik et
al, 2010], [Ribeiro et al , 2012], [Shin and Lee, 2002], [Shumway, 2001], [Slowinski and Zopounidis,
1995], [Tinoco and Wilson, 2013], [Tsai, Hsu and Yen, 2014], [Wilson and Sharda, 1994], [Woodlock
and Dangol, 2014], [Yang, You and Ji, 2011], [Zhou, 2013], [Zmijewski, 1984].
110
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 112

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
factor-based strategies.202 To mitigate this, the strategy can be modiﬁed as follows
(see, e.g., [Eisdorfer and Misirli, 2015]):
HMD∗ = σtarget
ˆσ HMD (519)
Here: HMD is for the standard HMD strategy in Subsection 15.3; σtarget is the
level of target volatility (typically, between 10% and 15%, depending on the trader
preferences); andˆσ is the estimated realized volatility over the prior year using daily
data. So, 100% of the investment is allocated only ifˆσ = σtarget, and a lower amount
is allocated when ˆσ > σtarget. When ˆσ < σtarget, the strategy could be leveraged. 203
16 Real Estate
16.1 Generalities
Real estate, unlike most other ﬁnancial assets, is tangible. It can be divided into two
main groups: commercial (oﬃces, shopping centers, etc.) and residential (houses,
apartments, etc.) real estate. There are various ways to get exposure to real estate,
e.g., via real estate investment trusts (REITs), which often trade on major exchanges
and allow investors to take a liquid stake in real estate. 204 There are several ways
to measure a return from a real estate investment. A common and simple way is as
follows:
R(t1, t2) = P (t2) + C(t1, t2)
P (t1) − 1 (520)
Here: R(t1, t2) is the return of the investment from the beginning of the holding
period t1 to the end of the holding period t2; P (t1) and P (t2) are the market values
of the property at those times; C(t1, t2) is the cash ﬂows received, net of costs. 205
16.2 Strategy: Mixed-asset diversiﬁcation with real estate
Real estate assets are attractive as a tool for diversiﬁcation. Empirical studies
suggest that their correlation with traditional assets, such as bonds and stocks, is
low and remains such even through extreme market events (e.g., ﬁnancial crises),
202 See, e.g., [Barroso and Santa-Clara, 2014], [Blitz, Huij and Martens, 2011], [Daniel and
Moskowitz, 2016].
203 Or, more simply, 100% of the investment could be allocated without leverage, in which case
the prefactor in Eq. (519) is min( σtarget/ˆσ, 1) instead.
204 REITs are in a sense similar to mutual funds as they provide a way for individual investors
to acquire ownership in income-generating real estate portfolios.
205 For some literature, see, e.g., [Block, 2011], [Eldred, 2004], [Geltner, Rodriguez and O’Connor,
1995], [Goetzmann and Ibbotson, 1990], [Hoesli and Lekander, 2008], [Hudson-Wilson et al , 2005],
[Larkin, Babin and Rose, 2004], [Mazurczak, 2011], [Pivar, 2003], [Steinert and Crowe, 2001].
111
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 113

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
when the correlations between traditional assets tend to increase. In addition, the
correlation tends to be lower at longer time horizons, so long-term investors may
improve their portfolio performance in terms of risk-adjusted returns by including
real estate assets (see, e.g., [Feldman, 2003], [Geltner et al, 2006], [Seiler, Webb and
Myer, 1999], [Webb, Curcio and Rubens, 1988]). So, a simple strategy amounts to
buying and holding real estate assets within a traditional portfolio containing, e.g.,
bonds, equities, etc. The optimal allocation varies depending on investor preferences
(in terms of risk and return) and the horizon (see, e.g., [Geltner, Rodriguez and
O’Connor, 1995], [Lee and Stevenson, 2005], [Mueller and Mueller, 2003], [Rehring,
2012]), and techniques such as mean-variance optimization or vector autoregressive
model (VAR)206 can be used to calculate the optimal allocation conditional on the
time horizon and desired performance characteristics (see, e.g., [Fugazza, Guidolin
and Nicodano, 2007], [Hoevenaars et al, 2008], [MacKinnon and Al Zaman, 2009]).
16.3 Strategy: Intra-asset diversiﬁcation within real estate
This strategy amounts to diversifying real estate holdings (which can be part of
a larger portfolio as in Subsection 16.2). Real estate assets can be diversiﬁed by
geographic area, type of property, size, proximity to a metropolitan area, economic
region, etc. (see, e.g., [Eichholtz et al , 1995], [Hartzell, Hekman and Miles, 1986],
[Hartzell, Shulman and Wurtzebach, 1987], [Hudson-Wilson, 1990], [Seiler, Webb
and Myer, 1999], [Viezer, 2000]). Various standard portfolio construction techniques
(such as those mentioned in Subsection 16.2) can be applied to determine allocations.
16.3.1 Strategy: Property type diversiﬁcation
This strategy amounts to investing in real estate assets of diﬀerent types, e.g.,
apartments, oﬃces, industrial properties (which include manufacturing buildings
and property), shopping centers, etc. Empirical studies suggest that property type
diversiﬁcation can be beneﬁcial for non-systematic risk reduction after taking into
account transaction costs (see, e.g., [Firstenberg, Ross and Zisler, 1988], [Grissom,
Kuhle and Walther, 1987], [Miles and McCue, 1984], [Mueller and Laposa, 1995]).
16.3.2 Strategy: Economic diversiﬁcation
This strategy amounts to diversifying real estate investments by diﬀerent regions
divided according to economic characteristics such as the main economic activity,
employment statistics, average income, etc. Empirical studies suggest that such di-
versiﬁcation can reduce non-systematic risk and transaction costs (see, e.g., [Hartzell,
Shulman and Wurtzebach, 1987], [Malizia and Simons, 1991], [Mueller, 1993]).
206 For some literature on the VAR approach, see, e.g., [Barberis, 2000], [Campbell, 1991], [Camp-
bell, Chan and Viceira, 2003], [Campbell and Viceira, 2004], [Campbell and Viceira, 2005], [Kandel
and Stambaugh, 1987], [Sørensen and Trolle, 2005].
112
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 114

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
16.3.3 Strategy: Property type and geographic diversiﬁcation
This strategy combines diversiﬁcation based on more than one attribute, e.g., prop-
erty type and region. Thus, if we consider four property types, to wit, oﬃce, retail,
industrial and residential, and four U.S. regions, to wit, East, Midwest, South, and
West, we can diversify across the resultant 16 groups (see, e.g., [Viezer, 2000]). 207
16.4 Strategy: Real estate momentum – regional approach
This strategy amounts to buying real estate properties based on their past re-
turns. Empirical evidence suggests that there is a momentum eﬀect across the U.S.
metropolitan statistical areas (MSAs), i.e., areas with higher (lower) past returns
tend to continue to deliver higher (lower) returns in the future (see, e.g., [Beracha
and Downs, 2015], [Beracha and Skiba, 2011]). In some cases, a zero-cost strategy
can be constructed, e.g., by using alternative real estate vehicles such as REITs, and
futures and options on U.S. housing indices based on diﬀerent geographical areas.208
16.5 Strategy: Inﬂation hedging with real estate
Empirical studies suggest a strong relationship between the real estate returns and
inﬂation rate. Therefore, real estate can be used as a hedge against inﬂation. Fur-
ther, empirically, some property types (e.g., commercial real estate, which tends to
adjust faster to inﬂationary price increases) appear to provide a better hedge than
others, albeit this can depend on various aspects such as the sample, market, etc. 209
207 For some additional pertinent literature, see, e.g., [De Wit, 2010], [Ertugrul and Giambona,
2011], [Gatzlaﬀ and Tirtiroglu, 1995], [Hartzell, Eichholtz and Selender, 2007], [Hastings and
Nordby, 2007], [Ross and Zisler, 1991], [Seiler, Webb and Myer, 1999], [Worzala and Newell, 1997].
208 For some literature on real estate momentum strategies (including using REITs and other
investment vehicles mentioned above) and related topics, see, e.g., [Abraham and Hendershott,
1993], [Abraham and Hendershott, 1996], [Anglin, Rutherford and Springer, 2003], [Buttimer,
Hyland and Sanders, 2005], [Caplin and Leahy, 2011], [Capozza, Hendershott and Mack, 2004],
[Case and Shiller, 1987], [Case and Shiller, 1989], [Case and Shiller, 1990], [Chan, Hendershott and
Sanders, 1990], [Chan, Leung and Wang, 1998], [Chen et al, 1998], [Cho, 1996], [Chui, Titman and
Wei, 2003a], [Chui, Titman and Wei, 2003b], [Cooper, Downs and Patterson, 1999], [Derwall et
al, 2009], [de Wit and van der Klaauw, 2013], [Genesove and Han, 2012], [Genesove and Mayer,
1997], [Genesove and Mayer, 2001], [Goebelet al, 2013], [Graﬀ, Harrington and Young, 1999], [Graﬀ
and Young, 1997], [Gupta and Miller, 2012], [Guren, 2014], [Haurin and Gill, 2002], [Haurin et al ,
2010], [Head, Lloyd-Ellis and Sun, 2014], [Kallberg, Liu and Trzcinka, 2000], [Kang and Gardner,
1989], [Karolyi and Sanders, 1998], [Knight, 2002], [Krainer, 2001], [Kuhle and Alvayay, 2000], [Lee,
2010], [Levitt and Syverson, 2008], [Li and Wang, 1995], [Lin and Yung, 2004], [Liu and Mei,
1992], [Malpezzi, 1999], [Meen, 2002], [Mei and Gao, 1995], [Mei and Liao, 1998], [Moss et al ,
2015], [Nelling and Gyourko, 1998], [Novy-Marx, 2009], [Ortalo-Magn´ e and Rady, 2006], [Piazzesi
and Schneider, 2009], [Peterson and Hsieh, 1997], [Poterba and Sinai, 2008], [Smith and Shulman,
1976], [Stein, 1995], [Stevenson, 2001], [Stevenson, 2002], [Taylor, 1999], [Titman and Warga, 1986],
[Wheaton, 1990], [Yavas and Yang, 1995], [Young and Graﬀ, 1996].
209 For some pertinent literature, see, e.g., [Bond and Seiler, 1998], [Fama and Schwert, 1977],
[Gunasekarage, Power and Zhou, 2008], [Hamelink and Hoesli, 1996], [Hartzell, Hekman and Miles,
113
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 115

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
16.6 Strategy: Fix-and-ﬂip
This is a short-term real estate investment strategy. It amounts to purchasing a
property, which typically is in a distressed condition and requires renovations, at a
(substantial) discount below market prices. The investor renovates the property and
resells it at a price high enough to cover the renovation costs and make a proﬁt. 210
17 Cash
17.1 Generalities
Cash is an asset, albeit at times its function as an asset might be overlooked or
taken for granted. As an asset, cash can be used in a variety of ways, e.g., i) as a
risk management tool , as it can help mitigate drawdowns and volatility; ii) as an
opportunity management tool , as it allows to take advantage of speciﬁc or unusual
situations; and iii) as a liquidity management tool in unexpected situations that
require liquid funds. There are several ways to include liquid funds in a portfolio,
e.g., via U.S. Treasury bills, bank deposit certiﬁcates (CDs), commercial paper,
banker’s acceptances, eurodollars, and repurchase agreements (a.k.a. repos), etc. 211
17.2 Strategy: Money laundering – the dark side of cash
Money laundering, broadly, is an activity wherein cash is used as a vehicle to trans-
form illegal proﬁts into legitimate-appearing assets. There are three main steps in a
money laundering process. The ﬁrst and the riskiest step is the placement, whereby
illegal funds are introduced into the legal economy via fraudulent means, e.g., by
dividing funds into small amounts and depositing them into multiple bank accounts
thereby avoiding detection. The second step, layering, involves moving the money
around between diﬀerent accounts and even countries thereby creating complexity
and separating the money from its source by several degrees. The third step is
integration, whereby money launderers get back the money via legitimate-looking
sources, e.g., cash-intensive businesses such as bars and restaurants, car washes, ho-
tels (at least in some countries), gambling establishments, parking garages, etc. 212
1987], [Le Moigne and Viveiros, 2008], [Mauer and Sebastian, 2002], [Miles and Mahoney, 1997],
[Newell, 1996], [Sing and Low, 2000], [Wurtzebach, Mueller and Machi, 1991].
210 For some pertinent literature, see, e.g., [Anacker, 2009], [Anacker and Schintler, 2015], [Bayer
et al , 2015], [Chinco and Mayer, 2012], [Corbett, 2006], [Depken, Hollans and Swidler, 2009],
[Depken, Hollans and Swidler, 2011], [Fu and Qian, 2014], [Hagopian, 1999], [Kemp, 2007], [Leung
and Tse, 2013], [Montelongo and Chang, 2008], [Villani and Davis, 2006].
211 For some literature, see, e.g., [Cook and LaRoche, 1993], [Cook and Rowe, 1986], [Damiani,
2012], [Duchin, 2010], [Goodfriend, 2011], [Schaede, 1990], [Summers, 1980], [Ysmailov, 2017].
212 For some literature, see, e.g., [Ardizzi et al , 2014], [Cox, 2015], [Gilmour and Ridley, 2015],
[Hopton, 1999], [John and Brigitte, 2009], [Kumar, 2012], [Levi and Reuter, 2006], [Schneider and
Windischbauer, 2008], [Seymour, 2008], [Soudijn, 2016], [Walker, 1999], [Wright et al , 2017].
114
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 116

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
17.3 Strategy: Liquidity management
From a portfolio management perspective, this strategy amounts to optimally deﬁn-
ing the amount of cash to be held in the portfolio to meet liquidity demands gen-
erated by unforeseen events. 213 Cash provides immediate liquidity, whereas other
assets would have to be liquidated ﬁrst, which can be associated with substantial
transaction costs, especially if liquidation is abrupt.214 From a corporate perspective,
holding cash can be a precautionary measure aimed at avoiding cash ﬂow shortfalls
that can yield, inter alia, loss of investment opportunities, ﬁnancial distress, etc. 215
17.4 Strategy: Repurchase agreement (REPO)
A repurchase agreement (REPO) is a cash-equivalent asset that provides immediate
liquidity at a preset interest rate for a speciﬁc period of time in exchange for another
asset used as a collateral. A reverse repurchase agreement is the opposite. So, a
REPO strategy amounts to borrowing (lending) cash with interest in exchange for
securities with the commitment of repurchasing them from (reselling them to) the
counterparty. This type of a transaction typically spans from 1 day to 6 months. 216
17.5 Strategy: Pawnbroking
REPOs are in some sense similar to much more ancient pawnbroking strategies. A
pawnbroker extends a secured cash loan with pre-agreed interest and period (which
can sometimes be extended). The loan is secured with a collateral, which is some
valuable item(s), such as jewelry, electronics, vehicles, rare books or musical instru-
ments, etc. If the loan is not repaid with interest as agreed, then the collateral is
forfeited by the borrower and the pawnbroker can keep it or sell it. The amount of
loan typically is at a signiﬁcant discount to the appraised value of the collateral. 217
213 Note that this is not necessarily the same reason for holding cash as that behind Kelly
strategies. For some pertinent literature, see, e.g., [Browne, 2000], [Cover, 1984], [Davis and Lleo,
2012], [Hsieh and Barmish, 2015], [Hsieh, Barmish and Gubner, 2016], [Kelly, 1956], [Laureti, Medo
and Zhang, 2010], [Lo, Orr and Zhang, 2017], [Maslov and Zhang, 1998], [Nekrasov, 2014], [Rising
and Wyner, 2012], [Samuelson, 1971], [Thorp, 2006], [Thorp and Kassouf, 1967].
214 For some literature, see, e.g., [Agapova, 2011b], [Aragon et al , 2017], [Cao et al , 2013],
[Chernenko and Sunderam, 2016], [Connor and Leland, 1995], [Jiang, Li and Wang, 2017], [Kruttli,
Monin and Watugala, 2018], [Leland and Connor, 1995], [Simutin, 2014], [Yan, 2006].
215 For some literature on corporate aspects of liquidity management and related topics, see,
e.g., [Acharya, Almeida and Campello, 2007], [Almeida, Campello and Weisbach, 2005], [Azmat
and Iqbal, 2017], [Chidambaran, Fernando and Spindt, 2001], [Disatnik, Duchin and Schmidt,
2014], [Froot, Scharfstein and Stein, 1993], [Han and Qiu, 2007], [Opler et al , 1999], [Sher, 2014].
216 See, e.g., [Adrian et al , 2013], [Bowsher, 1979], [Duﬃe, 1996], [Garbade, 2004], [Gorton and
Metrick, 2012], [Happ, 1986], [Kraenzlin, 2007], [Lumpkin, 1987], [Ruchin, 2011], [Schatz, 2012],
[Simmons, 1954], [Sollinger, 1994], [Zhang, Fargher and Hou, 2018].
217 In Section 9 we discussed trading strategies based on commodity futures. Pawnbrokers,
among other things, trade physical commodities such as silver and gold. For some literature on
pawnbroking and related topics, see, e.g., [Bos, Carter and Skiba, 2012], [Bouman and Houtman,
115
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 117

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
17.6 Strategy: Loan sharking
Unlike pawnbroking, loan sharking in many jurisdictions is illegal. Loan sharking
consists of oﬀering a loan at excessively high interest rates. Such a loan is not
necessarily secured by a collateral. Instead, a loan shark can sometimes resort to
blackmail and/or violence to enforce the terms of a loan (see, e.g., [Aldohni, 2013]).
18 Cryptocurrencies
18.1 Generalities
Cryptocurrencies, such as Bitcoin (BTC), Ethereum (ETH), etc., unlike traditional
ﬁat currencies (USD, EUR, etc.), are decentralized digital currencies based on open-
source peer-to-peer (P2P) internet protocols. Cryptocurrencies such as BTC and
ETH use the blockchain technology [Nakamoto, 2008]. 218 Total market capital-
ization of cryptocurrencies is measured in hundreds of billions of dollars. 219 Many
investors are attracted to cryptocurrencies as speculative buy-and-hold assets. Thus,
some view them as diversiﬁers due to their low correlation with traditional assets.
Others perceive them as the future of money. Some investors simply want to make
a quick buck on a speculative bubble. Etc. 220 Be it as it may, unlike, e.g., stocks,
there are no evident “fundamentals” for cryptoassets based on which one could build
“fundamental” trading strategies (e.g., value-based strategies). So, cryptocurrency
trading strategies tend to rely on trend data mining via machine learning techniques.
18.2 Strategy: Artiﬁcial neural network (ANN)
This strategy uses ANN to forecast short-term movements of BTC based on input
technical indicators. In ANN we have an input layer, an output layer, and some
1988], [Caskey, 1991], [D’Este, 2014], [Fass and Francis, 2004], [Maaravi and Levy, 2017], [McCants,
2007], [Shackman and Tenney, 2006], [Zhou et al , 2016].
218 Blockchain is a distributed ledger, which keeps a record of all transactions. It is a sequential
chain of blocks, which are linked using cryptography and time-stamping, containing transaction
records. No block can be altered retroactively without altering all subsequent blocks, which renders
blockchain resistant to data modiﬁcation by its very design. For a blockchain maintained by a large
network as a distributed ledger continuously updated on a large number of systems simultaneously,
collusion of the network majority would be required for a nefarious modiﬁcation of blockchain.
219 Cryptocurrencies are highly volatile, so their market cap has substantial time variability.
220 For some pertinent literature, see, e.g., [Baek and Elbeck, 2014], [Bariviera et al , 2017],
[Bouoiyour, Selmi and Tiwari, 2015], [Bouoiyour et al , 2016], [Bouri et al , 2017a], [Bouri et al ,
2017b], [Brandvold et al , 2015], [Bri` ere, Oosterlinck and Szafarz, 2015], [Cheah and Fry, 2015],
[Cheung, Roca and Su, 2015], [Ciaian, Rajcaniova and Kancs, 2015], [Donier and Bouchaud, 2015],
[Dowd and Hutchinson, 2015], [Dyhrberg, 2015], [Dyhrberg, 2016], [Eisl, Gasser and Weinmayer,
2015], [Fry and Cheah, 2016], [Gajardo, Kristjanpoller and Minutolo, 2018], [Garcia and Schweitzer,
2015], [Garcia et al, 2014], [Harvery, 2014], [Harvey, 2016], [Kimet al, 2016], [Kristoufek, 2015], [Lee,
Guo and Wang, 2018], [Liew, Li and Budav´ ari, 2018], [Ortisi, 2016], [Van Alstyne, 2014], [Wang
and Vergne, 2017], [White, 2015].
116
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 118

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
number of hidden layers. So, in this strategy the input layer is built using technical
indicators.221 E.g., we can use (exponential) moving averages ((E)MAs), (exponen-
tial) moving standard deviations ((E)MSDs), relative strength index (RSI), 222 etc.
More concretely, we can construct the input layer as follows (see, e.g., [Nakano,
Takahashi and Takahashi, 2018]). Let P (t) be the BTC price at time t, where
t = 1, 2, . . . is measured in some units (e.g., 15-minute intervals; also, t = 1 is the
most recent time). Let:
R(t) = P (t)
P (t + 1)− 1 (521)
˜R(t, T1) = R(t)− R(t, T1) (522)
R(t, T1) = 1
T1
t+T1∑
t′=t+1
R(t′) (523)
ˆR(t, T1) =
˜R(t, T1)
σ(t, T1) (524)
[σ(t, T1)]2 = 1
T1− 1
t+T1∑
t′=t+1
[˜R(t, T1)]2 (525)
So: R(t) is the return from t + 1 to t; R(t, T1) is the serial mean return from t + T1
to t + 1, i.e., over T1 periods, where T1 can be chosen to be long enough to provide a
reasonable estimate for the volatility (see below); ˜R(t, T1) is the serially demeaned
return; σ(t, T1) is the volatility computed from t + T1 to t + 1; and ˆR(t, T1) is the
normalized (serially demeaned) return. Below, for notational simplicity we will omit
the reference to the T1 parameter and will useˆR(t) to denote the normalized returns.
Next, we can deﬁne EMAs, EMSDs and RSI as follows: 223
EMA(t, λ, τ) = 1− λ
1− λτ
t+τ∑
t′=t+1
λt′−t−1 ˆR(t′) (526)
[EMSD(t, λ, τ)]2 = 1− λ
λ− λτ
t+τ∑
t′=t+1
λt′−t−1 [ˆR(t′)− EMA(t, λ, τ)]2 (527)
RSI(t, τ) = ν+(t, τ)
ν+(t, τ) + ν−(t, τ) (528)
ν±(t, τ) =
t+τ∑
t′=t+1
max(±ˆR(t′), 0) (529)
Here: τ is the moving average length; λ is the exponential smoothing parameter. 224
221 Thus, in spirit, it is somewhat similar to the single-stock KNN trading strategy discussed in
Subsection 3.17, which utilizes the k-nearest neighbor (KNN) algorithm (as opposed to ANN).
222 Typically, RSI> 0.7 (< 0.3) is interpreted as overbought (oversold). See, e.g., [Wilder, 1978].
223 Note that this can be done in more than one way.
224 To reduce the number of parameters, we can, e.g., take λ = (τ− 1)/(τ + 1).
117
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 119

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
The input layer can then be deﬁned as consisting of, e.g., ˆR(t), EMA(t, λa, τa),
EMSD(t, λa, τa), and RSI( t, τ′
a′), where a = 1, . . . , m, a′ = 1, . . . , m′. The values τa
can, e.g., be chosen to correspond to 30 min, 1 hr, 3 hrs and 6 hrs (so m = 4; see fn.
224 for the values of λa). The values τ′
a′ can, e.g., be chosen to correspond to 3 hrs,
6 hrs and 12 hrs (so m′ = 3). There is no magic bullet here. These values can be
chosen based on out-of-sample backtests keeping in mind, however, the ever-present
danger of over-ﬁtting various free parameters (see below), including τa, λa and τ′
a′.
The output layer can be constructed as follows. Let the objective be to forecast
which quantile the future normalized return will belong to. Let the number of
quantiles be K. Thus, for the values of t corresponding to the training dataset
Dtrain,225 we have the normalized returns ˆR(t), t∈ Dtrain. Let the ( K− 1) quantile
values of ˆR(t), t∈ Dtrain, be qα, α = 1 , . . . ,(K− 1). For each value of t, we can
deﬁne the supervisory K-vectors Sα(t), α = 1, . . . , K, as follows:



S1(t) = 1, ˆR(t)≤ q1
Sα(t) = 1, q α−1≤ ˆR(t) < qα, 1 < α < K
SK(t) = 1, q K−1≤ ˆR(t)
Sα(t) = 0, otherwise
(530)
The output layer can then be a nonnegative K-vector pα(t), whose elements are
interpreted as the probabilities of the future normalized return to be in the α-th
quantile. So, we have
K∑
α=1
pα(t) = 1 (531)
The output layer is constructed from the input layer as some nonlinear function
thereof with some number of parameters to be determined via training. In ANN we
have L layers labeled by ℓ = 1, . . . , L, where ℓ = 1 corresponds to the input layer,
and ℓ = L corresponds to the output layer. At each layer we have N (ℓ) nodes and
the corresponding N (ℓ)-vectors ⃗X(ℓ) with components X(ℓ)
i(ℓ), i(ℓ) = 1, . . . , N(ℓ):226
X(ℓ)
i(ℓ) = h(ℓ)
i(ℓ)(⃗Y (ℓ)), ℓ = 2, . . . , L (532)
Y (ℓ)
i(ℓ) =
N (ℓ−1)
∑
j(ℓ−1)=1
A(ℓ)
i(ℓ)j(ℓ−1) X(ℓ−1)
j(ℓ−1) + B(ℓ)
i(ℓ) (533)
Here: ⃗Y (ℓ) is an N (ℓ)-vector with components Y (ℓ)
i(ℓ), i(ℓ) = 1 , . . . , N(ℓ); X(1)
i(1) are
the input data (for each value of t, i.e., ˆR(t), EMA( t, λa, τa), EMSD( t, λa, τa), and
RSI(t, τ′
a′) – see above); X(L)
i(L) are the output data pα(t) (i.e., N (L) = K and the index
225 Ideally, when computing the quantiles, an appropriate number d1 of the values of t =
td,td−1,...,t d−d1+1, d =|Dtrain|, should be excluded to ensure that all the EMA, EMSD and
RSI values are computed using the required numbers of datapoints.
226 We suppress the time variable t for the sake of notational simplicity.
118
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 120

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
i(L) is the same as α); the unknown parameters A(ℓ)
i(ℓ)j(ℓ−1) (the so-called weights) and
B(ℓ)
i(ℓ) (the so-called bias) are determined via training (see below); and there is much
arbitrariness in terms of picking the values of N (ℓ) and the so-called activation
functions h(ℓ)
i(ℓ). A possible choice (out of myriad others) is as follows (see, e.g.,
[Nakano, Takahashi and Takahashi, 2018]):227
h(ℓ)
i(ℓ)(⃗Y (ℓ)) = max
(
Y (ℓ)
i(ℓ) , 0
)
, ℓ = 2, . . . , L− 1 (ReLU) (534)
h(L)
i(L)(⃗Y (L)) = Y (L)
i(L)


N (L)
∑
j(L)=1
Y (L)
j(L)


−1
(softmax) (535)
I.e., ReLU is used at the hidden layers (and the algorithm moves onto the next layer
only if some neurons are activated (ﬁred) at layer ℓ, i.e., at least some Y (ℓ)
i(ℓ) > 0),
and softmax is used at the output layer (so that we have the condition (531) by con-
struction). Further, to train the model, i.e., to determine the unknown parameters,
some kind of error function E (we suppress its variables) must be minimized, e.g.,
the so-called cross-entropy (see, e.g., [de Boer et al, 2005]):
E =−
∑
t∈Dtrain
K∑
α=1
Sα(t) ln( pα(t)) (536)
To minimize E, one can, e.g., use the stochastic gradient descent (SGD) method,
which minimizes the error function iteratively until the procedure converges. 228
Finally, we must specify the trading rules. There are a number of possibilities
here depending on the number of quantiles, i.e., the choice of K. A reasonable
trading signal is given by:
Signal =
{
Buy, iﬀ max( pα(t)) = pK(t)
Sell, iﬀ max( pα(t)) = p1(t) (537)
Therefore, the trader buys BTC if the predicted class is pK(t) (the top quantile),
and sells if it is p1(t) (the bottom quantile). This trading rule can be modiﬁed. E.g.,
the buy signal can be based on the top 2 quantiles, and the sell signal can be based
on the bottom 2 quantiles (see, e.g., [Nakano, Takahashi and Takahashi, 2018]). 229
227 Again, there is no magic bullet here. A priori, a host of activation functions can be used,
e.g., sigmoid (a.k.a. logistic), tanh (hyperbolic tangent), rectiﬁed linear unit (ReLU), softmax, etc.
For some pertinent literature, see, e.g., [Bengio, 2009], [Chandra, 2003], [da S. Gomes, Ludermir
and Lima, 2011], [Glorot, Bordes and Bengio, 2011], [Goodfellow et al , 2013], [Karlik and Vehbi,
2011], [Mhaskar and Micchelli, 1993], [Singh and Chandra, 2003], [Wu, 2009].
228 A variety of methods can be used. For some pertinent literature, see, e.g., [Denton and Hung,
1996], [Dong and Zhou, 2008], [Dreyfus, 1990], [Ghosh, 2012], [Kingma and Ba, 2014], [Ruder,
2017], [Rumelhart, Hinton and Williams, 1986], [Schmidhuber, 2015], [Wilson et al , 2018].
229 Various techniques used in applying ANNs to other asset classes such as equities may also be
useful for cryptocurrencies. See, e.g., [Ballings et al , 2015], [Chong, Han and Park, 2017], [Dash
and Dash, 2016], [de Oliveira, Nobre and Z´ arate, 2013], [Sezer, Ozbayoglu and Dogdu, 2017], [Yao,
Tan and Poh, 1999]. For some additional literature, see fn. 61.
119
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 121

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
18.3 Strategy: Sentiment analysis – na¨ ıve Bayes Bernoulli
Social media sentiment analysis based strategies have been used in stock trading 230
and also applied to cryptocurrency trading. The premise is to use a machine learning
classiﬁcation scheme to forecast, e.g., the direction of the BTC price movement based
on tweet data. This entails collecting all tweets containing at least one keyword from
a pertinent (to BTC price forecasting) learning vocabulary V over some timeframe,
and cleaning this data. 231 The resultant data is then further processed by assigning
a so-called feature ( M-vector) Xi to each tweet labeled by i = 1, . . . , N, where N
is the number of tweets in the dataset. Here M =|V| is the number of keywords
in the learning vocabulary V . So, the components of each vector Xi are Xia, where
a = 1, . . . , M labels the words in V . Thus, if the word wa∈ V labeled by a is not
present in the tweet Ti labeled by i, then Xia = 0. If wa is present in Ti, then we can
set Xia = 1 or Xia = nia, where nia counts the number of times wa appears in Ti.
In the former case (which is what we focus on in the following) we have a Bernoulli
probability distribution, while in the latter case we have a multinomial distribution.
Next, we need to build a model that, given the N feature vectors Xi, predicts
one out of a preset number K of outcomes (so-called classes) Cα, α = 1 , . . . , K.
E.g., we can have K = 2 outcomes, whereby BTC is forecasted to go up or down,
which can be used as the buy/sell signal. Alternatively, as in the ANN strategy
in Subsection 18.2, we can have K quantiles for the normalized returns ˆR(t). Etc.
This then deﬁnes our trading rules. Once the classes Cα are chosen, a simple way
to forecast them is to build a model for conditional probabilities P (Cα|X1, . . . , XN).
Here, generally, P (A|B) denotes the conditional probability of A occurring assuming
B is true. Pursuant to Bayes’ theorem, we have
P (A|B) = P (B|A) P (A)
P (B) (538)
where P (A) and P (B) are the probabilities of A and B occurring independently of
each other. So, we have
P (Cα|X1, . . . , XN) = P (X1, . . . , XN|Cα) P (Cα)
P (X1, . . . , XN) (539)
Note that P (X1, . . . , XN) is independent of Cα and will not be important below.
Now, P (Cα) can be estimated from the training data. The primary diﬃculty is in
230 For some literature, see, e.g., [Bollen and Mao, 2011], [Bollen, Mao and Zeng, 2011], [Kordonis,
Symeonidis and Arampatzis, 2016], [Liew and Budav´ ari, 2016], [Mittal and Goel, 2012], [Nisar and
Yeung, 2018], [Pagolu et al , 2016], [Rao and Srivastava, 2012], [Ruan, Durresi and Alfantoukh,
2018], [Sprenger et al , 2014], [Sul, Dennis and Yuan, 2017]), [Zhang, Fuehres and Gloor, 2011].
231 This, among other things, includes removing duplicate tweets likely generated by ubiquitous
Twitter bots, removing the so-called stop-words (e.g., “the”, “is”, “in”, “which”, etc.), which do
not add value, from the tweets, and performing the so-called stemming, i.e., reducing words to
their base form (e.g., “investing” and “invested” are reduced to “invest”, etc.). The latter can be
achieved using, e.g., the Porter stemming algorithm or other similar algorithms (for some literature,
see, e.g., [Hull, 1996], [Porter, 1980], [Raulji and Saini, 2016], [Willett, 2006]).
120
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 122

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
estimating P (X1, . . . , XN|Cα). Here a simpliﬁcation occurs if we make the “na¨ ıve”
conditional independence assumption (hence the term “na¨ ıve Bayes”), i.e., that,
given the class Cα, for all i the feature Xi is conditionally independent of every
other feature Xj, j = 1, . . . , N (j̸= i):
P (Xi|Cα, X1, . . . , Xi−1, Xi+1, . . . , XN) = P (Xi|Cα) (540)
Then Eq. (539) simpliﬁes as follows:
P (Cα|X1, . . . , XN) = γ P (Cα)
N∏
i=1
P (Xi|Cα) (541)
γ = 1/P (X1, . . . , XN) (542)
The conditional probabilities P (Xi|Cα) can be estimated using the conditional prob-
abilities P (wa|Cα) for the M words wa in the learning vocabulary V :
P (Xi|Cα) =
M∏
a=1
Qiaα (543)
Qiaα = P (wa|Cα), X ia = 1 (544)
Qiaα = 1− P (wa|Cα), X ia = 0 (545)
The conditional probabilities P (wa|Cα) can simply be estimated based on the occur-
rence frequencies of the words wa in the training data. Similarly, the probabilities
P (Cα) can be estimated from the training data. 232 So, if we set the forecasted value
Cpred of the outcome to that with the maximum P (Cα|X1, . . . , XN), then
Cpred = argmaxCα∈{1,...,K}P (Cα)
N∏
i=1
M∏
a=1
[P (wa|Cα)]Xia[1− P (wa|Cα)]1−Xia (546)
19 Global Macro
19.1 Generalities
Actually, macro trading strategies constitute an investment style, not an asset class.
These types of strategies are not limited to any particular asset class or a geographi-
cal region and can invest in stocks, bonds, currencies, commodities, derivatives, etc.,
232 For some literature on applying Twitter sentiment to Bitcoin trading, see, e.g., [Colianni,
Rosales and Signorotti, 2015], [Georgoula et al , 2015], which also discuss other machine learning
methods such as support vector machines (SVM) and logistic regression (a.k.a. logit model). For
some literature on Bitcoin trading using other sentiment data, see, e.g., [Garcia and Schweitzer,
2015], [Li et al , 2018]. For some literature on applying tree boosting algorithms to cryptocurrency
trading, see, e.g., [Alessandretti et al, 2018], [Li et al, 2018]. For some additional pertinent literature
(which generally appears to be relatively scarce for BTC compared with similar literature on stock
trading), see, e.g., [Amjad and Shah, 2017], [Jiang and Liang, 2017], [Shah and Zhang, 2014].
121
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 123

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
seeking to capitalize on regional, economic and political changes around the world.
While many macro strategies are based on analysts’ subjective opinions (these are
discretionary strategies), a systematic approach (non-discretionary strategies) also
plays a prominent role. Global macro strategies can vary by their style, e.g., there
are directional strategies, long-short strategies, relative value strategies, etc. 233
19.2 Strategy: Fundamental macro momentum
This strategy aims to capture returns from the market underreaction to changes
in macroeconomic trends by buying (selling) assets favored (adversely aﬀected) by
incoming macroeconomic trends. Diﬀerent asset classes can be used in building
an investment portfolio, e.g., global equity indexes, currencies, government bonds,
etc.234 The “state variables” to consider are the business cycle, international trade,
monetary policy, and risk sentiment trends (see, e.g., [Brooks, 2017]).235 E.g., equity
indexes from some number of countries are ranked using the values of the aforesaid
4 state variables for each country. 236 A zero-cost portfolio can then be constructed
by, e.g., going long the indexes in the top decile and shorting those in the bottom
decile. The so-constructed portfolios for various asset classes can, e.g., be combined
with equal weights. Typically, the holding period ranges from three to six months.
19.3 Strategy: Global macro inﬂation hedge
Exogenous shocks (such as a political or geopolitical issue) can have an impact
on commodity prices such as oil leading to an increase in prices in oil-dependent
economies. There are two steps in this process: (i) a pass-through from commodity
prices to the headline inﬂation (HI), and (ii) then, a pass-through from HI to the
core inﬂation (CI). 237 I.e., HI quickly reﬂects various shocks around the world. So,
233 Macro strategies can be divided into 3 classes: discretionary macro, systematic macro, and
CTA/managed futures. For some literature on macro strategies and related topics, see, e.g.,
[Asgharian et al , 2004], [Chung, 2000], [Connor and Woo, 2004], [Dobson, 1984], [Drobny, 2006],
[Fabozzi, Focardi and Jonas, 2010], [Fung and Hsieh, 1999], [Gliner, 2014], [Kidd, 2014], [Lambert,
Papageorgiou and Platania, 2006], [Potjer and Gould, 2007], [Stefanini, 2006], [Zaremba, 2014].
234 Diﬀerent asset classes are aﬀected by the same macroeconomic trends diﬀerently. E.g., in-
creasing growth is positive for equities and currencies, but negative for bonds.
235 Business cycle trends can be estimated using 1-yr changes in the real GDP growth and CPI
inﬂation forecast, each contributing with a 50% weight. International trade trends can be estimated
using 1-yr changes in spot FX rates against an export-weighted basket. Monetary policy trends can
be estimated using 1-yr changes in short-term rates. Risk sentiment trends can be estimated using
1-yr equity market excess returns. For some literature on the rationale behind these variables, see,
e.g., [Bernanke and Kuttner, 2005], [Clarida and Waldman, 2007], [Eichenbaum and Evans, 1995].
236 There is a variety of ways to do this ranking using the 4 variables. See, e.g., Subsection 3.6.
237 HI is the raw inﬂation measured by indices such as the Consumer Price Index (CPI) based on
prices of goods and services in a broad basket, while CI excludes some products such as commodi-
ties, which are highly volatile and add sizable noise to the index. For some pertinent literature, see,
e.g., [Blanchard and Gali, 2007], [Blanchard and Riggi, 2013], [Clark and Terry, 2010], [Hamilton,
2003], [Marques, Neves and Sarmento, 2003], [Trehan, 2005], [van den Noord and Andr´ e, 2004].
122
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 124

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
the global macro inﬂation hedge strategy is based on the spread between HI and CI
as an indicator to hedge inﬂation using commodities: 238
CA = max
(
0, min
(HIYoY − CIYoY
HIYoY
, 1
))
(547)
Here: CA is the commodity allocation percentage within the portfolio, and “YoY”
stands for “year-on-year”. The hedge can be executed by, e.g., buying a basket of
various commodities through ETFs, futures, etc. (see, e.g., [Fulli-Lemaire, 2013]).
19.4 Strategy: Global ﬁxed-income strategy
This systematic macro trading strategy is based on a cross-sectional analysis of
government bonds from various countries using variables such as (see, e.g., [Br¨ uck
and Fan, 2017]) GDP, inﬂation, sovereign risk, real interest rate, output gap, value,
momentum, term spread, and the so-called Cochrane-Piazzesi predictor [Cochrane
and Piazzesi, 2005]. Thus, said bonds can be ranked based on these factors and a
zero-cost portfolio can be constructed by buying bonds in the top quantile and selling
bonds in the bottom quantile. Similarly to Subsection 3.6, multifactor portfolios can
also be constructed. Typically, country-bond ETFs are used in such portfolios. 239
19.5 Strategy: Trading on economic announcements
Empirical evidence suggests that stocks tend to yield higher returns on important
announcement dates such Federal Open Market Committee (FOMC) announce-
ments.240 So, a simple macro trading strategy consists of buying stocks on impor-
tant announcement days (ADs), such as the FOMC announcements, and switching
to risk-free assets during non-announcement days (NDAs). This is done via ETFs,
futures, etc., as opposed to individual stocks, as the strategy involves moving from
100% allocated in equities to 100% allocated in Treasuries (see, e.g., [Stotz, 2016]).241
20 Infrastructure
Broadly, investing in infrastructure includes investing in long-term projects such as
transportation (roads, bridges, tunnels, railways, ports, airports, etc.), telecommuni-
238 For some literature on using commodities as an inﬂation hedge, see, e.g., [Amenc, Martellini
and Ziemann, 2009], [Bodie, 1983], [Bodie and Rosansky, 1980], [Greer, 1978], [Hoevenaars et al ,
2008], [Jensen, Johnson and Mercer, 2002].
239 For some literature on factor investing in ﬁxed-income assets, see, e.g., [Beekhuizenet al, 2016],
[Correia, Richardson and Tuna, 2012], [Houweling and van Vundert, 2017], [Koijen, Moskowitz,
Pedersen and Vrugt, 2018], [L’Hoir and Boulhabel, 2010], [Staal et al , 2015].
240 For some pertinent literature, see, e.g., [Ai and Bansal, 2016], [Bernanke and Kuttner, 2005],
[Boyd, Hu and Jagannathan, 2005], [Donninger, 2015], [Graham, Nikkinen and Sahlstr¨ om, 2003],
[Jones, Lamont and Lumsdaine, 1998], [Lucca and Moench, 2012], [Savor and Wilson, 2013].
241 This strategy can be augmented with various (e.g., technical) ﬁlters (see, e.g., [Stotz, 2016]).
123
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 125

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
cations (transmission cables, satellites, towers, etc.), utilities (electricity generation,
gas or electricity transmission or distribution, water supply, sewage, waste, etc.), en-
ergy (including but not limited to renewable energy), healthcare (hospitals, clinics,
senior homes, etc.), educational facilities (schools, universities, research institutes,
etc.), etc. An investor can gain exposure to infrastructure assets through diﬀerent di-
rect or indirect investments such private equity-type investments (e.g., via unlisted
infrastructure funds), listed infrastructure funds, stocks of publicly traded infras-
tructure companies, municipal bonds earmarked to infrastructure projects, etc. 242
Infrastructure investments, by their nature, are long-term, buy-and-hold invest-
ments. One investment strategy is to use infrastructure assets to improve risk-
adjusted returns of well-diversiﬁed portfolios, e.g., via tracking ETFs, global infras-
tructure funds, unlisted infrastructure funds, etc. 243 Another investment strategy is
to use infrastructure assets for inﬂation hedging.244 Yet another investment strategy
is to generate stable cash ﬂows from infrastructure investments. For this purpose,
“brownﬁeld” projects (associated with established assets in need of improvement)
are more appropriate than “greenﬁeld” projects (associated with assets to be con-
structed). Diversiﬁcation across diﬀerent sectors can be beneﬁcial in this regard. 245
Acknowledgments
JAS would like to thank Juli´ an R. Siri for valuable discussions.
242 For some literature on infrastructure as an asset class and related topics, see, e.g., [Ansar et
al, 2016], [Bitsch, Buchner and Kaserer, 2010], [Blanc-Brude, Hasan and Whittaker, 2016], [Blanc-
Brude, Whittaker and Wilde, 2017], [Blundell, 2006], [Clark, 2017], [Clarket al, 2012], [Finkenzeller,
Dechant and Sch¨ afers, 2010], [Grigg, 2010], [Grimsey and Lewis, 2002], [Hartigan, Prasad and De
Francesco, 2011], [Helm, 2009], [Helm and Tindall, 2009], [Herranz-Lonc´ an, 2007], [Inderst, 2010a],
[McDevitt and Kirwan, 2008], [Newell, Chau and Wong, 2009], [Newell and Peng, 2008], [Peng
and Newell, 2007], [Ramamurti and Doh, 2004], [Rickards, 2008], [Sanchez-Robles, 1998], [Sawant,
2010a], [Sawant, 2010b], [Singhal, Newell and Nguyen, 2011], [Smit and Trigeorgis, 2009], [Torrance,
2007], [Vives, 1999], [Weber, Staub-Bisang and Alfen, 2016], [Wurstbauer et al , 2016].
243 See, e.g., [Dechant and Finkenzeller, 2013], [Haran et al , 2011], [Joshi and Lambert, 2011],
[Martin, 2010], [Nartea and Eves, 2010], [Newell, Peng and De Francesco, 2011], [Oyedele, Adair
and McGreal, 2014], [Panayiotou and Medda, 2016], [Rothballer and Kaserer, 2012].
244 Infrastructure, as real estate, can be an inﬂation-hedging investment, albeit apparently with
some heterogeneity. For some literature, see, e.g., [Armann and Weisdorf, 2008], [Bird, Liem and
Thorp, 2014], [Inderst, 2010b], [Wurstbauer and Sch¨ afers, 2015], [R¨ odel and Rothballer, 2012].
245 For some pertinent literature, see, e.g., [Arezki and Sy, 2016], [Espinoza and Luccioni, 2002],
[Leigland, 2018], [Panayiotou and Medda, 2014], [Weber, Adair and McGreal, 2008].
124
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 126

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
A R Source Code for Backtesting
In this appendix we give the R (R Package for Statistical Computing, http://www.
r-project.org) source code for backtesting intraday strategies, where the posi-
tion is established at the open and liquidated at the close of the same day. The
sole purpose of this code is to illustrate some simple tricks for doing out-of-sample
backtesting. In particular, this code does not deal with the survivorship bias in any
way,246 albeit for this kind of strategies – precisely because these are intraday strate-
gies – the survivorship bias is not detrimental (see, e.g., [Kakushadze, 2015b]). 247
The main function (which internally calls some subfunctions) is qrm.backtest()
with the following inputs: (i) days is the lookback; (ii) d.r is used for computing
risk, both as the length of the moving standard deviation tr (computed internally
over d.r-day moving windows) as well as the lookback for computing the risk model
(and, if applicable, a statistical industry classiﬁcation) – see below; (iii) d.addv is
used as the lookback for the average daily dollar volume addv, which is computed
internally; (iv) n.addv is the number of top tickers by addv used as the trading
universe, which is recomputed every d.r days; (v) inv.lvl is the total investment
level (long plus short, and the strategy is dollar-neutral); (vi) bnds controls the
position bounds (which are the same in this strategy as the trading bounds), i.e.,
the dollar holdings Hi for each stock are bounded via ( Bi are the bnds elements,
which can be uniform)
|Hi|≤ Bi Ai (548)
where i = 1, . . . , N labels the stocks in the trading universe, and Ai are the corre-
sponding elements of addv; (vii) incl.cost is a Boolean for including linear trading
costs, which are modeled as follows. 248 For the stock labeled by i, let Ei be its
expected return, and wi be its weight in the portfolio. The source code below deter-
mines wi via (mean-variance) optimization (with bounds). For the stock labeled by
i, let the linear trading cost per dollar traded be τi. Including such costs in portfolio
optimization amounts to replacing the expected return of the portfolio
Eport =
N∑
i=1
Ei wi (549)
by
Eport =
N∑
i=1
[Ei wi− τi|wi|] (550)
246 I.e., simply put, it does not account for the fact that in the past there were tickers that are
no longer there at present, be it due to bankruptcies, mergers, acquisitions, etc. Instead, the input
data is taken for the tickers that exist on a given day by looking back, say, some number of years.
247 For some literature related to the survivorship bias, which is important for longer-horizon
strategies, see, e.g., [Amin and Kat, 2003], [Brown et al , 1992], [Bu and Lacey, 2007], [Carhart et
al, 2002], [Davis, 1996], [Elton, Gruber and Blake, 1996b], [Garcia and Gould, 1993].
248 Here we closely follow the discussion in Subsection 3.1 of [Kakushadze and Yu, 2018b].
125
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 127

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
A complete algorithm for including linear trading costs in mean-variance optimiza-
tion is given in, e.g., [Kakushadze, 2015b]. However, for our purposes here the
following simple “hack” suﬃces. We can deﬁne the eﬀective return
Eeff
i = sign(Ei) max(|Ei|− τi, 0) (551)
and simply set
Eport =
N∑
i=1
Eeff
i wi (552)
I.e., if the magnitude for the expected return for a given stock is less than the
expected cost to be incurred, we set the expected return to zero, otherwise we
reduce said magnitude by said cost. This way we can avoid a nontrivial iterative
procedure (see, e.g., [Kakushadze, 2015b]), albeit this is only an approximation.
So, what should we use as τi in (551)? The model of [Almgren et al , 2005] is
reasonable for our purposes here. Let Hi be the dollar amount traded for the stock
labeled by i. Then for the linear trading costs we have
Ti = ζ σi
|Hi|
Ai
(553)
where σi is the historical volatility, Ai is the average daily dollar volume (ADDV),
and ζ is an overall normalization constant we need to ﬁx. However, above we work
with weights wi, not traded dollar amounts Hi. In our case of a purely intraday
trading strategy discussed above, they are related simply via Hi = I w i, where I
is the total investment level (i.e., the total absolute dollar holdings of the portfolio
after establishing it). Therefore, we have (note that Ti = τi|Hi| = τi I|wi|)
τi = ζ σi
Ai
(554)
We will ﬁx the overall normalizationζ via the following heuristic. We will (conserva-
tively) assume that the average linear trading cost per dollar traded is 10 bps (1 bps
= 1 basis point = 1/100 of 1%),249 i.e., mean(τi) = 10−3 and ζ = 10−3/mean(σi/Ai).
Next, internally the code sources price and volume data by reading it from tab-
delimited ﬁles 250 nrm.ret.txt (overnight return internally referred to as ret – see
below), nrm.open.txt (daily raw, unadjusted open price, internally referred to as
open), nrm.close.txt (daily raw, unadjusted close price, internally referred to as
close), nrm.vol.txt (daily raw, unadjusted volume, internally referred to as vol),
nrm.prc.txt (daily close price fully adjusted for all splits and dividends, internally
referred to as prc). The rows of ret, open, close, vol and prc correspond to the N
tickers (index i). Let trading days be labeled by t = 0, 1, 2, . . . , T, where t = 0 is the
249 This amounts to assuming that, to establish an equally-weighted portfolio, it costs 10 bps.
250 This speciﬁc code does not use high, low, VWAP (volume-weighted average price), intraday
(e.g., minute-by-minute) prices, etc. However, it is straightforward to modify it such that it does.
126
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 128

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
most recent day. Then the columns of open, close, vol and prc correspond to the
trading days t = 1, 2, . . . , T, i.e., the value of t is the same as the value of the column
index. On the other hand, the columns of ret correspond to the overnight close-to-
open returns from the trading day t to the trading day t− 1. I.e., the ﬁrst column
of ret corresponds to the overnight close-to-open return from the trading day t = 1
to the trading day t = 0. Furthermore, ret, call it Ri(t), where t = 1, 2, . . . , T labels
the columns of ret, is computed as follows:
Ri(t) = ln
( PAO
i (t− 1)
PAC
i (t)
)
(555)
PAO
i (t) = γadj
i (t) PO
i (t) (556)
γadj
i (t) = PAC
i (t)
PC
i (t) (557)
Here: PO
i (t) is the raw open price (which is the corresponding element of open for
t = 1 , 2, . . . , T); PC
i (t) is the raw close price (which is the corresponding element
of close for t = 1, 2, . . . , T); PAC
i (t) is the fully adjusted close price (which is the
corresponding element of prc for t = 1, 2, . . . , T); γadj
i (t) is the adjustment factor,
which is used for computing the fully adjusted open price PAO
i (t); so Ri(t) is the
overnight, close-to-open return based on fully adjusted prices. Note that the t = 0
prices required for computing Ri(1) are not part of the matrices open, close and
prc. Also, the code internally assumes that the matrices ret, open, close, vol
and prc are all aligned, i.e., all tickers and dates are the same and in the same
order in each of the 5 ﬁles nrm.ret.txt (note the labeling of the returns described
above), nrm.open.txt, nrm.close.txt, nrm.vol.txt and nrm.prc.txt. The ordering
of the tickers in these ﬁles is immaterial, so long as it is the same in all 5 ﬁles as
the code is oblivious to this ordering. However, the dates must be ordered in the
descending order, i.e., the ﬁrst column corresponds to the most recent date, the
second column corresponds to the date before it, etc. (here “date” corresponds to a
trading day). Finally, note that the internal function read.x() reads these ﬁles with
the parameter value as.is = T . This means that these ﬁles are in the “R-ready”
tab-delimited format, with N + 1 tab-delimited lines. The lines 2 through N + 1
have T + 1 elements each, the ﬁrst element being a ticker symbol (so the N ticker
symbols comprise dimnames(·)[[1]] of the corresponding matrix, e.g., open for the
open prices), and the other T elements being the T values (e.g., PO
i (t), t = 1, . . . , T,
for the open prices). However, the ﬁrst line has only T elements, which are the labels
of the trading days (so these comprisedimnames(·)[[2]] of the corresponding matrix,
e.g., open for the open prices). Internal functions that use this input data, such as
calc.mv.avg() (which computes simple moving averages) and calc.mv.sd() (which
computes simple moving standard deviations) are simple and self-explanatory.
As mentioned above, the input parameterd.r is used for recomputing the trading
universe every d.r trading days and also recomputing the risk models (see below)
every d.r trading days. These computations are done 100% out-of-sample, i.e., the
127
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 129

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
data used in these computations is 100% in the past w.r.t. to the trading day on
which the resultant quantities are used for (simulated) trading. This is accomplished
in part by using the internal function calc.ix(). Note that the input data described
above is structured and further used in such a way that the backtests are 100% out-
of-sample. Here two conceptually diﬀerent aspects must be distinguished. Thus,
we have the expected returns and “the rest”, the latter – which can be loosely
referred to as “risk management” – being the universe selection, the risk model
computation, etc., i.e., the machinery that gets us from the expected returns to
the desired holdings (that is, the strategy positions). The risk management part
must be 100% out-of-sample. In real life the expected returns are also 100% out-
of-sample. However, in backtesting, while the expected returns cannot under any
circumstances look into the future, they can sometimes be “borderline in-sample”.
Thus, consider a strategy that today trades on the overnight yesterday’s-close-to-
today’s-open return. If we assume that the positions are established based on this
return sometime after the open, then the backtest is out-of-sample by the “delay”
time between the open and when the position is established. However, if we assume
that the position is established at the open, then this is the so-called “delay-0”
strategy, and the backtest is “borderline in-sample” in the sense that in real life the
orders would have to be sent with some, albeit possibly small, delay, but could never
be executed exactly at the open. In this sense it still makes sense to backtest such
a strategy to measure the strength of the signal. What would make no sense and
should never be done is to run an outright in-sample backtest that looks into the
future. E.g., using today’s closing prices for computing expected returns for trading
at today’s open would be grossly in-sample. On the other hand, using yesterday’s
prices to trade at today’s open is the so-called “delay-1” strategy, which is basically
1 day out-of-sample (and, not surprisingly, is expected to backtest much worse than
a delay-0 strategy). The code gives examples of both delay-0 (mean-reversion) and
delay-1 (momentum) strategies (see the commentsDELAY-0 and DELAY-1 in the code).
The code internally computes the desired holdings via optimization. The op-
timizer function (which incorporates bounds and linear constraints such as dollar-
neutrality) bopt.calc.opt() is given in [Kakushadze, 2015e]. One of its inputs is
the inverse model covariance matrix for the stocks. This matrix is computed inter-
nally via functions such as qrm.cov.pc() and qrm.erank.pc(), which are given in
and utilize the statistical risk model construction of [Kakushadze and Yu, 2017a],
or qrm.gen.het(), which is given in and utilizes the heterotic risk model construc-
tion of [Kakushadze and Yu, 2016a]. The latter requires a multilevel binary in-
dustry classiﬁcation. The code below builds such a classiﬁcation via the function
qrm.stat.ind.class.all(), which is given in and utilizes the statistical industry
classiﬁcation construction of [Kakushadze and Yu, 2016b]. However, the code can
be straightforwardly modiﬁed to utilize a fundamental industry classiﬁcation, such as
GICS (Global Industry Classiﬁcation Standard), BICS (Bloomberg Industry Clas-
siﬁcation System), SIC (Standard Industrial Classiﬁcation), etc. One issue with
this is that practically it is diﬃcult to do this 100% out-of-sample. However, “in-
128
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 130

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
sampleness” of a fundamental industry classiﬁcation – which is relatively stable –
typically does not pose a serious issue in such backtests as stocks rarely jump indus-
tries. Furthermore, note that the aforesaid “external” functions have various other
parameters (which are set to their implicit default values in the code below), which
can be modiﬁed (see the references above that provide the aforesaid functions).
Finally, the code internally computes the desired holdings and various perfor-
mance characteristics such as the total P&L over the backtesting period, annualized
return, annualized Sharpe ratio, and cents-per-share. These and other quantities
computed internally can be returned (e.g., via environments or lists), dumped into
ﬁles, printed on-screen, etc. The code is straightforward and can be tweaked depend-
ing on the user’s speciﬁc needs/strategies. Its purpose is illustrative/pedagogical.
qrm.backtest <- function (days = 252 * 5, d.r = 21, d.addv = 21,
n.addv = 2000, inv.lvl = 2e+07, bnds = .01, incl.cost = F)
{
calc.ix <- function(i, d, d.r)
{
k1 <- d - i
k1 <- trunc(k1 / d.r)
ix <- d - k1 * d.r
return(ix)
}
calc.mv.avg <- function(x, days, d.r)
{
y <- matrix(0, nrow(x), days)
for(i in 1:days)
y[, i] <- rowMeans(x[, i:(i + d.r - 1)])
return(y)
}
calc.mv.sd <- function(x, days, d.r)
{
y <- matrix(0, nrow(x), days)
for(i in 1:days)
y[, i] <- apply(x[, i:(i + d.r - 1)], 1, sd)
return(y)
}
read.x <- function(file)
{
129
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 131

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
x <- read.delim(file, as.is = T)
x <- as.matrix(x)
mode(x) <- "numeric"
return(x)
}
calc.sharpe <- function (pnl, inv.lvl)
{
print(sum(pnl, na.rm = T))
print(mean(pnl, na.rm = T) * 252 / inv.lvl * 100)
print(mean(pnl, na.rm = T) / sd(pnl, na.rm = T) * sqrt(252))
}
ret <- read.x("nrm.ret.txt")
open <- read.x("nrm.open.txt")
close <- read.x("nrm.close.txt")
vol <- read.x("nrm.vol.txt")
prc <- read.x("nrm.prc.txt")
addv <- calc.mv.avg(vol * close, days, d.addv)
ret.close <- log(prc[, -ncol(prc)]/prc[, -1])
tr <- calc.mv.sd(ret.close, days, d.r)
ret <- ret[, 1:days]
prc <- prc[, 1:days]
close <- close[, 1:days]
open <- open[, 1:days]
close1 <- cbind(close[, 1], close[, -ncol(close)])
open1 <- cbind(close[, 1], open[, -ncol(open)])
pnl <- matrix(0, nrow(ret), ncol(ret))
des.hold <- matrix(0, nrow(ret), ncol(ret))
for(i in 1:ncol(ret))
{
ix <- calc.ix(i, ncol(ret), d.r)
if(i == 1)
prev.ix <- 0
if(ix != prev.ix)
{
liq <- addv[, ix]
x <- sort(liq)
130
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 132

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
x <- x[length(x):1]
take <- liq >= x[n.addv]
r1 <- ret.close[take, (ix:(ix + d.r - 1))]
### ind.list <- qrm.stat.ind.class.all(r1,
### c(100, 30, 10), iter.max = 100)
### rr <- qrm.gen.het(r1, ind.list)
rr <- qrm.cov.pc(r1)
### rr <- qrm.erank.pc(r1)
cov.mat <- rr$inv.cov
prev.ix <- ix
}
w.int <- rep(1, sum(take))
ret.opt <- ret ### DELAY-0 MEAN-REVERSION
### ret.opt <- -log(close/open) ### DELAY-1 MOMENTUM
if(incl.cost)
{
lin.cost <- tr[take, i] / addv[take, i]
lin.cost <- 1e-3 * lin.cost / mean(lin.cost)
}
else
lin.cost <- 0
ret.lin.cost <- ret.opt[take, i]
ret.lin.cost <- sign(ret.lin.cost) *
pmax(abs(ret.lin.cost) - lin.cost, 0)
des.hold[take, i] <- as.vector(bopt.calc.opt(ret.lin.cost, w.int,
cov.mat, bnds * liq[take]/inv.lvl, -bnds * liq[take]/inv.lvl))
des.hold[take, i] <- -des.hold[take, i] *
inv.lvl / sum(abs(des.hold[take, i]))
pnl[take, i] <- des.hold[take, i] *
(close1[take, i]/open1[take, i] - 1)
pnl[take, i] <- pnl[take, i] - abs(des.hold[take, i]) * lin.cost
131
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 133

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
}
des.hold <- des.hold[, -1]
pnl <- pnl[, -1]
pnl <- colSums(pnl)
calc.sharpe(pnl, inv.lvl)
trd.vol <- 2 * sum(abs(des.hold/open1[, -1]))
cps <- 100 * sum(pnl) / trd.vol
print(cps)
}
B DISCLAIMERS
Wherever the context so requires, the masculine gender includes the feminine and/or
neuter, and the singular form includes the plural and vice versa. The author of this
paper (“Author”) and his aﬃliates including without limitation Quantigic ® Solu-
tions LLC (“Author’s Aﬃliates” or “his Aﬃliates”) make no implied or express
warranties or any other representations whatsoever, including without limitation
implied warranties of merchantability and ﬁtness for a particular purpose, in con-
nection with or with regard to the content of this paper including without limitation
any code or algorithms contained herein (“Content”).
The reader may use the Content solely at his/her/its own risk and the reader
shall have no claims whatsoever against the Author or his Aﬃliates and the Author
and his Aﬃliates shall have no liability whatsoever to the reader or any third party
whatsoever for any loss, expense, opportunity cost, damages or any other adverse
eﬀects whatsoever relating to or arising from the use of the Content by the reader
including without any limitation whatsoever: any direct, indirect, incidental, spe-
cial, consequential or any other damages incurred by the reader, however caused
and under any theory of liability; any loss of proﬁt (whether incurred directly or
indirectly), any loss of goodwill or reputation, any loss of data suﬀered, cost of pro-
curement of substitute goods or services, or any other tangible or intangible loss;
any reliance placed by the reader on the completeness, accuracy or existence of the
Content or any other eﬀect of using the Content; and any and all other adversities
or negative eﬀects the reader might encounter in using the Content irrespective of
whether the Author or his Aﬃliates is or are or should have been aware of such
adversities or negative eﬀects.
Any information or opinions provided herein are for informational purposes only
and are not intended, and shall not be construed, as an investment, legal, tax or
any other such advice, or an oﬀer, solicitation, recommendation or endorsement of
any trading strategy, security, product or service, or any article, book or any other
publication referenced herein or any of the content contained therein.
132
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 134

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
The R code included in Appendix A hereof is part of the copyrighted R code
of Quantigic® Solutions LLC and is provided herein with the express permission of
Quantigic® Solutions LLC. The copyright owner retains all rights, title and interest
in and to its copyrighted source code included in Appendix A hereof and any and
all copyrights therefor.
133
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 135

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
References
Abken, P.A. (1989) An analysis of intra-market spreads in heating oil futures.
Journal of Futures Markets 9(1): 77-86.
Abken, P.A. and Nandi, S. (1996) Options and Volatility. Federal Reserve
Bank of Atlanta, Economic Review 81(3): 21-35.
Abraham, J.M. and Hendershott, P.H. (1993) Patterns and Determinants of
Metropolitan House Prices, 1977 to 1991. In: Browne, L.E. and Rosengren,
E.S. (eds.) Real Estate and the Credit Crunch. Boston, MA: Federal Reserve
Bank of Boston, pp. 18-42.
Abraham, J.M. and Hendershott, P.H. (1996) Bubbles in Metropolitan Hous-
ing Markets. Journal of Housing Research 7(2): 191-207.
Abreu, D. and Brunnermeier, M.K. (2002) Synchronization risk and delayed
arbitrage. Journal of Financial Economics 66(2-3): 341-360.
Accominotti, O. and Chambers, D. (2014) Out-of-Sample Evidence on the
Returns to Currency Trading. Working Paper. Available online: https://
ssrn.com/abstract=2293684.
Acharya, V.V., Almeida, H. and Campello, M. (2007) Is cash negative debt?
A hedging perspective on corporate ﬁnancial policies. Journal of Financial
Intermediation 16(4): 515-554.
Ackert, L.F. and Tian, Y.S. (2000) Arbitrage and valuation in the market
for Standard and Poor’s Depositary Receipts. Financial Management 29(3):
71-87.
Adam, F. and Lin, L.H. (2001) An Analysis of the Applications of Neural
Networks in Finance. Interfaces 31(4): 112-122.
Adams, Z. and Gl¨ uck, T. (2015) Financialization in commodity markets: A
passing trend or the new normal? Journal of Banking & Finance 60: 93-111.
Adrangi, B., Chatrath, A., Song, F. and Szidarovszky, F. (2006) Petroleum
spreads and the term structure of futures prices. Applied Economics 38(16):
1917-1929.
Adrian, T., Begalle, B., Copeland, A. and Martin, A. (2013) Repo and
Securities Lending. Federal Reserve Bank of New York Staﬀ Reports, No. 529.
Available online:
https://www.newyorkfed.org/medialibrary/media/research/staff_
reports/sr529.pdf.
134
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 136

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Adrian, T. and Wu, H. (2010) The Term Structure of Inﬂation Expectations.
Federal Reserve Bank of New York Staﬀ Reports , No. 362. Available online:
https://www.newyorkfed.org/medialibrary/media/research/staff_
reports/sr362.pdf.
Agapova, A. (2011a) Conventional mutual funds versus exchange-traded funds.
Journal of Financial Markets 14(2): 323-343.
Agapova, A. (2011b) The Role of Money Market Mutual Funds in Mutual
Fund Families. Journal of Applied Finance 21(1): 87-102.
Agarwal, V., Fung, W.H., Loon, Y.C. and Naik, N.Y. (2011) Risk and return
in convertible arbitrage: Evidence from the convertible bond market. Journal
of Empirical Finance 18(2): 175-194.
Ahmadi, H.Z., Sharp, P.A. and Walther, C.H. (1986) The eﬀectiveness of
futures and options in hedging currency risk. In: Fabozzi, F. (ed.) Advances
in Futures and Options Research , Vol. 1, Part B. Greenwich, CT: JAI Press,
Inc., pp. 171-191.
Ahmerkamp, J.D. and Grant, J. (2013) The Returns to Carry and Momentum
Strategies. Working Paper. Available online: https://ssrn.com/abstract=
2227387.
Ahn, D.-H., Boudoukh, J., Richardson, M. and Whitelaw, R.F. (2002) Partial
adjustment or stale prices? Implications from stock index and futures return
autocorrelations. Review of Financial Studies 15(2): 655-689.
Ahn, D.-H., Conrad, J. and Dittmar, R. (2003) Risk Adjustment and Trading
Strategies. Review of Financial Studies 16(2): 459-485.
Ai, H. and Bansal, R. (2016) Risk Preferences and the Macro Announcement
Premium. Working Paper. Available online: https://ssrn.com/abstract=
2827445.
Aiba, Y. and Hatano, N. (2006) A microscopic model of triangular arbitrage.
Physica A: Statistical Mechanics and its Applications 371(2): 572-584.
Aiba, Y., Hatano, N., Takayasu, H., Marumo, K. and Shimizu, T. (2002)
Triangular arbitrage as an interaction among foreign exchange rates. Physica
A: Statistical Mechanics and its Applications 310(3-4): 467-479.
Aiba, Y., Hatano, N., Takayasu, H., Marumo, K. and Shimizu, T. (2003)
Triangular arbitrage and negative auto-correlation of foreign exchange rates.
Physica A: Statistical Mechanics and its Applications 324(1-2): 253-257.
135
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 137

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
¨Aij¨ o, J. (2008) Implied volatility term structure linkages between VDAX,
VSMI and VSTOXX volatility indices. Global Finance Journal 18(3): 290-
302.
A¨ ıt-Sahalia, Y. and Duarte, J. (2003) Nonparametric option pricing under
shape restrictions. Journal of Econometrics 116(1-2): 9-47.
A¨ ıt-Sahalia, Y., Karaman, M. and Mancini, L. (2015) The Term Structure of
Variance Swaps and Risk Premia. Working Paper. Available online: https:
//ssrn.com/abstract=2136820.
Akram, Q.F., Rime, D. and Sarno, L. (2008) Arbitrage in the foreign exchange
market: Turning on the microscope. Journal of International Economics 76(2):
237-253.
Alaminos, D., del Castillo, A. and Fern´ andez, M. ´A. (2016) A Global Model
for Bankruptcy Prediction. PLoS ONE 11(11): e0166693.
Alaton, P., Djehiche, B. and Stillberger, D. (2010) On modelling and pricing
weather derivatives. Applied Mathematical Finance 9(1): 1-20.
Albeverio, S., Steblovskaya, V. and Wallbaum, K. (2013) Investment instru-
ments with volatility target mechanism. Quantitative Finance 13(10): 1519-
1528.
Albrecht, P. (1985) A note on immunization under a general stochastic equi-
librium model of the term structure. Insurance: Mathematics and Economics
4(4): 239-244.
Aldohni, A.K. (2013) Loan Sharks v. Short-term Lenders: How Do the Law
and Regulators Draw the Line? Journal of Law and Society 40(3): 420-449.
Aldridge, I. (2013) High-Frequency Trading: A Practical Guide to Algorithmic
Strategies and Trading Systems. (2nd ed.) Hoboken, NJ: John Wiley & Sons,
Inc.
Aldridge, I. (2016) ETFs, High-Frequency Trading, and Flash Crashes. Jour-
nal of Portfolio Management 43(1): 17-28.
Alessandretti, L., ElBahrawy, A., Aiello, L.M. and Baronchelli, A. (2018) Ma-
chine Learning the Cryptocurrency Market. Working Paper. Available online:
https://arxiv.org/pdf/1805.08550.pdf.
Alexander, C. and Korovilas, D. (2012) Understanding ETNs on VIX Futures.
Working Paper. Available online: https://ssrn.com/abstract=2043061.
Alexander, G.J. and Resnick, B.G. (1985) Using linear and goal programming
to immunize bond portfolios. Journal of Banking & Finance 9(1): 35-54.
136
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 138

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Allen, F. and Michaely, R. (1995) Dividend Policy. In: Jarrow, R.A., Mak-
simovic, V. and Ziemba, W.T. (eds.) Handbooks in Operations Research and
Management Science, Vol 9. Amsterdam, The Netherlands: Elsevier, Chapter
25, pp. 793-837.
Almeida, H., Campello, M. and Weisbach, M.S. (2005) The Cash Flow Sensi-
tivity of Cash. Journal of Finance 59(4): 1777-1804.
Almgren, R., Thum, C., Hauptmann, E. and Li, H. (2005) Equity market
impact. Risk Magazine 18(7): 57-62.
Altman, E.I. (1968) Financial Ratios, Discriminant Analysis and the Predic-
tion of Corporate Bankruptcy. Journal of Finance 23(4): 589-609.
Altman, E. (1993) Corporate ﬁnancial distress and bankruptcy. (2nd ed.)
Hoboken, NJ: John Wiley & Sons, Inc.
Altman, E.I. (1998) Market Dynamics and Investment Performance of Dis-
tressed and Defaulted Debt Securities. Working Paper. Available online:
https://ssrn.com/abstract=164502.
Altman, N.S. (1992) An introduction to kernel and nearest-neighbor nonpara-
metric regression. American Statistician 46(3): 175-185.
Altman, E.I., Brady, B., Resti, A. and Sironi, A. (2005) The link between de-
fault and recovery rates: theory, empirical evidence and implications. Journal
of Business 78(6): 2203-2228.
Altman, E.I. and Hotchkiss, E. (2006) Corporate Financial Distress and
Bankruptcy: Predict and Avoid Bankruptcy, Analyze and Invest in Distressed
Debt. Hoboken, NJ: John Wiley & Sons, Inc.
Amaitiek, O.F.S., B´ alint, T. and Reˇ sovsk´ y, M. (2010) The Short Call Ladder
strategy and its application in trading and hedging.Acta Montanistica Slovaca
15(3): 171-182.
Amato, J.D. and Gyntelberg, J. (2005) CDS Index Tranches and the Pricing
of Credit Risk Correlations. BIS Quarterly Review, December 2005, pp. 73-87.
Available online: https://www.bis.org/publ/qtrpdf/r_qt0503g.pdf.
Amato, J.D. and Remolona, E.M. (2003) The credit spread puzzle. BIS Quar-
terly Review, December 2003, pp. 51-63. Available online: https://www.bis.
org/publ/qtrpdf/r_qt0312e.pdf.
Ambrose, B., LaCour-Little, M. and Sanders, A. (2004) The Eﬀect of Con-
forming Loan Status on Mortgage Yield Spreads: A Loan Level Analysis. Real
Estate Economics 32(4): 541-569.
137
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 139

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Amenc, N., Ducoulombier, F., Goltz, F. and Ulahel, J. (2016) Ten Miscon-
ceptions about Smart Beta. Working Paper. Available online: https://www.
edhec.edu/sites/www.edhec-portail.pprod.net/files/publications/
pdf/edhec-position-paper-ten-misconceptions-about-smart-beta%
5F1468395239135-pdfjpg.
Amenc, N., Goltz, F., Sivasubramanian, S. and Lodh, A. (2015) Robustness
of Smart Beta Strategies. Journal of Index Investing 6(1): 17-38.
Amenc, N., Martellini, L. and Ziemann, V. (2009) Inﬂation-Hedging Properties
of Real Assets and Implications for Asset-Liability Management Decisions.
Journal of Portfolio Management 35(4): 94-110.
Amihud, Y. (2002) Illiquidity and stock returns: cross-section and time-series
eﬀects. Journal of Financial Markets 5(1): 31-56.
Amihud, Y. and Goyenko, R. (2013) Mutual Fund’s R2 as Predictor of Per-
formance. Review of Financial Studies 26(3): 667-694.
Amihud, Y. and Murgia, M. (1997) Dividends, Taxes, and Signaling: Evidence
from Germany. Journal of Finance 52(1): 397-408.
Amin, G.S. and Kat, H.M. (2003) Welcome to the Dark Side: Hedge Fund
Attrition and Survivorship Bias over the Period 1994-2001. Journal of Alter-
native Investments 6(1): 57-73.
Amiri, M., Zandieh, M., Vahdani, B., Soltani, R. and Roshanaei, V. (2010) An
integrated eigenvector-DEA-TOPSIS methodology for portfolio risk evaluation
in the FOREX spot market. Expert Systems with Applications 37(1): 509-516.
Amjad, M.J. and Shah, D. (2017) Trading Bitcoin and Online Time Series Pre-
diction. Working Paper. Available online: http://proceedings.mlr.press/
v55/amjad16.pdf.
Ammann, M., Kind, A. and Seiz, R. (2010) What drives the performance of
convertible-bond funds? Journal of Banking & Finance 34(11): 2600-2613.
Ammann, M., Kind, A. and Wilde, C. (2003) Are convertible bonds under-
priced? An analysis of the French market. Journal of Banking & Finance
27(4): 635-653.
An, B.-J., Ang, A., Bali, T.G. and Cakici, N. (2014) The Joint Cross Section
of Stocks and Options. Journal of Finance 69(5): 2279-2337.
Anacker, K.B. (2009) Big ﬂipping schemes in small cities? The case of Mans-
ﬁeld, Ohio. Housing and Society 36(1): 5-28.
138
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 140

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Anacker, K.B. and Schintler, L.A. (2015) Flip that house: visualising and
analysing potential real estate property ﬂipping transactions in a cold local
housing market in the United States. International Journal of Housing Policy
15(3): 285-303.
Anand, A. and Venkataraman, K. (2016) Market Conditions, Fragility, and
the Economics of Market Making. Journal of Financial Economics 121(2):
327-349.
Andersen, L. (1999) A Simple Approach to the Pricing of Bermudan Swaptions
in the Multi-factor Libor Market Model. Journal of Computational Finance
3(2): 5-32.
Andersen, L.B.G. (2010) Markov models for commodity futures: theory and
practice. Quantitative Finance 10(8): 831-854.
Andersen, L. and Sidenius, J. (2005) Extensions to the Gaussian Copula:
Random Recovery and Random Factor Loadings. Journal of Credit Risk 1(1):
29-70.
Andersen, L., Sidenius, J. and Basu, S. (2003) All your hedges in one basket.
Risk, November 2003, pp. 67-72.
Anderson, R.M., Bianchi, S.W. and Goldberg, L.R. (2014) Determinants of
Levered Portfolio Performance. Financial Analysts Journal 70(5): 53-72.
Anderson, R.W. and Danthine, J.P. (1981) Cross Hedging.Journal of Political
Economy 89(6): 1182-1196.
Andrade, G., Mitchell, M. and Staﬀord, E. (2001) New evidence and perspec-
tives on mergers. Journal of Economic Perspectives 15(2): 103-120.
Andrie¸ s, A.M. and Vˆ ırlan, C.A. (2017) Risk arbitrage in emerging Europe: are
cross-border mergers and acquisition deals more risky? Economic Research –
Ekonomska Istraˇ zivanja30(1): 1367-1389.
An´ e, T. and Labidi, C. (2001) Implied volatility surfaces and market activity
over time. Journal of Economics and Finance 25(3): 259-275.
Ang, S., Alles, L. and Allen, D. (1998) Riding the Yield Curve: An Analysis
of International Evidence. Journal of Fixed Income 8(3): 57-74.
Ang, A., Bekaert, G. and Wei, M. (2008) The Term Structure of Real Rates
and Expected Inﬂation. Journal of Finance 63(2): 797-849.
Ang, A., Green, R.C., Longstaﬀ, F.A. and Xing, Y. (2017) Advance Refund-
ings of Municipal Bonds. Journal of Finance 72(4): 1645-1682.
139
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 141

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Ang, A., Hodrick, R., Xing, Y. and Zhang, X. (2006) The Cross-Section of
Volatility and Expected Returns. Journal of Finance 61(1): 259-299.
Ang, A., Hodrick, R., Xing, Y. and Zhang, X. (2009) High Idiosyncratic
Volatility and Low Returns: International and Further U.S. Evidence.Journal
of Financial Economics 91(1): 1-23.
Ang, K.K. and Quek, C. (2006) Stock trading using RSPOP: A novel rough
set-based neuro-fuzzy approach.IEEE Transactions on Neural Networks17(5):
1301-1315.
Anglin, P.M., Rutherford, R. and Springer, T. (2003) The Trade-oﬀ Between
the Selling Price of Residential Properties and Time-on-the-Market: The Im-
pact of Price Setting. Journal of Real Estate Finance and Economics 26(1):
95-111.
Anker, P. (1999) Uncovered interest parity, monetary policy and time-varying
risk premia. Journal of International Money and Finance 18(6): 835-851.
Ankirchner, S., Dimitroﬀ, G., Heyne, G. and Pigorsch, C. (2012) Futures
Cross-Hedging with a Stationary Basis. Journal of Financial and Quantitative
Analysis 47(6): 1361-1395.
Ankirchner, S. and Heyne, G. (2012) Cross Hedging with Stochastic Correla-
tion. Finance and Stochastics 16(1): 17-43.
Ansar, A., Flyvbjerg, B., Budzier, A. and Lunn, D. (2016) Does infrastructure
investment lead to economic growth or economic fragility? Evidence from
China. Oxford Review of Economic Policy 32(3): 360-390.
Anson, M.J.P (1998) Spot Returns, Roll Yield, and Diversiﬁcation with Com-
modity Futures. Journal of Alternative Investments 1(3): 16-32.
Anson, M. (2013) Performance Measurement in Private Equity: The Impact
of FAS 157 on the Lagged Beta Eﬀect. Journal of Private Equity 17(1): 29-44.
Antonacci, G. (2014) Dual Momentum Investing: An Innovative Strategy for
Higher Returns with Lower Risk. New York, NY: McGraw-Hill, Inc.
Antonacci, G. (2017) Risk Premia Harvesting Through Dual Momentum.
Journal of Management & Entrepreneurship 11(1): 27-55.
Antoniou, A. and Holmes, P. (1995) Futures Trading, Information and Spot
Price Volatility: Evidence from the FTSE 100 Stock Index Futures Contract
using GARCH. Journal of Banking & Finance 19(1): 117-129.
140
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 142

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Aragon, G.O., Ergun, A.T., Getmansky, M. and Girardi, G. (2017) Hedge
Fund Liquidity Management. Working Paper. Available online: https://
ssrn.com/abstract=3033930.
Ardizzi, G., Petraglia, C., Piacenza, M., Schneider, F. and Turati, G. (2014)
Money Laundering as a Crime in the Financial Sector: A New Approach to
Quantitative Assessment, with an Application to Italy. Journal of Money,
Credit and Banking 46(8): 1555-1590.
Aretz, K. and Pope, P.F. (2013) Common factors in default risk across coun-
tries and industries. European Financial Management 19(1): 108-152.
Arezki, R. and Sy, A. (2016) Financing Africa’s Infrastructure Deﬁcit: From
Development Banking to Long-term Investing. Journal of African Economies
25(S2): 59-73.
Armann, V. and Weisdorf, M. (2008) Hedging Inﬂation with Infrastructure
Assets. In: Benaben, B. and Goldenberg, S. (eds.) Inﬂation Risk and Products:
The Complete Guide. London, UK: Risk Books, pp. 111-126.
Arnott, R., Chaves, D., Gunzberg, J., Hsu, J. and Tsui, P. (2014) Getting
Smarter about Commodities: An index to counter the possible pitfalls.Journal
of Indexes, November/December 2014, pp. 52-60.
Arnott, R.D., Hsu, J., Kalesnik, V. and Tindall, P. (2013) The Surprising Al-
pha from Malkiel’s Monkey and Upside-Down Strategies. Journal of Portfolio
Management 39(4): 91-105.
Arnsdorf, M. and Halperin, I. (2007) BSLP: Markovian bivariate spread-
loss model for portfolio credit derivatives. Working Paper. Available online:
https://arxiv.org/pdf/0901.3398.
Asem, E. and Tian, G. (2010) Market Dynamics and Momentum Proﬁts.Jour-
nal of Financial and Quantitative Analysis 45(6): 1549-1562.
Asgharian, M., Diz, F., Gregoriou, G.N. and Rouah, F. (2004) The Global
Macro Hedge Fund Cemetery. Journal of Derivatives Accounting 1(2): 187-
194.
Asgharian, H. and Karlsson, S. (2008) An Empirical Analysis of Factors Driv-
ing the Swap Spread. Journal of Fixed Income 18(2): 41-56.
Asness, C.S. (1994) Variables that Explain Stock Returns (Ph.D. Thesis).
Chicago, IL: University of Chicago.
Asness, C.S. (1995) The Power of Past Stock Returns to Explain Future Stock
Returns. Working Paper (unpublished). New York, NY: Goldman Sachs Asset
Management.
141
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 143

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Asness, C. (1997) The Interaction of Value and Momentum Strategies. Finan-
cial Analysts Journal 53(2): 29-36.
Asness, C., Frazzini, A., Israel, R. and Moskowitz, T. (2014) Fact, Fiction,
and Momentum Investing. Journal of Portfolio Management 40(5): 75-92.
Asness, C., Krail, R.J. and Liew, J.M. (2001) Do Hedge Funds Hedge?Journal
of Portfolio Management 28(1): 6-19.
Asness, C., Moskowitz, T. and Pedersen, L.H. (2013) Value and Momentum
Everywhere. Journal of Finance 68(3): 929-985.
Asness, C.S., Porter, R.B. and Stevens, R.L. (2000) Predicting Stock Returns
Using Industry-Relative Firm Characteristics. Working Paper. Available on-
line: https://ssrn.com/abstract=213872.
Augustin, P., Brenner, B. and Subrahmanyam, M.G. (2015) Informed Options
Trading prior to M&A Announcements: Insider Trading? Working Paper .
Available online: https://ssrn.com/abstract=2441606.
Aussenegg, W., G¨ otz, L. and Jelic, R. (2014) European asset swap spreads
and the credit crisis. European Journal of Finance 22(7): 572-600.
Avdjiev, S., Du, W., Koch, C. and Shin, H.S. (2016) The Dollar, Bank Lever-
age and the Deviation from Covered Interest Parity.Working Paper. Available
online: https://ssrn.com/abstract=2870057.
Avellaneda, M. and Lee, J.H. (2010) Statistical arbitrage in the U.S. equity
market. Quantitative Finance 10(7): 761-782.
Avellaneda, M. and Papanicolaou, A. (2018) Statistics of VIX Futures and
Applications to Trading Volatility Exchange-Traded Products. Journal of In-
vestment Strategies 7(2): 1-33.
Avellaneda, M. and Stoikov, S. (2008) High frequency trading in a limit order
book. Quantitative Finance 8(3): 217-224.
Avellaneda, M. and Zhang, S. (2010) Path-Dependence of Leveraged ETF
Returns. Journal on Financial Mathematics 1(1): 586-603.
Ayache, E., Forsyth, P.A. and Vetzal, K.R. (2003) Valuation of Convertible
Bonds With Credit Risk. Journal of Derivatives 11(1): 9-29.
Ayuso, J. and Restoy, F. (1996) Interest Rate Parity and Foreign Exchange
Risk Premia in the ERM. Journal of International Money and Finance 15(3):
369-382.
142
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 144

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Azmat, Q. and Iqbal, A.M. (2017) The role of ﬁnancial constraints on precau-
tionary cash holdings: evidence from Pakistan. Economic Research – Ekonom-
ska Istraˇ zivanja30(1): 596-610.
Baba, N. and Packer, F. (2009) Interpreting deviations from covered interest
parity during the ﬁnancial market turmoil of 2007-08. Journal of Banking &
Finance 33(11): 1953-1962.
Babbs, S.H. and Nowman, B.K. (1999) Kalman ﬁltering of generalized Vasicek
term structure models. Journal of Financial and Quantitative Analysis 34(1):
115-130.
Bacchetta, P. and van Wincoop, E. (2006) Incomplete Information Processing:
A Solution to the Forward Discount Puzzle.American Economic Review96(3):
552-576.
Bacchetta, P. and van Wincoop, E. (2010) Infrequent Portfolio Decisions: A
Solution to the Forward Discount Puzzle. American Economic Review 100(3):
870-904.
Baek, C. and Elbeck, M. (2014) Bitcoins as an Investment or Speculative
Vehicle? A First Look. Applied Economics Letters 22(1): 30-34.
Bai, Q., Bond, S.A. and Hatch, B.C. (2015) The Impact of Leveraged and In-
verse ETFs on Underlying Real Estate Returns. Real Estate Economics 43(1):
37-66.
Bai, J. and Collin-Dufresne, P. (2013) The CDS-Bond Basis. Working Paper.
Available online: https://ssrn.com/abstract=2024531.
Baillie, R.T. and Myers, R.J. (1991) Bivariate GARCH estimation of the opti-
mal commodity futures hedge. Journal of Applied Econometrics 6(2): 109-124.
Baillie, R.T. and Osterberg, W.P. (2000) Deviations from daily uncovered
interest rate parity and the role of intervention. Journal of International Fi-
nancial Markets, Institutions and Money 10(4): 363-379.
Baker, M., Bradley, B. and Wurgler, J. (2011) Benchmarks as Limits to Arbi-
trage: Understanding the Low-Volatility Anomaly.Financial Analysts Journal
67(1): 40-54.
Baker, M., Pan, A. and Wurgler, J. (2012) The eﬀect of reference point prices
on mergers and acquisitions. Journal of Financial Economics 106(1): 49-71.
Baker, M. and Sava¸ soglu, S. (2002) Limited arbitrage in mergers and acquisi-
tions. Journal of Financial Economics 64(1): 91-115.
143
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 145

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bakshi, G. and Kapadia, N. (2003a) Delta-Hedged Gains and the Negative
Market Volatility Risk Premium. Review of Financial Studies 16(2): 527-566.
Bakshi, G. and Kapadia, N. (2003b) Volatility Risk Premiums Embedded in
Individual Equity Options. Journal of Derivatives 11(1): 45-54.
Bakshi, G., Kapadia, N. and Madan, D. (2003) Stock Return Characteristics,
Skew Laws, and the Diﬀerential Pricing of Individual Equity Options. Review
of Financial Studies 16(1): 101-143.
Bakshi, G. and Panayotov, G. (2013) Predictability of currency carry trades
and asset pricing implications. Journal of Financial Economics 110(1): 139-
163.
Balb´ as, A., Longarela, I.R. and Lucia, J.J. (1999) How Financial Theory Ap-
plies to Catastrophe-Linked Derivatives – An Empirical Test of Several Pricing
Models. Journal of Risk and Insurance 66(4): 551-582.
Bali, T.G. and Demirtas, K.O. (2008) Testing mean reversion in ﬁnancial
market volatility: Evidence from S&P 500 index futures. Journal of Futures
Markets 28(1): 1-33.
Bali, T.G. and Hovakimian, A. (2009) Volatility Spreads and Expected Stock
Returns. Management Science 55(11): 1797-1812.
Ballings, M., Van den Poel, D., Hespeels, N. and Gryp, R. (2015) Evaluating
multiple classiﬁers for stock price direction prediction. Expert Systems with
Applications 42(20): 7046-7056.
Balta, A.-N. and Kosowki, R. (2013) Momentum Strategies in Futures Markets
and Trend-Following Funds. Working Paper. Available online: https://www.
edhec.edu/sites/www.edhec-portail.pprod.net/files/publications/
pdf/edhec-working-paper-momentum-strategies-in-futures_
1410350911195-pdfjpg.
Bandarchuk, P. and Hilscher, J. (2013) Sources of Momentum Proﬁts: Evi-
dence on the Irrelevance of Characteristics. Review of Finance 17(2): 809-845.
Banz, R. (1981) The relationship between return and market value of common
stocks. Journal of Financial Economics 9(1): 3-18.
Barber, J., Bennett, S. and Gvozdeva, E. (2015) How to Choose a Strategic
Multifactor Equity Portfolio? Journal of Index Investing 6(2): 34-45.
Barberis, N. (2000) Investing for the Long Run when Returns Are Predictable.
Journal of Finance 55(1): 225-264.
144
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 146

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Barberis, N. and Huang, M. (2008) Stocks as Lotteries: The Implications of
Probability Weighting for Security Prices. American Economic Review 98(5):
2066-2100.
Bardong, F. and Lehnert, T. (2004) TIPS, Break-Even Inﬂation, and Inﬂation
Forecasts. Journal of Fixed Income 14(3): 15-35.
Bariviera, A.F., Basgall, M.J., Hasperu´ e, W. and Naiouf, M. (2017) Some
stylized facts of the Bitcoin market. Physica A: Statistical Mechanics and its
Applications 484: 82-90.
Barnes, M.L., Bodie, Z., Triest, R.K. and Wang, J.C. (2010) A TIPS Score-
card: Are They Accomplishing Their Objectives? Financial Analysts Journal
66(5): 68-84.
Baron, M., Brogaard, J., Hagstr¨ omer, B. and Kirilenko, A. (2014) Risk and Re-
turn in High-Frequency Trading. Journal of Financial and Quantitative Anal-
ysis (forthcoming). Available online: https://ssrn.com/abstract=2433118.
Barr, D.G. and Campbell, J.Y. (1997) Inﬂation, real interest rates, and the
bond market: A study of UK nominal and index-linked government bond
prices. Journal of Monetary Economics 39(3): 361-383.
Barrett, W.B. and Kolb, R.W. (1995) Analysis of spreads in agricultural fu-
tures. Journal of Futures Markets 15(1): 69-86.
Barrieu, P. and El Karoui, N. (2002) Optimal design of weather derivatives.
ALGO Research 5(1): 79-92.
Barrieu, P. and Scaillet, O. (2010) A Primer on Weather Derivatives. In: Filar,
J.A. and Haurie, A. (eds.) Uncertainty and Environmental Decision Making:
A Handbook of Research and Best Practice. International Series in Operations
Research & Management Science, Vol. 138. New York, NY: Springer U.S.
Barroso, P. and Santa-Clara, P. (2014) Momentum Has Its Moments. Journal
of Financial Economics 116(1): 111-120.
Bartonov´ a, M. (2012) Hedging of Sales by Zero-cost Collar and its Financial
Impact. Journal of Competitiveness 4(2): 111-127.
Bartov, E., Radhakrishnan, S. and Krinsky, I. (2005) Investor Sophistication
and Patterns in Stock Returns after Earnings Announcements. Accounting
Review 75(1): 289-319.
Basu, S. (1977) The investment performance of common stocks in relation to
their price to earnings ratios: A test of the eﬃcient market hypothesis.Journal
of Finance 32(3): 663-682.
145
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 147

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Basu, D. and Miﬀre, J. (2013) Capturing the risk premium of commodity
futures: The role of hedging pressure. Journal of Banking & Finance 37(7):
2652-2664.
Batta, G., Chacko, G. and Dharan, B. (2010) A Liquidity-Based Explanation
of Convertible Arbitrage Alphas. Journal of Fixed Income 20(1): 28-43.
Battalio, R. and Mendenhall, R. (2007) Post-Earnings Announcement Drift:
Intra-Day Timing and Liquidity Costs. Working Paper. Available online:
https://ssrn.com/abstract=937257.
Batten, J. and Ellis, C. (1996) Technical trading system performance in the
Australian share market: Some empirical evidence. Asia Paciﬁc Journal of
Management 13(1): 87-99.
Batten, J.A., Khaw, K. and Young, M.R. (2014) Convertible Bond Pricing
Models. Journal of Economic Surveys 28(5): 775-803.
Baxter, M. and King, R. (1999) Measuring business cycles: Approximate band-
pass ﬁlters for economic time-series. Review of Economics and Statistics 81(4):
575-593.
Baxter, M. and Rennie, A. (1996) Financial Calculus: An Introduction to
Derivative Pricing. Cambridge, UK: Cambridge University Press.
Bayer, P.J., Geissler, C., Mangum, K. and Roberts, J.W. (2015) Speculators
and Middlemen: The Strategy and Performance of Investors in the Hous-
ing Market. Working Paper. Available online: https://ssrn.com/abstract=
1754003.
Beaver, W.H. (1966) Financial ratios as predictors of failure. Journal of Ac-
counting Research 4: 71-111.
Beaver, W.H., McNichols, M.F. and Rhie, J.-W. (2005) Have ﬁnancial state-
ments become less informative? Evidence from the ability of ﬁnancial ratios
to predict bankruptcy. Review of Accounting Studies 10(1): 93-122.
Bedendo, M., Cathcart, L. and El-Jahel, L. (2007) The Slope of the Term
Structure of Credit Spreads: An Empirical Investigation. Journal of Financial
Research 30(2): 237-257.
Beekhuizen, P., Duyvesteyn, J., Martens, M. and Zomerdijk, C. (2016) Carry
Investing on the Yield Curve.Working Paper. Available online: http://ssrn.
com/abstract=2808327.
Bekaert, G. and Wang, X. (2010) Inﬂation Risk and the Inﬂation Risk Pre-
mium. Economic Policy 25(64): 755-806.
146
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 148

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bekaert, G., Wei, M. and Xing, Y. (2007) Uncovered interest rate parity and
the term structure. Journal of International Money and Finance 26(6): 1038-
1069.
Bekkers, N., Doeswijk, R.Q. and Lam, T.W. (2009) Strategic Asset Allocation:
Determining the Optimal Portfolio with Ten Asset Classes. Journal of Wealth
Management 12(3): 61-77.
Belgrade, N. and Benhamou, E. (2004) Reconciling Year on Year and Zero
Coupon Inﬂation Swap: A Market Model Approach. Working Paper. Available
online: https://ssrn.com/abstract=583641.
Belgrade, N., Benhamou, E. and Koehler, E. (2004) A Market Model for
Inﬂation. Working Paper. Available online: https://ssrn.com/abstract=
576081.
Belkin, B., Suchover, S. and Forest, L. (1998) A one-parameter representation
of credit risk and transition matrices. Credit Metrics Monitor 1(3): 46-56.
Bellamy, D.E. (1994) Evidence of imputation clienteles in the Australian equity
market. Asia Paciﬁc Journal of Management 11(2): 275-287.
Bellovary, J.L., Giacomino, D.E. and Akers, M.D. (2007) A review of
bankruptcy prediction studies: 1930 to present. Journal of Financial Edu-
cation 33(4): 3-41.
Benavides, G. (2009) Predictive Accuracy of Futures Options Implied Volatil-
ity: The Case of the Exchange Rate Futures Mexican Peso-US Dollar.
Panorama Econ´ omico5(9): 55-95.
Ben-David, I., Franzoni, F.A. and Moussawi, R. (2012) ETFs, Arbitrage, and
Contagion. Working Paper. Available online: http://www.nccr-finrisk.
uzh.ch/media/pdf/wp/WP793_B1.pdf.
Ben-David, I., Franzoni, F.A. and Moussawi, R. (2017) Do ETFs Increase
Volatility? Journal of Finance (forthcoming). Available online: https://
ssrn.com/abstract=1967599.
Beneish, M.D. and Whaley, R.E. (1996) An Anatomy of the “S&P Game”:
The Eﬀects of Changing the Rules. Journal of Finance 51(5): 1909-1930.
Benet, B.A. (1990) Commodity futures cross hedging of foreign exchange ex-
posure. Journal of Futures Markets 10(3): 287-306.
Bengio, Y. (2009) Learning Deep Architectures for AI.Foundations and Trends
in Machine Learning 2(1): 1-127.
147
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 149

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Benhamou, E. (2016) Trend Without Hiccups – A Kalman Filter Approach.
Working Paper. Available online: https://ssrn.com/abstract=2747102.
Benos, E., Brugler, J., Hjalmarsson, E. and Zikes, F. (2017) Interactions
among High-Frequency Traders. Journal of Financial and Quantitative Anal-
ysis 52(4): 1375-1402.
Benos, E. and Sagade, S. (2016) Price Discovery and the Cross-Section of
High-Frequency Trading. Journal of Financial Markets 30: 54-77.
Benth, F. (2003) On arbitrage-free pricing of weather derivatives based on
fractional Brownian motion. Applied Mathematical Finance 10(4): 303-324.
Benth, F.E. and Kettler, P.C. (2010) Dynamic copula models for the spark
spread. Quantitative Finance 11(3): 407-421.
Benth, F.E., Kholodnyi, V.A. and Laurence, P. (eds.) (2014) Quantitative
Energy Finance: Modeling, Pricing, and Hedging in Energy and Commodity
Markets. New York, NY: Springer-Verlag.
Benth, F.E. and Saltyte-Benth, J. (2005) Stochastic modelling of temperature
variations with a view towards weather derivatives. Applied Mathematical Fi-
nance 12(1): 53-85.
Benth, F.E. and Saltyte-Benth, J. (2007) The volatility of temperature and
pricing of weather derivatives. Quantitative Finance 7(5): 553-561.
Benth, F., Saltyte-Benth, J. and Koekebakker, S. (2007) Putting a price on
temperature. Scandinavian Journal of Statistics 34(4): 746-767.
BenZion, U., Anan, S.D. and Yagil, J. (2005) Box Spread Strategies and Ar-
bitrage Opportunities. Journal of Derivatives 12(3): 47-62.
BenZion, U., Klein, P., Shachmurove, Y. and Yagil, J. (2003) Eﬃciency dif-
ferences between the S&P 500 and the Tel-Aviv 25 indices: a moving average
comparison. International Journal of Business 8(3): 267-284.
Beracha, E. and Downs, D.H. (2015) Value and Momentum in Commer-
cial Real Estate: A Market-Level Analysis. Journal of Portfolio Management
41(6): 48-61.
Beracha, E. and Skiba, H. (2011) Momentum in Residential Real Estate.Jour-
nal of Real Estate Finance and Economics 43(3): 229-320.
Berk, J., Green, R. and Naik, V. (1999) Optimal Investment, Growth Options
and Security Returns. Journal of Finance 54(5): 1153-1608.
148
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 150

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bernadell, C., Coche, J. and Nyholm, K. (2005) Yield curve prediction for the
strategic investor. Working Paper Series , No. 472. Frankfurt am Main, Ger-
many: European Central Bank. Available online: https://www.ecb.europa.
eu/pub/pdf/scpwps/ecbwp472.pdf?1dc8846d9df4642959c54aa73cee81ad.
Bernanke, B.S. and Kuttner, K.N. (2005) What Explains the Stock Market’s
Reaction to Federal Reserve Policy? Journal of Finance 60(3): 1221-1257.
Bernard, C., Cui, Z. and Mcleish, D. (2014) Convergence of the discrete vari-
ance swap in time-homogeneous diﬀusion models.Quantitative Finance Letters
2(1): 1-6.
Bernard, V.L. and Thomas, J.K. (1989) Post-Earnings-Announcement Drift:
Delayed Price Response or Risk Premium? Journal of Accounting Research
27: 1-36.
Bernard, V.L. and Thomas, J.K. (1990) Evidence That Stock Prices Do Not
Fully Reﬂect the Implications of Current Earnings for Future Earnings. Jour-
nal of Accounting and Economics 13(4): 305-340.
Bernardi, S., Leippold, M. and Lohre, H. (2018) Maximum Diversiﬁcation
Strategies along Commodity Risk Factors. European Financial Management
24(1): 53-78.
Bernstein, J. (1990) Jake Bernstein’s seasonal futures spreads: high-probability
seasonal spreads for futures traders. Hoboken, NJ: John Wiley & Sons, Inc.
Bessembinder, H. (1992) Systematic risk, hedging pressure, and risk premiums
in futures markets. Review of Financial Studies 5(4): 637-667.
Bessembinder, H. (1993) An empirical analysis of risk premia in futures mar-
kets. Journal of Futures Markets 13(6): 611-630.
Bessembinder, H. and Chan, K. (1992) Time-varying risk premia and fore-
castable returns in futures markets. Journal of Financial Economics 32(2):
169-193.
Bessembinder, H., Coughenour, J.F., Seguin, P.J. and Smoller, M.M. (1995)
Mean reversion in equilibrium asset prices: evidence from the futures term
structure. Journal of Finance 50(1): 361-375.
Bessembinder, H. and Maxwell, W. (2008) Markets: Transparency and the
Corporate Bond Market. Journal of Economic Perspectives 22(2): 217-234.
Bessembinder, H. and Seguin, P.J. (1993) Price volatility, trading volume,
and market depth: Evidence from futures markets. Journal of Financial and
Quantitative Analysis 28(1): 21-39.
149
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 151

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bester, A., Martinez, V.H. and Rosu, I. (2017) Cash Mergers and the Volatil-
ity Smile. Working Paper. Available online: https://ssrn.com/abstract=
1364491.
Beyaert, A., Garc´ ıa-Solanes, J. and P´ erez-Castej´ on, J.J. (2007) Uncovered
interest parity with switching regimes. Economic Modelling 24(2): 189-202.
Bharadwaj, A. and Wiggins, J.B. (2001) Box Spread and Put-Call Parity Tests
for the S&P 500 Index LEAPS Market. Journal of Derivatives 8(4): 62-71.
Bhattacharya, U., Loos, B., Meyer, S. and Hackethal, A. (2017) Abusing
ETFs. Review of Finance 21(3): 1217-1250.
Bhojraj, S. and Swaminathan, B. (2006) Macromomentum: Returns Pre-
dictability in International Equity Indices.Journal of Business 79(1): 429-451.
Bhushan, R. (1994) An Informational Eﬃciency Perspective on the Post-
Earnings Announcement Drift. Journal of Accounting and Economics 18(1):
45-65.
Biais, B. and Foucault, T. (2014) HFT and market quality. Bankers, Markets
& Investors 128: 5-19.
Biais, B., Foucault, T. and Moinas, S. (2014) Equilibrium Fast Trading.Work-
ing Paper. Available online: https://ssrn.com/abstract=2024360.
Bianchi, R.J., Drew, M. and Fan, J. (2015) Combining momentum with re-
versal in commodity futures. Journal of Banking & Finance 59: 423-444.
Biby, J.D., Modukuri, S. and Hargrave, B. (2001) Collateralized Borrowing
via Dollar Rolls. In: Fabozzi, F.J. (ed.) The Handbook of Mortgage-Backed
Securities. (5th ed.) New York, NY: McGraw-Hill, Inc.
Bielecki, T.R., Brigo, D. and Patras, F. (2011)Credit Risk Frontiers: Subprime
Crisis, Pricing and Hedging, CVA, MBS, Ratings, and Liquidity. Hoboken,
NJ: John Wiley & Sons, Inc.
Bielecki, T., Jeanblanc, M. and Rutkowski, M. (2007) Hedging of basket credit
derivatives in the Credit Default Swap market. Journal of Credit Risk 3(1):
91-132.
Bielecki, T., Vidozzi, A. and Vidozzi, L. (2008) A Markov copulae approach to
pricing and hedging of credit index derivatives and ratings triggered step-up
bonds. Journal of Credit Risk 4(1): 47-76.
Bieri, D.S. and Chincarini, L.B. (2004) Riding the Yield Curve: Diversiﬁ-
cation of Strategies. Working Paper. Available online: https://ssrn.com/
abstract=547682.
150
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 152

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bieri, D.S. and Chincarini, L.B. (2005) Riding the Yield Curve: A Variety of
Strategies. Journal of Fixed Income 15(2): 6-35.
Bierwag, G.O. (1979) Dynamic portfolio immunization policies. Journal of
Banking & Finance 3(1): 23-41.
Bierwag, G.O. and Kaufman, G. (1978) Bond Portfolio Strategy Simulations:
A Critique. Journal of Financial and Quantitative Analysis 13(3): 519-525.
Billingsley, R.S. and Chance, D.M. (1985) Options Market Eﬃciency and the
Box Spread Strategy. Financial Review 20(4): 287-301.
Billingsley, R.S. and Chance, D.M. (1988) The pricing and performance of
stock index futures spreads. Journal of Futures Markets 8(3): 303-318.
Bilson, J.F.O. (1981) The “Speculative Eﬃciency” Hypothesis. Journal of
Business 54(3): 435-451.
Birari, A. and Rode, M. (2014) Edge Ratio of Nifty for Last 15 Years on
Donchian Channel. SIJ Transactions on Industrial, Financial & Business
Management (IFBM) 2(5): 247-254.
Bird, R., Liem, H. and Thorp, S. (2014) Infrastructure: Real Assets and Real
Returns. European Financial Management 20(4): 802-824.
Bitsch, F., Buchner, A. and Kaserer, C. (2010) Risk, Return and Cash Flow
Characteristics of Infrastructure Fund Investments. EIB Papers 15(1): 106-
136.
Bjornson, B. and Carter, C.A. (1997) New Evidence on Agricultural Com-
modity Return Performance under Time-Varying Risk. American Journal of
Agricultural Economics 79(3): 918-930.
Black, F. (1972) Capital Market Equilibrium with Restricted Borrowing.Jour-
nal of Business 45(3): 444-455.
Black, F. and Litterman, R. (1991) Asset allocation: Combining investors’
views with market equilibrium. Journal of Fixed Income 1(2): 7-18.
Black, F. and Litterman, R. (1992) Global portfolio optimization. Financial
Analysts Journal 48(5): 28-43.
Black, F. and Scholes, M. (1973) The pricing of options and corporate liabili-
ties. Journal of Political Economy 81(3): 637-659.
Blake, M.L. and Catlett, L. (1984) Cross Hedging Hay Using Corn Futures:
An Empirical Test. Western Journal of Agricultural Economics 9(1): 127-134.
151
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 153

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Blanc-Brude, F., Hasan, M. and Whittaker, T. (2016) Benchmarking infras-
tructure project ﬁnance: Objectives, roadmap, and recent progress. Journal
of Alternative Investments 19(2): 7-18.
Blanc-Brude, F., Whittaker, T. and Wilde, S. (2017) Searching for a listed
infrastructure asset class using mean-variance spanning. Financial Markets
and Portfolio Management 31(2): 137-179.
Blanchard, O.J. and Gali, J. (2007) The Macroeconomic Eﬀects of Oil Shocks:
Why are the 2000s So Diﬀerent from the 1970s? Working Paper. Available
online: http://www.nber.org/papers/w13368.pdf.
Blanchard, O.J. and Riggi, M. (2013) Why are the 2000s so diﬀerent from the
1970s? A structural interpretation of changes in the macroeconomic eﬀects of
oil prices. Journal of the European Economic Association 11(5): 1032-1052.
Blank, S.C. (1984) Cross Hedging Australian Cattle. Australian Journal of
Agricultural Economics 28(2-3): 153-162.
Blitz, D., Huij, J., Lansdorp, S. and Verbeek, M. (2013) Short-term residual
reversal. Journal of Financial Markets 16(3): 477-504.
Blitz, D., Huij, J. and Martens, M. (2011) Residual Momentum. Journal of
Empirical Finance 18(3): 506-521.
Blitz, D.C. and van Vliet, P. (2007) The Volatility Eﬀect: Lower Risk without
Lower Return. Journal of Portfolio Management 34(1): 102-113.
Blitz, D. and Van Vliet, P. (2008) Global Tactical Cross Asset Allocation:
Applying Value and Momentum Across Asset Classes. Journal of Portfolio
Management 35(1): 23-28.
Block, R.L. (2011) Investing in REITs: Real Estate Investment Trusts. New
York, NY: Bloomberg Press.
Bloesch, J. and Gourio, F. (2015) The eﬀect of winter weather on U.S. eco-
nomic activity.Federal Reserve Bank of Chicago, Economic Perspectives39(1):
1-20.
Bloom, L., Easley, D. and O’Hara, M. (1994) Market Statistics and Technical
Analysis: The Role of Volume. Journal of Finance 49(1): 153-181.
Blundell, L. (2006) Infrastructure investment: On the up. Property Australia
20(9): 20-22.
Bobey, B. (2010) The Eﬀects of Default Correlation on Corporate Bond Credit
Spreads. Working Paper. Available online: https://ssrn.com/abstract=
1510170.
152
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 154

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bodie, Z. (1983) Commodity Futures as a Hedge against Inﬂation. Journal of
Portfolio Management 9(3): 12-17.
Bodie, Z., Kane, A. and Marcus, A.J. (1996) Investments. New York, NY:
McGraw-Hill, Inc.
Bodie, Z. and Rosansky, V.I. (1980) Risk and Return in Commodity Futures.
Financial Analysts Journal 36(3): 27-39.
Bogomolov, T. (2013) Pairs trading based on statistical variability of the
spread process. Quantitative Finance 13(9): 1411-1430.
Bohlin, S. and Strickland, G. (2004) Climbing the Ladder: How to Manage
Risk in Your Bond Portfolio. American Association of Individual Investors
Journal, July 2004, pp. 5-8.
Bol, G., Rachev, S.T. and W¨ urth, R. (eds.) (2009)Risk Assessment: Decisions
in Banking and Finance. Heidelberg, Germany: Physica-Verlag.
Bollen, N.P.B. and Busse, J.A. (2005) Short-Term Persistence in Mutual Fund
Performance. Review of Financial Studies 18(2): 569-597.
Bollen, J. and Mao, H. (2011) Twitter mood as a stock market predictor.
Computer 44(10): 91-94.
Bollen, J., Mao, H. and Zeng, X. (2011) Twitter mood predicts the stock
market. Journal of Computational Science 2(1): 1-8.
Bollen, N.P.B. and Whaley, R. (2004) Does Net Buying Pressure Aﬀect the
Shape of Implied Volatility Functions? Journal of Finance 59(2): 711-754.
Bollerslev, T., Gibson, M. and Zhou, H. (2011) Dynamic estimation of volatil-
ity risk premia and investor risk aversion from option-implied and realized
volatilities. Journal of Econometrics 160(1): 235-245.
Bologna, P. and Cavallo, L. (2002) Does the Introduction of Index Futures
Eﬀectively Reduce Stock Market Volatility? Is the Futures Eﬀect Immediate?
Evidence from the Italian Stock Exchange Using GARCH. Applied Financial
Economics 12(3): 183-192.
Bond, M.T. and Seiler, M.J. (1998) Real Estate Returns and Inﬂation: An
Added Variable Approach. Journal of Real Estate Research 15(3): 327-338.
Bondarenko, O. (2014) Why Are Put Options So Expensive? Quarterly Jour-
nal of Finance 4(3): 1450015.
Booth, L.D. (1987) The dividend tax credit and Canadian ownership objec-
tives. Canadian Journal of Economics 20(2): 321-339.
153
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 155

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Booth, L.D. and Johnston, D.J. (1984) The ex-dividend day behavior of Cana-
dian stock prices: Tax changes and clientele eﬀects. Journal of Finance 39(2):
457-476.
Booth, J.R., Smith, R.L. and Stolz, R.W. (1984) The Use of Interest Rate
Futures by Financial Institutions. Journal of Bank Research 15(1): 15-20.
Borovkova, S. and Geman, H. (2006) Seasonal and stochastic eﬀects in com-
modity forward curves. Review of Derivatives Research 9(2): 167-186.
Bos, R. (2000) Index Calculation Primer. New York, NY: Standard and Poor’s
Quantitative Services.
Bos, M., Carter, S. and Skiba, P.M. (2012) The Pawn Industry and Its Cus-
tomers: The United States and Europe. Working Paper. Available online:
https://ssrn.com/abstract=2149575.
Boscher, H. and Ward, I. (2002) Long or short in CDOs. Risk, June 2002, pp.
125-129.
Bossu, S. (2006) Introduction to Variance Swaps. Wilmott Magazine , March
2006, pp. 50-55.
Boudoukh, J., Richardson, M. and Whitelaw, R.F. (1994) Industry Returns
and the Fisher Eﬀect. Journal of Finance 49(5): 1595-1615.
Boudoukh, J., Whitelaw, R., Richardson, M. and Stanton, R. (1997) Pricing
Mortgage-Backed Securities in a Multifactor Interest Rate Environment: A
Multivariate Density Estimation Approach.Review of Financial Studies 10(2):
405-446.
Boulos, N. and Swanson, P.E. (1994) Interest Rate Parity in Times of Turbu-
lence: The Issue Revisited. Journal of Financial and Strategic Decisions 7(2):
43-52.
Bouman, F.J.A. and Houtman, R. (1988) Pawnbroking as an Instrument
of Rural Banking in the Third World. Economic Development and Cultural
Change 37(1): 69-89.
Bouoiyour, J., Selmi, R. and Tiwari, A.K. (2015) Is Bitcoin business income
or speculative foolery? New ideas through an improved frequency domain
analysis. Annals of Financial Economics 10(1): 1-23.
Bouoiyour, J., Selmi, R., Tiwari, A.K. and Olayeni, O.R. (2016) What drives
Bitcoin price? Economics Bulletin 36(2): 843-850.
154
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 156

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bouri, E., Gupta, R., Tiwari, A.K. and Roubaud, D. (2017a) Does Bitcoin
hedge global uncertainty? Evidence from wavelet-based quantile-in-quantile
regressions. Finance Research Letters 23: 87-95.
Bouri, E., Moln´ ar, P., Azzi, G., Roubaud, D. and Hagfors, L.I. (2017b) On the
hedge and safe haven properties of Bitcoin: Is it really more than a diversiﬁer?
Finance Research Letters 20: 192-198.
Bouzoubaa, M. and Osseiran, A. (2010) Exotic options and hybrids: a Guide
to Structuring, Pricing and Trading. Chichester, UK: John Wiley & Sons, Ltd.
Bowen, D.A. and Hutchinson, M.C. (2016) Pairs trading in the UK equity
market: Risk and return. European Journal of Finance 22(14): 1363-1387.
Bowen, D., Hutchinson, M.C. and O’Sullivan, N. (2010) High frequency equity
pairs trading: Transaction costs, speed of execution and patterns in returns.
Journal of Trading 5(3): 31-38.
Bowsher, N. (1979) Repurchase Agreements.Federal Reserve Bank of St. Louis
Review 61(9): 17-22.
Boyarchenko, N., Fuster, A. and Lucca, D.O. (2014) Understanding Mortgage
Spreads. Federal Reserve Bank of New York Staﬀ Reports , No. 674. Available
online:
https://www.newyorkfed.org/medialibrary/media/research/staff_
reports/sr674.pdf.
Boyd, J.H., Hu, J. and Jagannathan, R. (2005) The Stock Market’s Reaction
to Unemployment News: Why Bad News Is Usually Good for Stocks. Journal
of Finance 60(2): 649-672.
Boyd, N.E. and Mercer, J.M. (2010) Gains from Active Bond Portfolio Man-
agement Strategies. Journal of Fixed Income 19(4): 73-83.
Boyle, P.P. (1978) Immunization under stochastic models of the term struc-
ture. Journal of the Institute of Actuaries 105(2): 177-187.
Bozdog, D., Florescu, I., Khashanah, K. and Wang, J. (2011) Rare Events
Analysis of High-Frequency Equity Data. Wilmott Magazine 2011(54): 74-81.
Bozic, M. and Fortenbery, T.R. (2012) Creating Synthetic Cheese Futures: A
Method for Matching Cash and Futures Prices in Dairy. Journal of Agribusi-
ness 30(2): 87-102.
Brandvold, M., Moln´ ar, P., Vagstad, K. and Valstad, O.C.A. (2015) Price
discovery on Bitcoin exchanges. Journal of International Financial Markets,
Institutions and Money 36: 18-35.
155
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 157

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Branger, N. and Schlag, C. (2004) Why is the Index Smile So Steep? Review
of Finance 8(1): 109-127.
Brazil, A.J. (1988) Citicorp’s mortgage valuation model: Option-adjusted
spreads and option-based durations. Journal of Real Estate Finance and Eco-
nomics 1(2): 151-162.
Breeden, D.T. and Litzenberger, R.H. (1978) Prices of state-contingent claims
implicit in option prices. Journal of Business 51(4): 621-651.
Brennan, M.J. and Schwartz, E.S. (1977) Convertible Bonds: Valuation and
Optimal Strategies for Call and Conversion. Journal of Finance 32(5): 1699-
1715.
Brennan, M.J. and Schwartz, E.S. (1985) Determinants of GNMA Mortgage
Prices. Real Estate Economics 13(3): 209-228.
Brennan, M.J. and Schwartz, E.S. (1988) The case for convertibles. Journal
of Applied Corporate Finance 1(2): 55-64.
Brenner, M., Subrahmanyam, M.G. and Uno, J. (1989) Stock index futures
arbitrage in the Japanese markets. Japan and the World Economy 1(3): 303-
330.
Brezigar-Masten, A. and Masten, P. (2012) CART-based selection of
bankruptcy predictors for the logit model. Expert Systems with Applications
39(11): 10153-10159.
Bri` ere, M., Oosterlinck, K. and Szafarz, A. (2015) Virtual currency, tangible
return: Portfolio diversiﬁcation with bitcoin. Journal of Asset Management
16(6): 365-373.
Briys, E. and Solnik, B. (1992) Optimal currency hedge ratios and interest
rate risk. Journal of International Money and Finance 11(5): 431-445.
Broadie, M. and Jain, A. (2008) The eﬀect of jumps and discrete sampling on
volatility and variance swaps.International Journal of Theoretical and Applied
Finance 11(8): 761-797.
Brock, W., Lakonishock, J. and LeBaron, B. (1992) Simple technical trading
rules and the stochastic properties of stock returns. Journal of Finance 47(5):
1731-1764.
Brockett, P., Golden, L.L., Wen, M. and Yang, C. (2010) Pricing weather
derivatives using the indiﬀerence pricing approach. North American Actuarial
Journal 13(3): 303-315.
156
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 158

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Brockett, P.L., Wang, M. and Yang, C. (2005) Weather Derivatives And
Weather Risk Management. Risk Management and Insurance Review 8(1):
127-140.
Brody, D., Syroka, J. and Zervos, M. (2002) Dynamical pricing of weather
derivatives. Quantitative Finance 2(3): 189-198.
Brogaard, J. and Garriott, C. (2018) High-Frequency Trading Competition.
Working Paper. Available online: https://ssrn.com/abstract=2435999.
Brogaard, J., Hagstr¨ omer, B., Nord´ en, L. and Riordan, R. (2015) Trading
Fast and Slow: Colocation and Liquidity. Review of Financial Studies 28(12):
3407-3443.
Brogaard, J., Hendershott, T. and Riordan, R. (2014) High-Frequency Trading
and Price Discovery. Review of Financial Studies 27(8): 2267-2306.
Brooks, J. (2017) A Half Century of Macro Momentum. Working Paper.
Available online:
https://www.aqr.com/-/media/AQR/Documents/Insights/White-Papers/
A-Half-Century-of-Macro-Momentum.pdf .
Brooks, C. and Chong, J. (2001) The Cross-Currency Hedging Performance
of Implied Versus Statistical Forecasting Models. Journal of Futures Markets
21(11): 1043-1069.
Brooks, C., Davies, R.J. and Kim, S.S. (2007) Cross Hedging with Single Stock
Futures. Assurances et Gestion des Risques 74(4): 473-504.
Brooks, C., Henry, O.T. and Persand, G. (2002) The Eﬀect of Asymmetries
on Optimal Hedge Ratios. Journal of Business 75(2): 333-352.
Brooks, J. and Moskowitz, T.J. (2017) Yield Curve Premia. Working Paper.
Available online: https://ssrn.com/abstract=2956411.
Brown, D. (1999) The Determinants of Expected Returns on Mortgage-backed
Securities: An Empirical Analysis of Option-adjusted Spreads. Journal of
Fixed Income 9(2): 8-18.
Brown, P. and Clarke, A. (1993) The Ex-Dividend Day Behaviour of Aus-
tralian Share Prices Before and After Dividend Imputation.Australian Journal
of Management 18(1): 1-40.
Brown, D.C., Davies, S. and Ringgenberg, M. (2018) ETF Arbitrage and
Return Predictability. Working Paper. Available online: https://ssrn.com/
abstract=2872414.
157
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 159

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Brown, S.J., Goetzmann, W., Ibbotson, R.G. and Ross, S.A. (1992) Survivor-
ship Bias in Performance Studies. Review of Financial Studies 5(4): 553-580.
Brown, S.J., Grundy, B.D., Lewis, C.M. and Verwijmeren, P. (2012) Convert-
ibles and hedge funds as distributors of equity exposure. Review of Financial
Studies 25(10): 3077-3112.
Brown, K.C. and Raymond, M.V. (1986) Risk arbitrage and the prediction of
successful corporate takeovers. Financial Management 15(3): 54-63.
Browne, S. (2000) Risk-constrained dynamic active portfolio management.
Management Science 46(9): 1188-1199.
Br¨ uck, E. and Fan, Y. (2017) Smart Beta In Global Government Bonds And
Its Risk Exposure. Working Paper. Available online:
https://www.cfasociety.org/France/Documents/QuantAwards2017_
Etienne%20BRUECK%20and%20Yuanting%20FAN_EDHEC.pdf.
Bruder, B., Dao, T.-L., Richard, R.-J. and Roncalli, T. (2013) Trend Filtering
Methods for Momentum Strategies. Working Paper. Available online: https:
//ssrn.com/abstract=2289097.
Brunnermeier, M.K., Nagel, S. and Pedersen, L.H. (2008) Carry Trades and
Currency Crashes. NBER Macroeconomics Annual 23(1): 313-347.
Bu, Q. and Lacey, N. (2007) Exposing Survivorship Bias in Mutual Fund Data.
Journal of Business and Economics Studies 13(1): 22-37.
Budish, E., Cramton, P. and Shim, J. (2015) The High-Frequency Trading
Arms Race: Frequent Batch Auctions as a Market Design Response.Quarterly
Journal of Economics 130(4): 1547-1621.
Buetow, G.W. and Henderson, B.J. (2012) An empirical analysis of exchange-
traded funds. Journal of Portfolio Management 38(4): 112-127.
Buetow, G.W. and Henderson, B.J. (2016) The VIX Futures Basis: Determi-
nants and Implications. Journal of Portfolio Management 42(2): 119-130.
B¨ uhler, W. and Kempf, A. (1995) DAX index futures: Mispricing and arbi-
trage in German markets. Journal of Futures Markets 15(7): 833-859.
Bundgaard, J. (2013) Coordination Rules as a Weapon in the War against
Cross-Border Tax Arbitrage – The Case of Hybrid Entities and Hybrid Finan-
cial Instruments. Bulletin for International Taxation , April/May 2013, pp.
200-204.
Buraschi, A. and Jiltsov, A. (2005) Inﬂation Risk Premia and the Expectations
Hypothesis. Journal of Financial Economics 75(2): 429-490.
158
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 160

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Burnside, C., Eichenbaum, M., Kleshchelski, I. and Rebelo, S. (2011) Do peso
problems explain the returns to the carry trade? Review of Financial Studies
24(3): 853-891.
Burnside, C., Eichenbaum, M. and Rebelo, S. (2007) The Returns to Currency
Speculation in Emerging Markets. American Economic Review97(2): 333-338.
Burnside, C., Eichenbaum, M. and Rebelo, S. (2008) Carry Trade: The Gains
of Diversiﬁcation. Journal of the European Economic Association 6(2/3): 581-
588.
Burnside, C., Eichenbaum, M. and Rebelo, S. (2011) Carry trade and momen-
tum in currency markets. Annual Review of Financial Economics 3: 511-535.
Burtshell, X., Gregory, J. and Laurent, J.-P. (2009) A comparative analysis of
CDO pricing models under the factor copula framework.Journal of Derivatives
16(4): 9-37.
Busch, T., Christensen, B.J. and Nielsen, M.Ø. (2011) The Role of Implied
Volatility in Forecasting Future Realized Volatility and Jumps in Foreign Ex-
change, Stock, and Bond Markets. Journal of Econometrics 160(1): 48-57.
Buser, S.A. and Hess, P.J. (1986) Empirical determinants of the relative yields
on taxable and tax-exempt securities. Journal of Financial Economics 17(2):
335-355.
Butterworth, D. and Holmes, P. (2010) Mispricing in stock index futures con-
tracts: evidence for the FTSE 100 and FTSE mid 250 contracts. Applied
Economics Letters 7(12): 795-801.
Buttimer, R.J., Hyland, D.C. and Sanders, A.B. (2005) REITs, IPO Waves,
and Long-Run Performance. Real Estate Economics 33(1): 51-87.
Caginalp, G., DeSantis, M. and Sayrak, A. (2014) The nonlinear price dynam-
ics of US equity ETFs. Journal of Econometrics 183(2): 193-201.
Calamos, N.P. (2003) Convertible Arbitrage: Insights and Techniques for Suc-
cessful Hedging. Hoboken, NJ: John Wiley & Sons, Inc.
Caldeira, J. and Moura, G.V. (2013) Selection of a portfolio of pairs based
on cointegration: A statistical arbitrage strategy. Working Paper. Available
online: https://ssrn.com/abstract=2196391.
Callaghan, S.R. and Barry, C.B. (2003) Tax-induced trading of equity securi-
ties: Evidence from the ADR market. Journal of Finance 58(4): 1583-1611.
159
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 161

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Callej´ on, A.M., Casado, A.M., Fern´ andez, M.A. and Pel´ aez, J.I. (2013) A
System of Insolvency Prediction for industrial companies using a ﬁnancial al-
ternative model with neural networks. International Journal of Computational
Intelligence Systems 6(1): 29-37.
Campbell, J.Y. (1991) A Variance Decomposition for Stock Returns.Economic
Journal 101(405): 157-179.
Campbell, J.Y., Chan, Y.L. and Viceira, L.M. (2003) A multivariate model of
strategic asset allocation. Journal of Financial Economics 67(1): 41-80.
Campbell, S.D. and Diebold, F.X. (2005) Weather forecasting for weather
derivatives. Journal of the American Statistical Association 100(469): 6-16.
Campbell, J.Y., Hilscher, J. and Sziglayi, J. (2008) In Search of Distress Risk.
Journal of Finance 63(6): 2899-2939.
Campbell, J.Y., Shiller, R.J. and Viceira, L.M. (2009) Understanding
Inﬂation-Indexed Bond Markets. In: Romer, D. and Wolfers, J. (eds.) Brook-
ings Papers on Economic Activity. Washington, DC: Brookings Institution
Press, pp. 79-120.
Campbell, J.Y., Sunderam, A. and Viceira, L.M. (2017) Inﬂation Bets or
Deﬂation Hedges? The Changing Risks of Nominal Bonds. Critical Finance
Review 6(2): 263-301.
Campbell, J.Y. and Viceira, L.M. (2004) Long-Horizon Mean-Variance Anal-
ysis: A User Guide. Working Paper. Available online: http://www.people.
hbs.edu/lviceira/faj_cv_userguide.pdf.
Campbell, J.Y. and Viceira, L.M. (2005) The Term Structure of the Risk:
Return Trade-Oﬀ. Financial Analysts Journal 61(1): 34-44.
Canina, L. and Figlewski, S. (1993) The Informational Content of Implied
Volatility. Review of Financial Studies 6(3): 659-681.
Cao, C., Chen, Y., Liang, B. and Lo, A.W. (2013) Can hedge funds time
market liquidity? Journal of Financial Economics 109(2): 493-516.
Cao, C., Goldie, B., Liang, B. and Petrasek, L. (2016) What Is the Nature
of Hedge Fund Manager Skills? Evidence from the Risk-Arbitrage Strategy.
Journal of Financial and Quantitative Analysis 51(3): 929-957.
Cao, M. and Wei, J. (2000) Pricing the weather. Risk, May 2000, pp. 67-70.
Cao, M. and Wei, J. (2004) Weather derivatives valuation and market price
of weather risk. Journal of Futures Markets 24(11): 1065-1089.
160
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 162

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Caplin, A. and Leahy, J. (2011) Trading Frictions and House Price Dynamics.
Journal of Money, Credit and Banking 43(7): 283-303.
Capozza, D.R., Hendershott, P.H. and Mack, C. (2004) An Anatomy of Price
Dynamics in Illiquid Markets: Analysis and Evidence from Local Housing
Markets. Real Estate Economics 32(1): 1-32.
Carhart, M.M. (1997) Persistence in mutual fund performance. Journal of
Finance 52(1): 57-82.
Carhart, M.M., Carpenter, J.N., Lynch, A.W. and Musto, D.K. (2002) Mutual
Fund Survivorship. Review of Financial Studies 15(5): 1439-1463.
Carmona, R. and Cr´ epey, S. (2010) Particle methods for the estimation of
credit portfolio loss distributions. International Journal of Theoretical and
Applied Finance 13(4): 577-602.
Carmona, R. and Durrleman, V. (2003) Pricing and Hedging Spread Options.
SIAM Review 45(4): 627-685.
Carr, P. and Javaheri, A. (2005) The forward PDE for European options on
stocks with ﬁxed fractional jumps. International Journal of Theoretical and
Applied Finance 8(2): 239-253.
Carr, P. and Lee, R. (2007) Realized volatility and variance: Options via
swaps. Risk 20(5): 76-83.
Carr, P. and Lee, R. (2009) Volatility Derivatives.Annual Review of Financial
Economics 1: 319-339.
Carr, P., Lee, R. and Wu, L. (2012) Variance swaps on time-changed L´ evy
processes. Finance and Stochastics 16(2): 335-355.
Carr, P. and Wu, L. (2009) Variance risk premiums.Review of Financial Stud-
ies 22(3): 1311-1341.
Carr, P. and Wu, L. (2016) Analyzing volatility risk and risk premium in
option contracts: A new theory. Journal of Financial Economics 120(1): 1-20.
Carrasco, C.G. (2007) Studying the properties of the correlation trades. Work-
ing Paper. Available online: https://mpra.ub.uni-muenchen.de/22318/1/
MPRA_paper_22318.pdf.
Carrion, A. (2013) Very fast money: High-frequency trading on the NASDAQ.
Journal of Financial Markets 16(4): 680-711.
Carrion, A. and Kolay, M. (2017) Trade Signing in Fast Markets. Working
Paper. Available online: https://ssrn.com/abstract=2489868.
161
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 163

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Carron, A.S. and Hogan, M. (1988) The option valuation approach to mort-
gage pricing. Journal of Real Estate Finance and Economics 1(2): 131-149.
Cartea, A. and Figueroa, M. (2005) Pricing in electricity markets: a mean
reverting jump diﬀusion model with seasonality.Applied Mathematical Finance
12(4): 313-335.
Cartea, A. and Pedraz, C.G. (2012) How Much Should We Pay for Intercon-
necting Electricity Markets? A Real Options Approach. Energy Economics
34(1): 14-30.
Carter, C., Rausser, G. and Schmitz, A. (1983) Eﬃcient asset portfolios and
the theory of normal backwardation. Journal of Political Economy 91(2): 319-
331.
Casassus, J. and Collin-Dufresne, P. (2005) Stochastic convenience yield im-
plied from commodity futures and interest rates. Journal of Finance 60(5):
2283-2331.
Case, K.E. and Shiller, R.J. (1987) Prices of Single Family Homes since 1970:
New Indexes for Four Cities. Federal Reserve Bank of Boston, New England
Economic Review, September-October 1987, pp. 45-56.
Case, K.E. and Shiller, R.J. (1989) The Eﬃciency of the Market for Single-
Family Homes. American Economic Review 79(1): 125-137.
Case, K.E. and Shiller, R.J. (1990) Forecasting Prices and Excess Returns in
the Housing Market. Real Estate Economics 18(3): 253-273.
Caskey, J.P. (1991) Pawnbroking in America: the Economics of a Forgotten
Credit Market. Journal of Money, Credit and Banking 23(1): 85-99.
Cassano, M. and Sick, G. (2013) Valuation of a spark spread: an LM6000
power plant. European Journal of Finance 18(7-8): 689-714.
Castelino, M.G and Vora, A. (1984) Spread volatility in commodity futures:
The length eﬀect. Journal of Futures Markets 4(1): 39-46.
Cavaglia, S. and Vadim, M. (2002) Cross-Industry, Cross Country Allocation.
Financial Analysts Journal 58(6): 78-97.
Cecchetti, S.G., Cumby, R.E. and Figlewski, S. (1988) Estimation of the Op-
timal Futures Hedge. Review of Economics and Statistics 70(4): 623-630.
ˇCerovi´ c, S. and Pepi´ c, M. (2011) Interest rate derivatives in developing coun-
tries in Europe. Perspectives of Innovation in Economics and Business 9(3):
38-42.
162
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 164

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ˇCerovi´ c, S., Pepi´ c, M.,ˇCerovi´ c, S. andˇCerovi´ c, N. (2014) Duration and con-
vexity of bonds. Singidunum Journal of Applied Sciences 11(1): 53-66.
Cerrato, M. and Djennad, A. (2008) Dynamic Option Adjusted Spread and
the Value of Mortgage Backed Securities. Working Paper. Available online:
https://www.gla.ac.uk/media/media_71226_en.pdf.
Chaboud, A.P. and Wright, J.H. (2005) Uncovered interest parity: it works,
but not for long. Journal of International Economics 66(2): 349-362.
Chaiyapo, N. and Phewchean, N. (2017) An application of Ornstein-Uhlenbeck
process to commodity pricing in Thailand. Advances in Diﬀerence Equations
2017: 179.
Chakravarty, S., Gulen, H. and Mayhew, S. (2004) Informed Trading in Stock
and Option Markets. Journal of Finance 59(3): 1235-1257.
Chalmers, J.M.R. (1998) Default Risk Cannot Explain the Muni Puzzle: Ev-
idence from Municipal Bonds that are Secured by U.S. Treasury Obligations.
Review of Financial Studies 11(2): 281-308.
Chambers, D.R., Foy, M., Liebner, J. and Lu, Q. (2014) Index Option Returns:
Still Puzzling. Review of Financial Studies 27(6): 1915-1928.
Chan, E.P. (2013) Algorithmic Trading: Winning Strategies and Their Ratio-
nale. Hoboken, NJ: John Wiley & Sons, Inc.
Chan, A.W.H. and Chen, N.-F. (2007) Convertible bond underpricing: Rene-
gotiable covenants, seasoning, and convergence. Management Science 53(11):
1793-1814.
Chan, K.C. and Chen, N.-F. (1991) Structural and Return Characteristics of
Small and Large Firms. Journal of Finance 46(4): 1467-1484.
Chan, K. and Chung, Y.P. (1993) Intraday relationships among index arbi-
trage, spot and futures price volatility, and spot market volume: A transac-
tions data test. Journal of Banking & Finance 17(4): 663-687.
Chan, K.C., Hendershott, P.H. and Sanders, A.B. (1990) Risk and Return on
Real Estate: Evidence from Equity REITs. AREUEA Journal 18(4): 431-452.
Chan, K.C., Jegadeesh, N. and Lakonishok, J. (1996) Momentum Strategies.
Journal of Finance 51(5): 1681-1713.
Chan, S.H., Leung, W.K. and Wang, K. (1998) Institutional Investment in
REITs: Evidence and Implications. Journal of Real Estate Research 16(3):
357-374.
163
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 165

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Chan, K.F., Treepongkaruna, S., Brooks, R. and Gray, S. (2011) Asset market
linkages: Evidence from ﬁnancial, commodity and real estate assets. Journal
of Banking & Finance 35(6): 1415-1426.
Chance, D. (1994) Managed Futures and Their Role in Investment Portfolios.
Charlottesville, VA: The Research Foundation of the Institute of Chartered
Financial Analysts.
Chance, D.M. and Jordan, J.V. (1996) Duration, Convexity, and Time as
Components of Bond Returns. Journal of Fixed Income 6(2): 88-96.
Chandra, P. (2003) Sigmoidal Function Classes for Feedforward Artiﬁcial Neu-
ral Networks. Neural Processing Letters 18(3): 205-215.
Chang, E.C., Cheng, J.W. and Pinegar, J.M. (1999) Does Futures Trading
Increase Stock Market Volatility? The Case of the Nikkei Stock Index Futures
Exchange. Journal of Banking & Finance 23(5): 727-753.
Chang, J.S. and Fang, H. (1990) An intertemporal measure of hedging eﬀec-
tiveness. Journal of Futures Markets 10(3): 307-321.
Chang, R.P., Ko, K.-C., Nakano, S. and Rhee, S.G. (2016) Residual Mo-
mentum and Investor Underreaction in Japan. Working Paper. Available
online: http://sfm.finance.nsysu.edu.tw/php/Papers/CompletePaper/
134-1136665035.pdf.
Chaput, J.S. and Ederington, L.H. (2003) Option Spread and Combination
Trading. Journal of Derivatives 10(4): 70-88.
Chaput, J.S. and Ederington, L.H. (2005) Vertical Spread Design. Journal of
Derivatives 12(3): 28-46.
Chaput, J.S. and Ederington, L.H. (2008) Ratio Spreads. Journal of Deriva-
tives 15(3): 41-57.
Charupat, N. and Miu, P. (2011) The Pricing and Performance of Leveraged
Exchange-Traded Funds. Journal of Banking & Finance 35(4): 966-977.
Chatterjee, S., Dhillon, U.S. and Ram´ ırez, G.G. (1996) Resolution of Financial
Distress: Debt Restructurings via Chapter 11, Prepackaged Bankruptcies, and
Workouts. Financial Management 25(1): 5-18.
Chaudhuri, A. and De, K. (2011) Fuzzy support vector machine for bankruptcy
prediction. Applied Soft Computing 11(2): 2472-2486.
Chaumont, S., Imkeller, P. and M¨ uller, M. (2006) Equilibrium Trading of Cli-
mate and Weather Risk and Numerical Simulation in a Markovian Framework.
Stochastic Environment Research and Risk Assessment 20(3): 184-205.
164
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 166

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Chava, S. and Jarrow, R.A. (2004) Bankruptcy Prediction with Industry Ef-
fects. Review of Finance 8(4): 537-569.
Chaves, D.B. (2012) Eureka! A Momentum Strategy that Also Works in
Japan. Working Paper. Available online:
https://ssrn.com/abstract=1982100.
Chaves, D.B. and Viswanathan, V. (2016) Momentum and mean-reversion in
commodity spot and futures markets. Journal of Commodity Markets 3(1):
39-53.
Che, Y.S. (2016) A study on the risk and return of option writing strategies
(Ph.D. Thesis). HKBU Institutional Repository. Open Access Theses and Dis-
sertations. 187. Hong Kong, China: Hong Kong Baptist University. Available
online: https://repository.hkbu.edu.hk/etd_oa/187/.
Che, S.Y.S. and Fung, J.K.W. (2011) The performance of alternative futures
buy-write strategies. Journal of Futures Markets 31(12): 1202-1227.
Cheah, E.T. and Fry, J. (2015) Speculative Bubbles in Bitcoin markets? An
Empirical Investigation into the Fundamental Value of Bitcoin. Economics
Letters 130: 32-36.
Chen, M.Y. (2014) A high-order fuzzy time series forecasting model for inter-
net stock trading. Future Generation Computer Systems 37: 461-467.
Chen, H.J., Chen, S.J., Chen, Z. and Li, F. (2017) Empirical Investigation of
an Equity Pairs Trading Strategy. Management Science (forthcoming). DOI:
https://doi.org/10.1287/mnsc.2017.2825.
Chen, A.H.Y., Chen, K.C. and Howell, S. (1999) An analysis of dividend
enhanced convertible stocks. International Review of Economics and Finance
8(3): 327-338.
Chen, T.F., Chung, S.L. and Tsai, W.C. (2016) Option-Implied Equity Risk
and the Cross-Section of Stock Returns. Financial Analysts Journal 72(6):
42-55.
Chen, S.-J., Hsieh, C., Vines, T.W. and Chiou, S. (1998) Macroeconomic
Variables, Firm-Speciﬁc Variables and Returns to REITs. Journal of Real
Estate Research 16(3): 269-278.
Chen, A.H., Kang, J. and Yang, B. (2005) A Model for Convexity-Based
Cross-Hedges with Treasury Futures. Journal of Fixed Income 15(3): 68-79.
Chen, L., Lesmond, D.A. and Wei, J. (2007) Corporate Yield Spreads and
Bond Liquidity. Journal of Finance 62(1): 119-149.
165
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 167

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Chen, A.S., Leung, M.T. and Daouk, H. (2003) Application of neural networks
to an emerging ﬁnancial market: Forecasting and trading the Taiwan Stock
Index. Computers & Operations Research 30(6): 901-923.
Chen, R.-R., Liu, B. and Cheng, X. (2010) Pricing the Term Structure of
Inﬂation Risk Premia: Theory and Evidence from TIPS. Journal of Empirical
Finance 17(4): 702-721.
Chen, Z., Mao, C.X. and Wang, Y. (2010) Why ﬁrms issue callable bonds:
Hedging investment uncertainty. Journal of Corporate Finance 16(4): 588-
607.
Chen, G., Roberts, M.C. and Thraen, C.S. (2006) Managing dairy proﬁt risk
using weather derivatives. Journal of Agricultural and Resource Economics
31(3): 653-666.
Chen, A.H. and Selender, A.K. (1994) Determination of Swap Spreads: An
Empirical Analysis. Cox School of Business Historical Working Papers , No.
170. Dallas, TX: Southern Methodist University. Available online: http://
scholar.smu.edu/business_workingpapers/170.
Chen, F. and Sutcliﬀe, C. (2007) Better Cross Hedges With Composite Hedg-
ing? Hedging Equity Portfolios Using Financial and Commodity Futures.
European Journal of Finance 18(6): 575-595.
Chen, H.-L., Yang, B., Wang, G., Liu, J., Xu, X., Wang, S.-J. and Liu D.-
Y. (2011) A novel bankruptcy prediction model based on an adaptive fuzzy
k-nearest neighbor method. Knowledge-Based Systems 24(8): 1348-1359.
Cheng, M. and Madhavan, A. (2010) The Dynamics of Leveraged and Inverse
Exchange-Traded Funds. Journal of Investment Management 7(4): 43-62.
Cheng, I.-H. and Xiong, W. (2013) Why Do Hedgers Trade so Much?Working
Paper. Available online: https://ssrn.com/abstract=2358762.
Chernenko, S. and Sunderam, A. (2016) Liquidity Transformation in Asset
Management: Evidence from the Cash Holdings of Mutual Funds. Working
Paper. Available online: http://www.nber.org/papers/w22391.
Chernov, M. and Mueller, P. (2012) The Term Structure of Inﬂation Expec-
tations. Journal of Financial Economics 106(2): 367-394.
Cherry, J. (2004) The Limits of Arbitrage: Evidence from Exchange Traded
Funds. Working Paper. Available online: https://ssrn.com/abstract=
628061.
166
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 168

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Cheung, W. (2010) The Black-Litterman model explained. Journal of Asset
Management 11(4): 229-243.
Cheung, C.S., Kwan, C.C.Y. and Sarkar, S. (2010) Bond Portfolio Laddering:
A Mean-Variance Perspective. Journal of Applied Finance 20(1): 103-109.
Cheung, C.W., Kwan, C.C. and Yip, P.C. (1990) The hedging eﬀectiveness of
options and futures: a mean-gini approach. Journal of Futures Markets 10(1):
61-73.
Cheung, A., Roca, E. and Su, J.-J. (2015) Crypto-currency Bubbles: an Appli-
cation of the Phillips-Shi-Yu (2013) Methodology on Mt. Gox Bitcoin Prices.
Applied Economics 47(23): 2348-2358.
Chiang, T.C. and Jiang, C.X. (1995) Foreign exchange returns over short and
long horizons. International Review of Economics & Finance 4(3): 267-282.
Chiang, M.H. and Wang, C.Y. (2002) The Impact of Futures Trading on Spot
Index Volatility: Evidence from Taiwan Index Futures. Applied Economics
Letters 9(6): 381-385.
Chidambaran, N.K., Fernando, C.S. and Spindt, P.A. (2001) Credit enhance-
ment through ﬁnancial engineering: Freeport McMoRan’s gold-denominated
depositary shares. Journal of Financial Economics 60(2-3): 487-528.
Chin, J.Y.F., Prevost, A.K. and Gottesman, A.A. (2002) Contrarian invest-
ing in a small capitalization market: Evidence from New Zealand. Financial
Review 37(3): 421-446.
Chinco, A. and Mayer, C. (2012) Distant speculators and asset bubbles in the
housing market. Working Paper. Available online: http://www.econ.yale.
edu/~shiller/behfin/2012-04-11/Chinco_Mayer.pdf.
Chinloy, P. (1989) The Probability of Prepayment. Journal of Real Estate
Finance and Economics 2(4): 267-283.
Cho, M. (1996) House Price Dynamics: A Survey of Theoretical and Empirical
Issues. Journal of Housing Research 7(2): 145-172.
Choi, M.S. (2011) Momentary exchange rate locked in a triangular mechanism
of international currency. Applied Economics 43(16): 2079-2087.
Choi, D., Getmansky, M., Henderson, B. and Tookes, H. (2010) Convertible
bond arbitrageurs as suppliers of capital. Review of Financial Studies 23(6):
2492-2522.
167
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 169

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Choi, D., Getmansky, M. and Tookes, H. (2009) Convertible bond arbitrage,
liquidity externalities, and stock prices. Journal of Financial Economics 91(2):
227-251.
Choi, H.I., Kwon, S.-H., Kim, J.Y. and Jung, D.-S. (2014) Commodity Futures
Term Structure Model. Bulletin of the Korean Mathematical Society 51(6):
1791-1804.
Chong, E., Han, C. and Park, F.C. (2017) Deep learning networks for stock
market analysis and prediction: Methodology, data representations, and case
studies. Expert Systems with Applications 83: 187-205.
Chong, J. and Miﬀre, J. (2010) Conditional Correlation and Volatility in Com-
modity Futures and Traditional Asset Markets. Journal of Alternative Invest-
ments 12(3): 61-75.
Chordia, T., Goyal, A., Sadka, G., Sadka, R. and Shivakumar, L. (2009) Liq-
uidity and the Post-Earnings-Announcement Drift.Financial Analysts Journal
65(4): 18-32.
Chordia, T. and Shivakumar, L. (2002) Momentum, Business Cycle, and Time-
Varying Expected Returns. Journal of Finance 57(2): 985-1019.
Chordia, T. and Shivakumar, L. (2006) Earnings and price momentum. Jour-
nal of Financial Economics 80(3): 627-656.
Choro´ s-Tomczyk, B., H¨ ardle, W.K. and Okhrin, O. (2016) A semiparametric
factor model for CDO surfaces dynamics. Journal of Multivariate Analysis
146: 151-163.
Choudhry, M. (2004) The credit default swap basis: analysing the relation-
ship between cash and synthetic credit markets. Journal of Derivatives Use,
Trading and Regulation 10(1): 8-26.
Choudhry, M. (2006) Revisiting the Credit Default Swap Basis: Further Anal-
ysis of the Cash and Synthetic Credit Market Diﬀerential. Journal of Struc-
tured Finance 11(4): 21-32.
Choudhry, M. (2007) Trading the CDS Basis: Illustrating Positive and Nega-
tive Basis Arbitrage Trades. Journal of Trading 2(1): 79-94.
Christensen, M. (1999) Duration and Convexity for Bond Portfolios. Finanz-
markt und Portfolio Management 13(1): 66-72.
Christensen, P.E. and Fabozzi, F.J. (1985) Bond Immunization: An Asset
Liability Optimization Strategy. In: Fabozzi, F.J. and Pollack, I.M. (eds.) The
Handbook of Fixed Income Securities. (2nd ed.) Homewood, IL: Dow Jones-
Irwin, pp. 676-703.
168
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 170

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Christensen, J.H.E. and Gillan, J.M. (2012) Could the U.S. Treasury Bene-
ﬁt from Issuing More TIPS? Federal Reserve Bank of San Francisco, Work-
ing Papers Series , No. 2011-16. Available online: https://www.frbsf.org/
economic-research/files/wp11-16bk.pdf.
Christensen, J.H.E., Lopez, J.A. and Rudebusch, G.D. (2010) Inﬂation Ex-
pectations and Risk Premiums in an Arbitrage-Free Model of Nominal and
Real Bond Yields. Journal of Money, Credit, and Banking 42(6): 143-178.
Christensen, B.J. and Prabhala, N.R. (1998) The relation between implied
and realized volatility. Journal of Financial Economics 50(2): 125-150.
Christiansen, C. and Lund, J. (2005) Revisiting the Shape of the Yield
Curve: The Eﬀect of Interest Rate Volatility.Working Paper. Available online:
https://ssrn.com/abstract=264139.
Christie-David, R. and Chaudry, M. (2001) Coskewness and cokurtosis in fu-
tures markets. Journal of Empirical Finance 8(1): 55-81.
Christoﬀersen, S.E.K., G´ eczy, C.C., Musto, D.K. and Reed, A.V. (2005) Cross-
border Dividend Taxation and the Preferences of Taxable and Nontaxable
Investors: Evidence From Canada. Journal of Financial Economics 78(1):
121-144.
Christoﬀersen, S.E.K., Reed, A.V., G´ eczy, C.C. and Musto, D.K. (2003) The
Limits to Dividend Arbitrage: Implications for Cross Border Investment.
Working Paper. Available online: https://ssrn.com/abstract=413867.
Chua, C.T., Koh, W.T.H. and Ramaswamy, K. (2006) Proﬁting from Mean-
Reverting Yield Curve Trading Strategies. Journal of Fixed Income 15(4):
20-33.
Chuang, H. (2015) Time Series Residual Momentum. Working Paper. Avail-
able online: http://www.econ.tohoku.ac.jp/econ/datascience/DDSR-DP/
no38.pdf.
Chuang, H. and Ho, H.-C. (2014) Implied Price Risk and Momentum Strategy.
Review of Finance 18(2): 591-622.
Chui, A.C.W., Titman, S. and Wei, K.C.J. (2003a) The Cross-Section of Ex-
pected REIT Returns. Real Estate Economics 31(3): 451-479.
Chui, A.C.W., Titman, S. and Wei, K.C.J. (2003b) Intra-industry momentum:
the case of REITs. Journal of Financial Markets 6(3): 363-387.
Chung, S.Y. (2000) Review of Macro Trading and Investment Strategies:
Macroeconomic Arbitrage in Global Markets. Journal of Alternative Invest-
ments 3(1): 84-85.
169
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 171

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Ciaian, P., Rajcaniova, M. and Kancs, D. (2015) The economics of BitCoin
price formation. Applied Economics 48(19): 1799-1815.
Cirelli, S., Vitali, S., Ortobelli Lozza, S. and Moriggia, V. (2017) A conser-
vative discontinuous target volatility strategy. Investment Management and
Financial Innovations 14(2-1): 176-190.
Clare, A.D., Ioannides, M. and Skinner, F.S. (2000) Hedging Corporate Bonds
with Stock Index Futures: A Word of Caution. Journal of Fixed Income 10(2):
25-34.
Clarida, R.H., Davis, J.M. and Pedersen, N. (2009) Currency carry trade
regimes: Beyond the Fama regression. Journal of International Money and
Finance 28(8): 1375-1389.
Clarida, R. and Waldman, D. (2007) Is Bad News About Inﬂation Good News
for the Exchange Rate? Working Paper. Available online: http://www.nber.
org/papers/w13010.pdf.
Clark, G.L. (2017) Financial intermediation, infrastructure investment and
regional growth. Area Development and Policy 2(3): 217-236.
Clark, G.L., Monk, A.H.B., Orr, R. and Scott, W. (2012) The new Era of
infrastructure investing. Pensions: An International Journal 17(2): 103-111.
Clark, T.E. and Terry, S.J. (2010) Time Variation in the Inﬂation Passthrough
of Energy Prices. Journal of Finance 42(7): 1419-1433.
Clark, T.A. and Weinstein, M.I. (1983) The behavior of the common stock of
bankrupt ﬁrms. Journal of Finance 38(2): 489-504.
Clarke, R.G., de Silva, H. and Thorley, S. (2006) Minimum-Variance Portfolios
in the U.S. Equity Market. Journal of Portfolio Management 33(1): 10-24.
Clarke, R.G., de Silva, H. and Thorley, S. (2010) Know Your VMS Exposure.
Journal of Portfolio Management 36(2): 52-59.
Clarke, R.G., de Silva, H. and Thorley, S. (2013) Fundamentals of Futures and
Options. New York, NY: The Research Foundation of CFA Institute.
Cliﬀord, C.P., Fulkerson, J.A. and Jordan, B.D. (2014) What Drives ETF
Flows? Financial Review 49(3): 619-642.
Clinton, K. (1988) Transactions costs and covered interest arbitrage: Theory
and evidence. Journal of Political Economy 96(2): 358-370.
Cochrane, J.H. (1999) Portfolio Advice for a Multifactor World. Federal Re-
serve Bank of Chicago, Economic Perspectives 23(3): 59-78.
170
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 172

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Cochrane, J.H. and Piazzesi, M. (2005) Bond Risk Premia. American Eco-
nomic Review 95(1): 138-160.
Coﬀey, N., Hrung, W.B. and Sarkar, A. (2009) Capital constraints, counter-
party risk, and deviations from covered interest rate parity. Federal Reserve
Bank of New York Staﬀ Reports , No. 393. Available online:
https://www.newyorkfed.org/medialibrary/media/research/staff_
reports/sr393.pdf.
Cohen, G. (2005) The bible of options strategies: the deﬁnitive guide for practi-
cal trading strategies. Upper Saddle River, NJ: Financial Times Prentice Hall.
Cole, C.A., Kastens, T.L., Hampel, F.A. and Gow, L.R. (1999) A calendar
spread trading simulation of seasonal processing spreads. In: Proceedings of
the NCCC-134 Conference on Applied Commodity Price Analysis, Forecast-
ing, and Market Risk Management. Available online: http://www.farmdoc.
illinois.edu/nccc134/conf_1999/pdf/confp14-99.pdf.
Cole, C.S. and Young, P.J. (1995) Modiﬁed duration and convexity with semi-
annual compounding. Journal of Economics and Finance 19(1): 1-15.
Colianni, S., Rosales, S. and Signorotti, M. (2015) Algorithmic Trading of
Cryptocurrency Based on Twitter Sentiment Analysis. Working Paper. Avail-
able online: http://cs229.stanford.edu/proj2015/029_report.pdf.
Collin-Dufresne, P. and Solnik, B. (2001) On the Term Structure of Default
Premia in the Swap and LIBOR Markets. Journal of Finance 56(3): 1095-
1115.
Cong, J., Tan, K.S. and Weng, C. (2013) VAR-Based Optimal Partial Hedging.
ASTIN Bulletin: The Journal of the IAA 43(3): 271-299.
Cong, J., Tan, K.S. and Weng, C. (2014) CVaR-Based Optimal Partial Hedg-
ing. Journal of Risk 16(3): 49-83.
Connor, G. and Leland, H. (1995) Cash Management for Index Tracking.
Financial Analysts Journal 51(6): 75-80.
Connor, G. and Woo, M. (2004) An Introduction to hedge funds. Working
Paper. Available online: http://eprints.lse.ac.uk/24675/1/dp477.pdf.
Conover, C.M., Jensen, G., Johnson, R. and Mercer, M. (2008) Sector Rotation
and Monetary Conditions. Journal of Investing 28(1): 34-46.
Conover, C.M., Jensen, G.R., Johnson, R.R. and Mercer, J.M. (2010) Is Now
the Time to Add Commodities to Your Portfolio? Journal of Investing 19(3):
10-19.
171
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 173

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Conrad, J., Dittmar, R.F. and Ghysels, E. (2013) Ex Ante Skewness and
Expected Stock Returns. Journal of Finance 68(1): 85-124.
Conrad, J.S., Hameed, A. and Niden, C. (1994) Volume and autocovariances
in short-horizon individual security returns. Journal of Finance 49(4): 1305-
1329.
Conrad, J. and Kaul, G. (1998) An Anatomy of Trading Strategies. Review of
Financial Studies 11(3): 489-519.
Cont, R. and Minca, A. (2013) Recovering Portfolio Default Intensities Implied
by CDO Quotes. Mathematical Finance 23(1): 94-121.
Cook, T.Q. and LaRoche, R.B. (eds.) (1993)Instruments of the money market.
(7th ed.) Richmond, Virginia: Federal Reserve Bank of Richmond.
Cook, T.Q. and Rowe, T.D. (eds.) (1986) Instruments of the money market.
(6th ed.) Richmond, Virginia: Federal Reserve Bank of Richmond.
Cooper, T. (2010) Alpha Generation and Risk Smoothing Using Managed
Volatility. Working Paper. Available online: https://ssrn.com/abstract=
1664823.
Cooper, M., Downs, D.H. and Patterson, G.A. (1999) Real Estate Securi-
ties and a Filter-based, Short-term Trading Strategy. Journal of Real Estate
Research 18(2): 313-334.
Cooper, M.J., Gutierrez, R.C., Jr. and Hameed, A. (2004) Market States and
Momentum. Journal of Finance 59(3): 1345-1365.
Cooper, I. and Priestley, R. (2008) Time-Varying Risk Premiums and the
Output Gap. Review of Financial Studies 22(7): 2801-2833.
Copeland, T.E. and Galai, D. (1983) Information Eﬀects on the bid-ask spread.
Journal of Finance 38(5): 1457-1469.
Corbally, M. and Dang, P. (2002) Underlying Markets and Indexes. In: Banks,
E. (ed.) Weather Risk Management: Market, Products and Applications. Lon-
don, UK: Palgrave Macmillan.
Corbett, M. (2006) Find it, ﬁx it, ﬂip it! Make millions in real estate – one
house at a time. New York, NY: Plume.
Cornell, B. and French, K.R. (1983) The pricing of stock index futures.Journal
of Futures Markets 3(1): 1-14.
Cornelli, F. and Li, D.D. (2002) Risk Arbitrage in Takeovers. Review of Fi-
nancial Studies 15(3): 837-868.
172
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 174

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Corrado, C.J. and Miller, T.W., Jr. (2005) The forecast quality of CBOE
implied volatility indexes. Journal of Futures Markets 25(4): 339-373.
Corrado, C.J. and Su, T. (1997) Implied volatility skews and stock return
skewness and kurtosis implied by stock option prices. European Journal of
Finance 3(1): 73-85.
Correia, M.M., Richardson, S.A. and Tuna, A.I. (2012) Value Investing in
Credit Markets. Review of Accounting Studies 17(3): 572-609.
Cosandier, P.-A. and Lang, B.R. (1981) Interest rate parity tests: Switzerland
and some major western countries. Journal of Banking & Finance 5(2): 187-
200.
Cousin, A. and Laurent, J. (2012) Dynamic Hedging of Synthetic CDO
Tranches: Bridging the Gap between Theory and Practice. In: Bielecki, T.R.,
Brigo, D. and Patras, F. (eds.) Credit Risk Frontiers . Hoboken, NJ: John
Wiley & Sons, Inc., Chapter 6.
Coval, J.D. and Shumway, T. (2001) Expected options returns. Journal of
Finance 56(3): 983-1009.
Cover, T.M. (1984) An algorithm for maximizing expected log investment
return. IEEE Transactions on Information Theory 30(2): 369-373.
Cox, D. (2015) Handbook of Anti Money Laundering. Chichester, UK: John
Wiley & Sons, Ltd.
Crabbe, L.E. and Fabozzi, F.J. (2002) Corporate Bond Portfolio Management.
Hoboken, NJ: John Wiley & Sons, Inc.
Creamer, G.G. and Freund, Y. (2007) A Boosting Approach for Automated
Trading. Journal of Trading 2(3): 84-96.
Creamer, G.G. and Freund, Y. (2010) Automated Trading with Boosting and
Expert Weighting. Quantitative Finance 10(4): 401-420.
Cremers, M. and Weinbaum, D. (2010) Deviations from Put-Call Parity and
Stock Return Predictability. Journal of Financial and Quantitative Analysis
45(2): 335-367.
Creti, A., Jo¨ ets, M. and Mignon, V. (2013) On the links between stock and
commodity markets’ volatility. Energy Economics 37: 16-28.
Cross, R. and Kozyakin, V. (2015) Fact and ﬁctions in FX arbitrage processes.
Journal of Physics: Conference Series 585: 012015.
173
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 175

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Cultrera, L. and Br´ edart, X. (2015) Bankruptcy prediction: the case of Belgian
SMEs. Review of Accounting and Finance 15(1): 101-119.
Czaja, M.-G., Kaufmann, P. and Scholz, H. (2013) Enhancing the proﬁtability
of earnings momentum strategies: The role of price momentum, information
diﬀusion and earnings uncertainty.Journal of Investment Strategies 2(4): 3-57.
Dahlgran, R.A. (2000) Cross-hedging the cottonseed crush: A case study.
Agribusiness 16(2): 141-158.
Daigler, R.T. (2007) Spread volume for currency futures.Journal of Economics
and Finance 31(1): 12-19.
Daigler, R.T. and Copper, M. (1998) A Futures Duration-Convexity Hedging
Method. Financial Review 33(4): 61-80.
Dale, A. and Currie, E. (2015) An alternative funding model for agribusiness
research in Canada. Agricultural Sciences 6(9): 961-969.
Damghani, B.M. and Kos, A. (2013) De-arbitraging With a Weak Smile: Ap-
plication to Skew Risk. Wilmott Magazine 2013(64): 40-49.
Damiani, D. (2012) The Case for Cash. CFA Institute Magazine 23(4): 8-9.
D’Amico, S., Kim, D. and Wei, M. (2018) Tips from TIPS: The Informational
Content of Treasury Inﬂation-Protected Security Prices. Journal of Financial
and Quantitative Analysis 53(1): 395-436.
Daniel, K. (2001) The Power and Size of Mean Reversion Tests. Journal of
Empirical Finance 8(5): 493-535.
Daniel, K. and Moskowitz, T.J. (2016) Momentum crashes. Journal of Finan-
cial Economics 122(2): 221-247.
D’Antonio, L. (2008) Equity Collars as Alternative to Asset Allocation. Jour-
nal of Financial Service Professionals 62(1): 67-76.
Dao, T.-L. (2014) Momentum strategies with the L1 ﬁlter. Journal of Invest-
ment Strategies 3(4): 57-82.
Das, S. (2005) Credit Derivatives: Trading & Management of Credit & Default
Risk. (3rd ed.) Hoboken, NJ: John Wiley & Sons, Inc.
da S. Gomes, G.S., Ludermir, T.B. and Lima, L.M.M.R. (2011) Comparison
of new activation functions in neural network for forecasting ﬁnancial time
series. Neural Computing and Applications 20(3): 417-439.
174
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 176

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Dash, R. and Dash, P.K. (2016) A hybrid stock trading framework integrating
technical analysis with machine learning techniques. Journal of Finance and
Data Science 2(1): 42-57.
Da Silva, A.S., Lee, W. and Pornrojnangkool, B. (2009) The Black-Litterman
model for active portfolio management. Journal of Portfolio Management
35(2): 61-70.
Daumas, L.D. (2017) Hedging stocks through commodity indexes: a DCC-
GARCH approach. Working Paper. Available online: https://impa.br/
wp-content/uploads/2017/11/RiO2017-PP_FAiube.pdf.
Davidson, A.S., Herskovitz, M.D. and Van Drunen, L.D. (1988) The reﬁnanc-
ing threshold pricing model: An economic approach to valuing MBS. Journal
of Real Estate Finance and Economics 1(2): 117-130.
Davis, J.L. (1996) The cross-section of stock returns and survivorship bias:
Evidence from delisted stocks. Quarterly Review of Economics and Finance
36(3): 365-375.
Davis, M. (2001) Pricing Weather Derivatives by Marginal Value.Quantitative
Finance 1(3): 305-308.
Davis, M.H.A. (2006) Optimal Hedging with Basis Risk. In: Kabanov, Y.,
Liptser, R. and Stoyanov, J. (eds.) From Stochastic Calculus to Mathematical
Finance. Berlin, Germany: Springer.
Davis, M. and Lleo, S. (2012) Fractional Kelly strategies in continuous time:
Recent developments. In: MacLean, L.C. and Ziemba, W. (eds.) Handbook of
the Fundamentals of Financial Decision Making. Singapore: World Scientiﬁc
Publishing.
Davis, M. and Lo, V. (2001) Infectious defaults. Quantitative Finance 1(4):
382-387.
Deacon, M., Derry, A. and Mirfendereski, D. (2004) Inﬂation-indexed Secu-
rities: Bonds, Swaps and other Derivatives. Chichester, UK: John Wiley &
Sons, Ltd.
Deardorﬀ, A.V. (1979) One-Way Arbitrage and Its Implications for the Foreign
Exchange Markets. Journal of Political Economy 87(2): 351-364.
de Boer, P.-T., Kroese, D.P., Mannor, S. and Rubinstein, R.Y. (2005) A Tu-
torial on the Cross-Entropy Method. Annals of Operations Research 134(1):
19-67.
175
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 177

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
DeBondt, W.F.M. and Thaler, R.H. (1985) Does stock market overreact?
Journal of Finance 40(3): 793-807.
De Carvalho, R.L., Dugnolle, P., Lu, X. and Moulin, P. (2014) Low-Risk
Anomalies in Global Fixed Income: Evidence from Major Broad Markets.
Journal of Fixed Income 23(4): 51-70.
Dechant, T. and Finkenzeller, K. (2013) How much into infrastructure? Ev-
idence from dynamic asset allocation. Journal of Property Research 30(2):
103-127.
Dechario, T., Mosser, P., Tracy, J., Vickery, J. and Wright, J. (2010) A
Private Lender Cooperative Model for Residential Mortgage Finance. Federal
Reserve Bank of New York Staﬀ Reports , No. 466. Available online:
https://www.newyorkfed.org/medialibrary/media/research/staff_
reports/sr466.pdf.
De Jong, A., Dutordoir, M. and Verwijmeren, P. (2011) Why do convert-
ible issuers simultaneously repurchase stock? An arbitrage-based explanation.
Journal of Financial Economics 100(1): 113-129.
De La Pe˜ na, J.I., Garayeta, A. and Iturricastillo, I. (2017) Dynamic immunisa-
tion does not imply cash ﬂow matching: a hard application to Spain.Economic
Research – Ekonomska Istraˇ zivanja30(1): 238-255.
DeLisle, J., Doran, J. and Krieger, K. (2014) Volatility as an Asset Class:
Holding VIX in a Portfolio. Working Paper. Available online: https://ssrn.
com/abstract=2534081.
DeMaskey, A.L. (1995) A Comparison of the Eﬀectiveness of Currency Futures
and Currency Options in the Context of Foreign Exchange Risk Management.
Managerial Finance 21(4): 40-51.
DeMaskey, A.L. (1997) Single and Multiple Portfolio Cross-Hedging with Cur-
rency Futures. Multinational Finance Journal 1(1): 23-46.
DeMaskey, A.L. and Pearce, J.A. (1998) Commodity and Currency Futures
Cross-Hedging of ASEAN Currency Exposures.Journal of Transnational Man-
agement Development 4(1): 5-24.
Demeterﬁ, K., Derman, E., Kamal, M. and Zou, J. (1999) A guide to volatility
and variance swaps. Journal of Derivatives 6(4): 9-32.
DeMiguel, V., Plyakha, Y., Uppal, R. and Vilkov, G. (2013) Improving Port-
folio Selection Using Option-Implied Volatility and Skewness. Journal of Fi-
nancial and Quantitative Analysis 48(6): 1813-1845.
176
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 178

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
DeMoura, C.E., Pizzinga, A. and Zubelli, J. (2016) A pairs trading strategy
based on linear state space models and the Kalman ﬁlter.Quantitative Finance
16(10): 1559-1573.
Dempster, M.A.H. and Jones, C.M. (2002) Can channel pattern trading be
proﬁtably automated? European Journal of Finance 8(3): 275-301.
Deng, Q. (2008) Volatility Dispersion Trading. Working Paper. Available on-
line: https://ssrn.com/abstract=1156620.
Deng, S.-J., Johnson, B. and Sogomonian, A. (2001) Exotic electricity options
and the valuation of electricity generation and transmission assets. Decision
Support Systems 30(3): 383-392.
Deng, G., McCann, C. and Wang, O. (2012) Are VIX Futures ETPs Eﬀective
Hedges? Journal of Index Investing 3(3): 35-48.
Dennis, P. and Mayhew, S. (2002) Risk-Neutral Skewness: Evidence from
Stock Options. Journal of Financial and Quantitative Analysis 37(3): 471-
493.
Dennis, P., Mayhew, S. and Stivers, C. (2006) Stock Returns, Implied Volatil-
ity Innovations, and the Asymmetric Volatility Phenomenon. Journal of Fi-
nancial and Quantitative Analysis 41(2): 381-406.
Denton, J.W. and Hung, M.S. (1996) A comparison of nonlinear optimization
methods for supervised learning in multilayer feedforward neural networks.
European Journal of Operational Research 93(2): 358-368.
de Oliveira, F.A., Nobre, C.N. and Z´ arate, L.E. (2013) Applying Artiﬁcial
Neural Networks to prediction of stock price and improvement of the direc-
tional prediction index – Case study of PETR4, Petrobras, Brazil. Expert
Systems with Applications 40(18): 7596-7606.
Depken, C.A., Hollans, H. and Swidler, S. (2009) An empirical analysis of
residential property ﬂipping. Journal of Real Estate Finance and Economics
39(3): 248-263.
Depken, C.A., Hollans, H. and Swidler, S. (2011) Flips, ﬂops and foreclosures:
Anatomy of a real estate bubble. Journal of Financial Economic Policy 3(1):
49-65.
Derman, E. and Kani, I. (1994) Riding on a Smile. Risk 7(2): 139-145.
de Roon, F.A., Nijman, T.E. and Veld, C. (1998) Pricing Term Structure Risk
in Futures Markets. Journal of Financial and Quantitative Analysis 33(1):
139-157.
177
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 179

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
de Roon, F.A., Nijman, T.E. and Veld, C. (2000) Hedging pressure eﬀects in
futures markets. Journal of Finance 55(3): 1437-1456.
Derwall, J., Huij, J., Brounen, D. and Marquering, W. (2009) REIT Momen-
tum and the Performance of Real Estate Mutual Funds. Financial Analysts
Journal 65(5): 24-34.
Derwall, J., Huij, J. and De Zwart, G.B. (2009) The Short-Term Corpo-
rate Bond Anomaly. Working Paper. Available online: https://ssrn.com/
abstract=1101070.
D’Este, R. (2014) The Eﬀect of Stolen Goods Markets on Crime: Evi-
dence from a Quasi-Natural Experiment. Working Paper. Available online:
https://warwick.ac.uk/fac/soc/economics/research/workingpapers/
2014/twerp_1040b_deste.pdf.
Detemple, J. and Rindisbacher, M. (2010) Dynamic Asset Allocation: Port-
folio Decomposition Formula and Applications. Review of Financial Studies
23(1): 25-100.
Detlefsen, K. and H¨ ardle, W.K. (2013) Variance swap dynamics.Quantitative
Finance 13(5): 675-685.
Dewally, M., Ederington, L.H. and Fernando, C.S. (2013) Determinants of
Trader Proﬁts in Commodity Futures Markets. Review of Financial Studies
26(10): 2648-2683.
De Wit, I. (2010) International Diversiﬁcation Strategies for Direct Real Es-
tate. Journal of Real Estate Finance and Economics 41(4): 433-457.
De Wit, J. (2006) Exploring the CDS-Bond Basis. Working Paper. Available
online: https://ssrn.com/abstract=1687659.
de Wit, E.R. and van der Klaauw, B. (2013) Asymmetric Information and
List-Price Reductions in the Housing Market. Regional Science and Urban
Economics 43(3): 507-520.
De Zwart, G., Markwat, T., Swinkels, L. and van Dijk, D. (2009) The economic
value of fundamental and technical information in emerging currency markets.
Journal of International Money and Finance 28(4): 581-604.
Dichev, I. (1998) Is the risk of bankruptcy a systematic risk? Journal of
Finance 53(3): 1131-1147.
Diebold, F.X. and Li, C. (2002) Forecasting the term structure of government
bond yields. Journal of Econometrics 130(2): 337-364.
178
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 180

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Diebold, F.X., Rudebusch, G.D. and Aruoba, S.B. (2006) The macroeconomy
and the yield curve: a dynamic latent factor approach. Journal of Economet-
rics 131(1-2): 309-338.
Ding, J.J. and Sherris, M. (2011) Comparison of market models for measuring
and hedging synthetic CDO tranche spread risks. European Actuarial Journal
1(S2): 261-281.
Disatnik, D., Duchin, R. and Schmidt, B. (2014) Cash Flow Hedging and
Liquidity Choices. Review of Finance 18(2): 715-748.
Dischel, B. (1998a) At last: A model for weather risk. Energy and Power Risk
Management 11(3): 20-21.
Dischel, B. (1998b) Black-Scholes won’t do. Energy and Power Risk Manage-
ment 11(10): 8-9.
Dischel, B. (1999) Shaping history for weather risk management. Energy and
Power Risk Management 12(8): 13-15.
Do, B. and Faﬀ, R. (2010) Does simple pairs trading still work? Financial
Analysts Journal 66(4): 83-95.
Do, B. and Faﬀ, R. (2012) Are pairs trading proﬁts robust to trading costs?
Journal of Financial Research 35(2): 261-287.
Doan, M.P., Alexeev, V. and Brooks, R. (2014) Concurrent momentum and
contrarian strategies in the Australian stock market. Australian Journal of
Management 41(1): 77-106.
Dobson, M.W.R. (1984) Global Investment Portfolios: The United Kingdom
and Scandinavia. ICFA Continuing Education Series 1984(4): 56-60.
Doeswijk, R., Lam, T. and Swinkels, L. (2014) The Global Multi-Asset Market
Portfolio, 1959-2012. Financial Analysts Journal 70(2): 26-41.
Doeswijk, R. and van Vliet, P. (2011) Global tactical sector allocation: a
quantitative approach. Journal of Portfolio Management 28(1): 29-47.
Dolan, C.P. (1999) Forecasting the Yield Curve Shape. Journal of Fixed In-
come 9(1): 92-99.
Dolvin, S.D. (2009) ETFs: Arbitrage opportunities and market forecasting.
Journal of Index Investing 1(1): 107-116.
Dolvin, S. and Kirby, J. (2011) Momentum Trading in Sector ETFs. Journal
of Index Investing 2(3): 50-57.
179
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 181

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Donchian, R.D. (1960) High ﬁnance in copper. Financial Analysts Journal
16(6): 133-142.
Dong, J.-C., Liu, J.-X., Wang, C.-H., Yuan, H. and Wang, W.-J. (2009) Pricing
Mortgage-Backed Security: An Empirical Analysis. Systems Engineering –
Theory & Practice 29(12): 46-52.
Dong, Z. and Zhou, D.-X. (2008) Learning gradients by a gradient descent
algorithm. Journal of Mathematical Analysis and Applications 341(2): 1018-
1027.
Donier, J. and Bouchaud, J.-P. (2015) Why Do Markets Crash? Bitcoin Data
Oﬀers Unprecedented Insights. PLoS ONE 10(10): e0139356.
Donninger, C. (2014) VIX Futures Basis Trading: The Calvados-Strategy 2.0.
Working Paper. Available online: https://ssrn.com/abstract=2379985.
Donninger, C. (2015) Trading the Patience of Mrs. Yellen. A Short Vix-Futures
Strategy for FOMC Announcement Days. Working Paper. Available online:
https://ssrn.com/abstract=2544445.
Doran, J.S. and Krieger, K. (2010) Implications for Asset Returns in the Im-
plied Volatility Skew. Financial Analysts Journal 66(1): 65-76.
Doran, J.S., Peterson, D.R. and Tarrant, B.C. (2007) Is there information in
the volatility skew? Journal of Futures Markets 27(10): 921-959.
Dorﬂeitner, G. and Wimmer, M. (2010) The pricing of temperature futures
at the Chicago Mercantile Exchange. Journal of Banking & Finance 34(6):
1360-1370.
Dornier, F. and Queruel, M. (2000) Caution to the wind. Energy and Power
Risk Management 13(8): 30-32.
Doskov, N. and Swinkels, L. (2015) Empirical evidence on the currency carry
trade, 1900-2012. Journal of International Money and Finance 51: 370-389.
Douglas, R. (ed.) (2007) Credit Derivative Strategies: New Thinking on Man-
aging Risk and Return. New York, NY: Bloomberg Press.
Dowd, K. and Hutchinson, M. (2015) Bitcoin Will Bite the Dust.Cato Journal
35(2): 357-382.
Downing, C., Jaﬀee, D. and Wallace, N. (2009) Is the Market for Mortgage-
Backed Securities a Market for Lemons? Review of Financial Studies 22(7):
2457-2494.
180
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 182

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Doyle, J.T., Lundholm, R.J. and Soliman, M.T. (2006) The extreme future
stock returns following I/B/E/S earnings surprises. Journal of Accounting Re-
search 44(5): 849-887.
Draper, P., Faﬀ, R.W. and Hillier, D. (2006) Do Precious Metals Shine? An
Investment Perspective. Financial Analysts Journal 62(2): 98-106.
Dreyfus, S.E. (1990) Artiﬁcial neural networks, back propagation, and the
Kelley-Bryson gradient procedure. Journal of Guidance, Control, and Dynam-
ics 13(5): 926-928.
Driessen, J., Maenhout, P.J. and Vilkov, G. (2009) The Price of Correlation
Risk: Evidence from Equity Options. Journal of Finance 64(3): 1377-1406.
Driessen, J., Nijman, T. and Simon, Z. (2017) The Missing Piece of the Puzzle:
Liquidity Premiums in Inﬂation-Indexed Markets. Working Paper. Available
online: https://ssrn.com/abstract=3042506.
Drobetz, W. (2001) How to Avoid the Pitfalls in Portfolio Optimization?
Putting the Black-Litterman Approach at Work. Financial Markets and Port-
folio Management 15(1): 59-75.
Drobny, S. (2006) Inside the House of Money: Top Hedge Fund Traders on
Proﬁting in the Global Markets. Hoboken, NJ: John Wiley & Sons, Inc.
Droms, W.G. and Walker, D.A. (2001) Performance persistence of interna-
tional mutual funds. Global Finance Journal 12(2): 237-248.
Du, W., Tepper, A. and Verdelhan, A. (2018) Deviations from Covered Interest
Rate Parity. Journal of Finance (forthcoming). DOI: https://doi.org/10.
1111/jofi.12620. Available online: https://ssrn.com/abstract=2768207.
Duarte, J., Longstaﬀ, F.A. and Yu, F. (2006) Risk and Return in Fixed-
Income Arbitrage: Nickels in Front of a Steamroller? Review of Financial
Studies 20(3): 769-811.
Dubil, R. (2011) Hedge Funds: Alpha, Beta and Replication Strategies. Jour-
nal of Financial Planning 24(10): 68-77.
Duca, E., Dutordoir, M., Veld, C. and Verwijmeren, P. (2012) Why are
convertible bond announcements associated with increasingly negative issuer
stock returns? An arbitrage based explanation. Journal of Banking & Finance
36(11): 2884-2899.
Duchin, R. (2010) Cash Holdings and Corporate Diversiﬁcation. Journal of
Finance 65(3): 955-992.
181
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 183

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Dudley, W., Roush, J.E. and Steinberg, M. (2009) The Case for Tips: An
Examination of the Costs and Beneﬁts. Federal Reserve Bank of New York,
Economic Policy Review 15(1): 1-17.
Duﬃe, D. (1996) Special repo rates. Journal of Finance 51(2): 493-526.
Duﬃe, D. (2004) Time to adapt copula methods for modelling credit risk
correlation. Risk, April 2004, p. 77.
Duﬃe, D. (2017) The covered interest parity conundrum. Risk, May 2017.
Available online: https://www.risk.net/4353726.
Duﬃe, D. and Gˆ arleanu, N. (2001) Risk and Valuation of Collateralized Debt
Obligations. Financial Analysts Journal 57(1): 41-59.
Duﬃe, D. and Huang, M. (1996) Swap Rates and Credit Quality. Journal of
Finance 51(2): 921-949.
Duﬃe, D., Saita, L. and Wang, K. (2007) Multi-period corporate default pre-
diction with stochastic covariates. Journal of Financial Economics 83(3): 635-
665.
Duﬃe, D. and Singleton, K.J. (1997a) Modeling term structures of defaultable
bonds. Review of Financial Studies 12(4): 687-720.
Duﬃe, D. and Singleton, K.J. (1997b) An Econometric Model of the Term
Structure of Interest Rate Swap Yields. Journal of Finance 52(4): 1287-1321.
DuJardin, P. (2015) Bankruptcy prediction using terminal failure processes.
European Journal of Operational Research 242(1): 286-303.
Dukes, W.P., Frolich, C.J. and Ma, C.K. (1992) Risk arbitrage in tender oﬀers.
Journal of Portfolio Management 18(4): 47-55.
Dumas, B., Fleming, J. and Whaley, R. (1998) Implied Volatility Functions:
Empirical Tests. Journal of Finance 53(6): 2059-2106.
Dunis, C., Laws, J. and Evans, B. (2006) Trading futures spreads. Applied
Financial Economics 16(12): 903-914.
Dunis, C., Laws, J. and Evans, B. (2010) Trading and ﬁltering futures spread
portfolios. Journal of Derivatives & Hedge Funds 15(4): 274-287.
Dunis, C., Laws, J. and Rudy, J. (2013) Mean Reversion Based on Autocor-
relation: A Comparison Using the S&P 100 Constituent Stocks and the 100
Most Liquid ETFs. ETF Risk, October 2013, pp. 36-41.
182
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 184

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Dunn, K.B. and McConnell, J.J. (1981a) A Comparison of Alternative Mod-
els for Pricing GNMA Mortgage-Backed Securities. Journal of Finance 36(2):
471-484.
Dunn, K.B. and McConnell, J.J. (1981b) Valuation of GNMA Mortgage-
Backed Securities. Journal of Finance 36(3): 599-616.
Dupire, B. (1994) Pricing with a smile. Risk 7(1): 18-20.
Dusak, K. (1973) Futures Trading and Investor Returns: An Investigation
of Commodity Market Risk Premiums. Journal of Political Economy 81(6):
1387-1406.
Dutordoir, M., Lewis, C.M., Seward, J. and Veld, C. (2014) What we do and
do not know about convertible bond ﬁnancing. Journal of Corporate Finance
24: 3-20.
Dutt, H.R., Fenton, J., Smith, J.D. and Wang, G.H.K. (1997) Crop year
inﬂuences and variability of the agricultural futures spreads.Journal of Futures
Markets 17(3): 341-367.
Dwyer, G.P., Jr., Locke, P. and Yu, W. (1996) Index Arbitrage and Nonlinear
dynamics Between the S&P 500 Futures and Cash.Review of Financial Studies
9(1): 301-332.
Dyhrberg, A.H. (2015) Bitcoin, gold and the dollar – a GARCH volatility
analysis. Finance Research Letters 16: 85-92.
Dyhrberg, A.H. (2016) Hedging capabilities of bitcoin. Is it the virtual gold?
Finance Research Letters 16: 139-144.
Dyl, E.A. and Joehnk, M.D. (1981) Riding the Yield Curve: Does it Work?
Journal of Portfolio Management 7(3): 13-17.
Dyl, E.A. and Martin, S.A. (1986) Another Look at Barbells Versus Ladders.
Journal of Portfolio Management 12(3): 54-59.
Dynkin, L., Hyman, J., Konstantinovsky, V. and Roth, N. (2001) Building
an MBS Index: Conventions and Calculations. In: Fabozzi, F.J. (ed.) The
Handbook of Mortgage-Backed Securities. (5th ed.) New York, NY: McGraw-
Hill, Inc.
Dzikeviˇ cius, A. andˇSanranda, S. (2010) EMA versus SMA: Usage to forecast
Stock Markets: The Case of S&P 500 and OMX Baltic Benchmark. Verslas:
teorija ir praktika – Business: theory and practice 11(3): 248-255.
183
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 185

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Easley, D., L´ opez de Prado, M.M. and O’Hara, M. (2011) The microstruc-
ture of the ‘ﬂash crash’: ﬂow toxicity, liquidity crashes and the probability of
informed trading. Journal of Portfolio Management 37(2): 118-128.
Easley, D., L´ opez de Prado, M.M. and O’Hara, M. (2012) The volume clock:
Insights into the high frequency paradigm. Journal of Portfolio Management
39(1): 19-29.
Eastman, A.M. and Lucey, B.M. (2008) Skewness and asymmetry in futures
returns and volumes. Applied Financial Economics 18(10): 777-800.
Eberhart, A., Altman, E. and Aggarwal, R. (1999) The Equity Performance
of Firms Emerging from Bankruptcy. Journal of Finance 54(5): 1855-1868.
Eberhart, A.C. and Sweeney, R.J. (1992) Does the Bond Market Predict
Bankruptcy Settlements? Journal of Finance 47(3): 943-980.
Ebrahim, S. and Rahman, S. (2005) On the pareto-optimality of futures con-
tracts over Islamic forward contracts: Implications for the emerging Muslim
economies. Journal of Economic Behavior & Organization 56(2): 273-295.
Ederington, L.H. (1979) The hedging performance of the new futures markets.
Journal of Finance 34(1): 157-170.
Edwards, D.W. (2009) Energy Trading & Investing: Trading, Risk Manage-
ment and Structuring Deals in the Energy Market. New York, NY: McGraw-
Hill, Inc.
Edwards, F.R. (1988) Futures Trading and Cash Market Volatility: Stock
Index and Interest Rate Futures. Journal of Futures Markets 8(4): 421-439.
Edwards, R. and Magee, J. (1992) Technical Analysis of Stock Trends. New
York, NY: New York Institute of Finance.
Edwards, F.R. and Park, J.M. (1996) Do Managed Futures Make Good In-
vestments? Journal of Futures Markets 16(5): 475-517.
Edwards, S. and Susmel, R. (2003) Interest-Rate Volatility in Emerging Mar-
kets. Review of Economics and Statistics 85(2): 328-348.
Egginton, J.F., Van Ness, B.F. and Van Ness, R.A. (2016) Quote Stuﬃng.
Financial Management 45(3): 583-608.
Ehlgen, J. (1998) Distortionary eﬀects of the optimal Hodrick-Prescott ﬁlter.
Economics Letters 61(3): 345-349.
184
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 186

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Eichenbaum, M. and Evans, C.L. (1995) Some Empirical Evidence on the
Eﬀects of Shocks to Monetary Policy on Exchange Rates. Quarterly Journal
of Economics 110(4): 975-1009.
Eichholtz, P.M.A., Hoesli, M., MacGregor, B.D. and Nanthakumaran, N.
(1995) Real estate portfolio diversiﬁcation by property type and region. Jour-
nal of Property Finance 6(3): 39-59.
Eisdorfer, A. and Misirli, E. (2015) Distressed Stocks in Distressed Times.
Working Paper. Available online: https://ssrn.com/abstract=2697771.
Eisl, A., Gasser, S. and Weinmayer, K. (2015) Caveat Emptor: Does Bitcoin
Improve Portfolio Diversiﬁcation? Working Paper. Available online: https:
//ssrn.com/abstract=2408997.
Elder, A. (2014) The New Trading for a Living. Hoboken, NJ: John Wiley &
Sons, Inc.
Eldred, G.W. (2004) The Beginner’s Guide to Real Estate Investing. Hoboken,
NJ: John Wiley & Sons, Inc.
Elias, R.S., Wahab, M.I.M. and Fang, L. (2016) The spark spread and clean
spark spread option based valuation of a power plant with multiple turbines.
Energy Economics 59: 314-327.
El Kalak, I. and Hudson, R. (2016) The eﬀect of size on the failure probabilities
of SMEs: An empirical study on the US market using discrete hazard model.
International Review of Financial Analysis 43: 135-145.
Elliott, R., Siu, T. and Chan, L. (2007) Pricing volatility swaps under Hes-
ton’s stochastic volatility model with regime switching. Applied Mathematical
Finance 14(1): 41-62.
Elliott, R.J., van der Hoek, J. and Malcolm, W.P. (2005) Pairs trading. Quan-
titative Finance 5(3): 271-276.
Elton, E.J., Gruber, M.J. and Blake, C.R. (1996a) The Persistence of Risk-
Adjusted Mutual Fund Performance. Journal of Business 69(2): 133-157.
Elton, E.J., Gruber, M.J. and Blake, C.R. (1996b) Survivor Bias and Mutual
Fund Performance. Review of Financial Studies 9(4): 1097-1120.
Elton, E.J., Gruber, M.J. and Rentzler, J.C. (1987) Professionally Managed,
Publicly Traded Commodity Funds. Journal of Business 60(2): 175-199.
Emery, G.W. and Liu, Q. (2002) An analysis of the relationship between
electricity and natural gas futures prices. Journal of Futures Markets 22(2):
95-122.
185
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 187

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Engel, C. (1996) The Forward Discount Anomaly and the Risk Premium: A
Survey of Recent Evidence. Journal of Empirical Finance 3(2): 123-192.
Engle, R.F. and Granger, C.W.J. (1987) Co-integration and error correction:
Representation, estimation and testing. Econometrica 55(2): 251-276.
Engle, R. and Rosenberg, J. (2000) Testing the volatility term structure using
option hedging criteria. Journal of Derivatives 8(1): 10-28.
Engle, R.F. and Watson, M.W. (1987) The Kalman Filter: applications to fore-
casting and rational-expectation models. In: Bewley, T.F. (ed.) Fifth World
Conference: Advances in Econometrics , Vol. 1. Cambridge, UK: Cambridge
University Press.
Eraker, B. (2009) The Volatility Premium. Working Paper. Available online:
http://www.nccr-finrisk.uzh.ch/media/pdf/Eraker_23-10.pdf.
Eraker, B. and Wu, Y. (2014) Explaining the Negative Returns to VIX Fu-
tures and ETNs: An Equilibrium Approach. Working Paper. Available online:
https://ssrn.com/abstract=2340070.
Erb, C. and Harvey, C. (2006) The Strategic and Tactical Value of Commodity
Futures. Financial Analysts Journal 62(2): 69-97.
Erickson, M., Goolsbee, A. and Maydew, E. (2003) How Prevalent is Tax
Arbitrage? Evidence from the Market for Municipal Bonds. National Tax
Journal 56(1): 259-270.
Ertugrul, M. and Giambona, E. (2011) Property Segment and REIT Capital
Structure. Journal of Real Estate Finance and Economics 43(4): 505-526.
Espinoza, R.D. and Luccioni, L. (2002) Proper Risk Management: The Key
To Successful Brownﬁeld Development. WIT Transactions on Ecology and the
Environment 55: 297-306.
Eun, C.S. and Sabherwal, S. (2003) Cross-border listings and price discovery:
Evidence from U.S. listed Canadian stocks. Journal of Finance 58(2): 549-575.
Evans, M.D.D. (1998) Real Rates, Expected Inﬂation, and Inﬂation Risk Pre-
mia. Journal of Finance 53(1): 187-218.
Evans, C.L. and Marshall, D.A. (2007) Economic determinants of the nominal
treasury yield curve. Journal of Monetary Economics 54(7): 1986-2003.
Faber, M. (2007) A Quantitative Approach to Tactical Asset Allocation.Jour-
nal of Wealth Management 9(4): 69-79.
186
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 188

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Faber, M. (2015) Learning to Play Oﬀense and Defense: Combining Value
and Momentum from the Bottom Up, and the Top Down. Working Paper.
Available online: https://ssrn.com/abstract=2669202.
Faber, M. (2016) The Trinity Portfolio: A Long-Term Investing Framework
Engineered for Simplicity, Safety, and Outperformance.Working Paper. Avail-
able online: https://ssrn.com/abstract=2801856.
Fabozzi, F.J. (ed.) (2002) The Handbook of Financial Instruments. Hoboken,
NJ: John Wiley & Sons, Inc.
Fabozzi, F.J. (2006a) Fixed Income Mathematics: Analytical & Statistical
Techniques. New York, NY: McGraw-Hill, Inc.
Fabozzi, F.J. (ed.) (2006b) The Handbook of Mortgage-Backed Securities. New
York, NY: McGraw-Hill, Inc.
Fabozzi, F.J. (2012a) Bond markets, analysis, and strategies. Upper Saddle
River, NJ: Prentice Hall.
Fabozzi, F.J. (2012b) Institutional Investment Management: Equity and Bond
Portfolio Strategies and Applications. Hoboken, NJ: John Wiley & Sons, Inc.
Fabozzi, F.J., Focardi, S.M. and Jonas, C. (2010) Investment Management af-
ter the Global Financial Crisis. Charlottesville, VA: The Research Foundation
of CFA Institute.
Fabozzi, F.J. and Mann, S.V. (2010) Introduction to Fixed Income Analytics:
Relative Value Analysis, Risk Measures, and Valuation. Hoboken, NJ: John
Wiley & Sons, Inc.
Fabozzi, F.J., Martellini, L. and Priaulet, P. (2006) Advanced Bond Portfolio
Management. Best Practices in Modeling and Strategies. Hoboken, NJ: John
Wiley & Sons, Inc.
Falkenstein, E. and Hanweck, J. (1996) Minimizing Basis Risk from Non-
Parallel Shifts in the Yield Curve. Journal of Fixed Income 6(1): 60-68.
Fama, E.F. (1984) Forward and spot exchange rates. Journal of Monetary
Economics 14(3): 319-338.
Fama, E.F. (1996) Multifactor Portfolio Eﬃciency and Multifactor Asset Pric-
ing. Journal of Financial and Quantitative Analysis 31(4): 441-465.
Fama, E.F. and French, K.R. (1987) Commodity futures prices: some evidence
on forecast power, premiums, and the theory of storage. Journal of Business
60(1): 55-73.
187
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 189

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Fama, E.F. and French, K.R. (1988) Business Cycles and the Behavior of
Metals Prices. Journal of Finance 43(5): 1075-1093.
Fama, E.F. and French, K.R. (1992) The Cross-Section of Expected Stock
Returns. Journal of Finance 47(2): 427-465.
Fama, E.F. and French, K.R. (1993) Common Risk Factors in the Returns on
Stocks and Bonds. Journal of Financial Economics 33(1): 3-56.
Fama, E.F. and French, K.R. (1996) Multifactor Explanations of Asset Pricing
Anomalies. Journal of Finance 51(1): 55-84.
Fama, E.F. and French, K.R. (1998) Value versus Growth: The International
Evidence. Journal of Finance 53(6): 1975-1999.
Fama, E.F. and French, K.R. (2008) Dissecting Anomalies.Journal of Finance
63(4): 1653-1678.
Fama, E.F. and French, K.R. (2012) Size, Value and Momentum in Interna-
tional Stock Returns. Journal of Financial Economics 105(3): 457-472.
Fama, E.F. and Schwert, G.W. (1977) Asset returns and inﬂation. Journal of
Financial Economics 5(2): 115-146.
Fass, S.M. and Francis, J. (2004) Where have all the hot goods gone? The role
of pawnshops. Journal of Research in Crime and Delinquency 41(2): 156-179.
Fassas, A.P. (2011) Mispricing in stock index futures markets – the case of
Greece. Investment Management and Financial Innovations 8(2): 101-107.
Fedorova, E., Gilenko, E. and Dovzhenko, S. (2013) Bankruptcy prediction for
Russian companies: Application of combined classiﬁers. Expert Systems with
Applications 40(18): 7285-7293.
Feldh¨ utter, P. and Lando, D. (2008) Decomposing swap spreads. Journal of
Financial Economics 88(2): 375-405.
Feldman, B.E. (2003) Investment Policy for Securitized and Direct Real Es-
tate. Journal of Portfolio Management 29(5): 112-121.
Feldman, B. and Roy, D. (2004) Passive Options-based Investment Strategies:
The Case of the CBOE S&P 500 BuyWrite Index. ETF and Indexing 38(1):
72-89.
Feldman, B. and Till, H. (2006) Backwardation and Commodity Futures Per-
formance: Evidence from Evolving Agricultural Markets. Journal of Alterna-
tive Investments 9(3): 24-39.
188
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 190

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
F´ elix, J.A. and Rodr´ ıguez, F.F. (2008) Improving moving average trading rules
with boosting and statistical learning methods. Journal of Forecasting 27(5):
433-449.
Fengler, M.R., Herwartz, H. and Werner, C. (2012) A Dynamic Copula Ap-
proach to Recovering the Index Implied Volatility Skew. Journal of Financial
Econometrics 10(3): 457-493.
Fenn, D.J., Howison, S.D., Mcdonald, M., Williams, S. and Johnson, N.F.
(2009) The mirage of triangular arbitrage in the spot foreign exchange market.
International Journal of Theoretical and Applied Finance 12(8): 1105-1123.
Fernandez-Perez, A., Frijns, B., Fuertes, A.M. and Miﬀre, J. (2018) The skew-
ness of commodity futures returns. Journal of Banking & Finance 86: 143-158.
Fernandez-Perez, A., Fuertes, A.M. and Miﬀre, J. (2016) Is idiosyncratic
volatility priced in commodity futures markets? International Review of Fi-
nancial Analysis 46: 219-226.
Ferreira, S., Grammatikos, T. and Michala, D. (2016) Forecasting distress in
Europe SME portfolios. Journal of Banking & Finance 64: 112-135.
Ferson, W. and Mo, H. (2016) Performance measurement with selectivity,
market and volatility timing. Journal of Financial Economics 121(1): 93-110.
Fiﬁeld, S.G.M., Power, D.M. and Knipe, D.G.S. (2008) The performance of
moving average rules in emerging stock markets. Applied Financial Economics
18(19): 1515-1532.
Figlewski, S., Chidambaran, N.K. and Kaplan, S. (1993) Evaluating the Per-
formance of the Protective Put Strategy. Financial Analysts Journal 49(4):
46-56, 69.
Filipovi´ c, D., Gourier, E. and Mancini, L. (2016) Quadratic variance swap
models. Journal of Financial Economics 119(1): 44-68.
Finger, C.C. (1999) Conditional approaches for credit metrics portfolio distri-
butions. Credit Metrics Monitor 2(1): 14-33.
Finkenzeller, K., Dechant, T. and Sch¨ afers, W. (2010) Infrastructure: a new
dimension of real estate? An asset allocation analysis. Journal of Property
Investment & Finance 28(4): 263-274.
Finnerty, J.D. and Tu, M. (2017) Valuing Convertible Bonds: A New Ap-
proach. Business Valuation Review 36(3): 85-102.
189
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 191

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Fiorenzani, S. (2006) Quantitative Methods for Electricity Trading and Risk
Management: Advanced Mathematical and Statistical Methods for Energy Fi-
nance. London, UK: Palgrave Macmillan.
Firstenberg, P.M., Ross, S.A. and Zisler, R.C. (1988) Real estate: The whole
story. Journal of Portfolio Management 14(3): 22-34.
Fishe, R.P.H., Janzen, J.P. and Smith, A. (2014) Hedging and Speculative
Trading in Agricultural Futures Markets. American Journal of Agricultural
Economics 96(2): 542-556.
Fisher, M. (2002) Special Repo Rates: An Introduction. Federal Reserve Bank
of Atlanta, Economic Review 87(2): 27-43.
Fisher, G., Shah, R. and Titman, S. (2016) Combining Value and Momentum.
Journal of Investment Management 14(2): 33-48.
Fisher, L. and Weil, R.L. (1971) Coping with the Risk of Interest-Rate Fluc-
tuations: Returns to Bondholders from Na¨ ıve and Optimal Strategies.Journal
of Business 44(4): 408-431.
Fleckenstein, M. (2012) The Inﬂation-Indexed Bond Puzzle. Working Paper.
Available online: https://ssrn.com/abstract=2180251.
Fleckenstein, M., Longstaﬀ, F.A. and Lustig, H.N. (2013) Why Does the Trea-
sury Issue TIPS? The TIPS-Treasury Bond Puzzle. Journal of Finance 69(5):
2151-2197.
Fleckenstein, M., Longstaﬀ, F.A. and Lustig, H.N. (2017) Deﬂation Risk. Re-
view of Financial Studies 30(8): 2719-2760.
Fleming, M.J. and Krishnan, N. (2012) The Microstructure of the TIPS Mar-
ket. Federal Reserve Bank of New York, Economic Policy Review 18(1): 27-45.
Fleming, J., Ostdiek, B. and Whaley, R.E. (1995) Predicting stock market
volatility: A new measure. Journal of Futures Markets 15(3): 265-302.
Fleming, M.J. and Sporn, J.R. (2013) Trading Activity and Price Trans-
parency in the Inﬂation Swap Market. Federal Reserve Bank of New York,
Economic Policy Review 19(1): 45-58.
Flint, E. and Mar´ e, E. (2017) Fractional Black-Scholes option pricing, volatil-
ity calibration and implied Hurst exponents in South African context. South
African Journal of Economic and Management Sciences 20(1): a1532.
Fong, H.G. and Vasicek, O.A. (1983). The tradeoﬀ between return and risk in
immunized portfolios. Financial Analysts Journal 39(5): 73-78.
190
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 192

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Fong, H.G. and Vasicek, O.A. (1984) A Risk Minimizing Strategy for Portfolio
Immunization. Journal of Finance 39(5): 1541-1546.
Fong, W.M. and Yong, L.H.M. (2005) Chasing trends: recursive moving av-
erage trading rules and internet stocks. Journal of Empirical Finance 12(1):
43-76.
Fontaine, J.-F. and Nolin, G. (2017) Measuring Limits of Arbitrage in Fixed-
Income Markets. Staﬀ Working Paper , No. 2017-44. Ottawa, Canada: Bank
of Canada.
Fontana, A. (2010) The Persistent Negative CDS-Bond Basis during the
2007/08 Financial Crisis. Working Paper. Available online:
http://www.unive.it/media/allegato/DIP/Economia/Working_papers/
Working_papers_2010/WP_DSE_fontana_13_10.pdf.
Fontana, A. and Scheicher, M. (2016) An analysis of euro area sovereign CDS
and their relation with government bonds. Journal of Banking & Finance 62:
126-140.
Fortin, M. and Khoury, N. (1984) Hedging Interest Rate Risks with Financial
Futures. Canadian Journal of Administrative Sciences 1(2): 367-382.
Foster, G., Olsen, C. and Shevlin, T. (1984) Earnings releases, anomalies, and
the behavior of security returns. Accounting Review 59(4): 574-603.
Foster, F.D. and Whiteman, C.H. (2002) Bayesian Cross Hedging: An Ex-
ample from the Soybean Market. Australian Journal of Management 27(2):
95-122.
Frachot, A. (1996) A reexamination of the uncovered interest rate parity hy-
pothesis. Journal of International Money and Finance 15(3): 419-437.
Frankel, J.A. (2006) The Eﬀect of Monetary Policy on Real Commodity Prices.
In: Campbell, J. (ed.) Asset Prices and Monetary Policy. Chicago, IL: Uni-
versity of Chicago Press, pp. 291-333.
Franken, J.R.V. and Parcell, J.L. (2003) Cash Ethanol Cross-Hedging Oppor-
tunities. Journal of Agricultural and Applied Economics 35(3): 509-516.
Frazzini, A. and Pedersen, L.H. (2014) Betting against Beta. Journal of Fi-
nancial Economics 111(1): 1-25.
Frenkel, J.A. and Levich, R.M. (1975) Covered interest arbitrage: Unexploited
proﬁts? Journal of Political Economy 83(2): 325-338.
Frenkel, J.A. and Levich, R.M. (1981) Covered interest arbitrage in the 1970’s.
Economics Letters 8(3): 267-274.
191
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 193

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Frey, R. and Backhaus, J. (2008) Pricing and Hedging of Portfolio Credit
Derivatives with Interacting Default Intensities. International Journal of The-
oretical and Applied Finance 11(6): 611-634.
Frey, R. and Backhaus, J. (2010) Dynamic hedging of synthetic CDO tranches
with spread risk and default contagion. Journal of Economic Dynamics and
Control 34(4): 710-724.
Frey, R., McNeil, A. and Nyfeler, N. (2001) Copulas and Credit Models. Risk,
October 2001, pp. 111-114.
Fridson, M.S. and Xu, X. (2014) Duration Targeting: No Magic for High-Yield
Investors. Financial Analysts Journal 70(3): 28-33.
Friewald, N., Jankowitsch, R. and Subrahmanyam, M. (2012) Illiquidity, or
Credit Deterioration: A Study of Liquidity in the U.S. Bond Market during
Financial Crises. Journal of Financial Economics 105(1): 18-36.
Frino, A., Gallagher, D.R., Neubert, A.S. and Oetomo, T.N. (2004) Index
Design and Implications for Index Tracking. Journal of Portfolio Management
30(2): 89-95.
Frino, A. and McKenzie, M. (2002) The pricing of stock index futures spreads
at contract expiration. Journal of Futures Markets 22(5): 451-469.
Froot, K.A., Scharfstein, D.S. and Stein, J.C. (1993) Risk Management: Co-
ordinating Corporate Investment and Financing Policies. Journal of Finance
48(5): 1629-1658.
Froot, K.A. and Thaler, R.H. (1990) Anomalies: Foreign Exchange. Journal
of Economic Perspectives 4(3): 179-192.
Fry, J. and Cheah, E.T. (2016) Negative bubbles and shocks in cryptocurrency
markets. International Review of Financial Analysis 47: 343-352.
Fu, F. (2009) Idiosyncratic Risk and the Cross-Section of Expected Stock
Returns. Journal of Financial Economics 91(1): 24-37.
Fu, Y. and Qian, W. (2014) Speculators and Price Overreaction in the Housing
Market. Real Estate Economics 42(4): 977-1007.
Fu, X., Sandri, M. and Shackleton, M.B. (2016) Asymmetric Eﬀects of Volatil-
ity Risk on Stock Returns: Evidence from VIX and VIX Futures. Journal of
Futures Markets 36(11): 1029-1056.
Fuertes, A., Miﬀre, J. and Fernandez-Perez, A. (2015) Commodity Strategies
Based on Momentum, Term Structure, and Idiosyncratic Volatility. Journal
of Futures Markets 35(3): 274-297.
192
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 194

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Fuertes, A., Miﬀre, J. and Rallis, G. (2010) Tactical allocation in commodity
futures markets: Combining momentum and term structure signals. Journal
of Banking & Finance 34(10): 2530-2548.
Fugazza, C., Guidolin, M. and Nicodano, G. (2007) Investing for the Long-
run in European Real Estate. Journal of Real Estate Finance and Economics
34(1): 35-80.
Fulli-Lemaire, N. (2013) An Inﬂation Hedging Strategy with Commodities: A
Core Driven Global Macro. Journal of Investment Strategies 2(3): 23-50.
Fung, W. and Hsieh, D.A. (1999) A Primer on Hedge Funds. Journal of Em-
pirical Finance 6(3): 309-331.
Fung, J.K.W., Mok, H.M.K. and Wong, K.C.K. (2004) Pricing Eﬃciency in a
Thin Market with Competitive Market Makers: Box Spread Strategies in the
Hang Seng Index Options Market. Financial Review 39(3): 435-454.
Fusaro, P.C. and James, T. (2005) Energy Hedging in Asia: Market Structure
and Trading Opportunities. London, UK: Palgrave Macmillan.
F¨ uss, R. and Nikitina, O. (2011) Explaining Yield Curve Dynamics. Journal
of Fixed Income 21(2): 68-87.
Gabaix, X., Krishnamurthy, A. and Vigneron, O. (2007) Limits of arbitrage:
theory and evidence from the mortgage-backed securities market. Journal of
Finance 62(2): 557-595.
Gajardo, G., Kristjanpoller, W.D. and Minutolo, M. (2018) Does Bitcoin ex-
hibit the same asymmetric multifractal cross-correlations with crude oil, gold
and DJIA as the Euro, Great British Pound and Yen? Chaos, Solitons &
Fractals 109: 195-205.
Gande, A., Altman, E. and Saunders, A. (2010) Bank Debt vs. Bond Debt:
Evidence from Secondary Market Prices. Journal of Money, Credit and Bank-
ing 42(4): 755-767.
Gao, B. and Ren, R.-E. (2015) A New Sector Rotation Strategy and its Per-
formance Evaluation: Based on a Principal Component Regression Model.
Working Paper. Available online: https://ssrn.com/abstract=2628058.
Gao, C., Xing, Y. and Zhang, X. (2017) Anticipating Uncertainty: Straddles
Around Earnings Announcements. Working Paper. Available online: https:
//ssrn.com/abstract=2204549.
Garbade, K.D. (2004) Origins of the Federal Reserve Book-Entry System.
Federal Reserve Bank of New York, Economic Policy Review 10(3): 33-50.
193
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 195

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Garcia, C.B. and Gould, F.J. (1993) Survivorship Bias. Journal of Portfolio
Management 19(3): 52-56.
Garcia, D. and Schweitzer, F. (2015) Social signals and algorithmic trading of
Bitcoin. Royal Society Open Science 2(9): 150288.
Garcia, D., Tessone, C.J., Mavrodiev, P. and Perony, N. (2014) The digital
traces of bubbles: feedback cycles between socioeconomic signals in the Bitcoin
economy. Journal of The Royal Society Interface 11(99): 0623.
Garcia-Feij´ oo, L., Kochard, L., Sullivan, R.N. and Wang, P. (2015) Low-
Volatility Cycles: The Inﬂuence of Valuation and Momentum on Low-
Volatility Portfolios. Financial Analysts Journal 71(3): 47-60.
Garlappi, L. and Yan, H. (2011) Financial Distress and the Cross-section of
Equity Returns. Journal of Finance 66(3): 789-822.
Gˆ arleanu, N., Pedersen, L.H. and Poteshman, A.M. (2009) Demand-Based
Option Pricing. Review of Financial Studies 22(10): 4259-4299.
Garvey, R. and Wu, F. (2009) Intraday time and order execution quality di-
mensions. Journal of Financial Markets 12(2): 203-228.
Garyn-Tal, S. (2014a) An Investment Strategy in Active ETFs. Journal of
Index Investing 4(1): 12-22.
Garyn-Tal, S. (2014b) Explaining and Predicting ETFs Alphas: The R2
Methodology. Journal of Index Investing 4(4): 19-32.
Garzarelli, F., Cristelli, M., Pompa, G., Zaccaria, A. and Pietronero, L. (2014)
Memory eﬀects in stock price dynamics: evidences of technical trading. Sci-
entiﬁc Reports 4: 4487.
Gatev, E., Goetzmann, W.N. and Rouwenhorst, K.G. (2006) Pairs Trading:
Performance of a Relative-Value Arbitrage Rule. Review of Financial Studies
19(3): 797-827.
Gatheral, J. and Jacquier, A. (2014) Arbitrage-free SVI volatility surfaces.
Quantitative Finance 14(1): 59-71.
Gatzlaﬀ, D.H. and Tirtiroglu, D. (1995) Real Estate Market Eﬃciency: Issues
and Evidence. Journal of Real Estate Literature 3(2): 157-189.
Gay, G.D. and Kolb, R.W. (1983) The Management of Interest Rate Risk.
Journal of Portfolio Management 9(2): 65-70.
194
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 196

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Gay, G.D., Kolb, R.W. and Chiang, R. (1983) Interest Rate Hedging: An
Empirical Test Of Alternative Strategies. Journal of Financial Research 6(3):
187-197.
Ge, W. (2016) A Survey of Three Derivative-Based Methods to Harvest the
Volatility Premium in Equity Markets. Journal of Investing 25(3): 48-58.
G´ eczy, C., Minton, B.A. and Schrand, C. (1997) Why Firms Use Currency
Derivatives. Journal of Finance 52(4): 1323-1354.
G´ eczy, C.C. and Samonov, M. (2016) Two Centuries of Price-Return Momen-
tum. Financial Analysts Journal 72(5): 32-56.
Gehricke, S.A. and Zhang, J.E. (2018) Modeling VXX. Journal of Futures
Markets 38(8): 958-976.
Geltner, D.M., Miller, N.G., Clayton, J. and Eichholtz, P. (2006) Commer-
cial Real Estate Analysis and Investments. (2nd ed.) Atlanta, GA: OnCourse
Learning Publishing.
Geltner, D.M., Rodriguez, J.V. and O’Connor, D. (1995) The Similar Genetics
of Public and Private Real Estate and the Optimal Long-Horizon Portfolio
Mix. Real Estate Finance 12(3): 13-25.
Geman, H. (1998) Insurance and Weather Derivatives: From Exotic Options
to Exotic Underlyings. London, UK: Risk Books.
Geman, H. and Leonardi, M.-P. (2005) Alternative approaches to weather
derivatives pricing. Managerial Finance 31(6): 46-72.
Geman, H. and Roncoroni, A. (2006) Understanding the ﬁne structure of
electricity prices. Journal of Business 79(3): 1225-1261.
Gen¸ cay, R. (1996) Nonlinear prediction of security returns with moving aver-
age rules. Journal of Forecasting 15(3): 165-174.
Gen¸ cay, R. (1998) The Predictability of securities returns with simple technical
rules. Journal of Empirical Finance 5(4): 347-359.
Gen¸ cay, R. and Stengos, T. (1998) Moving average rules, volume and the
predictability of security returns with feedforward networks. Journal of Fore-
casting 17(5-6): 401-414.
Genesove, D. and Han, L. (2012) Search and Matching in the Housing Market.
Journal of Urban Economics 72(1): 31-35.
Genesove, D. and Mayer, C. (1997) Equity and Time to Sale in the Real Estate
Market. American Economic Review 87(3): 255-269.
195
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 197

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Genesove, D. and Mayer, C. (2001) Loss Aversion and Seller Behavior: Ev-
idence From the Housing Market. Quarterly Journal of Economics 116(4):
1233-1260.
George, T.J. and Hwang, C.-Y. (2010) A resolution of the distress risk and
leverage puzzles in the cross section of stock returns. Journal of Financial
Economics 96(1): 56-79.
Georgoula, I., Pournarakis, D., Bilanakos, C., Sotiropoulos, D. and Gi-
aglis, G.M. (2015) Using Time-Series and Sentiment Analysis to Detect the
Determinants of Bitcoin Prices. Working Paper. Available online: https:
//ssrn.com/abstract=2607167.
Gerakos, J. and Linnainmaa, J. (2012) Decomposing Value. Working Paper.
Available online: https://ssrn.com/abstract=2083166.
Gervais, S. and Odean, T. (2001) Learning to Be Overconﬁdent. Review of
Financial Studies 14(1): 1-27.
Geske, R.L. and Pieptea, D.R. (1987) Controlling Interest Rate Risk and Re-
turn with Futures. Review of Futures Markets 6(1): 64-86.
Gestel, T., Suykens, J.A.K., Baestaend, D.E., Lambrechts, A., Lanckriet, G.,
Vandaele, B., Moor, B. and Vandewalle, J. (2001) Financial time series predic-
tion using least squares support vector machines within the evidence frame-
work. IEEE Transactions on Neural Networks 12(4): 809-821.
Ghiulnara, A. and Viegas, C. (2010) Introduction of weather-derivative con-
cepts: perspectives for Portugal. Journal of Risk Finance 11(1): 9-19.
Ghosh, A. (1993) Hedging with stock index futures: Estimation and forecast-
ing with error correction model. Journal of Futures Markets 13(7): 743-752.
Ghosh, A. (2012) Comparative study of Financial Time Series Prediction by
Artiﬁcial Neural Network with Gradient Descent Learning.International Jour-
nal of Scientiﬁc & Engineering Research 3(1): 41-49.
Gibson, M.S. (2004) Understanding the Risk of Synthetic CDOs. Finance and
Economics Discussion Series (FEDS) , Paper No. 2004-36. Washington, DC:
Board of Governors of the Federal Reserve System. Available online: https:
//www.federalreserve.gov/pubs/feds/2004/200436/200436pap.pdf.
Gibson, M.S. and Pritsker, M. (2000) Improving Grid-based Methods for Esti-
mating Value at Risk of Fixed-Income Portfolios. Journal of Risk 3(2): 65-89.
Gibson, R. and Schwartz, E.S. (1990) Stochastic convenience yield and the
pricing of oil contingent claims. Journal of Finance 15(3): 959-967.
196
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 198

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Giese, P. (2012) Optimal design of volatility-driven algo-alpha trading strate-
gies. Risk 25(5): 68-73.
Giesecke, K. and Weber, S. (2006) Credit contagion and aggregate losses.
Journal of Economic Dynamics and Control 30(5): 741-767.
Gilbert, S., Jones, S.K. and Morris, G.H. (2006) The impact of skewness in
the hedging decision. Journal of Futures Markets 26(5): 503-520.
Gilmour, N. and Ridley, N. (2015) Everyday vulnerabilities – money launder-
ing through cash intensive businesses. Journal of Money Laundering Control
18(3): 293-303.
Gilson, S.C. (1995) Investing in Distressed Situations: A Market Survey. Fi-
nancial Analysts Journal 51(6): 8-27.
Gilson, S.C. (2010) Creating Value Through Corporate Restructuring: Case
Studies in Bankruptcies, Buyouts, and Breakups. Hoboken, NJ: John Wiley &
Sons, Inc.
Gilson, S. (2012) Preserving Value by Restructuring Debt. Journal of Applied
Corporate Finance 24(4): 22-35.
Gilson, S.C., John, K. and Lang, L.H.P. (1990) Troubled debt restructurings:
An empirical study of private reorganization of ﬁrms in default. Journal of
Financial Economics 27(2): 315-353.
Girma, P.B. and Paulson, A.S. (1998) Seasonality in petroleum futures
spreads. Journal of Futures Markets 18(5): 581-598.
Glabadanidis, P. (2015) Market Timing With Moving Averages. International
Review of Finance 15(3): 387-425.
Glaeser, E.L. and Kallal, H.D. (1997) Thin Markets, Asymmetric Information,
and Mortgage-Backed Securities. Journal of Financial Intermediation 6(1):
64-86.
Glasserman, P. and Wu, Q. (2010) Forward and future implied volatility. In-
ternational Journal of Theoretical and Applied Finance 14(3): 407-432.
Gliner, G. (2014) Global Macro Trading: Proﬁting in a New World Economy.
Hoboken, NJ: John Wiley & Sons, Inc.
Glorot, X., Bordes, A. and Bengio, Y. (2011) Deep Sparse Rectiﬁer Neural
Networks. Proceedings of Machine Learning Research 15: 315-323.
197
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 199

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Godfrey, C. and Brooks, C. (2015) The Negative Credit Risk Premium Puzzle:
A Limits to Arbitrage Story.Working Paper. Available online: https://ssrn.
com/abstract=2661232.
Goebel, P.R., Harrison, D.M., Mercer, J.M. and Whitby, R.J. (2013) REIT
Momentum and Characteristic-Related REIT Returns. Journal of Real Estate
Finance and Economics 47(3): 564-581.
Goetzmann, W.N. and Ibbotson, R.G. (1990) The Performance of Real Estate
as an Asset Class. Journal of Applied Corporate Finance 3(1): 65-76.
Goetzmann, W.N. and Ibbotson, R.G. (1994) Do Winners Repeat? Journal
of Portfolio Management 20(2): 9-18.
Golden, L.L., Wang, M. and Yang, C. (2007) Handling Weather Related Risks
through the Financial Markets: Considerations of Credit Risk, Basis Risk, and
Hedging. Journal of Risk and Insurance 74(2): 319-346.
Goldstein, H.N. (1964) The Implications of Triangular Arbitrage for Forward
Exchange Policy. Journal of Finance 19(3): 544-551.
Goltz, F. and Lai, W.N. (2009) Empirical properties of straddle returns. Jour-
nal of Derivatives 17(1): 38-48.
G¨ onc¨ u, A. (2012) Pricing temperature-based weather derivatives in China.
Journal of Risk Finance 13(1): 32-44.
Goodfellow, I., Warde-Farley, D., Mirza, M., Courville, A. and Bengio, Y.
(2013) Maxout Networks. Proceedings of Machine Learning Research 28(3):
1319-1327.
Goodfriend, M. (2011) Money Markets. Annual Review of Financial Eco-
nomics 3: 119-1137.
Goodman, L.S. (2002) Synthetic CDOs: An Introduction. Journal of Deriva-
tives 9(3): 60-72.
Goodman, L.S. and Lucas, D.J. (2002) And When CDOs PIK? Journal of
Fixed Income 12(1): 96-102.
Gordini, N. (2014) A genetic algorithm approach for SMEs bankruptcy predic-
tion: Empirical evidence from Italy. Expert Systems with Applications 41(14):
6433-6455.
Gorton, G.B., Hayashi, F. and Rouwenhorst, K.G. (2013) The Fundamentals
of Commodity Futures Returns. Review of Finance 17(1): 35-105.
198
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 200

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Gorton, G. and Metrick, A. (2012) Securitized banking and the run on repo.
Journal of Financial Economics 104(3): 425-451.
Gorton, G.B. and Rouwenhorst, K.G. (2006) Facts and Fantasies about Com-
modity Futures. Financial Analysts Journal 62(2): 47-68.
Gradojevic, N., Gen¸ cay, R. and Erdemlioglu, D. (2017) Robust Prediction of
Triangular Currency Arbitrage with Liquidity and Realized Risk Measures: A
New Wavelet-Based Ultra-High-Frequency Analysis.Working Paper. Available
online: https://ssrn.com/abstract=3018815.
Graﬀ, R., Harrington, A. and Young, M. (1999) Serial Persistence in Dis-
aggregated Australian Real Estate Returns. Journal of Real Estate Portfolio
Management 5(2): 113-128.
Graﬀ, R.A. and Young, M.S. (1997) Serial Persistence in Equity REIT Re-
turns. Journal of Real Estate Research 14(3): 183-214.
Graham, M., Nikkinen, J. and Sahlstr¨ om, P. (2003) Relative importance of
scheduled macroeconomic news for stock market investors. Journal of Eco-
nomics and Finance 27(2): 153-165.
Graham, S. and Pirie, W. (1994) Index Fund Rebalancing and Market Eﬃ-
ciency. Journal of Economics and Finance 18(2): 219-229.
Grant, J. (2016) Trading Strategies in Futures Markets (Ph.D. Thesis). Lon-
don, UK: Imperial College. Available online: https://spiral.imperial.ac.
uk/bitstream/10044/1/32011/1/Grant-J-2016-PhD-Thesis.PDFA.pdf .
Grantier, B.J. (1988) Convexity and Bond Performance: The Benter the Bet-
ter. Financial Analysts Journal 44(6): 79-81.
Grasselli, M. and Wagalath, L. (2018) VIX vs VXX: A Joint Analytical
Framework. Working Paper. Available online: https://ssrn.com/abstract=
3144526.
Green, R.C. and Rydqvist, K. (1999) Ex-day behavior with dividend pref-
erence and limitations to short-term arbitrage: the case of Swedish lottery
bonds. Journal of Financial Economics 53(2): 145-187.
Greenhaus, S.F. (1991) Approaches to Investing in Distressed Securities: Pas-
sive Approaches. In: Bowman, T.A. (ed.) Analyzing Investment Opportunities
in Distressed and Bankrupt Companies. (AIMR Conference Proceedings, Vol.
1991, Iss. 1.) Chicago, IL: AIMR, pp. 47-52.
Greer, R.J. (1978) Conservative Commodities: A Key Inﬂation Hedge.Journal
of Portfolio Management 4(4): 26-29.
199
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 201

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Greer, R.J. (2000) The Nature of Commodity Index Returns. Journal of Al-
ternative Investments 3(1): 45-52.
Greer, R.J. (2007) The Role of Commodities in Investment Portfolios. CFA
Institute Conference Proceedings Quarterly 24(4): 35-44.
Grieves, R. (1999) Butterﬂy Trades. Journal of Portfolio Management 26(1):
87-95.
Grieves, R. and Mann, S.V. (2004) An Overlooked Coupon Eﬀect in Treasury
Futures Contracts. Journal of Derivatives 12(2): 56-61.
Grieves, R., Mann, S.V., Marcus, A.J. and Ramanlal, P. (1999) Riding the
Bill Curve. Journal of Portfolio Management 25(3): 74-82.
Grieves, R. and Marcus, A.J. (1992) Riding the Yield Curve: Reprise. Journal
of Portfolio Management 18(4): 67-76.
Grieves, R. and Marcus, A.J. (2005) Delivery Options and Treasury-Bond
Futures Hedge Ratios. Journal of Derivatives 13(2): 70-76.
Griﬃn, J.M., Ji, X. and Martin, J.S. (2003) Momentum Investing and Business
Cycle Risks: Evidence from Pole to Pole. Journal of Finance 58(6): 2515-2547.
Griﬃn, J.M. and Lemmon, M.L. (2002) Book-to-Market Equity, Distress Risk,
and Stock Returns. Journal of Finance 57(5): 2317-2336.
Grigg, N.S. (2010) Infrastructure Finance: The Business of Infrastructure for
a Sustainable Future. Hoboken, NJ: John Wiley & Sons, Inc.
Grimsey, D. and Lewis, M.K. (2002) Evaluating the risks of public private
partnerships for infrastructure projects. International Journal of Project Man-
agement 20(2): 107-118.
Grinblatt, M. and Moskowitz, T.J. (2004) Predicting Stock Price Movements
from Past Returns: The Role of Consistency and Tax-Loss Selling. Journal of
Financial Economics 71(3): 541-579.
Grinblatt, M. and Titman, S. (1992) The Persistence of Mutual Fund Perfor-
mance. Journal of Finance 47(5): 1977-1984.
Grinold, R.C. and Kahn, R.N. (2000)Active Portfolio Management. New York,
NY: McGraw-Hill, Inc.
Grishchenko, O.V. and Huang, J.-Z. (2013) Inﬂation Risk Premium: Evidence
from the TIPS Market. Journal of Fixed Income 22(4): 5-30.
200
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 202

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Grishchenko, O.V., Vanden, J.M. and Zhang, J. (2016) The Informational
Content of the Embedded Deﬂation Option in TIPS. Journal of Banking &
Finance 65: 1-26.
Grissom, T.V., Kuhle, J.L. and Walther, C.H. (1987) Diversiﬁcation works in
real estate, too. Journal of Portfolio Management 13(2): 66-71.
Grobys, K., Heinonen, J.-P. and Kolari, J.W. (2016) Is Currency Momentum
a Hedge for Global Economic Risk? Working Paper. Available online: https:
//ssrn.com/abstract=2619146.
Grudnitski, G. and Osborn, L. (1993) Forecasting S&P and Gold Futures
Prices: An Application of Neural Networks. Journal of Futures Markets 13(6):
631-643.
Grundy, B.D. and Martin, J.S. (2001) Understanding the Nature of the Risks
and the Source of the Rewards to Momentum Investing. Review of Financial
Studies 14(1): 29-78.
Grundy, B.D. and Verwijmeren, P. (2016) Disappearing call delay and
dividend-protected convertible bonds. Journal of Finance 71(1): 195-224.
Gunasekarage, A. and Power, D.M. (2001) The proﬁtability of moving average
trading rules in South Asian stock markets. Emerging Markets Review 2(1):
17-33.
Gunasekarage, A., Power, D.M. and Ting Zhou, T.T. (2008) The long-term in-
ﬂation hedging eﬀectiveness of real estate and ﬁnancial assets: A New Zealand
investigation. Studies in Economics and Finance 25(4): 267-278.
Guo, D. (2000) Dynamic Volatility Trading Strategies in the Currency Option
Market. Review of Derivatives Research 4(2): 133-154.
Gupta, R. and Miller, S.M. (2012) “Ripple eﬀects” and forecasting home prices
in Los Angeles, Las Vegas, and Phoenix. Annals of Regional Science 48(3):
763-782.
Guren, A.M. (2014) The Causes and Consequences of House Price Mo-
mentum. Working Paper. Available online: http://scholar.harvard.edu/
files/guren/files/gurenjmp.pdf.
G¨ urkaynak, R.S., Sack, B. and Wright, J.H. (2010) The TIPS Yield Curve and
Inﬂation Compensation. American Economic Journal: Macroeconomics 2(1):
70-92.
Gutierrez, R.C. and Prinsky, C.A. (2007) Momentum, Reversal, and the Trad-
ing Behaviors of Institutions. Journal of Financial Markets 10(1): 48-75.
201
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 203

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hafner, R. and Wallmeier, M. (2007) Volatility as an Asset Class: European
Evidence. European Journal of Finance 13(7): 621-644.
Hagenstein, F., Mertz, A. and Seifert, J. (2004) Investing in Corporate Bonds
and Credit Risk. London, UK: Palgrave Macmillan.
Hagopian, G.C. (1999) Property-ﬂipping and fraudulent appraisals: The phe-
nomenon and the crackdown. Assessment Journal 6(6): 33-39.
Hagstr¨ omer, B. and Nord´ en, L. (2013) The Diversity of High-Frequency
Traders. Journal of Financial Markets 16(4): 741-770.
Hagstr¨ omer, B., Nord´ en, L. and Zhang, D. (2014) The Aggressiveness of High-
Frequency Traders. Financial Review 49(2): 395-419.
Hall, P., Park, B.U. and Samworth, R.J. (2008) Choice of neighbor order in
nearest-neighbor classiﬁcation. Annals of Statistics 36(5): 2135-2152.
Hall, J., Pinnuck, M. and Thorne, M. (2013) Market risk exposure of merger
arbitrage in Australia. Accounting & Finance 53(1): 185-215.
Hamelink, F. and Hoesli, M. (1996) Swiss real estate as a hedge against in-
ﬂation: New evidence using hedonic and autoregressive models. Journal of
Property Finance 7(1): 33-49.
Hamerle, A., Igl, A. and Plank, K. (2012) Correlation smile, volatility skew,
and systematic risk sensitivity of tranches. Journal of Derivatives 19(3): 8-27.
Hamilton, J. (2003) What is an oil shock? Journal of Econometrics 113(2):
363-398.
Hamisultane, H. (2009) Utility-based pricing of weather derivatives. European
Journal of Finance 16(6): 503-525.
Han, S. and Qiu, J. (2007) Corporate precautionary cash holdings. Journal of
Corporate Finance 13(1): 43-57.
Hancock, G.D. (2013) VIX Futures ETNs: Three Dimensional Losers. Ac-
counting and Finance Research 2(3): 53-64.
Hanley, M. (1999) Hedging the Force of Nature. Risk Professional 5(4): 21-25.
Hanly, J., Morales, L. and Cassells, D. (2018) The eﬃcacy of ﬁnancial futures
as a hedging tool in electricity markets. International Journal of Financial
Economics 23(1): 29-40.
Hansch, O., Naik, N.Y. and Viswanathan, S. (1998) Do inventories matter in
dealership markets? Evidence from the London stock exchange. Journal of
Finance 53(5): 1623-1656.
202
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 204

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hansen, L.P. and Hodrick, R.J. (1980) Forward Exchange Rates as Optimal
Predictors of Future Spot Rates: An Econometric Analysis. Journal of Polit-
ical Economy 88(5): 829-853.
Happ, S. (1986) The Behavior of Rates on Federal Funds and Repurchase
Agreements. American Economist 30(2): 22-32.
Haran, M., Newell, G., Adair, A., McGreal, S. and Berry, J. (2011) The per-
formance of UK regeneration property within a mixed asset portfolio. Journal
of Property Research 28(1): 75-95.
Harˇ carikov´ a, M. andˇSolt´ es, M. (2016) Risk Management in Energy Sector
Using Short Call Ladder Strategy. Montenegrin Journal of Economics 12(3):
39-54.
H¨ ardle, W.K. and L´ opez Cabrera, B. (2011) The Implied Market Price of
Weather Risk. Applied Mathematical Finance 19(1): 59-95.
H¨ ardle, W. and Silyakova, E. (2010) Volatility Investing with Variance Swaps.
Working Paper. Available online: https://ssrn.com/abstract=2894245.
Hardy, C.C. (1978) The Investor’s Guide to Technical Analysis. New York,
NY: McGraw-Hill, Inc.
Harford, J. (2005) What drives merger waves?Journal of Financial Economics
77(3): 529-560.
Harner, M.M. (2008) The Corporate Governance and Public Policy Impli-
cations of Activist Distressed Debt Investing. Fordham Law Review 77(2):
703-773.
Harner, M.M. (2011) Activist Distressed Debtholders: The New Barbarians
at the Gate? Washington University Law Review 89(1): 155-206.
Harris, T.S., Hubbard, R.G. and Kemsley, D. (2001) The Share Price Eﬀects
Of Dividend Taxes And Tax Imputation Credits.Journal of Public Economics
79(3): 569-596.
Harris, L.E. and Namvar, E. (2016) The Economics of Flash Orders and Trad-
ing. Journal of Investment Management 14(4): 74-86.
Harris, R.D.F. and Yilmaz, F. (2009) A momentum trading strategy based
on the low frequency component of the exchange rate. Journal of Banking &
Finance 33(9): 1575-1585.
Harrison, J.M. and Pliska, S.R. (1981) Martingales and stochastic integrals in
the theory of continuous trading. Stochastic Processes and Their Applications
11(3): 215-260.
203
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 205

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hartigan, L.R., Prasad, R. and De Francesco, A.J. (2011) Constructing an
investment return series for the UK unlisted infrastructure market: estimation
and application. Journal of Property Research 28(1): 35-58.
Hartzell, D.J., Eichholtz, P. and Selender, A. (2007) Economic diversiﬁcation
in European real estate portfolios. Journal of Property Research 10(1): 5-25.
Hartzell, D., Hekman, J. and Miles, M. (1986) Diversiﬁcation Categories in
Investment Real Estate. Real Estate Economics 14(2): 230-254.
Hartzell, D., Hekman, J.S. and Miles, M.E. (1987) Real Estate Returns and
Inﬂation. Real Estate Economics 15(1): 617-637.
Hartzell, D.J., Shulman, D.G. and Wurtzebach, C.H. (1987) Reﬁning the Anal-
ysis of Regional Diversiﬁcation for Income-Producing Real Estate. Journal of
Real Estate Research 2(2): 85-95.
Hartzog, J. (1982) Controlling Proﬁt Volatility: Hedging with GNMA Options.
Federal Home Loan Bank Board Journal 15(2): 10-14.
Harvey, A.C. (1984) A uniﬁed view of statistical forecasting procedures. Jour-
nal of Forecasting 3(3): 245-275.
Harvey, A.C. (1990) Forecasting, Structural Time Series Models and the
Kalman Filter. Cambridge, UK: Cambridge University Press.
Harvey, C.R. (2014) Bitcoin Myths and Facts. Working Paper. Available on-
line: https://ssrn.com/abstract=2479670.
Harvey, C.R. (2016) Cryptoﬁnance. Working Paper. Available online: https:
//ssrn.com/abstract=2438299.
Harvey, J.T. (2015) Deviations from uncovered interest rate parity: a Post
Keynesian explanation. Journal of Post Keynesian Economics 27(1): 19-35.
Harvey, A. and Trimbur, T. (2008) Trend Estimation and the Hodrick-Prescott
Filter. Journal of the Japan Statistical Society 38(1): 41-49.
Hasbrouck, J. and Saar, G. (2013) Low-latency Trading. Journal of Financial
Markets 16(4): 646-679.
Hastings, A. and Nordby, H. (2007) Beneﬁts of Global Diversiﬁcation on a
Real Estate Portfolio. Journal of Portfolio Management 33(5): 53-62.
Hatemi-J, A. and Roca, E. (2006) Calculating the optimal hedge ratio: con-
stant, time varying and the Kalman Filter approach. Applied Economics Let-
ters 13(5): 293-299.
204
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 206

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hau, H. (2014) The exchange rate eﬀect of multi-currency risk arbitrage.Jour-
nal of International Money and Finance 47: 304-331.
Haubrich, J., Pennacchi, G. and Ritchken, P. (2012) Inﬂation Expectations,
Real Rates, and Risk Premia: Evidence from Inﬂation Swaps. Review of Fi-
nancial Studies 25(5): 1588-1629.
Haug, E.G. (2001) Closed form Valuation of American Barrier Options. Inter-
national Journal of Theoretical and Applied Finance 4(2): 355-359.
Haugen, R.A. (1995) The New Finance: The Case Against Eﬃcient Markets.
Upper Saddle River, NJ: Prentice Hall.
Haurin, D.R. and Gill, H.L. (2002) The Impact of Transaction Costs and the
Expected Length of Stay on Homeownership. Journal of Urban Economics
51(3): 563-584.
Haurin, D.R., Haurin, J.L., Nadauld, T. and Sanders, A. (2010) List Prices,
Sale Prices and Marketing Time: An Application to U.S. Housing Markets.
Real Estate Economics 38(4): 659-685.
Hautcoeur, P.C. (2006) Why and how to measure stock market ﬂuctua-
tions? The early history of stock market indices, with special reference
to the French case. Working Paper. Available online: https://halshs.
archives-ouvertes.fr/halshs-00590522/PDF/wp200610.pdf.
Hayes, B. (2011) Multiple time scale attribution for commodity trading advisor
(CTA) funds. Journal of Investment Management 9(2): 35-72.
Hayre, L.S. (1990) Understanding option-adjusted spreads and their use.Jour-
nal of Portfolio Management 16(4): 68-69.
He, D.X., Hsu, J.C. and Rue, N. (2015) Option-Writing Strategies in a Low-
Volatility Framework. Journal of Investing 24(3): 116-128.
He, J., Tang, Q. and Zhang, H. (2016) Risk reducers in convex order. Insur-
ance: Mathematics and Economics 70: 80-88.
Head, A., Lloyd-Ellis, H. and Sun, H. (2014) Search, Liquidity, and the Dy-
namics of House Prices and Construction. American Economic Review 104(4):
1172-1210.
Heaton, H. (1988) On the possible tax-driven arbitrage opportunities in the
new municipal bond futures contract. Journal of Futures Markets 8(3): 291-
302.
205
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 207

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hegde, S.P. (1982) The Impact of Interest Rate Level and Volatility on the
Performance of Interest Rate Hedges. Journal of Futures Markets 2(4): 341-
356.
Heidari, M. and Wu, L. (2003) Are Interest Rate Derivatives Spanned by the
Term Structure of Interest Rates? Journal of Fixed Income 13(1): 75-86.
Helm, D. (2009) Infrastructure Investment, the Cost of Capital, and Regula-
tion: an Assessment. Oxford Review of Economic Policy 25(3): 307-326.
Helm, D. and Tindall, T. (2009) The Evolution of Infrastructure and Utility
Ownership and its Implications. Oxford Review of Economic Policy 25(3):
411-434.
Hemler, M.L. and Miller, T.W., Jr. (1997) Box spread arbitrage proﬁts fol-
lowing the 1987 market crash. Journal of Financial and Quantitative Analysis
32(1): 71-90.
Hemler, M.L. and Miller, T.W., Jr. (2015) The Performance of Options-Based
Investment Strategies: Evidence for Individual Stocks During 2003-2013.
Working Paper. Available online:
http://www.optionseducation.org/content/dam/oic/documents/
literature/files/perf-options-strategies.pdf.
Hendershott, T., Jones, C. and Menkveld, A. (2011) Does Algorithmic Trading
Improve Liquidity? Journal of Finance 66(1): 1-33.
Hendershott, T., Jones, C. and Menkveld, A. (2013) Implementation Shortfall
with Transitory Price Eﬀects. In: Easley, D., L´ opez de Prado, M. and O’Hara,
M. (eds.) High Frequency Trading: New Realities for Traders, Markets and
Regulators. London, UK: Risk Books, Chapter 9.
Hendershott, T. and Moulton, P.C. (2011) Automation, speed, and stock mar-
ket quality: The NYSE’s Hybrid. Journal of Financial Markets 14(4): 568-604.
Hendershott, T. and Riordan, R. (2013) Algorithmic Trading and the Market
for Liquidity. Journal of Financial and Quantitative Analysis 48(4): 1001-
1024.
Henderson, B. (2005) Convertible Bonds: New Issue Performance and Ar-
bitrage Opportunities (Ph.D. Thesis). Urbana-Champaign IL: University of
Illinois.
Henderson, R. (1924) A new method of graduation. Transactions of the Actu-
arial Society of America 25: 29-40.
206
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 208

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Henderson, R. (1925) Further remarks on graduation. Transactions of the Ac-
tuarial Society of America 26: 52-57.
Henderson, R. (1938) Mathematical Theory of Graduation. New York, NY:
Actuarial Society of America.
Henderson, T.M. (2003) Fixed Income Strategy: The Practitioner’s Guide to
Riding the Curve. Chichester, UK: John Wiley & Sons, Ltd.
Henderson, B.J. and Tookes, H. (2012) Do investment banks’ relationships
with investors impact pricing? The case of convertible bond issues. Manage-
ment Science 58(2): 2272-2291.
Henrard, M.P.A. (2006) A Semi-Explicit Approach to Canary Swaptions in
HJM One-Factor Model. Applied Mathematical Finance 13(1): 1-18.
Hensher, D. and Jones, S. (2007) Forecasting corporate bankruptcy: Optimiz-
ing the performance of the mixed logit model. Abacus 43(3): 241-364.
Herbertsson, A. (2008) Pricing synthetic CDO tranches in a model with default
contagion using the matrix-analytic approach. Journal of Credit Risk 4(4): 3-
35.
Herranz-Lonc´ an, A. (2007) Infrastructure investment and Spanish economic
growth, 1850-1935. Explorations in Economic History 44(3): 452-468.
Hess, D., Huang, H. and Niessen, A. (2008) How Do Commodity Futures Re-
spond to Macroeconomic News? Financial Markets and Portfolio Management
22(2): 127-146.
Hew, D., Skerratt, L., Strong, N. and Walker, M. (1996) Post-earnings-
announcement drift: Some preliminary evidence for the UK. Accounting &
Business Research 26(4): 283-293.
Hill, J.M., Balasubramanian, V., Gregory, K. and Tierens, I. (2006) Finding
Alpha via Covered Call Writing. Financial Analysts Journal 62(5): 29-46.
Hill, J.M., Nadig, D. and Hougan, M. (2015) A Comprehensive Guide to
Exchange-Traded Funds (ETFs). Research Foundation Publications 2015(3):
1-181.
Hillegeist, S.A., Keating, E., Cram, D.P. and Lunstedt, K.G. (2004) Assessing
the probability of bankruptcy. Review of Accounting Studies 9(1): 5-34.
Hilliard, J.E. (1984) Hedging Interest Rate Risk with Futures Portfolios under
Term Structure Eﬀects. Journal of Finance 39(5): 1547-1569.
207
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 209

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hilliard, J. and Jordan, S. (1989) Hedging Interest Rate Risk with Futures
Portfolios under Full-Rank Assumptions. Journal of Financial and Quantita-
tive Analysis 24(2): 217-240.
Hilliard, J. and Reis, J. (1998) Valuation of commodity futures and options
under stochastic convenience yields, interest rates, and jump diﬀusions on the
spot. Journal of Financial and Quantitative Analysis 33(1): 61-86.
Hinnerich, M. (2008) Inﬂation-indexed swaps and swaptions. Journal of Bank-
ing & Finance 32(11): 2293-2306.
Hirschey, N. (2018) Do High-Frequency Traders Anticipate Buying and Selling
Pressure? Working Paper. Available online: https://ssrn.com/abstract=
2238516.
Hirshleifer, D. (1990) Hedging Pressure and Futures Price Movements in a
General Equilibrium Model. Econometrica 58(2): 411-428.
Hirshleifer, D., Lim, S.S. and Teoh, S.H. (2009) Driven to distraction: Extra-
neous events and underreaction to earnings news. Journal of Finance 64(5):
2289-2325.
Ho, T. and Saunders, A. (1983) Fixed Rate Loan Commitments, Take-Down
Risk, and the Dynamics of Hedging with Futures. Journal of Financial and
Quantitative Analysis 18(4): 499-516.
Hodges, S. and Carverhill, A. (1993) Quasi mean reversion in an eﬃcient
stock market: the characterization of economic equilibria which support Black-
Scholes option pricing. Economic Journal 103(417): 395-405.
Hodrick, R.J. (1987) The Empirical Evidence on the Eﬃciency of Forward and
Futures Foreign Exchange Markets. New York, NY: Harwood Academic.
Hodrick, R.J. and Prescott, E.C. (1997) Postwar U.S. Business Cycles: An
Empirical Investigation. Journal of Money, Credit and Banking 29(1): 1-16.
Hoesli, M. and Lekander, J. (2008) Real estate portfolio strategy and product
innovation in Europe. Journal of Property Investment & Finance 26(2): 162-
176.
Hoevenaars, R.P.M.M., Molenaar, R.D.J., Schotman, P.C. and Steenkamp,
T.B.M. (2008) Strategic asset allocation with liabilities: Beyond stocks and
bonds. Journal of Economic Dynamics and Control 32(9): 2939-2970.
Holden, C.W. and Jacobsen, S. (2014) Liquidity Measurement Problems in
Fast Competitive Markets: Expensive and Cheap Solutions. Journal of Fi-
nance 69(4): 1747-1885.
208
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 210

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Holmes, P. (1996) Stock index futures hedging: hedge ratio estimation, dura-
tion eﬀects, expiration eﬀects and hedge ratio stability. Journal of Business
Finance & Accounting 23(1): 63-77.
Hong, H., Torous, W. and Valkanov, R. (2007) Do Industries Lead Stock
Markets? Journal of Financial Economics 83(2): 367-396.
Hopton, D. (1999) Prevention of Money Laundering: The Practical Day-to-
Day Problems and Some Solutions.Journal of Money Laundering Control 2(3):
249-252.
H¨ ordahl, P. and Tristani, O. (2012) Inﬂation Risk Premia in the Term Struc-
ture of Interest Rates. Journal of the European Economic Association 10(3):
634-657.
H¨ ordahl, P. and Tristani, O. (2014) Inﬂation Risk Premia in the Euro Area
and the United States. International Journal of Central Banking 10(3): 1-47.
Horvath, P.A. (1998) A Measurement of the Errors in Intra-Period Compound-
ing and Bond Valuation: A Short Extension. Financial Review 23(3): 359-363.
Hotchkiss, E.S. and Mooradian, R.M. (1997) Vulture Investors and the Market
for Control of Distressed Firms. Journal of Financial Economics 43(3): 401-
432.
Hotchkiss, E.S. and Ronen, R. (2002) The Informational Eﬃciency of the
Corporate Bond Market: An Intraday Analysis. Review of Financial Studies
15(5): 1325-1354.
Hou, A.J. and Nord´ en, L.L. (2018) VIX futures calendar spreads. Journal of
Futures Markets 38(7): 822-838.
Houdain, J.P. and Guegan, D. (2006) Hedging tranches index products: illus-
tration of model dependency. ICFAI Journal of Derivatives Markets 4: 39-61.
Houweling, P. and van Vundert, J. (2017) Factor Investing in the Corporate
Bond Market. Financial Analysts Journal 73(2): 100-115.
Howison, S.D., Reisinger, C. and Witte, J.H. (2013) The Eﬀect of Nonsmooth
Payoﬀs on the Penalty Approximation of American Options. SIAM Journal
on Financial Mathematics 4(1): 539-574.
Hsieh, C.H. and Barmish, B.R. (2015) On Kelly betting: Some limitations.
In: Proceeding of the 53rd Annual Allerton Conference on Communication,
Control, and Computing. Washington, DC: IEEE, pp. 165-172.
209
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 211

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hsieh, C.H., Barmish, B.R. and Gubner, J.A. (2016) Kelly betting can be too
conservative. In: Proceedings of the 2016 Conference on Decision and Control
(CDC). Washington, DC: IEEE, pp. 3695-3701.
Hsieh, J. and Walkling, R.A. (2005) Determinants and Implications of Arbi-
trage Holdings in Acquisitions. Journal of Financial Economics 77(3): 605-
648.
Hsu, M. (1998) Spark Spread Options Are Hot! Electricity Journal 11(2):
28-39.
Hsu, Y.-C., Lin, H.-W. and Vincent, K. (2018) Analyzing the Performance
of Multi-Factor Investment Strategies under Multiple Testing Framework.
Working Paper. Available online:
http://www.econ.sinica.edu.tw/UpFiles/2013092817175327692/
Seminar_PDF2013093010102890633/17-A0001(all).pdf.
Hu, J. (2001) Basics of Mortgage-Backed Securities. (2nd ed.) Hoboken, NJ:
John Wiley & Sons, Inc.
Huang, J-.Z. and Kong, W. (2003) Explaining Credit Spread Changes: New
Evidence From Option-Adjusted Bond Indexes. Journal of Derivatives 11(1):
30-44.
Huang, W., Nakamori, Y. and Wang, S.-Y. (2005) Forecasting stock market
movement direction with support vector machine. Computers & Operation
Research 32(10): 2513-2522.
Huang, H., Shiu, Y. and Lin, P. (2008) HDD and CDD option pricing with
market price of weather risk for Taiwan. Journal of Futures Markets 28(8):
790-814.
Huang, C.L. and Tsai, C.Y. (2009) A hybrid SOFM-SVR with a ﬁlter-based
feature selection for stock market forecasting. Expert Systems with Applica-
tions 36(2): 1529-1539.
Huault, I. and Rainelli-Weis, H. (2011) A Market for Weather Risk? Con-
ﬂicting Metrics, Attempts at compromise, and Limits to Commensuration.
Organization Studies 32(10): 1395-1419.
Huck, N. (2009) Pairs selection and outranking: An application to the S&P
100 index. European Journal of Operational Research 196(2): 819-825.
Huck, N. (2015) Pairs trading: Does volatility timing matter? Applied Eco-
nomics 47(57): 6239-6256.
210
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 212

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Huck, N. and Afawubo, K. (2014) Pairs trading and selection methods: is
cointegration superior? Applied Economics 47(6): 599-613.
Hudson-Wilson, S. (1990) New Trends in Portfolio Theory.Journal of Property
Management 55(3): 57-58.
Hudson-Wilson, S., Gordon, J.N., Fabozzi, F.J., Anson, M.J.P. and Giliberto,
M. (2005) Why Real Estate? Journal of Portfolio Management 31(5): 12-21.
Huerta, R., Elkan, C. and Corbacho, F. (2013) Nonlinear Support Vector Ma-
chines Can Systematically Identify Stocks with High and Low Future Returns.
Algorithmic Finance 2(1): 45-58.
H¨ uhn, H. and Scholz, H. (2017) Alpha Momentum and Price Momentum.
Working Paper. Available online: https://ssrn.com/abstract=2287848.
Huij, J. and Lansdorp, S. (2017) Residual Momentum and Reversal Strategies
Revisited. Working Paper. Available online: https://ssrn.com/abstract=
2929306.
Hull, D.A. (1996) Stemming algorithms: A case study for detailed evalua-
tion. Journal of the American Society for Information Science and Technology
47(1): 70-84.
Hull, J.C. (2012) Options, Futures and Other Derivatives. Upper Saddle River,
NJ: Prentice Hall.
Hull, J.C. and White, A.D. (2004) Valuation of a CDO and an nth to Default
CDS without Monte Carlo Simulation. Journal of Derivatives 12(2): 8-23.
Hull, J.C. and White, A.D. (2006) Valuing Credit Derivatives Using an Implied
Copula Approach. Journal of Derivatives 14(2): 8-28.
Hull, J.C. and White, A.D. (2010) An Improved Implied Copula Model and its
Application to the Valuation of Bespoke CDO Tranches.Journal of Investment
Management 8(3): 11-31.
Hull, J., Predescu, M. and White, A. (2005) Bond Prices, Default Probabilities
and Risk Premiums. Journal of Credit Risk 1(2): 53-60.
Hung, N.H. (2016) Various moving average convergence divergence trading
strategies: a comparison. Investment Management and Financial Innovations
13(2): 363-369.
Hunter, R. (1999) Managing Mother Nature. Derivatives Strategy 4(2): 15-19.
211
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 213

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Hunter, D.M. and Simon, D.P. (2005) Are TIPS the “real” deal?: A conditional
assessment of their role in a nominal portfolio. Journal of Banking & Finance
29(2): 347-368.
H¨ urlimann, W. (2002) On immunization, stop-loss order and the maximum
Shiu measure. Insurance: Mathematics and Economics 31(3): 315-325.
H¨ urlimann, W. (2012) On directional immunization and exact matching.Com-
munications in Mathematical Finance 1(1): 1-12
Hurst, B., Ooi, Y.H. and Pedersen, L.H. (2017) A Century of Evidence on
Trend-Following Investing. Journal of Portfolio Management 44(1): 15-29.
Husson, T. and McCann, C.J. (2011) The VXX ETN and Volatility Exposure.
PIABA Bar Journal 18(2): 235-252.
Hutson, E. (2000) Takeover targets and the probability of bid success: Evi-
dence from the Australian market. International Review of Financial Analysis
9(1): 45-65.
Hwang, C.-Y. and George, T.J. (2004) The 52-Week High and Momentum
Investing. Journal of Finance 59(5): 2145-2176.
Idzorek, T. (2007) A Step-by-Step Guide to the Black-Litterman Model.
In: Satchell, S. (ed.) Forecasting Expected Returns in the Financial Markets.
Waltham, MA: Academic Press.
Illueca, M. and Lafuente, J.A. (2003) The Eﬀect of Spot and Futures Trading
on Stock Index Volatility: A Non-parametric Approach. Journal of Futures
Markets 23(9): 841-858.
Ilmanen, A. (2011) Expected Returns: An Investor’s Guide to Harvesting Mar-
ket Rewards. Hoboken, NJ: John Wiley & Sons, Inc.
Ilmanen, A., Byrne, R., Gunasekera, H. and Minikin, R. (2004) Which Risks
Have Been Best Rewarded? Journal of Portfolio Management 30(2): 53-57.
Ilut, C. (2012) Ambiguity Aversion: Implications for the Uncovered Interest
Rate Parity Puzzle. American Economic Journal: Macroeconomics 4(3): 33-
65.
Inderst, G. (2010a) Infrastructure as an Asset Class. EIB Papers 15(1): 70-
105.
Inderst, G. (2010b) Pension fund investment in infrastructure: What have we
learnt? Pensions: An International Journal 15(2): 89-99.
212
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 214

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Ingersoll, J. (1977) A contingent-claims valuation of convertible securities.
Journal of Financial Economics 4(3): 289-322.
Irwin, S.H., Zulauf, C.R. and Jackson, T.E. (1996) Monte Carlo analysis of
mean reversion in commodity futures prices. American Journal of Agricultural
Economics 78(2): 387-399.
Israelov, R. (2017) Pathetic Protection: The Elusive Beneﬁts of Protec-
tive Puts. Working Paper. Available online: https://ssrn.com/abstract=
2934538.
Israelov, R. and Klein, M. (2016) Risk and Return of Equity Index Collar
Strategies. Journal of Alternative Investments 19(1): 41-54.
Israelov, R. and Nielsen, L.N. (2014) Covered Call Strategies: One Fact and
Eight Myths. Financial Analysts Journal 70(6): 23-31.
Israelov, R. and Nielsen, L.N. (2015a) Covered Calls Uncovered. Financial
Analysts Journal 71(6): 44-57.
Israelov, R. and Nielsen, L.N. (2015b) Still Not Cheap: Portfolio Protection
in Calm Markets. Journal of Portfolio Management 41(4): 108-120.
Israelov, R., Nielsen L.N. and Villalon, D. (2017) Embracing Downside Risk.
Journal of Alternative Investments 19(3): 59-67.
Ito, T., Yamada, K., Takayasu, M. and Takayasu, H. (2012) Free Lunch!
Arbitrage Opportunities in the Foreign Exchange Markets. Working Paper.
Available online: http://www.nber.org/papers/w18541.
Iturricastillo, I. and De La Pe˜ na, J.I. (2010) Absolute Immunization Risk as
general measure of immunization risk. An´ alisis Financiero114(3): 42-59.
Ivanov, I.T. and Lenkey, S.L. (2014) Are Concerns About Leveraged ETFs
Overblown? Finance and Economics Discussion Series (FEDS) , Paper No.
2014-106. Washington, DC: Board of Governors of the Federal Reserve System.
Available online: https://www.federalreserve.gov/econresdata/feds/
2014/files/2014106pap.pdf.
Jabbour, G. and Budwick, P. (2010) The option trader handbook: strategies
and trade adjustments. (2nd ed.) Hoboken, NJ: John Wiley & Sons, Inc.
Jackwerth, J.C. (2000) Recovering Risk Aversion from Option Prices and Re-
alized Returns. Review of Financial Studies 13(2): 433-451.
Jacobs, H. and Weber, M. (2015) On the determinants of pairs trading prof-
itability. Journal of Financial Markets 23: 75-97.
213
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 215

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Jacoby, G. and Shiller, I. (2008) Duration and Pricing of TIPS. Journal of
Fixed Income 18(2): 71-84.
Jain, G. and Baile, C. (2000) Managing weather risks. Strategic Risk, Septem-
ber 2000, pp. 28-31.
James, F.E., Jr. (1968) Monthly moving averages – An eﬀective investment
tool? Journal of Financial and Quantitative Analysis 3(3): 315-326.
James, T. (2003) Energy Price Risk: Trading and Price Risk Management.
London, UK: Palgrave Macmillan.
Jan, T.C. and Hung, M.W. (2004) Short-Run and Long-Run Persistence in
Mutual Funds. Journal of Investing 13(1): 67-71.
Jankowitsch, R. and Nettekoven, M. (2008) Trading strategies based on term
structure model residuals. European Journal of Finance 14(4): 281-298.
Jansen, I.P. and Nikiforov, A.L. (2016) Fear and Greed: A Returns-Based
Trading Strategy around Earnings Announcements.Journal of Portfolio Man-
agement 42(4): 88-95.
Jarrow, R.A. (2010) Understanding the risk of leveraged ETFs. Finance Re-
search Letters 7(3): 135-139.
Jarrow, R., Kchia, Y., Larsson, M. and Protter, P. (2013) Discretely sampled
variance and volatility swaps versus their continuous approximations.Finance
and Stochastics 17(2): 305-324.
Jarrow, R., Lando, D. and Turnbull, S. (1997) A Markov model for the term
structure of credit spreads. Review of Financial Studies 10(2): 481-523.
Jarrow, R.A. and Protter, P. (2012) A Dysfunctional Role of High Frequency
Trading in Electronic Markets. International Journal of Theoretical and Ap-
plied Finance 15(3): 1250022.
Jarrow, R.A. and Turnbull, S.M. (1995) Pricing Derivatives on Financial Se-
curities Subject to Credit Risk. Journal of Finance 50(1): 53-85.
Jarrow, R. and Yildirim, Y. (2003) Pricing treasury inﬂation protected secu-
rities and related derivatives using an HJM model. Journal of Financial and
Quantitative Analysis 38(2): 409-430.
Jasemi, M. and Kimiagari, A.M. (2012) An investigation of model selection
criteria for technical analysis of moving average. Journal of Industrial Engi-
neering International 8: 5.
214
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 216

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Jegadeesh, N. (1990) Evidence of Predictable Behavior of Security Returns.
Journal of Finance 45(3): 881-898.
Jegadeesh, N. and Titman, S. (1993) Returns to Buying Winners and Selling
Losers: Implications for Stock Market Eﬃciency. Journal of Finance 48(1):
65-91.
Jegadeesh, N. and Titman, S. (1995) Overreaction, delayed reaction, and con-
trarian proﬁts. Review of Financial Studies 8(4): 973-993.
Jegadeesh, N. and Titman, S. (2001) Proﬁtability of Momentum Strategies:
An Evaluation of Alternative Explanations. Journal of Finance 56(2): 699-
720.
Jensen, M.C. (1968) The Performance of Mutual Funds in the Period 1945-
1964. Journal of Finance 23(2): 389-416.
Jensen, G.R., Johnson, R.R. and Mercer, J.M. (2000) Eﬃcient use of commod-
ity futures in diversiﬁed portfolios. Journal of Futures Markets 20(5): 489-506.
Jensen, G.R., Johnson, R.R. and Mercer, J.M. (2002) Tactical Asset Allocation
and Commodity Futures. Journal of Portfolio Management 28(4): 100-111.
Jermann, U.J. (2016) Negative Swap Spreads and Limited Arbitrage. Working
Paper. Available online: https://ssrn.com/abstract=2737408.
Jetley, G. and Ji, X. (2010) The shrinking merger arbitrage spread: Reasons
and implications. Financial Analysts Journal 66(2): 54-68.
Jewson, S. (2004a) Weather Derivative Pricing and the Distributions of Stan-
dard Weather Indices on US Temperatures. Working Paper. Available online:
https://ssrn.com/abstract=535982.
Jewson, S. (2004b) Introduction to Weather Derivative Pricing. Working Pa-
per. Available online: https://ssrn.com/abstract=557831.
Jewson, S., Brix, A. and Ziehmann, C. (2005) Weather Derivative Valua-
tion: The Meteorological, Statistical, Financial and Mathematical Founda-
tions. Cambridge, UK: Cambridge University Press.
Jewson, S. and Caballero, R. (2003) Seasonality in the statistics of surface
air temperature and the pricing of weather derivatives. Meteorological Appli-
cations 10(4): 367-376.
Jha, R. and Kalimipal, M. (2010) The economic signiﬁcance of conditional
skewness in index option markets. Journal of Futures Markets 30(4): 378-406.
215
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 217

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Jiang, H., Li, D. and Wang, A. (2017) Dynamic Liquidity Management by
Corporate Bond Mutual Funds. Working Paper. Available online: https:
//ssrn.com/abstract=2776829.
Jiang, W., Li, K. and Wang, W. (2012) Hedge Funds and Chapter 11. Journal
of Finance 67(2): 513-560.
Jiang, Z. and Liang, J. (2017) Cryptocurrency Portfolio Management with
Deep Reinforcement Learning. Working Paper. Available online: https://
arxiv.org/pdf/1612.01277.pdf.
Jiang, X. and Peterburgsky, S. (2017) Investment performance of shorted lever-
aged ETF pairs. Applied Economics 49(44): 4410-4427.
Jo, H., Han, I. and Lee, H. (1997) Bankruptcy prediction using case-based
reasoning, neural networks, and discriminant analysis. Expert Systems with
Applications 13(2): 97-108.
Jobst, A. (2005) Tranche Pricing in Subordinated Loan Securitization.Journal
of Structured Finance 11(2): 64-96.
Jobst, A. (2006a) European Securitization: A GARCH Model of Secondary
Market Spreads. Journal of Structured Finance 12(1): 55-80.
Jobst, A. (2006b) Sovereign Securitization in Emerging Markets. Journal of
Structured Finance 12(3): 2-13.
Jobst, A. (2006c) Correlation, Price Discovery and Co-movement of ABS and
Equity. Derivatives Use, Trading & Regulation 12(1-2): 60-101.
Jobst, A. (2007) A Primer on Structured Finance. Journal of Derivatives &
Hedge Funds 13(3): 199-213.
John, W. and Brigitte, U. (2009) Measuring Global Money Laundering: “The
Walker Gravity Model”. Review of Law & Economics 5(2): 821-853.
Johnson, H.F. (1979) Is It Better to Go Naked on the Street? A Primer on the
Options Market. Notre Dame Lawyer (Notre Dame Law Review) 55(1): 7-32.
Johnson, T.C. (2002) Rational Momentum Eﬀects. Journal of Finance 57(2):
585-608.
Johnson, T.C. (2008) Volume, liquidity, and liquidity risk.Journal of Financial
Economics 87(2): 388-417.
Jones, F.J. (1991) Yield Curve Strategies. Journal of Fixed Income 1(2): 43-
48.
216
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 218

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Jones, C.M., Lamont, O. and Lumsdaine, R.L. (1998) Macroeconomic news
and bond market volatility. Journal of Financial Economics 47(3): 315-337.
Jongadsayakul, W. (2016) A Box Spread Test of the SET50 Index Options
Market Eﬃciency: Evidence from the Thailand Futures Exchange. Interna-
tional Journal of Economics and Financial Issues 6(4): 1744-1749.
Jongadsayakul, W. (2017) Arbitrage Opportunity In Thailand Futures Ex-
change: An Empirical Study of SET50 Index Options. In: 2017 IACB, ICE
& ISEC Proceedings, Paper No. 381. Littleton, CO: Clute Institute.
Jonsson, J. and Fridson, M. (1996) Forecasting Default Rates on High Yield
Bonds. Journal of Fixed Income 6(1): 69-77.
Jordan, B.D. and Jordan, S. (1997) Special repo rates: An empirical analysis.
Journal of Finance 52(5): 2051-2072.
Joseph, A. (1952) The Whittaker-Henderson Method of Graduation. Journal
of the Institute of Actuaries 78(1): 99-114.
Joshi, N.N. and Lambert, J.H. (2011) Diversiﬁcation of infrastructure projects
for emergent and unknown non-systematic risks. Journal of Risk Research
14(6): 717-733.
Joslin, S. and Konchitchki, Y. (2018) Interest rate volatility, the yield curve,
and the macroeconomy. Journal of Financial Economics 128(2): 344-362.
Joslin, S., Priebsch, M. and Singleton, K.J. (2014) Risk Premiums in Dynamic
Term Structure Models with Unspanned Macro Risks. Journal of Finance
69(3): 1197-1233.
Jostarndt, P. and Sautner, Z. (2010) Out-of-Court Restructuring versus For-
mal Bankruptcy in a Non-Interventionist Bankruptcy Setting. Review of Fi-
nance 14(4): 623-668.
Jostova, G., Nikolova, S., Philipov, A. and Stahel, C.W. (2013) Momentum in
Corporate Bond Returns. Review of Financial Studies 26(7): 1649-1693.
Joyce, M., Lildholdt, P. and Sorensen, S. (2010) Extracting Inﬂation Expec-
tations and Inﬂation Risk Premia from the Term Structure: A Joint Model of
the UK Nominal and Real Yield Curves. Journal of Banking & Finance 34(2):
281-294.
Judd, K.L., Kubler, F. and Schmedders, K. (2011) Bond Ladders and Optimal
Portfolios. Review of Financial Studies 24(12): 4123-4166.
Julio, I.F., Hassan, M.K. and Ngene, G.M. (2013) Trading Strategies in Fu-
tures Markets. Global Journal of Finance and Economics 10(1): 1-12.
217
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 219

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Junkus, J.C. (1991) Systematic skewness in futures contracts. Journal of Fu-
tures Markets 11(1): 9-24.
Jurek, J.W. (2014) Crash-neutral currency carry trades. Journal of Financial
Economics 113(3): 325-347.
Kablan, A. (2009) Adaptive Neuro-Fuzzy Inference System for Financial Trad-
ing using Intraday Seasonality Observation Model. International Journal of
Economics and Management Engineering 3(10): 1909-1918.
Kahn, R.N. and Lemmon, M. (2015) Smart Beta: The Owner’s Manual. Jour-
nal of Portfolio Management 41(2): 76-83.
Kahn, R.N. and Lemmon, M. (2016) The Asset Manager’s Dilemma: How
Smart Beta Is Disrupting the Investment Management Industry. Financial
Analysts Journal 72(1): 15-20.
Kahneman, D. and Tversky, A. (1979) Prospect theory: an analysis of decision
under risk. Econometrica 47(2): 263-292.
Kakodkar, A., Galiani, S., J´ onsson, J.G. and Gallo, A. (2006) Credit Deriva-
tives Handbook 2006 – Vol. 2: A Guide to the Exotics Credit Derivatives
Market. New York, NY: Credit Derivatives Strategy, Merrill Lynch.
Kakushadze, Z. (2015a) Phynance. Universal Journal of Physics and Applica-
tion 9(2): 64-133. Available online: https://ssrn.com/abstract=2433826.
Kakushadze, Z. (2015b) Mean-Reversion and Optimization. Journal of Asset
Management 16(1): 14-40. Available online: https://ssrn.com/abstract=
2478345.
Kakushadze, Z. (2015c) 4-Factor Model for Overnight Returns. Wilmott
Magazine 2015(79): 56-62. Available online: https://ssrn.com/abstract=
2511874.
Kakushadze, Z. (2015d) On Origins of Alpha. Hedge Fund Journal 108: 47-50.
Available online: https://ssrn.com/abstract=2575007.
Kakushadze, Z. (2015e) Heterotic Risk Models. Wilmott Magazine 2015(80):
40-55. Available online: https://ssrn.com/abstract=2600798.
Kakushadze, Z. (2016) 101 Formulaic Alphas. Wilmott Magazine 2016(84):
72-80. Available online: https://ssrn.com/abstract=2701346.
Kakushadze, Z. and Tulchinsky, I. (2016) Performance v. Turnover: A Story by
4,000 Alphas. Journal of Investment Strategies 5(2): 75-89. Available online:
http://ssrn.com/abstract=2657603.
218
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 220

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Kakushadze, Z. and Yu, W. (2016a) Multifactor Risk Models and Heterotic
CAPM. Journal of Investment Strategies 5(4): 1-49. Available online: https:
//ssrn.com/abstract=2722093.
Kakushadze, Z. and Yu, W. (2016b) Statistical Industry Classiﬁcation. Jour-
nal of Risk & Control 3(1): 17-65. Available online: https://ssrn.com/
abstract=2802753.
Kakushadze, Z. and Yu, W. (2017a) Statistical Risk Models.Journal of Invest-
ment Strategies 6(2): 1-40. Available online: https://ssrn.com/abstract=
2732453.
Kakushadze, Z. and Yu, W. (2017b) How to Combine a Billion Alphas.Journal
of Asset Management 18(1): 64-80. Available online: https://ssrn.com/
abstract=2739219.
Kakushadze, Z. and Yu, W. (2017c) *K-Means and Cluster Models for Can-
cer Signatures. Biomolecular Detection and Quantiﬁcation 13: 7-31. Available
online: https://ssrn.com/abstract=2908286.
Kakushadze, Z. and Yu, W. (2018a) Decoding Stock Market with Quant Al-
phas. Journal of Asset Management 19(1): 38-48. Available online: https:
//ssrn.com/abstract=2965224.
Kakushadze, Z. and Yu, W. (2018b) Notes on Fano Ratio and Portfolio Op-
timization. Journal of Risk & Control 5(1): 1-33. Available online: https:
//ssrn.com/abstract=3050140.
Kalev, P.S. and Inder, B.A. (2006) The information content of the term struc-
ture of interest rates. Applied Economics 38(1): 33-45.
Kallberg, J.G., Liu, C.L. and Trzcinka, C. (2000) The Value Added from In-
vestment Managers: An Examination of Funds of REITs. Journal of Financial
and Quantitative Analysis 35(3): 387-408.
Kalman, P.E. (1960) A New Approach to Linear Filtering and Prediction
Problems. Journal of Basic Engineering 82(1): 35-45.
Kambhu, J. (2006) Trading Risk, Market Liquidity, and Convergence Trad-
ing in the Interest Rate Swap Spread. Federal Reserve Bank of New York,
Economic Policy Review 12(1): 1-13.
Kaminski, V. (2004) Managing Energy Price Risk: The New Challenges and
Solutions. London, UK: Risk Books.
Kandel, S., Ofer, A.R. and Sarig, O. (1996) Real Interest Rates and Inﬂation:
An Ex-Ante Empirical Analysis. Journal of Finance 51(1): 205-225.
219
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 221

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Kandel, S. and Stambaugh, R.F. (1987) Long-horizon Returns and Short-
horizon Models. CRSP Working Paper No. 222. Chicago, IL: University of
Chicago.
Kang, H.B. and Gardner, J. (1989) Selling Price and Marketing Time in the
Residential Real Estate Market. Journal of Real Estate Research 4(1): 21-35.
Kang, J.K. and Lee, Y.W. (1996) The pricing of convertible debt oﬀerings.
Journal of Financial Economics 41(2): 231-248.
Kang, J., Liu, M.H. and Ni, S.X. (2002) Contrarian and momentum strategies
in the China stock market: 1993-2000. Paciﬁc-Basin Finance Journal 10(3):
243-265.
Kapadia, N. and Szado, E. (2007) The Risk Return Characteristics of the Buy-
Write Strategy on the Russell 2000 Index. Journal of Alternative Investments
9(4): 39-56.
Kaplan, P. and Lummer, S.L. (1998) Update: GSCI Collateralized Futures as
a Hedging Diversiﬁcation Tool for Institutional Portfolios.Journal of Investing
7(4): 11-18.
Kara, Y., Boyacioglu, M.A. and Baykan, O.K. (2011) Predicting direction of
stock price index movement using artiﬁcial neural networks and support vector
machines: The sample of the Istanbul Stock Exchange. Expert Systems with
Applications 38(5): 5311-5319.
Karlik, B. and Vehbi, A. (2011) Performance Analysis of Various Activation
Functions in Generalized MLP Architectures of Neural Networks. Interna-
tional Journal of Artiﬁcial Intelligence and Expert Systems 1(4): 111-122.
Karolyi, G.A. and Kho, B.C. (2004) Momentum strategies: Some bootstrap
tests. Journal of Empirical Finance 11(4): 509-536.
Karolyi, G.A. and Sanders, A.B. (1998) The Variation of Economic Risk Pre-
miums in Real Estate Returns. Journal of Real Estate Finance and Economics
17(3): 245-262.
Karolyi, G.A. and Shannon, J. (1999) Where’s the Risk in Risk Arbitrage?
Canadian Investment Review 12(2): 12-18.
Kau, J.B., Keenan, D.C., Muller, W.J., III and Epperson, J.F. (1995) The
valuation at origination of ﬁxed-rate mortgages with default and prepayment.
Journal of Real Estate Finance and Economics 11(1): 5-36.
Kawaller, I.G., Koch, P.D. and Ludan, L. (2002) Calendar spreads, outright
futures positions and risk. Journal of Alternative Investments 5(3): 59-74.
220
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 222

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Kazemi, H. and Li, Y. (2009) Market timing of CTAs: An examination of
systematic CTAs vs. discretionary CTAs. Journal of Futures Markets 29(11):
1067-1099.
Keane, F. (1996) Repo rate patterns for new Treasury notes. Federal Reserve
Bank of New York, Current Issues in Economics and Finance 2(10): 1-6.
Kelly, J.L. (1956) A New Interpretation of Information Rate. Bell System
Technical Journal 35(4): 917-926.
Kemp, K. (2007) Flipping conﬁdential: The secrets of renovating property for
proﬁt in any market. Hoboken, NJ: John Wiley & Sons, Inc.
Kenett, D.Y., Ben-Jacob, E., Stanley, H.E. and gur-Gershgoren, G. (2013)
How High Frequency Trading Aﬀects a Market Index. Scientiﬁc Reports 3:
2110.
Kenyon, C. (2008) Inﬂation is normal. Risk, July 2008, pp. 76-82.
Khan, S.A. (2002) Merger Arbitrage: A Long-Term Investment Strategy.Jour-
nal of Wealth Management 4(4): 76-81.
Khandani, A. and Lo, A.W. (2011) What Happened to the Quants in August
2007? Evidence from Factors and Transactions Data. Journal of Financial
Markets 14(1): 1-46.
Khang, C.H. (1983) A dynamic global portfolio immunization strategy in the
world of multiple interest rate changes: A dynamic immunization and minimax
theorem. Journal of Financial and Quantitative Analysis 18(3): 355-363.
Khuzwayo, B. and Mar´ e, E. (2014) Aspects of volatility targeting for South
African equity investors. South African Journal of Economic and Management
Sciences 17(5): 691-699.
Kidd, D. (2014) Global Tactical Asset Allocation: One Strategy Fits All? In:
Investment Risk and Performance. Charlottesville, VA: CFA Institute.
Kilgallen, T. (2012) Testing the Simple Moving Average across Commodities,
Global Stock Indices, and Currencies. Journal of Wealth Management 15(1):
82-100.
Kim, I.J. (1990) The analytic valuation of American options. Review of Fi-
nancial Studies 3(4): 547-572.
Kim, K. (2011) Performance Analysis of Pairs Trading Strategy Utilizing High
Frequency Data with an Application to KOSPI 100 Equities. Working Paper.
Available online: https://ssrn.com/abstract=1913707.
221
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 223

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Kim, K.J. (2003) Financial time series forecasting using support vector ma-
chines. Neurocomputing 55(1-2): 307-319.
Kim, K.J. (2006) Artiﬁcial neural networks with evolutionary instance selec-
tion for ﬁnancial forecasting. Expert Systems with Applications 30(3): 519-526.
Kim, Y. and Enke, D. (2016) Using neural networks to forecast volatility for
an asset allocation strategy based on the target volatility. Procedia Computer
Science 95: 281-286.
Kim, K. and Han, I. (2000) Genetic algorithms approach to feature discretiza-
tion in artiﬁcial neural networks for the prediction of stock price index. Expert
Systems with Applications 19(2): 125-132.
Kim, M.-K. and Leuthold, R.M. (1997) The Distributional Behavior of Futures
Price Spread Changes: Parametric and Nonparametric Tests for Gold, T-
Bonds, Corn, and Live Cattle. Working Paper. Available online: https://
ageconsearch.umn.edu/bitstream/14767/1/aceo9703.pdf.
Kim, G.H., Li, H. and Zhang, W. (2016) CDS-Bond Basis and Bond Return
Predictability. Journal of Empirical Finance 38: 307-337.
Kim, G.H., Li, H. and Zhang, W. (2017) The CDS-Bond Basis Arbitrage and
the Cross Section of Corporate Bond Returns. Journal of Futures Markets
37(8): 836-861.
Kim, Y.B., Kim, J.G., Kim, W., Im, J.H., Kim, T.H., Kang, S.J. and Kim,
C.H. (2016) Predicting Fluctuations in Cryptocurrency Transactions Based on
User Comments and Replies. PLoS ONE 11(8): e0161197.
King, R. (1986) Convertible Bond Valuation: An Empirical Test. Journal of
Financial Research 9(1): 53-69.
King, T.H.D. and Mauer, D.C. (2014) Determinants of corporate call policy
for convertible bonds. Journal of Corporate Finance 24: 112-134.
Kingma, D.P. and Ba, J. (2014) Adam: A Method for Stochastic Optimization.
Working Paper. Available online: https://arxiv.org/pdf/1412.6980.
Kirby, C. and Ostdiek, B. (2012) It’s All in the Timing: Simple Active Portfolio
Strategies that Outperform Na¨ ıve Diversiﬁcation. Journal of Financial and
Quantitative Analysis 47(2): 437-467.
Kirilenko, A., Kyle, A., Samadi, M. and Tuzun, T. (2017) The Flash Crash:
High-Frequency Trading in an Electronic Market. Journal of Finance 72(3):
967-998.
222
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 224

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Kishore, V. (2012) Optimizing Pairs Trading of US Equities in a High
Frequency Setting. Working Paper. Available online:
https://repository.upenn.edu/cgi/viewcontent.cgi?article=1095&
context=wharton_research_scholars.
Kitsul, Y. and Wright, J.H. (2013) The Economics of Options-Implied Inﬂation
Probability Density Functions. Journal of Financial Economics 110(3): 696-
711.
Klingler, S. and Sundaresan, S.M. (2016) An Explanation of Negative Swap
Spreads: Demand for Duration from Underfunded Pension Plans. Working
Paper. Available online: https://ssrn.com/abstract=2814975.
Knight, J.R. (2002) Listing Price, Time on Market, and Ultimate Selling Price:
Causes and Eﬀects of Listing Price Changes. Real Estate Economics 30(2):
213-237.
Kobor, A., Shi, L. and Zelenko, I. (2005) What Determines U.S. Swap Spreads?
World Bank Working Paper No. 62. Washington, DC: World Bank.
Kocherlakota, R., Rosenbloom, E. and Shiu, E. (1988) Algorithms for cash-
ﬂow matching. Transactions of Society of Actuaries 40: 477-484.
Kocherlakota, R., Rosenbloom, E. and Shiu, E. (1990) Cash-ﬂow matching and
linear programming duality. Transactions of Society of Actuaries 42: 281-293.
Kochin, L. and Parks, R. (1988) Was the tax-exempt bond market ineﬃcient
or were future expected tax rates negative? Journal of Finance 43(4): 913-931.
Koijen, R.S.J., Moskowitz, T.J., Pedersen, L.H. and Vrugt, E.B. (2018) Carry.
Journal of Financial Economics 127(2): 197-225.
Kolb, R.W. and Chiang, R. (1981) Improving Hedging Performance Using
Interest Rate Futures. Financial Management 10(3): 72-79.
Kolb, R.W. and Chiang, R. (1982) Duration, Immunization, and Hedging with
Interest Rate Futures. Journal of Financial Research 5(2): 161-170.
Konstantinidi, E. and Skiadopoulos, G. (2016) How does the market variance
risk premium vary over time? Evidence from S&P 500 variance swap invest-
ment returns. Journal of Banking & Finance 62: 62-75.
Koopman, S.J., Lucas, A. and Schwaab, B. (2012) Dynamic factor models
with macro, frailty, and industry eﬀects for U.S. default counts: The credit
crisis of 2008. Econometric Reviews 30(4): 521-532.
223
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 225

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Korajczyk, R.A. and Murphy, D. (2017) High Frequency Market Making to
Large Institutional Trades. Working Paper. Available online: https://ssrn.
com/abstract=2567016.
Korajczyk, R.A. and Sadka, R. (2004) Are momentum proﬁts robust to trading
costs? Journal of Finance 59(3): 1039-1082.
Kordonis, J., Symeonidis, A. and Arampatzis, A. (2016) Stock Price Fore-
casting via Sentiment Analysis on Twitter. In: Proceedings of the 20th Pan-
Hellenic Conference on Informatics (PCI’16). New York, NY: ACM, Article
No. 36.
Kordos, M. and Cwiok, A. (2011) A new approach to neural network based
stock trading strategy. In: Yin, H., Wang, W. and Rayward-Smith, V. (eds.)
Intelligent Data Engineering and Automated Learning-IDEAL. Berlin, Ger-
many: Springer, pp. 429-436.
Korkeamaki, T. and Michael, T.B. (2013) Where are they now? An analysis
of the life cycle of convertible bonds. Financial Review 48(3): 489-509.
Korol, T. (2013) Early warning models against bankruptcy risk for Central
European and Latin American enterprises. Economic Modelling 31: 22-30.
Kozhan, R., Neuberger, A. and Schneider, P. (2013) The Skew Risk Premium
in the Equity Index Market. Review of Financial Studies 26(9): 2174-2203.
Kozhan, R. and Tham, W.W. (2012) Execution Risk in High-Frequency Ar-
bitrage. Management Science 58(11): 2131-2149.
Kozhemiakin, A.V. (2007) The Risk Premium of Corporate Bonds. Journal of
Portfolio Management 33(2): 101-109.
Kozicki, S. and Tinsley, P.A. (2012) Eﬀective Use of Survey Information in
Estimating the Evolution of Expected Inﬂation. Journal of Money, Credit and
Banking 44(1): 145-169.
Kozlov, M. and Petajisto, A. (2013) Global Return Premiums on Earnings
Quality, Value, and Size. Working Paper. Available online: https://ssrn.
com/abstract=2179247.
Kraenzlin, S. (2007) The characteristics and development of the Swiss franc
repurchase agreement market. Financial Markets and Portfolio Management
21(2): 241-261.
Krainer, J. (2001) A Theory of Liquidity in Residential Real Estate Markets.
Journal of Urban Economics 49(1): 32-53.
224
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 226

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Krause, T., Ehsani, S. and Lien, D. (2014) Exchange-traded funds, liquidity
and volatility. Applied Financial Economics 24(24): 1617-1630.
Krauss, C. (2017) Statistical arbitrage pairs trading strategies: Review and
outlook. Journal of Economic Surveys 31(2): 513-545.
Krauss, C. and St¨ ubinger, J. (2017) Non-linear dependence modelling with
bivariate copulas: Statistical arbitrage pairs trading on the S&P 100. Applied
Economics 23(1): 1-18.
Krishnamurthy, A. (2002) The Bond/Old-Bond Spread. Journal of Financial
Economics 66(2): 463-506.
Kristoufek, L. (2015) What Are the Main Drivers of the Bitcoin Price? Evi-
dence from Wavelet Coherence Analysis. PLoS ONE 10(4): e0123923.
Kroner, K.F. and Sultan, J. (1993) Time-Varying Distributions and Dynamic
Hedging with Foreign Currency Futures.Journal of Financial and Quantitative
Analysis 28(4): 535-551.
Kruttli, M., Monin, P. and Watugala, S.W. (2018) Investor Concentration,
Flows, and Cash Holdings: Evidence from Hedge Funds. Working Paper.
Available online: https://ssrn.com/abstract=3031663.
Kryzanowski, L., Galler, M. and Wright, D. (1993) Using Artiﬁcial Neural
Networks to Pick Stocks. Financial Analysts Journal 49(4): 21-27.
Kuberek, R.C. and Peﬂey, N.G. (1983) Hedging Corporate Debt with U.S.
Treasury Bond Futures. Journal of Futures Markets 3(4): 345-353.
Kudryavtsev, A. (2012) Overnight stock price reversals. Journal of Advanced
Studies in Finance 3(2): 162-170.
Kuhle, J. and Alvayay, J. (2000) The Eﬃciency of Equity REIT Prices.Journal
of Real Estate Portfolio Management 6(4): 349-354.
Kumar, A. (2009) Who Gambles in the Stock Market? Journal of Finance
64(4): 1889-1933.
Kumar, V.A. (2012) Money Laundering: Concept, Signiﬁcance and its Impact.
European Journal of Business and Management 4(2): 113-119.
Kumar, M. and Thenmozhi, M. (2001) Forecasting Stock Index Movement: A
Comparison of Support Vector Machines and Random Forest.Working Paper.
Available online: https://ssrn.com/abstract=876544.
Kwok, Y.K. (2014) Game option models of convertible bonds: Determinants
of call policies. Journal of Financial Engineering 1(4): 1450029.
225
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 227

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Lafuente, J.A. (2013) Optimal cross-hedging under futures mispricing: A note.
Journal of Derivatives & Hedge Funds 19(3): 181-188.
Lahmiri, S. (2014) Wavelet low- and high-frequency components as features
for predicting stock prices with backpropagation neural networks. Journal of
King Saud University – Computer and Information Sciences 26(2): 218-227.
Lai, H.-C., Tseng, T.-C. and Huang, S.-C. (2016) Combining value averaging
and Bollinger Band for an ETF trading strategy. Applied Economics 48(37):
3550-3557.
Laitinen, E.K. and Laitinen, T. (2000) Bankruptcy prediction application of
the Taylor’s expansion in logistic regression.International Review of Financial
Analysis 9(4): 327-349.
Lakonishok, J., Lee, I., Pearson, N.D. and Poteshman, A.M. (2007) Option
market activity. Review of Financial Studies 20(3): 813-857.
Lakonishok, J., Shleifer, A. and Vishny, R.W. (1994) Contrarian investment,
extrapolation, and risk. Journal of Finance 49(5): 1541-1578.
Lakonishok, J. and Vermaelen, T. (1986) Tax-Induced Trading Around the
Ex-Day. Journal of Financial Economics 16(3): 287-319.
Lambert, M., Papageorgiou, N. and Platania, F. (2006) Market Eﬃciency
and Hedge Fund Trading Strategies. Working Paper. Available online:
https://www.edhec.edu/sites/www.edhec-portail.pprod.net/files/
edhec_working_paper_market_efficiency_and_hedge_fund_trading_
strategies_f.compressed.pdf.
Lamoureux, C.G. and Lastrapes, W. (1993) Forecasting stock return variance:
towards understanding stochastic implied volatility.Review of Financial Stud-
ies 6(2): 293-326.
Lamoureux, C. and Wansley, J. (1987) Market Eﬀects of Changes in the S&P
500 Index. Financial Review 22(1): 53-69.
Landes, W.J., Stoﬀels, J.D. and Seifert, J.A. (1985) An Empirical Test of
a Duration-Based Hedge: The Case of Corporate Bonds. Journal of Futures
Markets 5(2): 173-182.
Lang, L.H.P., Litzenberger, R.H. and Liu, A.L. (1998) Determinants of Interest
Rate Swap Spreads. Journal of Banking & Finance 22(12): 1507-1532.
Langetieg, T.C., Leibowitz, L. and Kogelman, S. (1990) Duration Target-
ing and the Management of Multiperiod Returns. Financial Analysts Journal
46(5): 35-45.
226
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 228

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Larker, D. and Lys, T. (1987) An empirical analysis of the incentives to en-
gage in costly information acquisition: The case of risk arbitrage. Journal of
Financial Economics 18(1): 111-126.
Larkin, D.E., Babin, M.L. and Rose, C.A. (2004) Structuring European real
estate private equity funds. Brieﬁngs in Real Estate Finance 3(3): 229-235.
Larsen, G. and Resnick, B. (1998) Empirical Insights on Indexing. Journal of
Portfolio Management 25(1): 51-60.
Larsson, P. and Flohr, L. (2011) Optimal proxy-hedging of options on illiq-
uid baskets. Working Paper. Available online: https://www.math.kth.se/
matstat/seminarier/reports/M-exjobb11/110131a.pdf.
Lasfer, M.A. (1995) Ex-Day Behavior: Tax or Short-Term Trading Eﬀects.
Journal of Finance 50(3): 875-897.
Laurent, J.-P. and Gregory, J. (2005) Basket Default Swaps, CDOs and Factor
Copulas. Journal of Risk 7(4): 8-23.
Laurent, J.-P., Cousin, A. and Fermanian, J.D. (2011) Hedging default risks
of CDOs in Markovian contagion models. Quantitative Finance 11(12): 1773-
1791.
Laureti, P., Medo, M. and Zhang, Y.-C. (2010) Analysis of Kelly-optimal
portfolios. Quantitative Finance 10(7): 689-697.
Lautier, D. and Galli, A. (2004) Simple and extended Kalman ﬁlters: an appli-
cation to term structures of commodity prices. Applied Financial Economics
14(13): 963-973.
Lazo, J.K., Lawson, M., Larsen, P.H. and Waldman, D.M. (2011) U.S. Eco-
nomic Sensitivity to Weather Variability. Bulletin of the American Meteoro-
logical Society 92(6): 709-720.
Lebeck, W.W. (1978) Futures trading and hedging. Food Policy 3(1): 29-35.
Lee, S. (2010) The Changing Beneﬁt of REITs to the Multi-Asset Portfolio.
Journal of Real Estate Portfolio Management 16(3): 201-215.
Lee, D.K.C., Guo, L. and Wang, Y. (2018) Cryptocurrency: A New Investment
Opportunity? Journal of Alternative Investments 20(3): 16-40.
Lee, H., Liao, T. and Tung, P. (2017) Investors’ Heterogeneity in Beliefs, the
VIX Futures Basis, and S&P 500 Index Futures Returns. Journal of Futures
Markets 37(9): 939-960.
227
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 229

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Lee, S.B. and Oh, S.H. (1993) Managing non-parallel shift risk of yield curve
with interest rate futures. Journal of Futures Markets 13(5): 515-526.
Lee, Y. and Oren, S. (2009) An equilibrium pricing model for weather deriva-
tives in a multi-commodity setting. Energy Economics 31(5): 702-713.
Lee, S. and Stevenson, S. (2005) The Case for REITs in the Mixed-Asset Port-
folio in the Short and Long Run. Journal of Real Estate Portfolio Management
11(1): 55-80.
Leggio, K. and Lien, D. (2002) Hedging gas bills with weather derivatives.
Journal of Economics and Finance 26(1): 88-100.
Lehecka, G.V. (2013) Hedging and Speculative Pressures: An Investigation
of the Relationships among Trading Positions and Prices in Commodity Fu-
tures Markets. In: Proceedings of the NCCC-134 Conference on Applied Com-
modity Price Analysis, Forecasting, and Market Risk Management. Avail-
able online: http://www.farmdoc.illinois.edu/nccc134/conf_2013/pdf/
Lehecka_NCCC-134_2013.pdf.
Lehmann, B.N. (1990) Fads, Martingales, and Market Eﬃciency. Quarterly
Journal of Economics 105(1): 1-28.
Leibowitz, M.L. and Bova, A. (2013) Duration Targeting and Index Conver-
gence. Morgan Stanley Investment Management Journal 3(1): 73-80.
Leibowitz, M.L., Bova, A. and Kogelman, S. (2014) Long-Term Bond Returns
under Duration Targeting. Financial Analysts Journal 70(1): 31-51.
Leibowitz, M.L., Bova, A. and Kogelman, S. (2015) Bond Ladders and Rolling
Yield Convergence. Financial Analysts Journal 71(2): 32-46.
Leigland, J. (2018) Changing Perceptions of PPP Risk and Return: The Case
of Brownﬁeld Concessions. Journal of Structured Finance 23(4): 47-56.
Leland, H. and Connor, G. (1995) Optimal Cash Management for Investment
Funds. Research Program in Finance Working Papers, No. RPF-244. Berkeley,
CA: University of California at Berkeley.
Leland, E.C. and Panos, N. (1997) The Puttable Bond Market: Structure,
Historical Experience, and Strategies. Journal of Fixed Income 7(3): 47-60.
Le Moigne, C. and Viveiros, ´E. (2008) Private Real Estate as an Inﬂation
Hedge: An Updated Look with a Global Perspective. Journal of Real Estate
Portfolio Management 14(4): 263-286.
Leontsinis, S. and Alexander, C. (2016) Arithmetic variance swaps. Quantita-
tive Finance 17(4): 551-569.
228
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 230

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Lessambo, F.I. (2016) International Aspects of the US Taxation System. New
York, NY: Palgrave Macmillan.
Leung, T., Li, J., Li, X. and Wang, Z. (2016) Speculative Futures Trading
under Mean Reversion. Asia-Paciﬁc Financial Markets 23(4): 281-304.
Leung, C.K.Y. and Tse, C.-Y. (2013) Flippers in housing market search.
Working Paper. Available online: https://hub.hku.hk/bitstream/10722/
190689/1/Content.pdf.
Levi, M. and Reuter, P. (2006) Money Laundering. Crime and Justice 34(1):
289-375.
Levin, A. and Davidson, A. (2005) Prepayment Risk-and Option-Adjusted
Valuation of MBS. Journal of Portfolio Management 31(4): 73-85.
Levine, A. and Pedersen, L.H. (2016) Which Trend Is Your Friend? Financial
Analysts Journal 72(3): 51-66.
Levis, M. and Liodakis, M. (1999) The Proﬁtability of Style Rotation Strate-
gies in the United Kingdom. Journal of Portfolio Management 26(1): 73-86.
Levitt, S.D. and Syverson, C. (2008) Market Distortions When Agents Are
Better Informed: The Value of Information in Real Estate Transactions. Re-
view of Economics and Statistics 90(4): 599-611.
Levy, P.S. (1991) Approaches to Investing in Distressed Securities: Active
Approaches. In: Bowman, T.A. (ed.) Analyzing Investment Opportunities in
Distressed and Bankrupt Companies. (AIMR Conference Proceedings, Vol.
1991, Iss. 1.) Chicago, IL: AIMR, pp. 44-46.
Levy, A. and Lieberman, O. (2013) Overreaction of country ETFs to US mar-
ket returns: Intraday vs. daily horizons and the role of synchronized trading.
Journal of Banking & Finance 37(5): 1412-1421.
Lewis, K. (1995) Puzzles in International Financial Markets. In: Grossman
G.M. and Rogoﬀ, K. (eds.) Handbook of International Economics, Vol. 3. Am-
sterdam, The Netherlands: North-Holland, Chapter 37.
Lewis, M. (2014) Flash Boys: A Wall Street Revolt. New York, NY: W.W.
Norton & Company, Inc.
Lewis, C.M., Rogalski, R.J. and Seward, J.K. (1999) Is convertible debt a
substitute for straight debt or for common equity? Financial Management
28(3): 5-27.
Lewis, C.M. and Verwijmeren, P. (2011) Convertible security design and con-
tract innovation. Journal of Corporate Finance 17(4): 809-831.
229
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 231

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Lhabitant, F.-S. (2002) Hedge Funds: Myths and Limits. Chichester, UK: John
Wiley & Sons, Ltd.
L’Hoir, M. and Boulhabel, M. (2010) A Bond-Picking Model for Corporate
Bond Allocation. Journal of Portfolio Management 36(3): 131-139.
Li, D.X. (2000) On default correlation: a copula function approach. Journal
of Fixed Income 9(4): 43-54.
Li, T.R., Chamrajnagar, A.S., Fong, X.R., Rizik, N.R. and Fu, F. (2018)
Sentiment-Based Prediction of Alternative Cryptocurrency Price Fluctua-
tions Using Gradient Boosting Tree Model. Working Paper. Available online:
https://arxiv.org/pdf/1805.00558.pdf.
Li, X., Deng, X., Zhu, S., Wang, F. and Xie, H. (2014) An intelligent market
making strategy in algorithmic trading. Frontiers of Computer Science 8(4):
596-608.
Li, B., Hoi, S.C.H., Sahoo, D. and Liu, Z.-Y. (2015) Moving average reversion
strategy for on-line portfolio selection. Artiﬁcial Intelligence 222: 104-123.
Li, L. and Kleindorfer, P.R. (2009) On hedging spark spread options in elec-
tricity markets. Risk and Decision Analysis 1(4): 211-220.
Li, X., Sullivan, R.N. and Garcia-Feij´ oo, L. (2014) The Limits to Arbitrage
and the Low-Volatility Anomaly. Financial Analysts Journal 70(1): 52-63.
Li, X., Sullivan, R.N. and Garcia-Feij´ oo, L. (2016) The Low-Volatility
Anomaly: Market Evidence on Systematic Risk vs. Mispricing. Financial An-
alysts Journal 72(1): 36-47.
Li, Y. and Wang, K. (1995) The Predictability of REIT Returns and Market
Segmentation. Journal of Real Estate Research 10(5): 471-482.
Li, P. and Yang, J. (2017) Pricing Collar Options with Stochastic Volatility.
Discrete Dynamics in Nature and Society 2017: 9673630.
Li, B., Zhao, P., Hoi, S.C.H. and Gopalkrishnan, V. (2012) PAMR: Passive
aggressive mean reversion strategy for portfolio selection. Machine Learning
87(2): 221-258.
Liao, G.Y. (2016) Credit migration and covered interest rate parity. Work-
ing Paper. Available online: http://scholar.harvard.edu/files/gliao/
files/creditcip.pdf.
Lien, D. (1992) Optimal Hedging and Spreading in Cointegrated Markets.
Economics Letters 40(1): 91-95.
230
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 232

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Lien, D. (2004) Cointegration and the Optimal Hedge Ratio: The General
Case. Quarterly Review of Economics and Finance 44(5): 654-658.
Lien, D. (2010) The eﬀects of skewness on optimal production and hedging
decisions: An application of the skew-normal distribution. Journal of Futures
Markets 30(3): 278-289.
Lien, D. and Luo, X. (1993) Estimating Multiperiod Hedge Ratios in Cointe-
grated Markets. Journal of Futures Markets 13(8): 909-920.
Lien, D. and Tse, Y.K. (2000) Hedging downside risk with futures contracts.
Applied Financial Economics 10(2): 163-170.
Lien, D. and Wang, Y. (2015) Eﬀects of skewness and kurtosis on production
and hedging decisions: A skewed t distribution approach. European Journal
of Finance 21(13-14): 1132-1143.
Liew, J.K.-S. and Budav´ ari, T. (2016) Do Tweet Sentiments Still Predict
the Stock Market? Working Paper. Available online: https://ssrn.com/
abstract=2820269.
Liew, J.K.-S., Li, R.Z. and Budav´ ari, T. (2018) Crypto-Currency Investing
Examined. Working Paper. Available online: https://ssrn.com/abstract=
3157926.
Liew, J.K.-S. and Mayster, B. (2018) Forecasting ETFs with Machine Learning
Algorithms. Journal of Alternative Investments 20(3): 58-78.
Liew, J. and Roberts, R. (2013) U.S. Equity Mean-Reversion Examined. Risks
1(3): 162-175.
Liew, J. and Vassalou, M. (2000) Can Book-to-Market, Size and Momentum be
Risk Factors that Predict Economic Growth? Journal of Financial Economics
57(2): 221-245.
Liew, R. and Wu, Y. (2013) Pairs trading: A copula approach. Journal of
Derivatives & Hedge Funds 19(1): 12-30.
Lin, L., Lan, L.-H. and Chuang, S.-s. (2013) An Option-Based Approach to
Risk Arbitrage in Emerging Markets: Evidence from Taiwan Takeover At-
tempts. Journal of Forecasting 32(6): 512-521.
Lin, Y.-X., McCrae, M. and Gulati, C. (2006) Loss protection in pairs trading
through minimum proﬁt bounds: A cointegration approach.Journal of Applied
Mathematics and Decision Sciences 2006(4): 1-14.
231
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 233

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Lin, S.-Y. and Shyy, G. (2008) Credit Spreads, Default Correlations and CDO
Tranching: New Evidence from CDS Quotes.Working Paper. Available online:
https://ssrn.com/abstract=496225.
Lin, C.Y. and Yung, K. (2004) Real Estate Mutual Funds: Performance and
Persistence. Journal of Real Estate Research 26(1): 69-93.
Lindahl, M. (1992) Minimum variance hedge ratios for stock index futures:
duration and expiration eﬀects. Journal of Futures Markets 12(1): 33-53.
Lioui, A. and Poncet, P. (2005) General equilibrium pricing of CPI derivatives.
Journal of Banking & Finance 29(5): 1265-1294.
Litterman, R.B. and Scheinkman, J. (1991) Common Factors Aﬀecting Bond
Returns. Journal of Fixed Income 1(1): 54-61.
Litzenberger, R.H. and Rabinowitz, N. (1995) Backwardation in oil futures
markets: Theory and empirical evidence. Journal of Finance 50(3): 1517-
1545.
Liu, B., Chang, L.B. and Geman, H. (2017) Intraday pairs trading strategies
on high frequency data: The case of oil companies.Quantitative Finance 17(1):
87-100.
Liu, B. and Dash, S. (2012) Volatility ETFs and ETNs. Journal of Trading
7(1): 43-48.
Liu, J., Longstaﬀ, F.A. and Mandell, R.E. (2006) The Market Price of Risk
in Interest Rate Swaps: The Roles of Default and Liquidity Risks. Journal of
Business 79(5): 2337-2360.
Liu, C.H. and Mei, J. (1992) The Predictability of Returns on Equity REITs
and their Co-Movement with Other Assets. Journal of Real Estate Finance
and Economics 5(4): 401-418.
Liu, F., Pantelous, A.A. and von Mettenheim, H.-J. (2018) Forecasting and
trading high frequency volatility on large indices. Quantitative Finance 18(5):
737-748.
Liu, P. and Tang, K. (2010) No-arbitrage conditions for storable commodities
and the models of futures term structures. Journal of Banking & Finance
34(7): 1675-1687.
Liu, P. and Tang, K. (2011) The stochastic behavior of commodity prices
with heteroscedasticity in the convenience yield. Journal of Empirical Finance
18(2): 211-224.
232
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 234

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Liu, Z.F. and van der Heijden, T. (2016) Model-Free Risk-Neutral Mo-
ments and Proxies. Working Paper. Available online: https://ssrn.com/
abstract=2641559.
Liu, J.-G. and Xu, E. (1998) Pricing of mortgage-backed securities with option-
adjusted spread. Managerial Finance 24(9-10): 94-109.
Liu, L.X. and Zhang, L. (2008) Momentum Proﬁts, Factor Pricing, and
Macroeconomic Risk. Review of Financial Studies 21(6): 2417-2448.
Liverance, E. (2010) Variance Swap. In: Cont, R. (ed.) Encyclopedia of Quan-
titative Finance. Hoboken, NJ: John Wiley & Sons, Inc.
Livnat, J. and Mendenhall, R.R. (2006) Comparing the post-earnings an-
nouncement drift for surprises calculated from analyst and time series fore-
casts. Journal of Accounting Research 44(1): 177-205.
Lo, A. (2008) Where Do Alphas Come From?: A New Measure of the Value
of Active Investment Management. Journal of Investment Management 6(2):
1-29.
Lo, A. (2016) What Is an Index? Journal of Portfolio Management 42(2):
21-36.
Lo, A.W. and MacKinlay, A.C. (1990) When Are Contrarian Proﬁts Due to
Stock Market Overreaction? Review of Financial Studies 3(3): 175-205.
Lo, A., Mamaysky, H. and Wang, J. (2000) Foundations of Technical Analysis:
Computational Algorithms, Statistical Inference, and Empirical Implementa-
tion. Journal of Finance 55(4): 1705-1765.
Lo, A.W., Orr, A. and Zhang, R. (2017) The Growth of Relative Wealth and
the Kelly Criterion. Working Paper. Available online: https://ssrn.com/
abstract=2900509.
Loh, R.K. and Warachka, M. (2012) Streaks in earnings surprises and the
cross-section of stock returns. Management Science 58(7): 1305-1321.
Loncarski, I., ter Horst, J.R. and Veld, C.H. (2006) The Convertible Arbitrage
Strategy Analyzed. Working Paper. Available online: https://pure.uvt.nl/
ws/files/779871/98.pdf.
Loncarski, I., ter Horst, J. and Veld, C. (2009) The Rise and Demise of the
Convertible Arbitrage Strategy. Financial Analysts Journal 65(5): 35-50.
Longstaﬀ, F. (2005) Borrower Credit and the Valuation of Mortgage-Backed
Securities. Real Estate Economics 33(4): 619-661.
233
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 235

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Longstaﬀ, F.A. (2011) Municipal Debt and Marginal Tax Rates: Is There a
Tax Premium in Asset Prices? Journal of Finance 66(3): 721-751.
Low, A., Muthuswamy, J., Sakar, S. and Terry, E. (2002) Multiperiod hedging
with futures contracts. Journal of Futures Markets 22(12): 1179-1203.
Lozovaia, T. and Hizhniakova, H. (2005) How to Extend Modern Portfolio
Theory to Make Money from Trading Equity Options. Working Paper. Avail-
able online:
http://www.ivolatility.com/doc/Dispersion_Article.pdf.
Lu, C.J., Lee, T.S. and Chiu, C. (2009) Financial time series forecasting us-
ing independent component analysis and support vector regression. Decision
Support Systems 47(2): 115-125.
Lu, L., Wang, J. and Zhang, G. (2012) Long term performance of leveraged
ETFs. Financial Services Review 21(1): 63-80.
Lucas, D.J., Goodman, L.S. and Fabozzi, F.J. (eds.) (2006)Collateralized Debt
Obligations: Structures and Analysis. Hoboken, NJ: John Wiley & Sons, Inc.
Lucca, D.O. and Moench, E. (2012) The Pre-FOMC Announcement Drift.
Journal of Finance 70(1): 329-371.
Lummer, S.L. and Siegel, L.B. (1993) GSCI Collateralized Futures: A Hedging
and Diversiﬁcation Tool for Institutional Portfolio. Journal of Investing 2(2):
75-82.
Lumpkin, S.A. (1987) Repurchase and Reverse Repurchase Agreements. Fed-
eral Reserve Bank of Richmond, Economic Review 73(1): 15-23.
Lustig, H., Roussanov, N. and Verdelhan, A. (2011) Common Risk Factors in
Currency Markets. Review of Financial Studies 24(11): 3731-3777.
Lustig, H., Roussanov, N. and Verdelhan, A. (2014) Countercyclical currency
risk premia. Journal of Financial Economics 111(3): 527-553.
Lustig, H. and Verdelhan, A. (2007) The Cross-Section of Foreign Currency
Risk Premia and US Consumption Growth Risk. American Economic Review
97(1): 89-117.
Ma, K., Mercer, M. and Walker, M. (1992) Rolling over futures contracts: A
note. Journal of Futures Markets 12(2): 203-217.
Maaravi, Y. and Levy, A. (2017) When your anchor sinks your boat: Informa-
tion asymmetry in distributive negotiations and the disadvantage of making
the ﬁrst oﬀer. Judgment and Decision Making 12(5): 420-429.
234
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 236

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Macaulay, F.R. (1938) Some theoretical problems suggested by the movements
of interest rates, bond yields and stock prices in the United States since 1856.
New York, NY: NBER, Inc.
MacKinnon, G.H. and Al Zaman, A. (2009) Real estate for the long term: the
eﬀect of return predictability on long-horizon allocations. Real Estate Eco-
nomics 37(1): 117-153.
Mackintosh, P. (2017) It’s all about active ETFs. Journal of Index Investing
7(4): 6-15.
Madhavan, A. (2012) Exchange-Traded Funds, Market Structure, and the
Flash Crash. Financial Analysts Journal 68(4): 20-35.
Madhavan, A.N. (2016) Exchange-Traded Funds and the New Dynamics of
Investing. Oxford, UK: Oxford University Press.
Madura, J. and Ngo, T. (2008) Impact of ETF inception on the valuation and
trading of component stocks. Applied Financial Economics 18(12): 995-1007.
Maghrebi, N., Kim, M. and Nishina, K. (2007) The KOSPI200 Implied Volatil-
ity Index: Evidence of Regime Shifts in Expected Volatility.Asia-Paciﬁc Jour-
nal of Financial Studies 36(2): 163-187.
Maheswaran, K. and Yeoh, S.C. (2005) The Proﬁtability of Merger Arbitrage:
Some Australian Evidence. Australian Journal of Management 30(1): 111-126.
Malizia, E.E. and Simons, R.A. (1991) Comparing Regional Classiﬁcations for
Real Estate Portfolio Diversiﬁcation. Journal of Real Estate Research 6(1):
53-77.
Malkiel, B.G. (2014) Is Smart Beta Really Smart? Journal of Portfolio Man-
agement 40(5): 127-134.
Malpezzi, S. (1999) A Simple Error Correction Model of House Prices. Journal
of Housing Economics 8(1): 27-62.
Maluf, Y.S. and Albuquerque, P.H.M. (2013) Empirical evidence: arbitrage
with Exchange-traded Funds (ETFs) on the Brazilian market. Revista Con-
tabilidade & Finan¸ cas24(61): 64-74.
Mancini-Griﬀoli, T. and Ranaldo, A. (2011) Limits to Arbitrage During the
Crisis: Funding Liquidity Constraints and Covered Interest Parity. Working
Paper. Available online: https://ssrn.com/abstract=1549668.
Mankiw, N.G. and Summers, L.H. (1984) Do Long-Term Interest Rates Over-
react to Short-Term Interest Rates? Brookings Papers on Economic Activity ,
No. 1, pp. 223-242.
235
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 237

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Mann, S.V. and Ramanlal, P. (1997) The relative performance of yield curve
strategies. Journal of Portfolio Management 23(4): 64-70.
Manoliu, M. (2004) Storage options valuation using multilevel trees and cal-
endar spreads. International Journal of Theoretical and Applied Finance 7(4):
425-464.
Maribu, K.M., Galli, A. and Armstrong, M. (2007) Valuation of spark-spread
options with mean reversion and stochastic volatility. International Journal of
Electronic Business Management 5(3): 173-181.
Mark, N.C. and Wu, Y. (2001) Rethinking Deviations From Uncovered Interest
Parity: the Role of Covariance Risk and Noise. Economic Journal 108(451):
1686-1706.
Markowitz, H. (1952) Portfolio Selection. Journal of Finance 7(1): 77-91.
Markwardt, D., Lopez, C. and DeVol, R. (2016) The Economic Impact of
Chapter 11 Bankruptcy versus Out-of-Court Restructuring.Journal of Applied
Corporate Finance 28(4): 124-128.
Marques, C.R., Neves, P.D. and Sarmento, L.M. (2003) Evaluating core inﬂa-
tion indicators. Economic Modelling 20(4): 765-775.
Marshall, C.M. (2008) Volatility trading: Hedge funds and the search for alpha
(new challenges to the eﬃcient markets hypothesis) (Ph.D. Thesis). New York,
NY: Fordham University. Available online: https://fordham.bepress.com/
dissertations/AAI3353774/.
Marshall, C.M. (2009) Dispersion trading: Empirical evidence from U.S. op-
tions markets. Global Finance Journal 20(3): 289-301.
Marshall, B.R., Cahan, R.H. and Cahan, J.M. (2008) Can commodity futures
be proﬁtably traded with quantitative market timing strategies? Journal of
Banking & Finance 32(9): 1810-1819.
Marshall, B.R., Nguyen, N.H. and Visaltanachoti, N. (2013) ETF arbitrage:
Intraday evidence. Journal of Banking & Finance 37(9): 3486-3498.
Martellini, L., Milhau, V. and Tarelli, A. (2015) Hedging Inﬂation-Linked Lia-
bilities without Inﬂation-Linked Instruments through Long/Short Investments
in Nominal Bonds. Journal of Fixed Income 24(3): 5-29.
Martellini, L., Priaulet, P. and Priaulet, S. (2002) Understanding the butterﬂy
strategy. Journal of Bond Trading and Management 1(1): 9-19.
236
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 238

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Martellini, L., Priaulet, P. and Priaulet, S. (2003) Fixed Income Securities:
Valuation, Risk Management and Portfolio Strategies. Hoboken, NJ: John Wi-
ley & Sons, Inc.
Martin, G. (2010) The Long-Horizon Beneﬁts of Traditional and New Real
Assets in the Institutional Portfolio. Journal of Alternative Investments 13(1):
6-29.
Martin, I. (2011) Simple Variance Swaps. Working Paper. Available online:
http://www.nber.org/papers/w16884.
Martinelli, R. and Rhoads, N. (2010) Predicting Market Data Using The
Kalman Filter, Part 1 and Part 2.Technical Analysis of Stocks & Commodities
28(1): 44-47; ibid. 28(2): 46-51.
Mart´ ınez, B. and Torr´ o, H. (2018) Hedging spark spread risk with futures.
Energy Policy 113: 731-746.
Maslov, S. and Zhang, Y.-C. (1998) Optimal investment strategy for risky
assets. International Journal of Theoretical and Applied Finance 1(3): 377-
387.
Matsypura, D. and Timkovsky, V.G. (2010) Combinatorics of Option Spreads:
The Margining Aspect. Working Paper. Available online:
https://ses.library.usyd.edu.au/bitstream/2123/8172/1/OMWP_2010_
04.pdf.
Mauer, R. and Sebastian, S. (2002) Inﬂation Risk Analysis of European Real
Estate Securities. Journal of Real Estate Research 24(1): 47-78.
Mayers, D. (1998) Why ﬁrms issue convertible bonds: The matching of ﬁ-
nancial and real investment options. Journal of Financial Economics 47(1):
83-102.
Mayhew, S. (1995) Implied Volatility. Financial Analysts Journal 51(4): 8-20.
Maze, S. (2012) Dispersion Trading in South Africa: An Analysis of Prof-
itability and a Strategy Comparison.Working Paper. Available online: https:
//ssrn.com/abstract=2398223.
Mazurczak, A. (2011) Development of Real Estate Investment Trust (REIT)
regimes in Europe. Journal of International Studies 4(1): 115-123.
McCants, A. (2007) Goods at Pawn: The Overlapping Worlds of Material
Possessions and Family Finance in Early Modern Amsterdam. Social Science
History 31(2): 213-238.
237
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 239

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
McComas, A. (2003) Getting technical with spreads. Futures Magazine, July
2013, pp. 52-55.
McConnell, J.J. and Buser, S.A. (2011) The Origins and Evolution of the Mar-
ket for Mortgage-Backed Securities. Annual Review of Financial Economics 3:
173-192.
McConnell, J.J. and Schwartz, E.S. (1986) LYON Taming.Journal of Finance
41(3): 561-577.
McDevitt, D. and Kirwan, J. (2008) Corporate and Infrastructure-backed
Inﬂation-linked Bonds. In: Benaben, B. and Goldenberg, S. (eds.) Inﬂation
Risk and Products: The Complete Guide. London, UK: Risk Books, pp. 621-
641.
McDonald, R.L. (2001) Cross-Border Investing with Tax Arbitrage: The Case
of German Dividend Tax Credits. Review of Financial Studies 14(3): 617-657.
Mcelroy, T. (2008) Exact formulas for the Hodrick-Prescott Filter. Economet-
rics Journal 11(1): 208-217.
McEnally, R.W. and Rice, M.L. (1979) Hedging Possibilities in the Flotation
of Debt Securities. Financial Management 8(4): 12-18.
McKee, T.E. and Lensberg, T. (2002) Genetic programming and rough sets: A
hybrid approach to bankruptcy classiﬁcation.European Journal of Operational
Research 138(2): 436-451.
McKenzie, J.A. (2002) A Reconsideration of the Jumbo/Non-Jumbo Mortgage
Rate Diﬀerential. Journal of Real Estate Finance and Economics 25(2-3): 197-
213.
McMillan, L.G. (2002) Options as a Strategic Investment. (4th ed.) New York,
NY: New York Institute of Finance.
Meen, G. (2002) The Time-Series Behavior of House Prices: A Transatlantic
Divide? Journal of Housing Economics 11(1): 1-23.
Mehra, Y.P. (2002) Survey Measures of Expected Inﬂation: Revisiting the
Issues of Predictive Content and Rationality. Federal Reserve Bank of Rich-
mond, Economic Quarterly 88(3): 17-36.
Mei, J. and Gao, B. (1995) Price Reversals, Transaction costs and Arbitrage
Proﬁts in the Real Estate Securities Market. Journal of Real Estate Finance
and Economics 11(2): 153-165.
238
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 240

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Mei, J. and Liao, H.H. (1998) Risk Characteristics of Real Estate Related Se-
curities: An Extension of Liu and Mei (1992). Journal of Real Estate Research
16(3): 279-290.
Meissner, G. (ed.) (2008) The Deﬁnitive Guide to CDOs. London, UK: Incisive
Media.
Meissner, G. (2016) Correlation Trading Strategies: Opportunities and Limi-
tations. Journal of Trading 11(4): 14-32.
Mendenhall, R. (2004) Arbitrage Risk and the Post-Earnings-Announcement
Drift. Journal of Business 77(6): 875-894.
Menkhoﬀ, L., Sarno, L., Schmeling, M. and Schrimpf, A. (2012) Currency
momentum strategies. Journal of Financial Economics 106(3): 660-684.
Menkveld, A.J. (2013) High Frequency Trading and the New Market Makers.
Journal of Financial Markets 16(4): 712-740.
Menkveld, A.J. (2016) The Economics of High-Frequency Trading: Taking
Stock. Annual Review of Financial Economics 8: 1-24.
Mercurio, F. (2005) Pricing inﬂation-indexed derivatives.Quantitative Finance
5(3): 289-302.
Mercurio, F. and Moreni, N. (2006) Inﬂation with a smile. Risk 19(3): 70-75.
Mercurio, F. and Moreni, N. (2009) Inﬂation modelling with SABR dynamics.
Risk, June 2009, pp. 106-111.
Mercurio, F. and Yildirim, Y. (2008) Modelling Inﬂation. In: Benaben, B.
and Goldenberg, S. (eds.) Inﬂation Risks and Products: The Complete Guide.
London, UK: Risk Books.
Merton, R.C. (1987) A Simple Model of Capital Market Equilibrium with
Incomplete Information. Journal of Finance 42(3): 483-510.
Metghalchi, M., Marcucci, J. and Chang, Y.-H. (2012) Are moving average
trading rules proﬁtable? Evidence from the European stock markets. Applied
Economics 44(12): 1539-1559.
Meziani, A.S. (2015) Active exchange-traded funds: Are we there yet? Journal
of Index Investing 6(2): 86-98.
Mhaskar, H.N. and Micchelli, C.A. (1993) How to choose an activation func-
tion. In: Proceedings of the 6th International Conference on Neural Informa-
tion Processing Systems (NIPS’93). San Francisco, CA: Morgan Kaufmann
Publishers, Inc., pp. 319-326.
239
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 241

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Miao, G.J. (2014) High frequency and dynamic pairs trading based on sta-
tistical arbitrage using a two-stage correlation and cointegration approach.
International Journal of Economics and Finance 6(3): 96-110.
Miao, G.J., Wei, B. and Zhou, H. (2012) Ambiguity Aversion and Variance
Premium. Working Paper. Available online: https://ssrn.com/abstract=
2023765.
Miﬀre, J. (2012) Hedging pressure-based long/short commodity strategy used
for third generation commodity index. Risk, January 2012. Available online:
https://www.risk.net/2247251.
Miﬀre, J. and Rallis, G. (2007) Momentum strategies in commodity futures
markets. Journal of Banking & Finance 31(6): 1863-1886.
Milanov, K., Kounchev, O., Fabozzi, F.J., Kim, Y.S. and Rachev, S.T. (2013)
A Binomial-Tree Model for Convertible Bond Pricing.Journal of Fixed Income
22(3): 79-94.
Miles, M. and Mahoney, J. (1997) Is commercial real estate an inﬂation hedge?
Real Estate Finance 13(4): 31-45.
Miles, M. and McCue, T. (1984) Commercial Real Estate Returns. Real Estate
Economics 12(3): 355-377.
Miller, M.H. (1977) Debt and taxes. Journal of Finance 32(2): 261-275.
Milonas, N.T. (1991) Measuring seasonalities in commodity markets and the
half-month eﬀect. Journal of Futures Markets 11(3): 331-346.
Milosevic, N. (2016) Equity Forecast: Predicting Long Term Stock Price Move-
ment using Machine Learning. Journal of Economics Library 3(2): 288-294.
Miltersen, K.R. and Schwartz, E.S. (1998) Pricing of options on commodity
futures with stochastic term structures of convenience yield and interest rates.
Journal of Financial and Quantitative Analysis 33(1): 33-59.
Min, S., Lee, J. and Han, I. (2006) Hybrid genetic algorithms and support
vector machines for bankruptcy prediction. Expert Systems with Applications
31(3): 652-660.
Minton, B.A. (1997) An empirical examination of basic valuation models for
plain vanilla U.S. interest rate swaps. Journal of Financial Economics 44(2):
251-277.
Mitchell, M. and Pulvino, T. (2001) Characteristics of Risk and Return in
Risk Arbitrage. Journal of Finance 56(6): 2135-2175.
240
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 242

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Mittal, A. and Goel, A. (2012) Stock Prediction Using Twitter Sentiment
Analysis. Working Paper. Palo Alto, CA: Stanford University.
Mitton, T. and Vorkink, K. (2007) Equilibrium Underdiversiﬁcation and the
Preference for Skewness. Review of Financial Studies 20(4): 1255-1288.
Mixon, S. (2007) The implied volatility term structure of stock index options.
Journal of Empirical Finance 14(3): 333-354.
Mixon, S. (2011) What Does Implied Volatility Skew Measure? Journal of
Derivatives 18(4): 9-25.
Mladina, P. (2014) Dynamic Asset Allocation with Horizon Risk: Revisiting
Glide Path Construction. Journal of Wealth Management 16(4): 18-26.
Monkhouse, P.H.L. (1993) The Cost of Equity Under the Australian Dividend
Imputation Tax System. Accounting and Finance 33(2): 1-18.
Monoyios, M. (2004) Performance of Utility-Based Strategies for Hedging Ba-
sis Risk. Quantitative Finance 4(3): 245-255.
Monoyios, M. and Sarno, L. (2002) Mean reversion in stock index futures
markets: a nonlinear analysis. Journal of Futures Markets 22(4): 285-314.
Montelongo, A. and Chang, H.K. (2008) Flip and grow rich: The heart and
mind of real estate investing. San Antonio, TX: Armondo Montelongo World-
wide, Inc.
Montrucchio, L. and Peccati, L. (1991) A note on Shiu-Fisher-Weil immuniza-
tion theorem. Insurance: Mathematics and Economics 10(2): 125-131.
Moore, S., Toepke, J. and Colley, N. (2006) The encyclopedia of commodity
and ﬁnancial spreads. Hoboken, NJ: John Wiley & Sons, Inc.
Moosa, I. (2001) Triangular Arbitrage in the Spot and Forward Foreign Ex-
change Markets. Quantitative Finance 1(4): 387-390.
Moosa, I.A. (2003a) Two-Currency, Three-Currency and Multi-Currency Ar-
bitrage. In: International Financial Operations: Arbitrage, Hedging, Specula-
tion, Financing and Investment. Finance and Capital Markets Series. London,
UK: Palgrave Macmillan, Chapter 1, pp. 1-18.
Moosa, I.A. (2003b) The sensitivity of the optimal hedge ratio to model spec-
iﬁcation. Finance Letters 1(1): 15-20.
Moran, M.T. and Dash, S. (2007) VIX Futures and Options: Pricing and
Using Volatility Products to Manage Downside Risk and Improve Eﬃciency
in Equity Portfolios. Journal of Trading 2(3): 96-105.
241
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 243

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Morisawa, Y. (2009) Toward a Geometric Formulation of Triangular Arbitrage:
An Introduction to Gauge Theory of Arbitrage.Progress of Theoretical Physics
Supplement 179: 209-215.
Morse, D. and Shaw, W. (1988) Investing in Bankrupt Firms. Journal of Fi-
nance 43(5): 1193-1206.
Moskowitz, T.J. and Grinblatt, M. (1999) Do Industries Explain Momentum?
Journal of Finance 54(4): 1249-1290.
Moskowitz, T.J., Ooi, Y.H. and Pedersen, L.H. (2012) Time Series Momentum.
Journal of Financial Economics 104(2): 228-250.
Moss, A., Clare, A., Thomas, S. and Seaton, J. (2015) Trend Following and
Momentum Strategies for Global REITs. Journal of Real Estate Portfolio
Management 21(1): 21-31.
Mossman, C.E., Bell, G.G., Swartz, L.M. and Turtle, H. (1998) An empirical
comparison of bankruptcy models. Financial Review 33(2): 35-54.
Mou, Y. (2010) Limits to Arbitrage and Commodity Index Investment: Front-
Running the Goldman Roll. Working Paper. Available online: https://ssrn.
com/abstract=1716841.
Mouakhar, T. and Roberge, M. (2010) The Optimal Approach to Futures
Contract Roll in Commodity Portfolios. Journal of Alternative Investments
12(3): 51-60.
Moyer, S.G., Martin, D. and Martin, J. (2012) A Primer on Distressed Invest-
ing: Buying Companies by Acquiring Their Debt. Journal of Applied Corpo-
rate Finance 24(4): 59-76.
Mraoua, M. (2007) Temperature stochastic modelling and weather derivatives
pricing: empirical study with Moroccan data. Afrika Statistika 2(1): 22-43.
Mueller, G.R. (1993) Reﬁning Economic Diversiﬁcation Strategies for Real
Estate Portfolios. Journal of Real Estate Research 8(1): 55-68.
Mueller, G.R. and Laposa, S.P. (1995) Property-Type Diversiﬁcation in Real
Estate Portfolios: A Size and Return Perspective. Journal of Real Estate Port-
folio Management 1(1): 39-50.
Mueller, A. and Mueller, G. (2003) Public and Private Real Estate in a Mixed-
Asset Portfolio. Journal of Real Estate Portfolio Management 9(3): 193-203.
Mugwagwa, T., Ramiah, V., Naughton, T. and Moosa, I. (2012) The eﬃciency
of the buy-write strategy: Evidence from Australia. Journal of International
Financial Markets, Institutions and Money 22(2): 305-328.
242
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 244

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
M¨ uller, A. and Grandi, M. (2000) Weather Derivatives: A Risk Management
Tool for Weather-sensitive Industries. Geneva Papers on Risk and Insurance
25(2): 273-287.
Mun, K.-C. (2016) Hedging bank market risk with futures and forwards.Quar-
terly Review of Economics and Finance 61: 112-125.
Mun, K.-C. and Morgan, G.E. (1997) Cross-hedging foreign exchange rate
risks: The case of deposit money banks in emerging Asian countries. Paciﬁc-
Basin Finance Journal 5(2): 215-230.
Mun, J.C., Vasconcellos, G.M. and Kish, R. (2000) The contrarian overreac-
tion hypothesis: An analysis of the US and Canadian stock markets. Global
Finance Journal 11(1-2): 53-72.
Murphy, J.J. (1986) Technical analysis of the futures markets: A comprehen-
sive guide to trading methods and applications. New York, NY: New York
Institute of Finance.
Muthuswamy, J., Palmer, J., Richie, N. and Webb, R. (2011) High-Frequency
Trading: Implications for Markets, Regulators, and Eﬃciency. Journal of
Trading 6(1): 87-97.
Mwangi, C.I. and Duncan, M.O. (2012) An investigation into the existence of
exchange rate arbitrage in the Mombasa spot market. International Journal
of Humanities and Social Science 2(21): 182-196.
Myers, R.J. (1991) Estimating time-varying optimal hedge ratios on futures
markets. Journal of Futures Markets 11(1): 39-53.
Nakamoto, S. (2008) Bitcoin: A Peer-to-Peer Electronic Cash System. Work-
ing Paper. Available online: https://bitcoin.org/bitcoin.pdf.
Nakano, M., Takahashi, A. and Takahashi, S. (2018) Bitcoin Technical Trading
With Artiﬁcial Neural Network. Working Paper. Available online: https:
//ssrn.com/abstract=3128726.
Nandy (Pal), S. and Chattopadhyay, A.Kr. (2016) Impact of Individual Stock
Derivatives Introduction in India on Its Underlying Spot Market Volatility.
Asia-Paciﬁc Journal of Management Research and Innovation 12(2): 109-133.
Nartea, G. and Eves, C. (2010) Role of farm real estate in a globally diversiﬁed
asset portfolio. Journal of Property Investment & Finance 28(3): 198-220.
Nashikkar, A., Subrahmanyam, M.G. and Mahanti, S. (2011) Liquidity and
Arbitrage in the Market for Credit Risk.Journal of Financial and Quantitative
Analysis 46(3): 627-656.
243
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 245

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Nawalkha, S.K. and Chambers, D.R. (1996) An improved immunization strat-
egy: M-absolute. Financial Analysts Journal 52(5): 69-76.
Nekrasov, V. (2014) Kelly Criterion for Multivariate Portfolios: A Model-Free
Approach. Working Paper. Available online: https://ssrn.com/abstract=
2259133.
Nelken, I. (2006) Variance swap volatility dispersion.Derivatives Use, Trading
& Regulation 11(4): 334-344.
Nelling, E. and Gyourko, J. (1998) The Predictability of Equity REIT Returns.
Journal of Real Estate Research 16(3): 251-268.
Newell, G. (1996) The inﬂation-hedging characteristics of Australian commer-
cial property: 1984-1995. Journal of Property Finance 7(1): 6-20.
Newell, G., Chau, K.W. and Wong, S.K. (2009) The signiﬁcance and perfor-
mance of infrastructure in China. Journal of Property Investment & Finance
27(2): 180-202.
Newell, G. and Peng, H.W. (2008) The role of US infrastructure in investment
portfolios. Journal of Real Estate Portfolio Management 14(1): 21-34.
Newell, G., Peng, H.W. and De Francesco, A. (2011) The performance of
unlisted infrastructure in investment portfolios. Journal of Property Research
28(1): 59-74.
Ng, K.Y. and Phelps, B.D. (2015) The Hunt for a Low-Risk Anomaly in the
USD Corporate Bond Market. Journal of Portfolio Management 42(1): 63-84.
Ng, V.K. and Pirrong, S.C. (1994) Fundamentals and volatility: storage,
spreads, and the dynamics of metals prices. Journal of Business 67(2): 203-
230.
Ng, J., Rusticus, T. and Verdi, R. (2008) Implications of Transaction Costs
for the Post-Earnings Announcement Drift. Journal of Accounting Research
46(3): 661-696.
Nguyen, V.T.T. and Sercu, P. (2010) Tactical Asset Allocation with Commod-
ity Futures: Implications of Business Cycle and Monetary Policy. Working
Paper. Available online: https://ssrn.com/abstract=1695889.
Niblock, S.J. (2017) Flight of the Condors: Evidence on the Performance of
Condor Option Spreads in Australia. Applied Finance Letters 6(1): 38-53.
Nielsen, M.J. and Schwartz, E.S. (2004) Theory of storage and the pricing of
commodity claims. Review of Derivatives Research 7(1): 5-24.
244
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 246

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Nisar, T.M. and Yeung, M. (2018) Twitter as a tool for forecasting stock
market movements: A short-window event study.Journal of Finance and Data
Science 4(2): 101-119.
Noh, J., Engle, R.F. and Kane, A. (1994) Forecasting volatility and option
prices of the S&P500 Index. Journal of Derivatives 2(1): 17-30.
Nossman, M. and Wilhelmsson, A. (2009) Is the VIX Futures Market Able
to Predict the VIX Index? A Test of the Expectation Hypothesis. Journal of
Alternative Investments 12(2): 54-67.
Nothaft, F.E., Lekkas, V. and Wang, G.H.K. (1995) The Failure of the
Mortgage-Backed Futures Contract. Journal of Futures Markets 15(5): 585-
603.
Novak, M.G. and Veluˇ s¸ cek, D. (2016) Prediction of stock price movement
based on daily high prices. Quantitative Finance 16(5): 793-826.
Novy-Marx, R. (2009) Hot and Cold Markets. Real Estate Economics 37(1):
1-22.
Novy-Marx, R. (2013) The other side of value: The gross proﬁtability pre-
mium. Journal of Financial Economics 108(1): 1-28.
Nyaradi, J. (2010) Super Sectors: How to Outsmart the Market Using Sector
Rotation and ETFs. Hoboken, NJ: John Wiley & Sons, Inc.
Odean, T. (2002) Volume, Volatility, Price, and Proﬁt When All Traders Are
Above Average. Journal of Finance 53(6): 1887-1934.
O’Doherty, M.S. (2012) On the Conditional Risk and Performance of Finan-
cially Distressed Stocks. Management Science 58(8): 1502-1520.
Odom, M.D. and Sharda, R. (1990) A neural network model for bankruptcy
prediction. In: Proceedings of the International Joint Conference on Neural
Networks, Vol. 2. Washington, DC: IEEE, pp. 163-168.
Oetomo, T. and Stevenson, M. (2005) Hot or cold? A comparison of diﬀerent
approaches to the pricing of weather derivatives. Journal of Emerging Market
Finance 4(2): 101-133.
Oﬃcer, M.S. (2004) Collars and renegotiation in mergers and acquisitions.
Journal of Finance 59(6): 2719-2743.
Oﬃcer, M.S. (2006) The market pricing of implicit options in merger collars.
Journal of Business 79(1): 115-136.
245
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 247

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
O’Hara, M. (2015) High frequency market microstructure. Journal of Finan-
cial Economics 116(2): 257-270.
Ohlson, J.A. (1980) Financial Ratios and the Probabilistic Prediction of
Bankruptcy. Journal of Accounting Research 18(1): 109-131.
Okunev, J. and White, D. (2003) Do Momentum-Based Strategies Still Work
in Foreign Currency Markets? Journal of Financial and Quantitative Analysis
38(2): 425-447.
Olmo, J. and Pilbeam, K. (2009) The proﬁtability of carry trades. Annals of
Finance 5(2): 231-241.
Olszweski, F. and Zhou, G. (2013) Strategy diversiﬁcation: Combining mo-
mentum and carry strategies within a foreign exchange portfolio. Journal of
Derivatives & Hedge Funds 19(4): 311-320.
O’Neal, E.S. (2000) Industry Momentum and Sector Mutual Funds. Financial
Analysts Journal 56(4): 37-49.
Opler, T., Pinkowitz, L., Stulz, R. and Williamson, R. (1999) The deter-
minants and implications of corporate cash holdings. Journal of Financial
Economics 52(1): 3-46.
Opp, C.C. (2017) Learning, Optimal Default, and the Pricing of Distress Risk.
Working Paper. Available online: https://ssrn.com/abstract=2181441.
Ortalo-Magn´ e, F. and Rady, S. (2006) Housing Market Dynamics: On the
Contribution of Income Shocks and Credit Constraints. Review of Economic
Studies 73(2): 459-485.
Ortisi, M. (2016) Bitcoin Market Volatility Analysis Using Grand Canonical
Minority Game. Ledger 1: 111-118.
Osborne, M.J. (2005) On the computation of a formula for the duration of a
bond that yields precise results. Quarterly Review of Economics and Finance
45(1): 161-183.
Osler, C.L. (2000) Support for Resistance: Technical Analysis and Intraday
Exchange Rates. Federal Reserve Bank of New York, Economic Policy Review
6(2): 53-68.
Osler, C.L. (2003) Currency Orders and Exchange Rate Dynamics: An ex-
planation for the predictive success of Technical Analysis. Journal of Finance
58(5): 1791-1819.
Osteryoung, J.S., McCarty, D.E. and Roberts, G.S. (1981) Riding the Yield
Curve with Treasury Bills. Financial Review 16(3): 57-66.
246
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 248

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Osu, B.O. (2010) Currency Cross Rate and Triangular Arbitrage in Nigerian
Exchange Market. International Journal of Trade, Economics and Finance
1(4): 345-348.
O’Tool, R. (2013) The Black-Litterman model: A risk budgeting perspective.
Journal of Asset Management 14(1): 2-13.
Ou, P. and Wang, H. (2009) Prediction of stock market index movement by
ten data mining techniques. Modern Applied Science 3(12): 28-42.
Oyedele, J.B., Adair, A. and McGreal, S. (2014) Performance of global listed
infrastructure investment in a mixed asset portfolio. Journal of Property Re-
search 31(1): 1-25.
Ozdagli, A.K. (2010) The Distress Premium Puzzle. Working Paper. Available
online: https://ssrn.com/abstract=1713449.
Oztekin, A.S., Mishra, S., Jain, P.K., Daigler, R.T., Strobl, S. and Holowczak,
R.D. (2017) Price Discovery and Liquidity Characteristics for U.S. Electronic
Futures and ETF Markets. Journal of Trading 12(2): 59-72.
Packer, F. and Zhu, H. (2005) Contractual terms and CDS pricing. BIS Quar-
terly Review, March 2005, pp. 89-100. Available online: https://www.bis.
org/publ/qtrpdf/r_qt0503h.pdf.
Pagnotta, E. and Philippon, T. (2012) Competing on Speed. Working Paper.
Available online: https://ssrn.com/abstract=1972807.
Pagolu, V.S., Reddy, K.N., Panda, G. and Majhi, B. (2016) Sentiment analysis
of Twitter data for predicting stock market movements. In: Proceedings of the
2016 International Conference on Signal Processing, Communication, Power
and Embedded System (SCOPES). Washington, DC: IEEE, pp. 1345-1350.
Pagonidis, A.S. (2014) The IBS Eﬀect: Mean Reversion in Equity ETFs.
Working Paper. Available online:
http://www.naaim.org/wp-content/uploads/2014/04/00V_Alexander_
Pagonidis_The-IBS-Effect-Mean-Reversion-in-Equity-ETFs-1.pdf .
Pan, J. and Poteshman, A.M. (2006) The Information in Option Volume for
Future Stock Prices. Review of Financial Studies 19(3): 871-908.
Panayiotou, A. and Medda, F.R. (2014) Attracting Private Sector Participa-
tion in Transport Investment. Procedia – Social and Behavioral Sciences 111:
424-431.
Panayiotou, A. and Medda, F. (2016) Portfolio of Infrastructure Investments:
Analysis of European Infrastructure. Journal of Infrastructure Systems 22(3):
04016011.
247
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 249

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Pantalone, C. and Platt, H. (1984) Riding the Yield Curve. Journal of Finan-
cial Education, No. 13, pp. 5-9.
Papageorgiou, N.A., Reeves, J.J. and Sherris, M. (2017) Equity investing
with targeted constant volatility exposure. Working Paper. Available online:
https://ssrn.com/abstract=2614828.
Park, K., Jung, M. and Lee, S. (2018) Credit ratings and convertible bond
prices: a simulation-based valuation. European Journal of Finance 24(12):
1001-1025.
Parnaudeau, M. and Bertrand, J.-L. (2018) The contribution of weather vari-
ability to economic sectors. Applied Economics 50(43): 4632-4649.
Pascalau, R. and Poirier, R. (2015) Bootstrapping the Relative Performance
of Yield Curve Strategies. Journal of Investment Strategies 4(2): 55-81.
Paschke, R. and Prokopczuk, M. (2012) Investing in commodity futures mar-
kets: can pricing models help? European Journal of Finance 18(1): 59-87.
Passmore, W., Sherlund, S.M. and Burgess, G. (2005) The Eﬀect of Hous-
ing Government-Sponsored Enterprises on Mortgage Rates. Real Estate Eco-
nomics 33(3): 427-463.
P´ astor, L’. and Stambaugh, R.F. (2003) Liquidity Risk and Expected Stock
Returns. Journal of Political Economy 111(3): 642-685.
P¨ at¨ ari, E. and Vilska, M. (2014) Performance of moving average trading strate-
gies over varying stock market conditions: the Finnish evidence. Applied Eco-
nomics 46(24): 2851-2872.
Pelaez, R.F. (1997) Riding the yield curve: Term premiums and excess returns.
Review of Financial Economics 6(1): 113-119.
Peng, H.W. and Newell, G. (2007) The Signiﬁcance of Infrastructure in Aus-
tralian Investment Portfolios. Paciﬁc Rim Property Research Journal 13(4):
423-450.
Pennacchi, G.G. (1991) Identifying the Dynamics of Real Interest Rates and
Inﬂation: Evidence Using Survey Data. Review of Financial Studies 4(1): 53-
86.
Pepi´ c, M. (2014) Managing interest rate risk with interest rate futures.
Ekonomika preduze´ ca62(3-4): 201-209.
Perchanok, K. (2012) Futures spreads: theory and praxis (Ph.D. Thesis).
Northampton, UK: The University of Northampton. Available online: http:
//nectar.northampton.ac.uk/4963/1/Perchanok20124963.pdf.
248
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 250

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Perchanok, K. and Kakabadse, N. (2013) Causes of Market Anomalies of Crude
Oil Calendar Spreads: Does Theory of Storage Address the Issue? Problems
and Perspectives in Management 11(2): 35-47.
Perchet, R., de Carvalho, R.L. and Moulin, P. (2014) Intertemporal risk parity:
a constant volatility framework for factor investing. Journal of Investment
Strategies 4(1): 19-41.
Perez-Gonzalez, F. and Yun, H. (2010) Risk Management and Firm Value:
Evidence from Weather Derivatives.Working Paper. Available online: https:
//ssrn.com/abstract=1357385.
Peri´ c, M.R. (2015)Ekonomski aspekti korporativnih bankrotstava i steˇ cajnih
procesa. Belgrade, Serbia: Modern Business School.
Perlin, M.S. (2009) Evaluation of pairs-trading strategy at the Brazilian ﬁnan-
cial market. Journal of Derivatives & Hedge Funds 15(2): 122-136.
Person, J.L. (2007) Candlestick and Pivot Point Trading Triggers. Hoboken,
NJ: John Wiley & Sons, Inc.
Peterson, J.D. and Hsieh, C.-H. (1997) Do Common Risk Factors in the Re-
turns on Stocks and Bonds Explain Returns on REITs?Real Estate Economics
25(2): 321-345.
Petre, G. (2015) A Case for Dynamic Asset Allocation for Long Term Investors.
Procedia Economics and Finance 29: 41-55.
Pﬂueger, C.E. and Viceira, L.M. (2011) Inﬂation-Indexed Bonds and the Ex-
pectations Hypothesis. Annual Review of Financial Economics 3: 139-158.
Philosophov, L.V. and Philosophov, V.L. (2005) Optimization of a ﬁrm’s cap-
ital structure: A quantitative approach based on a probabilistic prognosis of
risk and time of bankruptcy.International Review of Financial Analysis 14(2):
191-209.
Piazzesi, M. and Schneider, M. (2009) Momentum Traders in the Housing
Market: Survey Evidence and a Search Model. American Economic Review
99(2): 406-411.
Picou, G. (1981) Managing Interest Rate Risk with Interest Rate Futures.
Bankers Magazine, Vol. 164, May-June 1981, pp. 76-81.
Pindado, J., Rodrigues, L. and de la Torre, C. (2008) Estimating ﬁnancial
distress likelihood. Journal of Business Research 61(9): 995-1003.
Pindyck, R.S. (2001) The dynamics of commodity spot and futures markets:
a primer. Energy Journal 22(3): 1-30.
249
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 251

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Piotroski, J.D. (2000) Value investing: The use of historical ﬁnancial statement
information to separate winners from losers. Journal of Accounting Research
38: 1-41.
Piotroski, J.D. and So, E.C. (2012) Identifying Expectation Errors in Value/
Glamour Strategies: A Fundamental Analysis Approach. Review of Financial
Studies 25(9): 2841-2875.
Pirrong, C. (2005) Momentum in Futures Markets. Working Paper. Available
online: https://ssrn.com/abstract=671841.
Pirrong, C. (2017) The economics of commodity market manipulation: A
survey. Journal of Commodity Markets 5: 1-17.
Pisani, B. (2010) Man Vs. Machine: How Stock Trading Got So Complex.
CNBC (September 13, 2010). Available online: https://www.cnbc.com/id/
38978686.
Pitts, M. (1985) The Management of Interest Rate Risk: Comment. Journal
of Portfolio Management 11(4): 67-69.
Pivar, W. (2003)Real Estate Investing From A to Z: The Most Comprehensive,
Practical, and Readable Guide to Investing Proﬁtably in Real Estate. New
York, NY: McGraw-Hill, Inc.
Pizzutilo, F. (2013) A note on the eﬀectiveness of pairs trading for individual
investors. International Journal of Economics and Financial Issues 3(3): 763-
771.
Podobnik, B., Horvatic, D., Petersen, A.M., Uroˇ sevi´ c, B. and Stanley, H.E.
(2010) Bankruptcy risk model and empirical tests. Proceedings of the National
Academy of Sciences 107(43): 18325-18330.
Poitras, G. (1990) The distribution of gold futures spreads. Journal of Futures
Markets 10(6): 643-659.
Pole, A. (2007) Statistical arbitrage: algorithmic trading insights and tech-
niques. Hoboken, NJ: John Wiley & Sons, Inc.
Popper, H. (1993) Long-term covered interest parity: evidence from currency
swaps. Journal of International Money and Finance 12(4): 439-448.
Porter, M.F. (1980) An Algorithm for Suﬃx Stripping. Program 14(3): 130-
137.
Poterba, J. (1986) Explaining the yield spread between taxable and tax exempt
bonds. In: Rosen, H. (ed.) Studies in State and Local Public Finance. Chicago,
IL: University of Chicago Press, pp. 5-48.
250
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 252

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Poterba, J. (1989) Tax reform and the market for tax-exempt debt. Regional
Science and Urban Economics 19(3): 537-562.
Poterba, J. and Sinai, T. (2008) Tax Expenditures for Owner-Occupied Hous-
ing: Deductions for Property Taxes and Mortgage Interest and the Exclusion
of Imputed Rental Income. American Economic Review 98(2): 84-89.
Poterba, J.M. and Summers, L.H. (1988) Mean reversion in stock prices: evi-
dence and implications. Journal of Financial Economics 22(1): 27-59.
Potjer, D. and Gould, C. (2007) Global Tactical Asset Allocation: Exploit-
ing the opportunity of relative movements across asset classes and ﬁnancial
markets. London, UK: Risk Books.
Pounds, H. (1978) Covered Call Option Writing Strategies and Results. Jour-
nal of Portfolio Management 4(2): 31-42.
Prince, J.T. (2005) Investing in Collateralized Debt Obligations.CFA Institute
Conference Proceedings2005(1): 52-61.
Pring, M.J. (1985) Technical analysis explained: The successful investor’s
guide to spotting investment trends and turning points. (3rd ed.) New York,
NY: McGraw-Hill, Inc.
Prokopczuk, M. and Simen, C.W. (2014) The importance of the volatility risk
premium for volatility forecasting. Journal of Banking & Finance 40: 303-320.
Putnam, G., III (1991) Investment Opportunities in Distressed Equities. In:
Levine, S. (ed.) Handbook of Turnaround and Bankruptcy Investing.New York,
NY: HarperCollins, pp. 196-207.
Puttonen, V. (1993) The ex ante proﬁtability of index arbitrage in the new
Finnish markets. Scandinavian Journal of Management 9(S1): 117-127.
Quintero, R.G. (1989) Acquiring the Turnaround Candidate. In: Levine, S.
(ed.) The Acquisitions Manual. New York, NY: New York Institute of Finance,
pp. 379-441.
Rad, H., Low, R.K.Y. and Faﬀ, R. (2016) The proﬁtability of pairs trading
strategies: distance, cointegration and copula methods. Quantitative Finance
16(10): 1541-1558.
Rajan, A., McDermott, G. and Roy, R. (eds.) (2007) The Structured Credit
Handbook. Hoboken, NJ: John Wiley & Sons, Inc.
Ramamurti, R. and Doh, J. (2004) Rethinking Foreign Infrastructure Invest-
ment in Developing Countries. Journal of World Business 39(2): 151-167.
251
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 253

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Rao, V.K. (2011) Multiperiod Hedging using Futures: Mean Reversion and
the Optimal Hedging Path. Journal of Risk and Financial Management 4(1):
133-161.
Rao, T. and Srivastava, S. (2012) Analyzing stock market movements using
twitter sentiment analysis. In: Proceedings of the 2012 International Confer-
ence on Advances in Social Networks Analysis and Mining (ASONAM 2012).
Washington, DC: IEEE, pp. 119-123.
Raulji, J.K. and Saini, J.R. (2016) Stop-Word Removal Algorithm and its
Implementation for Sanskrit Language. International Journal of Computer
Applications 150(2): 15-17.
Ready, R., Roussanov, N. and Ward, C. (2017) Commodity Trade and the
Carry Trade: A Tale of Two Countries. Journal of Finance 72(6): 2629-2684.
Reddington, F.M. (1952) Review of the Principles of Life Insurance Valuations.
Journal of the Institute of Actuaries 78(3): 286-340.
Refenes, A.N., Zapranis, A.S. and Francis, G. (1994) Stock Performance Mod-
eling Using Neural Networks: Comparative Study with Regressive Models.
Neural Networks 7(2): 375-388.
Rehring, C. (2012) Real Estate in a Mixed-Asset Portfolio: The Role of the
Investment Horizon. Real Estate Economics 40(1): 65-95.
Reiss, M.F. and Phelps, T.G. (1991) Identifying a Troubled Company.
In: Dinapoli, D., Sigoloﬀ, S.C. and Cushman, R.F. (eds.) Workouts and
Turnarounds: The Handbook of Restructuring and Investing in Distressed
Companies. Homewood, IL: Business One-Irwin, pp. 7-43.
Reitano, R. (1996) Non-parallel yield curve shifts and stochastic immunization.
Journal of Portfolio Management 22(2): 71-78.
Remolona, E.M., Wickens, M.R. and Gong, F.F. (1998) What Was the Mar-
ket’s View of UK Monetary Policy? Estimating Inﬂation Risk and Expected
Inﬂation with Indexed Bonds. Federal Reserve Bank of New York Staﬀ Re-
ports, No. 57. Available online: https://ssrn.com/abstract=937350.
Rendleman, R.J. (1999) Duration-Based Hedging with Treasury Bond Futures.
Journal of Fixed Income 9(1): 84-91.
Rendleman, R.J., Jones, C.P. and Latan´ e, H.A. (1982) Empirical anomalies
based on unexpected earnings and the importance of risk adjustments.Journal
of Financial Economics 10(3): 269-287.
252
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 254

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Reynauld, J. and Tessier, J. (1984) Risk Premiums in Futures Markets: An
Empirical Investigation. Journal of Futures Markets 4(2): 189-211.
Rhee, S.G. and Chang, R.P. (1992) Intra-Day Arbitrage Opportunities in For-
eign Exchange and Eurocurrency Markets. Journal of Finance 47(1): 363-379.
Ribeiro, B., Silva, C., Chen, N., Vieira, A. and das Neves, J.C. (2012) En-
hanced default risk models with SVM+. Expert Systems with Applications
39(11): 10140-10152.
Richard, S.F. and Roll, R. (1989) Prepayments on ﬁxed-rate mortgage-backed
securities. Journal of Portfolio Management 15(3): 73-82.
Richards, T., Manfredo, M. and Sanders, D. (2004) Pricing weather deriva-
tives. American Journal of Agricultural Economics 86(4): 1005-1017.
Richie, N., Daigler, R.T. and Gleason, K.C. (2008) The limits to stock in-
dex arbitrage: Examining S&P 500 futures and SPDRS. Journal of Futures
Markets 28(12): 1182-1205.
Rickards, D. (2008) Global Infrastructure – A Growth Story. In: Davis,
H. (ed.) Infrastructure Finance: Trends and Techniques. London, UK: Eu-
romoney Books, pp. 1-47.
Rime, D., Schrimpf, A. and Syrstad, O. (2017) Segmented Money Markets and
Covered Interest Parity Arbitrage. Working Paper. Available online: https:
//ssrn.com/abstract=2879904.
Riordan, R. and Storkenmaier, A. (2012) Latency, liquidity and price discov-
ery. Journal of Financial Markets 15(4): 416-437.
Rising, J.K. and Wyner, A.J. (2012) Partial Kelly portfolios and shrinkage es-
timators. In: Proceedings of the 2012 International Symposium on Information
Theory (ISIT). Washington, DC: IEEE, pp. 1618-1622.
R¨ odel, M. and Rothballer, C. (2012) Infrastructure as Hedge against Inﬂation
– Fact or Fantasy? Journal of Alternative Investments 15(1): 110-123.
Rodr´ ıguez-Gonz´ alez, A., Garc´ ıa-Crespo,´A., Colomo-Palacios, R., Iglesias,
F.G. and G´ omez-Berb´ ıs, J.M. (2011) CAST: Using neural networks to improve
trading systems based on technical analysis by means of the RSI ﬁnancial in-
dicator. Expert Systems with Applications 38(9): 11489-11500.
Rogers, L.C.G. and Shi, Z. (1995) The Value of an Asian Option. Journal of
Applied Probability 32(4): 1077-1088.
Roll, R. (1996) U.S. Treasury Inﬂation-Indexed Bonds: The Design of a New
Security. Journal of Fixed Income 6(3): 9-28.
253
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 255

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Roll, R. (2004) Empirical TIPS. Financial Analysts Journal 60(1): 31-53.
Roll, R. and Yan, S. (2008) An explanation of the forward premium ‘puzzle’.
European Financial Management 6(2): 121-148.
Rompotis, G.G. (2011a) The performance of actively managed exchange
traded funds. Journal of Index Investing 1(4): 53-65.
Rompotis, G.G. (2011b) Active vs. passive management: New evidence from
exchange traded funds. International Review of Applied Financial Issues and
Economics 3(1): 169-186.
Ronn, A.G. and Ronn, E.I. (1989) The Box Spread Arbitrage Conditions:
Theory, Tests, and Investment Strategies. Review of Financial Studies 2(1):
91-108.
Rosales, E.B. and McMillan, D. (2017) Time-series and cross-sectional momen-
tum and contrarian strategies within the commodity futures markets. Cogent
Economics & Finance 5(1): 1339772.
Rosenberg, H. (1992) Vulture Investors. New York, NY: HarperCollins.
Rosenberg, B., Reid, K. and Lanstein, R. (1985) Persuasive evidence of market
ineﬃciency. Journal of Portfolio Management 11(3): 9-16.
Ross, J. (2006) Exploiting spread trades. Futures Magazine, December 2006,
pp. 34-36.
Ross, S. and Zisler, R. (1991) Risk and return in real estate. Journal of Real
Estate Finance and Economics 4(2): 175-190.
Rothballer, C. and Kaserer, C. (2012) The Risk Proﬁle of Infrastructure In-
vestments: Challenging Conventional Wisdom. Journal of Structured Finance
18(2): 95-109.
Routledge, B., Seppi, D.J. and Spatt, C. (2000) Equilibrium forward curves
for commodities. Journal of Finance 55(3): 1297-1338.
Rouwenhorst, K.G. (1998) International Momentum Strategies. Journal of
Finance 53(1): 267-284.
Roy, O. and Vetterli, M. (2007) The eﬀective rank: A measure of eﬀective
dimensionality. In: Proceedings – EUSIPCO 2007, 15th European Signal Pro-
cessing Conference. Pozna´ n, Poland (September 3-7), pp. 606-610.
Ruan, Y., Durresi, A. and Alfantoukh, L. (2018) Using Twitter trust network
for stock market analysis. Knowledge-Based Systems 145: 207-218.
254
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 256

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Ruchin, A. (2011) Can Securities Lending Transactions Substitute for Repur-
chase Agreement Transactions? Banking Law Journal 128(5): 450-480.
Ruder, S. (2017) An overview of gradient descent optimization algorithms.
Working Paper. Available online:
https://arxiv.org/pdf/1609.04747.pdf.
Rudy, J., Dunis, C. and Laws, J. (2010) Proﬁtable Pair Trading: A Compar-
ison Using the S&P 100 Constituent Stocks and the 100 Most Liquid ETFs.
Working Paper. Available online: https://ssrn.com/abstract=2272791.
Rujivan, S. and Zhu, S.P. (2012) A simpliﬁed analytical approach for pricing
discretely sampled variance swaps with stochastic volatility. Applied Mathe-
matics Letters 25(11): 1644-1650.
Rumelhart, D.E., Hinton, G.E. and Williams, R.J. (1986) Learning represen-
tations by back-propagating errors. Nature 323(6088): 533-536.
Rusn´ akov´ a, M. andˇSolt´ es, V. (2012) Long strangle strategy using barrier
options and its application in hedging. Actual Problems of Economics 134(8):
452-465.
Rusn´ akov´ a, M.,ˇSolt´ es, V. and Szabo, Z.K. (2015) Short Combo Strategy
Using Barrier Options and its Application in Hedging. Procedia Economics
and Finance 32: 166-179.
Ryabkov, N. (2015) Hedge Fund Price Pressure in Convertible Bond Markets.
Working Paper. Available online: https://ssrn.com/abstract=2539929.
Saad, E.W., Prokhorov, D.V. and Wunsch, D.C. (1998) Comparative study
of stock trend prediction using time delay, recurrent and probabilistic neural
networks. IEEE Transactions on Neural Networks 9(6): 1456-1470.
Sack, B. and Elsasser, R. (2004) Treasury Inﬂation-Indexed Debt: A Review
of the U.S. Experience. Federal Reserve Bank of New York, Economic Policy
Review 10(1): 47-63.
Sadka, R. (2002) The Seasonality of Momentum: Analysis of Tradability.
Working Paper. Available online: https://ssrn.com/abstract=306371.
Sagi, J. and Seasholes, M. (2007) Firm-speciﬁc Attributes and the Cross-
section of Momentum. Journal of Financial Economics 84(2): 389-434.
Salcedo, Y. (2004) Spreads for the fall. Futures Magazine, September 2004,
pp. 54-57.
255
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 257

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Saltyte-Benth, J. and Benth, F.E. (2012) A critical view on temperature mod-
elling for application in weather derivatives markets. Energy Economics 34(2):
592-602.
Samuelson, P.A. (1945) The eﬀect of interest rate increases on the banking
system. American Economic Review 35(1): 16-27.
Samuelson, P. (1971) The “fallacy” of maximizing the geometric mean in long
sequences of investing or gambling. Proceedings of the National Academy of
Sciences 68(10): 2493-2496.
Samuelson, W. and Rosenthal, L. (1986) Price Movements as Indicators of
Tender Oﬀer Success. Journal of Finance 41(2): 481-499.
Samworth, R.J. (2012) Optimal weighted nearest neighbour classiﬁers. Annals
of Statistics 40(5): 2733-2763.
Sanchez-Robles, B. (1998) Infrastructure Investment and Growth: Some Em-
pirical Evidence. Contemporary Economic Policy 16(1): 98-108.
Saretto, A. and Goyal, A. (2009) Cross-section of option returns and volatility.
Journal of Financial Economics 94(2): 310-326.
Sassetti, P. and Tani, M. (2006) Dynamic Asset Allocation Using Systematic
Sector Rotation. Journal of Wealth Management 8(4): 59-70.
Satchell, S. and Scowcroft, A. (2000) A demystiﬁcation of the Black-Litterman
model: Managing quantitative and traditional portfolio construction. Journal
of Asset Management 1(2): 138-150.
Savor, P. and Wilson, M. (2013) How Much Do Investors Care About Macroe-
conomic Risk? Evidence from Scheduled Economic Announcements. Journal
of Financial and Quantitative Analysis 48(2): 343-375.
Sawant, R.J. (2010a) Infrastructure Investing: Managing Risks & Rewards for
Pensions, Insurance Companies & Endowments. Hoboken, NJ: John Wiley &
Sons, Inc.
Sawant, R.J. (2010b) Emerging Market Infrastructure Project Bonds: Their
Risks and Returns. Journal of Structured Finance 15(4): 75-83.
Schaede, U. (1990) The introduction of commercial paper – a case study in the
liberalisation of the Japanese ﬁnancial markets. Japan Forum 2(2): 215-234.
Schap, K. (2005) The complete guide to spread trading. New York, NY:
McGraw-Hill, Inc.
256
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 258

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Schatz, H.R. (2012) The Characterization of Repurchase Agreements in the
Context of the Federal Securities Laws. St. John’s Law Review 61(2): 290-310.
Schiereck, D., Bondt, W.D. and Weber, M. (1999) Contrarian and momentum
strategies in Germany. Financial Analysts Journal 55(6): 104-116.
Schiller, F., Seidler, G. and Wimmer, M. (2010) Temperature models for pric-
ing weather derivatives. Quantitative Finance 12(3): 489-500.
Schizas, P. (2014) Active ETFs and their performance vis-` a-vis passive ETFs,
mutual funds, and hedge funds. Journal of Wealth Management 17(3): 84-98.
Schizas, P., Thomakos, D.D. and Wang, T. (2011) Pairs Trading on In-
ternational ETFs. Working Paper. Available online: https://ssrn.com/
abstract=1958546.
Schmidhuber, J. (2015) Deep learning in neural networks: An overview.Neural
Networks 61: 85-117.
Schmidt, W. and Ward, I. (2002) Pricing default baskets. Risk, January 2002,
pp. 111-114.
Schneeweis, T. and Gupta, R. (2006) Diversiﬁcation beneﬁts of managed fu-
tures. Journal of Investment Consulting 8(1): 53-62.
Schneider, F. and Windischbauer, U. (2008) Money laundering: some facts.
European Journal of Law and Economics 26(3): 387-404.
Scholes, M. and Williams, J. (1977) Estimating Betas from Nonsynchronous
Data. Journal of Financial Economics 5(3): 309-327.
Sch¨ onbucher, P.J. (2003)Credit Derivatives Pricing Models. Hoboken, NJ:
John Wiley & Sons, Inc.
Schoutens, W. (2005) Moment swaps. Quantitative Finance 5(6): 525-530.
Schultz, G.M. (2016) Investing in Mortgage-Backed and Asset-Backed Securi-
ties: Financial Modeling with R and Open Source Analytics + Website. Hobo-
ken, NJ: John Wiley & Sons, Inc.
Schumaker, R.P. and Chen, H. (2010) A Discrete Stock Price Prediction En-
gine Based on Financial News. Computer 43(1): 51-56.
Schwartz, E.S. (1997) The Stochastic Behavior of Commodity Prices: Impli-
cations for Valuation and Hedging. Journal of Finance 52(3): 923-973.
Schwartz, E.S. (1998) Valuing long-term commodity assets. Journal of Energy
Finance & Development 3(2): 85-99.
257
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 259

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Schwartz, T.V. and Laatsch, F. (1991) Price Discovery and Risk Transfer in
Stock Index Cash and Futures Markets. Journal of Futures Markets 11(6):
669-683.
Schwartz, E.S. and Smith, J.E. (2000) Short-term variations and long-term
dynamics in commodity prices. Management Science 46(7): 893-911.
Schwartz, E.S. and Torous, W.N. (1989) Prepayment and the Valuation of
Mortgage-Backed Securities. Journal of Finance 44(2): 375-392.
Schwartz, E.S. and Torous, W.N. (1992) Prepayment, Default, and the Valua-
tion of Mortgage Pass-through Securities. Journal of Business 65(2): 221-239.
Schwert, G.W. (2003) Anomalies and market eﬃciency. In: Constantinides,
G.M., Harris, M. and Stulz, R.M. (eds.) Handbook of the Economics of Fi-
nance, Vol 1B. (1st ed.) Amsterdam, The Netherlands: Elsevier, Chapter 15,
pp. 939-974.
Sefton, J.A. and Scowcroft, A. (2005) Understanding Momentum. Financial
Analysts Journal 61(2): 64-82.
Seiler, M.J., Webb, J.R. and Myer, F.C.N. (1999) Diversiﬁcation Issues in
Real Estate Investment. Journal of Real Estate Literature 7(2): 163-179.
Sepp¨ al¨ a, J. (2004) The term structure of real interest rates: theory and ev-
idence from UK index-linked bonds. Journal of Monetary Economics 51(7):
1509-1549.
Serban, A.F. (2010) Combining mean reversion and momentum trading strate-
gies in foreign exchange markets. Journal of Banking & Finance 34(11): 2720-
2727.
Seymour, B. (2008) Global Money Laundering. Journal of Applied Security
Research 3(3-4): 373-387.
Sezer, O.B., Ozbayoglu, M. and Dogdu, E. (2017) A Deep Neural-Network
Based Stock Trading System Based on Evolutionary Optimized Technical
Analysis Parameters. Procedia Computer Science 114: 473-480.
Shackman, J.D. and Tenney, G. (2006) The Eﬀects of Government Regulations
on the Supply of Pawn Loans: Evidence from 51 Jurisdictions in the US.
Journal of Financial Services Research 30(1): 69-91.
Shah, A. (2017) Hedging of a Portfolio of Rainfall Insurances using Rainfall
Bonds and European Call Options (Bull Spread). Working Paper. Available
online: https://ssrn.com/abstract=2778647.
258
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 260

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Shah, D. and Zhang, K. (2014) Bayesian regression and Bitcoin. Working
Paper. Available online: https://arxiv.org/pdf/1410.1231.pdf.
Shaikh, I. and Padhi, P. (2015) The implied volatility index: Is ‘ investor fear
gauge’ or ‘forward-looking’? Borsa Istanbul Review 15(1): 44-52.
Shan, L., Garvin, M.J. and Kumar, R. (2010) Collar options to manage rev-
enue risks in real toll public-private partnership transportation projects. Con-
struction Management and Economics 28(10): 1057-1069.
Sharpe, W.F. (1966) Mutual Fund Performance. Journal of Business 39(1):
119-138.
Sharpe, W.F. (1994) The Sharpe Ratio. Journal of Portfolio Management
21(1): 49-58.
Sharpe, W.F. (2009) Adaptive Asset Allocation Policies. Financial Analysts
Journal 66(3): 45-59.
Sharpe, W.F. and Perold, A.F. (1988) Dynamic Strategies for Asset Alloca-
tion. Financial Analysts Journal 44(1): 16-27.
Shaviro, D. (2002) Dynamic Strategies for Asset Allocation. Chicago Journal
of International Law 3(2): 317-331.
Shen, P. (2006) Liquidity Risk Premia and Breakeven Inﬂation Rates. Federal
Reserve Bank of Kansas City, Economic Review 91(2): 29-54.
Shen, P. and Corning, J. (2001) Can TIPS Help Identify Long-Term Inﬂation
Expectations? Federal Reserve Bank of Kansas City, Economic Review 86(4):
61-87.
Sher, G. (2014) Cashing in for Growth: Corporate Cash Holdings as an Op-
portunity for Investment in Japan. Working Paper. Available online: https:
//ssrn.com/abstract=2561246.
Sherrill, D.E. and Upton, K. (2018) Actively managed ETFs vs actively man-
aged mutual funds. Managerial Finance 44(3): 303-325.
Shi, H.-L., Jiang, Z.-Q. and Zhou, W.-X. (2015) Proﬁtability of Contrarian
Strategies in the Chinese Stock Market. PLoS ONE 10(9): e0137892.
Shiller, R.J. (1979) The Volatility of Long-Term Interest Rates and Expec-
tations Models of the Term Structure. Journal of Political Economy 87(6):
1190-1219.
259
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 261

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Shiller, R.J. and Modigliani, F. (1979) Coupon and tax eﬀects on new and
seasoned bond yields and the measurement of the cost of debt capital. Journal
of Financial Economics 7(3): 297-318.
Shimko, D.C. (1994) Options on futures spreads: Hedging, speculation, and
valuation. Journal of Futures Markets 14(2): 183-213.
Shin, K. and Lee, Y. (2002) A genetic algorithm application in bankruptcy
prediction modeling. Expert Systems with Applications 23(3): 321-328.
Shiu, E.S.W. (1987) On the Fisher-Weil immunization theorem. Insurance:
Mathematics and Economics 6(4): 259-266.
Shiu, E.S.W. (1988) Immunization of multiple liabilities. Insurance: Mathe-
matics and Economics 7(4): 219-224.
Shiu, Y.-M. and Lu, T.-H. (2011) Pinpoint and Synergistic Trading Strategies
of Candlesticks. International Journal of Economics and Finance 3(1): 234-
244.
Shum, P., Hejazi, W., Haryanto, E. and Rodier, A. (2016) Intraday Share
Price Volatility and Leveraged ETF Rebalancing. Review of Finance 20(6):
2379-2409.
Shumway, T. (2001) Forecasting Bankruptcy More Accurately: A Simple Haz-
ard Model. Journal of Business 74(1): 101-104.
Siganos, A. and Chelley-Steeley, P. (2006) Momentum Proﬁts Following Bull
and Bear Markets. Journal of Asset Management 6(5): 381-388.
Sill, K. (1996) The Cyclical Volatility of Interest Rates. Business Review of
the Federal Reserve Bank of Philadelphia , January/February 1996, pp. 15-29.
Simmons, E. (1954) Sales of Government Securities to Federal Reserve Banks
Under Repurchase Agreements. Journal of Finance 9(1): 23-40.
Simon, D.P. and Campasano, J. (2014) The VIX Futures Basis: Evidence and
Trading Strategies. Journal of Derivatives 21(3): 54-69.
Simpson, M.W. and Grossman, A. (2016) The Role of Industry Eﬀects in
Simultaneous Reversal and Momentum Patterns in One-Month Stock Returns.
Journal of Behavioral Finance 17(4): 309-320.
Simutin, M. (2014) Cash Holdings and Mutual Fund Performance. Review of
Finance 18(4): 1425-1464.
260
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 262

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Sing, T.-F. and Low, S.-H.Y. (2000) The inﬂation-hedging characteristics of
real estate and ﬁnancial assets in Singapore. Journal of Real Estate Portfolio
Management 6(4): 373-386.
Singh, Y. and Chandra, P. (2003) A class +1 sigmoidal activation functions
for FFANNs. Journal of Economic Dynamics and Control 28(1): 183-187.
Singhal, S., Newell, G. and Nguyen, T.K. (2011) The signiﬁcance and perfor-
mance of infrastructure in India. Journal of Property Research 28(1): 15-34.
Siriopoulos, C. and Fassas, A. (2009) Implied Volatility Indices – A Review.
Working Paper. Available online: https://ssrn.com/abstract=1421202.
Skelton, J.L. (1983) Banks, ﬁrms and the relative pricing of tax-exempt and
taxable bonds. Journal of Financial Economics 12(3): 343-355.
Skiadopoulos, G. (2004) The Greek implied volatility index: construction and
properties. Applied Financial Economics 14(16): 1187-1196.
Skiadopoulos, G., Hodges, S. and Clewlow, L. (1999) The Dynamics of the
S&P 500 Implied Volatility Surface. Review of Derivatives Research 3(3): 263-
282.
Slowinski, R. and Zopounidis, C. (1995) Application of the rough set approach
to evaluation of bankruptcy risk. Intelligent Systems in Accounting, Finance
and Management 4(1): 27-41.
Smit, H.T.J. and Trigeorgis, L. (2009) Valuing infrastructure investment: An
option games approach. California Management Review 51(2): 82-104.
Smith, D.M. and Pantilei, V.S. (2015) Do “Dogs of the World” Bark or Bite?
Evidence from Single-Country ETFs. Journal of Investing 24(1): 7-15.
Smith, K.V. and Shulman, D. (1976) Institutions Beware: The Performance
of Equity Real Estate Investment Trusts. Financial Analysts Journal 32(5):
61-66.
Sollinger, A. (1994) The Triparty Is Just Beginning. Institutional Investor
28(1): 133-135.
ˇSolt´ es, M. (2010) Relationship of speed certiﬁcates and inverse vertical ratio
call back spread option strategy. E+M Ekonomie a Management 13(2): 119-
124.
ˇSolt´ es, V. (2011) The application of the long and short combo option strategies
in the building of structured products. In: Kocourek, A. (ed.) Proceedings of
the 10th International Conference: Liberec Economic Forum 2011 . Liberec,
Czech Republic: Technical University of Liberec, pp. 481-487.
261
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 263

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ˇSolt´ es, V. and Amaitiek, O.F.S. (2010a) The Short Put Ladder Strategy and its
Application in Trading and Hedging. Club of Economics in Miskolc: Theory,
Methodology, Practice 6(2): 77-85.
ˇSolt´ es, V. and Amaitiek, O.F.S. (2010b) Inverse Vertical Ratio Put Spread
Strategy and its Application in Hedging against a Price Drop. Journal of
Advanced Studies in Finance 1(1): 100-107.
ˇSolt´ es, V. and Rusn´ akov´ a, M. (2012) Long Combo strategy using barrier op-
tions and its application in hedging against a price drop. Acta Montanistica
Slovaca 17(1): 17-32.
ˇSolt´ es, V. and Rusn´ akov´ a, M. (2013) Hedging Against a Price Drop Using
the Inverse Vertical Ratio Put Spread Strategy Formed by Barrier Options.
Engineering Economics 24(1): 18-27.
Sørensen, C. (1999) Dynamic Asset Allocation and Fixed Income Manage-
ment. Journal of Financial and Quantitative Analysis 34(4): 513-531.
Sorensen, E.H. and Burke, T. (1986) Portfolio Returns from Active Industry
Group Rotation. Financial Analysts Journal 42(5): 43-50.
Sørensen, C. and Trolle, A.B. (2005) A General Model of Dynamic Asset Al-
location with Incomplete Information and Learning. Working paper. Available
online: https://ssrn.com/abstract=675625.
S¨ orensson, T. (1993) Two methods for valuing convertible bonds – A compar-
ison. Scandinavian Journal of Management 9(S1): 129-139.
Soudijn, M.R.J. (2016) Rethinking money laundering and drug traﬃcking:
Some implications for investigators, policy makers and researchers. Journal of
Money Laundering Control 19(3): 298-310.
Sprenger, T.O., Tumasjan, A., Sandner, P.G. and Welpe, I.M. (2014) Tweets
and trades: The information content of stock microblogs. European Financial
Management 20(5): 926-957.
Spyrou, S.I. (2005) Index Futures Trading and Spot Price Volatility: Evidence
from an Emerging Market.Journal of Emerging Market Finance 4(2): 151-167.
Staal, A., Corsi, M., Shores, S. and Woida, C. (2015) A Factor Approach to
Smart Beta Development in Fixed Income. Journal of Index Investing 6(1):
98-110.
Stambaugh, R.F. (1988) The information in forward rates: Implications for
models of the term structure. Journal of Financial Economics 21(1): 41-70.
262
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 264

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Stanton, R. (1995) Rational Prepayment and the Valuation of Mortgage-
Backed Securities. Review of Financial Studies 8(3): 677-708.
Statman, M., Thorley, S. and Vorkink, K. (2006) Investor Overconﬁdence and
Trading Volume. Review of Financial Studies 19(4): 1531-1565.
Stattman, D. (1980) Book Values and Stock Returns. Chicago MBA: A Jour-
nal of Selected Papers 1980(4): 25-45.
Stefanini, F. (2006) Investment Strategies of Hedge Funds. Chichester, UK:
John Wiley & Sons, Ltd.
Stein, J.C. (1992) Convertible bonds as backdoor equity ﬁnancing. Journal of
Financial Economics 32(1): 3-21.
Stein, J.C. (1995) Prices and Trading Volume in the Housing Market: A Model
with Down-Payment Eﬀects.Quarterly Journal of Economics 110(2): 379-406.
Steinert, M. and Crowe, S. (2001) Global Real Estate Investment: Character-
istics, Optimal Portfolio Allocation and Future Trends. Paciﬁc Rim Property
Research Journal 7(4): 223-239.
Stevenson, S. (2001) Bayes-Stein Estimators and International Real Estate
Asset Allocation. Journal of Real Estate Research 21(1/2): 89-104.
Stevenson, S. (2002) Momentum Eﬀects and Mean Reversion in Real Estate
Securities. Journal of Real Estate Research 23(1/2): 47-64.
Stickel, S.E. (1991) Common stock returns surrounding earnings forecast re-
visions: More puzzling evidence. Accounting Review 66(2): 402-416.
Stivers, C. and Sun, L. (2010) Cross-Sectional Return Dispersion and Time
Variation in Value and Momentum Premiums.Journal of Financial and Quan-
titative Analysis 45(4): 987-1014.
Stoll, H.R. (1969) The Relationship Between Put and Call Option Prices.
Journal of Finance 24(5): 801-824.
Stotz, O. (2016) Investment strategies and macroeconomic news announce-
ment days. Journal of Asset Management 17(1): 45-56.
Stovall, S. (1996) Sector Investing. New York, NY: McGraw Hill, Inc.
Stroebel, J. and Taylor, J.B. (2012) Estimated Impact of the Federal Reserve’s
Mortgage-Backed Securities Purchase Program. International Journal of Cen-
tral Banking 8(2): 1-42.
263
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 265

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
St¨ ubinger, J. and Bredthauer, J. (2017) Statistical Arbitrage Pairs Trading
with High-frequency Data. International Journal of Economics and Financial
Issues 7(4): 650-662.
St¨ ubinger, J. and Endres, S. (2017) Pairs trading with a mean-reverting jump-
diﬀusion model on high-frequency data. Quantitative Finance (forthcoming).
DOI: https://doi.org/10.1080/14697688.2017.1417624.
Stulz, R.M. (1996) Rethinking risk management. Journal of Applied Corporate
Finance 9(3): 8-25.
Stulz, R.M. (2010) Credit Default Swaps and the Credit Crisis. Journal of
Economic Perspectives 24(1): 73-92.
Su, X. (2006) Hedging basket options by using a subset of underlying assets.
Working paper. Available online: https://www.econstor.eu/bitstream/
10419/22959/1/bgse14_2006.pdf.
Su, E. and Knowles, T.W. (2010) Measuring Bond Portfolio Value at Risk and
Expected Shortfall in US Treasury Market. Asia Paciﬁc Management Review
15(4): 477-501.
Subha, M. and Nambi, S. (2012) Classiﬁcation of stock index movement using
k-Nearest Neighbours (k-NN) algorithm. WSEAS Transactions on Informa-
tion Science and Applications 9(9): 261-270.
Subramanian, A. (2004) Option pricing on stocks in mergers and acquisitions.
Journal of Finance 59(2): 795-829.
Suhonen, A., Lennkh, M. and Perez, F. (2017) Quantifying Backtest Overﬁt-
ting in Alternative Beta Strategies. Journal of Portfolio Management 43(2):
90-104.
Sul, H.K., Dennis, A.R. and Yuan, L.(I). (2017) Trading on Twitter: Using
Social Media Sentiment to Predict Stock Returns. Decision Sciences 48(3):
454-488.
Sullivan, R., Timmermann, A. and White, H. (1999) Data-snooping, technical
trading rule performance, and the bootstrap. Journal of Finance 54(5): 1647-
1691.
Summers, B.J. (1980) Negotiable Certiﬁcates of Deposit.Federal Reserve Bank
of Richmond, Economic Review 66(4): 8-19.
Suresh, A.S. (2015) Analysis of Option Combination Strategies. Management
Insight 11(1): 31-40.
264
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 266

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Svec, J. and Stevenson, M. (2007) Modelling and forecasting temperature
based weather derivatives. Global Finance Journal 18(2): 185-204.
Swank, T.A. and Root, T.H. (1995) Bonds in Default: Is Patience a Virtue?
Journal of Fixed Income 5(1): 26-31.
Swinkels, L. (2002) International Industry Momentum. Journal of Asset Man-
agement 3(2): 124-141.
Swishchuk, A. and Cui, K. (2013) Weather derivatives with applications to
Canadian data. Journal of Mathematical Finance 3(1): 81-95.
Switzer, L.N. and Jiang, H. (2010) Market Eﬃciency and the Risks and Re-
turns of Dynamic Trading Strategies with Commodity Futures. In: Stanley,
H.E. (ed.) Proceedings Of The First Interdisciplinary Chess Interactions Con-
ference. Singapore: World Scientiﬁc Publishing, pp. 127-156.
Symeonidis, L., Prokopczuk, M., Brooks, C. and Lazar, E. (2012) Futures ba-
sis, inventory and commodity price volatility: An empirical analysis.Economic
Modelling 29(6): 2651-2663.
Szado, E. and Schneeweis, T. (2010) Loosening Your Collar: Alternative Im-
plementations of QQQ Collars. Journal of Trading 5(2): 35-56.
Szado, E. and Schneeweis, T. (2011) An Update of ‘Loosening Your Collar: Al-
ternative Implementations of QQQ Collars’: Credit Crisis and Out-of-Sample
Performance. Working Paper. Available online: http://ssrn.com/abstract=
1507991.
Szakmary, A.C., Shen, Q. and Sharma, S.C. (2010) Trend-following trading
strategies in commodity futures: A re-examination. Journal of Banking &
Finance 34(2): 409-426.
Szakmary, A.C. and Zhou, X. (2015) Industry momentum in an earlier time:
Evidence from the Cowles data. Journal of Financial Research 38(3): 319-347.
Tang, C.H. and Jang, S.H. (2011) Weather risk management in ski resorts:
Financial hedging and Geographical diversiﬁcation. International Journal of
Hospitality Management 30(2): 301-311
Tang, H. and Xu, X.E. (2013) Solving the Return Deviation Conundrum of
Leveraged Exchange-Traded Funds. Journal of Financial and Quantitative
Analysis 48(1): 309-342.
Tavakoli, J.M. (1998) Credit Derivatives & Synthetic Structures: A Guide to
Instruments and Applications. (2nd ed.) Hoboken, NJ: John Wiley & Sons,
Inc.
265
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 267

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Tay, F.E.H. and Cao, L. (2001) Application of support vector machines in
ﬁnancial time series forecasting. Omega 29(4): 309-317.
Taylor, C.R. (1999) Time-on-the-Market as a Sign of Quality. Review of Eco-
nomic Studies 66(3): 555-578.
Taylor, N. (2004) Modeling discontinuous periodic conditional volatility: Evi-
dence from the commodity futures market. Journal of Futures Markets 24(9):
805-834.
Taylor, N. (2016) Roll strategy eﬃciency in commodity futures markets. Jour-
nal of Commodity Markets 1(1): 14-34.
Taylor, M.P. and Allen, H. (1992) The use of technical analysis in the foreign
exchange market. Journal of International Money and Finance 11(3): 304-314.
Teixeira, L.A. and de Oliveira, A.L.I. (2010) A method for automatic stock
trading combining technical analysis and nearest neighbor classiﬁcation. Ex-
pert Systems with Applications 37(10): 6885-6890.
Telser, L.G. (1958) Futures Trading and the Storage of Cotton and Wheat.
Journal of Political Economy 66(3): 233-255.
The Options Institute (1995) Options: Essential Concepts and Trading Strate-
gies. (2nd ed.) Chicago, IL: Richard D. Irwin, Inc.
Thibodeau, T.G. and Giliberto, S.M. (1989) Modeling Conventional Residen-
tial Mortgage Reﬁnancing. Journal of Real Estate Finance and Economics
2(4): 285-299.
Thomsett, M.C. (2003) Support and Resistance Simpliﬁed. Columbia, MD:
Marketplace Books.
Thornes, J.E. (2006) An introduction to weather and climate derivatives.
Weather 58(5): 193-196.
Thorp, E.O. (2006) The Kelly criterion in blackjack, sports betting, and the
stock market. In: Zenios, S.A. and Ziemba, W.T. (eds.) Handbook of Asset
and Liability Management: Theory and Methodology (Vol. 1). Amsterdam,
The Netherlands: Elsevier, pp. 385-428.
Thorp, E.O. and Kassouf, S.T. (1967) Beat the Market: A Scientiﬁc Stock
Market System. New York, NY: Random House.
Till, H. (2008) Case Studies and Risk Management Lessons in Commodity
Derivatives Trading. In: Geman, H. (ed.) Risk Management in Commodity
Markets: From Shipping to Agriculturals and Energy. Chichester, UK: John
Wiley & Sons, Ltd., pp. 255-291.
266
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 268

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Till, H. and Eagleeye, J. (2017) Commodity Futures Trading Strategies:
Trend-Following and Calendar Spreads. Working Paper. Available online:
https://ssrn.com/abstract=2942340.
Tille, C., Stoﬀels, N. and Gorbachev, O. (2001) To What Extent Does Pro-
ductivity Drive the Dollar? Current Issues in Economics and Finance 7(8):
1-6.
Timmermans, S.H.J.T., Schumacher, J.M. and Ponds, E.H.M. (2017) A multi-
objective decision framework for lifecycle investment. Working Paper. Avail-
able online: http://ssrn.com/abstract=3038803.
Tinoco, M.H. and Wilson, N. (2013) Financial distress and bankruptcy pre-
diction among listed companies using accounting, market and macroeconomic
variables. International Review of Financial Analysis 30: 394-419.
Titman, S. and Warga, A. (1986) Risk and the Performance of Real Estate
Investment Trusts: A Multiple Index Approach.AREUEA Journal 14(3): 414-
431.
Todorov, V. (2010) Variance Risk-Premium Dynamics: The Role of Jumps.
Review of Financial Studies 23(1): 345-383.
Toevs, A. and Jacob, D. (1986) Futures and Alternative Hedge Ratio Method-
ologies. Journal of Portfolio Management 12(3): 60-70.
Tokic, D. (2013) Crude oil futures markets: Another look into traders’ posi-
tions. Journal of Derivatives & Hedge Funds 19(4): 321-342.
Topaloglou, N., Vladimirou, H. and Zenios, S.A. (2011) Optimizing Interna-
tional Portfolios with Options and Forwards. Journal of Banking & Finance
35(12): 3188-3201.
Torrance, M.I. (2007) The Power of Governance in Financial Relationships:
Governing Tensions in Exotic Infrastructure Territory. Growth and Change
38(4): 671-695.
Torricelli, L. (2018) Volatility Targeting Using Delayed Diﬀusions. Working
Paper. Available online: https://ssrn.com/abstract=2902063.
Trainer, F.H., Jr. (1983) The Uses of Treasury Bond Futures in Fixed Income
Portfolio Management. Financial Analysts Journal 39(1): 27-34.
Trainor, W.J., Jr. (2010) Do Leveraged ETFs Increase Volatility? Technology
and Investment 1(3): 215-220.
267
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 269

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Trehan, B. (2005) Oil price shocks and inﬂation. Federal Reserve Bank of San
Francisco, Economic Letter , No. 2005-28. Available online: https://www.
frbsf.org/economic-research/files/el2005-28.pdf.
Trifonov, Y., Yashin, S., Koshelev, E. and Podshibyakin, D. (2011) Application
of Synthetic Straddles for Equity Risk Management. In: ˇCern´ ak, Z. (ed.)
Materi´ aly VII mezin´ arodn´ ı vˇ edecko – praktick´ a konference “Zpr´ avy vˇ edeck´ e
ideje – 2011”. Prague, Czech Republic: Education and Science.
Trifonov, Y., Yashin, S., Koshelev, E. and Podshibyakin, D. (2014) Testing the
Technology of Synthetic Straddles. Working Paper. Available online: https:
//ssrn.com/abstract=2429657.
Tripathi, V. and Garg, S. (2016) A Cross-Country Analysis of Pricing Eﬃ-
ciency of Exchange Traded Funds. Journal of Applied Finance 22(3): 41-63.
Trzcinka, C. (1982) The Pricing of Tax-Exempt Bonds and the Miller Hypoth-
esis. Journal of Finance 37(4): 907-923.
Tsai, C.F. and Hsiao, Y.C. (2010) Combining multiple feature selection
methods for stock prediction: Union, intersection, and multi-intersection ap-
proaches. Decision Support Systems 50(1): 258-269.
Tsai, C., Hsu, Y. and Yen, D.C. (2014) A comparative study of classiﬁer
ensembles for bankruptcy prediction. Applied Soft Computing 24: 977-984.
Tse, Y. (2017) Return predictability and contrarian proﬁts of international
index futures. Journal of Futures Markets 38(7): 788-803.
Tsiveriotis, K. and Fernandes, C. (1998) Valuing convertible bonds with credit
risk. Journal of Fixed Income 8(2): 95-102.
Tuckman, B. and Serrat, A. (2012) Fixed Income Securities: Tools for Today’s
Markets. (3rd ed.) Hoboken, NJ: John Wiley & Sons, Inc.
Tulchinsky, I.et al. (2015) Finding Alphas: A Quantitative Approach to Build-
ing Trading Strategies. New York, NY: John Wiley & Sons, Inc.
Turnovsky, S.J. (1989) The Term Structure of Interest Rates and the Eﬀects of
Macroeconomic Policy. Journal of Money, Credit and Banking 21(3): 321-347.
Tuzun, T. (2013) Are Leveraged and Inverse ETFs the New Portfolio Insur-
ers? Finance and Economics Discussion Series (FEDS) , Paper No. 2013-48.
Washington, DC: Board of Governors of the Federal Reserve System. Avail-
able online: https://www.federalreserve.gov/pubs/feds/2013/201348/
201348pap.pdf.
268
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 270

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Tversky, A. and Kahneman, D. (1992) Advances in prospect theory: Cumu-
lative representation of uncertainty. Journal of Risk and Uncertainty 5(4):
297-323.
Uhlenbeck, G.E. and Ornstein, L.S. (1930) On the Theory of the Brownian
Motion. Physical Review 36(5): 823-841.
Vaitonis, M. and Masteika, S. (2016) Research in high frequency trading and
pairs selection algorithm with Baltic region stocks. In: Dregvaite, G. and
Damasevicius, R. (eds.) Proceedings of the 22nd International Conference on
Information and Software Technologies (ICIST 2016). Cham, Switzerland:
Springer, pp. 208-217.
Van Alstyne, M. (2014) Why Bitcoin has value. Communications of the ACM
57(5): 30-32.
van den Goorbergh, R.W.J. (2004) Essays on optimal hedging and investment
strategies and on derivative pricing (Ph.D. Thesis). Tilburg, The Netherlands:
Tilburg University.
van den Noord, P. and Andr´ e, C. (2007) Why has Core Inﬂation Remained
so Muted in the Face of the Oil Shock? Working Paper. Available online:
http://dx.doi.org/10.1787/206408110285.
Van Kervel, V. and Menkveld, A.J. (2017) High-Frequency Trading around
Large Institutional Orders. Journal of Finance (forthcoming). Available on-
line: https://ssrn.com/abstract=2619686.
van Marle, M. and Verwijmeren, P. (2017) The long and the short of con-
vertible arbitrage: An empirical examination of arbitrageurs’ holding periods.
Journal of Empirical Finance 44: 237-249.
Van Oord, J.A. (2016) Essays on Momentum Strategies in Finance (Ph.D.
Thesis). Rotterdam, The Netherlands: Erasmus University. Available online:
https://repub.eur.nl/pub/80036/EPS2016380F-A9789058924445.pdf.
Vanstone, B. and Finnie, G. (2009) An empirical methodology for developing
stockmarket trading systems using artiﬁcial neural networks. Expert Systems
with Applications 36(3): 6668-6680.
Van Tassel, P. (2016) Merger Options and Risk Arbitrage. Federal Reserve
Bank of New York Staﬀ Reports , No. 761. Available online:
https://www.newyorkfed.org/medialibrary/media/research/staff_
reports/sr761.pdf?la=en.
269
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 271

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Vasicek, O.A. (2015) Probability of Loss on Loan Portfolio. In: Vasicek, O.A.
(ed.) Finance, Economics and Mathematics. Hoboken, NJ: John Wiley & Sons,
Inc., Chapter 17.
Vassalou, M. and Xing, Y. (2004) Default Risk in Equity Returns. Journal of
Finance 59(2): 831-868.
Vedenov, D.V. and Barnett, B.J. (2004) Eﬃciency of Weather Derivatives
as Primary Crop Insurance Instruments. Journal of Agricultural Economics
29(3): 387-403.
Vickery, J. and Wright, J. (2010) TBA Trading and Liquidity in the
Agency MBS Market. Federal Reserve Bank of New York Staﬀ Reports , No.
468. Available online: https://www.newyorkfed.org/medialibrary/media/
research/staff_reports/sr468.pdf.
Vidyamurthy, G. (2004) Pairs Trading: Quantitative Methods and Analysis.
Hoboken, NJ: John Wiley & Sons, Inc.
Viezer, T.W. (2000) Evaluating “Within Real Estate” Diversiﬁcation Strate-
gies. Journal of Real Estate Portfolio Management 6(1): 75-95.
Villani, R. and Davis, C. (2006) FLIP: How to ﬁnd, ﬁx, and sell houses for
proﬁt. New York, NY: McGraw-Hill, Inc.
Vipul (2009) Box-spread arbitrage eﬃciency of Nifty index options: The Indian
evidence. Journal of Futures Markets 29(6): 544-562.
Viswanath, P.V. (1993) Eﬃcient Use of Information, Convergence Adjust-
ments, and Regression Estimates of Hedge Ratios. Journal of Futures Markets
13(1): 43-53.
Vives, A. (1999) Pension Funds in Infrastructure Project Finance: Regulations
and Instrument Design. Journal of Structured Finance 5(2): 37-52.
Volpert, B.S. (1991) Opportunities for Investing in Troubled Companies.
In: Dinapoli, D., Sigoloﬀ, S.C. and Cushman, R.F. (eds.) Workouts and
Turnarounds: The Handbook of Restructuring and Investing in Distressed
Companies. Homewood, IL: Business One-Irwin, pp. 514-542.
Vrugt, E.B., Bauer, R., Molenaar, R. and Steenkamp, T. (2007) Dynamic
commodity trading strategies. In: Till, H. and Eagleeye, J. (eds.) Intelligent
Commodity Investing: New Strategies and Practical Insights for Informed De-
cision Making. London, UK: Risk Books, Chapter 16.
Walker, J. (1999) How Big is Global Money Laundering? Journal of Money
Laundering Control 3(1): 25-37.
270
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 272

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Walker, M.B. (2008) The static hedging of CDO tranche correlation risk. In-
ternational Journal of Computer Mathematics 86(6): 940-954.
Walkling, R.A. (1985) Predicting tender oﬀer success: A logistic analysis.
Journal of Financial and Quantitative Analysis 20(4): 461-478.
Wang, K.Q. (2005) Multifactor Evaluation of Style Rotation. Journal of Fi-
nancial and Quantitative Analysis 40(2): 349-372.
Wang, L. (2014) Margin-Based Asset Pricing and the Determinants of the
CDS Basis. Journal of Fixed Income 24(2): 61-78.
Wang, J., Brooks, R., Lu, X. and Holzhauer, H.M. (2017) Sector Momentum.
Journal of Investing 26(2): 48-60.
Wang, C.-H. and Min, K.J. (2013) Electric Power Plant Valuation Based on
Day-Ahead Spark Spreads. Engineering Economist 58(3): 157-178.
Wang, S. and Vergne, J.-P. (2017) Buzz factor or innovation potential: What
explains cryptocurrencies returns? PLoS ONE 12(1): e0169556.
Wang, C. and Yu, M. (2004) Trading activity and price reversals in futures
markets. Journal of Banking & Finance 28(6): 1337-1361.
Ward, D. and Griepentrog, G. (1993) Risk and Return in Defaulted Bonds.
Financial Analysts Journal 49(3): 61-65.
Watts, R.L. (1978) Systematic ‘abnormal’ returns after quarterly earnings
announcements. Journal of Financial Economics 6(2-3): 127-150.
Webb, J.R., Curcio, R.J. and Rubens, J.H. (1988) Diversiﬁcation gains from
including real estate in mixed-asset portfolios. Decision Sciences 19(2): 434-
452.
Weber, B.R., Adair, A. and McGreal, S. (2008) Solutions to the ﬁve key brown-
ﬁeld valuation problems. Journal of Property Investment & Finance 26(1):
8-37.
Weber, B., Staub-Bisang, M. and Alfen, H.W. (2016) Infrastructure as an
Asset Class: Investment Strategy, Sustainability, Project Finance and PPP.
Chichester, UK: John Wiley & Sons, Ltd.
Weinert, H.L. (2007) Eﬃcient computation for Whittaker-Henderson smooth-
ing. Computational Statistics & Data Analysis 52(2): 959-974.
Weiser, S. (2003) The strategic case for commodities in portfolio diversiﬁca-
tion. Commodities Now, September 2003, pp. 7-11.
271
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 273

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Weller, P.A., Friesen, G.C. and Dunham, L.M. (2009) Price trends and pat-
terns in technical analysis: a theoretical and empirical examination. Journal
of Banking & Finance 6(33): 1089-1100.
Wells, B. (2016) The Foreign Tax Credit War.Brigham Young University Law
Review 2016(6): 1895-1965.
Whaley, R.E. (2000) The Investor Fear Gauge. Journal of Portfolio Manage-
ment 26(3): 12-16.
Whaley, R.E. (2002) Return and Risk of CBOE Buy Write Monthly Index.
Journal of Derivatives 10(2): 35-42.
Whaley, R.E. (2009) Understanding the VIX. Journal of Portfolio Manage-
ment 35(3): 98-105.
Wheaton, W.C. (1990) Vacancy, Search, and Prices in a Housing Market
Matching Model. Journal of Political Economy 98(6): 1270-1292.
White, L.H. (2015) The Market for Cryptocurrencies. Cato Journal 35(2):
383-402.
Whittaker, E.T. (1923) On a New Method of Graduations. Proceedings of the
Edinburgh Mathematical Society 41: 63-75.
Whittaker, E.T. (1924) On the theory of graduation. Proceedings of the Royal
Society of Edinburgh 44: 77-83.
Wilder, J.W., Jr. (1978) New Concepts in Technical Trading Systems. Greens-
boro, NC: Trend Research.
Willett, P. (2006) The Porter stemming algorithm: then and now. Program:
Electronic Library and Information Systems 40(3): 219-223.
Wilner, R. (1996) A new tool for portfolio managers: Level, slope, and curva-
ture durations. Journal of Fixed Income 6(1): 48-59.
Wilson, D.J. (2016) The Impact of Weather on Local Employment: Using
Big Data on Small Places. Federal Reserve Bank of San Francisco Work-
ing Papers Series , No. 2016-21. Available online: https://www.frbsf.org/
economic-research/files/wp2016-21.pdf.
Wilson, A.C., Roelofs, R., Stern, M., Stern, N. and Recht, B. (2018) The
Marginal Value of Adaptive Gradient Methods in Machine Learning. Working
Paper. Available online: https://arxiv.org/pdf/1705.08292.pdf.
Wilson, R.L. and Sharda, R. (1994) Bankruptcy prediction using neural net-
works. Decision Support Systems 11(5): 545-557.
272
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 274

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Windas, T. (2007) An Introduction to Option-Adjusted Spread Analysis.
(Miller, T. (ed.) Revised and Expanded Third Edition.) Princeton, NJ:
Bloomberg Press.
Wolf, A. (1987) Optimal hedging with futures options. Journal of Economics
and Business 39(2): 141-158.
Wolf, V. (2014) Comparison of Markovian Price Processes and Optimality
of Payoﬀs (Ph.D. Thesis). Freiburg im Breisgau, Germany: Albert-Ludwigs-
Universit¨ at Freiburg. Available online:https://freidok.uni-freiburg.de/
fedora/objects/freidok:9664/datastreams/FILE1/content.
Wong, W.-K., Thompson, H.E. and Teh, K. (2011) Was There Abnormal
Trading in the S&P 500 Index Options Prior to the September 11 Attacks?
Multinational Finance Journal 15(3/4): 1-46.
Wood, J. (1997) A Simple Model for Pricing Imputation Tax Credits Under
Australia’s Dividend Imputation Tax System. Paciﬁc-Basin Finance Journal
5(4): 465-480.
Woodard, J. and Garcia, P. (2008) Weather Derivatives, Spatial Aggregation,
and Systemic Risk: Implications for Reinsurance Hedging. Journal of Agricul-
tural and Resource Economics 33(1): 34-51.
Woodlock, P. and Dangol, R. (2014) Managing bankruptcy and default risk.
Journal of Corporate Accounting & Finance 26(1): 33-38.
Woodward, G.T. (1990) The Real Thing: A Dynamic Proﬁle of the Term
Structure of Real Interest Rates and Inﬂation. Journal of Business 63(3): 373-
398.
Working, H. (1953) Futures Trading and Hedging.American Economic Review
43(3): 314-434.
Worzala, E. and Newell, G. (1997) International real estate: A review of strate-
gic investment issues. Journal of Real Estate Portfolio Management 3(2): 87-
96.
Wright, R., Tekin, E., Topalli, V., McClellan, C., Dickinson, T. and Rosen-
feld, R. (2017) Less Cash, Less Crime: Evidence from the Electronic Beneﬁt
Transfer Program. Journal of Law and Economics 60(2): 361-383.
Wu, H. (2009) Global stability analysis of a general class of discontinuous
neural networks with linear growth activation functions. Information Sciences
179(19): 3432-3441.
273
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 275

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Wu, L. (2003) Jumps and Dynamic Asset Allocation. Review of Quantitative
Finance and Accounting 20(3): 207-243.
Wurstbauer, D., Lang, S., Rothballer, C. and Sch¨ afers, W. (2016) Can common
risk factors explain infrastructure equity returns? Evidence from European
capital markets. Journal of Property Research 33(2): 97-120.
Wurstbauer, D. and Sch¨ afers, W. (2015) Inﬂation hedging and protection char-
acteristics of infrastructure and real estate assets. Journal of Property Invest-
ment & Finance 33(1): 19-44.
Wurtzebach, C.H., Mueller, G.R. and Machi, D. (1991) The Impact of Inﬂation
and Vacancy on Real Estate Returns. Journal of Real Estate Research 6(2):
153-168.
Wystup, U. (2017) FX Options and Structured Products. (2nd ed.) eBook:
John Wiley & Sons, Inc.
Wystup, U. and Zhou, Q. (2014) Volatility as investment – crash protection
with calendar spreads of variance swaps. Journal of Applied Operational Re-
search 6(4): 243-254.
Xiao, T. (2013) A simple and precise method for pricing convertible bond with
credit risk. Journal of Derivatives & Hedge Funds 19(4): 259-277.
Xie, W., Liew, Q.R., Wu, Y. and Zou, X. (2014) Pairs Trading with Copulas.
Working Paper. Available online: https://ssrn.com/abstract=2383185.
Xing, Y., Zhang, X. and Zhao, R. (2010) What Does Individual Option Volatil-
ity Smirk Tell Us About Future Equity Returns? Journal of Financial and
Quantitative Analysis 45(3): 641-662.
Yadav, P.K. and Pope, P.F. (1990) Stock index futures arbitrage: International
evidence. Journal of Futures Markets 10(6): 573-603.
Yadav, P.K. and Pope, P.F. (1994) Stock index futures mispricing: proﬁt
opportunities or risk premia? Journal of Banking & Finance 18(5): 921-953.
Yamada, S. (1999) Risk Premiums in the JGB Market and Application to
Investment Strategies. Journal of Fixed Income 9(2): 20-41.
Yan, X. (2006) The Determinants and Implications of Mutual Fund Cash
Holdings: Theory and Evidence. Financial Management 35(2): 67-91.
Yang, C.C., Brockett, P.L. and Wen, M.-M. (2009) Basis risk and hedging
eﬃciency of weather derivatives. Journal of Risk Finance 10(5): 517-536.
274
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 276

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Yang, Z., You, W. and Ji, G. (2011) Using partial least squares and support
vector machines for bankruptcy prediction. Expert Systems with Applications
38(7): 8336-8342.
Yao, Y. (2012) Momentum, contrarian, and the January seasonality. Journal
of Banking & Finance 36(10): 2757-2769.
Yao, J. and Tan, C.L. (2000) A case study on using neural networks to perform
technical forecasting of forex. Neurocomputing 34(1-4): 79-98.
Yao, J., Tan, C.L. and Poh, H.L. (1999) Neural networks for technical analysis:
a study on KLCI. International Journal of Theoretical and Applied Finance
2(2): 221-241.
Yared, F. and Veronesi, P. (1999) Short and Long Horizon Term and Inﬂation
Risk Premia in the US Term Structure: Evidence from an Integrated Model for
Nominal and Real Bond Prices Under Regime Shifts.Working Paper. Available
online: https://ssrn.com/abstract=199448.
Yavas, A. and Yang, S. (1995) The Strategic Role of Listing Price in Marketing
Real Estate: Theory and Evidence. Real Estate Economics 23(3): 347-368.
Yawitz, J.B., Maloney, K.J. and Ederington, L.H. (1985) Taxes, Default Risk,
and Yield Spreads. Journal of Finance 40(4): 1127-1140.
Yawitz, J.B. and Marshall, W.B. (1985) The Use of Futures in Immunized
Portfolios. Journal of Portfolio Management 11(2): 51-55.
Yeutter, C. and Dew, J.K. (1982) The Use of Futures in Bank Loans. In:
Prochnow, H.V. (ed.) Bank Credit. New York, NY: Harper and Row.
Yim, H.L., Lee, S.H., Yoo, S.K. and Kim, J.J. (2011) A zero-cost collar option
applied to materials procurement contracts to reduce price ﬂuctuation risks in
construction. International Journal of Social, Behavioral, Educational, Eco-
nomic, Business and Industrial Engineering 5(12): 1769-1774.
Yo, S.W. (2001) Index Futures Trading and Spot Price Volatility. Applied
Economics Letters 8(3): 183-186.
Yoshikawa, D. (2017) An Entropic Approach for Pair Trading. Entropy 19(7):
320.
Youbi, F., Pindza, E. and Mar´ e, E. (2017) A Comparative Study of Spectral
Methods for Valuing Financial Options. Applied Mathematics & Information
Sciences 11(3): 939-950.
275
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 277

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Young, M. and Graﬀ, R.A. (1996) Systematic Behavior in Real Estate In-
vestment Risk: Performance Persistence in NCREIF Returns. Journal of Real
Estate Research 12(3): 369-381.
Ysmailov, B. (2017) Interest Rates, Cash and Short-Term Investments. Work-
ing Paper. Available online: http://www.fmaconferences.org/Boston/
Interest_Rates_Cash_and_ShortTermInv.pdf.
Yu, L., Wang, S. and Lai, K.K. (2005) Mining Stock Market Tendency Using
GA-Based Support Vector Machines. In: Deng, X. and Ye, Y. (eds.) Internet
and Network Economics. WINE 2005. Lecture Notes in Computer Science,
Vol. 3828. Berlin, Germany: Springer, pp. 336-345.
Yu, S. and Webb, G. (2014) The Proﬁtability of Pairs Trading Strategies
Based on ETFs. Working Paper. Available online: http://swfa2015.uno.
edu/B_Asset_Pricing_III/paper_196.pdf.
Zabolotnyuk, Y., Jones, R. and Veld, C. (2010) An empirical comparison of
convertible bond valuation models. Financial Management 39(2): 675-706.
Zakamulin, V. (2014a) The Real-Life Performance of Market Timing with
Moving Average and Time-Series Momentum Rules. Journal of Asset Man-
agement 15(4): 261-278.
Zakamulin, V. (2014b) Dynamic Asset Allocation Strategies Based on Unex-
pected Volatility. Journal of Alternative Investments 16(4): 37-50.
Zakamulin, V. (2015) A Comprehensive Look at the Empirical Performance of
Moving Average Trading Strategies. Working Paper. Available online: https:
//ssrn.com/abstract=2677212.
Zapranis, A. and Alexandridis, A. (2008) Modelling the temperature time-
dependent speed of mean reversion in the context of weather derivatives pric-
ing. Applied Mathematical Finance 15(3-4): 355-386.
Zapranis, A. and Alexandridis, A. (2009) Weather derivatives pricing: mod-
eling the seasonal residual variance of an Ornstein-Uhlenbeck temperature
process with neural networks. Neurocomputing 73(1-3): 37-48.
Zapranis, A. and Tsinaslanidis, P.E. (2012) Identifying and evaluating hori-
zontal support and resistance levels: an empirical study on US stock markets.
Applied Financial Economics 22(19): 1571-1585.
Zaremba, A. (2014) A Performance Evaluation Model for Global Macro Funds.
International Journal of Finance & Banking Studies 3(1): 161-171.
276
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 278

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Zeng, L. (2000) Pricing weather derivatives. Journal of Risk Finance 1(3):
72-78.
Zeng, Z. and Lee, C.G. (2014) Pairs trading: Optimal thresholds and prof-
itability. Quantitative Finance 14(11): 1881-1893.
Zhang, C. (2015) Using Excel’s Data Table and Chart Tools Eﬀectively in
Finance Courses. Journal of Accounting and Finance 15(7): 79-93.
Zhang, L. (2005) The Value Premium. Journal of Finance 60(1): 67-103.
Zhang, L. (2014) A closed-form pricing formula for variance swaps with mean-
reverting Gaussian volatility. ANZIAM Journal 55(4): 362-382.
Zhang, X.F. (2006) Information Uncertainty and Stock Returns. Journal of
Finance 61(1): 105-136.
Zhang, J.Z., Fargher, N.L. and Hou, W. (2018) Do Banks Audited by Spe-
cialists Engage in Less Real Activities Management? Evidence from Repur-
chase Agreements. AUDITING: A Journal of Practice & Theory (forthcom-
ing). DOI: https://doi.org/10.2308/ajpt-52017.
Zhang, X., Fuehres, H. and Gloor, P.A. (2011) Predicting Stock Market Indi-
cators Through Twitter “I hope it is not as bad as I fear”. Procedia – Social
and Behavioral Sciences 26: 55-62.
Zhang, J.E., Shu, J. and Brenner, M. (2010) The new market for volatility
trading. Journal of Futures Markets 30(9): 809-833.
Zhang, J.E. and Xiang, Y. (2008) The implied volatility smirk. Quantitative
Finance 8(3): 263-284.
Zhang, J.E. and Zhu, Y. (2006) VIX futures.Journal of Futures Markets 26(6):
521-531.
Zheng, W. and Kwok, Y.K. (2014) Closed form pricing formulas for discretely
sampled generalized variance swaps. Mathematical Finance 24(4): 855-881.
Zheng, H., Thomas, L.C. and Allen, D.E. (2003) The Duration Derby: A
Comparison of Duration Strategies in Asset Liability Management. Journal of
Bond Trading and Management 1(4): 371-380.
Zhou, L. (2013) Performance of corporate bankruptcy prediction models on
imbalanced dataset: The eﬀect of sampling methods. Knowledge-Based Sys-
tems 41: 16-25.
277
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 279

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Zhou, L., Yao, S., Wang, J. and Ou, J. (2016) Global ﬁnancial crisis and
China’s pawnbroking industry. Journal of Chinese Economic and Business
Studies 14(2): 151-164.
Zhu, H. (2006) An Empirical Comparison of Credit Spreads between the Bond
Market and the Credit Default Swap Market. Journal of Financial Services
Research 29(3): 211-235.
Zmijewski, M.E. (1984) Methodological Issues Related to the Estimation of
Financial Distress Prediction Models. Journal of Accounting Research 22: 59-
82.
278
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 280

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Glossary
absolute momentum: time-series momentum.
acquirer company: the company purchasing another company (target com-
pany) in a corporate acquisition.
activation function: a function that deﬁnes the output of a node (artiﬁcial
neuron) in an artiﬁcial neural network given an input (or a set of inputs).
active investing (a.k.a. active management): an investment strategy that
involves active (frequent) buying and selling of securities in a portfolio (cf. passive
investing) with the view of exploiting (perceived) proﬁt-generating opportunities.
actively managed ETF: an exchange-traded fund whose underlying portfo-
lio allocation is actively managed.
adjusted price: a stock’s price adjusted for splits and dividends.
adverse selection: an eﬀect caused by smart order ﬂow, whereby most limit or-
ders to buy at the bid (sell at the ask) get ﬁlled when the market is trading through
them downward (upward).
aggressive order: a market order, or a marketable limit order (to buy at the
ask or higher, or to sell at the bid or lower).
aggressive order ﬂow: order ﬂow comprised of aggressive orders.
alpha: following common trader lingo, any reasonable “expected return” that
one may wish to trade on.
alpha portfolio (a.k.a. alpha combo): a portfolio of (typically, a large
number of) alphas combined with some weights.
alpha rotation: a type of ETF trading strategy.
American option: an option (e.g., call or put) that can be exercised on any
trading day on or before expiration.
announcement days: days with important economic announcements such as
FOMC announcements (cf. non-announcement days).
annualization factor: a multiplicative factor for annualizing a quantity.
279
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 281

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
annualized return: an average daily return times 252 (the number of trad-
ing days in a year).
annualized Sharpe ratio: a daily Sharpe ratio times the square root of 252
(the number of trading days in a year).
appraised value: an evaluation of a property’s or some other valuable ob-
ject’s (e.g., jewelry) value at a given time.
arbitrage: taking advantage of a (perceived) mispricing (a.k.a. arbitrage op-
portunity) in one or more securities to make a proﬁt.
arbitrage trade: a set of transactions executed with the view of exploiting
an arbitrage opportunity.
artiﬁcial neural network (ANN): a computing system (inspired by the neu-
ral structure of a brain) of nodes (artiﬁcial neurons) linked by connections (akin to
the synapses in a brain) that can transmit signals from one node to another.
Asian option: an option whose payoﬀ is determined by the average under-
lying price over some preset time period.
ask (a.k.a. ask price, or oﬀer, or oﬀer price): the price at which a seller is
willing (oﬀering) to sell.
asset allocation: assigning weights (allocation percentages) to the assets in
a portfolio, typically based on risk-reward considerations.
asset-backed security (ABS): a ﬁnancial security collateralized by a pool
of assets such as loans, mortgages, royalties, etc.
asset class: a group of securities with similar characteristics.
at-the-money (ATM) option: an option whose exercise price is the same
as the current price of the underlying asset.
attachment (a.k.a. attachment point): the percentage of the underlying
portfolio loss at which a tranche of a CDO (collateralized debt obligation) starts to
lose value.
back leg: longer-maturity bonds in a yield curve spread strategy (ﬂattener
or steepener).
280
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 282

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
backspread: a type of options strategies.
backtest: a simulation of strategy performance using historical data.
backtesting period: the historical period over which a backtest is performed.
backwardation: when the futures curve (term structure) is downward-sloping.
bank deposit certiﬁcate (a.k.a. certiﬁcate of deposit, or CD): a sav-
ings certiﬁcate (a promissory note issued by a bank) with a ﬁxed maturity date and
interest rate.
banker’s acceptance (BA): a short-term debt instrument issued by a com-
pany and guaranteed by a commercial bank.
bankruptcy: a legal status (imposed by a Court order) of a company that
cannot repay debts to its creditors.
barbell: a bond portfolio consisting of bonds with only two (typically, short
and long) maturities.
barrier option: an option that can be exercised only if the underlying se-
curity’s price passes a certain level or “barrier”.
base form (a.k.a. stem): in linguistics, the part of a word that is com-
mon to all its inﬂected variants.
basis point (bps): 1/100 of 1%.
basket: a portfolio of assets combined with some weights.
Bayes’ theorem: P (A|B) = P (B|A)× P (A)/P (B), where P (A|B) is the con-
ditional probability of A occurring assuming B is true, and P (A) and P (B) are the
probabilities of A and B occurring independently of each other.
bearish outlook: when a trader expects the market or a security to trade lower.
bearish strategy: a directional strategy where the trader proﬁts if the un-
derlying instrument’s price goes down.
Bermudan option: an option that can be exercised only on speciﬁed dates
on or before expiration.
281
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 283

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Bernoulli probability distribution: a discrete probability distribution of a
random variable which takes the value 1 with probability p and the value 0 with
probability q = 1− p.
bias: in an artiﬁcial neural network, the inhomogeneous component of the ar-
gument of an activation function.
bid (a.k.a. bid price): the price at which a buyer is willing to buy.
bid-ask spread: ask price minus bid price.
binary industry classiﬁcation: an industry classiﬁcation where each com-
pany belongs to one and only one sub-industry, industry, sector, etc.
binary option (a.k.a. digital option, or all-or-nothing option): an option
that pays a preset amount, say, $1, if the underlying security meets a predeﬁned
condition on expiration, otherwise it simply expires without paying anything to the
holder.
bisection method: a root-ﬁnding method that repeatedly bisects an inter-
val and selects a subinterval in which a root must lie for further examination.
Bitcoin (BTC): the world’s ﬁrst decentralized digital currency (cryptocur-
rency).
black-box algorithm: an algorithm that can be viewed in terms of its in-
puts and outputs, without any knowledge of its internal workings.
Black-Scholes model (a.k.a. Black-Scholes-Merton model): a mathe-
matical model of stock (or other underlying asset) dynamics used in pricing options
and other derivatives, where the log of the underlying price is described by a Brow-
nian motion with a constant drift.
blockchain: a distributed ledger for keeping a record of all transactions that con-
sists of a sequential chain of blocks, linked using cryptography and time-stamping,
and containing transaction records.
body: the middle (by maturity in bond portfolios, and by strike price in option
portfolios) leg of a butterﬂy portfolio.
bond: a ﬁxed-income instrument, a promise of being paid some amount (princi-
pal) at some future time T (maturity), and possibly some smaller amounts (coupon
282
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 284

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
payments) at some times prior to T .
bond immunization: matching the duration of a bond portfolio to the matu-
rity of a future cash obligation.
bond maturity: the time at which the principal of a bond is paid.
bond principal: the amount the borrower (bond issuer) owes to the bond-
holder in full at bond maturity.
bond value: the worth of a bond at a given time before maturity.
bond yield (here, yield to maturity): the overall interest rate earned as-
suming the bond is held until maturity and all coupon and principal payments are
made as promised.
bond yield spread (a.k.a. bond spread): the spread between the bond
yield and the risk-free rate.
bondholder: bond owner.
book-to-market ratio: the company’s total book value divided by its mar-
ket capitalization (same as B/P ratio).
book-to-price ratio (a.k.a. B/P ratio): the company’s book value per share
outstanding divided by its stock share price.
book value: the company’s total assets minus its total liabilities.
Boolean: a binary variable with only two possible values, TRUE and FALSE.
box: an option trading strategy.
break-even price (a.k.a. break-even point): a price of the underlying
security (e.g., stock) in an option trading strategy at which it breaks even (i.e.,
when the P&L is zero).
breakeven rate: the ﬁxed rate of an inﬂation swap.
broad market index: an index based on a broad cross-section of securities
(e.g., S&P 500, Russell 3000, etc.).
brownﬁeld project: a project associated with established infrastructure as-
283
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 285

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
sets in need of improvement.
Brownian motion (a.k.a. Wiener process): a continuous-time (t) stochas-
tic process Wt, where W0 = 0, Wt is a normal random variable with mean 0 and
variance t, and the increment Ws+t− Ws is a normal random variable with mean 0
and variance t and is independent of the history of what the process did up to times.
Btu: British thermal unit, approximately 1,055 Joules.
bubble (a.k.a. economic, asset, speculative, market, price or ﬁnancial
bubble): an asset trading at prices strongly inﬂated compared with its intrinsic
value.
bullet: a bond portfolio where all bonds have the same maturity.
bullish outlook: when a trader expects the market or a security to trade higher.
bullish strategy: a directional strategy where the trader proﬁts if the un-
derlying instrument’s price goes up.
butterﬂy: a portfolio (of bonds or options) with 3 legs, two peripheral (by
maturity in bond portfolios, and by strike price in option portfolios) wings and a
body in the middle.
butterﬂy spread: a butterﬂy option strategy.
buy-and-hold asset/investment: an asset/investment for a passive long-term
strategy where the investor holds a long position irrespective of short-term ﬂuctua-
tions in the market.
buy-write strategy: buying stock and writing (selling) a call option against
the stock position.
calendar spread (for futures): buying (selling) a near-month futures and
selling (buying) a deferred-month futures.
calendar spread (for options): buying a longer-expiration option (call or
put) and selling a shorter-expiration option (of the same type, for the same under-
lying, and with the same strike price).
call option (a.k.a. call): see European call option, option .
Canary option: an option that can be exercised, say, quarterly, but not before
284
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 286

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
a determined time period, say, 1 year, has elapsed.
cancel-replaced order: a placed order that has been subsequently canceled
and replaced with another order.
canceled order: a placed order that has been subsequently canceled.
capital allocation: see asset allocation.
capital gain strategy: a strategy that proﬁts from buying and selling an asset
(or, more generally, establishing and liquidating a position).
Carhart’s momentum factor (a.k.a. MOM): winners minus losers by (12-
month) momentum.
carry (a.k.a. cost of carry): a return (positive or negative) from holding
an asset.
carry trade (a.k.a. carry strategy): a strategy based on earning a spread
between borrowing a low carry asset and lending a high carry asset.
cash (for indexes): in common trader lingo, “cash” refers to the underly-
ing index portfolio (e.g., the S&P 500 stocks for the S&P 500 index).
cash-equivalent asset: a highly liquid short-term investment security with
high credit quality (e.g., REPO).
cash ﬂow: the net amount of cash and cash-equivalent assets being transferred
into and out of a company (in the business context) or a portfolio (in the trading
context).
cash ﬂow shortfall: the amount by which a ﬁnancial obligation or liability
exceeds the amount of cash (or, more generally, liquid funds) that is available.
cash merger: a merger where the acquirer company pays the target company’s
shareholders cash for its stock.
CDO tranche: a part of a CDO consisting of assets with diﬀerent credit ratings
and interest rates.
CDO tranche spread: for achieving a null MTM of a CDO tranche, the value
of the default leg of the tranche divided by its risky duration.
285
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 287

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
CDS basis: CDS spread minus bond yield spread.
CDS basis arbitrage (a.k.a. CDS arbitrage): buying a bond and insuring
it with a CDS.
CDS index: a credit default swap index such as CDX and iTraxx.
CDS spread: a periodic (e.g., annual) premium per dollar of the insured debt.
cents-per-share (CPS): the realized P&L in cents (as opposed to dollars)
divided by the total shares traded (which includes both establishing and liquidating
trades).
channel: a range/band, bounded by a ceiling and a ﬂoor, within which the
stock price ﬂuctuates.
Chapter 11: a chapter of Title 11, the United States Bankruptcy Code.
cheap stock: a stock that is perceived to be undervalued by some criterion.
claim: the payoﬀ of an option (or some other derivative).
class: in machine learning, one of the possible predicted outcomes of a ma-
chine learning algorithm.
close (a.k.a. close price, or closing price): the closing price of a stock
at the NYSE close (4:00 PM Eastern Time).
close-to-close return: the return from the close of the previous trading day to
the close of the current trading day.
close-to-open return: the return from the close of the previous trading day to
the open of the current trading day.
clustering algorithm: grouping objects (into clusters) based on some simi-
larity criterion (or criteria).
Cochrane-Piazzesi predictor: a bond return predictor.
collar (a.k.a. fence): an option trading strategy.
collateral: something of value pledged as security for repayment of a loan,
forfeited if the borrower defaults.
286
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 288

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
collateralized debt obligation (CDO): an asset-backed security (ABS) con-
sisting of a basket of assets such as bonds, credit default swaps, etc.
combo (for options): a type of option trading strategies.
commercial paper: short-term unsecured promissory notes issued by com-
panies.
commercial real estate: real estate property used for business purposes (rather
than living space), e.g., shopping centers, retail shops, oﬃce space, etc.
Commitments of Traders (COT): weekly reports provided by CFTC.
commodity: a raw material (e.g., gold, silver, oil, copper) or an agricultural
product (e.g., wheat, soy, rice) that can be bought and sold.
commodity allocation percentage (CA): the allocation weight for commodi-
ties included as an inﬂation hedge in a portfolio of other assets.
commodity futures: futures contracts on commodities.
common stock: a security representing ownership in a corporation entitling
its holder to exercise control over the company aﬀairs (e.g., via voting on electing a
board of directors and corporate policy), with the lowest priority (after bondholders,
preferred stockholders, etc.) for rights to the company’s assets in the event of its
liquidation.
compounding: reinvestment of interest earned to generate additional inter-
est in the future.
compounding period: the period between two consecutive points in time when
interest is paid or added to the principal.
conditional expectation (a.k.a. conditional expected value, or conditional
mean): an average value of a quantity assuming some condition occurs.
conditional independence: A and B are conditionally independent assum-
ing C is true iﬀ the occurrence of A assuming C is independent from the occurrence
of B assuming C and vice versa, i.e., P (A∩ B|C) = P (A|C)× P (B|C), where
P (A|B) is a conditional probability.
conditional probability: P (A|B), the probability of A occurring assuming
287
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 289

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
B is true.
condor: a type of options strategies.
constrained regression: a linear regression subject to a set of linear or non-
linear constraints, e.g., non-negative least squares (NNLS), where the regression
coeﬃcients are required to be nonnegative.
Consumer Price Index (CPI): a measure of the price level of a market basket
of consumer goods and services.
contango: when the futures curve (term structure) is upward-sloping.
contingent leg: in a CDO, the default leg, the other leg being the premium leg.
continuous compounding: an idealized mathematical limit of compounding
where the number of compounding periods n goes to inﬁnity, the length δ of each
compounding period goes to zero, and the product n× δ is kept ﬁxed and ﬁnite.
contrarian eﬀect: see mean-reversion eﬀect.
control rights: the legal entitlements granted to an investor (e.g., a share-
holder holding common stock), such as the right to transfer shares, receive regular
and accurate ﬁnancial disclosure, vote on speciﬁc issues at the company, etc.
conversion factor: the quoted price a bond would have per dollar of principal
on the ﬁrst day of the delivery month of an interest rate futures contract assuming
that the interest rate for all maturities equals 6% per annum with semiannual com-
pounding.
conversion factor model: a model (based on the conversion factor) com-
monly used to calculate hedge ratios when hedging interest rate risk with interest
rate futures.
conversion price: the price of the underlying stock at which a convertible
bond can be converted into stock.
conversion ratio: the number of the issuer’s stock shares into which a con-
vertible bond can be converted.
convertible arbitrage: a trading strategy involving a convertible bond and
stock of the same issuer.
288
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 290

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
convertible bond: a hybrid security with an embedded option to convert a
bond to a preset number (conversion ratio) of the issuer’s stock when, e.g., the
stock price reaches a preset level (conversion price).
convexity (for bonds): a measure of non-linear dependence of bond prices
on changes in interest rates, which involves the second derivative of the bond price
w.r.t. the interest rates.
core inﬂation (CI): long run inﬂation, with items subject to volatile prices
(such as food and energy) excluded (cf. headline inﬂation)
corporate actions: events initiated by a publicly traded company such as
stock splits, dividends, mergers and acquisitions (M&A), rights issues, spin-oﬀs, etc.
correlation: a measure of how closely two securities move in relation to each
other, deﬁned as the covariance of their returns divided by a product of the standard
deviations of said returns.
correlation matrix: an N× N matrix with unit diagonal elements, whose
oﬀ-diagonal elements are the pair-wise correlations of N diﬀerent securities.
correlation trading: arbitraging the average pair-wise correlation of the in-
dex constituents vs. its future realized value.
counterparty: the other party that participates in a ﬁnancial transaction.
coupon bond: a bond that makes periodic coupon payments before matu-
rity.
coupon rate: an uncompounded, ﬁxed or variable rate at which a coupon
bond makes coupon payments.
covariance: a mean value of the product of the deviations of the returns of
two securities from their respective mean values.
covariance matrix: an N× N matrix, whose oﬀ-diagonal elements are the
pair-wise covariances of N diﬀerent securities, and whose diagonal elements are the
corresponding variances.
covered call: see buy-write strategy.
covered interest arbitrage: a trading strategy that exploits deviations from
CIRP.
289
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 291

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
covered put: see sell-write strategy.
credit default swap (CDS): a swap that provides insurance against default
on a bond.
credit derivatives: ﬁnancial contracts (e.g., CDS) that allow parties to trans-
fer or receive exposure to credit risk.
credit rating (for bonds): a measure of the creditworthiness of corporate
or government bonds (e.g., S&P’s credit ratings AAA, AA+, AA, AA-, A+, A, A-,
BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, CCC+, CCC, CCC-, CC, C, D).
credit spread: the diﬀerence between the bond yield and the risk-free rate
(same as the bond yield spread).
cross-border tax arbitrage: exploiting diﬀerences in the tax regimes of two
or more countries.
cross-hedging: managing risk exposure to one security by taking an opposite
position (with some hedge ratio) in another security (or its derivative, e.g., futures),
where the two securities are positively correlated and have similar price movements.
cross-sectional quantity: a quantity (e.g., mean, standard deviation, etc.)
computed across a set of securities (e.g., stocks in a portfolio) as opposed to serially
(i.e., across a time series for each security).
cross-sectional regression: a regression where the independent variables are
vectors whose elements are labeled by a cross-sectional index, e.g., that which labels
stocks in a portfolio (cf. serial regression).
cross-validation (a.k.a. out-of-sample testing): a technique to evaluate
predictive models by partitioning the original data sample into a training set to
train the model, and a test set to evaluate it.
cryptoassets: cryptocurrencies and similar digital assets.
cryptocurrency: a digital medium of exchange that uses cryptography (e.g.,
BTC).
cryptography: constructing and analyzing protocols that prevent third par-
ties from reading private messages.
290
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 292

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
cum-dividend: when the stock buyer is entitled to receive a dividend that
has been declared but not paid (cf. ex-dividend).
cumulative inﬂation: inﬂation rate measured from time t1 to time t2 (cf.
year-on-year inﬂation).
cumulative return: an asset’s return from time t1 to time t2.
curvature: in a yield curve, the change in the slope thereof as a function of
maturity.
curve-neutrality: approximate neutrality of a bond portfolio to small steepen-
ing and ﬂattening of the yield curve.
curve trade: a ﬂattener or steepener (in bonds or CDOs).
daily roll value: futures basis divided by the number of business days until
the settlement.
dark spread: the diﬀerence between the wholesale price of electricity and the
price of coal required to produce it by a coal-ﬁred power plant.
data mining: a process of ﬁnding patterns/trends in large data sets.
debt seniority: the order of repayment of debt in the event of a sale or
bankruptcy of the debt issuer.
decentralized digital currency: a decentralized cryptocurrency such as BTC,
ETH, etc.
decile: each of the 10 (approximately) equal parts of a sample (e.g., data sam-
ple).
default: a failure to repay a loan/debt.
default risk: the (estimated/perceived) risk of a default of a borrower.
deferred-month futures: a futures contract with the settlement date in the
later months (cf. front-month futures).
delay-d backtest: a backtest in which all quantities used for establishing or
liquidating simulated positions at any given time t are computed using historical
quantities from times at least d trading days prior to t.
291
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 293

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
deliverable bond: a bond in the delivery basket of an interest rate futures
contract.
delivery: transferring the underlying instrument (or commodity) in a contract
(e.g., futures or forward) to the buyer at maturity (delivery date) at a pre-agreed
price (delivery price).
delivery basket: in interest rate futures, the array of bonds that can be deliv-
ered at the delivery date.
delivery month: the month in which the delivery in a futures contract oc-
curs.
Delta: the ﬁrst derivative of the value of a derivative asset (e.g., option) w.r.t.
the price of the underlying asset.
Delta-hedge: hedging a long (short) position in a derivative asset with a short
(long) position in the underlying asset with the hedge ratio equal the Delta of the
derivative asset.
Delta-neutral strategy: a trading strategy which achieves null Delta via, e.g.,
Delta-hedging.
demeaning: subtracting from the elements of a sample their mean value across
said sample.
derivative (a.k.a. derivative contract, or contingent claim): a secu-
rity (e.g., option) whose future payoﬀ depends on the value of its underlying asset
(e.g., stock) and is contingent on some uncertain future event.
desired holdings: portfolio holdings to be attained by a trading strategy.
detachment (a.k.a. detachment point): the percentage of the underly-
ing portfolio loss at which a tranche of a CDO (collateralized debt obligation) loses
all its value.
diagonal spread: an option trading strategy.
dimnames: a command in R for the names of column and row labels of a
matrix.
directional strategy: a strategy that proﬁts based on the underlying secu-
292
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 294

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
rity’s (or securities’) future direction (cf. non-directional strategy).
discount bond (a.k.a. zero-coupon bond): a bond that pays only its prin-
cipal at maturity but makes no coupon payments.
discount factor: the worth of a discount bond with $1 principal at time t
prior to its maturity T .
discount rate (a.k.a. Fed discount rate, or Federal discount rate): the
interest rate charged to commercial banks and other depository institutions for loans
received from the U.S. Federal Reserve.
discretionary strategy: a strategy that relies on the fund manager’s skills
(cf. systematic strategy).
discretionary macro: discretionary global macro strategies based on analysts’
subjective opinions.
dispersion trading: arbitraging the index implied volatility vs. implied volatil-
ities of its constituents.
distress risk puzzle: an empirical occurrence that companies with lower bankruptcy
risk tend to yield higher returns than riskier ones.
distressed asset: an asset (e.g., debt) of a distressed company.
distressed debt: see distressed asset.
distressed debt strategy: strategies based on acquiring debt of a distressed
company.
distressed company: a company undergoing ﬁnancial or operational distress.
distributed ledger: a database shared and synchronized across a (typically
large, peer-to-peer) network encompassing multiple sites.
diversiﬁcation: allocating capital to reduce exposure to any one particular
asset or risk by investing in a variety of assets.
dividend: a distribution of some of the earnings of a company, as decided by its
board of directors, to a class of its shareholders, usually (but not always) quarterly.
dividend imputation: a corporate tax system in which some or all of the
293
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 295

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
tax paid by a company may be attributed, or imputed, to the shareholders via a tax
credit to reduce the income tax payable on a distribution via, e.g., dividends.
dollar carry trade: an FX trading strategy.
dollar duration: a measure of the absolute bond price sensitivity to changes
in the interest rates, deﬁned as the modiﬁed duration times the bond price.
dollar-duration-neutrality: when the sum of dollar durations of a bond port-
folio is null (with dollar durations of short bond positions deﬁned to be negative).
dollar holding (a.k.a. dollar position): the dollar value of an asset’s posi-
tion in a portfolio.
dollar-neutrality: when the sum of dollar holdings in a portfolio is null (with
dollar holdings of short positions deﬁned to be negative).
domestic currency: the currency of the investor’s home country.
Donchian Channel: a commonly used deﬁnition of a channel in channel trad-
ing strategies.
double-taxation: a corporate taxation system (e.g., in the U.S.) where the
corporate income is ﬁrst taxed at the corporate level, and then again when divi-
dends are received by the shareholders.
downside risk: the risk associated with losses.
drawdown: a peak-to-trough decline in the P&L during a given period, where
the peak (trough) is deﬁned as the P&L maximum (minimum) in said period.
drift: a mean change in a time-dependent quantity over a period of time, i.e., a
serial mean.
dual-momentum sector rotation: an ETF momentum strategy.
dumb order ﬂow (a.k.a. uninformed order ﬂow): aggressive order ﬂow
not based on a predictive expected return.
dummy variable (a.k.a. binary variable): a predictor variable taking bi-
nary values 0 or 1 to indicate the absence or presence of some eﬀect or belonging
or not belonging to some category that may aﬀect the outcome (e.g., if a company
belongs to a given economic sector).
294
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 296

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
duration: see dollar duration, Macaulay duration, modiﬁed duration, risky du-
ration.
duration-hedging: hedging duration risk (i.e., interest rate risk) with inter-
est rate swaps or interest rate futures.
duration-targeting strategy: a strategy (e.g., a bond ladder) that maintains
an approximately constant duration by selling shorter-maturity bonds as they ap-
proach maturity and replacing them with new longer-maturity bonds.
dynamic asset allocation: frequently adjusting the asset allocations in a port-
folio according to changing market conditions.
earnings: the after-tax net income of a company.
earnings-momentum: a momentum strategy based on earnings.
economic activity: production, distribution, exchange and consumption of
goods and services.
economic data: data (typically, time series) pertaining to an actual economy.
eigenvalue: a root of the characteristic equation of a matrix (see eigenvec-
tor).
eigenvector: for a square symmetric N× N matrix A, an N-vector V that
solves the characteristic equation A V = λ V , where λ is the corresponding eigen-
value (which is a number).
electronic trading: trading securities electronically, as opposed to by human
traders on the trading ﬂoors of the exchanges.
EMA: an exponential moving average, a serial moving average with past con-
tributions suppressed with exponentially decreasing weights.
embedded option: in a convertible bond, the option to convert the bond to a
preset number of the issuer’s stock.
EMSD: an exponential moving standard deviation, a serial moving standard
deviation with past contributions suppressed with exponentially decreasing weights.
equally-weighted portfolio: a portfolio where all assets have equal dollar
295
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 297

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
holdings.
equity: a company’s stock or other security representing its ownership inter-
est.
equity market: a stock market.
equity tranche: the lowest quality tranche of a CDO.
eRank (a.k.a. eﬀective rank): a measure of eﬀective dimensionality of a
matrix.
error function: in machine learning, a function to be minimized that is con-
structed from the errors (or similar), e.g., the sum of squares of the errors, or some
other suitable function (not to be confused with the Gauss error function erf( x)).
establishing: buying or shorting an asset or portfolio from a null position.
estimation period: the length of a time-series data sample used in estimating
some parameters, e.g., regression coeﬃcients.
ETH: ether/Ethereum, a cryptocurrency.
Euclidean distance: the distance between two vectors deﬁned as the square
root of the sum of squares of the diﬀerences between their components.
EUR: euro, a unit of the eurozone currency.
eurodollar: a USD deposit held in a bank outside the U.S.
European call option: a right (but not an obligation) to buy a stock at the
maturity time T for the strike price k agreed on at time t = 0.
European put option: a right (but not an obligation) to sell a stock at the
maturity time T for the strike price k agreed on at time t = 0.
ex-dividend when the stock seller is entitled to receive a dividend that has
been declared but not paid (cf. cum-dividend).
excess return: a return of an asset in excess of some benchmark return (e.g.,
risk-free rate).
exchange rate (a.k.a. FX rate): the rate of exchange between two dif-
296
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 298

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ferent currencies.
execution price: the price at which an order (e.g., to buy stock) is ﬁlled
(executed).
exercise date: a date on which an option can be exercised.
exotic options: a broad category of options that typically are complexly struc-
tured.
expected return: a future return of an asset expected based on some rea-
sonable consideration, e.g., an average realized return over some past period.
expiration: the last date on which a derivatives contract (e.g., option or fu-
tures) is valid.
explanatory variable: a variable that has (or is expected to have) some ex-
planatory power for an observed variable (e.g., hours studied by a student for a ﬁnal
exam can be expected to be an explanatory variable for the student’s ﬁnal exam
grade/score).
exponential smoothing parameter: the exponential suppression factor in
an exponential moving average.
exposure: the amount that can be lost (or gained) in an investment.
face value (a.k.a. principal): the amount paid to the bondholder at maturity.
factor (a.k.a. risk factor): a common explanatory variable for a cross-section
of asset returns (e.g., stocks).
factor loadings matrix: the N× K matrix ΩiA (i = 1, . . . , N, A = 1, . . . , K,
typically K≪ N) in a K-factor model Yi =∑K
A=1 ΩiA FA + ϵi, where Yi are the
observed variables, FA are the unobserved variables (common factors), and ϵi are
the unobserved error terms.
factor portfolio: a portfolio that aims to attain exposure to a given factor.
fair value: a market value of a security or, in the absence of a market value, a
theoretical value based on some reasonable modeling.
Fama-French factors: MKT, the excess return (deﬁned as the return in ex-
cess of the risk-free rate, in turn deﬁned as the one-month Treasury bill rate) of
297
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 299

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
the market portfolio; SMB, the excess return of the Small minus Big (by market
capitalization) portfolio; HML, the excess return of the High minus Low (by book-
to-market) portfolio.
Fama puzzle: see forward discount anomaly.
feature (in machine learning): a predictor, an input variable.
ﬁat currency: a legal tender declared by a government (e.g., U.S. dollar) but
not backed by a physical commodity (such as gold).
ﬁll: when an order to buy or sell a security or commodity is completed, with a
partial completion (e.g., only 100 shares of a 200 share buy order are ﬁlled) known
as a partial ﬁll.
ﬁll or kill limit order (a.k.a. FOK): a limit order to buy or sell stock
that must be executed immediately and completely or not at all (no partial ﬁlls are
allowed).
ﬁnancial crisis: when some ﬁnancial assets suddenly lose a large part of their
nominal value.
ﬁrst-month contract: see front-month futures.
ﬁx-and-ﬂip: a real estate strategy.
ﬁxed coupon bond (a.k.a. ﬁxed rate coupon bond): a bond with a
ﬁxed (as opposed to variable) coupon rate.
ﬁxed-income asset: a debt instrument that generates ﬁxed returns in the
form of interest payments.
ﬁxed interest rate (a.k.a. ﬁxed rate): an interest rate on a liability that
remains unchanged either for the entire term of the loan or for its part.
ﬁxed rate payment: a coupon payment of a ﬁxed coupon bond.
ﬂattener: a yield curve spread bond strategy.
ﬂoating coupon bond (a.k.a. ﬂoating rate coupon bond, or variable
coupon bond, or variable rate coupon bond): a bond with a variable
(as opposed to ﬁxed) coupon rate.
298
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 300

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ﬂoating interest rate (a.k.a. ﬂoating rate, or variable interest rate, or
variable rate): interest rate on a liability that varies during the term of the
loan.
ﬂoating rate payment: a coupon payment of a ﬂoating coupon bond.
FOMC announcements: Federal Open Market Committee announcements
such as interest rate hikes.
forecasting future returns: predicting future returns.
foreign currency: a currency (that is diﬀerent from the domestic currency)
of a country other than the investor’s home country.
formation period: in momentum strategies, the period over which the mo-
mentum indicator is computed.
forward (a.k.a. forward contract): a contract struck at time t = 0, where
one of the two parties agrees to sell the other an asset at some future time T (known
as the expiry, delivery date or maturity of the contract) for the pre-agreed strike
price k.
forward discount: when the forward FX rate is lower than the spot FX rate.
forward discount anomaly (a.k.a. forward premium anomaly, or forward
discount puzzle, or forward premium puzzle, or Fama puzzle): an empir-
ical occurrence whereby on average high interest rate currencies tend to appreciate
(somewhat) w.r.t. low interest rate currencies.
forward FX rate: the FX rate of a forward FX contract.
forward premium: when the forward FX rate is higher than the spot FX
rate.
front leg: shorter-maturity bonds in a yield curve spread strategy (ﬂattener
or steepener).
front-month futures: a futures contract with the settlement date closest to
the current date (cf. deferred-month futures).
fundamental analysis: evaluating securities based on fundamental data.
fundamental data: data pertaining to the fundamentals of stocks or other
299
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 301

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
securities, including time series and/or cross-sectional data.
fundamental industry classiﬁcation: an industry classiﬁcation of compa-
nies (into sectors, industries, sub-industries, etc.) based on fundamental/economic
data, such as companies’ products and services, revenue sources, suppliers, competi-
tors, partners, etc. (cf. statistical industry classiﬁcation).
fundamental trading strategy: a trading strategy based on fundamental
analysis.
fundamentals: quantitative and qualitative information on the ﬁnancial/economic
health and valuation of a company, security, currency, etc.
futures (a.k.a. futures contract): a standardized forward contract traded
on a futures exchange.
futures basis: the futures price minus the underlying spot price.
futures curve (a.k.a. futures term structure): the dependence of the
futures prices on time to delivery.
futures delivery basket: see delivery basket.
futures spread: see calendar spread (for futures).
FX pair: currencies of 2 diﬀerent countries.
FX rate: see exchange rate.
FX rate risk: exposure to FX rate changes.
FX spot rate: see spot FX rate.
FX triangular arbitrage: arbitraging 3 FX pairs.
Gamma: the second derivative of the value of a derivative asset (e.g., option)
w.r.t. the price of the underlying asset.
Gamma hedging: an options hedging strategy to eliminate or reduce the ex-
posure caused by changes in an option portfolio’s Delta as a result of the underlying
security’s price movements.
Gamma scalping: Gamma hedging by buying and selling the underlying secu-
300
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 302

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
rity in response to its price movements that cause changes in an option portfolio’s
Delta.
global macro: trading strategies seeking to capitalize on regional, economic
and political changes around the world.
Greeks: see Delta, Gamma, Theta, Vega .
greenﬁeld project: a project associated with infrastructure assets to be con-
structed.
guaranteed loan: a loan guaranteed by a third party in case the borrower
defaults.
guts: an option trading strategy.
hard-to-borrow security: a security on a “Hard-to-Borrow List”, an inven-
tory record used by brokerages for securities that are diﬃcult to borrow for short
sale transactions due to short supply or high volatility.
headline inﬂation (HI): a measure of the total inﬂation within an economy,
including commodity prices such as food and energy (cf. core inﬂation).
heat rate: the eﬃciency with which an electricity production plant converts
fuel into electricity.
hedge: an investment (typically, via an oﬀsetting position in a related secu-
rity) to reduce the risk of losing money on an existing position.
hedge ratio: in a hedge, the number of units (or the dollar notional) of the
oﬀsetting security for each unit (or dollar) of the security to be hedged.
hedger: a market participant attempting to reduce risk associated with a secu-
rity’s price movement (cf. speculator).
hedging pressure (HP): in (commodities) futures markets, the number of
long contracts divided by the total number of contracts (long plus short).
hedging strategy: see hedge.
heterotic risk model: a multifactor risk model combining a multilevel fun-
damental industry classiﬁcation with principal component analysis.
301
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 303

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
hidden layers: in an artiﬁcial neural network, the intermediate layers of nodes
(artiﬁcial neurons) between the input layer and the output layer.
high (a.k.a. high price): the maximum price attained by a stock (or other
security) within a given trading day (or some other time interval).
high-minus-low carry: an FX trading strategy based on the forward discount
anomaly.
High Yield bonds (a.k.a. junk bonds): bonds with S&P credit ratings
below BBB-.
historical quantity: a quantity (e.g., correlation, variance, volatility, return,
etc.) computed based on historical data.
HMD (a.k.a. healthy-minus-distressed): buying the safest companies and
selling the riskiest ones by probability of bankruptcy.
HML (a.k.a. High minus Low): see Fama-French factors.
Hodrick-Prescott ﬁlter (a.k.a. HP ﬁlter, or Whittaker-Henderson method
in actuarial sciences): a time-series ﬁlter for separating a lower-frequency
(“regular”) component from a higher-frequency (“irregular”) component (noise).
holding period: the period for which a position in a security or a portfolio
is held after being established and before being liquidated (or, more loosely, rebal-
anced).
holding weights: the weights with which assets are held in a portfolio.
holdings: the contents of a portfolio; also, a shorthand for, e.g., dollar holdings.
horizon (a.k.a. investment horizon): see holding period.
horizontal spread (a.k.a. time spread): see calendar spread.
Hybrid Market: a blend of an automated electronic trading platform and
a traditional (human-operated) ﬂoor broker system.
hybrid security: a security with mixed characteristics of two asset classes,
e.g., a convertible bond.
IBS: internal bar strength, deﬁned as the diﬀerence between the close price
302
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 304

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
and the low price divided by the diﬀerence between the high price and the low price.
implied volatility: in option pricing, the volatility of the underlying instru-
ment, which, when used as an input in an option pricing model (such as the Black-
Scholes model), yields the model value of the option price equal to its market value.
imputation system: see dividend imputation.
in-sample: when a computation or backtest is not out-of-sample.
in-the-money (ITM) option: a call (put) option whose exercise price is below
(above) the current price of the underlying asset.
income strategy: a trading strategy that generates income, usually via some
risk exposure.
incomplete basket: a subset of the portfolio that would ideally be traded,
e.g., in index arbitrage.
index: a diversiﬁed portfolio of assets combined with some weights.
index arbitrage (a.k.a. cash-and-carry arbitrage): an arbitrage strategy
exploiting mispricings between the index spot price and index futures price (i.e., the
index futures basis).
index basket: an index portfolio.
index constituents: the assets in an index portfolio.
index ETF: an ETF that tracks an index.
index futures: a futures on an index.
index hedging: hedging a position (e.g., a CDO tranche) with a pertinent
index.
index level: for market cap weighted indexes, the current value of the in-
dex level I(t) = I(0)× C(t)/C(0), where I(0) is the initial value of the index level
(which is deﬁned, not calculated), C(t) is the current total market cap of the index
constituents, and C(0) is its initial value.
index spot price: the current market price of an index basket, where the
number of units of each constituent is determined by the index weighting scheme
303
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 305

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
(market cap weighted index, price weighted index, etc.) with the overall normal-
ization constant ﬁxed depending on a speciﬁc purpose, e.g., to match the index
portfolio to be delivered at the index futures delivery in the case of index arbitrage.
indexed payments: payments adjusted according to the value of some in-
dex, e.g., CPI in inﬂation swaps or TIPS.
industrial properties: commercial real estate properties including manufac-
turing buildings and property, warehouses, etc.
industry (in economy): a group of companies that are related based on their
primary business activities.
industry (in industry classiﬁcation): a grouping of companies based (among
other things) on which economic industry they belong to.
industry classiﬁcation: a taxonomy of companies (stocks) based on some
similarity criterion (or criteria), e.g., a company’s main source of revenues, how
closely stock returns follow each other historically, etc.
inﬂation: a sustained increase in the price level of goods and services in an
economy over a period of time, which is measured as an annual percentage change
known as the inﬂation rate.
inﬂation hedge: a hedge against inﬂation.
inﬂation index: e.g., CPI.
inﬂation-indexed product: a security (e.g., TIPS) with indexed payments
based on an inﬂation index.
inﬂation swap: a swap whose buyer is long the inﬂation and receives a ﬂoating
rate (based on an inﬂation index) and pays a ﬁxed rate (breakeven rate).
informed order ﬂow: see smart order ﬂow .
infrastructure funds: unlisted infrastructure funds (private equity-type in-
vestments), listed infrastructure funds (exchange-traded).
infrastructure investment: investing in long-term projects such as trans-
portation (roads, bridges, tunnels, railways, ports, airports, etc.), telecommunica-
tions (transmission cables, satellites, towers, etc.), utilities (electricity generation,
gas or electricity transmission or distribution, water supply, sewage, waste, etc.), en-
304
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 306

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ergy (including but not limited to renewable energy), healthcare (hospitals, clinics,
senior homes, etc.), educational facilities (schools, universities, research institutes,
etc.), etc.
input layer: in an artiﬁcial neural network, the layer of nodes (artiﬁcial neu-
rons) that processes the input data.
institutional trader: a trader who buys and sells securities for an account
of a group or institution such as a pension fund, mutual fund, insurance company,
ETF, etc.
integration: the ﬁnal step of the money laundering process whereby money
launderers get back the money via legitimate-looking sources.
intercept: in a linear regression, the regression coeﬃcient of the independent
variable (which is also colloquially referred to as the intercept) whose elements are
all equal 1.
interest: the amount paid by the borrower to the lender above the principal
(the actual amount borrowed).
interest rate: the interest per $1 of the principal.
interest rate futures: a futures contract typically with an array (delivery
basket) of underlying instruments (e.g., bonds) that pay interest.
interest rate risk (a.k.a. interest rate exposure): the exposure to in-
terest rate ﬂuctuations, which aﬀect bond and other ﬁxed-income asset prices.
interest rate spread: the diﬀerence between the interest rates paid by two
instruments.
interest rate swap: a contract that exchanges a stream of ﬂoating rate pay-
ments for a stream of ﬁxed rate payments or vice versa.
intra-asset diversiﬁcation: in real estate investments, diversiﬁcation by prop-
erty type (residential, commercial, etc.), economic diversiﬁcation (by diﬀerent re-
gions divided according to economic characteristics), geographic diversiﬁcation, etc.
intraday arbitrage: taking advantage of intraday mispricings, e.g., in ETFs
and stocks.
intraday signal: a trading signal used by an intraday strategy.
305
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 307

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
intraday strategy: a trading strategy that starts with a null position, buys
and sells/shorts securities intraday, and ends with a null position by the close (in
trader lingo, “goes home ﬂat”).
inverse ETF: an ETF designed to track the return inverse to its underlying
index.
inverse matrix: for an N× N square matrix A, the inverse matrix A−1 is
the N× N square matrix such that A A−1 = A−1 A = I, where I is the N× N
identity matrix (whose diagonal elements equal 1, and oﬀ-diagonal elements equal 0).
investment: allocating money with an expectation of a positive return.
Investment Grade bonds (a.k.a. IG bonds): bonds with S&P credit rat-
ings AAA through AA- (high credit quality) and A+ through BBB- (medium credit
quality).
investment vehicle: an investment product (e.g., ETF) used by investors for
generating positive returns.
iron butterﬂy: a type of option trading strategies.
iron condor: a type of option trading strategies.
iShares (ticker IVV): an S&P 500 tracking EFT.
Jensen’s alpha: an abnormal return of a security or portfolio, usually cal-
culated as the intercept coeﬃcient in a linear model, where excess returns of said
security or portfolio are serially regressed over excess returns of one or more factor
portfolios (e.g., MKT).
Joule: a unit of work, heat and energy in the International System of Units
(SI).
JPY: Japanese Yen, a unit of Japanese currency.
junior mezzanine tranche: the next (by increasing quality) tranche of a CDO
after the equity tranche.
k-nearest neighbor algorithm (a.k.a. KNN or k-NN): a statistical classiﬁ-
cation algorithm based on a similarity criterion such as distance, angle, etc., between
multi-dimensional vectors.
306
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 308

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Kalman ﬁlter: a time-series ﬁlter for separating signal from noise.
Kelly strategy: an allocation (betting) strategy based on maximizing the ex-
pectation of the logarithm of wealth.
keyword: in sentiment analysis (e.g., Twitter sentiment) using machine learning
techniques, a word in the learning vocabulary pertinent to the goal (e.g., predicting
stock or cryptocurrency price movements).
ladder (for bonds): a bond portfolio with (roughly) equal capital allocations
into bonds of a sizable number of diﬀerent (and usually approximately equidistant)
maturities.
ladder (for options): a vertical spread consisting of 3 options, all 3 are call
options or put options, 2 are long and 1 is short, or 1 is long and 2 are short.
Lagrange multiplier: when minimizing a (multivariate) function g(x) w.r.t. x
subject to a constraint h(x) = 0, an additional variable λ in the function ˜g(x, λ) =
g(x) + λ h (x), whose (unconstrained) minimization w.r.t. x and λ is equivalent to
the original constrained minimization problem.
layer: see input layer, output layer, hidden layer .
layering: the middle step in the money laundering process, which amounts
to moving the money around between diﬀerent accounts and even countries thereby
creating complexity and separating the money from its source by several degrees.
learning vocabulary: in sentiment analysis (e.g., Twitter sentiment) using
machine learning techniques, a set of keywords pertinent to the goal (e.g., predict-
ing stock or cryptocurrency price movements).
least squares: in regression analysis, minimizing the sum of squares of the
residuals (possibly, with nonuniform weights).
ledger: a book or other collection of ﬁnancial accounts and transaction records.
leg: a component in a trading portfolio, usually when a portfolio can be thought
of as consisting of a relatively small number of groupings (e.g., short leg and long
leg, referring to short and long positions, respectively).
LETF: leveraged (inverse) ETF, an ETF designed to track the return (inverse
to) n times the return of its underlying index, wheren is the leverage (usually, 2 or 3).
307
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 309

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
leverage: using borrowed funds to purchase an asset.
limit order: an order to buy or sell a stock (or other security) at a speci-
ﬁed price or better.
linear homogeneous constraint: for an N-vector xi (i = 1 , . . . , N), a con-
straint of the form ∑N
i=1 ai xi = 0, where at least some ai are nonzero.
linear regression (a.k.a. linear model): ﬁtting data for the observable
variable using a linear combination of some number of (linear or nonlinear) func-
tions of independent variables, with or without the intercept.
liquid asset: an asset that can be converted into cash quickly with minimal
transaction costs.
liquid U.S. stocks: a subset of U.S. listed stocks usually deﬁned using ADDV
and market cap ﬁlters (e.g., top 2,000 most liquid stocks by ADDV).
liquidation (for assets or portfolios): closing of the open positions.
liquidation (for companies): winding up (bringing to an end) a company’s
business and distributing its assets to claimants, usually when the company is in-
solvent.
liquidity: availability of liquid assets/funds.
loadings matrix: see factor loadings matrix .
loan: lending of money or another asset by one party (lender) to another (bor-
rower).
loan shark: a lender oﬀering a loan at excessively high interest rates.
loan-to-own strategy: ﬁnancing a distressed company via secured loans with
the view of obtaining equity with control rights if the company ﬁles for bankruptcy.
log: a logarithm (usually, unless speciﬁed otherwise, the natural logarithm).
log-return: the natural log of the ratio of an asset’s price at time t2 to its
price at time t1 (t2 > t1).
log-volatility: a standard deviation of the natural logarithms of prices.
308
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 310

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
logistic regression (a.k.a. logit model): a statistical model typically ap-
plied to a binary dependent variable.
long-only: a portfolio or strategy with only long holdings.
long-run mean: in a mean-reverting Ornstein-Uhlenbeck process, the mean
value of the state variable in the inﬁnite time limit.
long-short: a portfolio or strategy with both long and short holdings.
lookback (a.k.a. lookback period): the length of a time-series data sam-
ple used in a backtest or historical computation.
losers: stocks or other assets in a portfolio or trading universe that under-
perform based on some criterion (benchmark).
low (a.k.a. low price): the minimum price attained by a stock (or other
security) within a given trading day (or some other time interval).
low-volatility anomaly: an empirical occurrence that future returns of pre-
viously low-return-volatility portfolios outperform those of previously high-return-
volatility portfolios.
Macaulay duration: a weighted average maturity of a bond’s cash ﬂows, where
the weights are the present values of said cash ﬂows.
machine learning (ML): a method of data analysis that automates predic-
tive analytical model building based on the premise that computational systems
can “learn” from data, identify patterns and make decisions with minimal human
intervention.
macro: macro trading strategies.
Manhattan distance: the distance between two vectors deﬁned as the sum
of the absolute values of the diﬀerences between their components.
margin account: a brokerage account in which the broker lends the customer
cash to purchase securities.
mark-to-market (MTM): valuing assets or portfolios based on the most re-
cent pertinent market prices.
309
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 311

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
market: a medium that allows buyers and sellers to interact to facilitate an
exchange of securities, commodities, goods, services, etc.
market beta: a measure of the volatility (systematic risk) of an asset or port-
folio in comparison to the broad market.
market capitalization (a.k.a. market cap, or cap): the market value
of a company’s shares outstanding.
market crash: a sudden dramatic decline of asset prices across their signiﬁ-
cant cross-section.
market data: price and trade-related data for a ﬁnancial security reported
by a trading exchange (or similar).
market-making: providing liquidity by simultaneously quoting both buy and
sell prices in a ﬁnancial instrument or commodity held in inventory with the view
of making a proﬁt on the bid-ask spread.
married call: see protective call.
married put: see protective put.
maturity (a.k.a. maturity date, or maturity time): the time at which
a ﬁnancial instrument will cease to exist and any principal and/or interest are re-
paid in full.
mean: an average value.
mean-reversion eﬀect (a.k.a. mean-reversion, or contrarian eﬀect): a
tendency of asset prices and/or their returns to revert to their mean values, which
mean values can be serial and/or cross-sectional, depending on the context.
mean-reversion parameter: in a mean-reverting Ornstein-Uhlenbeck process,
the parameter that controls the rate of mean-reversion.
mean-reversion strategy: a trading strategy based on a mean-reversion eﬀect.
mean-variance optimization: an optimization technique for constructing a
portfolio of assets such that its expected return is maximized for a given level of its
risk.
Megawatt: 1,000,000 watts.
310
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 312

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Megawatt hour (Mwh): 1,000,000 watts times 1 hour, which equals 3 .6× 109
Joules.
merger: a consolidation of two companies into one.
merger arbitrage (a.k.a. risk arbitrage): a trading strategy that attempts
to capture excess returns generated via corporate actions such as mergers and ac-
quisitions (M&A).
metropolitan statistical area (MSA): a core area containing a substantial
population nucleus, together with adjacent communities having a high degree of
economic and social integration with that core.
mini-S&P futures (a.k.a. e-mini): a futures contract on S&P 500 with
the notional value of 50 times the value of the S&P 500 stock index.
mishedge: an imperfect hedge, or when a hedge becomes undone (e.g., by
underlying price movements).
mispricing: an ineﬃciency in the pricing of a security, when its price does
not match its intrinsic value or (perceived) fair value.
MKT: see Fama-French factors.
modiﬁed duration: a measure of the relative bond price sensitivity to changes
in the interest rates, deﬁned as the negative ﬁrst derivative of the bond price w.r.t.
the bond yield.
MOM: see Carhart’s momentum factor .
momentum (a.k.a. momentum eﬀect): an empirical occurrence whereby
assets’ future returns are positively correlated with their past returns.
momentum strategy: a trading strategy based on momentum.
monetary policy: usually by a central bank, a process by which the mone-
tary authority of a country controls the size and rate of growth of the money supply,
via modifying the interest rates, buying or selling government bonds, and changing
the required bank reserves (the amount of money banks are required to keep in their
vaults).
money laundering: an activity wherein cash is used as a vehicle to trans-
311
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 313

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
form illegal proﬁts into legitimate-appearing assets.
moneyness: where a derivative contract’s strike price is in relation to its un-
derlying asset’s current price, which determines the derivative’s intrinsic value.
mortgage: a debt instrument, secured by a real estate property as a collateral,
that the borrower is obligated to pay back with a predetermined set of payments.
mortgage-backed security (MBS): an asset backed by a pool of mortgages.
moving average (a.k.a. rolling average): in a time series, an average (pos-
sibly computed with nontrivial weights) over a time interval of ﬁxed length (moving
average length), where the most recent time in said interval can take various values
in the time series.
moving standard deviation: in a time series, a standard deviation (possi-
bly computed with nontrivial weights) over a time interval of ﬁxed length, where
the most recent time in said interval can take various values in the time series.
multi-currency arbitrage: arbitraging 4 or more FX pairs.
multifactor risk model: a risk model based on a number (which can be siz-
able) of risk factors.
multifactor strategy: a trading strategy based on combining exposures to
multiple factors, e.g., momentum, value, etc. (multifactor portfolio).
multinomial probability distribution: a discrete probability distribution
of a random variable which takes k diﬀerent values with probabilities p1, . . . , pk.
municipal bond (a.k.a. muni bond): a bond issued by a local govern-
ment/territory or its agency.
municipal bond tax arbitrage: a trading strategy based on borrowing money
and buying tax-exempt municipal bonds.
mutual fund: an investment vehicle funded by a pool of money collected from
many investors for the purpose of buying various securities (stocks, bonds, money
market instruments, etc.).
naked call: a stand-alone short call option.
naked put: a stand-alone put call option.
312
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 314

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
near-month contract: see near-month futures.
near-month futures: see front-month futures.
neutral curve butterﬂy: a bond butterﬂy strategy with curve-neutrality.
neutral outlook: when a trader expects the market or a security to trade
around its current level.
no-risk-free-arbitrage condition: a condition that ensures that no risk-free
proﬁts can be made by a trading strategy (at least, in excess to the risk-free rate).
node: in an artiﬁcial neural network, an artiﬁcial neuron, which (using an acti-
vation function) processes a set of inputs and generates an output.
noise: in a ﬁnancial time series, random ﬂuctuations without any apparent
trend.
non-announcement days: days without any important economic announce-
ments such as FOMC announcements (cf. announcement days).
non-deliverable bond: a bond not in the delivery basket of an interest rate
futures contract.
non-directional strategy (a.k.a. neutral strategy): a strategy not based
on the underlying security’s (or securities’) future direction, so the trader is oblivi-
ous to whether its price goes up or down (cf. directional strategy).
non-discretionary strategy: a trading strategy based on a systematic ap-
proach (as opposed to discretionary).
non-systematic risk: speciﬁc (a.k.a. idiosyncratic) risk, which is speciﬁc to
each company, asset, etc., and exposure to which can be reduced via diversiﬁcation,
albeit never completely eliminated (cf. systematic risk).
nonlinear least squares: least squares used to ﬁt a set of observations with a
model that is nonlinear in the unknown parameters (regression coeﬃcients).
notional (a.k.a. notional value): the total (dollar) value of a position.
objective function: a function to be maximized or minimized in optimiza-
tion.
313
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 315

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
open (a.k.a. open price, or opening price): the opening price of a stock at
the NYSE open (9:30 AM Eastern Time).
open interest (a.k.a. open contracts, or open commitments): the total
number of open futures (or options) contracts at any given time (i.e., those contracts
that have not been settled).
optimal hedge ratio: a hedge ratio calculated by minimizing the variance
of a hedged portfolio.
optimization: see portfolio optimization.
option: a ﬁnancial derivative contract that gives the buyer (option holder) the
right (but not the obligation) to buy (call option) or sell (put option) the underlying
asset at an agreed-upon price during a predeﬁned period of time or on a speciﬁc date.
option-adjusted spread (OAS): a parallel shift in the Treasury curve (or
some other benchmark yield curve) that matches a security’s price calculated based
on a pricing model to its market value, with the view to account for the security’s
embedded options.
option premium: the cost charged by the option seller to the option buyer.
option writer: an option seller.
order: an investor’s instructions to a broker or brokerage ﬁrm to purchase or
sell a security.
order execution system: a software component that executes trades based
on input buy and/or sell order sequences.
Ornstein-Uhlenbeck process: Brownian motion with mean-reversion.
orthogonality: vectors xi and yi (i = 1, . . . , N) are orthogonal if∑N
i=1 xi yi = 0.
out-of-sample backtest: a backtest in which all quantities used for estab-
lishing or liquidating simulated positions corresponding to any given time t are
computed using historical quantities from times prior to t.
out-of-sample computation: a computation where all quantities to be used
for forecasting purposes at any given simulated time t are computed using historical
quantities from times prior to t.
314
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 316

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
out-of-the-money (OTM) option: a call (put) option whose exercise price is
above (below) the current price of the underlying asset.
outcome (a.k.a. class): in machine learning, one of the possible results (out-
puts, predictions) of a machine learning algorithm.
output gap: the diﬀerence between the actual output of an economy and its
maximum potential output as a percentage of GDP.
output layer: in an artiﬁcial neural network, the layer of nodes (artiﬁcial neu-
rons) that generates the output data (the result).
over-ﬁtting: in a statistical model, ﬁtting more free parameters than justi-
ﬁed by the data, thereby (often unwittingly) essentially ﬁtting noise and rendering
the model unpredictive out-of-sample.
overnight return: broadly, a return from some time during the previous trad-
ing day to some time during the current day (e.g., close-to-open return, close-to-close
return); usually, close-to-open return.
overreaction: in ﬁnancial markets, an irrational response by market partici-
pants (based on greed or fear) to new information.
pairs trading: a mean-reversion strategy involving two historically correlated
assets.
parallel shift: in a yield curve, all interest rates for all maturities changing
by the same amount.
passive investing: a longer-horizon, essentially buy-and-hold, investment strat-
egy with the view of minimizing transaction costs and replicating the performance
of a (typically, well-diversiﬁed) benchmark portfolio.
passive limit order: a liquidity-providing limit order to buy at the bid (or
lower) or sell at the ask (or higher).
passive trading strategy: a trading strategy based on the passive invest-
ing approach.
passthrough MBS: an MBS where cash ﬂows are passed from debtors to in-
vestors through an intermediary.
315
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 317

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
pawnbroker: a lender that extends a secured cash loan with pre-agreed in-
terest and period (which can sometimes be extended), where the loan is secured
with a collateral (forfeited if the borrower defaults), which is some valuable item(s),
such as jewelry, electronics, vehicles, rare books or musical instruments, etc.
payment period: the period between two consecutive bond coupon payments.
payoﬀ: the amount the option seller pays to the option buyer if and when
the option is exercised.
peer-to-peer (P2P) network: a distributed computing application architec-
ture with workload partitioned between equally privileged peers.
pension fund: a pool of funds that provides retirement income.
performance characteristics: for a portfolio or strategy, characteristics such
as return-on-capital, Sharpe ratio, cents-per-share, maximum drawdown, etc.
periodic compounding: compounding with equal compounding periods, e.g.,
quarterly, semiannual or annual compounding.
physical commodity: the actual commodity (e.g., copper) that is delivered
to a commodity futures contract buyer at the expiration.
pivot point (a.k.a. center): in support and resistance strategies, a deﬁnition-
dependent quantity, e.g., deﬁned as the equally weighted average of the previous
trading day’s high, low and close prices.
placed order: an order that has been submitted to an exchange and placed
in a queue for execution.
placement: the initial stage in the money laundering process, whereby ille-
gal funds are introduced into the legal economy via fraudulent means.
Porter stemming algorithm: an algorithm for reducing words to their base
form (stemming).
portfolio: a collection of assets held by an institution or individual investor.
portfolio diversiﬁcation: see diversiﬁcation.
portfolio optimization: selecting the best portfolio based on some criterion
(e.g., maximizing the Sharpe ratio).
316
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 318

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
portfolio weights: the relative percentages of the dollar holdings in a portfolio
to its total notional value (deﬁned as the total notional value of the long positions
plus the total absolute notional value of the short positions).
position: the amount of stock or other security held, expressed in dollars,
shares, or some other units, with short positions possibly having negative values
depending on a convention used.
position bounds: upper or lower bounds on the dollar holdings of various
assets in a portfolio.
predicted class: in machine learning, the outcome predicted by an algorithm.
predictor (a.k.a. predictor variable): in machine learning, an input variable.
premium (for insurance-type products): a periodic payment for insurance
coverage, e.g., in a CDS, CDO, etc.
premium (for options): the cost of buying an option.
premium leg: the leg of a CDO corresponding to the CDO premiums, the
other leg being the default leg.
prepayment: settling a debt or installment payment before its due date (e.g.,
mortgage prepayment).
prepayment risk: the main risk to investors in a passthrough MBS whereby
homeowners have an option to prepay their mortgages (e.g., by reﬁnancing their
mortgages as the interest rates drop).
price-momentum strategy: a momentum strategy where the momentum in-
dicator is based on past returns.
pricing data: historical and real-time data containing prices, trading volumes
and related quantities (see market data).
pricing model: a model for valuing (pricing) a security or a set of securi-
ties.
principal: the amount the debt issuer (borrower) owes the lender at debt ma-
turity.
317
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 319

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
principal component: for a symmetric square matrix, an eigenvector thereof
normalized such that the sum of squares of its components equals 1, with diﬀerent
principal components ordered in the descending order by the corresponding eigen-
values.
principal component analysis (PCA): a mathematical procedure that trans-
forms some number of (typically, correlated) variables into a (typically, smaller)
number of uncorrelated variables (principal components), with the ﬁrst principal
component accounting for as much of the variability in the data as possible, and
each succeeding principal component accounting for as much of the remaining vari-
ability as possible.
probability distribution: a function that provides the probabilities of oc-
currence of diﬀerent possible outcomes.
probability measure: a real function valued in the interval between 0 and
1 (0 corresponding to the empty set and 1 corresponding to the entire space) de-
ﬁned on a set of events in a probability space that satisﬁes the countable additivity
property, i.e., simply put, that the probability of a union of disjoint events A and B
equals the sum of their probabilities.
protection buyer: a buyer of insurance.
protection seller: a seller of insurance.
protective call (a.k.a. married call, or synthetic put): hedging a short
stock position with a long call option position.
protective put (a.k.a. married put, or synthetic call): hedging a long
stock position with a long put option position.
publicly traded company (a.k.a. public company): a company whose
shares are freely traded on a stock exchange or in over-the-counter markets.
put-call parity: the relationship whereby the payoﬀ of a European call op-
tion (with a strike price K and expiration T ) minus the payoﬀ of a European put
option (on the same underlying and with the same strike and expiration) equals the
payoﬀ of a forward contract (on said underlying) with the strike K and expiry T .
put option (a.k.a. put): see European put option, option .
quantile: each of the n (approximately) equal parts of a sample (e.g., data
sample), where n > 1.
318
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 320

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
quantitative trading: systematic trading strategies based on quantitative anal-
ysis and mathematical computations with little to no human intervention outside of
developing a strategy (which includes coding it up in a suitable computer language).
quark spread: the analog of the spark spread and the dark spread for nu-
clear power plants.
quintile: each of the 5 (approximately) equal parts of a sample (e.g., data
sample).
R: R Package for Statistical Computing.
R-squared: in a regression, 1 minus a ratio, whose numerator is the sum of
squares of the residuals, and whose denominator is the sum of squares of the devia-
tions of the values of the observable variable from their mean value across the data
sample.
rally: in ﬁnancial markets, a period of sustained gains.
rank (for matrices): the maximum number of linearly independent columns
of a matrix.
rank (a.k.a. ranking): the position of an element of a set after sorting it
according to some criterion (with a prescription for resolving possible ties).
rate: see interest rate, inﬂation.
rating: see credit rating.
ratio spread: a type of options strategies.
real estate: tangible immovable assets including land, structures built on it, etc.
real estate investment trust (REIT): a company (often traded on major
exchanges and thus allowing investors to take a liquid stake in real estate) that
owns, operates or ﬁnances income-producing real estate.
real interest rate: interest rate adjusted for inﬂation.
realized P&L: the P&L on a completed trade, i.e., the P&L resulting from
establishing a position and then completely liquidating it.
319
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 321

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
realized proﬁt: see realized P&L.
realized return: historical return.
realized volatility: historical volatility.
rebalancing: changing the holding weights in a portfolio.
recovery rate: the percentage of the principal and accrued interest on de-
faulted debt that can be recovered.
rectiﬁed linear unit (ReLU): the function of x given by max(x, 0).
reference entities: in a CDS, bonds, loans, names of companies or countries,
etc., on which default protection is provided.
regression: see linear regression.
regression coeﬃcient: the slope of an independent variable in a linear re-
gression.
regression residuals: the diﬀerences between the observed values and the ﬁt-
ted (model predicted) values of the dependent variable in a linear regression.
regression-weighted butterﬂy: a type of bond butterﬂy portfolio.
regression weights: the positive weights wi (which need not equal 1) in the
sum of squares∑N
i=1 wi ϵ2
i , whose minimization determines the regression coeﬃcients
and regression residuals ϵi.
reinvestment risk: the risk that the proceeds (from the coupon payments
and/or principal of a bond or similar instrument) would be reinvested at a lower
rate than the original investment.
relative momentum: cross-sectional momentum.
relative strength index (RSI): during a speciﬁed timeframe, the average
gain of the up periods divided by the sum of the average gain of the up periods and
the absolute value of the average loss of the down periods.
relative value strategy: a strategy that aims to exploit diﬀerences in the
prices, returns or rates (e.g., interest rates) of related (by some criterion) securities
(e.g., historically correlated stock pairs in pairs trading).
320
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 322

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
reorganization: a Court-supervised process of restructuring a company’s ﬁ-
nances in bankruptcy.
reorganization plan: a plan for reorganization of a company in bankruptcy
that can be submitted (e.g., by a creditor with the view of obtaining participation
in the management of the company) to Court for approval.
replication: a strategy whereby a dynamic portfolio of assets precisely repli-
cates cash ﬂows of another asset or portfolio.
repurchase agreement (a.k.a. REPO or repo): a cash-equivalent asset
that provides immediate liquidity at a preset interest rate for a speciﬁc period of
time in exchange for another asset used as a collateral.
resistance: in technical analysis, the (perceived) price level at which a ris-
ing stock price is expected to bounce back down.
retail trader: a non-professional individual trader.
reverse repurchase agreement: a REPO from the standpoint of the lender.
rich stock: a stock that is perceived to be overvalued by some criterion.
risk: the possibility that the realized return will diﬀer from the expected re-
turn.
risk-adjusted return: return divided by volatility.
risk arbitrage: see merger arbitrage.
risk factor: see factor.
risk-free arbitrage: making proﬁt without any risk.
risk-free asset (a.k.a. riskless asset): an asset with a certain future re-
turn, e.g., Treasury bills.
risk-free discount factor: a discount factor that uses a risk-free rate for dis-
counting future cash ﬂows.
risk-free probability measure (a.k.a. risk-neutral measure): a theo-
retical probability measure under which an asset’s current price equals its future
321
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 323

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
expected value discounted by a risk-free rate.
risk-free rate: the rate of return of a risk-free asset, often taken to be the
one-month Treasury bill rate.
risk management: identifying, analyzing and mitigating potential risks.
risk model: a mathematical model for estimating risk (e.g., modeling a co-
variance matrix).
risk premia (same as risk premiums): plural of risk premium.
risk premium: the (expected) return in excess of the risk-free rate from an
investment.
risk reversal (a.k.a. combo): a type of options strategies.
risk sentiment: investor risk tolerance in response to global economic pat-
terns, whereby when risk is perceived as low (high), investors tend to engage in
higher-risk (lower-risk) investments (a.k.a. “risk-on risk-oﬀ”).
risky duration: a weighted sum (over the payment dates) of the (discounted)
diﬀerences between the notional (of a CDO tranche or similar) and expected loss
for each such date, where each weight is the time from the previous payment date.
roll: in futures contracts, rebalancing futures positions, whereby when the cur-
rent long (short) futures contract is about to expire, it is sold (covered) and another
futures contract with longer expiration is bought (sold).
roll loss (a.k.a. contango loss): in ETNs such as VXX and VXZ consisting
of VIX futures portfolios, a decay in their values (when the VIX futures curve is
in contango) due to their daily rebalancing required to maintain a constant maturity.
roll value: see daily roll value .
roll yield: in commodity futures, positive returns from the roll generated by
long (short) positions when the term structure is in backwardation (contango).
rolling down the yield curve (a.k.a. rolling down the curve): a trading
strategy that amounts to buying long- or medium-term bonds from the steepest
segment of the yield curve (assuming it is upward-sloping) and selling them as they
approach maturity.
322
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 324

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
root mean square error (RMSE): the square root of the mean value of the
squares of the diﬀerences between the predicted and observed values of a variable.
rotation: see alpha rotation, sector momentum rotation .
rung: in a bond ladder portfolio, the bonds of the same maturity.
Russell 3000: a market cap weighted index of the 3,000 largest U.S.-traded
stocks by market cap.
S&P 500: a market cap weighted index of the 500 largest U.S. publicly traded
companies by market cap.
sample correlation matrix: a correlation matrix for a set of securities com-
puted based on the time series of their historical returns.
sample covariance matrix: a covariance matrix for a set of securities com-
puted based on the time series of their historical returns.
sample variance: a variance computed based on the time series of a secu-
rity’s historical returns.
scale invariance: a function f(xi) of N variables xi (i = 1 , . . . , N) is scale
invariant if f(ζxi) = f(xi) for an arbitrary scale factor ζ taking values in a contin-
uous interval (e.g., positive real values).
seagull spread: a type of options strategies.
second-month futures: a futures contract with the nearest expiration after
the front-month futures.
sector (in economy): an area of the economy in which businesses share similar
products or services.
sector (in industry classiﬁcation): usually, the least granular level in a mul-
tilevel industry classiﬁcation (e.g., sectors are split into industries, industries are
split into sub-industries).
sector momentum rotation: a type of momentum strategy for ETFs.
secured loan: a loan secured with a collateral.
security: in ﬁnance, usually a fungible, negotiable ﬁnancial instrument with
323
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 325

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
monetary value.
selectivity: a quantitative measure of active management of mutual funds (as
well as actively-managed ETFs).
sell-write strategy: shorting stock and writing (selling) a put option against
the stock position.
senior mezzanine tranche: the next (by increasing quality) tranche of a CDO
after the junior mezzanine tranche.
senior tranche: the next (by increasing quality) tranche of a CDO after the
senior mezzanine tranche.
sentiment analysis (a.k.a. opinion mining): the use of natural language
processing and other computational techniques to extract information from (elec-
tronic) documents (e.g., tweets) pertinent to a security, e.g., for forecasting the
direction of its price movements.
sentiment data: the textual data used in sentiment analysis (e.g., the con-
tents of tweets).
Separate Trading of Registered Interest and Principal of Securities (a.k.a.
STRIPS): zero-coupon Treasury securities.
serial correlation: a pair-wise correlation between two securities computed
based on their time series of historical returns.
serial quantity: a quantity (e.g., mean, standard deviation, etc.) computed
serially (i.e., across the time series for each security) as opposed to cross-sectionally
(i.e., across a set of securities).
serial regression: a regression where the independent variables are time se-
ries (cf. cross-sectional regression).
settlement: the fulﬁllment of the obligations under a futures or forward con-
tract at expiration.
share: a unit of ownership interest in a corporation or ﬁnancial asset.
shareholder (a.k.a. stockholder): an owner of shares in a company.
shares outstanding: the total number of a company’s shares held by all its
324
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 326

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
shareholders.
Sharpe ratio: (excess) return divided by volatility.
short position (a.k.a. short): selling an asset without owning it by bor-
rowing it from someone else, typically, a brokerage ﬁrm.
short-sale (a.k.a. short-selling, or shorting): establishing a short posi-
tion.
sideways market: when prices remain in a tight range, without clear up or
down trends.
sideways strategy: a trading strategy that aims to capitalize on an expected
low volatility environment, e.g., by selling volatility.
sigmoid: the function of x given by 1/(1 + exp(−x)).
signal: a trading signal, e.g., to buy (buy signal) or sell (sell signal) a secu-
rity.
simple moving average (SMA): a moving average without suppressing past
contributions (cf. exponential moving average).
simple moving standard deviation: a moving standard deviation without
suppressing past contributions (cf. exponential moving standard deviation ).
single-name CDS: a CDS on a single reference entity.
single-stock option: an option on a single underlying stock (as opposed to,
e.g., an option on a portfolio of stocks such as an index).
single-stock strategy: a trading strategy that derives a trading signal for
any given stock using data for only that stock and no other stocks.
skewness: a measure of asymmetry in a probability distribution, deﬁned as
the mean value of the cubic power of the deviation from the mean divided by the
cubic power of the standard deviation.
skewness premium: in commodity futures, an empirical occurrence whereby
future expected returns tend to be negatively correlated with the skewness of his-
torical returns.
325
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 327

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
skip period: in price-momentum and similar strategies, the period (usually,
the last 1 month) skipped before the formation period (usually the last 12 months
prior to the skip period).
slippage: the diﬀerence between the price at which an (initial) order is placed
(or expected/hoped to be executed) and at which it is ﬁlled (including after cancel-
replacing the initial order when chasing the bid or ask with buy or sell limit orders,
respectively), sometimes averaged over multiple orders (e.g., when a large order is
broken up into smaller ones).
smart order ﬂow (a.k.a. toxic order ﬂow): order ﬂow based on some
predictive expected return.
SMB (a.k.a. Small minus Big): see Fama-French factors.
social media sentiment: the sentiment on stocks or other securities extracted
from social media posts or messages (e.g., on Twitter).
softmax: the function exp( xi)/∑N
j=1 exp(xj) of an N-vector xi (i = 1, . . . , N).
sorting: organizing a set in an ascending or descending order based on some
quantity (with a prescription for resolving possible ties).
source code (a.k.a. code): computer code written in some computer pro-
gramming language.
sovereign risk: the risk that a government could default on its debt (sovereign
debt, e.g., government-issued bonds) or other obligations, or that changes in a cen-
tral bank’s policy may adversely aﬀect FX contracts.
spark spread: the diﬀerence between the wholesale price of electricity and
the price of natural gas required to produce it.
SPDR Trust (ticker SPY): an S&P 500 tracking EFT.
specialist system: a (largely) human-controlled and operated market-making
system at NYSE prior to switching to (mostly) electronic trading.
speciﬁc risk (a.k.a. idiosyncratic risk): see non-systematic risk.
speculative asset: an asset with little to no intrinsic value.
speculative bubble: see bubble.
326
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 328

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
speculator: a market participant attempting to proﬁt from a security’s price
movement (cf. hedger).
spike: a relatively large upward or downward movement of a security’s price
in a short period of time.
split (a.k.a. stock split): a corporate action in which a company divides
its existing shares into multiple shares (forward stock split) or combines multiple
shares into one (reverse stock split).
spot (a.k.a. spot price, or spot value): the current price of an asset.
spot FX rate (a.k.a. FX spot rate, or spot rate): the current FX rate.
spread: the diﬀerence between two quantities, or a portfolio consisting of two
(or more) legs comprised of the same type of assets diﬀerent only by one or more
speciﬁc quantities (e.g., strike price, or strike price and expiration).
standard deviation: the square root of the variance.
standardized unexpected earnings (SUE): a ratio, whose numerator (un-
expected earnings) is the diﬀerence between the most recently announced quarterly
earnings per share and those announced 4 quarters ago, and whose denominator is
the standard deviation of the unexpected earnings over the last 8 quarters.
state variable: one of a set of variables (which may or may not be observ-
able) used to describe a dynamical system.
statistical arbitrage (a.k.a. Stat Arb, or StatArb): typically, shorter-
horizon trading strategies with sizable trading universes (e.g., a few thousand stocks)
based on complex cross-sectional (and serial) statistical mean-reversion signals.
statistical industry classiﬁcation: a multilevel clustering of companies based
on purely statistical techniques, e.g., distance-based clustering of the companies’ re-
turns (cf. fundamental industry classiﬁcation ).
statistical risk model: a risk model built using only the pricing data (e.g.,
using principal components of the sample correlation matrix of stock returns), with-
out any reference to fundamental data (including any fundamental industry classi-
ﬁcation).
steepener: a yield curve spread bond strategy.
327
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 329

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
stemming: reducing a word to its base form, the part of a word that is common
to all its inﬂected variants.
stemming algorithm: see Porter stemming algorithm .
stochastic dynamics: see stochastic process.
stochastic gradient descent (SGD): an iterative method for optimizing a
diﬀerentiable objective function.
stochastic process: a collection of random variables that change with time.
stock: a security representing fractional ownership in a corporation.
stock merger: a merger where each share of the target company is swapped
for some number (which can be fractional) of the acquirer company’s shares.
stop-loss price: the price of an asset at which a position in said asset is (auto-
matically) liquidated.
stop-word: the most commonly used words in a language (e.g., “the”, “is”,
“in”, “which”, etc.) that add no value in a particular context and are ignored by a
natural language processing tool.
straddle: an option trading strategy.
strangle: an option trading strategy.
strap: an option trading strategy.
strategy: see trading strategy.
strike price (a.k.a. strike): the price at which a derivative contract can
be exercised.
strip: an option trading strategy.
structured asset: a complexly structured (debt) instrument such as a CDO or
ABS.
style risk factor (a.k.a. style factor): risk factors such as value, growth,
size, momentum, liquidity and volatility.
328
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 330

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
sub-industry (in industry classiﬁcation): usually, a subgroup of compa-
nies within the same industry grouped together based on a more granular criterion.
super senior tranche: the highest quality tranche of a CDO.
support: in technical analysis, the (perceived) price level at which a falling
stock price is expected to bounce back up.
support and resistance strategy: a technical analysis strategy based on
support and resistance.
support vector machine (SVM): in machine learning, a type of supervised
learning models.
swap (a.k.a. swap agreement, or swap contract): a derivative contract
through which two parties exchange ﬁnancial instruments.
swap spread: the diﬀerence between the ﬁxed rate of an interest rate swap
and the yield on a Treasury security with a similar maturity.
swap-spread arbitrage: a dollar-neutral strategy consisting of a long (short)
position in an interest rate swap and a short (long) position in a Treasury bond with
the same maturity as the swap.
synthetic security (a.k.a. synthetic): a ﬁnancial instrument created (via
a portfolio of assets) to replicate (or approximately reproduce) the same cash ﬂows
as another security (e.g., synthetic put, call, straddle, forward, futures, etc.).
systematic approach: methodical, rules-based trading strategies with well-
deﬁned trade goals and risk controls (as opposed to, e.g., analysts’ subjective opin-
ions).
systematic macro: non-discretionary, systematic macro trading strategies.
systematic risk: non-diversiﬁable risk inherent to the entire market or its
segment, such as exposure to broad market movements, which cannot be diversiﬁed
away in long-only portfolios, but can nonetheless be substantially reduced or even
essentially eliminated in long-short (e.g., dollar-neutral) portfolios.
tactical asset allocation: a dynamic investment strategy that actively ad-
justs a portfolio’s asset allocation weights.
329
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 331

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
tanh: hyperbolic tangent.
target company: the company chosen by the acquirer company for a potential
corporate merger or acquisition.
target variable: in machine learning, the variable whose values are to be mod-
eled and predicted.
tax arbitrage: proﬁting from diﬀerences in how income, capital gains, transac-
tions, etc., are taxed.
tax credit: see dividend imputation.
tax-exempt municipal bonds: e.g., municipal bonds that are not subject
to Federal income taxes (on the interest earned) in the U.S.
tax shield: the reduction in income taxes that results from taking an allow-
able deduction from taxable income.
technical analysis: a methodology for forecasting the direction of prices using
historical market data, primarily price and volume (cf. fundamental analysis).
technical indicator: a mathematical quantity used in technical analysis.
tercile: each of the 3 (approximately) equal parts of a sample (e.g., data sample).
term spread: an interest rate spread corresponding to two diﬀerent maturi-
ties.
term structure (in futures): the dependence of futures prices on time to
maturity.
term structure (in interest rates): see yield curve.
Theta: the ﬁrst derivative of the value of a derivative asset (e.g., option) w.r.t.
time.
Theta-decay: the time decay of an option’s (or other asset’s) value as time
nears the expiration.
ticker (a.k.a. ticker symbol): a short character string representing a par-
ticular publicly traded security.
330
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 332

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
time series: a series of data points indexed in time order, i.e., labeled by
time values.
time-to-maturity (TTM): time left before an option expires.
TIPS-Treasury arbitrage: a trading strategy consisting of selling a T-bond
and oﬀsetting the short position by a lower-cost replicating portfolio consisting of
TIPS, inﬂation swaps and STRIPS.
Treasury Inﬂation-Protected Securities (TIPS): Treasury securities that
pay semiannual ﬁxed coupons at a ﬁxed rate, but the coupon payments (and prin-
cipal) are adjusted based on inﬂation.
tracking error: the square root of the variance of the diﬀerences between the
returns of a portfolio and those of the benchmark or index said portfolio is meant
to mimic or beat.
tracking ETF: an ETF that tracks an index.
trader: a person who buys and sells goods, currency, stocks, commodities, etc.
trading bounds: upper or lower bounds on the dollar amounts of allowed
trades for various assets in a portfolio, when establishing, rebalancing or liquidating.
trading on economic announcements: a trading strategy that buys stocks
on important announcement days, such as FOMC announcements, while holding
risk-free assets on other days.
trading costs (a.k.a. transaction costs): costs associated with trading secu-
rities, including (as applicable) exchange fees, brokerage fees, SEC fees, slippage, etc.
trading days: usually, the days on which NYSE is open.
trading rule: a set of buy and sell instructions, with the quantities of the
assets to be bought or sold.
trading signal: see signal.
trading strategy: a set of instructions to achieve certain asset holdings by
some predeﬁned times t1, t2, . . ., which holdings can (but need not) be null at one
or more of these times.
trading universe (a.k.a. universe): the tickers of stocks (or other securi-
331
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 333

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ties) in a trading portfolio.
traditional assets: stocks, bonds, cash, real estate and, in some cases, also
currencies and commodities.
training: in machine learning, ﬁxing free parameters in an algorithm using
training data.
training data (a.k.a. training dataset): in machine learning, a set of input-
output pairs known in advance, which are used to train a machine learning algorithm.
training period: in machine learning, the period spanned by the training data
when it is a time series.
tranche: see CDO tranche.
Treasuries: Treasury securities.
Treasury: the U.S. Department of Treasury.
Treasury bill (a.k.a. T-bill): a short-term debt obligation issued by the
U.S. Treasury with maturity under 1 year.
Treasury bond (a.k.a. T-bond): a bond issued by the U.S. Treasury with
maturity of more than 10 years.
Treasury curve: the yield curve of Treasury securities.
Treasury ETF: a tracking ETF for an index composed of U.S. government
debt obligations.
Treasury note (a.k.a. T-note): a debt security issued by the U.S. Trea-
sury with maturity between 1 and 10 years.
tree boosting: a machine learning technique.
trend: the general direction of a market or asset’s price, essentially, momentum.
trend following: a trading strategy that aims to capture gains from an as-
set’s momentum in a particular direction.
triangular arbitrage: see FX triangular arbitrage .
332
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 334

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Twitter sentiment: the sentiment on stocks or other securities extracted from
tweets.
U.S. regions: East, Mid-West, South and West.
unadjusted quantity: price or volume unadjusted for splits or dividends.
uncompounded rate: an interest rate applied to the principal during some
period without any compounding.
underlying: underlying instrument (e.g., stock in a single-stock option).
underreaction: in ﬁnancial markets, an insuﬃcient response to news, as some
market participants tend to be conservative and rely too much on their prior beliefs.
unexpected earnings: see standardized unexpected earnings.
value: a factor based on the book-to-price (B/P) ratio.
value strategy: buying high value (high B/P ratio) stocks and selling low
value (low B/P ratio) stocks.
variable coupon bond: see ﬂoating coupon bond.
variable rate: see ﬂoating interest rate.
variance: a mean value of the squares of the deviations of the values of a
quantity from their mean value.
variance swap: a derivative contract whose payoﬀ at maturity is a product
of a preset coeﬃcient (variance notional) times the diﬀerence between the realized
variance at maturity of the underlying and the preset variance strike.
Vega: the ﬁrst derivative of the value of a derivative asset (e.g., option) w.r.t.
the implied volatility of the underlying asset.
vertical spread: an option strategy that involves all identical put or all iden-
tical call options with the exception of their strike prices.
volatility: a statistical measure of the dispersion of returns for a security or
market index, which is expressed via the standard deviation or variance of said re-
turns.
333
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 335

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
VIX: CBOE Volatility Index, a.k.a. the “uncertainty index” or the “fear gauge
index”.
volatility carry strategy: a trading strategy consisting of shorting VXX and
oﬀsetting the short position with long VXZ (see volatility ETN ), generally with a
non-unit hedge ratio.
volatility ETN: an ETN that tracks VIX, e.g., VXX or VXZ.
volatility index: an index (e.g., VIX) that measures the market’s expectation
of future (30-day for VIX) volatility based on implied volatilities of the underlying
instruments (the S&P 500 stocks for VIX).
volatility risk premium: an empirical occurrence that implied volatility tends
to be higher than realized volatility most of the time.
volatility skew: an empirical occurrence whereby, with all else being equal,
the implied volatility for put options is higher than for call options.
volatility strategy: a trading strategy that aims to capitalize on an expected
high volatility environment, e.g., by buying volatility.
volatility targeting strategy: a trading strategy that aims to maintain a
constant volatility level (volatility target, or target volatility) by rebalancing be-
tween a risky asset and a risk-free asset.
volume: the number of shares or contracts traded in a security during some
period.
watt: a unit of power in the International System of Units (SI).
weather derivative: a derivative (e.g., option or futures) on a synthetic weather
index.
weather index: a synthetic index usually based on temperature, using, e.g.,
cooling-degree-days (CDD) and heating-degree-days (HDD).
weather risk: a risk stemming from businesses and sectors of the economy
being aﬀected by weather conditions.
weighted average: for N values xi (i = 1, . . . , N), the weighted mean given by
1
N
∑N
i=1 wi xi, where wi are the weights.
334
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 336

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
weighted regression: a linear regression with nonuniform regression weights.
weighting scheme: assigning portfolio weights according to some rule, e.g.,
by suppressing contributions of volatile stocks.
weights (in ANN): in an artiﬁcial neural network, the coeﬃcients of the inputs
in the argument of an activation function.
weights (in portfolios): see portfolio weights.
Whittaker-Henderson method: see Hodrick-Prescott ﬁlter.
wing: one of the 2 peripheral (by maturity in bond portfolios, and by strike
price in option portfolios) legs of a butterﬂy portfolio.
winners: stocks or other assets in a portfolio or trading universe that out-
perform based on some criterion (benchmark).
word (a.k.a. keyword): a keyword in a learning vocabulary.
year-on-year (YoY) inﬂation: annual inﬂation (cf. cumulative inﬂation).
year-on-year inﬂation swap: an inﬂation swap that references annual in-
ﬂation (cf. zero-coupon swap).
yield: see bond yield.
yield curve (a.k.a. term structure): the dependence of interest rates or
bond yields on maturities.
yield curve spread: the spread between shorter and longer maturity bonds
on the yield curve.
yield curve spread strategy: a bond strategy that makes a bet on the yield
curve spread (ﬂattener or steepener).
zero-cost strategy: a dollar-neutral strategy.
zero-coupon bond: see discount bond.
zero-coupon inﬂation swap: an inﬂation swap that has only one cash ﬂow
at maturity and references the cumulative inﬂation over the life of the swap (cf.
year-on-year inﬂation swap).
335
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 337

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Acronyms
ABS: asset-backed security.
ADDV: average daily dollar volume.
ANN: artiﬁcial neural network.
ATM: at-the-money.
B/P: book-to-price.
BA: banker’s acceptance.
BICS: Bloomberg Industry Classiﬁcation System.
bps: basis point.
BTC: Bitcoin.
Btu: British thermal unit.
CA: commodity allocation percentage.
CBOE: Chicago Board Options Exchange.
CD: certiﬁcate of deposit.
CDD: cooling-degree-days.
CDO: collateralized debt obligation.
CDS: credit default swap.
CFTC: U.S. Commodity Futures Trading Commission.
CI: core inﬂation.
CIRP: Covered Interest Rate Parity.
CME: Chicago Mercantile Exchange.
COT: Commitments of Traders.
336
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 338

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
CPI: Consumer Price Index.
CPS: cents-per-share.
CTA: commodity trading advisor.
DJIA: Dow Jones Industrial Average.
EMA: exponential moving average.
EMSD: exponential moving standard deviation.
ETF: exchange-traded fund.
ETH: Ethereum.
ETN: exchange-traded note.
EUR: euro.
FOMC: Federal Open Market Committee.
FX: foreign exchange.
GDP: Gross Domestic Product.
GICS: Global Industry Classiﬁcation Standard.
HDD: heating-degree-days.
HFT: high frequency trading.
HI: headline inﬂation.
HMD: healthy-minus-distressed.
HML: High minus Low.
HP: hedging pressure; Hodrick-Prescott.
IBS: internal bar strength.
337
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 339

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ITM: in-the-money.
JPY: Japanese Yen.
LETF: leveraged (inverse) ETF.
LIBOR: London Interbank Oﬀer Rate.
M&A: mergers and acquisitions.
MA: moving average.
ML: machine learning.
MBS: mortgage-backed security.
MBtu: 1,000 Btu.
MKT: market (excess) return.
MMBtu: 1,000,000 Btu.
MOM: Carhart’s momentum factor.
MSA: metropolitan statistical area.
MTM: mark-to-market.
Mwh: Megawatt hour.
NYSE: New York Stock Exchange.
OAS: option adjusted spread.
OTM: out-of-the-money.
P&L: proﬁt(s) and loss(es).
P2P: peer-to-peer.
PCA: principal component analysis.
REIT: real estate investment trust.
338
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 340

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ReLU: rectiﬁed linear unit.
REPO/repo: repurchase agreement.
RMSE: root mean square error.
RSI: relative strength index.
S&P: Standard and Poor’s.
SIC: Standard Industrial Classiﬁcation.
SMA: simple moving average.
SMB: Small minus Big.
SGD: stochastic gradient descent.
SS: sum of squares.
StatArb: statistical arbitrage.
STRIPS: Separate Trading of Registered Interest and Principal of Securities.
SUE: standardized unexpected earnings.
SVM: support vector machine.
TTM: time-to-maturity.
TIPS: Treasury Inﬂation-Protected Securities.
UIRP: Uncovered Interest Rate Parity.
USD: U.S. dollar.
VAR: vector autoregressive model.
VWAP: volume-weighted average price.
YoY: year-on-year.
339
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 341

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Some Math Notations
iﬀ if and only if.
max (min) maximum (minimum).
ﬂoor(x) the largest integer less than or equal x.
ceiling(x) the smallest integer greater than or equal x.
(x)+ max(x, 0).
sign(x) sign of x, deﬁned as: +1 if x > 0;−1 if x < 0; 0 if x = 0.
|x| absolute value of x if x is a real number.
rank(xi) rank of xi when N values xi (i = 1, . . . , N) are sorted in the ascending
order.
exp(x) or ex natural exponent of x.
ln(x) natural log of x.
∑N
i=1 xi sum of N values xi (i = 1, . . . , N).
∏N
i=1 xi product of N values xi (i = 1, . . . , N).
A|B=b (or A|b) the value of A when some quantity B it implicitly depends on
(usually evident from the context) takes value b.
f(x)→ min (max) minimizing (maximizing) f(x) w.r.t. x (where x can, e.g., be
an N-vector xi, i = 1, . . . , N).
argmaxz f(z) the value of z for which f(z) is maximized.
∂f /∂x the ﬁrst partial derivative of the function f (which may depend on vari-
ables other than x) w.r.t. x.
∂2f /∂x2 the second partial derivative of the function f (which may depend on
variables other than x) w.r.t. x.
G : A↦→ B G is a map from set A to set B.
340
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 342

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
A⊂ B set A is a subset of set B.
{i|f(i) = a} the set of values of i such that the condition f(i) = a is satis-
ﬁed.
min(i : f(i) > a ) the minimum value of i such that the condition f(i) > a
is satisﬁed.
i∈ J i is an element of set J.
|J| the number of elements of J if J is a ﬁnite set.
δAB (or δA,B) 1 if A = B; otherwise, 0 (Kronecker delta).
diag(xi) diagonal N× N matrix with xi (i = 1, . . . , N) on its diagonal.
AT transpose of matrix A.
A−1 inverse of matrix A.
Et(A) expected value of A at time t.
dX(t) an inﬁnitesimal increment of a continuous process X(t).
dt an inﬁnitesimal increment of time t.
P (A|B) conditional probability of A occurring assuming B is true.
Explanatory Comments for Index
In the index entries, plural in many (but not all) cases is reduced to singular (so,
e.g., “commodity” also includes “commodities”). Parentheses contain acronyms or
deﬁnitions, and in some (but not all) cases both versions are present in the main text.
Most (but not all) index entries with commas, i.e., “ noun, adjective”, correspond to
text entries such that the precise string “ adjective noun” is not directly present in
the text, but is present indirectly (e.g., as “ adjective (...) noun ”) or contextually.
341
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 343

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Index
absolute momentum, 62
academic alpha, 59
acquirer company, 52
acquisition, 125
activation function, 119
active approach, 90
active distressed investing, 109
active investing, 109
active management, 64
actively managed ETF, 64
adjusted close price, 127
adjusted open price, 127
adjusted price, 127
adjustment factor, 127
adverse selection, 58
aggressive order, 58
aggressive order ﬂow, 58
allocation weight, 80
alpha, 59, 63, 64
alpha combo, 59
alpha combo strategy, 59
alpha portfolio weights, 60
alpha return, 60
alpha rotation, 63
alpha rotation strategy, 64
alpha weights, 60
alternative real estate vehicles, 113
American option, 17
American put option, 104
announcement days, 123
annual inﬂation, 105
annualization factor, 84
annualized return, 129
annualized Sharpe ratio, 129
anomaly, forward discount, 86
appraised value, 115
arbitrage, 106
arbitrage trade, 77
artiﬁcial neural network (ANN), 116–119
Asian option, 17
ask, 58, 89
ask price, 80
asset, 42
asset class, 15, 16, 65, 80, 119, 121, 122,
124
asset-backed security (ABS), 97
ATM option, 78
ATM straddle, 83
attachment, 98
attachment point, 97
average daily dollar volume (ADDV), 125,
126
average underlying price, 17
B/P ratio, 42
back leg, 75
backspread, 30, 31
backtest, 16, 55, 128, 129
backtesting, 125, 128
backtesting period, 129
backwardation, 81, 89, 90
bank deposit certiﬁcate (CD), 114
banker’s acceptance, 114
bankruptcy, 108–110, 125
bankruptcy probability, 110
bankruptcy protection, 109
bankruptcy-ﬁling month, 109
barbell, 69, 70
barbell portfolio, 70, 71
barbell strategy, 69
barrier option, 17
base form, 120
basis point (bps), 109, 126
basis risk, 93
basket, 82, 88, 97, 123
Bayes’ theorem, 120
bearish strategy, 18, 23
Bermudan option, 17
Bernoulli probability distribution, 120
bias, 119
342
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 344

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
bid, 58, 89
bid price, 80
bid-ask spread, 58
binary industry classiﬁcation, 61, 128
bisection method, 102
Bitcoin (BTC), 116, 119–121
Bitcoin trading, 121
black-box machine learning techniques,
92
Black-Scholes model, 92
blockchain, 116
blockchain technology, 116
Bloomberg Industry Classiﬁcation System
(BICS), 128
body, 72
bond, 15, 17, 66–71, 73–76, 94, 97, 98,
100–102, 111, 112, 121–123
bond credit rating, 73
bond immunization, 70, 71
bond maturity, 73
bond portfolio, 70
bond price, 66, 68, 69
bond spread, 75, 76
bond value, 74
bond yield, 73–75, 94
bond yield spread, 75
bond, deliverable, 94
bond, non-deliverable, 94
bond, Treasury, 105
book value, 42
book-to-market ratio, 42
book-to-price (B/P) ratio, 42
Boolean, 125
bounds, position, 57
bounds, trading, 57
box, 37
box option strategies, 37
break-even point, 26
break-even price, 18
breakeven rate, 105
broad index, 76
broad market, 62, 97
broad market index, 63
broad market index ETF, 62, 63
brownﬁeld project, 124
Brownian motion, 91, 92
BTC price, 117, 120
Btu (British thermal unit), 108
bullet, 69, 70
bullet portfolio, 69, 71
bullet strategy, 69
bullish strategy, 18, 23
business cycle, 122
business cycle trends, 122
butterﬂy, 32, 33, 35, 36, 72
butterﬂy bond strategy, 72
butterﬂy spread, 32
butterﬂy strategy, 32, 33
buy signal, 86, 92, 119
buy-and-hold investment, 124
buy-write strategy, 18
calendar call spread, 24, 25
calendar put spread, 24–26
calendar spread, 94
call option, 17–39, 84, 102, 107
call spread, 19, 20, 22, 23, 34, 36, 37
call, naked, 19
call, short, 19
Canary option, 17
capital allocation, 70
capital allocation weights, 95
capital gain strategy, 20–22, 26–32, 34–
39
Carhart’s momentum factor (MOM), 63
carry, 74, 77, 99, 100
carry factor, 74
carry strategy, 74, 86–88
carry trade, 86
cash, 15, 77, 114, 115
cash ﬂow, 67, 68, 100, 102, 105, 106, 111,
124
cash ﬂow shortfall, 115
cash merger, 52
cash-and-carry arbitrage, 77
cash-equivalent asset, 115
343
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 345

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
CDO notional, 98
CDO tranche, 97, 98
CDO tranche hedging, 99
CDS arbitrage trade, 76
CDS basis, 75
CDS basis arbitrage, 75
CDS hedging, 100
CDS index, 98, 99
CDS price, 75
CDS spread, 75, 76
cents-per-share, 58, 129
channel, 52, 60
channel break, 52
channel indicator, 52
channel trading strategy, 52
Chapter 11, 109, 110
cheap stock, 45
Chicago Board Options Exchange
(CBOE), 80
claim, 17
claim pricing argument, 92
class, 120, 121
close, 60, 82, 125
close price, 126
close-to-close return, 79
close-to-open return, 127
closing price, 51, 65, 128
cluster, 46–48
clustering algorithm, 61
Cochrane-Piazzesi predictor, 123
collar, 37
collar strategy, 37
collateral, 115, 116
collateralized debt obligation (CDO), 15,
97, 98, 100
combo, 21, 22, 38, 39
combo strategy, 22
commercial paper, 114
commercial real estate, 113
Commitments of Traders (COT), 90
commodity, 15, 17, 89–91, 121–123
commodity allocation percentage (CA),
123
commodity futures, 15, 89–91, 94, 115
commodity futures term structure, 91
commodity investment, 90
commodity market, 90
commodity price, 122
commodity return, 90
common stock, 17
compounding period, 71, 86, 106
computation, out-of-sample, 127
conditional expectation, 92
conditional independence assumption, 121
conditional probability, 120, 121
condor, 34, 35
condor strategy, 32
constrained regression, 101
constraints, inhomogeneous, 57
constraints, nonlinear, 57
Consumer Price Index (CPI), 105, 106,
122
contango, 81, 82, 89, 90
continuous compounding, 66, 68, 69
contrarian trading, 95
control rights, 110
conversion factor, 94
conversion factor model, 94
conversion option, 101, 102
conversion price, 101
conversion ratio, 101
convertible arbitrage, 101
convertible arbitrage strategy, 101
convertible bond, 15, 101, 102
convertible bond pricing, 102
convertible option-adjusted spread, 102
convertibles, 101
convexity, 68–71, 100
cooling-degree-days (CDD), 107
core inﬂation (CI), 122, 123
corporate actions, 52
correlation, 65, 78, 79, 90, 91, 96, 111,
112, 116
correlation matrix, 79
correlation trading, 78
correlation, implied, 78
344
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 346

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
correlation, serial, 88
counterparty, 115
coupon, 66, 70, 94
coupon bond, 66, 74
coupon payment, 66, 67, 70, 105, 106
coupon payment, ﬁxed rate, 76
coupon rate, 66, 106
covariance matrix, 44, 65, 96
covariance matrix, sample, 55
covered call, 18, 29, 37
covered call option strategy, 19
covered call strategy, 18, 24
covered interest arbitrage, 87
Covered Interest Rate Parity (CIRP), 86,
87
covered put, 18, 37
covered put option strategy, 19
covered put strategy, 19, 25
covered short straddle, 29
covered short strangle, 29
covered straddle, 26
credit default swap (CDS), 75, 76, 97, 98,
100
credit derivatives, 98
credit rating, 73, 97
credit spread, 73
cross-border tax arbitrage, 103, 104
cross-entropy, 119
cross-hedging, 93
cross-sectional analysis, 59, 123
cross-sectional standard deviation, 96
cross-sectional strategy, 54
cross-sectional trade, 87
cross-validation, 54
cryptoassets, 116
cryptocurrency, 15, 116, 119
cryptocurrency trading, 120, 121
cryptocurrency trading strategy, 116
cryptography, 116
CTA (commodity trading advisor), 122
cum-dividend, 103, 104
cumulative ETF return, 63
cumulative inﬂation, 105
cumulative return, 40, 53, 62, 65, 96, 97
currency, 15, 17, 86–89, 121, 122
currency carry trade, 87
currency pair, 89
curvature, 72
curve trade, 100
curve-neutrality, 72
daily roll value, 81
dark spread, 108
data mining, 16
data, cross-sectional, 60
data, economic, 61
data, fundamental, 53, 61
data, single-stock, 60
data, technical, 53
debt seniority level, 109
decentralized digital currency, 116
decile, 40, 42–45, 62, 64, 65, 73, 74, 87,
110, 122
default, 75, 98, 108, 109
default month, 109
default payment, 98
default risk, 97
defaulted credit, 98
deferred-month contracts, 94
deferred-month futures, 94
delay, 128
delay-0 strategy, 128
delay-1 strategy, 128
delivery, 77, 93
delivery date, 92
delivery month, 94
delivery price, 21
delivery time, 77
Delta, 83, 99, 102
Delta-hedging, 84
Delta-hedging strategy, 84
demand, 94, 107
demand hedging, 106
demand risk, 107
demeaned rank, 44
demeaned return, 46–49, 97
345
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 347

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
derivative, 15, 81, 121
derivative contract, 84
desired holdings, 59, 128, 129
detachment, 98
detachment point, 97
diagonal call spread, 25
diagonal put spread, 25
diagonal spread, 25
directional exposure, 84
directional strategy, 18, 84, 122
discount bond, 66
discount factor, 106
discount rate, 76
discretionary macro, 122
discretionary strategy, 122
dispersion strategy, 78, 85
dispersion trading, 77, 78
dispersion trading strategy, 79
distress risk puzzle, 110
distress risk puzzle strategy, 110
distress situation, 109, 110
distress, ﬁnancial, 108
distress, operational, 108
distressed asset, 15, 108, 109
distressed company, 109
distressed debt, 108, 109
distressed debt market, 109
distressed debt passive trading strategy,
109
distressed debt portfolio, diversiﬁed, 109
distressed ﬁrm, 109, 110
distressed security, 108
distributed ledger, 116
diversiﬁcation, 111–113, 124
diversiﬁcation power, 65
diversiﬁcation strategy, 90
diversiﬁed portfolio, 69, 76
diversiﬁer, 116
dividend, 40, 45, 77, 103, 104, 126
dividend imputation, 103
dividend payment, 103
dollar carry trade, 88
dollar duration, 68, 72, 75, 94
dollar holding, 55, 125, 126
dollar position, 47
dollar-duration-neutral butterﬂy, 71, 72
dollar-duration-neutrality, 72
dollar-neutral book, 77
dollar-neutral portfolio, 41–43, 45, 50, 56,
57
dollar-neutral strategy, 45, 62, 64, 76
dollar-neutral trade, 87
dollar-neutrality, 46, 56, 57, 72, 97, 128
dollar-neutrality condition, 97
dollar-neutrality constraint, 47, 56, 57
domestic currency, 86, 87
domestic interest rate, 86
Donchian Channel, 52
double-taxation system, 103
Dow Jones Industrial Average (DJIA), 76
downside risk, 65
drawdown, 82, 114
drift, 65
dual-momentum sector rotation, 62
dumb order ﬂow, 58, 59
dummy variable, 73
duration, 68, 70
duration-targeting strategy, 70
dynamic asset allocation, 65
earnings, 41, 42, 59
earnings-momentum, 41
earnings-momentum strategy, 42
economic activity, 112
economic announcement, 123
economic diversiﬁcation, 112
eﬀect, contrarian, 40
eﬀect, mean-reversion, 40, 96
eigenvalue, 79
electricity futures, 108
electricity futures contract, 108
electronic trading, 16
embedded option, 101, 102
EMSD (exponential moving standard de-
viation), 117, 118
energy, 15, 47, 108, 124
346
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 348

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
energy hedging, 108
energy spreads, 108
equally-weighted portfolio, 126
equities, 17, 95, 112, 119, 122, 123
equity index, 77, 122
equity market, 81, 90
equity market excess return, 122
equity portfolio, 90
equity tranche, 99
equity tranche credit events, 99
equity tranche trade, 99
equity value, 110
eRank (eﬀective rank), 79
error function, 119
establishing, 18, 54, 126
estimation period, 63, 64, 86
ETF alpha, 63
ETF arbitrage, 79
ETF portfolio, 65
ETF return, 63, 65
ETF, leveraged, 64
ETF, leveraged inverse, 64
ETH (ether/Ethereum), 116
Euclidean distance, 44, 54
EUR (euro), 116
eurodollars, 114
European call option, 17
European option, 17
European put option, 17
ex-dividend, 103, 104
excess return, 44, 52
exchange rate, 89
exchange-traded fund (ETF), 15, 61–65,
79, 123
exchange-traded note (ETN), 15, 82
execution price, 59
exercise date, 17
exotic options, 17
expected alpha return, 60
expected return, 44, 54, 57–60, 65, 91,
96, 125, 126, 128
expected stock return, 55
expiration, 17, 24, 25, 78, 89, 104
explanatory variable, 110
exponential moving average (EMA), 50,
97, 117, 118
exponential smoothing parameter, 117
exposure, 43, 65, 70, 76, 90, 92, 94, 99,
111, 124
extreme market events, 111
face value, 66, 69
factor, 43, 44, 63, 65, 123
factor investing, 123
factor loadings matrix, 57
factor portfolio, 44
factor rankings, 44
factor-based strategies, 111
fair value, 77, 101
false signal, 51, 85
Fama puzzle, 86
Fama-French factors, 44, 63
fear gauge index, 81
feature, 120, 121
feature vector, 120
Fed discount rate, 90
Fed monetary policy, 90
Federal Open Market Committee (FOMC),
123
fence, 37
ﬁat currency, 116
ﬁfty-ﬁfty butterﬂy, 72
ﬁll or kill limit order, 80
ﬁlls, 58
ﬁlter, Hodrick-Prescott, 85
ﬁnanced portfolio, 74
ﬁnancial crises, 111
ﬁnancial derivative, 17
ﬁnancial distress, 115
ﬁnancial markets, 16
ﬁrm’s equity, 109, 110
ﬁrst-month contract, 81
ﬁx-and-ﬂip, 114
ﬁxed coupon, 105
ﬁxed coupon bond, 67
ﬁxed coupon rate, 106
347
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 349

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
ﬁxed income, 66
ﬁxed rate, 67, 105, 106
ﬁxed rate cash ﬂow, 105
ﬁxed rate coupon bond, 68
ﬁxed rate payment, 67
ﬁxed-income asset, 93, 123
ﬁxed-income instrument, 101
ﬂattener, 75, 100
ﬂoating coupon payment, 67
ﬂoating rate, 105
ﬂoating rate bond, 67
ﬂoating rate cash ﬂow, 105
ﬂoating rate payment, 67
FOMC announcements, 123
forecasting future returns, 63
foreign currency, 86–88
foreign currency forward, 88
foreign exchange (FX), 85
foreign interest rate, 86
formation period, 40, 45, 62
forward, 86, 87
forward contract, 21, 87
forward discount, 86–88
forward FX rate, 86
forward premium, 86
front leg, 75
front-month futures price, 89
fuel futures, 108
fundamental analysis, 60, 61
fundamental data, 59
fundamental industry classiﬁcation, 128,
129
fundamental macro momentum, 122
fundamental trading strategies, 116
fundamentals, 61, 94, 116
futures, 15, 17, 77, 81–83, 89, 91–97, 108,
113, 123
futures basis, 94
futures calendar spread, 94
futures contract, 77, 89, 92–94
futures contract size, 108
futures contract, front-month, 82
futures delivery basket, 94
futures position, 21, 89, 93, 107
futures price, 77, 81, 89, 91–93
futures return, 82, 95
futures spread, bear, 94
futures spread, bull, 94
futures yield, 94
futures, CTA, 122
futures, managed, 122
futures, T-bond, 94
futures, T-note, 94
FX momentum strategy, 88
FX rate, 86
FX rate risk, 86, 87
FX spot rate, 85
FX spot rate time series, 85
FX triangular arbitrage, 89
Gamma, 83
Gamma hedge, 84
Gamma hedging, 83, 84, 102
Gamma scalping, 84
gas futures contract, 108
GDP (gross domestic product), 122, 123
geographic diversiﬁcation, 113
Global Industry Classiﬁcation Standard
(GICS), 128
global macro, 15, 121
global macro inﬂation hedge, 122
global macro inﬂation hedge strategy, 123
global macro strategy, 122
government bond, 122, 123
government security, 76
Greeks, 83
greenﬁeld project, 124
guts, 26–28
guts strategy, 26
hard-to-borrow securities, 77
headline inﬂation (HI), 122, 123
healthy-minus-distressed (HMD), 110, 111
heat rate, 108
heating-degree-days (HDD), 107
hedge, 93, 94, 108, 113, 123
hedge position, 93
348
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 350

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
hedge ratio, 82, 93, 94, 99–102, 107, 108
hedgers, 90, 96
hedging, 15, 82
hedging pressure (HP), 90
hedging strategy, 15, 18, 19
heterotic risk model, 128
hidden layer, 117, 119
high frequency trading (HFT), 16, 58, 59,
77
high minus low (HML), 44
High Yield bonds, 73
high-minus-low carry, 87
high-return-volatility portfolio, 42
historical correlation, 45, 82, 83
historical data, 72, 73, 92, 94, 101
historical return, 43, 55, 78, 88, 91
historical stock price, 50
historical variance, 83, 88
historical volatility, 43, 44, 49, 65, 80, 82,
83, 95, 96, 126
Hodrick-Prescott ﬁlter, 97
holding horizon, 61
holding period, 41–43, 45, 62, 90, 111,
122
holding weights, 55, 56
horizon, 58, 59, 61, 112
horizontal spread, 24
HP ﬁlter, 85
Hybrid Market, 16
hybrid security, 101
hyperbolic tangent (tanh), 119
implied index volatility, 78
implied volatility, 43, 78, 80, 83–85
imputation system, 103
income strategy, 20, 22, 23, 27, 28, 31,
33, 34, 36
income-generating real estate portfolio,
111
incomplete basket, 77
index, 15, 17, 76–80, 85, 99, 100, 122
index arbitrage, 77
index basket, 77
index constituents, 77, 85
index ETF, 79
index futures, 76, 77
index futures price, 77
index hedging, 99
index implied volatility, 78
index level, 78
index option, 78, 83
index option straddle, 78
index portfolio, 77
index position, 99
index spot price, 77
index volatility, 77, 78
index volatility targeting, 80
index, market cap weighted, 78
index-based ETF, 76
indexed payment, 106
industrial properties, 112
industry, 46, 49, 60–62, 109, 129
industry classiﬁcation, 61
industry classiﬁcation data, 59
inﬂation, 104, 105, 113, 122, 123
inﬂation hedge, 123
inﬂation hedging, 104, 113, 124
inﬂation index, 105
inﬂation rate, 113
inﬂation swap, 104, 105
inﬂation-hedging investment, 124
inﬂation-indexed products, 105
infrastructure, 15, 123, 124
infrastructure asset, 124
infrastructure company, 124
infrastructure fund, 124
infrastructure investment, 124
infrastructure project, 124
input layer, 116–118
institutional trader, 59
integration, 114
intercept, 44, 48, 49, 54, 60, 63, 74, 82
interest, 67, 86, 115
interest rate, 66, 68, 69, 72, 74, 75, 77,
86, 87, 93, 94, 97, 100, 103, 115,
116
349
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 351

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
interest rate exposure, 100
interest rate futures, 93
interest rate futures contract, 94
interest rate futures hedge ratio, 94
interest rate risk, 69, 70, 93
interest rate risk hedging, 93
interest rate spread, 72, 105
interest rate swap, 76, 100, 104
Internal Bar Strength (IBS), 64
international trade, 122
international trade trends, 122
intra-asset diversiﬁcation, 112
intraday arbitrage, 79
intraday signal, 58
intraday strategy, 125
intraday trading strategy, 126
inverse, 56
inverse ETF, 65
inverse model covariance matrix, 128
investment, 15, 41, 46, 47, 70, 86, 111,
124
Investment Grade bonds, 73
investment level, 41, 43, 56, 125, 126
investment opportunity, 115
investment portfolio, 122
investment strategy, 124
investment style, 121
investment vehicle, 76, 113
investment, equity, 90
iron butterﬂy, 32, 34
iron condor, 36
iShares, 79
Jensen’s alpha, 59, 63
Joule, 108
JPY (Japanese Yen), 86
k-nearest neighbor (KNN) algorithm, 53,
54, 117
Kalman ﬁlter, 97
Kelly strategy, 115
keyword, 120
ladder, 22, 23, 70
ladder portfolio, 70
ladder strategy, 23
Lagrange multiplier, 57
layering, 114
learning vocabulary, 120, 121
leg, contingent, 98
leg, default, 98
level, resistance, 51
level, support, 51
leverage, 64, 65, 80, 111
leveraged ETF (LETF), 64, 65
leveraged inverse ETF, 65
limit order, 58
limit order, aggressive, 58
limit order, marketable, 80
linear homogeneous constraints, 57
linear model, 54
linear regression, 47, 48
linear trading costs, 125, 126
liquid funds, 114
liquid stake, 111
liquid U.S. stocks, 59
liquidating, 54
liquidation, 115
liquidity, 40, 61, 115
liquidity management, 115
liquidity management tool, 114
listed infrastructure funds, 124
loadings matrix, 48, 49, 61
loan, 87, 98, 103, 115, 116
loan shark, 116
loan sharking, 116
loan-to-own, 110
log forward FX rate, 87
log spot FX rate, 87
log-return, 84
log-volatility, 92
logistic regression, 110, 121
logit model, 121
London Interbank Oﬀer Rate (LIBOR),
67, 76
long portfolio, 73, 79
long risk reversal strategy, 84
350
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 352

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
long-maturity wing, 72
long-only, 50
long-only portfolio, 40, 41
long-only strategy, 62
long-only trend-following portfolio, 65
long-run mean, 92
long-short strategy, 122
lookback, 125
lookback period, 79
losers, 40–42, 44, 95, 97
loss, contango, 82
loss, roll, 82
low-return-volatility portfolio, 42
low-risk anomaly, 73
low-risk factor, 73
low-volatility anomaly, 42
Macaulay duration, 68
machine learning, 16, 53, 55, 59
machine learning algorithm, 54
machine learning classiﬁcation scheme, 120
machine learning methods, 59, 121
machine learning techniques, 53, 116
macro strategy, 122
macro trading strategy, 121, 123
macroeconomic trends, 122
managed futures, 122
Manhattan distance, 44, 54
margin account, 76
mark-to-market (MTM), 98, 99
market, 16, 17, 58, 61, 65, 70, 83, 110,
113
market activity, 95
market beta, 110
market cap, 59, 78, 116
market cap weighted index, 77
market capitalization, 42, 44, 76, 116
market crashes, 41
market data, 89
market downturn, 110
market index, 95, 97
market index return, 95, 97
market portfolio, 44
market price, 52, 92, 102, 114
market underreaction, 122
market value, 111
market volatility, 94
market-making, 58, 59
married call, 19
married put, 19
maturity, 17, 18, 21, 24, 25, 66–71, 73–76,
81, 82, 84, 87, 93, 94, 104–106
maturity date, 69, 87
maturity time, 17, 66
maturity-weighted butterﬂy, 73
MBS passthrough, 100
MBS price, 100, 101
MBtu, 108
mean-reversion, 46, 47, 49, 54, 60, 64, 81,
92, 95, 128
mean-reversion parameter, 92
mean-reversion strategy, 45, 47, 64, 81,
95
mean-variance optimization, 57, 112, 126
Megawatt, 108
Megawatt hour (Mwh), 108
merger, 125
merger arbitrage, 52
merger arbitrage opportunity, 52
mergers and acquisitions (M&A), 52
metropolitan statistical area (MSA), 113
mini-S&P 500 futures, 81, 82
mishedge, 77
mispricing, 45, 79
mixed-asset diversiﬁcation, 111
MMBtu, 108
model covariance matrix, 55, 57
modiﬁed duration, 68–70, 72, 74, 94
momentum, 43, 44, 61, 62, 65, 96, 97,
123, 128
momentum & carry combo, 88
momentum eﬀect, 40, 41, 60, 61, 113
momentum strategy, 41, 60, 88, 96
momentum, absolute, 62
momentum, cross-sectional, 62
momentum, industry, 62
351
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 353

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
momentum, relative, 62
momentum, sector, 62
momentum, time-series, 62
monetary policy, 122
monetary policy trends, 122
money laundering, 114
moneyness abbreviations
(ATM, ITM, OTM), 18
mortgage, 100
mortgage-backed security (MBS), 15, 100,
102
moving average, 49–51, 53, 60, 62, 63, 65,
85, 86
moving average length, 117
moving average, exponential, 117
moving standard deviation, 125
moving standard deviation, exponential,
117
multi-asset portfolio, 65
multi-asset trend following, 65
multi-currency arbitrage, 89
multifactor model, 57, 91
multifactor portfolio, 43, 123
multifactor risk model, 57
multifactor strategy, 44
multinomial distribution, 120
municipal bond, 103, 124
municipal bond tax arbitrage, 102
mutual fund, 59, 63, 64, 111
mutual fund return, 63
naked call, 19
naked put, 18
near-month contract, 94
near-month futures, 94
neutral curve butterﬂy, 72
New York Stock Exchange (NYSE), 16
no-risk-free-arbitrage condition, 87
node, 118
noise, 85, 97, 122
non-announcement days, 123
non-deliverable bond, 94
non-directional strategy, 18
non-discretionary strategy, 122
non-systematic risk, 112
non-systematic risk reduction, 112
nonlinear least squares, 92
normalized demeaned return, 60
notional, 106
notional amount, 98
objective function, 56, 57, 85
open, 125, 128
open interest, 95, 96
open price, 51, 127
operational distress, 108
opportunity management tool, 114
optimal hedge ratio, 82, 83, 93
optimal weighting scheme, 43
optimization, 55, 57, 128
optimization strategy, 96
optimization techniques, 71
optimization, mean-variance, 125
optimizer function, 128
option, 15, 17, 18, 21, 78, 80, 81, 83, 84,
104, 113
option Gamma, 102
option holder, 17
option premia, 18, 84
option pricing, 17
option straddle, 78
option styles, 17
option trading strategy, 37–39, 80
option writer, 17
option, all-or-nothing, 17
option, ATM (at-the-money), 19–34, 37–
39, 78
option, binary, 17
option, call, 26, 27, 84, 104
option, digital, 17
option, ITM (in-the-money), 25–28, 31–
35, 37, 104
option, OTM (out-of-the-money), 18–23,
25–27, 29–39, 84
option, put, 26, 27, 84, 104
option-adjusted spread (OAS), 102
352
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 354

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
order, 58, 128
order execution system, 80
order ﬂow, dumb, 58
order ﬂow, informed, 58
order ﬂow, smart, 58
order ﬂow, toxic, 58
order, market, 58
orders, cancel-replaced, 58
orders, canceled, 58
orders, placed, 58
Ornstein-Uhlenbeck process, 91
orthogonality condition, 49
OTM option, 78
out-of-sample backtest, 118
out-of-sample backtesting, 16, 125
outcome, 120, 121
output gap, 123
output layer, 116, 118, 119
over-ﬁtting, 118
overnight return, 126
overreaction, 95, 109
P&L, 76, 84, 93, 100, 104, 129
P&L drawdown, 82
pairs trading, 45–47
pairs trading strategy, 46
parallel shift, 68, 70, 72, 75, 102
passive approach, 90
passive distressed debt strategy, 109
passive limit order, 58
passive trading strategy, 109
passthrough MBS, 100
passthrough MBS price, 101
pawnbroker, 115
pawnbroking, 115, 116
pawnbroking strategy, 115
payment period, 66
payment, coupon, 106
payment, principal, 106
payoﬀ, 17–19, 78, 84, 93
peer-to-peer (P2P) internet protocol, 116
pension fund, 59
performance characteristics, 90, 112, 129
period, formation, 90
periodic compounding, 66, 68, 71
periodic premium payment, 97, 98
periodic premium payment rate, 97
physical commodity, 115
pivot point, 51
placement, 114
Porter stemming algorithm, 120
portfolio, 15, 40, 41, 43, 44, 55, 62, 65, 67,
69–72, 74, 75, 78, 79, 82, 83, 90,
91, 95, 110, 112, 114, 115, 122,
123, 125, 126
portfolio construction techniques, 112
portfolio diversiﬁcation, 90
portfolio management, 115
portfolio optimization, 125
portfolio P&L, 55
portfolio performance, 112
portfolio weights, 56
portfolio, barbell, 69
portfolio, HML, 44
portfolio, ladder, 69
portfolio, MKT, 44
portfolio, SMB, 44
position bounds, 125
position, bearish, 23
position, bullish, 23
predicted class, 119
predicted value, 54
predictor variable, 53
premium, 15, 17, 84, 99
premium leg, 98
premium payment, 100
premium, annual, 75
premium, periodic, 75
prepayment model, 101
prepayment risk, 100
price and volume data, 53, 126
price reversal, 52
price, close, 64
price, fully adjusted, 40, 45, 126, 127
price, high, 51, 64, 126
price, intraday, 126
353
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 355

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
price, low, 51, 64, 126
price-momentum, 40
price-momentum strategy, 40–42, 44
price-volume, 59
pricing data, 61
pricing model, 91, 102
principal, 66, 67, 70, 94, 105, 106
principal component analysis (PCA), 79
principal components, 61, 79
private equity-type investments, 124
probability distribution, 120
probability measure, 92
property type, 113
property type diversiﬁcation, 112
protection buyer, 98
protection seller, 97
protective call, 19
protective call option strategy, 19
protective put, 19
protective put option strategy, 19
protective put strategy, 19
publicly traded company, 52
publicly traded infrastructure companies,
124
put option, 17–39, 84, 104, 107
put spread, 20, 23, 34, 36–38
put, naked, 18
put, short, 18
put-call parity, 18
quantile, 87, 118–120, 123
quantitative trading alpha, 59
quark spread, 108
quintile, 44, 64, 90, 91
R Package for Statistical Computing (R),
125
R-squared, 63
R-squared strategy, 64
rallies, 81
rank, 44, 79
ranking, 44, 122
rate, ﬁxed, 104
rate, ﬂoating, 104
ratio call spread, 31
ratio put spread, 31
raw close price, 127
raw inﬂation, 122
raw open price, 127
raw spot rate, 85
real estate, 15, 111–113, 124
real estate asset, 111, 112
real estate holdings, 112
real estate investment, 111, 112
real estate investment strategy, 114
real estate investment trust (REIT), 111,
113
real estate momentum, 113
real estate momentum strategy, 113
real estate property, 113
real estate return, 113
real estate, commercial, 111
real estate, residential, 111
real interest rate, 123
realized alpha return, 60
realized P&L, 58
realized proﬁt, 50
realized variance, 84
realized volatility, 83, 85, 111
rebalancing, 80, 82, 89, 90, 110
recovery rate, 98
rectiﬁed linear unit (ReLU), 119
reference entities, 98
reference pools, 98
regression, 45, 48, 49, 54, 60, 72, 73
regression coeﬃcient, 45, 48, 63, 73, 74
regression R-squared, 63
regression residual, 48, 73
regression weights, 49
regression, cross-sectional, 73
regression-weighted butterﬂy, 72, 73
reinvestment risk, 70
relative momentum, 62
relative strength index (RSI), 117, 118
relative value strategy, 122
reorganization, 109, 110
reorganization plan, 109
354
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 356

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
reorganization process, 109
replication, 106
repo rate, 76
repo strategy, 115
repurchase agreement (repo), 114, 115
residual momentum, 44
residual momentum strategy, 45
resistance, 51, 60
retail trader, 58
return, risk-adjusted, 40, 45, 112, 124
reverse repurchase agreement, 115
rich stock, 45
risk, 15, 19, 28, 33, 35, 36, 42, 52, 62, 70,
77, 81, 82, 87, 92, 99, 100, 112,
125
risk arbitrage, 52
risk factor, 49, 79
risk management, 15, 57, 110, 128
risk management tool, 114
risk model, 125, 127, 128
risk premium, 110
risk reversal, 21, 22, 38, 39, 84
risk sentiment, 122
risk sentiment trends, 122
risk, idiosyncratic, 79
risk, interest rate, 70
risk, speciﬁc, 79
risk-free arbitrage, 87
risk-free arbitrage opportunity, 86
risk-free asset, 80, 86, 123
risk-free discount factor, 98
risk-free instrument, 75
risk-free interest rate, 86
risk-free interest rate curve, 102
risk-free position, 87
risk-free probability measure, 92
risk-free proﬁt, 27, 76
risk-free rate, 44, 73–75, 77, 94
riskless asset, 80
risky duration, 99, 100
roll loss, 82
roll yield, 89
roll-down component, 74
rolling down the curve, 75
rolling down the yield curve, 74
rolling down the yield curve strategy, 75
root mean square error (RMSE), 54
rotation, industry, 62
rotation, sector, 62
Russell 3000, 76
S&P 500, 76, 79, 83
S&P 500 ETFs, 79
S&P 500 option, 83
sample correlation matrix, 78, 79
sample covariance matrix, 55, 83, 88
sample variance, 60
scale invariance, 56, 57
seagull spread, 37–39
second-month futures price, 89
sector, 46, 47, 49, 61, 62, 65, 106, 124
sector ETF, 62
sector momentum rotation, 61, 62
sector momentum rotation strategy, 61–
63, 65
sector rotation signal, 62
secured cash loan, 115
secured loan, 110
security, 115
selectivity, 64
sell signal, 86, 92, 119
sell-oﬀs, 81
sell-write strategy, 18
semiannual compounding, 94
semiannual ﬁxed coupons, 105
sentiment analysis, 120
sentiment data, 59, 121
serial regression, 44, 63, 82, 93
serial variance, 88
serially demeaned return, 60, 117
settlement, 81
share, 17, 41, 42, 46, 52, 58
shareholder, 103
shares outstanding, 78
Sharpe ratio, 55, 56, 58, 65
Sharpe ratio maximization, 56, 57
355
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 357

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
short-maturity wing, 72
short-sale, 47
short-selling issues, 77
shorting ETFs, 62
shorting stock, 18, 19, 28, 29, 42, 43, 45
shorting Vega, 83
shorting VIX futures, 81
sideways market, 83
sideways strategy, 18, 27–29, 32–36
sigmoid, 119
signal, 16, 50, 52, 54, 55, 58, 128
signal, buy, 120
signal, ephemeral, 16
signal, machine learning, 57
signal, mean-reversion, 57
signal, momentum, 57
signal, sell, 120
simple moving average (SMA), 49, 50,
127
simple moving standard deviation, 127
single-stock KNN, 53, 60
single-stock KNN trading strategy, 117
single-stock methods, 59
single-stock option, 17, 78, 79, 83
single-stock option straddle, 78
single-stock strategy, 53
single-stock technical analysis strategies,
60
single-stock trading, 54
single-tranche CDO, 98
skew, 84
skewness, 91
skewness premium, 91
skip period, 40, 43, 45
slippage, 16, 41, 77, 80
Small minus Big (SMB), 44
smart order ﬂow, 58
smoothing parameter, 85
social media sentiment analysis, 120
softmax, 119
sorting, 64
source code, 16, 57, 79, 125
sovereign risk, 123
spark spread, 108
SPDR Trust, 79
specialist system, 16
speciﬁc risk, 57, 79
speculative bubble, 116
speculative buy-and-hold asset, 116
speculator, 90, 108
spike, 82
splits, 40, 45, 126
spot, 77, 82
spot FX rate, 86, 122
spot price, 77, 91, 93
spot value, 77
spread, 69, 75, 83, 100, 102, 108, 123
spread change, 72
spread curve, 100
spread, calendar, 24
spread, CDO tranche, 98–100
spread, diagonal, 24
spread, ratio, 30, 31
standard deviation, 42
Standard Industrial Classiﬁcation (SIC),
128
standardized unexpected earnings (SUE),
42
state variable, 122
statistical arbitrage, 15, 54, 55, 61
statistical arbitrage strategy, 16, 61
statistical industry classiﬁcation, 125, 128
statistical risk model, 79, 128
steepener, 75, 100
stemming, 120
stochastic dynamics, 92
stochastic gradient descent (SGD), 119
stochastic processes, 91
stochastic volatility models, 91
stock loan, 104
stock market, 61
stock merger, 52
stock price, break-even, 18
stock trading strategy, 60
stock, cheap, 46
stock, rich, 46
356
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 358

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
stop-loss price, 24, 25
stop-loss rule, 50
stop-words, 120
straddle, 26–29, 33, 35, 36, 79, 80, 83, 85
strangle, 26, 27, 33, 35, 36
strap, 30
strategy, ANN, 120
strategy, barbell, 69
strategy, bullet, 69
strategy, capital gain, 18, 35, 36
strategy, contrarian, 49
strategy, delay-0, 128
strategy, delay-1, 128
strategy, Delta-neutral, 83
strategy, earnings-momentum, 42
strategy, HMD, 110, 111
strategy, income, 18, 35, 36
strategy, ladder, 70
strategy, mean-reversion, 49
strategy, momentum, 60
strategy, price-momentum, 42
strategy, resistance, 51
strategy, straddle, 26
strategy, strangle, 26
strategy, strap, 30
strategy, strip, 30
strategy, support, 51
strategy, trend following, 60
strategy, zero-cost, 110
strike, 32–36, 84
strike price, 17–39, 84, 104, 107
strip, 30
STRIPS (Separate Trading of Registered
Interest and Principal of Securi-
ties), 106
structured assets, 15, 97
style factor, 61
style risk factor, 61
subset portfolio, 78
sum of squares (SS), 63
supply, 94
support, 51, 60
support vector machine (SVM), 121
survivorship bias, 125
swap, 67, 76, 105
swap agreement, 104
swap contract, 105
swap ﬁxed rate, 105
swap rate, 101
swap spread, 76
swap strategy, 76, 104
swap-spread arbitrage, 76
synthetic call, 19, 28, 29
synthetic CDO, 98
synthetic coupon payment, 106
synthetic forward, 21, 37
synthetic forward contract, 21
synthetic futures, 21
synthetic index, 106
synthetic portfolio, 106
synthetic put, 19, 28
synthetic short bond position, 76
synthetic straddle, 28, 29
systematic approach, 122
systematic macro, 122
systematic macro trading strategy, 123
systematic risk, 79
T-bond, 94
T-note, 94
tactical asset allocation, 90
target company, 52
target variable, 53
target volatility, 111
tax arbitrage, 15, 102
tax credit, 103, 104
tax credit rate, 103, 104
tax shield, 103
tax strategy, 37
tax-exempt municipal bonds, 102, 103
technical analysis strategies, 61
technical indicator, 116, 117
tercile, 91
term spread, 123
term structure, 74, 89, 92
Theta, 83
357
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 359

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
Theta play, 83
Theta-decay, 84
ticker, 79, 125–127
ticker symbol, 127
time series, 40, 43, 50, 55, 60, 78, 80, 91
time-series ﬁlter, 97
time-stamping, 116
time-to-maturity (TTM), 18, 24, 25, 29
TIPS principal, 106
TIPS-Treasury arbitrage, 105
tracking error, 82, 83
tracking ETF, 124
tradables, 15
trade execution system, 89
traded volume, 52
trader’s outlook, 69
trader’s outlook, bearish, 19–23, 25, 30,
38
trader’s outlook, bullish, 19–22, 25, 29,
30, 37, 39
trader’s outlook, conservatively bearish,
23
trader’s outlook, conservatively bullish,
22
trader’s outlook, moderately bullish, 37
trader’s outlook, neutral, 26–29, 32–37
trader’s outlook, neutral to bearish, 19,
24, 31
trader’s outlook, neutral to bullish, 18,
24, 31
trader’s outlook, non-directional, 22, 23
trader’s outlook, strongly bearish, 31
trader’s outlook, strongly bullish, 30
trades, establishing, 58
trades, liquidating, 58
trading bounds, 125
trading costs, 16, 41, 56, 57, 59
trading day, 17, 43, 50, 53, 79, 84, 126–
128
trading portfolio, 15, 96
trading rule, 81, 119, 120
trading signal, 51, 85, 119
trading signal, faint, 16
trading strategy, 15–17, 52, 85, 90, 115
trading universe, 40, 59, 125, 127
traditional assets, 111, 112, 116
traditional portfolio, 112
training, 54, 118, 119
training data, 120, 121
training dataset, 118
training period, 53
tranche, 97–100
tranche hedging, 99
tranche MTM, 100
tranche notional, 99, 100
tranche value, 97
tranche, equity, 97, 99
tranche, junior mezzanine, 97
tranche, senior, 97
tranche, senior mezzanine, 97
tranche, super senior, 97
transaction costs, 17, 71, 77, 79, 80, 86,
87, 104, 106, 112, 115
Treasuries, 123
Treasury bill rate, 44
Treasury bills, 80, 114
Treasury bond, 76, 105, 106, 109
Treasury bond coupons, 106
Treasury curve, 102
Treasury ETF, 63, 65
Treasury Inﬂation-Protected Securities (TIPS),
105, 106
Treasury note, 105
tree boosting algorithms, 121
trend, 52, 63, 97, 122
trend component, 85
trend data mining, 116
trend following, 96
trend, ephemeral, 16
Twitter sentiment, 121
U.S. regions, 113
unadjusted close price, 126
unadjusted open price, 126
unadjusted volume, 126
uncertainty index, 80
358
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 360

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
uncompounded rate, 66
Uncovered Interest Rate Parity (UIRP),
86
underlying, 83, 84
underlying asset, 17, 76, 93
underlying index, 64, 65, 79
underlying index portfolio, 77
underlying instrument, 59, 65
underlying price, 93
underlying security, 17
underlying single-stock options, 79
underlying stock, 25, 26, 59, 62, 77, 101
underlying stock price, 101
underreaction, 122
unexpected earnings, 42
unlisted infrastructure fund, 124
USD (U.S. dollar), 86, 116
value, 42–44, 61, 73, 74, 90, 91, 123
value factor, 73
value strategy, 42, 90
value-based strategies, 116
variable coupon bond, 67
variable rate, 67
variable rate coupon payment, 76
variable, feature, 53
variable, predictor, 53
variance, 83, 88
variance notional, 84
variance strike, 84
variance swap, 84, 85
variance, conditional, 92
vector autoregressive model (VAR), 112
vector, feature, 120
Vega, 83
Vega play, 83
vertical spread, 19, 20, 22, 23
VIX (CBOE Volatility Index), 80–83
VIX futures, 81, 82
VIX futures basis, 81
VIX futures basis trading, 81
VIX futures contract, 82
VIX futures curve, 81, 82
VIX futures price, 81, 82
VIX price, 81
volatility carry, 82
volatility ETN, 82
volatility index, 81
volatility risk premium, 83
volatility skew, 84
volatility spike, 83
volatility strategy, 18, 26, 28, 30, 33–37,
78, 80
volatility target, 80
volatility targeting strategy, 80
volatility, constituent, 78
volatility, index, 78
volume, 53, 95, 96
weather, 15
weather conditions, 106, 107
weather derivative, 106, 107
weather index, 106, 107
weather risk, 106
weighted average, 44, 68, 95
weighted regression, 49, 57
weighting scheme, 41, 44, 54, 65, 95
well-diversiﬁed portfolio, 124
Whittaker-Henderson method, 85
wing, 72
winners, 40–42, 44, 95, 97
word, 120, 121
world, 122
year-on-year inﬂation swap, 105
yield, 66, 68–71, 74–76, 109
yield curve, 68–72, 74, 75
yield curve dynamics, 75
yield curve spread, 75
yield curve spread strategy, 75
YoY (year-on-year), 105, 123
zero-cost combination, 71
zero-cost long-short portfolio, 89
zero-cost portfolio, 42, 90, 91, 110, 122,
123
zero-cost strategy, 40, 72, 74, 91, 113
359
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

## Page 361

Copyright c⃝ 2018 Zura Kakushadze and Juan Andr´ es Serur. All Rights
Reserved.
zero-coupon bond, 66, 69, 70, 74
zero-coupon discount bond, 106
zero-coupon government Treasury curve,
102
zero-coupon inﬂation swap, 105, 106
zero-coupon swap, 105
360
 Electronic copy available at: https://ssrn.com/abstract=3247865 

---

