# Tutorial - SciPy 2022

## Practical Numerical Optimization with SciPy, Estimagic and JAXopt

> by Janos Gabler & Tim Mensinger

## Contents

1. [Installation](#installation)
1. [Slides](#slides)
1. [Exercises](#exercises)
1. [Troubleshooting](#troubleshooting)

> **Warning** Please pull the repo and update your conda environment before the tutorial
> to make sure that the most recent versions are installed.

## Installation

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

1. Clone the repository

   ```console
   $ git clone https://github.com/OpenSourceEconomics/scipy-pres.git
   $ cd scipy-estimagic
   ```

1. Install and activate the environment

   ```console
   $ conda env create -f environment.yml
   $ conda activate scipy-estimagic
   ```

   > **Note** You have to repeat the activation step each time after closing your
   > terminal.

1. Test your installation

   ```console
   $ python test_installation.py
   ```

1. Update the environment

   > **Note** This step is only necessary if you have installed the environment a long
   > time ago and want to make sure that you're using the most recent versions.

   ```consolse
   $ cd scipy-estimagic
   $ conda activate scipy-estimagic
   $ conda env update -f environment.yml
   ```

   or use a completely fresh install:

   ```console
   $ cd scipy-estimagic
   $ conda deactivate scipy-estimagic
   $ conda env remove --name scipy-estimagic
   $ conda env create -f environment.yml
   ```

## Slides

You can download the slides by clicking
[here](https://github.com/OpenSourceEconomics/scipy-estimagic/raw/main/slides.pdf), or
you can view them directly on GitHub
[here](https://github.com/OpenSourceEconomics/scipy-estimagic/blob/main/slides.pdf).

## Exercises

You find the exercise notebooks in the folder
[exercises](https://github.com/OpenSourceEconomics/scipy-estimagic/tree/main/exercises),
and the corresponding solutions in the subfolder
[exercises/solutions](https://github.com/OpenSourceEconomics/scipy-estimagic/tree/main/exercises/solutions).

## Troubleshooting

If you have questions, problems with the installation or any other part of the
repository, please
[open an issue](https://github.com/OpenSourceEconomics/scipy-estimagic/issues).
