# Image Optimizer
## Pre-requisites
In order to use, you will need Python 3.6 or greater installed.  
In Linux systems, it usually comes installed as default.  
To check if you have it installed, just open the terminal and run the command below:  
```shell
python3 --version
```
If you don't have it installed yet, go to [Python official website](https://www.python.org/downloads/) 
and check the installation process.
## Installation
Open the project folder in the terminal, and run the command below to install the project:
```shell
pip install -e .
```
## Usage
After installation, you can optimize an image by running:
```shell
image-optimizer input_image.[jpg,jpeg,png] output_image.[jpg,jpeg,png]
```
> [!IMPORTANT]
> The first argument is the path to the input image. For example, if you have an image called `cat.jpg` inside a folder called `animals` and you want to optimize it, you can run:
  
```shell
image-optimizer animals/cat.jpg animais/cat_optimized.jpg
```
> [!IMPORTANT]
> The **file extensions of the input and output files must be the same**. For example, if you're optimizing a `.jpg` file, the output file must also have a `.jpg` extension.
  
## Supported formats
Currently, the supported formats are `.jpg`, `.jpeg`, and `.png`.

> [!NOTE]
> If you try to optimize a GIF file using image-optimizer, the animation will be lost. I may add support for GIF optimization (keeping the animation) in the future.