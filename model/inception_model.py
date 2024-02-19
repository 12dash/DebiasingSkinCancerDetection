import torch.nn as nn
import torch.nn.functional as F 

from torchvision import models

class InceptionModel(nn.Module):
    def __init__(self, num_last_layer = 1, device = 'cpu'):
        super().__init__()

        self.base_model = None
        self.num_last_layer = num_last_layer
        self.device = device

        self.__initialize_model__()    

    def __initialize_model__(self):
        self.base_model = models.inception_v3(init_weights = True)
        self.base_model.aux_logits = False

        self.base_model.fc = nn.Sequential(nn.Linear(self.base_model.fc.in_features, 16),
                                           nn.Linear(16, self.num_last_layer))
    
    def forward(self, x):
        return self.base_model(x)

