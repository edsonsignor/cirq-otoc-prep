# Op. spreading vs entanglement paper (2021 Google Science)

## Experimental techniques

(SPAM) State preparation and readout error. 

- iSWAP are better invertable to echo than some CPHASE used before. For inverted PowISWAP's there is a convinient formula using the actual gate and some 1Q Z gates. 

- The pulse naturally implement $PhasedFSim$ gate: $U_{PhasedFSim}(\theta, \phi, \Delta_+, \Delta_-, \Delta_{-,off})$. For $(\pi/2,0,0,0,0)$ gives $ISWAP$ and $(\pi/4,0,0,0,0)$ gives $\sqrt{ISWAP}$.  

- The implementation of PowISWAP through PhasedFSim generate unwanted coniditonal phase errors - it comes from the interaction of $|01 \rangle$ and $|10 \rangle$ to $|20 \rangle$ and $|02 \rangle$. Since this is from second-order perturbation theory, it scales as $\phi \propto g_{max}^2$ whereare $\theta \propto g_{max}$. Time of the gate can be increased $t_p$ by decreasing $g_{max}$, but this results in a increase decoherence effect. They set the parameters and know the $\theta$ and $\phi$. 

- After setting the gate parameters, use XEB to find the values of $\theta$ and $\phi$. After that, it uses $(\Delta_+, \Delta_-, \Delta_{-,off})$ to further reduce $\phi$. Find $\Delta_+ = \phi_a /2$ to minimize the non-identity weight
$$
r_p = 1 - \frac{1}{D^2}|Tr(U^\dagger_a U_t)|^2
$$
where $U_t$ is the target gate and $U_t$ is the actual gate. 

- 1Q Z rotations can be recompiled since it is used in the PowISWAP's inverse are also used in the FSim for the phases. Using some properties of Z and $R_x$ and $R_y$, and $ISWAP$, they can change their order and merge. 

- they do XEB for gate error benchmarking of ISWAP and sqrt. ECDF (empirical cumulative distribution function): it tells you the fraction of gates/pairs whose error is less than or equall to x. See worse error from before due to slower gates. 
-By running 2Q gates pairs alone give one error, but when other XEB are done simultanously, the error increased. This indicates cross-talk erros. 

- To reduce the cross-talk, they fit from the PhasedFSim wi the $\Delta s$. They add Z rotations to offset the shifts. 

- Dynamical decoupling (error mitigation): pulse trick to suppress slow dephasing noise due to idling. The ancilla has to wait the echo in idling, this can effect the coherence with the measument qubit. So, they do a spin echo XX- YY-ZZ to preserve the coherence. The idea comes that dephazing is essentially a Z gate, X and Y changes signs which on average descreases the dephasing XZX = -Z, ..., not just XXXX... because it can accumlate coherent erros form the 1Q gate. XXYY has the better cycling.  

- Any offset in the measurement is very detrimental specially for small values,  $\langle \sigma_y \rangle \to \langle \sigma_y \rangle + d$.
Say $a = P(report 1| true 0)$ and $b = P(report 1| true 1)$. Prob to measure $|1\rangle$ is $P_{\uparrow}^{meas} = a(1 - P_{\uparrow}^{true}) + bP_{\uparrow}^{true} = a + (b-a)P_{\uparrow}^{true}$. Since $\langle \sigma_y \rangle = 2P_{\uparrow} -1$, $P_{\uparrow}^{meas} = a + (b-a)(1+\langle \sigma_y \rangle_{true})/2$, then 
$$
\langle \sigma_y \rangle_{meas} = 2P_{\uparrow}^{meas} -1 = (a+b -1) + (b-a)\langle \sigma_y \rangle_{true}
$$
How to deal with the offset?
Balanced readout: Measure rotating $R_x(\pi/2)= \sqrt{X}$ and $R_x(-\pi/2)= -\sqrt{X}$. So, $P_{\uparrow, \pm} = (1 \pm \langle \sigma_y \rangle)/2$. Then, $P_{\uparrow, +} - P_{\uparrow, -} = \langle \sigma_y \rangle)$. The offset is canceled. 
However the observable is also biased by the state preparation and the first rotation (like cross-talk, imperfect rotation, ...). The ancilla starts with a phase $\phi_p$ and is measured with a phase $\phi_m$, therfore we extend the observable to 
$$
\langle \sigma_y \rangle =\frac{1}{2} (P_{\uparrow, ++} - P_{\uparrow, +-} - P_{\uparrow, -+} + P_{\uparrow, --}) 
$$


