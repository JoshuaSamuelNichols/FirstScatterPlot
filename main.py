# Numpy, Pandas and Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Generate data
np.random.seed(0)
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

# Step 2: Create a DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# Step 3: Create a scatter plot
plt.scatter(data['x'], data['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.grid(True)

# Step 4: Show the plot
plt.show()

