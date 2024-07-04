import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset
tips = sns.load_dataset('tips')

# Line graph
plt.figure(figsize=(10,6))
plt.plot(tips['total_bill'], label='Total Bill')
plt.plot(tips['tip'], label='Tip')
plt.xlabel('Index')
plt.ylabel('Amount ($)')
plt.title('Line Graph: Total Bill vs Tip')
plt.legend()
plt.show()

# Bar graph
plt.figure(figsize=(10,6))
tips.groupby('sex')['total_bill'].mean().plot(kind='bar')
plt.xlabel('Sex')
plt.ylabel('Average Total Bill ($)')
plt.title('Bar Graph: Average Total Bill by Sex')
plt.show()

# Scatter plot
plt.figure(figsize=(10,6))
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.title('Scatter Plot: Total Bill vs Tip')
plt.show()
