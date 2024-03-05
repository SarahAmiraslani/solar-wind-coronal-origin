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
| Data Source | Description | URL | Type | Date Accessed | Publisher | Shape |
|-------------|-------------|-----|------|---------------|-----------|-------|
| Heliospheric Current Sheet (HCS) Indexes  | Description of Source 1 | N/A | CSV | 2024-03-01 | University of Michigan, collected by Liang Zhao, PhD| ADD |
|Advanced Composition Explorer (ACE) Spacecraft Data | ADD|ADD|ADD|ADD|NASA|ADD|



<details>
<summary>HCS Indexes</summary>

There are 13 columns. The fields that are most relevant to this project are `fyear_CS` (gives the time as a fractional year), `SD_70` (the SD index), and `SL_70` (the SL index, we use log_10 on this index to make it more compatible with SD as was recomended by Dr. Liang. 

</details>


<details>
<summary>Advanced Composition Explorer (ACE) Spacecraft Data </summary>
<br></br>

**Measurement type**: In-situ located at the Sun-Earth L1 Lagrange point, about 870,000 miles (1.4 million kilometers) from Earth (NASA, n.d.)

**Summary**: Launched in 1997, NASA's Advanced Composition Explorer (ACE) mission is dedicated to capturing and analyzing particles from solar, interplanetary, interstellar, and galactic sources. Its primary aim is to explore the connections between the Sun, Earth, and the Milky Way by examining materials expelled by the Sun. In-situ data collection began in 1998, providing near-real-time insights into solar wind characteristics through hourly averages collected by ACE's suite of nine instruments. Our focus will be on four of these instruments: the Magnetometer (MAG), the Solar Wind Electron, Proton, and Alpha Monitor (SWEPAM), the Electron, Proton, and Alpha Monitor (EPAM), and the Solar Wind Ion Composition Spectrometer (SWICS). These instruments have been identified through our literature review as crucial for determining the coronal origins of the solar wind.
Data Cleaning Requirements: routine maintenance operations, instrument saturation and degradation lead to gaps or errors in the in-situ measurements. The SWICS data contains a flag to identify “good” vs “bad” quality entries, but we may have to perform careful preprocessing to identify bad quality metrics in other measurements that do not have this quality flag. 

</details>


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



