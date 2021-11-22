#! python3
import argparse

from asl_rgb import ASL_RGB
from src.nets import CNN_Net
from src.dataloaders import Dataloader

parser = argparse.ArgumentParser()

parser.add_argument("-tsd", "--test_dataset",
                    help="Path to testing dataset")
parser.add_argument("-b", "--batch_size", help="Batch size of dataloader")
parser.add_argument("-n", "--num_workers",
                    help="Number of workers in dataloader")
parser.add_argument("-p", "--pth_file", help="File path to .pth file")
parser.add_argument(
    "-s", "--save", help="Name of the output files need to save")
parser.add_argument("-c", "--confusion_matrix", help="Show Confusion Matrix")
parser.add_argument("-o", "--output", help="Show output")

args = parser.parse_args()

BATCH_SIZE = 32
OUTPUT = False
SAVE = 'test_outputs'
NUM_WORKERS = 2
TSD = './data/results/asl_alphabet_test'
PTH = './data/results/static_asl_rgb.pth'

if args.batch_size:
    BATCH_SIZE = int(args.batch_size)
if args.output == "true":
    OUTPUT = True
if args.pth_file:
    PTH = args.pth_file
if args.num_workers:
    NUM_WORKERS = int(args.num_workers)
if args.confusion_matrix:
    CM = bool(args.confusion_matrix)
if args.test_dataset:
    TSD = args.test_dataset
if args.save:
    SAVE = args.save

params = [
    ['batch size', BATCH_SIZE],
    ['num workers', NUM_WORKERS],
    ['pth file', PTH],
    ['training dataset', TSD],
    ['save in', SAVE],
    ['outputs', "enabled" if OUTPUT else "disabled"]
]

print('{:<20} | {:<30}'.format('Parameter', 'Value'))
print('{:<20} {:30}'.format('---------------------',
      '----------------------------------------'))
for param in params:
    print('{:<20} | {:<30}'.format(param[0], param[1]))
print('\n')


if __name__ == '__main__':

    net = CNN_Net([3, 224, 224])
    dl = Dataloader()
    dl.set_path(TSD, set="test")
    dlt, dataset = dl.test_loader(batch_size=BATCH_SIZE, workers=NUM_WORKERS)

    k_v_map = dataset.class_to_idx
    ar = ASL_RGB(batch_size=BATCH_SIZE)
    ar.test(net=net, dataloader=dlt, pth=PTH, k_v_map=k_v_map)
