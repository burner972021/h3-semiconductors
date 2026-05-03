# H3 — Semiconductor Physics & Devices
## Mock Test 2 — Worked Solutions

**Constants used throughout:**
*q* = 1.6 × 10⁻¹⁹ C ; *kT*/*q* = 0.0259 V ; *ε*₀ = 8.85 × 10⁻¹⁴ F/cm
*ε*<sub>s</sub>(Si) = 11.7 × *ε*₀ = 1.0355 × 10⁻¹² F/cm ; *n*<sub>i</sub>(Si) = 1.5 × 10¹⁰ cm⁻³
*N*<sub>c</sub>(Si) = 2.8 × 10¹⁹ cm⁻³

---

## Question 1 — PN Junction Electrostatics & Capacitance [22 marks]

**Given:** *N*<sub>a</sub> = 5 × 10¹⁷ cm⁻³, *N*<sub>d</sub> = 2 × 10¹⁶ cm⁻³, *A* = 5 × 10⁻⁴ cm².

### (a) Energy band diagram [3 marks]

On the p-side *E*<sub>F</sub> sits close to *E*<sub>V</sub> (since *N*<sub>a</sub> is heavy); on the n-side *E*<sub>F</sub> sits closer to *E*<sub>C</sub>. *E*<sub>F</sub> is **flat** across the junction in equilibrium. The bands bend across the depletion region — *E*<sub>C</sub>, *E*<sub>V</sub>, *E*<sub>i</sub> on the p-side are higher than on the n-side. The total band-bending equals *qV*<sub>bi</sub>. Because *N*<sub>a</sub> ≫ *N*<sub>d</sub>, most of the bending occurs on the n-side (*x*<sub>n</sub> ≫ *x*<sub>p</sub>).

### (b) Built-in potential [3 marks]

$$V_{bi} = \frac{kT}{q}\ln\!\left(\frac{N_a N_d}{n_i^2}\right) = 0.0259 \times \ln\!\left(\frac{(5\times10^{17})(2\times10^{16})}{(1.5\times10^{10})^2}\right)$$

$$= 0.0259 \times \ln(4.44\times10^{13}) = 0.0259 \times 31.42 = \boxed{0.814\text{ V}}$$

### (c) Depletion width, *x*<sub>n</sub>, *x*<sub>p</sub>, *E*<sub>max</sub> [7 marks]

$$W = \sqrt{\frac{2\varepsilon_s}{q}\,V_{bi}\,\frac{N_a + N_d}{N_a N_d}}$$

$$\frac{N_a + N_d}{N_a N_d} = \frac{5.2\times10^{17}}{1.0\times10^{34}} = 5.2\times10^{-17}\text{ cm}^3$$

$$W = \sqrt{\frac{2(1.0355\times10^{-12})}{1.6\times10^{-19}}(0.814)(5.2\times10^{-17})} = \sqrt{5.48\times10^{-10}}$$

$$\boxed{W = 2.34\times10^{-5}\text{ cm} = 0.234\ \mu\text{m}}$$

Charge balance gives *N*<sub>a</sub>*x*<sub>p</sub> = *N*<sub>d</sub>*x*<sub>n</sub>:

$$x_n = \frac{N_a}{N_a+N_d}W = \frac{5\times10^{17}}{5.2\times10^{17}}(0.234) = \boxed{0.225\ \mu\text{m}}$$

$$x_p = \frac{N_d}{N_a+N_d}W = \frac{2\times10^{16}}{5.2\times10^{17}}(0.234) = \boxed{0.009\ \mu\text{m}}$$

(As expected, *x*<sub>n</sub> ≫ *x*<sub>p</sub> since the n-side is more lightly doped.)

$$|E_{\max}| = \frac{q N_d x_n}{\varepsilon_s} = \frac{(1.6\times10^{-19})(2\times10^{16})(0.225\times10^{-4})}{1.0355\times10^{-12}}$$

$$\boxed{|E_{\max}| \approx 6.95\times10^{4}\text{ V/cm}}$$

### (d) Junction capacitance at *V*<sub>R</sub> = 5 V [5 marks]

Replacing *V*<sub>bi</sub> by (*V*<sub>bi</sub> + *V*<sub>R</sub>) = 5.814 V:

$$W' = \sqrt{\frac{2\varepsilon_s}{q}(V_{bi}+V_R)\frac{N_a+N_d}{N_aN_d}} = \sqrt{(1.294\times10^{7})(5.814)(5.2\times10^{-17})}$$

$$W' = 6.26\times10^{-5}\text{ cm} = 0.626\ \mu\text{m}$$

$$C_j = \frac{\varepsilon_s A}{W'} = \frac{(1.0355\times10^{-12})(5\times10^{-4})}{6.26\times10^{-5}} = \boxed{8.27\text{ pF}}$$

### (e) Why *C*<sub>j</sub> falls under reverse bias; why *C*<sub>s</sub> ≈ 0 [4 marks]

- **Junction capacitance:** *C*<sub>j</sub> = *ε*<sub>s</sub>*A*/*W*. Increasing *V*<sub>R</sub> widens *W*, so *C*<sub>j</sub> falls. Equivalently, more donor/acceptor charge is uncovered for the same *dV*, so |*dQ*/*dV*| decreases.
- **Storage (diffusion) capacitance:** Arises from *minority-carrier charge stored in the neutral regions* under forward bias. Under reverse bias the minority concentrations at the SCR edges fall to (essentially) zero, so there is no stored minority-carrier charge to modulate as *V* changes — *C*<sub>s</sub> is therefore negligible.

---

## Question 2 — Forward Bias and Breakdown [20 marks]

**Given:** *N*<sub>a</sub> = 10¹⁷ cm⁻³, *N*<sub>d</sub> = 5 × 10¹⁵ cm⁻³, *D*<sub>n</sub> = 25 cm²/s, *D*<sub>p</sub> = 10 cm²/s, *τ*<sub>n</sub> = 5 × 10⁻⁷ s, *τ*<sub>p</sub> = 10⁻⁷ s, *A* = 10⁻⁴ cm².

### (a) *I*₀ and forward current at *V*<sub>a</sub> = 0.62 V [6 marks]

Diffusion lengths:

$$L_n = \sqrt{D_n\tau_n} = \sqrt{(25)(5\times10^{-7})} = 3.54\times10^{-3}\text{ cm}$$

$$L_p = \sqrt{D_p\tau_p} = \sqrt{(10)(10^{-7})} = 1.0\times10^{-3}\text{ cm}$$

Equilibrium minority concentrations:

$$n_{p0} = \frac{n_i^2}{N_a} = \frac{2.25\times10^{20}}{10^{17}} = 2.25\times10^{3}\text{ cm}^{-3}$$

$$p_{n0} = \frac{n_i^2}{N_d} = \frac{2.25\times10^{20}}{5\times10^{15}} = 4.5\times10^{4}\text{ cm}^{-3}$$

Reverse-saturation current density:

$$J_0 = q\!\left(\frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p}\right)$$

$$= (1.6\times10^{-19})\!\left(\frac{25\cdot2250}{3.54\times10^{-3}} + \frac{10\cdot 4.5\times10^{4}}{10^{-3}}\right)$$

$$= (1.6\times10^{-19})(1.59\times10^{7} + 4.5\times10^{8}) = 7.45\times10^{-11}\text{ A/cm}^2$$

$$I_0 = J_0 A = (7.45\times10^{-11})(10^{-4}) = \boxed{7.45\times10^{-15}\text{ A}}$$

Forward current:

$$I = I_0\!\left[\exp(V_a/V_T) - 1\right] \approx (7.45\times10^{-15})\exp(0.62/0.0259)$$

$$I \approx (7.45\times10^{-15})(2.49\times10^{10}) = \boxed{0.186\text{ mA}}$$

### (b) Which side dominates [4 marks]

Inspect the two terms:
- Hole-injection term *D*<sub>p</sub>*p*<sub>n0</sub>/*L*<sub>p</sub> = 4.5 × 10⁸
- Electron-injection term *D*<sub>n</sub>*n*<sub>p0</sub>/*L*<sub>n</sub> = 1.59 × 10⁷

The hole current (holes injected from the heavily-doped p-side into the lightly-doped n-side) is ~28× larger and **dominates**. Physically: minority concentration on each side scales as *n*<sub>i</sub>²/*N*<sub>doping</sub>, so the *more lightly doped* side (the n-side here) has the *higher* minority population, giving the larger injection current. The current is therefore controlled by injection *into* the lightly-doped side.

### (c) Breakdown voltage [6 marks]

For a p⁺n one-sided junction with *N*<sub>a</sub> ≫ *N*<sub>d</sub>, *W* ≈ *x*<sub>n</sub> and (neglecting *V*<sub>bi</sub>):

$$x_n \approx \sqrt{\frac{2\varepsilon_s V_R}{qN_d}}, \qquad |E_{\max}| = \frac{qN_d x_n}{\varepsilon_s}$$

Eliminating *x*<sub>n</sub>:

$$|E_{\max}|^2 = \frac{2qN_d V_R}{\varepsilon_s}$$

Setting |*E*<sub>max</sub>| = *E*<sub>c</sub> at *V*<sub>R</sub> = *V*<sub>BR</sub>:

$$\boxed{V_{BR} = \frac{\varepsilon_s E_c^{\,2}}{2qN_d}}$$

Numerically:

$$V_{BR} = \frac{(1.0355\times10^{-12})(4\times10^{5})^2}{2(1.6\times10^{-19})(5\times10^{15})} = \frac{1.657\times10^{-1}}{1.6\times10^{-3}} \approx \boxed{104\text{ V}}$$

### (d) How to raise *V*<sub>BR</sub> [4 marks]

Since *V*<sub>BR</sub> ∝ 1/*N*<sub>d</sub>, **lower the doping on the lightly-doped side** (here *N*<sub>d</sub>). A lower *N*<sub>d</sub> widens the depletion region for any given *V*<sub>R</sub>, so the peak field reaches *E*<sub>c</sub> only at a larger *V*<sub>R</sub>. (Equivalent answers: insert a lightly-doped intrinsic region — i.e. a PIN structure — to spread the field; round the junction edges to avoid field crowding.)

---

## Question 3 — Schottky / Ohmic Contacts [18 marks]

**Given:** *qϕ*<sub>m</sub> = 4.75 eV, *qχ* = 4.01 eV, *N*<sub>d</sub> = 10¹⁶ cm⁻³, *A*\* = 110 A·K⁻²·cm⁻², *A* = 5 × 10⁻⁴ cm².

### (a) Barrier height and *V*<sub>bi</sub> [4 marks]

$$qϕ_B = qϕ_m - qχ = 4.75 - 4.01 = \boxed{0.74\text{ eV}}$$

$$qϕ_n = kT\ln(N_c/N_d) = 0.0259 \ln(2.8\times10^{19}/10^{16}) = 0.0259(7.94) = 0.206\text{ eV}$$

$$V_{bi} = ϕ_B - ϕ_n = 0.74 - 0.206 = \boxed{0.534\text{ V}}$$

### (b) *J*<sub>sT</sub> and *V*<sub>a</sub> for *I* = 1 mA [6 marks]

$$J_{sT} = A^* T^2 \exp(-qϕ_B/kT) = (110)(300)^2 \exp(-0.74/0.0259)$$

$$= 9.9\times10^{6} \times \exp(-28.57) = (9.9\times10^{6})(3.91\times10^{-13})$$

$$\boxed{J_{sT} \approx 3.87\times10^{-6}\text{ A/cm}^2}$$

$$I_0 = J_{sT}\,A = (3.87\times10^{-6})(5\times10^{-4}) = 1.94\times10^{-9}\text{ A}$$

For *I* = 10⁻³ A:

$$V_a = V_T\ln(I/I_0) = 0.0259\ln(10^{-3}/1.94\times10^{-9}) = 0.0259(13.16)$$

$$\boxed{V_a \approx 0.341\text{ V}}$$

### (c) Why Schottky has lower *V*<sub>on</sub> and faster switching [4 marks]

- **Lower turn-on voltage:** *J*<sub>sT</sub> for the Schottky (~10⁻⁶ A/cm²) is many orders of magnitude larger than *J*<sub>0</sub> for a pn junction (~10⁻¹¹ A/cm²). Since *V*<sub>a</sub> = *V*<sub>T</sub> ln(*J*/*J*<sub>0</sub>), a larger *J*<sub>0</sub> means a smaller *V*<sub>a</sub> is needed for the same current — hence the lower turn-on voltage seen here (0.34 V vs ~0.68 V).
- **Faster switching:** The Schottky diode is a *majority-carrier device*; current is carried by thermionic emission of electrons from the semiconductor over the barrier. There is essentially **no minority-carrier storage** in the neutral region, so no stored charge has to be removed when switching from forward to reverse bias. The pn junction stores significant minority-carrier charge (giving rise to the diffusion capacitance and storage time *t*<sub>s</sub>), which limits its switching speed.

