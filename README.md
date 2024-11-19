A/B Testing Automation in Python
This project features a Python class, ABTesting, designed to automate the A/B testing process, enabling users to analyze experimental data efficiently and make informed business decisions. By performing statistical hypothesis testing, it helps determine whether the differences observed between two groups—control and test—are statistically significant.

Project Overview
A/B testing is a crucial method used in data-driven industries to compare two versions of a variable and analyze which one performs better. This automation tool in Python simplifies the workflow, from data setup to result interpretation, providing key metrics and hypothesis test outcomes in a streamlined manner.

Key Features
Data Initialization: Handles the setup of control and test groups from a pandas DataFrame.
Conversion Rate Calculation: Computes the average conversion rate for both groups.
Hypothesis Testing: Uses an independent t-test to compare conversion rates and outputs statistical significance.
Comprehensive Summary: Outputs conversion rates, t-statistic, and p-value, along with a clear conclusion about the statistical significance.
Class Structure
ABTesting Class
The class is initialized with:

data: A pandas DataFrame containing experimental data.
group_column: The column name that identifies the groups (e.g., 'variant').
outcome_column: The column name for the outcome or metric being measured (e.g., 'conversion').
control_group and test_group: The values in group_column that specify the control and test groups.
Methods
get_conversion_rate: Calculates and returns the mean conversion rates for both control and test groups.
perform_ttest: Conducts an independent t-test and returns the t-statistic and p-value.
summarize: Prints a summary of the results, including conversion rates, t-test statistics, and a decision on statistical significance.
Example Usage
Here's a quick demonstration of how to use the ABTesting class:


import pandas as pd
import numpy as np
from ab_testing import ABTesting

# Simulated Data for A/B Testing
np.random.seed(42)
data = pd.DataFrame({
    'variant': ['A'] * 1000 + ['B'] * 1000,
    'conversion': np.concatenate([np.random.binomial(1, 0.10, 1000), np.random.binomial(1, 0.12, 1000)])
})

# Initialize the ABTesting class with the DataFrame
ab_test = ABTesting(data, group_column='variant', outcome_column='conversion', control_group='A', test_group='B')

# Summarize the results
ab_test.summarize()
Output Example

Control Group Conversion Rate: 0.1000
Test Group Conversion Rate: 0.1200
T-Statistic: -1.6780
P-Value: 0.0934
Result: Not statistically significant. We fail to reject the null hypothesis.
How It Works
Data Simulation: The example generates binary outcome data using a binomial distribution for two groups.
Group Comparison: Calculates the average conversion rates and performs a t-test.
Statistical Analysis: Provides an interpretation of the p-value to determine if the test group shows a statistically significant difference from the control group.
Requirements
To run the project, you will need the following Python packages:


pip install pandas scipy numpy
Potential Enhancements
Multiple Hypothesis Testing: Extend functionality to support testing multiple variants simultaneously.
Bayesian A/B Testing: Implement Bayesian analysis as an alternative to the frequentist approach.
Confidence Intervals: Add methods to calculate and display confidence intervals for conversion rates.
Data Visualization: Integrate visualization libraries like matplotlib or seaborn to generate insightful plots.
Author
Idriss Olivier BADO
License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.

