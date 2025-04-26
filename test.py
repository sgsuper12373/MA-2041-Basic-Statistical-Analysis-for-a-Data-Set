import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Load data
df = pd.read_csv('Grouped_Imports_by_Group_All_Years.csv')

# Get all QTY and VAL columns
qty_cols = [col for col in df.columns if 'QTY' in col]
val_cols = [col for col in df.columns if 'VAL' in col]

# Calculate totals
total_qty_per_year = df[qty_cols].sum(axis=0).values
total_val_per_year = df[val_cols].sum(axis=0).values

# Section 1: Basic Statistics
print("Total QTY per year:", total_qty_per_year)
print("Total VAL per year:", total_val_per_year)
print("\nQTY Stats - Mean: %.2f, Std: %.2f" % (total_qty_per_year.mean(), total_qty_per_year.std()))
print("VAL Stats - Mean: %.2f, Std: %.2f" % (total_val_per_year.mean(), total_val_per_year.std()))

# Section 2: Visualizations with more informative plots
plt.figure(figsize=(15, 5))


# Histograms
plt.subplot(1, 3, 2)
plt.hist(total_qty_per_year, bins=5, density=True, alpha=0.6, color='blue')
plt.title("QTY Distribution")
plt.subplot(1, 3, 3)
plt.hist(total_val_per_year, bins=5, density=True, alpha=0.6, color='green')
plt.title("VAL Distribution")
plt.tight_layout()
plt.show()

# Section 3: QQ Plots for normality check
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
stats.probplot(total_qty_per_year, dist="norm", plot=plt)
plt.title("QTY QQ Plot")
plt.subplot(1, 2, 2)
stats.probplot(total_val_per_year, dist="norm", plot=plt)
plt.title("VAL QQ Plot")
plt.tight_layout()
plt.show()

# Section 4: Statistical Tests (with caution due to small sample)
print("\nNormality Tests (small sample - interpret with caution):")
print("QTY - Shapiro-Wilk p-value: %.3f" % stats.shapiro(total_qty_per_year)[1])
print("VAL - Shapiro-Wilk p-value: %.3f" % stats.shapiro(total_val_per_year)[1])

# Section 5: Alternative Approach - Analyze by Group
# Extended Section: Testing multiple distributions

distributions = {
    'gamma': ('gamma', stats.gamma),
    'normal': ('norm', stats.norm),
    'exponential': ('expon', stats.expon),
    # 'beta': ('beta', stats.beta)  # Uncomment if needed
}

def test_distributions(data, data_name):
    print(f"\nTesting distributions for {data_name}:")
    for dist_name, (scipy_name, dist_func) in distributions.items():
        try:

                params = dist_func.fit(data)
                ks_stat, p_value = stats.kstest(data, scipy_name, args=params)
                print(f"{dist_name}: KS Stat={ks_stat:.3f}, p-value={p_value:.3f}")
        except Exception as e:
            print(f"Failed to fit {dist_name}: {str(e)}")

test_distributions(total_qty_per_year, "Total QTY")
test_distributions(total_val_per_year, "Total VAL")

# Plot fitted distributions (extended version)
def plot_fitted_distributions(data, data_name):
    plt.figure(figsize=(10, 6))
    x = np.linspace(min(data), max(data), 100)
    
    # Plot histogram
    plt.hist(data, bins=5, density=True, alpha=0.3, label='Data')
    
    # Fit and plot each distribution
    dists = {
        'Normal': stats.norm,
        'Exponential': stats.expon,
        'Gamma': stats.gamma,
    }
    
    for name, dist in dists.items():
        try:
            params = dist.fit(data)
            pdf = dist.pdf(x, *params)
            plt.plot(x, pdf, label=name)
        except:
            continue
    
    plt.title(f"Fitted Distributions for {data_name}")
    plt.legend()
    plt.show()

plot_fitted_distributions(total_qty_per_year, "Total QTY")
plot_fitted_distributions(total_val_per_year, "Total VAL")