### (d) Second metal *qϕ*<sub>m</sub> = 3.90 eV [4 marks]

The semiconductor work function is

$$qϕ_s = qχ + (E_C - E_F) = 4.01 + 0.206 = 4.216\text{ eV}$$

Since *qϕ*<sub>m</sub> = 3.90 eV < *qϕ*<sub>s</sub> = 4.216 eV, electrons flow from the metal *into* the n-Si on contact, forming an **electron accumulation layer** near the surface. This is an **ohmic contact** — no barrier in either direction, current flows linearly with applied voltage.

**Band diagram (after contact, equilibrium):** *E*<sub>F</sub> aligns; *E*<sub>C</sub> bends *downward* toward *E*<sub>F</sub> at the interface (no barrier seen by electrons travelling either way).

**Use in ICs:** Every device on a chip needs metal interconnections. Ohmic contacts provide a low-resistance, non-rectifying, bidirectional path between the metal interconnect and the semiconductor active region with negligible voltage drop.

---

## Question 4 — Light Emitting Diode [22 marks]

**Given:** n⁺p AlGaAs LED, *N*<sub>a</sub> = 5 × 10¹⁶ cm⁻³, *D*<sub>n</sub> = 200 cm²/s, *τ*<sub>n</sub> = 50 ns, *n*<sub>i</sub> = 5 × 10⁵ cm⁻³, *A* = 10⁻³ cm², *V*<sub>a</sub> = 1.10 V, *η*<sub>r</sub> = 0.6, *E*<sub>g</sub> = 1.85 eV, *n*₁ = 3.5, *n*₂ = 1.