-Light-cone pruning: Gates outside the light of from the butterfly qubit to the initial states can be filtered out. Also, the gates outside of the light cone from the measured qubit (q1) to the butterfly can be filtered out. The removal makes some qubits with a longer idling time, which means they can be subjected to decoherence, the same spin echo can be performed as it was done to the ancilla to mitigate that. 

- Normalization for Random circuits with fewer non-Clifford gates, the normalization can change from $\langle \sigma_y \rangle_B / \langle \sigma_y \rangle_I$ to $\langle \sigma_y \rangle_B / \langle \sigma_y \rangle_{B,Clifford}$, where the latter is contrsucted with the same 1Q and 2Q gates and butterfly op., but all non-cliffor gates are changed by random pauli X and Y. It uses the fact that $U_{clifford}PU_{clifford}^\dagger = \pm P$, therefore the ideal OTOC should be $\pm 1$. Therefore, it gives a better scalling factor than the previous option. 


# Constructive interference in quantum ergodicity (2025 Google Nature)

## Main text

- Different from the usual OTOC, an higher order OTOC(2) can be sensitive to the interference of many different Pauli strings of $B(t)$. OTOC(1) just concerns if $B(t)$ reaches or not the measument qubit. 

- OTOC(1) has not off-diagonal terms (less complexity) deu to the Trace orthogonality of Pauli Op.
$$
C^{(2)} = \frac{1}{D}Tr[B(t)MB(t)] = \frac{1}{D}Tr\left[ \left( \sum_\alpha b_\alpha P_\alpha \right)M\left( \sum_\beta b_\beta P_\beta \right) \right] = \sum_{\alpha,\beta} b_\alpha b_\beta \frac{1}{D}Tr{P_\alpha MP_\beta M} = \sum_{\alpha,\beta} b_\alpha b_\beta s_beta\frac{1}{D}Tr{P_\alpha P_\beta} = \sum_\alpha b_\alpha^2s_\alpha \\
= \sum_{\alpha \in commute} b_\alpha^2 - \sum_{\alpha \in anticommute} b_\alpha^2 = \sum_{\alpha \in commute} b_\alpha^2 + \sum_{\alpha \in anticommute} b_\alpha^2 - 2\sum_{\alpha \in anticommute} b_\alpha^2 = \sum_{\alpha} b_\alpha^2 - 2\sum_{\alpha \in anticommute} b_\alpha^2 = 1 - 2p_{anti}
$$
where we use $(1/D)Tr(P_\alpha P_\beta) = \delta_{\alpha,\beta}$ and $MP_\beta M = \pm P_\beta = s_\beta R_\beta$ for M being Pauli. 
However, for $C^{(4)} \proto \frac{1}{D}Tr{P_\alpha P_\beta P_\gamma P_\delta}$, give us more freedom because for any Pauli string if there is a non-Identity pauli the Trace is zero. EX: $Tr(I\0time I X) = Tr(I)Tr(X) = 0$, because X, Y, and Z are traceless. So, the only way of $Tr(Pauli) \ neq 0$ is if the Pauli is the Identity. Before, for the simple OTOC, this was only possible if the Puali were equal because $PP = I$. Now, that we have a 4 Pauli, we have more freedom. Ex: XYXY = -I, then it contributes. The resctrion is then $P_\alpha P_\beta P_\gamma P_\delta \propto I$, which measn this path form a loop. We initiate at a certain state, it jumps from Pauli to Pauli, until it comes back. 

- The problem is that $OTOC^{(4)}$ has also diagonal parts like the previous OTOC, if $P_\alpha P_\beta = P_\gamma P_\delta = I$. To differiencte two cases (to obtain $C_{diag}$ and $C_{off-diag}$), they insert random pauli during the evolutions. The off-diagonal contributions are way more sensitive to those insertions than the diagonal ones. Therefore, an average over many insertions 

- Inifinite temperature state $\rho_{\infty}=I/2^N$
