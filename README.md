# Understanding the in-situ Solar Wind Properties with Machine Learning and Artificial Intelligence

## Overview
The corona, the Sun's outer atmosphere, releases a stream of hot, high-pressure charged particles and magnetic fields that escape the Sun’s gravitational pull and extend throughout our solar system. This phenomenon, termed as solar wind, contributes to the plasma that fills the solar system and significantly impacts the space weather conditions surrounding Earth and other planets. As the solar wind travels through space, it carries with it the Sun's magnetic field, extending the solar magnetic field throughout the solar system. This interaction with Earth's magnetic field can cause geomagnetic storms, which can disrupt satellite operations, communication systems, and power grids on Earth. Our study aims to apply machine learning algorithms to explore how the physical characteristics of the solar wind, captured through in-situ measurements by satellite sensors and magnetometers, can be employed to more accurately determine the solar wind's coronal origins and more accurately predict the data for the future Heliophsyics phenomena. The accurate classification of solar wind’s coronal origins has direct implications for space weather forecasting, the protection and design of space missions, the development of early warning systems for space and weather events, and a holistic understanding of our solar system. 

## Table of Contents

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
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

### Installation

## Project Structure

Describe the organization of your project. Explain the purpose of the key directories and files.

`data/`: Folder containing the dataset and any data-related scripts.

`notebooks/`: Jupyter notebooks with the exploratory data analysis and models.

`src/`: Source code for use in this project.

`results/`: Output results, including figures and tables.

## Data Overview

### Data Sources
| Data Source | Description | URL | Type | Date Accessed | Publisher |
|-------------|-------------|-----|------|---------------|-----------|
| Source 1    | Description of Source 1 | http://example1.com | CSV | 2022-01-01 | Publisher 1 |
| Source 2    | Description of Source 2 | http://example2.com | JSON | 2022-01-02 | Publisher 2 |
| Source 3    | Description of Source 3 | http://example3.com | API | 2022-01-03 | Publisher 3 |

### Data Preparation

Data is in [hierarchical data format](https://izw1.caltech.edu/ACE/ASC/hdf.html)
New ACE Level 2 Data Server https://izw1.caltech.edu/ACE/ASC/level2/new/intro.html

ACE Level 2 Policy - https://izw1.caltech.edu/ACE/ASC/level2/policy_lvl2.html
ACE data levels explained - https://izw1.caltech.edu/ACE/ASC/level1/dpl_def.htm

https://izw1.caltech.edu/ACE/ASC/clock.html

## Analysis

### Analytical Questions
1. How can we apply novel dimension reduction methods, such as PCA, TSNE, etc., to obtain informative solar wind in-situ data representation in low-dimensional space? How can this low-dimensional representation provide better 2D/3D visualization support than traditional dimension reduction techniques?
2. How can we apply feature selection methods on the solar wind observed parameters, to objectively rank the importance of these measurements?
3. Employing clustering methods such as DBSCAN, OPTICS, etc., and their variants, can we objectively cluster the low-dimensional representation of the solar wind data, to better understand the potential differences among the categories caused by the different coronal origins?
4. Can we apply ensemble learning or deep learning methods, such as Extra tree, LSTM, transformer etc., to predict the sunspot number and Heliospheric current sheet (HCS) indexes and to provide implications for the solar wind global structure in the future?


### Methods and Tools


## Results
## Contributing
## Acknowledgments
- Sarah Amiraslani
- Andria Lesane
- Nikola Acin



