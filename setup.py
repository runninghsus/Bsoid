# from distutils.core import setup
from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='bsoid',         # How you named your package folder (MyLib)
  packages=['bsoid'],   # Chose the same as "name"
  version='0.1.3.3',      # Start with a small number and increase it with every change you make
  license='GPL-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description='An open-source machine learning algorithm for parsing spatio-temporal patterns.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Alex Hsu',                   # Type in your name
  author_email='ahsu2@andrew.cmu.edu',      # Type in your E-Mail
  url='https://github.com/YttriLab/B-SOID',   # Provide either the link to your github or to your website
  download_url='https://github.com/runninghsus/Bsoid/archive/v0.1.3.3.tar.gz',    # I explain this later on
  keywords=['Unsupervised learning', 'UMAP', 'HDBSCAN', 'Behavioral extraction'],   # Keywords that define your package best
  # install_requires=[            # I get to this in a second
  #         'ffmpeg-python>=0.18.2',
  #         'matplotlib>=3.1.3',
  #         'networkx>=2.4',
  #         'opencv-python-headless>=4.2.0.34',
  #         'pandas>=1.0.1',
  #         'scikit-learn>=0.22.2.post1',
  #         'seaborn>=0.10.0',
  #         'streamlit>=0.60.0',
  #         'tqdm>=4.42.1',
  #         'umap-learn>=0.4.2',
  #     ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)
