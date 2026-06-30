# Predicting Healthcare Access Barriers and Identifying Population Health Profiles Using BRFSS Data

SIADS Milestone II Project

University of Michigan Master of Applied Data Science
Team 17: Rechelle Transeth, Braeden Mahnke, Indrayan Banerjee

## Project Overview
This project uses the 2024 CDC BRFSS dataset to predict healthcare access barriers and identify population health profiles.

## Research Goal
The main supervised learning goal is to predict whether a respondent was unable to see a doctor due to cost in the past 12 months using BRFSS survey variables.

The unsupervised learning goal is to identify meaningful population-level healthcare access profiles using clustering and dimensionality reduction.

## Dataset
CDC BRFSS 2024 Annual Survey Data.

Raw data files are not stored in this repository. Users should download the BRFSS .XPT file from the CDC website and place it in `data/raw/`.

## Project Structure
- `data/raw/`: raw data files, not tracked by Git
- `data/processed/`: cleaned data files, not tracked by Git
- `notebooks/`: Jupyter notebooks for data loading, preprocessing, supervised learning, and unsupervised learning
- `src/`: reusable scripts
- `outputs/`: figures and model outputs
- `docs/`: proposal, notes, and documentation
