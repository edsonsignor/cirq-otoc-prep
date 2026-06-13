# Quantum channel 

- More general physical evolution when we have things like measurement, noise, decoherence, loss of information to an environment, or discarded measurement outcomes. Closed systems we have $\rho \to U \rho U^\dagger$, in general a channel is given by $\rho \to \mathcal{E}(\rho) = \rho'$, but $\rho'$ is a still valid density matrix $\rho'$ and $Tr(\rho') = 1$.

- It can be written as sum of Kraus op.
$$ \mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger $$
many branches and possibly irresversible after averaging. For a closed system there is just one possible branch given by $U$, now for a open, general system multiple branches can exist each being represented by $E_k$. The channel is an avarege over possible Q branches.  

- However, E_k is not unique, then it might or might not correspond to the actual quantum trajectory. For example the Measurement of a qubit can be represented by $E_0 = |0\rangle \langle 0|, E_1 = |1\rangle \langle 1|$ or by $ E_0 = I/\sqrt{2}, E_1=Z/\sqrt{2}$. The former correspond exactly what we see when running an experiement, but the latter does not. 

- In open systems, Lindblad can be understood as an average over many stochastic quantum trajectories, as no-jump or jump histories. The smooth decay is the ensemble average. 

- Kraus ops. completeness condition:
$$  Tr(\rho ') = 1 = Tr(\mathcal{E}(\rho)) = Tr\Big(\sum_k E_k \rho E_k^\dagger\Big) = Tr\Big(\sum_k E_k^\dagger E_k \rho \Big) = Tr(\rho)$$
so, 

$$
\sum_k E_k^\dagger E_k = I
$$

## Positive operator-valued measure (POVM)

- The Kraus op. tells you what happens to the state in a branch k, but POVM element tells you the probability rule of that branch 
$$
M_k = E_k^{\dagger} E_k
$$
whre $\langle \psi | M_k | \psi \rangle  > 0  \to M_k > 0$ (all eigenvalues are nonnegative) and $\sum_k M_k = I$.
The propability of the outcome k evaluated on the state $\rho$ is $p_k = Tr(M_k \rho)$ 

- Summary: Kraus op tell you the state update $\rho \to (E_k \rho E_k^\dagger)/p_k$, whereas the POVM element tells you the prob. rule $p = Tr(M_k \rho)$.

### Selective vs Nonselective measurement

- Selective measurement means keeping the state after the measurement and condition the circuit based on the outcome. The post-measurement state becomes $\rho = \rho_k' = (E_k \rho E_k^\dagger)/p_k$

- Nonselective measurement means performing the measurement and discarding the result. The post-measurement state becomes $\rho_k' = \sum_k p_k \rho_k'$
