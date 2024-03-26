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

### Installation

## Project Structure

Describe the organization of your project. Explain the purpose of the key directories and files.

`data/`: Folder containing the dataset and any data-related scripts.

`notebooks/`: Jupyter notebooks with the exploratory data analysis and models.

`src/`: Source code for use in this project.

`results/`: Output results, including figures and tables.

## Data Overview

### Data Sources

| Data Source                                         | Description             | URL | Type | Date Accessed | Publisher                                            | Shape     |
| --------------------------------------------------- | ----------------------- | --- | ---- | ------------- | ---------------------------------------------------- | --------- |
| Heliospheric Current Sheet (HCS) Indexes            | Description of Source 1 | N/A | CSV  | 2024-03-01    | University of Michigan, collected by Liang Zhao, PhD | (616, 13) |
| Advanced Composition Explorer (ACE) Spacecraft Data | ADD                     | ADD | ADD  | ADD           | NASA                                                 | ADD       |

<details>
<summary>HCS Indexes</summary>

There are 13 columns. The fields that are most relevant to this project are `fyear_CS` (gives the time as a fractional year), `SD_70` (the SD index), and `SL_70` (the SL index, we use log_10 on this index to make it more compatible with SD as was recomended by Dr. Liang.

</details>

<details>
<summary>ACE Spacecraft Data </summary>
<br></br>

__Measurement type__: In-situ located at the Sun-Earth L1 Lagrange point, about 870,000 miles (1.4 million kilometers) from Earth (NASA, n.d.). [Level 2](https://izw1.caltech.edu/ACE/ASC/level2/index.html) data will be used for this analysis as the principal investigators recommend the use of this data for scientific studies. The index of ACE level 2 data can be found [here](https://izw1.caltech.edu/ACE/ASC/DATA/level2/). For more information about the ACE data processing levels review the [documentation](https://izw1.caltech.edu/ACE/ASC/level1/dpl_def.htm).

Summary**: Launched in 1997, NASA's Advanced Composition Explorer (ACE) mission is dedicated to capturing and analyzing particles from solar, interplanetary, interstellar, and galactic sources. Its primary aim is to explore the connections between the Sun, Earth, and the Milky Way by examining materials expelled by the Sun. In-situ data collection began in 1998, providing near-real-time insights into solar wind characteristics through hourly averages collected by ACE's suite of nine instruments. Our focus will be on four of these instruments: the Magnetometer (MAG), the Solar Wind Electron, Proton, and Alpha Monitor (SWEPAM), the Electron, Proton, and Alpha Monitor (EPAM), and the Solar Wind Ion Composition Spectrometer (SWICS). These instruments have been identified through our literature review as crucial for determining the coronal origins of the solar wind.
Data Cleaning Requirements: routine maintenance operations, instrument saturation and degradation lead to gaps or errors in the in-situ measurements. The SWICS data contains a flag to identify “good” vs “bad” quality entries, but we may have to perform careful preprocessing to identify bad quality metrics in other measurements that do not have this quality flag.



</details>

### Data Preparation

Data is in [hierarchical data format](https://izw1.caltech.edu/ACE/ASC/hdf.html)
New ACE Level 2 Data Server https://izw1.caltech.edu/ACE/ASC/level2/new/intro.html

ACE Level 2 Policy - https://izw1.caltech.edu/ACE/ASC/level2/policy_lvl2.html
ACE data levels explained - https://izw1.caltech.edu/ACE/ASC/level1/dpl_def.htm

https://izw1.caltech.edu/ACE/ASC/clock.html

https://izw1.caltech.edu/ACE/ASC/docs/processing.html

## Analysis

### Analytical Questions

1. How can we apply novel dimension reduction methods, such as PCA, TSNE, etc., to obtain informative solar wind in-situ data representation in low-dimensional space? How can this low-dimensional representation provide better 2D/3D visualization support than traditional dimension reduction techniques?
2. How can we apply feature selection methods on the solar wind observed parameters, to objectively rank the importance of these measurements?
3. Employing clustering methods such as DBSCAN, OPTICS, etc., and their variants, can we objectively cluster the low-dimensional representation of the solar wind data, to better understand the potential differences among the categories caused by the different coronal origins?
4. Can we apply ensemble learning or deep learning methods, such as Extra tree, LSTM, transformer etc., to predict the sunspot number and Heliospheric current sheet (HCS) indexes and to provide implications for the solar wind global structure in the future?

### Methods and Tools

#### In-Situ data dimensionality reduction

1. **Principal Component Analysis (PCA)**: PCA is a technique that transforms the data into a new coordinate system such that the greatest variance by any projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.
2. **t-Distributed Stochastic Neighbor Embedding (t-SNE)**: t-SNE is a technique for dimensionality reduction that is particularly well suited for the visualization of high-dimensional datasets. It uses a probabilistic approach to model the similarity between points in high-dimensional and low-dimensional space.
3. **Linear Discriminant Analysis (LDA)**: LDA is a method used in statistics, pattern recognition, and machine learning to find a linear combination of features that characterizes or separates two or more classes of objects or events.
4. **Autoencoders**: Autoencoders are a type of artificial neural network used for learning efficient codings of input data. They are typically used for dimensionality reduction; the network is trained to reconstruct its input data, but the network architecture is designed to have a narrow layer in the middle that serves as a compressed representation of the input data.
5. **Non-negative Matrix Factorization (NMF)**: NMF is a group of algorithms where a matrix V is factorized into (usually) two matrices W and H, with the property that all three matrices have no negative elements. This non-negativity makes the resulting matrices easier to interpret.
6. **Independent Component Analysis (ICA)**: ICA is a computational method for separating a multivariate signal into additive subcomponents. It is a special case of blind source separation.
7. **Uniform Manifold Approximation and Projection (UMAP)**: UMAP is a dimension reduction technique that can be used for visualization similarly to t-SNE, but it also preserves more of the global structure and can be used for general non-linear dimension reduction.

#### Classifying coronal origin of solar wind

Ten machine learning classifiers to be explored:

- _k_-nearest neigbors
- Linear support vector machine
- SVM with Gaussian radial basis function kernel
- Decision tree
- Random forest
- Adaptive Boosting
- Neural network
- Gaussian naive bayes
- Quadratic discriminant analysis
- eXtreme Gradient Boosting

### Clustering

## Results

## Contributing

## Acknowledgments

We would like to acknowledge the ACE Science Center (ASC) for maintaining well documented public records of the data collected by the ACE spacecraft.


Please acknowledge the NASA National Space Science Data Center, the Space Physics
Data Facility, and the ACE Principal Investigator, Edward C. Stone of the
California Institute of Technology, for usage of ACE data. Additionally, we would like to thank the ACE Science Center (ASC) for maintaining well documented public records of the data collected by the ACE spacecraft.

NASA Official: Dr. Robert E. McGuire, Head, SPDF <mailto:Robert.E.McGuire@nasa.gov>
