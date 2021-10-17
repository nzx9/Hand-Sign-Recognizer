import torch
from tqdm import tqdm

class ASL_RGB:
    DEVICE = torch.device("cpu")

    def __init__(self, batch_size, learning_rate, device=None):
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.DEVICE = torch.device(
            "cuda:0" if torch.cuda.is_available() else device if device != None else "cpu")
        print("Executing on: {}".format(self.DEVICE))


    def count_correct(outputs, labels):
        _, predicted = torch.max(outputs.data, 1)
        total = labels.size(0)
        correct = (predicted == labels).sum().item()
        return [total, correct]

    def print_count_correct(total, correct):
        print('Total   : {}'.format(total))
        print('Correct : {}'.format(correct))
        print('Accuracy:  %.3f%%' %(100 * correct / total))

    def train(self, net, dataloader, loss_func, optimizer, epochs):
        correct, total = 0, 0
        net.to(self.DEVICE)
        print("training started...")
        for epoch in range(epochs):
            epoch_loss = 0.0
            for i, data in enumerate(tqdm(dataloader)):
                inputs, labels = data[0].to(
                    self.DEVICE), data[1].to(self.DEVICE)

                optimizer.zero_grad()
                outputs = net(inputs)
                loss = loss_func(outputs, labels)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
                cc = self.count_correct(outputs, labels)
                total += cc[0]
                correct += cc[1]
                

            print('[epoch: %d] loss: %.3f%%' %(epoch + 1, running_loss))
            self.print_count_correct(total, correct)
            running_loss = 0.0
            total, correct = 0, 0

        print('training complete...')

    def test(self, net, dataloader):
        correct = 0
        total = 0

        with torch.no_grad():
            for data in dataloader:
                images, labels = data[0].to(
                    self.DEVICE), data[1].to(self.DEVICE)

                outputs = net(images)

                _, predicted = torch.max(outputs.data, 1)

                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        self.print_correct_count(total, correct)
        print('Better than random: {}'.format(100 * 1 / 28 < (100 * correct / total)))
