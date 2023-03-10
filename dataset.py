import torch
import pandas as pd
import numpy as np
from torch.utils.data import DataLoader, Dataset

class MNISTDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = pd.read_csv(csv_file).values
        self.transform = transform

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, index):
        X = self.data[index, 1:].reshape(28, 28)
        y = torch.tensor(self.data[index, 0], dtype=torch.int64)
        if self.transform:
            X = self.transform(X)
        return X.to(torch.float32), y
