# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/plot_data.csv')

print(df.to_string())
# df.plot(kind='scatter', x='Duration', y='Maxpulse')
df["Duration"].plot(kind='hist')
plt.show()