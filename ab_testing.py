# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 06:47:55 2024

@author: Idriss Olivier BADO
"""

import pandas as pd
from scipy import stats
import numpy as np

class ABTesting:
    def __init__(self, data, group_column, outcome_column, control_group, test_group):
        """
        Initialize the A/B testing class.

        Parameters:
        data (DataFrame): The pandas DataFrame containing the data.
        group_column (str): The column name which defines the groups (e.g., 'variant').
        outcome_column (str): The column name for the outcome or metric (e.g., 'conversion').
        control_group (str/int): The value in the group column representing the control group.
        test_group (str/int): The value in the group column representing the test group.
        """
        self.data = data
        self.group_column = group_column
        self.outcome_column = outcome_column
        self.control_group = control_group
        self.test_group = test_group

        # Subset data for each group
        self.control_data = self.data[self.data[self.group_column] == self.control_group][self.outcome_column]
        self.test_data = self.data[self.data[self.group_column] == self.test_group][self.outcome_column]

    def get_conversion_rate(self):
        """
        Calculate conversion rates for both control and test groups.
        """
        control_conversion_rate = self.control_data.mean()
        test_conversion_rate = self.test_data.mean()
        
        return control_conversion_rate, test_conversion_rate

    def perform_ttest(self):
        """
        Perform an independent t-test to compare the means (conversion rates) of the control and test groups.
        Returns the t-statistic and p-value.
        """
        t_stat, p_value = stats.ttest_ind(self.control_data, self.test_data)
        return t_stat, p_value

    def summarize(self):
        """
        Print out a summary of the A/B test, including conversion rates and t-test results.
        """
        control_rate, test_rate = self.get_conversion_rate()
        t_stat, p_value = self.perform_ttest()

        print(f"Control Group Conversion Rate: {control_rate:.4f}")
        print(f"Test Group Conversion Rate: {test_rate:.4f}")
        print(f"T-Statistic: {t_stat:.4f}")
        print(f"P-Value: {p_value:.4f}")
        if p_value < 0.05:
            print("Result: Statistically significant! We reject the null hypothesis.")
        else:
            print("Result: Not statistically significant. We fail to reject the null hypothesis.")

# Example Usage:
if __name__ == "__main__":
    # Simulated Data for A/B Testing
    np.random.seed(42)
    
    # Create a DataFrame with two groups: 'A' (control) and 'B' (test)
    data = pd.DataFrame({
        'variant': ['A'] * 1000 + ['B'] * 1000,
        'conversion': np.concatenate([np.random.binomial(1, 0.10, 1000), np.random.binomial(1, 0.12, 1000)])
    })

    # Initialize the ABTesting class with the DataFrame
    ab_test = ABTesting(data, group_column='variant', outcome_column='conversion', control_group='A', test_group='B')

    # Summarize the results
    ab_test.summarize()
