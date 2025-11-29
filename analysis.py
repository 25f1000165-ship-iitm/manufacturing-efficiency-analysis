
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
efficiency_rates = [73.05, 75.67, 79.47, 79.18]
average_efficiency = 76.84
industry_target = 90

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(quarters, efficiency_rates, marker='o', linestyle='-', color='b', label='Quarterly Efficiency Rate')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target}%)')
plt.axhline(y=average_efficiency, color='g', linestyle=':', label=f'Average Efficiency ({average_efficiency}%)')

# Add labels and title
plt.title('Equipment Efficiency Rate - 2024 Quarterly Data')
plt.xlabel('Quarter')
plt.ylabel('Efficiency Rate (%)')
plt.ylim(70, 95)
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('efficiency_trend.png')

print("Analysis complete. Chart saved as efficiency_trend.png")
