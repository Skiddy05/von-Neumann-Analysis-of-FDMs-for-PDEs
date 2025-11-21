import numpy as np
import matplotlib.pyplot as plt

kh = np.linspace(0, np.pi, 600)
CFL = np.linspace(0.0, 2.0, 400)      # CFL (horizontal axis) - (limits adjustable)

CFL_grid, KH_grid = np.meshgrid(CFL, kh)
s = np.sin(KH_grid)

disc = 1.0 - (CFL_grid**2) * (s**2)
sqrt_disc = np.sqrt(disc.astype(complex))

G1 = -1j * CFL_grid * s + sqrt_disc
G2 = -1j * CFL_grid * s - sqrt_disc

absG = np.maximum(np.abs(G1), np.abs(G2))

if not np.isfinite(absG).all():
    finite_max = np.nanmax(absG[np.isfinite(absG)]) if np.any(np.isfinite(absG)) else 1.0
    absG = np.nan_to_num(absG, nan=finite_max, posinf=finite_max, neginf=finite_max)

vmin = np.percentile(absG, 1)
vmax = np.percentile(absG, 99)

plt.figure(figsize=(8,5))
extent = [CFL.min(), CFL.max(), kh.min()/np.pi, kh.max()/np.pi]  # [xmin, xmax, ymin, ymax]
img = plt.imshow(absG, origin='lower', aspect='auto', extent = extent, vmin = vmin, vmax = vmax, cmap='jet')
cbar = plt.colorbar(img)
cbar.set_label(r'$ \max(|G_1|,|G_2|)$')

levels = [1.2, 1.5, 2.0]
CS = plt.contour(CFL_grid, KH_grid/np.pi, absG, levels=levels, colors='white', linewidths=0.8)
plt.clabel(CS, inline=True, fmt='%g', fontsize=8)

plt.xlabel(r'CFL (ν = $a\,\Delta t/\Delta x$)')
plt.ylabel('kΔx / π')
plt.title(r'Leapfrog (Advection) — Analytical $ \max(|G_1|,|G_2|) $')
plt.tight_layout()
plt.savefig("Lpf_G.png")
plt.show()
