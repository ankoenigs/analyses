import pandas as pd
import re
import env

testfile = env.SIEGFRIED_FILES_PATH + "/Deluxe/" + "siegfried_deluxe_py.csv"
prefix_for_splitting = "namespace"

def read_file():
    df = pd.read_csv(testfile) # Todo: Validate input
    return df

def split_file(df):
    '''Split monolithic input file from deluxe.sig into individual '''
    start_indices = [df.columns.get_loc(col_name) for col_name in df.columns.to_list() if col_name.startswith(prefix_for_splitting)]
    # find length of boilerplate part
    df_boilerplate = df.iloc[:, :start_indices[0]].dropna(axis=1)
    # find start- and endpoints of different parts
    indices = []
    for x, idx in enumerate(start_indices):
        fin = -1
        if x+1 < len(start_indices):
            fin = start_indices[x+1]
        indices.append((idx, fin))
    new_dfs = []
    for tuple in indices:
        new_dfs.append(pd.concat([df_boilerplate,df.iloc[:, tuple[0]:tuple[1]]], axis=1))
    return new_dfs

# find out length of Index
# first start - exclusive border of boilerplate code 
# first from this list minus 1
# and then pop(0) or iterate over this in order to create individual data frames
# todo: how to create these data frames...

if __name__ == "__main__":
    data = read_file()
    print(split_file(data))