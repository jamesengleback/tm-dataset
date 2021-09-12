import pandas as pd
import torch
from torch import cat, Tensor, LongTensor
from torch.utils.data import Dataset
from torch.nn.functional import one_hot

DNA = {'A':0,
       'C':1,
       'G':2,
       'T':3}


class TmData(Dataset):
    def __init__(self, 
                 path,
                 max_len=30):
        self.max_len = max_len
        self.df = pd.read_csv(path)
        self.x = one_hot(\
                    cat(\
                        list(map(lambda seq : LongTensor([DNA[i] for i in seq] \
                                                       + [0 for _ in range(max_len - len(seq))]\
                                                       ).unsqueeze(0),
                              self.df['seq']))))
        self.y  = torch.from_numpy(self.df['tm'].values)

    def __len__(self):
        return len(self.df)
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]
