import numpy as np
import matplotlib.pyplot as plt


kh = np.linspace(0, 2* np.pi, 600)       # nondimensional wavenumber. Note that we're going till kh = 2 \pi
CFL = np.linspace(0.0, 2.0, 400)      # CFL range

CFL_grid, KH_grid = np.meshgrid(CFL, kh)

# analytic amplification factor (complex)
G = 1.0 - 1j * CFL_grid * np.sin(KH_grid) + (CFL_grid**2) * (np.cos(KH_grid) - 1.0)

absG = np.abs(G)


vmin = np.percentile(absG, 1)
vmax = np.percentile(absG, 99)


plt.figure(figsize=(8,5))
extent = [CFL.min(), CFL.max(), kh.min()/np.pi, kh.max()/np.pi]

img = plt.imshow(absG, origin='lower', aspect='auto',
                 extent=extent, vmin=vmin, vmax=vmax, cmap='jet')

cbar = plt.colorbar(img)
cbar.set_label(r'$|G(k\Delta x,\ \mathrm{CFL})|$')

# contour lines (include |G| = 1 stability boundary)
levels = [0.25, 0.5, 0.75, 1.0, 1.1, 1.2, 1.5]
CS = plt.contour(CFL_grid, KH_grid/np.pi, absG,
                 levels=levels, colors='white', linewidths=0.8)
plt.clabel(CS, inline=True, fmt='%g', fontsize=8)

plt.xlabel(r'$\mathrm{CFL} = \frac{c\,\Delta t}{\Delta x}$')
plt.ylabel(r'$\frac{k\Delta x}{\pi}$')
plt.title(r'Lax–Wendroff (Advection) — Analytical $|G(k\Delta x,\mathrm{CFL})|$')
plt.tight_layout()
plt.savefig("LW_G.png")