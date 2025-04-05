import math
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import stemgraphic

# TODO: Fix Dot Plot, Create actual reading of frequency table. Make Params for each function

randData = random.choices(range(1,10), k=25)
largeRandData = random.choices(range(1,100), k=25)
print(largeRandData)

def histogram(data):
    highest_value = max(data)
    bin_max_length = (highest_value * 2)

    plt.hist(data, bin_max_length, edgecolor='black')
    plt.xticks(list(range(0, highest_value + 1)))
    plt.title('Histogram')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

# histogram(randData)

def frequency_table(data):
    df = pd.DataFrame(data, columns=['Value'])
    new_frequency_table = df['Value'].value_counts().sort_index(ascending=True).reset_index()
    new_frequency_table.columns = ['Value', 'Frequency']

    return new_frequency_table

# print(frequency_table(randData))

def dot_plot(data):
    freq_table = frequency_table(data)
    for index, row in freq_table.iterrows():
        x = [row['Value']] * row['Frequency']
        print(x)
        y = list(range(1, row['Frequency'] + 1))
        plt.plot(x, y, 'bo')
    plt.title('Dot Plot')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# dot_plot(randData)

def stem_and_leaf(data):
    stemgraphic.stem_graphic(data, asc=False)
    plt.show()

stem_and_leaf(largeRandData)