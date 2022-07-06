# ACQUIRE

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def acquire_military():
    url = 'https://github.com/raycerna/military-firepower/blob/main/global_firepower_2022.csv?raw=true'
    df = pd.read_csv(url,index_col=0)

    return df