# spark22-unilu
Spark 2022 challenge

# YOLO Dataset Directory Setup

This document provides instructions on how to set up the directory structure for training and testing a YOLO model with the provided dataset.

## Directory Structure

The main directory is `datasets`, which contains subdirectories and files for each data stream. Below is the directory layout for `stream-1`:

```plaintext
datasets/
├── stream-1/
│   ├── images/
│   ├── labels/
│   ├── train_stream1_mgpus.py
│   ├── test_yolo_mgpus.sh
│   ├── stream1.yaml
├── stream-2/
│   ├── images/
│   ├── labels/
│   ├── ...
```

### Explanation of Subdirectories and Files

- **`images/`**  
  This directory contains all the images for training and testing. Images should be organized and named appropriately to correspond with their label files in the `labels/` directory.

- **`labels/`**  
  This directory contains the YOLO-compatible label files. Each `.txt` file corresponds to an image in the `images/` directory and defines the bounding box coordinates and class information.

- **`train_stream1_mgpus.py`**  
  Python script for training the YOLO model on multiple GPUs using the `stream-1` dataset.

- **`test_yolo_mgpus.sh`**  
  Shell script for testing the YOLO model on multiple GPUs. This script uses the trained model weights and the `stream1.yaml` configuration.

- **`stream1.yaml`**  
  YAML configuration file specifying the dataset paths, classes, and other settings required for YOLO training and testing.  

## Running the Training Code on an HPC Cluster

To train the YOLO model on an HPC (High-Performance Computing) cluster, follow these steps:

### 1. Submit the Job
Use the `sbatch` command to submit the training job using the provided `test_yolo_mgpus.sh` script:

```bash
sbatch datasets/stream-1/test_yolo_mgpus.sh
```
### 2. Monitor the job
```bash
sq
```
### 3. Wait until the job finishes
current setup with spark 2022 dataset takes up to 20 hours so be patient
if the .sh file was properly setup, you should receive an email with the begin and finish job 

## Training Output Directory Structure

When the training phase completes, a new directory called `runs` is created. This directory contains all the results and artifacts generated during the training process. Below is a detailed description of the structure and contents:

### Directory Structure

```plaintext
runs/
└── detect/
    └── trainX/  # X corresponds to the number of the training run (e.g., train1, train75, etc.)
        ├── confusion_matrix.png  # Visualization of the model's performance
        ├── results.csv          # Summary of the training epochs and main parameters
        ├── results.png          # Graphs for metrics like loss and mAP over epochs
        ├── weights/
            ├── best.pt          # Model weights with the best performance during training
            ├── last.pt          # Model weights at the end of training

```


### Key Files and Folders

- **`confusion_matrix.png`**  
  A graphical representation of the confusion matrix, showing the model's classification performance.

- **`results.csv`**  
  A CSV file summarizing the training metrics, including loss, mAP (mean Average Precision), and other key parameters for each epoch.

- **`results.png`**  
  Visualizations of training metrics such as loss, mAP, and accuracy trends across epochs.

- **`weights/` Folder**  
  This folder contains the saved model weights:
  - `best.pt`: The weights file corresponding to the best-performing epoch during training.
  - `last.pt`: The weights file corresponding to the final epoch of training.

### Notes

- Each training run creates a new subdirectory under `runs/detect/` with a unique name (e.g., `train1`, `train2`, etc.).
- You can use the `best.pt` weights for inference or further fine-tuning, as it represents the model's best performance.
- To review the training results, open the `.png` files or analyze the `results.csv` file.

This structure ensures all key outputs from the training phase are organized and easily accessible for analysis and future use.


## Submitting Results to the SPARK 2022 Challenge

To submit the results to the **SPARK 2022 Challenge**, follow the steps below. The challenge details and submission platform can be found here:  
[SPARK 2022 Challenge - Submit Results](https://codalab.lisn.upsaclay.fr/competitions/9079#participate-submit_results)

---

### 1. Generate the Submission File

Run the `submission.py` script to generate a `submission.csv` file containing the test results in the required format:

```bash
python submission.py
```

To run it on the HPC, since the test directoy has 22000 images:

```bash
sbatch datasets/stream-1/test_submission.sh
```
Finally download the generated .csv, compress it into .zip file and upload the .zip for evaluation to the spark challenge webpage.

