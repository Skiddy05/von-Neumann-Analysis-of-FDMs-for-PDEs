import numpy as np
import matplotlib.pyplot as plt


kh = np.linspace(0, np.pi, 600)      # nondimensional wavenumber (vertical axis)
CFL = np.linspace(0.0, 2.0, 400)     # CFL (horizontal axis) - explore beyond 1 to show instability

CFL_grid, KH_grid = np.meshgrid(CFL, kh)

absG = np.sqrt((np.cos(KH_grid))**2 + (CFL_grid * np.sin(KH_grid))**2)

if not np.isfinite(absG).all():
    finite_max = np.nanmax(absG[np.isfinite(absG)]) if np.any(np.isfinite(absG)) else 1.0
    absG = np.nan_to_num(absG, nan=finite_max, posinf=finite_max, neginf=finite_max)

vmin = np.percentile(absG, 1)
vmax = np.percentile(absG, 99)

plt.figure(figsize=(8,5))
extent = [CFL.min(), CFL.max(), kh.min()/np.pi, kh.max()/np.pi]

img = plt.imshow(absG, origin='lower', aspect='auto',
                 extent=extent, vmin=vmin, vmax=vmax, cmap='jet')

cbar = plt.colorbar(img)
cbar.set_label(r'$|G(k\Delta x,\ CFL)|$ (Lax–Friedrichs)')

levels = [0.2, 0.5, 1.0, 1.2, 1.5, 2.0]
CS = plt.contour(CFL_grid, KH_grid/np.pi, absG,
                 levels=levels, colors='white', linewidths=0.8)

plt.clabel(CS, inline=True, fmt='%g', fontsize=8)

plt.xlabel(r'CFL (ν = $a\,\Delta t/\Delta x$)')
plt.ylabel(r'$k\Delta x / \pi$')
plt.title(r'Lax–Friedrichs (Advection) — Analytical $|G(k\Delta x, CFL)|$')
plt.tight_layout()
plt.savefig("LF_G.png")

