import numpy as np, matplotlib.pyplot as plt, textwrap, os
os.makedirs("assets", exist_ok=True)

# --- banner: a parametric instability growing in space-time -------------
x = np.linspace(0, 40, 1600); t = np.linspace(0, 12, 400)
X, T = np.meshgrid(x, t)
rng = np.random.default_rng(3)
field = sum(np.exp(0.35*g*T) * np.sin(k*X - w*T + p)
            for k, w, g, p in zip(rng.uniform(1, 4, 7), rng.uniform(2, 6, 7),
                                  rng.uniform(0.4, 1, 7), rng.uniform(0, 6.3, 7)))
field *= np.exp(-((X-20)/14)**2)
fig, ax = plt.subplots(figsize=(16, 3.6), dpi=100)
ax.imshow(field, cmap="magma", aspect="auto", origin="lower",
          vmin=-np.abs(field).max()*0.6, vmax=np.abs(field).max()*0.6)
ax.axis("off"); fig.patch.set_alpha(0); fig.tight_layout(pad=0)
fig.savefig("assets/banner.svg", transparent=True); plt.close()

# --- cards ---------------------------------------------------------------
def card(name, w, h, bg, fg, kicker, title, body, title_size=48, body_size=19):
    lines = textwrap.wrap(body, width=int(w / (body_size * 0.62)))
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
           f'<rect width="{w}" height="{h}" rx="22" fill="{bg}"/>',
           f'<text x="36" y="48" font-size="13" letter-spacing="3" font-weight="700" fill="{fg}" opacity="0.75">{kicker}</text>',
           f'<text x="36" y="{48+title_size+18}" font-size="{title_size}" font-weight="800" fill="{fg}">{title}</text>']
    y = 48 + title_size + 18 + 42
    for ln in lines:
        svg.append(f'<text x="36" y="{y}" font-size="{body_size}" font-weight="500" fill="{fg}">{ln}</text>')
        y += body_size * 1.5
    svg.append('</svg>')
    open(f"assets/{name}.svg", "w").write("\n".join(svg))

PURPLE, LIME, DARK, CORAL, INK, PALE = "#8b7cf6", "#d4ff3f", "#1a1d24", "#f28b6a", "#0f1117", "#f5f5f7"

card("hero", 820, 280, PURPLE, INK, "COMPUTATIONAL PHYSICIST · PLASMA · COSMOLOGY",
     "COSMOTHEORETICIAN",
     "I build and stress-test numerical simulations: particle-in-cell parameter studies on HPC "
     "clusters, and my own solvers written to understand the physics from the ground up.")
card("focus", 380, 200, LIME, INK, "CURRENT FOCUS", "Verification first.",
     "Conservation laws, convergence and benchmarks before trusting a number.", title_size=30, body_size=16)
card("domains", 380, 210, DARK, PALE, "CORE DOMAINS", "Plasma · Cosmology · Orbits",
     "Laser-plasma instabilities, expansion histories, mission trajectories.", title_size=28, body_size=16)

# Selected work: a description card (left) and a figure panel (right) per row, all 600x338
card("thesis", 600, 338, CORAL, INK, "01 · BACHELOR THESIS", "Parametric plasma waves",
     "2D particle-in-cell campaign on HPC: a laser crossing an underdense gas jet near the "
     "quarter-critical density. The stimulated Raman back-scatter wave saturates at 0.55 TV/m "
     "through electron trapping, up to 0.75 TV/m with short pulses. Every number checked against "
     "16 particles per cell and independent random seeds.", title_size=40, body_size=17)
card("plasma", 600, 338, PURPLE, INK, "02", "Plasma physics",
     "icfsim, a verification-first radiation-hydrodynamics code for inertial confinement fusion, "
     "growing toward an integrated direct-drive implosion validated against OMEGA data. Also a "
     "relativistic two-fluid + Maxwell solver for SRS, SBS and TPD, and coupled-mode and Vlasov "
     "models for growth rates, Landau damping and particle trapping.", title_size=40, body_size=17)
card("cosmology", 600, 338, DARK, PALE, "03", "Cosmology",
     "skua, a test rig for cosmological expansion histories: validated against DESI DR2, Planck "
     "and three supernova catalogues, and used to reproduce and calibrate the evidence for "
     "evolving dark energy. Plus background fits of alternative cosmologies to BAO, supernovae "
     "and cosmic chronometers with MCMC posteriors.", title_size=40, body_size=17)
card("orbits", 600, 338, LIME, INK, "04", "Orbital mechanics",
     "orbit-lab, a real-time 3D orbit visualizer in the browser: 15,000+ satellites propagated "
     "with SGP4, and lunar missions including a reconstruction of ispace's RESILIENCE validated "
     "against radio-telescope Doppler data.", title_size=40, body_size=17)

# figure panels: the source figure fitted into a rounded 1200x676 panel (2x of 600x338)
from PIL import Image, ImageDraw
def panel(name, src, bg):
    W, H, pad = 1200, 676, 28
    im = Image.open(f"assets/src/{src}").convert("RGB")
    k = min((W - 2*pad) / im.width, (H - 2*pad) / im.height)
    im = im.resize((round(im.width*k), round(im.height*k)), Image.LANCZOS)
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(out).rounded_rectangle((0, 0, W-1, H-1), 44, fill=bg)
    out.paste(im, ((W - im.width)//2, (H - im.height)//2))
    out.save(f"assets/{name}.png", optimize=True)
panel("plasma-fig", "icfsim_resolution.png", "#1a1d24")
panel("cosmology-fig", "skua_w0wa.png", "#ffffff")
panel("orbits-fig", "orbit_lab.png", "#000000")
print("done")
