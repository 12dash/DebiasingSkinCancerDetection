import torch.nn as nn
import torch.nn.functional as F 

import torchvision
from torchvision import models


class DenseNetModel(nn.Module):
    def __init__(self, num_last_layer = 1, device = 'cpu'):
        super().__init__()

        self.base_model = None
        self.num_last_layer = num_last_layer
        self.device = device

        self.__initialize_model__()    

    def __initialize_model__(self):
        self.base_model = models.densenet121(weights = torchvision.models.DenseNet121_Weights.IMAGENET1K_V1)
        self.base_model.classifier = nn.Sequential(nn.Linear(self.base_model.classifier.in_features, 16),
                                                   nn.Linear(16, self.num_last_layer))
    
    def forward(self, x):
        return self.base_model(x)

