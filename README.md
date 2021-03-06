# B-SOiD

![Version](https://img.shields.io/github/v/release/runninghsus/Bsoid) ![Code size](https://img.shields.io/github/languages/code-size/runninghsus/Bsoid) ![License](https://img.shields.io/github/license/runninghsus/Bsoid) ![Open issues](https://img.shields.io/github/issues/YttriLab/B-SOID) ![Stars](https://img.shields.io/github/stars/YttriLab/B-SOID?style=social)

## Why B-SOiD?

  - DeepLabCut has revolutionized the way behavioral scientists analyze data. The algorithm utilizes recent advances in computer vision and deep learning to estimate poses. Interpreting the positions of an animal can be useful in studying behavior; however, it does not encompass the whole dynamic range of naturalistic behaviors.
  
  - Behavioral segmentation of open field in DeepLabCut, or B-SOID ("B-side"), is an unsupervised learning algorithm that serves to discover behaviors that are not pre-defined by users. Our algorithm can segregate statistically different sub-second rodent behaviors with a single video-camera. Upon estimating the positions, this algorithm agnostically separates statistically significant distributions and are found to be correlated with different observable rodent behaviors.
  
  - This usage of this algorithm has been outlined below, and is extremely flexible in adapting to what the user wants. With the ever-blooming advances in ways to study an animal behavior, our algorithm builds on and integrates what has already been robustly tested to help advance scientific research.

## New Features!

  - By implementing UMAP with HDBSCAN, B-SOiD can now handle high-dimension clustering (we’ve tried up to 784 features = 28 body parts).
  
  - Moreover, this update renders the code truly agnostic - not just to the groups extracted, but to the input data itself. It can handle any set of estimated positions, from any camera angle, and of any model system.
  
  - As always, once a machine learning classifier is trained, B-SOiD can be applied and generalized across datasets, processing hundreds of thousands of frames a minute - and do so with the same temporal resolution as the camera being used.

### Installation

B-SOiD requires [Anaconda/Python3](https://docs.anaconda.com/anaconda/install/) to run.

Create a virtual environment and activate it.

```sh
$ conda create -n bsoid_env
$ conda activate bsoid_env
```

Install non-PyPi dependencies.

```sh
$ conda install -c conda-forge hdbscan
$ conda install -c anaconda psutil
$ conda install -c conda-forge ffmpeg
```

Install B-SOiD.
```
$ pip install Bsoid==0.1.4
```


### More information

|  | README |
| ------ | ------ |
| GitHub | [https://github.com/YttriLab/B-SOID](https://github.com/YttriLab/B-SOID) |

### Todos

 - Update docker and add badge/link

License
----

GNU GPL-3.0


