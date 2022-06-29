# ACQUIRE

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def acquire_military():
    file = "/Users/Ray/codeup-data-science/military-firepower/global_firepower_2022.csv"
    df = pd.read_csv(file)
    return df