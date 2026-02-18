import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Create portfolio
n_loans = 100

data = pd.DataFrame({
    "Exposure": np.random.randint(10000, 100000, n_loans),
    "PD": np.random.uniform(0.01, 0.05, n_loans),
    "LGD": np.random.uniform(0.3, 0.6, n_loans)
})

data["EAD"] = data["Exposure"]

# Monte Carlo simulation
simulations = 10000
portfolio_losses = []

for i in range(simulations):
    
    # Random shock to PD (normal noise)
    pd_shock = np.random.normal(1, 0.2, n_loans)
    stressed_pd = data["PD"] * pd_shock
    
    # Make sure PD stays between 0 and 1
    stressed_pd = np.clip(stressed_pd, 0, 1)
    
    # Calculate loss for this scenario
    loss = stressed_pd * data["LGD"] * data["EAD"]
    
    portfolio_losses.append(loss.sum())

portfolio_losses = np.array(portfolio_losses)

# Calculate VaR at 95%
VaR_95 = np.percentile(portfolio_losses, 95)

print("Average Portfolio Loss:", portfolio_losses.mean())
print("95% VaR:", VaR_95)

# Plot distribution
plt.hist(portfolio_losses, bins=50)
plt.axvline(VaR_95)
plt.title("Monte Carlo Portfolio Loss Distribution")
plt.show()

