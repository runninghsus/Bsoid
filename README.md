# B-SOiD

![Version](https://img.shields.io/github/v/release/runninghsus/Bsoid) ![Code size](https://img.shields.io/github/languages/code-size/runninghsus/Bsoid) ![License](https://img.shields.io/github/license/runninghsus/Bsoid) ![Open issues](https://img.shields.io/github/issues/YttriLab/B-SOID) ![Stars](https://img.shields.io/github/stars/YttriLab/B-SOID?style=social)

## Why B-SOiD?

  - DeepLabCut has revolutionized the way behavioral scientists analyze data. The algorithm utilizes recent advances in computer vision and deep learning to automatically estimate 3D-poses. Interpreting the positions of an animal can be useful in studying behavior; however, it does not encompass the whole dynamic range of naturalistic behaviors.
  
  - Behavioral segmentation of open field in DeepLabCut, or B-SOID ("B-side"), is an unsupervised learning algorithm that serves to discover behaviors that are not pre-defined by users. Our algorithm can segregate statistically different sub-second rodent behaviors with a single video-camera. Upon estimating the positions, this algorithm agnostically separates statistically significant distributions in the 3-dimensional action space and are found to be correlated with different observable rodent behaviors.
  
  - This usage of this algorithm has been outlined below, and is extremely flexible in adapting to what the user wants. With the ever-blooming advances in ways to study an animal behavior, our algorithm builds on and integrates what has already been robustly tested to help advance scientific research.

## New Features!

  - By implementing UMAP with HDBSCAN, B-SOiD in Python can now handle high-dimension clustering with an essentially infinite number of features (we’ve tried up to 784 features = 28 body parts).
  
  - Moreover, this update renders the code truly agnostic - not just to the groups extracted, but to the input data itself. Although B-SOiD has always been capable of taking in any set of spatiotemporal data, it is now optimized to handle any set of estimated positions, from any camera angle, and of any model system.
  
  - As always, once trained, B-SOiD can be applied and generalized across datasets, processing hundreds of thousands of frames a minute - and do so with the same temporal resolution as the camera being used.

### Installation

B-SOiD requires [Anaconda/Python3](https://docs.anaconda.com/anaconda/install/) to run.

Create a virtual environment and activate it.

```sh
$ conda create -n bsoid_env
$ conda activate bsoid_env
```

Install non-PyPi dependencies.

```sh
$ conda install ipython  
$ conda install -c conda-forge hdbscan
```

### More information

|  | README |
| ------ | ------ |
| GitHub | [https://github.com/YttriLab/B-SOID](https://github.com/YttriLab/B-SOID) |

### Todos

 - Improve frame extraction using ffmpeg.
 - Add Google COLAB
 - Add Docker

License
----

GNU GPL-3.0


