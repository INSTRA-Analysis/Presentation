#%% dependancies:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

# %%
def plot_SDOF_forces_abstract():
    """
    Create a schematic diagram of a Single Degree of Freedom (SDOF) system with forces.
    
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
    # ax.text(M_x, M_y, 'Mass ($M$)', fontsize=14, ha='center', va='center', fontweight='bold')

    #Draw line supporting the damper and spring:
    ax.plot([-3, -3], [0-0.8, 0.8], color='black', linewidth=5)

    #Draw ground line:
    ax.plot([-3, 2], [-0.82, -0.82], color='black', linewidth=3)

    

    # Draw circles for friction:
    radius = 0.08
    circle1 = plt.Circle((-0.72, -0.72), radius, color='red', fill=False, linewidth=2)
    circle2 = plt.Circle((0.72, -0.72), radius, color='red', fill=False, linewidth=2)
    ax.add_patch(circle1)
    ax.add_patch(circle2)

    # Add external force arrow:
    arrow = FancyArrowPatch((1, 0), (2, 0), arrowstyle='->', mutation_scale=20, color='green', linewidth=2)
    ax.add_patch(arrow)
    plt.text(2, 0.1, r'$F_{ext}$', fontsize=10, ha='center', color='green', fontweight='bold')

    # Add external force arrow:
    arrow = FancyArrowPatch((-1, 0.3), (-2, 0.3), arrowstyle='->', mutation_scale=20, color='blue', linewidth=2)
    ax.add_patch(arrow)
    plt.text(-2, 0.1, r'$F_{k}$', fontsize=10, ha='center', color='blue', fontweight='bold')

    # Add external force arrow:
    arrow = FancyArrowPatch((-1, -0.3), (-2, -0.3), arrowstyle='->', mutation_scale=20, color='blue', linewidth=2)
    ax.add_patch(arrow)
    plt.text(-2, -0.15, r'$F_{c}$', fontsize=10, ha='center', color='blue', fontweight='bold')

    # Add displacement arrow:
    ax.plot([0, 0], [0.6, 0.9], color='purple', linewidth=0.8)

    # Add external force arrow:
    arrow = FancyArrowPatch((0, 0), (-1.3, 0), arrowstyle='->', mutation_scale=20, color='blue', linewidth=2, linestyle='--')
    ax.add_patch(arrow)
    # Add dot at start point
    dot = plt.Circle((0, 0), radius=0.05, color='blue', zorder=10)
    ax.add_patch(dot)
    plt.text(0.1, 0.1, r'$F_{i}$', fontsize=10, ha='center', color='blue', fontweight='bold')

    arrow_D = FancyArrowPatch((-0.3, 0.75), (0.3, 0.75), arrowstyle='<->', mutation_scale=20, color='purple', linewidth=0.8)
    ax.add_patch(arrow_D)
    plt.text(0.2, 0.85, r'$u$', fontsize=10, ha='center', color='purple', fontweight='bold')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.5, 1.)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('Schematic of SDOF forces', fontsize=16)

    ax.text(0, -1.3, r'$F_k + F_c + F_i = F_{ext}$', fontsize=12, ha='center', color='black', fontweight='bold')

    return fig, ax

fig, ax = plot_SDOF_forces_abstract()
plt.show()

# %%
