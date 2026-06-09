# OTOC

- Ehrenfest time: characteristic time when quantum correlators diverge from the corresponding classical correlators. 

- Introduced bu Larkin and Ovchinnikov in 1969. 

- Black-holes show exponential time-growth like classically chaotic systems. The Maldacena-Shenker-Stanford upper bound to the growth rate at temperature $T$ is $\lambda_L \leq 2\pi k_B T / \hbar$. 

- By preparing an operator in one site and the other in another site. OTOC measure the information scrambling. A velocity can be defined $v_{B}$, the state-dependent butterfly velocity. It is the light-cone slope to reach a site $l$ in a certain time "t".

- If $V = |\psi \rangle \langle \psi|$ and $W$ a evolution in a shor time, OTOC turns to a Loschmidt echo.

- OTOC can be divide in 3 time-regimes: Initial growth ($W(t)$ spreads), at the scrambling time, OTOC stops to grow (it decays a little bit). Long-time the mean is pratically constant with oscillations.  

- There are quantum chaotic systems which does not show exponential growth, but a power law.  

- System is scrambled when any subsystem has maximal enatanglement entropy. 

- Chaos is characterized by stretching and mixing. The former is related to the Lyapunov expoenent, which dictates short time behavior. THe latter relates to interdmediate times and can be quantified by the decay of correlation fucntions.

- Chaotic system the decay is exponential given by Ruelle-Pollicot resonances.

- For MBL systems, the propagation cone is logarithmic compared to the linear of ergotic systems. 

# Random Circuits

- Artificial chaotic evolution which make a local operator spread into many-qubit Pauli strings.

- After a sufficient depth the circuit can have aspects of Harr-random unitary design, like random evolution op.: called Haar/random-matrix limit. 

- Random circuit and Haar-random: the circuit has to have enough depth to approximate Haar moments relevant to the observable. It is not necessary a perfect Haar which requires infinite depth. 

- Haar-random unitary is matrix unifromaly chosen from a full unitary group.

- Unitary designs: Given an ensemble of circuits $\mathcal{E}=\{p_r, U_r\}$, it is a $k$-design if its $k$-fold average equals the Haar average:

$$
\sum_r p_r U_r^{\otimes k} O (U_r^{\dagger})^{\otimes k}
=
\int dU\, U^{\otimes k} O (U^{\dagger})^{\otimes k},
$$

where $U^{\otimes k} = U \otimes U \otimes \dots \otimes U$ with $k$ copies. In this way, an OTOC such as $\langle U^\dagger W^\dagger U V^\dagger U^\dagger W U V\rangle$ depends on second moments of the unitary ensemble and is connected to 2-design behavior. 


- Preare a Thermal state?

- Classical circuit, classical chaotic system. 

- Random matrix for Sensing?

# Info. scrambling

- Clifford gates: Puali string to Pauli strings (it can cause spreading)

- Non-Clifford: Pauli string to superposition of Pauli string.

- Ballistic light-cone spreading occurs for $iSWAP$, while fractional powers such as $\sqrt{iSWAP}$ only partially transfer population. Ex: $iSWAP |01 \rangle = i|10\rangle$, while $\sqrt{iSWAP}|01 \rangle = (|01\rangle + i|10\rangle)/\sqrt{2}$. 

- Op. spreading means growth of the Puali string $X_1 \to Z_1 X_2 Y_3 \dots$, while Op. entanglement means different superposition of Pauli strings $X_1 \to (Z_1 X_2 Y_3) + (Y_1 Y_2 Y_3) + i(Z_1 X_2 Z_3) \dots$

- Op. spreading is classical possible to characterize but Op. entanglement is not. 

# Classical vs. Quantum damaged circuit

## Classical 
Say $F$ is a random/chaotic map. So the classical protocol is:
$$x_0 \to F(x_0)=x_t \to \text{Damage one bit} = x'_t \to  F^{-1}(x'_t) \to x'_0 $$

Local damage inside the chaotic light cone destroyes the memory of the initial bit. Classical damage means bit flip or random bit. 


## Quantum 
Projective measurement is essentially the conditional operation: $\frac{1}{2}$ of the time it does nothing and $\frac{1}{2}$ of the time it applies $Z$. In the former, the echo is perfectly refocused. The $Z$ case still has memory from the initial state. Therefore, the probability to recover the state is

$$
P_{\mathrm{rec}} = \frac{1}{2}(1) + \frac{1}{2}\left(\frac{1}{2}\right) = \frac{3}{4}.
$$

Say a qubit density matrix:

$$
\rho =
\begin{pmatrix}
\rho_{00} & \rho_{01} \\
\rho_{10} & \rho_{11}
\end{pmatrix},
\qquad
\rho^\dagger = \rho,
\qquad
\operatorname{Tr}(\rho)=1,
\qquad
\rho \succeq 0.
$$

For a pure qubit state $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$, with $|\alpha|^2 + |\beta|^2 = 1$,

$$
\rho = |\psi\rangle\langle\psi| =
\begin{pmatrix}
|\alpha|^2 & \alpha\beta^* \\
\beta\alpha^* & |\beta|^2
\end{pmatrix}.
$$

If we measure and discard the result, the channel is 

$$
M(\rho) = \Pi_0 \rho \Pi_0 + \Pi_1 \rho \Pi_1
$$
where $\Pi_j = | j \rangle \langle j | $. Then, 
$$
\rho' = M(\rho) = \begin{pmatrix}
\rho_{00} & 0 \\
0 & \rho_{11}
\end{pmatrix}.
$$
exactly a dephasing channel, where the coherences (superposition,interferences,quantumness) are gone. 

However, $Z\rho Z = \begin{pmatrix}
\rho_{00} & -\rho_{01} \\
-\rho_{10} & \rho_{11}
\end{pmatrix} $, then $M(\rho) = \frac{1}{2} \rho + \frac{1}{2}Z\rho Z$. 


If we initialize the system at the state $\rho_0 = |1\rangle \langle 1| \otimes \rho_{rest}$. The protocol goes as $\rho_0 \to U \rho_0 U^{\dagger} \to M(U\rho_0 U^{\dagger}) \to U^{\dagger}M(U\rho_0 U^{\dagger}) U  \to Tr[P_1 U^{\dagger}M (U\rho_0 U^{\dagger}) U ] \to Tr[P_1 U^{\dagger}(\frac{1}{2}U\rho_0 U^{\dagger} + \frac{1}{2} Z_p U\rho_0 U^{\dagger} Z_p) U ]$. 

Meaning that 1/2 for Idenity giving the prob of getting 1  is $\frac{1}{2} Tr[P_{1} \rho_0] = 1/2$. The Z gives: $\frac{1}{2} Tr[P_{1} U^\dagger Z_p U \rho_0 U^\dagger Z_p U] = \frac{1}{2} Tr[P_{1} A^\dagger \rho_0 A]$, where $A$ is a scrabled operator deu to the random circuit. For a sufiencient depth, just look at the probe operator it can be with equal probability any Pauli op. $I, Z, Y, X$, where two preserves $|1\rangle$ and two flip to $|0\rangle$. Therefore,  $\frac{1}{2} Tr[P_{1} A^\dagger \rho_0 A] \approx \frac{1}{4}$. 

Finally the total probability to recover the state at $|1\rangle$ is the identy plus the Z $P_{\mathrm{rec}} = \frac{1}{2}(1) + \frac{1}{2}\left(\frac{1}{2}\right) = \frac{3}{4}$ 