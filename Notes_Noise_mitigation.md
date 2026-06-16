# Noise mitigation

Accept the noisy hardware, run multilple time to have a good prediction of the noise in the observable and with post-processing estimate what the system would have been noiseless. 

Different from Error correction which uses redundancy to encode the quantum information to detect the error and correct it. 

## Zero-noise extrapolation

- Run same logical noisy circuit, but run modified versions with deliberately amplified noise.

- Measure the observable vs noise level. By fitting the curve, extrapolate back to the hypothetical zero-noise value. 

say we have our observable $O(\lambda)$ affected by the noise scale $\lambda$. We find $O(\lambda) \sim a + b \lambda + c \lambda^2 + \dots$ and extrapolate $O_{ZNE} = O(0) \approx a$. 

### Circuit folding

The idea is simple, to amplify noise from the circuit, insert $U^\dagger U = I$. 

Nomenclature $U_{folded,3} = UU^\dagger U$, $U_{folded,5} = UU^\dagger U U^\dagger U, \dots$

Local folding: Instead of acting on the evolution operator, the folding is done in the gate level. Say we want to perform a gate $G$, the folded Gate will be $G_{folded,3} = GG^\dagger G$. It gives you more flexibility since one or two-qubit gates can be folded seperately, all gates, just one specific, and so on. 

Ex: $U = G_3 G_2 G_1$, $U_{folded} = G_3 (G_2 G_2^\dagger G_2) G_1$ 

To quantify $\lambda$, we basically assume gate count. Idle errors, leakage, readout, crosstalk 

- Statistical errors are small enough to make the fit meaningful.   
