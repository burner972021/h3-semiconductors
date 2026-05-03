# Stuff not in formula sheet

for whatever reason

## Junction Capacitance 

$$ C_j = \epsilon A \sqrt{\frac{q}{2 \epsilon (V_0 - V_a)} \frac{N_a N_d}{N_a + N_d}} $$

## Storage Capacitance

### p+n junctions (negligible Q_n):

$$ C_s = \frac{q^2}{k_B T} A L_p p_{n0} \exp (\frac{qV}{k_B T}) $$



## Storage vs Junction capacitance:

- FORWARD BIAS: $C_j <<  C_s$
- REVERSE BIAS: $C_j >> C_s$

## Schottky Contact Current

$$ I_0 = A A^{**} T^2 (\exp(-\frac{q \phi_B}{K_B T})) $$

Where $A^{**}$ is Richardson's constant.

## Reverse Breakdown

$$ V_{br} = \frac{\epsilon_r \epsilon_0 (N_a + N_d)}{2 q N_a N_d} \xi_{max}^2 $$

## Ideal shottky barrier height

$$ q \phi _B = q (\phi _m - \chi) $$

This does not change with different bias as electron affinity is an intrinsic property of the semiconductor.


## Shottky contact vs Ohmic contact

### Shottky:  
- n-type: $ q \phi_m > q \phi_{sn} $
- p-type: $q \phi_m < q \phi_{sp} $

### Ohmic:
- n-type: $ q \phi_m < q \phi_{sn} $
- p-type: $ q \phi_m > q \phi_{sp} $