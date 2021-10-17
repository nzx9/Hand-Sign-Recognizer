import torch
from torchvision import datasets, transforms
import os


class Dataloader:
    train_path = None
    test_path = None

    def set_path(self, path, set='train'):
        if set == "train":
            self.train_path = path
        elif set == "test":
            self.test_path = path

    def train_loader(self, batch_size, workers):
        if os.path.isdir(self.train_path):
            train_transforms = transforms.Compose([transforms.RandomRotation(30),
                                                   transforms.RandomResizedCrop(
                                                       224),
                                                   transforms.RandomHorizontalFlip(),
                                                   transforms.ToTensor(),
                                                   transforms.Normalize([0.5, 0.5, 0.5],
                                                                        [0.5, 0.5, 0.5])])

            train_dataset = datasets.ImageFolder(
                self.train_path, transform=train_transforms)
            return torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=workers, pin_memory=True)
        else:
            raise NotADirectoryError("[x] Error: Set path to training dataset")

    def test_loader(self, batch_size, workers):
        if os.path.isdir(self.test_path):
            test_transforms = transforms.Compose([transforms.Resize(224),
                                                  transforms.ToTensor(),
                                                  transforms.Normalize([0.5, 0.5, 0.5],
                                                                       [0.5, 0.5, 0.5])])

            test_dataset = datasets.ImageFolder(
                self.test_path, transform=test_transforms)

            return torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=workers)
        else:
            raise NotADirectoryError("[x] Error: Set path to testing dataset")
