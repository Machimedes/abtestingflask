import pandas as pd

df = pd.read_parquet("test.p")

df.info(verbose=True)