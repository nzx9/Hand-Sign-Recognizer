import torch.optim as optim


class Optimizer:
    def adamW(net, LR):
        return optim.AdamW(net.parameters(), lr=LR)

    def adam(net, LR):
        return optim.Adam(net.parameters(), lr=LR)
