# Machine Learning Lab 3: Density Peak Clustering
Modified by Yuanhao Pu 2023.11.26

## Update:
- 如使用该算法得到的聚类结果达不到理想的程度，可尝试在计算局部密度时使用核函数提升聚类算法的性能。

## 1. Theory of Clustering
Please refer to the contents of Chpt. 9 "Clustering". 

This experiment primarily implements the algorithm from the paper *"Clustering by fast search and find of density peaks"* 

(hereinafter referred to as **DPC**), by Alex Rodriguez and Alessandro Laio, published in *SCIENCE* in 2014.
[source](https://sites.psu.edu/mcnl/files/2017/03/9-2dhti48.pdf)

Each student is recommended to carefully read the entire article before the experiment.

### 1.1 Algorithm Overview
**DPC** integrates the ideas of **k-means** and **DBSCAN**:

- The density is lower at the edges of each cluster, but higher at the center.

- Points in cluster centers are usually far from other points with higher density.

### 1.2 Algorithm Flow

- Set **Hyperparameter**: a distance threshold $d_c$

- For each data point $i$, compute two quantities:

  - Local density: $\rho_i=\sum_j\chi(d_{ij}−d_c)$, where $\chi(x)=1$ if $x<0$ and $\chi(x)=0$ otherwise.

  - Distance from points of higher density: $\delta_i=\underset{j:\rho_j>\rho_i}{\min}d_{ij}$. For the point with the highest density, take $\delta_i=\max_jd_{ij}$.
 
  - Also, you can try other types of Kernel Functions

- Identify the cluster centers and out-of-distribution (OOD) points:

  - Cluster centers: points with both high $\rho_i$ and $\delta_i$.

  - OOD points: points with high $\delta_i$ but low $\rho_i$.

  - Draw a decision graph and make manual decisions.

## 2 Experimental Data

This experiment uses three 2-dimensional datasets for ease of visualization: 
- Datasets/D31.txt
- Datasets/R15.txt
- Datasets/Aggregation.txt

### Data Format
- Each file is a plain text file containing one dataset.

- Each line in the file represents a data example, separated by spaces.

- Notice that setting different hyperparameters to different datasets is acceptable.

## 3 Tasks and Requirements
### 3.1 Tasks
#### 3.1.1 Experimental Introduction

The overall process of this experiment is to complete the code implementation of the DPC algorithm and conduct visualization experiments on the given dataset. Specifically, students need to perform the following steps:
- Load the dataset and preprocess the data (if necessary).

- Implement the DPC algorithm, calculate $\delta_i$ and $\rho_i$ for data points.

- Draw a **decision graph**, select sample centers and outliers.

- Determine clustering results, calculate **evaluation metrics**, and draw **visualization graphs**.

We teaching assistants will evaluate your submitted content based on the following aspects besides the overall code flow:
- Visualized decision graph.
- Visualized clustering results.
- Calculated evaluation metric value (DBI).
- Notice that there is no strict restriction on your experimental results, outputs within a reasonable range are acceptable.

#### 3.1.2 Evaluation Metrics
We require using the **Davis-Bouldin Index** (DBI) as the evaluation metric.

All you need to do is call the `sklearn.metrics.davies_bouldin_score` for calculation.

#### 3.1.3 Data Visualization

We require two 2D scatter plots for visualization: a decision graph and a clustering result graph.

We recommend `pyplot` as your visualization library (or you can choose other reasonable tools).

Example：

```{python}
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(1, 10)
x2 = x1**2
fig = plt.figure()
ax1 = fig.add_subplot(111)
# Setting colors for all points
colors = ['r', 'y', 'g', 'b', 'r', 'y', 'g', 'b', 'r']
# Setting graph title
ax1.set_title('Scatter Plot')
# Setting label for x-axis
plt.xlabel('X')
# Setting label for y-axis
plt.ylabel('Y')
# Plot the scatter graph
ax1.scatter(x1, x2, c=colors, marker='o')
# Show the graph
plt.show()
# Note that plt.show() only displays the image in an interactive environment, use plt.savefig(...) as an alternative
```

### 3.2 Requirements

- `sklearn` and other machine learning libraries are forbidden in your manuscript(except for the calling of `sklearn.metrics.davies_bouldin_score`), you are only permitted with `numpy`, `pandas`, `matplotlib`, and Standard Library, you are required to write this project from scratch. However, if you cannot complete it from scratch, you can still use ML libraries for comprehension with a portion of the point penalty. Please give **explicit statement** in your report to avoid extra deduction of your points.

- You are allowed to discuss with other students, but you are not allowed to plagiarize the code, we will use an automatic system to determine the similarity of your programs, and once detected, both of you will get zero marks for this project.

## 4. Submission

Given that we have provided all the guidance to complete this experiment in the Task section, we will not provide the `.ipynb` framework again. Therefore, you should implement the experiment yourself and write it in **one** `main.ipynb` file. Your code should not be placed in more than one file.

Your report should include but not be limited to the following contents:

- Experiment purpose. (Optional)
- Brief explanation of the experimental principle. (Optional)
- Experimental steps. This part may include data-loading, model training, tuning parameters, obtaining how many sets of results, summarizing the contents in each code block, etc.
- Experimental results. Summarize, compare, and visualize your output.
- Experimental analysis. Analyze the reasons for your results. (Optional)

Submit a .zip file containing the following:
- main.ipynb
- Report.pdf

Note that you do not need to submit **any files**(which would potentially be original data or visualization images) other than the experiment code and report. You should add all visualization results to the report.

Please name your file as `LAB3_PBXXXXXXXX_中文名.zip`, for wrongly named files, we will not count the mark.

Sent an email to ml2023fall@163.com with your `.zip` file before the deadline

**Deadline**: 2023.12.10 23:59:59
