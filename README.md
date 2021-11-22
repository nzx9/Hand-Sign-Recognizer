# Hand-Sign-Recognizer

![python](https://img.shields.io/static/v1?logo=python&labelColor=3776AB&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Python3)
![pytorch](https://img.shields.io/static/v1?logo=pytorch&labelColor=EE4C2C&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Pytorch)

![linux](https://img.shields.io/static/v1?logo=linux&labelColor=FCC624&color=ffffff&logoColor=000000&style=flat-square&label=%20&message=Linux)
![macos](https://img.shields.io/static/v1?logo=macos&labelColor=000000&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=macOS)
![windows](https://img.shields.io/static/v1?logo=windows&labelColor=0078D6&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Windows)

- Supported for Static RGB Images

- Pretrained Model :  
  <https://github.com/nzx9/Hand-Sign-Recognizer/blob/main/models/pretrained_models/static_asl_rgb.pth>

- Pretrained Model Used American Sign Language (ASL)

- Pretrained Model Trained Using : <https://www.kaggle.com/grassknoted/asl-alphabet>

## Setting Up the Environment

### Mac OS, Linux Or Unix

1. Install python 3.6+ version
2. Install pip3
3. Open the `terminal` and clone the repository by running,

```bash
git clone https://github.com/nzx9/Hand-Sign-Recognizer.git
```

4. Navigate to the project folder,

```bash
cd Hand-Sign-Recognizer
```

5. Create virutal environment and activate the env

```bash
python3 -m env ./env
source ./env/bin/activate
```

6. Install the requiements by running,

```bash
pip3 install requirements.txt
```

### Windows

1. Install python 3.6+ version
2. Install pip3
3. Open the CLI and clone the repository by running,

```bash
git clone https://github.com/nzx9/Hand-Sign-Recognizer.git
```

## Usage

### Training the Model

#### Arguements

| Argument        | Short | Help                            | Default                                |
| --------------- | ----- | ------------------------------- | -------------------------------------- |
| --train_dataset | -trd  | Path to training dataset        | ./data/asl_alphabet/asl_alphabet_train |
| --epochs        | -e    | Number of epochs                | 10                                     |
| --learning_rate | -lr   | Learning rate                   | 1e-4                                   |
| --batch_size    | -b    | Batch size of dataloader        | 64                                     |
| --num_workers   | -n    | Number of workers in dataloader | 2                                      |
| --save          | -s    | Name of the .pth file to save   | 'asl-interpreter-rgb.pth'              |
| --output        | -o    | Show Output                     | False                                  |

#### Mac OS, Linux or Unix

```bash
python3 trainer.py -trd [? path_to_train_dataset] -e [? epochs] -lr [? learning_rate] -b [? batch_size] -n [? num_workers] -s [? save_to] -o [? output]
```

#### Windows

```cmd
python trainer.py -trd [? path_to_train_dataset] -e [? epochs] -lr [? learning_rate] -b [? batch_size] -n [? num_workers] -s [? save_to] -o [? output]
```

### Testing the Model

#### Arguements

| Argument           | Short | Description                                 | Default                           |
| ------------------ | ----- | ------------------------------------------- | --------------------------------- |
| --test_dataset     | -tsd  | Path to testing dataset                     | ./data/results/asl_alphabet_test  |
| --batch_size       | -b    | Batch size of dataloader                    | 32                                |
| --num_workers      | -n    | Number of workers in dataloader             | 2                                 |
| --pth_file         | -p    | File path to .pth file                      | ./data/results/static_asl_rgb.pth |
| --save             | -s    | Name of the output files need to save       | test_outputs                      |
| --confusion_matrix | -c    | Show Confusion Matrix (Not Implemented Yet) | -                                 |
| --output           | -o    | Show output                                 | False                             |

#### Mac OS, Linux or Unix

```bash
python3 tester.py -tsd [? path_to_test_dataset] -b [? batch_size] -n [? num_workers] -p [? pth_file] -s [? save_to] -c [? confusion_matrix] -o [? output]
```

#### Windows

```cmd
python tester.py -tsd [? path_to_test_dataset] -b [? batch_size] -n [? num_workers] -p [? pth_file] -s [? save_to] -c [? confusion_matrix] -o [? output]
```

## License

[BSD-3-Clause License](https://github.com/nzx9/dsc/blob/main/LICENSE)
