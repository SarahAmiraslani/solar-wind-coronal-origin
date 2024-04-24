# Understanding the in-situ Solar Wind Properties with Machine Learning

## Overview

The corona, the Sun's outer atmosphere, releases a stream of hot, high-pressure charged particles and magnetic fields that escape the Sun’s gravitational pull and extend throughout our solar system. This phenomenon, termed as solar wind, contributes to the plasma that fills the solar system and significantly impacts the space weather conditions surrounding Earth and other planets. As the solar wind travels through space, it carries with it the Sun's magnetic field, extending the solar magnetic field throughout the solar system. This interaction with Earth's magnetic field can cause geomagnetic storms, which can disrupt satellite operations, communication systems, and power grids on Earth. Our study aims to apply machine learning algorithms to explore how the physical characteristics of the solar wind, captured through in-situ measurements by satellite sensors and magnetometers, can be employed to more accurately determine the solar wind's coronal origins and more accurately predict the data for the future Heliophsyics phenomena. The accurate classification of solar wind’s coronal origins has direct implications for space weather forecasting, the protection and design of space missions, the development of early warning systems for space and weather events, and a holistic understanding of our solar system.

## Table of Contents

- [Understanding the in-situ Solar Wind Properties with Machine Learning and Artificial Intelligence](#understanding-the-in-situ-solar-wind-properties-with-machine-learning-and-artificial-intelligence)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Data Overview](#data-overview)
    - [Data Sources](#data-sources)
    - [Data Preparation](#data-preparation)
  - [Analysis](#analysis)
    - [Analytical Questions](#analytical-questions)
    - [Methods and Tools](#methods-and-tools)
      - [In-Situ data dimensionality reduction](#in-situ-data-dimensionality-reduction)
      - [Classifying coronal origin of solar wind](#classifying-coronal-origin-of-solar-wind)
    - [Clustering](#clustering)
  - [Results](#results)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

Ensure that you have the Python package dependencies installed before running this code. The required packages are listed in the `requirements.txt ` file of this

### Project Structure

`data/`: Folder contains open source data sets.

`notebooks/`: Jupyter notebooks with the exploratory data analysis and models.

`src/`: utility scripts used in this project.

## Data Access

### Advanced Composition Explorer (ACE) Spacecraft Data
launched in 1997, NASA's Advanced Composition Explorer (ACE) mission captures and analyzes particles from solar, interplanetary, interstellar, and galactic sources. Its primary aim is to explore the connections between the Sun, Earth, and the Milky Way by examining materials expelled by the Sun. ACE data comprise in-situ measurements collected at the Sun-Earth L1 Lagrange point, about 870,000 miles (1.4 million kilometers) from Earth (NASA, n.d.)—where the gravitational pull between the Earth and the Sun is at equilibrium. 

### Sunspot Index and Long-term Solar Observations
Monthly mean total sunspot number: This dataset contains monthly mean total sunspot numbers, which are averages derived from daily total counts per calendar month, starting from January 1749 up to the last elapsed month. This extensive time range is due to data availability only from 1749 onward because of sparse earlier observations. The dataset is available in plain ASCII text and CSV formats, detailing columns for the year, month, date in fraction of year, monthly mean sunspot number, monthly standard deviation, and number of observations used. Notably, an error value of -1 indicates missing observations, with the monthly standard deviation calculated from daily values. These monthly mean values provide critical insights into long-term solar activity patterns essential for various scientific and operational purposes.

### Heliospheric Current Sheet (HCS) Indexes, 
Curated by Dr. Liang Zhao from the University of Michigan, this dataset encompasses heliospheric current attributes recorded bi-monthly from 1976 to 2022. The key features of this dataset include the SD index and the SL index. The SD index describes the standard deviation of the HCS's latitude, while the SL index describes the HCS's integrated slope. These novel, derived parameters simplify current methods of evaluating HCS activity and tracking the solar cycle. In compliance with non-disclosure agreements, sharing this dataset with the public is restricted.

## Analytical Questions

1. How can we apply novel dimension reduction methods, such as PCA, TSNE, etc., to obtain informative solar wind in-situ data representation in low-dimensional space? How can this low-dimensional representation provide better 2D/3D visualization support than traditional dimension reduction techniques?
2. How can we apply feature selection methods on the solar wind observed parameters, to objectively rank the importance of these measurements?
3. Employing clustering methods such as DBSCAN, OPTICS, etc., and their variants, can we objectively cluster the low-dimensional representation of the solar wind data, to better understand the potential differences among the categories caused by the different coronal origins?

## Acknowledgments

We extend our gratitude to the ACE Science Center (ASC) for its maintenance of well-documented public records of data from the ACE spacecraft. We also wish to acknowledge the contributions of the NASA National Space Science Data Center, the Space Physics Data Facility, and Edward C. Stone of the California Institute of Technology, the Principal Investigator for the ACE project, for their support in the usage of ACE data. Additionally, we would like to
