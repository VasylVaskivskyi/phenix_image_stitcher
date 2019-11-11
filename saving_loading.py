import pandas as pd
import re


def load_param(dir_path, scan):
    if scan == 'auto':
        def load_txt(path):
            li = []
            with open(path) as f:
                for line in f.readlines():
                    line = re.sub(r"[\n\s']+", '', line).split(',')
                    line = [int(i) if i != 'zeros' else i for i in line]
                    li.append(line)
            return li

        ids = load_txt(dir_path + 'image_ids.txt')
        x_size = load_txt(dir_path + 'x_size.txt')
        y_size = load_txt(dir_path + 'y_size.txt')

    elif scan == 'manual':
        ids = pd.read_csv(dir_path + 'image_ids.csv', index_col=0, header='infer', dtype='object')
        x_size = pd.read_csv(dir_path + 'x_sizes.csv', index_col=0, header='infer', dtype='int64')
        y_size = pd.read_csv(dir_path + 'y_sizes.csv', index_col=0, header='infer', dtype='int64')
        # convert column names to int
        ids.columns = ids.columns.astype(int)
        x_size.columns = x_size.columns.astype(int)
        y_size.columns = y_size.columns.astype(int)
        # convert data to int where possible
        for j in ids.columns:
            for i in ids.index:
                try:
                    val = ids.loc[i, j]
                    val = int(val)
                    ids.loc[i, j] = val
                except ValueError:
                    pass
    return ids, x_size, y_size


def save_param(dir_path, scan, ids, x_size, y_size):
    if scan == 'auto':
        def save_txt(path, li):
            with open(path, 'w') as f:
                for row in li:
                    f.write(','.join(str(i) for i in row) + '\n')

        save_txt(dir_path + 'image_ids.txt', ids)
        save_txt(dir_path + 'x_sizes.txt', ids)
        save_txt(dir_path + 'y_sizes.txt', ids)
    elif scan == 'manual':
        ids.to_csv(dir_path + 'image_ids.csv')
        x_size.to_csv(dir_path + 'x_sizes.csv')
        y_size.to_csv(dir_path + 'y_sizes.csv')
