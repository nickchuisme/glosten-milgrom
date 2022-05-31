import numpy as np
import matplotlib.pyplot as plt


class Glosten_Milgrom():

    V_LOW = 100
    V_HIGH = 200
    MU = 0.3
    DELTA = 0.5
    GAMMA = 0.8
    T_MAX = 50

    def __init__(self):
        self.init_value = None
        self.ask = [self.V_HIGH]
        self.bid = [self.V_LOW]
        self.prices = [self.V_LOW * (1 - self.DELTA) + self.V_HIGH * self.DELTA]

        self.gm_model()

    def gm_model(self):
        # initialise real value and sequence of traders
        self.init_value = np.random.choice([self.V_LOW, self.V_HIGH], p=[self.DELTA, 1 - self.DELTA])
        traders = np.random.choice(['I', 'U'], p=[self.MU, 1 - self.MU], size=self.T_MAX)

        for trader in traders:
            # define action is a BUY or SELL order
            if trader == 'I':
                if self.init_value == self.V_HIGH:
                    action = 'B'
                else:
                    action = 'S'
            elif trader == 'U':
                action = np.random.choice(['B', 'S'], p=[self.GAMMA, 1 - self.GAMMA])

            # market makers make price
            bidask, price, self.DELTA = self.make_price(buy_action=(action=='B'))
            if bidask == 'bid':
                self.bid.append(price)
                self.ask.append(self.ask[-1])
            else:
                self.ask.append(price)
                self.bid.append(self.bid[-1])
            self.prices.append(price)

    def make_price(self, buy_action=True):
        # calculate conditional probability
        prob_buy = (1 - self.DELTA) * self.MU + (1 - self.DELTA) * (1 - self.MU) * self.GAMMA + self.DELTA * (1 - self.MU) * self.GAMMA
        prob_sell = 1 - prob_buy
        prob_low_buy = self.DELTA * (1 - self.MU) * self.GAMMA
        prob_low_sell = self.DELTA * self.MU + self.DELTA * (1 - self.MU) * (1 - self.GAMMA)
        prob_high_buy = (1 - self.DELTA) * self.MU + (1 - self.DELTA) * (1 - self.MU) * self.GAMMA
        prob_high_sell = (1 - self.DELTA) * (1 - self.MU) * (1 - self.GAMMA)

        # update market maker's belief
        if buy_action:
            price = (self.V_LOW * prob_low_buy / prob_buy) + (self.V_HIGH * prob_high_buy / prob_buy)
            return 'ask', price, (prob_low_buy / prob_buy)
        else:
            price = (self.V_LOW * prob_low_sell / prob_sell) + (self.V_HIGH * prob_high_sell / prob_sell)
            return 'bid', price, (prob_low_sell / prob_sell)

    def plot_result(self):
        fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(10,6))
        axes = axes.ravel()

        axes[0].plot(self.bid, 'g', label='bid')
        axes[0].plot(self.ask, 'r', label='ask')
        axes[0].legend()

        axes[1].plot(self.prices, 'b', label='price')
        axes[1].legend()

        axes[2].plot(np.array(self.prices) - self.init_value, label='profit')
        axes[2].legend()

        axes[3].plot(np.cumsum(np.array(self.prices) - self.init_value), label='cumulative profit')
        axes[3].legend()
        fig.suptitle(f'True price: {self.init_value}')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    gm = Glosten_Milgrom()
    gm.plot_result()