### (a) Why direct-bandgap [3 marks]

Photon emission requires both *energy* and *momentum* conservation. In a **direct-bandgap** semiconductor the conduction-band minimum and valence-band maximum occur at the same crystal-momentum *k*, so an electron can recombine with a hole *vertically* in the *E*–*k* diagram and the photon (which carries negligible *k*) supplies the only momentum needed. Recombination is therefore highly probable and radiatively efficient.

In an **indirect-bandgap** material such as Si, the band extrema are at different *k*, so radiative recombination additionally requires a phonon to supply the momentum. The probability of this three-particle event is ~10⁶ times smaller, so Si is essentially useless as a light emitter.

### (b) Forward current at *V*<sub>a</sub> = 1.10 V [6 marks]

For an n⁺p diode, current is dominated by electron injection into the p-side:

$$L_n = \sqrt{D_n\tau_n} = \sqrt{(200)(5\times10^{-8})} = 3.16\times10^{-3}\text{ cm}$$

$$n_{p0} = \frac{n_i^2}{N_a} = \frac{(5\times10^5)^2}{5\times10^{16}} = 5\times10^{-6}\text{ cm}^{-3}$$

$$J_0 \approx \frac{qD_n n_{p0}}{L_n} = \frac{(1.6\times10^{-19})(200)(5\times10^{-6})}{3.16\times10^{-3}} = 5.06\times10^{-20}\text{ A/cm}^2$$

