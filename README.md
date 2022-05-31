# Glosten-Milgrom
Glosten Milgrom model is a simulation model designed to portrait the process of which information impacts the formation of transaction price in a market-maker market. The process can also be thought of how a market-maker market arrives at its price equilibrium driven by information under the competitive market settings. In particular, the key of this process is the market maker learning the fundamental value of the traded security in order to make her quotes.

## Parameter settings
- Asset value $V$ can be low ($V_L$) or high ($V_H$)
- $\delta$: The probability of bad news about $V$
- $\mu$: The fraction of insiders in the market
- $\gamma$: The probability of uninformed traders submit a buy order
- Every $N$ trade

<img src="https://imgur.com/AaLAgKg.png" width="700" height="500">

## Results of simulation
<img src="https://imgur.com/JWxP50c.png" width="700" height="500">

Figure 1: The bid and ask price at each trade

Figure 2: The transaction price at each trade

Figure 3: The profit at each trade

Figure 4: The cumulative profits

## Reference
Lawrence R. Glosten and Paul R. Milgrom. Bid, ask and transaction prices in a specialist market with heteroge- neously informed traders. Journal of Financial Economics, 13:71–100, 1985.
