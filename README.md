# Hand-Sign-Recognizer

## [American Sign Language (ASL) Interpreter]

---

## Setting the Environment

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

| Argument        | Short | Help                            | Default                                | Required |
| --------------- | ----- | ------------------------------- | -------------------------------------- | -------- |
| --train_dataset | -trd  | Path to training dataset        | ./data/asl_alphabet/asl_alphabet_train | No       |
| --epochs        | -e    | Number of epochs                | 10                                     | No       |
| --learning_rate | -lr   | Learning rate                   | 1e-4                                   | No       |
| --batch_size    | -b    | Batch size of dataloader        | 64                                     | No       |
| --num_workers   | -n    | Number of workers in dataloader | 2                                      | No       |
| --save          | -s    | Name of the .pth file to save   | 'asl-interpreter-rgb.pth'              | No       |
| --output        | -o    | Show Output                     | False                                  | No       |

#### Mac OS, Linux or Unix

```bash
python3 trainer.py --trd [? path_to_train_dataset] -e [? epochs] -lr [? learning_rate] -b [? batch_size] -n [? num_workers] -s [? save_to] -o [? output]
```

#### Windows

```cmd
python trainer.py --trd [? path_to_train_dataset] -e [? epochs] -lr [? learning_rate] -b [? batch_size] -n [? num_workers] -s [? save_to] -o [? output]
```

### Testing the Model

```

```

- Static American Sign Language Interpreter using RGB Images

- dataset: <https://www.kaggle.com/grassknoted/asl-alphabet>
