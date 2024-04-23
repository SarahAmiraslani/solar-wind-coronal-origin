# Understanding the in-situ Solar Wind Properties with Machine Learning and Artificial Intelligence

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

## Data Overview

### Data Sources

| Data Source                                                                               | Description             | Type | Date Accessed | Publisher                                                  | Shape                      |
| ----------------------------------------------------------------------------------------- | ----------------------- | ---- | ------------- | ---------------------------------------------------------- | -------------------------- |
| Heliospheric Current Sheet (HCS) Indexes                                                  | Description of Source 1 | CSV  | 2024-03-01    | University of Michigan, collected by Liang Zhao, PhD       | (616, 13)                  |
| [Advanced Composition Explorer (ACE)](https://science.nasa.gov/mission/ace/) Spacecraft Data | ADD                     | HDF  | 2024-03-01    | ACE Science Center (ASC), maintained by Caltech Univeristy | (132245, 175) |

### Data Access Statement

We have each signed non-disclosure agreements with the principal investigators who have created the HCS Indexes data, preventing us from sharing the data source. However, the ACE dataset is open source and can be pulled from the [ACE Level 2 (Verified) Data](https://izw1.caltech.edu/ACE/ASC/level2/).

## Analytical Questions

1. How can we apply novel dimension reduction methods, such as PCA, TSNE, etc., to obtain informative solar wind in-situ data representation in low-dimensional space? How can this low-dimensional representation provide better 2D/3D visualization support than traditional dimension reduction techniques?
2. How can we apply feature selection methods on the solar wind observed parameters, to objectively rank the importance of these measurements?
3. Employing clustering methods such as DBSCAN, OPTICS, etc., and their variants, can we objectively cluster the low-dimensional representation of the solar wind data, to better understand the potential differences among the categories caused by the different coronal origins?
4. Can we apply ensemble learning or deep learning methods, such as Extra tree, LSTM, transformer etc., to predict the sunspot number and Heliospheric current sheet (HCS) indexes and to provide implications for the solar wind global structure in the future?
5. ojection of the data comes to lie on the first coordinate (called the first principal cClustering

## Acknowledgments

We extend our gratitude to the ACE Science Center (ASC) for its maintenance of well-documented public records of data from the ACE spacecraft. We also wish to acknowledge the contributions of the NASA National Space Science Data Center, the Space Physics Data Facility, and Edward C. Stone of the California Institute of Technology, the Principal Investigator for the ACE project, for their support in the usage of ACE data. Additionally, we would like to
