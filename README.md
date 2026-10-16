## Hi there 👋

I'm a physicist who mostly builds and stress-tests numerical simulations. My background is in laser-plasma physics, where I ran and analysed large particle-in-cell parameter studies on HPC clusters, and I've since been writing my own codes to understand the physics from the ground up.

## What I work on

**Plasma physics.** I've built a dimensionless relativistic two-fluid + Maxwell solver in Python for parametric instabilities (SRS, SBS, TPD), a 3D radiation-hydrodynamics ablation code with a C++/OpenMP core and a Python frontend, and coupled-mode and Vlasov models for studying growth rates, Landau damping and particle trapping.

**Gravitational dynamics.** I wrote a neutral reproduction and stress test of the 1990s "twin matter" (negative mass) N-body simulations: a 2D particle-mesh code with convergence tests, seed ensembles and runs with and without cosmic expansion, to find out where the original results hold and where they don't.

**Orbital mechanics.** I'm building a sandbox for modelling real mission trajectories, perturbations and low-thrust manoeuvres.

**Tooling.** I build pipelines that crawl, organise and analyse large document sets with LLMs, and multi-agent workflows where models write simulation stages with human approval gates before anything runs. I also do GPU computing on AMD/ROCm.

## How I work

What ties it together is verification. I check conservation laws, convergence and benchmarks against known analytic results before trusting a number.

## Stack

Python (NumPy, PyTorch) · C++ · OpenMP · pybind11 · Slurm · Linux/WSL
