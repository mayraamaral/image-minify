# Image Optimizer
## Summary
- [Pre-requisites](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#pre-requisites)
- [Installation](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#installation)
- [Usage](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#usage)
- [Supported formats](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#supported-formats)
- [Running tests](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#running-tests)
    - [Steps to run tests](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#steps-to-run-tests)
    - [Example output](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#example-output)
- [Author](https://github.com/mayraamaral/image-optimizer?tab=readme-ov-file#author)
  
## Pre-requisites
In order to use, you will need Python 3.6 or greater installed. In Linux systems, it usually comes installed as default.  
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
  
### Optional parameters
In addition to the mandatory input and output file paths, the `image-optimizer` offers optional parameters to customize the behavior of the image optimization process. These parameters give you control over the compression quality, resizing scale, and the verbosity of the process. Below is a detailed explanation of each optional parameter:

- `--quality`
**Description:** This parameter controls the quality of the image after compression. The value must be an integer between 0 (maximum compression, lowest quality) and 100 (no compression, maximum quality).
**Default value:** `85`
  
Usage:
```shell
image-optimizer input_image.jpg output_image.jpg --quality 75
```
This example will compress the image and save it with a quality level of 75.
- `--scale`
**Description:** This parameter allows you to resize the image by a given scale factor. The value must be a float between 0.1 (10% of the original size) and 1.0 (100%, i.e., no resizing).
**Default value:** `0.8`
  
Usage:
```shell
image-optimizer input_image.jpg output_image.jpg --scale 0.5
```
This example resizes the image to 50% of its original dimensions.
- `--verbose` / `--no-verbose`
**Description:** This boolean flag controls whether to print messages about the optimization process. By default, `--verbose` is enabled, which prints a message when the image is successfully optimized. You can disable this by using `--no-verbose`.
Default value: `--verbose` (enabled by default)
  
Usage:  
Verbose output (enabled):
```shell
image-optimizer input_image.jpg output_image.jpg --verbose
```
This will display a success message after the image is optimized.

No verbose output (disabled):
```shell
image-optimizer input_image.jpg output_image.jpg --no-verbose
```
This will suppress any messages during the optimization process.
## Supported formats
Currently, the supported formats are `.jpg`, `.jpeg`, and `.png`.

> [!NOTE]
> If you try to optimize a GIF file using image-optimizer, the animation will be lost. I may add support for GIF optimization (keeping the animation) in the future.
  
## Running tests
To ensure that everything is working correctly, you can run the provided unit tests. These tests validate that the image-optimizer behaves as expected in various scenarios (e.g., handling valid and invalid input files).

### Steps to run tests
Open your terminal in the root project folder. Then run the following command to execute all the tests:
```shell
python -m unittest discover
```
This command will automatically discover and run all test files in the project.
### Example output
If the tests pass, you should see output like this:
```shell
....
----------------------------------------------------------------------
Ran 4 tests in 0.015s

OK
```
## Author
This project was made with ❤️ by [mayraamaral](https://github.com/mayraamaral).