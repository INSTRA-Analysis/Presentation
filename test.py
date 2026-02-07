#%%[markdown]
# # ***Dynamic of structures - SDoF***
# %%
# Depandancies:
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math
import scipy as sp
# %% DEFINE PLOTTING PARAMETERS
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.5
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['legend.loc'] = 'best'
plt.rcParams['figure.dpi'] = 200
plt.rcParams['grid.linewidth'] = 0.8
plt.rcParams['grid.linestyle'] = '--'



# %% [markdown]
# ## Equation of motion and newton second law

# %%
import sys
from pathlib import Path

# Add the project root to path if utils is in a different directory
# sys.path.insert(0, str(Path(__file__).parent))

from utils import utils as ut
# import matplotlib.pyplot as plt

ut.plot_SDOF_forces()
plt.show()

# %%
