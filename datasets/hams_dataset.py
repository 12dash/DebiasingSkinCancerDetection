import pandas as pd
from PIL import Image

import torch
from torch.utils.data import Dataset

class HamDataset(Dataset):
    def __init__(self, file_, attr, label, 
                 transform = None, 
                 annotation_dir_='processed data/', 
                 img_dir_ = 'data/imgs/'
                ):
        super().__init__()
        self.file_path = annotation_dir_ + attr +'/'+ file_
        self.df = self.df = pd.read_csv(self.file_path)
        self.transform = transform

        self.img_list_ = (img_dir_ + self.df['image_id']+'.jpg').to_list()
        self.labels_ = self.df[label].to_list()
        self.attr_ = self.df[attr].to_list()
        
    def __len__(self):
        return len(self.labels_)
    
    def __convert_dtype__(self, x, dtype=torch.float32):
        return torch.tensor(x, dtype=dtype)

    def __getitem__(self, idx):
        img_path, label, attr = self.img_list_[idx], self.labels_[idx], self.attr_[idx]

        img = Image.open(img_path)
        if (self.transform is not None) : img = self.transform(img)
        label, attr = self.__convert_dtype__(label), self.__convert_dtype__(attr)
        return img, label, attr