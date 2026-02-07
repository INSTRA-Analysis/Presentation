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
def plot_SDOF_free_vibration():
    """
    Create a schematic diagram of a Single Degree of Freedom (SDOF) system.
    Components: fixed wall, spring, damper, and mass
    
    Returns:
    --------
    matplotlib.figure.Figure
        Figure object with the SDOF schematic
    """
    fig, ax = plt.subplots()
    
    
    
    # Draw the spring from x=1 to x=2 at y=0.5
    spring_x = np.linspace(1, 2, 100)
    spring_amplitude = 0.1
    spring_y = 0.3 + spring_amplitude * np.sin(10 * np.pi * (spring_x - 1) / (2 - 1))
    ax.plot(spring_x, spring_y, color='orange', linewidth=1, label='Spring (K)')
    
    # Draw the damper box at x=2, y=0 (centered)
    damper_w = 0.3
    damper_h = 0.15
    damper_x = 1.5
    damper_y = -0.25
    damper = Rectangle((damper_x - damper_w/2, damper_y - damper_h/2), damper_w, damper_h, 
                       edgecolor='blue', facecolor='lightblue', linewidth=1, alpha=0.8)
    # Left connector: from end of spring to left side of damper
    ax.plot([1, 1.35], [-0.25, -0.25], color='blue', linewidth=1) #([x_start, x_end], [y_connector, y_connector]
    ax.plot([1.65, 2], [-0.25, -0.25], color='blue', linewidth=1) #([x_start, x_end], [y_connector, y_connector]

    ax.add_patch(damper)
    #ax.text(damper_x, damper_y, 'C', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Draw the mass rectangle at x=4, y=0 (centered)
    mass_w = 2
    mass_h = 1.2
    mass_x = 3.0
    mass_y = 0.0
    mass = Rectangle((mass_x - mass_w/2, mass_y - mass_h/2), mass_w, mass_h, 
                     edgecolor='darkblue', facecolor='lightblue', linewidth=2, alpha=0.9)
    ax.add_patch(mass)
    ax.text(mass_x, mass_y, 'Mass ($M$)', fontsize=14, ha='center', va='center', fontweight='bold')
    
    # Add labels
    ax.text(1.5, 0.45, r'spring with' + '\n' + 'Stiffness ($k$)', fontsize=11, ha='center', color='black', fontweight='bold')
    ax.text(1.5, -0.1, r'Damper with' '\n' 'Damping Coefficient ($c$)', fontsize=11, ha='center', color='black', fontweight='bold')
    
    # Displacement arrow at top of mass (double-headed)
    arrow_u_start = (4, 0.8)
    arrow_u_end = (4.5, 0.8)
    arrow_u = FancyArrowPatch(arrow_u_start, arrow_u_end, 
                            arrowstyle='<->', 
                         mutation_scale=15, 
                         linewidth=2, 
                         color='black')
    ax.add_patch(arrow_u)
    ax.text(4.25, 0.85, r'$u$', fontsize=12, ha='center', va='bottom')

    arrow_x_start = 4  # Right side of mass
    arrow_x_end = 4.8    # Further right
    arrow_y = 0        # Center height

    arrow = FancyArrowPatch((arrow_x_start, arrow_y), (arrow_x_end, arrow_y),
                       arrowstyle='->', mutation_scale=20,
                       linewidth=2.5, color='green')
    ax.add_patch(arrow)
    ax.text (4.9, 0, r'F(t)', fontsize=12, ha='center', color='black', fontweight='bold')
    
    # Draw the fixed wall at x=1
    ax.axvline(1, color='b', linewidth=4)
    #ax.axhline(-mass_h/2 -0.065, color='b', linewidth=6)
    #ax.text(0.7, 0, 'Wall', fontsize=12, ha='right', va='center', fontweight='bold')

    ax.set_aspect('equal')
    ax.axis('off')
    
    
    ax.set_title('SDOF System Free vibration', fontsize=14, fontweight='bold', pad=20)
    
    return fig, ax
# %%
from matplotlib.patches import Rectangle, FancyArrowPatch

plot_SDOF_free_vibration()
plt.show()

# %%
