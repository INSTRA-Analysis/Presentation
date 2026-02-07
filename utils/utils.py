#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from scipy.integrate import solve_ivp
import math
import scipy as sp

#%%
#######################################################
# Plot a signgle degree of freedom system (SDOF) schematic
#######################################################
def plot_SDOF_forces():
    """
    Create a schematic diagram of a Single Degree of Freedom (SDOF) system with forces.
    Components: fixed wall, spring, damper, mass, and force arrows
    
    Returns:
    --------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots()
    # Draw mass rectangle:
    M_w = 2
    M_h = 1.2
    M_x = 0.0
    M_y = 0.0
    mass = Rectangle((M_x - M_w/2, M_y - M_h/2), M_w, M_h, 
                     edgecolor='darkblue', facecolor='lightblue', linewidth=2, alpha=0.9)
    ax.add_patch(mass)
    ax.text(M_x, M_y, 'Mass ($M$)', fontsize=14, ha='center', va='center', fontweight='bold')

    #Draw line supporting the damper and spring:
    ax.plot([-3, -3], [0-0.8, 0.8], color='black', linewidth=5)

    #Draw line supporting the damper and spring:
    ax.plot([-3, 2], [-0.82, -0.82], color='black', linewidth=3)

    # Draw spring:
    spring_x = np.linspace(-3, -1, 100)
    spring_amplitude = 0.1
    spring_y = 0.3 + spring_amplitude * np.sin(20 * np.pi * (spring_x + 3) / 3)
    ax.plot(spring_x, spring_y, color='orange', linewidth=2, label='Spring (K)')
    plt.text(-2, 0.45, r'spring ($k$)', fontsize=10, ha='center', color='black', fontweight='bold')

    # Draw damper box:
    damper_w = 0.3
    damper_h = 0.15
    damper_x = -2
    damper_y = -0.25
    damper = Rectangle((damper_x - damper_w/2, damper_y - damper_h/2), damper_w, damper_h, 
                       edgecolor='blue', facecolor='lightblue', linewidth=1, alpha=0.8)
    ax.add_patch(damper)
    ax.plot([-3, -2.15], [-0.25, -0.25], color='blue', linewidth=1) #([x_start, x_end], [y_connector, y_connector]
    ax.plot([-1.85, -1], [-0.25, -0.25], color='blue', linewidth=1) #([x_start, x_end], [y_connector, y_connector]

    plt.text(-2, -0.5, r'Damping ($c$)', fontsize=10, ha='center', color='black', fontweight='bold')

    # Draw circles for friction:
    radius = 0.08
    circle1 = plt.Circle((-0.72, -0.72), radius, color='red', fill=False, linewidth=2)
    circle2 = plt.Circle((0.72, -0.72), radius, color='red', fill=False, linewidth=2)
    ax.add_patch(circle1)
    ax.add_patch(circle2)

    # Add external force arrow:
    arrow = FancyArrowPatch((1, 0), (2, 0), arrowstyle='->', mutation_scale=20, color='green', linewidth=2)
    ax.add_patch(arrow)
    plt.text(2, 0.1, r'Force ($F_{external}$)', fontsize=10, ha='center', color='green', fontweight='bold')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.5, 1.)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('Schematic of SDOF System', fontsize=16)

    ax.text(0, -1.3, r'$F_k + F_c + F_i = F_{ext}$', fontsize=12, ha='center', color='black', fontweight='bold')

    return fig, ax