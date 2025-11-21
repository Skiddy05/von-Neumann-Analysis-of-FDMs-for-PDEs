import numpy as np
import matplotlib.pyplot as plt

kh = np.linspace(0, np.pi, 600)
CFL = np.linspace(0, 5.0, 400)

CFL_grid, KH_grid = np.meshgrid(CFL, kh)

absG = 1.0 / np.sqrt(1.0 + (CFL_grid * np.sin(KH_grid)) ** 2)

vmin = 0.0
vmax = 1.0  # Clips all outliers

plt.figure(figsize=(8,5))
extent = [CFL.min(), CFL.max(), kh.min()/np.pi, kh.max()/np.pi]
img = plt.imshow(absG, origin='lower', aspect='auto', extent=extent, vmin=vmin, vmax=vmax, cmap='jet')
cbar = plt.colorbar(img)
cbar.set_label(r'$|G(k\Delta x, CFL)|$')

# contour lines to indicate damping levels
levels = [0.25, 0.5, 0.75, 0.99]
CS = plt.contour(CFL_grid, KH_grid / np.pi, absG, levels=levels, colors='white', linewidths=0.8)
plt.clabel(CS, inline=True, fmt='%0.2f', fontsize=8)

plt.xlabel(r'CFL = $ \frac {c\Delta t}{\Delta x} $')
plt.ylabel(r'$\frac{kΔx}{π}$')
plt.title('BTCS Scheme — Analytical |G(kΔx, CFL)|')
plt.tight_layout()
plt.savefig("BTCS_A_G.png")
plt.show()