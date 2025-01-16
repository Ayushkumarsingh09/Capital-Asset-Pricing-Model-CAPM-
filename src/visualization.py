import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_beta_vs_market(stock_returns, market_returns, stock_name):
        """Plot stock returns vs. market returns with beta line."""
        plt.figure(figsize=(8, 6))
        plt.scatter(market_returns, stock_returns, alpha=0.6, label="Daily Returns")
        plt.title(f"Beta Visualization for {stock_name}")
        plt.xlabel("Market Returns")
        plt.ylabel(f"{stock_name} Returns")
        plt.legend()
        plt.savefig(f"data/outputs/charts/beta_vs_market_{stock_name}.png")
        plt.close()

    @staticmethod
    def plot_expected_returns(expected_returns):
        """Bar chart of expected returns for all stocks."""
        plt.figure(figsize=(10, 6))
        plt.bar(expected_returns.keys(), expected_returns.values(), color="skyblue")
        plt.title("Expected Returns (CAPM)")
        plt.xlabel("Stocks")
        plt.ylabel("Expected Returns")
        plt.savefig("data/outputs/charts/expected_returns.png")
        plt.close()
