import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
data_folder = Path('C:/Users/langzx/Desktop/github/HsML/data')

housing = pd.read_csv(data_folder/'housing/housing.csv')
housing.info()
housing.describe()
housing.hist(bins=50, figsize=(20,15))

## great test set

def split_train_test(data, test_ratio):
shuffled_indices = np.random.permutation(len(data))
test_set_size = int(len(data) * test_ratio)
test_indices = shuffled_indices[:test_set_size]
train_indices = shuffled_indices[test_set_size:]
return data.iloc[train_indices], data.iloc[test_indices]