$$I_0 = J_0 A = 5.06\times10^{-23}\text{ A}$$

$$I \approx I_0 \exp(V_a/V_T) = (5.06\times10^{-23})\exp(1.10/0.0259)$$

$$= (5.06\times10^{-23})(2.78\times10^{18}) = \boxed{0.141\text{ mA}}$$

### (c) Optical output power [7 marks]

Internal optical power generated by radiative recombination:

$$P_{\text{int}} = \eta_r \cdot \frac{I}{q}\cdot E_g = \eta_r \cdot I \cdot \frac{E_g}{q} = (0.6)(1.41\times10^{-4})(1.85)$$

$$P_{\text{int}} = 1.57\times10^{-4}\text{ W} = 0.157\text{ mW}$$

External extraction efficiency:

$$F = \tfrac{1}{4}\!\left(\tfrac{n_2}{n_1}\right)^2\!\left[1-\!\left(\tfrac{n_1-n_2}{n_1+n_2}\right)^2\right]$$

$$= \tfrac{1}{4}(0.2857)^2\!\left[1-(0.5556)^2\right] = (0.02041)(0.6914) = 0.0141$$

So *F* ≈ 1.41 % — characteristic of a flat-surface III-V LED.

$$\boxed{P_{\text{opt}} = F\cdot P_{\text{int}} = (0.0141)(0.157\text{ mW}) \approx 2.2\ \mu\text{W}}$$

