# Data-intensive-systems

This project analyzes network logs using Apache Spark, Hadoop, and Python. The analysis is split into two main parts, both utilizing MinHash and LSH techniques to find similarities and dissimilarities in network logs.

## Overview

In this system, a server receives a service request either from a user or another server and responds with a service response. The duration of a service task is the time elapsed between receiving the request and sending the response. Importantly, we disregard network delays for simplicity in modeling.

### Example Scenario

Consider a scenario where Server S1 receives a request to purchase a book (X) from a user at time t0. Server S1, realizing the need for a credit check, sends a request to Server S2 at time t1. Meanwhile, at time t3, Server S1 receives another request to buy another book (Y). It further requests an ID check from Server S3 at time t4. Subsequently, Server S1 receives a response from Server S2 at time t5 and responds to the initial book purchase request at time t6. Finally, Server S1 receives a response from Server S3 at time t7.

### Log File Analysis

The system logs each request and response exchange between servers in the following format:

```<FromServer, ToServer, time, action (Request or Response), processId >```

### Goals

1. **Identify Variations**: The first goal is to identify variations in processes recorded in the log file. A unified representation should represent Processes exhibiting similar characteristics to simplify analysis.
2. **Group Similar Processes**: The second goal involves grouping processes that share some similarities but are distinct enough to warrant separate representations.


## Prerequisites

Ensure you have the following software installed with the specified versions:

- **Apache Spark** (version 3.5.1): [Download Apache Spark](https://spark.apache.org/downloads.html)
- **Hadoop** (version 3.4.0): [Download Hadoop](https://hadoop.apache.org/releases.html)
- **Python** (version 3.12.4): [Download Python](https://www.python.org/downloads/)
- **Java** (version 22.0.1): [Download Java](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/project-name.git
   cd project-name
   
2. **Set up Hadoop:**
- Download Hadoop into `C:/hadoop`, and in the `bin` folder you need to download `winutils` corresponding to your Hadoop version. In our case, you can download it from this link: [winutils for Hadoop 3.4.0 on Windows 10 (x64)](https://github.com/kontext-tech/winutils/tree/master/hadoop-3.4.0-win10-x64/bin).
- Add to the `Environment Variables` the variable name `HADOOP_HOME` with the path `C:/hadoop`.

3. **Set up Spark**
- Download Spark into `C:/spark`
- Add to the `Environment Variables` the variable name `SPARK_HOME` with the path `C:/spark/YOUR-SPARK-FOLDER`.
- Add to the `Environment Variables` the variable name `PYSPARK_HOME` with the path of your Python installation.
- Add to the `Environment Variables` the variable name `JAVA_HOME` with the path of your JAVA JDK from the JAVA installation.

4. **Run the Spark standalone application:**
-  Use the provided batch script to create the Master and Workers:
  ```sh
  ./start_spark_cluster.bat
  ```
- You can edit this file to adjust the number of workers, the amount of RAM and the number of cores per worker, and the allocated RAM and cores for the master.


## Running the Analysis:
1. **Open Jupyter Notebook:**
-  Open Jupyter notebook as an administrator:
  ```sh
  jupyter notebook
  ```
- Navigate to the `Src` folder where the notebooks are located.

2. **Log Generator:**
- Open `log_generator.ipynb`.
- Define your network and generate logs with the desired amount and depth.

3. **Part 1 Analysis:**
- Open `Part1.ipynb`.
- This notebook uses shingles and MinHash LSH to identify similar pairs.
- The current output files are generated in `output/part1Observations.txt` and `output/part1Output.txt`.

4. **Part 2 Analysis:**
- Open `Part2.ipynb`.
- This notebook uses server names instead of shingles and identifies less similar pairs using MinHash LSH.
- The current output file is generated in `output/part2Observations.txt`.

## Documentation
- **Report:**
  - The detailed project report can be found in `Report/PSZ.pdf`.
- **Presentation:**
  - The project presentation slides are in `Presentation/PSZ.pptx`.

## Data
- All test data used in this project can be found in the `Data` folder.

## Project Structure
```scss
Data-intensive-systems/
├── Data/
│   └── ... (test data files)
├── Output/
│   ├── part1Observations.txt
│   ├── part1Output.txt
│   └── part2Observations.txt
├── Report/
│   └── PSZ.pdf
├── Presentation/
│   └── PSZ.pptx
├── Src/
│   ├── log_generator.ipynb
│   ├── Part1.ipynb
│   └── Part2.ipynb
├── start_spark_cluster.bat
└── README.md
```


