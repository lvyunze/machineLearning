import numpy as np
import pandas as pd
from public import timer
df = pd.DataFrame(np.arange(100000000).reshape((50000000, 2)), columns=['A', 'B'])
compressed_file = 'compressed.feather'
df.to_feather(compressed_file, compression='zstd', compression_level=2)
df.to_csv("csv_file.csv", index=False)


@timer
def get_feather_file(feather_file):
    feather_df = pd.read_feather(feather_file)
    print(feather_df)


@timer
def get_csv_file(csv_file):
    csv_df = pd.read_csv(csv_file)
    print(csv_df)


if __name__ == '__main__':
    get_feather_file("compressed.feather")
    get_csv_file("csv_file.csv")