### (d) Wavelength and colour [3 marks]

$$\lambda = \frac{hc}{E_g} = \frac{1.24}{E_g\text{(eV)}}\ \mu\text{m} = \frac{1.24}{1.85} = \boxed{0.670\ \mu\text{m} = 670\text{ nm}}$$

This is in the **red** region of the visible spectrum.

### (e) Why measured *P*<sub>opt</sub> is even lower [3 marks]

Any one of:
- **Re-absorption inside the semiconductor:** emitted photons have *hf* ≥ *E*<sub>g</sub>, so the absorption coefficient is *not* zero — many photons are reabsorbed before reaching the surface.
- **Absorption by the top metal contact** (and shadowing of the emission area).
- **Additional non-radiative recombination** at surfaces, defects, and ohmic-contact regions, beyond what is captured in the bulk *η*<sub>r</sub>.

---

## Question 5 — Photodetector and Conceptual [18 marks]

### (a) Steady-state photocurrent [5 marks]

For a long, uniformly illuminated reverse-biased pn diode:

$$I_L = qG_L A\,(W + L_n + L_p)$$

$$W + L_n + L_p = (1.2 + 35 + 10)\times10^{-4} = 4.62\times10^{-3}\text{ cm}$$

$$I_L = (1.6\times10^{-19})(10^{21})(10^{-4})(4.62\times10^{-3})$$

$$\boxed{I_L \approx 7.4\times10^{-5}\text{ A} = 74\ \mu\text{A}}$$

### (b) Origin of the delayed component [4 marks]

