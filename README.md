<p align="center">
  <img src= "scripts/icon.png" height=100>
</p>

<div align="center">

## TheaterGen: Character Management with LLM for Consistent Multi-turn Image Generation
[📄[Original Paper](https://arxiv.org/abs/2404.18919)] &emsp; [🚩[Project Page](https://howe140.github.io/theatergen.io/)]

This repository contains my implementation and improvements to the TheaterGen project.
</div>

## 🔥 Local Setup Guide

## 1. Conda Setup

```bash
conda create -n theaterGen python=3.10
conda activate theaterGen
```

### 2. Model Downloads
The notebook is for reference. setup the path manually.
Run the provided `app.ipynb` notebook to automatically download required model files:
Create a folder with name `1.5` and download required files.
- VAE Model
- UNET Model
- Text Encoder
- Other necessary components
- create visualization folder in root directory


### 3. GroundingDINO Setup
```bash
# Clone GroundingDINO repository
git clone https://github.com/IDEA-Research/GroundingDINO.git
cd GroundingDINO

# Install required packages
pip install -r requirements.txt

# Download the model weights
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
```

Move the downloaded weights to the appropriate directory structure:

```bash
└── GroudingDino
    └── groundingdino_swint_ogc.pth
```
### 4. Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

### 🚀 Generate Images
Run the generation script with the benchmark dataset:
```bash
python generate.py --task story --sd_version '1.5' --dataset_path CMIGBench
```

### 🎯 My Results
Here are some examples of the results I achieved using the modified implementation:

see the ```database_1.5``` and ```cmigbench_1.5``` directroy


### 📊 Evaluation
Organize your output in the following structure:

```bash 
└── output_dir
    └── dialogue 1
        ├── turn1.png 
        ├── turn2.png 
        ├── turn3.png 
        └── turn4.png
```

### Run evaluation:
```bash
python CMIGBench/eval/eval.py 
python CMIGBench/eval/eval_extra.py
```

### 💡 Acknowledgements

This work is based on:
- Stable Diffusion
- Grounded-SAM
- T2I-Adapter
- IP-Adapter

### 📝 Citation

If you use this code, please cite the original paper:
```bash
@article{cheng2024theatergen,
  title={TheaterGen: Character Management with LLM for Consistent Multi-turn Image Generation},
  author={Cheng, Junhao and Yin, Baiqiao and Cai, Kaixin and Huang, Minbin and Li, Hanhui and He, Yuxin and Lu, Xi and Li, Yue and Li, Yifei and Cheng, Yuhao and others},
  journal={arXiv preprint arXiv:2404.18919},
  year={2024}
}
```