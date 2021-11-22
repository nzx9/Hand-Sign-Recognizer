import argparse

from asl_rgb import ASL_RGB
from src.nets import CNN_Net
from src.optimizers import Optimizer
from src.loss_functions import Loss_Fn
from src.dataloaders import Dataloader
# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-e", "--epochs", help="Number of epochs")
parser.add_argument("-lr", "--learning_rate", help="Learning rate")
parser.add_argument("-b", "--batch_size", help="Batch size of dataloader")
parser.add_argument("-n", "--num_workers",
                    help="Number of workers in dataloader")
parser.add_argument("-trd", "--train_dataset",
                    help="Path to training dataset")
# parser.add_argument("-tsd", "--test_dataset",
#                     help="Path to testing dataset")
parser.add_argument("-s", "--save", help="Name of the .pkt file to save")
parser.add_argument("-o", "--output", help="Show Output")

# Read arguments from command line
args = parser.parse_args()

EPOCHS = 10
OUTPUT = False
LR = 1e-4
BATCH_SIZE = 64
SAVE = 'asl-interpreter-rgb.pth'
NUM_WORKERS = 2
TRD = './data/asl_alphabet/asl_alphabet_train'

if args.batch_size:
    BATCH_SIZE = int(args.batch_size)
if args.output == "true":
    OUTPUT = True
if args.learning_rate:
    LR = float(args.learning_rate)
if args.num_workers:
    NUM_WORKERS = int(args.num_workers)
if args.epochs:
    EPOCHS = int(args.epochs)
if args.train_dataset:
    TRD = args.train_dataset
if args.save:
    SAVE = args.save

params = [['epochs', EPOCHS],
          ['learning rate', LR],
          ['batch size', BATCH_SIZE],
          ['num workers', NUM_WORKERS],
          ['training dataset', TRD],
          ['save as', SAVE],
          ['outputs', "enabled" if OUTPUT else "disabled"]
          ]

print('{:<20} | {:<30}'.format('Parameter', 'Value'))
print('{:<20} {:30}'.format('---------------------', '----------------------------------------'))
for param in params:
    print('{:<20} | {:<30}'.format(param[0], param[1]))
print('\n')

if __name__ == '__main_':
    ar = ASL_RGB(BATCH_SIZE, LR)
    dl = Dataloader()
    dl.set_path(TRD)
    tdl = dl.train_loader(BATCH_SIZE, NUM_WORKERS)
    net = CNN_Net([3, 224, 224])
    op = Optimizer.adamW(net, LR)
    lf = Loss_Fn.cross_entropy()
    ar.train(dataloader=tdl, net=net, epochs=EPOCHS,
             loss_func=lf, optimizer=op)
