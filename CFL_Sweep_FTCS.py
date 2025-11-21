import numpy as np
import matplotlib.pyplot as plt


kh = np.linspace(0, np.pi, 600)      # nondimensional wavenumber (vertical axis)
CFL = np.linspace(0, 2.0, 300)       # CFL (horizontal axis)

CFL_grid, KH_grid = np.meshgrid(CFL, kh)


absG = np.sqrt(1.0 + (CFL_grid * np.sin(KH_grid)) ** 2)



vmax = np.percentile(absG, 99)
vmin = np.percentile(absG, 1)

plt.figure(figsize=(8,5))
extent = [CFL.min(), CFL.max(), kh.min()/np.pi, kh.max()/np.pi]  # [xmin, xmax, ymin, ymax]
img = plt.imshow(absG, origin='lower', aspect='auto', extent = extent, vmin=vmin, vmax=vmax, cmap = "jet")
cbar = plt.colorbar(img)
cbar.set_label('|G(kΔx, CFL)|')

levels = [1.0, 2.0, 2.5, 3.0]
CS = plt.contour(CFL_grid, KH_grid / np.pi, absG, levels=levels, colors='white', linewidths=0.8)
plt.clabel(CS, inline=True, fmt='%1.0f', fontsize=8)

plt.xlabel(r'CFL =  $ \frac{c \Delta t}{Δx}$')
plt.ylabel(r'$\frac{kΔx}{π}$')
plt.title('FTCS — Analytical |G(kΔx, CFL)|')
plt.tight_layout()
plt.savefig("FTCS_A_G.pdf")
plt.show()