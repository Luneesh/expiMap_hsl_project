# Introduction

As part of our externship project for the **Bioinformatics faculty at the University of Applied Sciences Leiden**, we were required to review and reproduce Figures 2 and 4 from the document [Biologically informed deep learning to query gene programs in single-cell atlases](https://www.nature.com/articles/s41556-022-01072-x). This led to some issues that needed to be resolved due to the outdated scripts (after all, the code was written back in 2020).

# Installation
In the process of trying to understand how the scripts work, we discovered several things, spending a fair amount of time on it (don’t be foolish—read instructions more often and ask questions frequently). The article uses a refork of the `scArches` module, version approximately 0.3.5, which currently has an updated version 0.6.1.

As of 12.11.2024, we have found the following method to set up the required environment; the instructions below are specifically written for `wheel`:


1. Torch installation
```bash
   pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
   ```
**For GPU supporting CUDA**
```bash
pip install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
```
**For CPU**

2. Site-Packages 
```bash
pip install -r requirements.txt --no-dependencies
```

```bash
pip install pytorch-lightning==1.3.8
```

```bash
   pip install fsspec==2021.11.0
   ```

5. scArches 
```bash
pip install <pathway> --no-dependencies
```
Download the `scarches-soft_new_mask` package from the provided link and install it. However, due to an error, don’t forget to note in Git that during installation, the path `./scarches-soft_new_mask/scarches/trainers/scgen` is missing. This results in an initialization error due to the incomplete package—`./trainers/scgen` is missing. You’ll need to manually add it to the root.



# expiMap reproducibility

Immune healthy atlas  
https://drive.google.com/file/d/1oKpcxQSm238SMNY77TAR5bzKUMIqgGU_/view?usp=sharing

PBMC IFN-beta  
https://drive.google.com/file/d/1wg_21to_sNzDmoWq6vOxWdG4-9ZWldql/view?usp=sharing

PBMC COVID-19  
https://drive.google.com/file/d/1WhmpTHoDXLyq4sOc6viRDEuCZ8Nz2q86/view?usp=sharing

Mouse endocrinogenesis  
https://drive.google.com/file/d/1lJ1AdHsfdiQHDaaO6eG9F95USmMBXOkW/view?usp=sharing

Heart from scVI used for the integration benchmark  
https://drive.google.com/file/d/1Z2ZFTotQxwth3jUGCPiawq-ZCOPlgKBy/view?usp=sharing

Code to run  
https://github.com/theislab/scarches/tree/soft_new_mask

For the new api use  
https://github.com/theislab/scarches
