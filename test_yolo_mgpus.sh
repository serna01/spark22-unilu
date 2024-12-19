#!/bin/bash -l
#SBATCH -N 1
#SBATCH --time=0-25:00:00
#SBATCH -p gpu
#SBATCH --gres=gpu:4
#SBATCH --mail-type=BEGIN,END,FAIL,INVALID_DEPEND,REQUEUE
#SBATCH --mail-user=alejandro.serna.001@student.uni.lu

cd /home/users/aserna/datasets
module load system/CUDA/
module load lang/Python/3.8.6-GCCcore-10.2.0 
source venv/bin/activate
cd /home/users/aserna/datasets/stream-1
python train_stream1_mgpus.py