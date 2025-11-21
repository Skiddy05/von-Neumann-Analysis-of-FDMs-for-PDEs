import numpy as np
import matplotlib.pyplot as plt

thetas = [0.0, 0.25, 0.5, 0.75, 1.0]
nu_values = np.linspace(0, 2, 300)
kh = np.linspace(0, np.pi, 400)

# Meshgrid
NU, KH = np.meshgrid(nu_values, kh, indexing='ij')

S2 = np.sin(KH / 2.0) ** 2

def amplification_abs(theta):
    num = 1 - 4 * NU * (1 - theta) * S2
    den = 1 + 4 * NU * theta * S2
    return np.abs(num / den)

all_G = [amplification_abs(th) for th in thetas]

G_min = min(arr.min() for arr in all_G)
G_max = max(arr.max() for arr in all_G)

print("Global |G| min =", G_min)
print("Global |G| max =", G_max)

# Contour levels requested
contour_levels = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]

for theta in thetas:
    Gabs = amplification_abs(theta)

    plt.figure(figsize=(6, 5))

    # Heatmap
    hm = plt.imshow(
        Gabs,
        extent=[0, np.pi, nu_values[0], nu_values[-1]],
        origin='lower',
        aspect='auto',
        cmap='viridis',
        vmin=G_min,
        vmax=G_max
    )

    # Contours
    CS = plt.contour(
        KH, NU, Gabs,
        levels=contour_levels,
        colors='white',
        linewidths=1.1
    )
    plt.clabel(CS, inline=True, fontsize=8, fmt="%.2f", colors='white')

    # Labels
    plt.title(f"Heatmap of $|G(k)|$ for θ = {theta}")
    plt.xlabel(r"$k \Delta x$")
    plt.ylabel(r"$\frac{\alpha \Delta t}{(\Delta x)^2}$")
    plt.xlim(0, np.pi)
    plt.ylim(nu_values[0], nu_values[-1])

    # Colorbar
    cbar = plt.colorbar(hm)
    cbar.set_label(r"$|G(k)|$")

    plt.tight_layout()
    if theta == 0.0:
        plt.title(f"Heatmap of $|G(k)|$ for FTCS Scheme (Heat Equation)")
        plt.savefig(f"FTCS_H_G.pdf")
    elif theta == 0.5:
        plt.title(f"Heatmap of $|G(k)|$ for Crank-Nicolson Scheme")
        plt.savefig(f"CN_G.pdf")
    elif theta == 1.0:
        plt.title(f"Heatmap of $|G(k)|$ for BTCS Scheme (Heat Equation)")
        plt.savefig(f"BTCS_H_G.pdf")
    else:
        plt.title(f"Heatmap of $|G(k)|$ for θ = {theta}")
        plt.savefig(f"Gem_method_{theta}.pdf")