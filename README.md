# Understanding the In-Situ Solar Wind Properties with Machine Learning

## Overview

The corona, the Sun's outer atmosphere, releases a stream of hot, high-pressure charged particles and magnetic fields that escape the Sun’s gravitational pull and extend throughout our solar system. This phenomenon, termed as solar wind, contributes to the plasma that fills the solar system and significantly impacts the space weather conditions surrounding Earth and other planets. As the solar wind travels through space, it carries the Sun's magnetic field, extending it throughout the solar system. This interaction with Earth's magnetic field can cause geomagnetic storms, disrupting satellite operations, communication systems, and power grids on Earth.

Our study aims to apply machine learning algorithms to explore how the physical characteristics of the solar wind, captured through in-situ measurements by satellite sensors and magnetometers, can be employed to more accurately determine the solar wind's coronal origins and predict future heliophysics phenomena. Accurately classifying the solar wind’s coronal origins has direct implications for space weather forecasting, the protection and design of space missions, the development of early warning systems for space weather events, and a holistic understanding of our solar system.

## Getting Started

### Prerequisites

1. Clone the repository:
```bash
git clone https://github.com/yourusername/formula1-predictions-track-clustering.git
```
2. Ensure you have the necessary Python package dependencies installed before running this code. The required packages are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Project Structure

- `data/`: Contains open source data sets.
- `notebooks/`: Jupyter notebooks with the exploratory data analysis and models.
- `src/`: Utility scripts used in this project.

## Data Access

### Advanced Composition Explorer (ACE) Spacecraft Data

Launched in 1997, NASA's Advanced Composition Explorer (ACE) mission captures and analyzes particles from solar, interplanetary, interstellar, and galactic sources. Its primary aim is to explore the connections between the Sun, Earth, and the Milky Way by examining materials expelled by the Sun. ACE data comprise in-situ measurements collected at the Sun-Earth L1 Lagrange point, about 870,000 miles (1.4 million kilometers) from Earth, where the gravitational pull between the Earth and the Sun is at equilibrium.

### Sunspot Index and Long-term Solar Observations

The dataset contains monthly mean total sunspot numbers, which are averages derived from daily total counts per calendar month, starting from January 1749 up to the present. This extensive time range is due to data availability only from 1749 onward. The dataset is available in plain ASCII text and CSV formats, detailing columns for the year, month, date in fraction of year, monthly mean sunspot number, monthly standard deviation, and number of observations used. An error value of -1 indicates missing observations, with the monthly standard deviation calculated from daily values. These monthly mean values provide critical insights into long-term solar activity patterns essential for various scientific and operational purposes.

### Heliospheric Current Sheet (HCS) Indexes

Curated by Dr. Liang Zhao from the University of Michigan, this dataset encompasses heliospheric current attributes recorded bi-monthly from 1976 to 2022. The key features of this dataset include the SD index, which represents the standard deviation of the HCS's latitude, and the SL index, which measures the HCS's integrated slope. These innovative parameters enhance the evaluation of HCS activity and facilitate tracking the solar cycle. Please note, due to non-disclosure agreements, this dataset is not available for public sharing.

## Analytical Questions

1. How can we apply novel dimension reduction methods, such as PCA, TSNE, etc., to obtain informative solar wind in-situ data representation in low-dimensional space? How can this low-dimensional representation provide better 2D/3D visualization support than traditional dimension reduction techniques?
2. How can we apply feature selection methods on the solar wind observed parameters to objectively rank the importance of these measurements?
3. Can we use clustering methods such as DBSCAN, OPTICS, etc., to objectively cluster the low-dimensional representation of the solar wind data and better understand the potential differences among the categories caused by different coronal origins?
4. Can we accurately forecast the number of sunspots on the Sun?
5. Can we apply ensemble learning and deep learning methods, such as Extra Tree, LSTM, and Transformers, to predict the sunspot number and Heliospheric Current Sheet (HCS) indexes, and provide implications for the future solar wind global structure?

## Acknowledgments

We thank the ACE Science Center (ASC) for maintaining well-documented public data records from the ACE spacecraft. We also wish to acknowledge the contributions of the NASA National Space Science Data Center, the Space Physics Data Facility, and Edward C. Stone of the California Institute of Technology, the Principal Investigator for the ACE project, for their support in using ACE data.
