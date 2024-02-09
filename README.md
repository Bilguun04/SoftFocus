# SoftFocus

## Overview
SoftFocus is a Python application that allows you to blur images using the PIL (Python Imaging Library). It provides a simple interface to apply Gaussian blur to images, resulting in softened and blurred versions of the original images.

## Features
- Blur images using Gaussian blur algorithm
- Adjustable blur radius to control the level of blur
- Supports common image formats such as JPEG, PNG, etc.
- Easy-to-use command-line interface

## Requirements
- Python 3.x
- PIL (Python Imaging Library)

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Bilguun04/soft-focus.git
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install pillow
    ```

## Usage
1. Navigate to the project directory:

    ```bash
    cd soft-focus
    ```

2. Run the script with the following command:

    ```bash
    python blur_image.py input_image.jpg output_image.jpg
    ```

    Replace `input_image.jpg` with the path to your input image file and `output_image.jpg` with the desired path to save the blurred image.

    You can also specify an optional blur radius (default is 2) by adding it as a third argument:

    ```bash
    python blur_image.py input_image.jpg output_image.jpg 5
    ```

3. The blurred image will be saved to the specified output path.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
