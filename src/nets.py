import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN_Net(nn.Module):
    _to_linear = None
    def __init__(self, chw_dim):
        super(CNN_Net, self).__init__()
        
        # define NET
        self.conv1 = nn.Conv2d(3, 64, 3)
        self.conv2 = nn.Conv2d(64, 128, 3)
        self.conv3 = nn.Conv2d(128, 256, 3)
        self.conv4 = nn.Conv2d(256, 512, 3)
        
        x = torch.randn(1, chw_dim[0], chw_dim[1], chw_dim[2])
        self._to_linear = None
        self.convs(x)
        
        self.fc1 = nn.Linear(self._to_linear, 29)
#         self.fc2 = nn.Linear(4048, 1024)
#         self.fc3 = nn.Linear(1024, 29)
        
        
    
    def convs(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv3(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv4(x)), (2,2))
                              
        if self._to_linear is None:
            self._to_linear = x[0].shape[0] * x[0].shape[1] * x[0].shape[2]
        return x
    
    def forward(self, x):
        x = self.convs(x)
        
        x = torch.flatten(x, 1)
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
        x = F.softmax(self.fc1(x), dim=1)
        return x