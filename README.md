# image-resize
Python tool to resize a bunch of images quickly.

## Installation

Install via pip using:

`pip install image-resizer`

Get the cutting edge version using:

`pip install -e git+https://github.com/ssundarraj/image_resizer.git#egg=image_resizer`

or

Clone/download the git repo, and install using `python setup.py`.

## Usage

`image-resize input_file.jpg`

This will resize the image to `500x500` and save it as `input_file_thumbnail.jpg`



To resize to a particular size use `-s`:

`image-resize  -s 1000 1000 input_file.jpg`



To append something other than `_thumbnail` to the new image use `-a`:

`image-resize  -a _small input_file.jpg`

This will same it as `input_file_small.jpg`

