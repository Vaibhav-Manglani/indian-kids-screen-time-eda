# eda_screen_time.py

"""
Exploratory Data Analysis on Indian Kids' Screen Time Dataset

This script reads a CSV dataset, processes multi-label fields, and visualizes the relationship 
between screen time, age, device usage, and health impacts among Indian children.

Dataset Source: https://www.kaggle.com/datasets/ankushpanday2/indian-kids-screentime-2025/data

Author: Vaibhav Manglani
Date: 29/07/2025
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Setup
sns.set(style="whitegrid")
OUTPUT_DIR = "../outputs/plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the dataset
data = pd.read_csv('../data/Indian_Kids_Screen_Time.csv')

# Basic exploration
print("First 5 rows:")
print(data.head())

print("\nShape:", data.shape)
print("\nStatistics:")
print(data.describe())

# Preprocessing multi-label 'Health_Impacts' column
data['Health_Impacts'] = data['Health_Impacts'].str.split(',')
data = data.explode('Health_Impacts').reset_index(drop=True)

print("\nShape after exploding Health_Impacts:", data.shape)

# =====================
# Visualizations
# =====================

sns.displot(data=data, x="Age", col="Primary_Device", kde=True)
plt.savefig(f"{OUTPUT_DIR}/age_by_primary_device.png")

sns.displot(data=data, x="Age", col="Exceeded_Recommended_Limit", kde=True)
plt.savefig(f"{OUTPUT_DIR}/age_by_exceed_limit.png")

sns.displot(data=data, x="Primary_Device", col="Urban_or_Rural", kde=True)
plt.savefig(f"{OUTPUT_DIR}/primary_device_by_urban_rural.png")

sns.displot(data=data, x="Age", col="Urban_or_Rural", kde=True)
plt.savefig(f"{OUTPUT_DIR}/age_by_urban_rural.png")

sns.displot(data=data, x="Educational_to_Recreational_Ratio",
            col="Primary_Device", kde=True)
plt.savefig(f"{OUTPUT_DIR}/edurec_ratio_by_device.png")

sns.displot(data=data, x="Age", col="Health_Impacts", kde=True)
plt.savefig(f"{OUTPUT_DIR}/age_by_health_impact.png")

# Swarm plot
sns.catplot(data=data, kind="swarm", x="Age",
            y="Avg_Daily_Screen_Time_hr", hue="Exceeded_Recommended_Limit")
plt.savefig(f"{OUTPUT_DIR}/screen_time_by_age_swarm.png")

# Joint plots
sns.jointplot(data=data, x="Educational_to_Recreational_Ratio",
              y="Age", hue="Primary_Device")
plt.savefig(f"{OUTPUT_DIR}/joint_edurec_vs_age.png")

sns.jointplot(data=data, x="Avg_Daily_Screen_Time_hr",
              y="Age", hue="Health_Impacts")
plt.savefig(f"{OUTPUT_DIR}/joint_screen_time_vs_age.png")

# Pair plot
sns.pairplot(data=data, hue="Urban_or_Rural")
plt.savefig(f"{OUTPUT_DIR}/pairplot_urban_rural.png")

print("Plots saved in:", OUTPUT_DIR)
