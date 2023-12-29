import pandas as pd

def load_data(path):
    df = pd.read_json(path)
    df_expanded = df['user'].apply(lambda x: pd.Series(x))
    df = pd.concat([df.drop('user', axis=1), df_expanded], axis=1)
    return df

df = load_data("./data/test.json")
df_raw = load_data("./data/rawtest.json")

assert set(df["label"]) == {"human", "bot"}
assert list(df["id"]) == list(df_raw["id"])

print("检测通过")