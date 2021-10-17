import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    _to_linear = None
    img_cwh = [0, 0, 0]

    def __init__(self, img_cwh):
        super(Net, self).__init__()
        self.img_cwh = img_cwh
        # define NET
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 12, 5)
        self.conv3 = nn.Conv2d(12, 18, 3)

        x = torch.randn(1, self.img_cwh[0], self.img_cwh[1], self,img_cwh[2])
        self._to_linear = None
        self.convs(x)

        self.fc1 = nn.Linear(self._to_linear, 40)
        self.fc2 = nn.Linear(40, 35)
        self.fc3 = nn.Linear(35, 29)

    def convs(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv3(x)), (2, 2))

        if self._to_linear is None:
            self._to_linear = x[0].shape[0] * x[0].shape[1] * x[0].shape[2]
        return x

    def forward(self, x):
        x = self.convs(x)

        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x), dim=1)
        return x