Carriers generated in the *neutral* p- and n-regions are not subject to the strong field of the depletion region. They must first **diffuse** to the edge of the SCR before being swept across; this diffusion takes time of order *L*²/*D* — typically much slower than the drift transit through the SCR. This is the **delayed photocurrent**.

**Design fix:** use a **PIN photodiode**. The intrinsic *i*-region greatly widens the depletion region so almost all carriers are generated *inside* the SCR and contribute as fast (prompt) drift current. This raises both the speed of response and the ratio of prompt-to-delayed photocurrent.

### (c) I-V sketch [3 marks]

Sketch should show:
- Forward region: very small current up to ~0.6–0.7 V (turn-on/cut-in voltage *V*<sub>γ</sub>), then exponentially rising current.
- Reverse region: small, near-constant reverse-saturation current *I*<sub>0</sub> for −*V*<sub>BR</sub> < *V* < 0.
- At *V* = −*V*<sub>BR</sub>: sharp, near-vertical increase in reverse current (breakdown).

Axes labelled *I* (vertical) and *V* (horizontal), with *V*<sub>γ</sub> and *V*<sub>BR</sub> indicated.

### (d) Why a voltmeter cannot measure *V*<sub>bi</sub> [3 marks]

To measure *V*<sub>bi</sub> with a voltmeter you must form additional metal-semiconductor contacts on the p- and n-sides. Each of those contacts has its own contact potential. Around the closed loop (probe → p-region → junction → n-region → probe), Kirchhoff's voltage law gives a sum of zero: the contact potentials at the probes exactly cancel *V*<sub>bi</sub>. Equivalently, in thermal equilibrium *E*<sub>F</sub> is *flat* throughout the entire loop, so no current flows and the voltmeter reads zero. (If a voltage really did appear across the open terminals, current could flow through a load and energy would be extracted from a system in thermal equilibrium — a violation of the second law.)

### (e) Avalanche vs Zener breakdown [3 marks]

- **Avalanche:** the high field in the SCR accelerates mobile carriers to high kinetic energy; on collision with lattice atoms they break covalent bonds, creating new electron-hole pairs (impact ionisation). The new carriers are themselves accelerated and create more pairs — a chain reaction. Dominant at *moderate* doping (wider SCR, longer mean free path).
- **Zener (tunnelling):** in a *very heavily doped* junction the SCR is so narrow that the high field bends the bands sharply enough for valence-band electrons on the p-side to tunnel directly into empty conduction-band states on the n-side. No carrier multiplication is needed.

**In a heavily-doped junction, Zener (tunnelling) breakdown dominates.** (Empirically, *V*<sub>BR</sub> < ~4*E*<sub>g</sub>/*q* → Zener; *V*<sub>BR</sub> > ~6*E*<sub>g</sub>/*q* → avalanche.)

---

## Answer Key (numerical results)

| Q | Quantity | Answer |
|---|---|---|
| 1b | *V*<sub>bi</sub> | 0.814 V |
| 1c | *W* / *x*<sub>n</sub> / *x*<sub>p</sub> | 0.234 / 0.225 / 0.009 μm |
| 1c | *E*<sub>max</sub> | 6.95 × 10⁴ V/cm |
| 1d | *C*<sub>j</sub>(5 V) | 8.27 pF |
| 2a | *I*₀ ; *I*(0.62 V) | 7.45 fA ; 0.186 mA |
| 2c | *V*<sub>BR</sub> | ~104 V |
| 3a | *qϕ*<sub>B</sub> ; *V*<sub>bi</sub> | 0.74 eV ; 0.534 V |
| 3b | *J*<sub>sT</sub> ; *V*<sub>a</sub>(1 mA) | 3.87 μA/cm² ; 0.341 V |
| 4b | *I*(1.10 V) | 0.141 mA |
| 4c | *F* ; *P*<sub>opt</sub> | 1.41 % ; ~2.2 μW |
| 4d | *λ* | 670 nm (red) |
| 5a | *I*<sub>L</sub> | ~74 μA |