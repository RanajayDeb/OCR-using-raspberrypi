#OCR using raspberrypi

##Image capture using raspberrypi
Using the Raspberry Pi camera and the Python module, picamera, it's a pretty trivial task. This guide will walk you through the process of setting up the camera and writing a Python script to snap a picture.

## Capture

```
cd page-dewarp
```
```
cd example_input
```
```
python3 test2.py
```

For adjusting camera position, focus and page positioning

```
libcamera-hello -t 0 --width 480 --height 640
```
## Page dewarping

Document image dewarping library using a cubic sheet model

Python 3 library for page dewarping and thresholding,
[available on PyPI](https://pypi.org/project/page_dewarp/).

## Requirements

Python 3 and NumPy, SciPy, SymPy, Matplotlib, OpenCV, and TOML Kit are required to run `page-dewarp`.

- See [`CONDA_SETUP.md`](https://github.com/lmmx/page-dewarp/blob/master/CONDA_SETUP.md) for
  an example conda environment 
- If you prefer to install everything from pip, run `pip install page-dewarp`

This library was renovated from the [original (2016) Python 2 script](https://github.com/mzucker/page_dewarp/)
by Matt Zucker, which you can use if you are somehow still using Python 2.
- PDF conversion not yet implemented

To try out an example image, run

```sh
git clone https://github.com/lmmx/page-dewarp
cd page-dewarp
mkdir results && cd results
page-dewarp ../example_input/boston_cooking_a.jpg
```

## Explanation and extension to Gpufit

A book on a flat surface can be said to be 'fixed to zero' at the endpoints of a curve, which
you can model as a cubic (see [`derive_cubic.py`](derive_cubic.py))

The "cubic Hermite spline" is one of the models supported by
[Gpufit](https://github.com/gpufit/Gpufit/), a library for Levenberg Marquardt curve fitting in
CUDA (C++ with Python API).

_[Work in progress]_

- See full writeup on [Matt Zucker's blog](https://mzucker.github.io/2016/08/15/page-dewarping.html)
- See [lecture](https://www.cs.cornell.edu/courses/cs4620/2013fa/lectures/16spline-curves.pdf)
  on splines by Steve Marschner for more details and how a spline can be represented in matrix form.
- Brief notes on this project are over on [my website](https://doc.spin.systems/page-dewarp)

## OCR using pytesseract

Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.

Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.

Pip install pytesseract command-
```
pip install pytesseract
```

Finding ocr output of the captured input

```
/page-dewarp/results $ python3 ocr.py

The python file needs to be called from directory from results
```

## Image capture & Ocr needs to be called from two different terminals
