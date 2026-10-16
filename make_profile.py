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
    lines = textwrap.wrap(body, width=int(w / (body_size * 0.55)))
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

card("hero", 820, 330, PURPLE, INK, "COMPUTATIONAL PHYSICIST · PLASMA · GRAVITY",
     "COSMOTHEORETICIAN",
     "I build and stress-test numerical simulations: particle-in-cell parameter studies on HPC "
     "clusters, and my own solvers written to understand the physics from the ground up.")
card("focus", 380, 150, LIME, INK, "CURRENT FOCUS", "Verification first.",
     "Conservation laws, convergence and benchmarks before trusting a number.", title_size=30, body_size=16)
card("domains", 380, 160, DARK, PALE, "CORE DOMAINS", "Plasma · Gravity · Orbits",
     "Laser-plasma instabilities, N-body dynamics, mission trajectories.", title_size=28, body_size=16)

card("plasma", 600, 260, PURPLE, INK, "01", "Plasma physics",
     "Dimensionless relativistic two-fluid + Maxwell solver for SRS, SBS and TPD; 3D "
     "radiation-hydro ablation code with a C++/OpenMP core and Python frontend; coupled-mode "
     "and Vlasov models for growth rates, Landau damping and particle trapping.", title_size=40, body_size=17)
card("gravity", 600, 260, CORAL, INK, "02", "Gravitational dynamics",
     "A neutral reproduction and stress test of the 1990s twin-matter (negative mass) N-body "
     "simulations: 2D particle-mesh code with convergence tests, seed ensembles, and runs with "
     "and without cosmic expansion.", title_size=40, body_size=17)
card("orbits", 600, 260, LIME, INK, "03", "Orbital mechanics",
     "A sandbox for modelling real mission trajectories, perturbations and low-thrust manoeuvres.",
     title_size=40, body_size=17)
card("tooling", 600, 260, DARK, PALE, "04", "Tooling",
     "Pipelines that crawl, organise and analyse large document sets with LLMs; multi-agent "
     "workflows that write simulation stages behind human approval gates; GPU computing on AMD/ROCm.",
     title_size=40, body_size=17)
print("done")
