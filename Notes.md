# Square lattice vs Line lattice

- Two-qubit gates are physically local. Geometry determines the two-qubit gates. Locality enables the existence of the light-cone. 

Example of 3x3 grid

(0,0) -- (0,1) -- (0,2)
  |        |        |
(1,0) -- (1,1) -- (1,2)
  |        |        |
(2,0) -- (2,1) -- (2,2)

- Manhattan distance: $d[(r_[1], c_{1}), (r_2, c_2)] = |r_2 - r_1| + |c_2 - c_1|$
Number of step from one qubit to another. 

- Number of qubits affect: 
$$N_{linear} \sim v_B t, \quad \quad N_{square} \sim (v_B t)^2$$
- In a grid, direction can be controlled using different EG for different directions. 

- Operator support means how many qubits it acts as non-identity. 

## Lieb-Robinson bounds
- In local Q systems, info and op. cannot spread arbitrarily fast - lattice speed limit cause by locality. 

Say we have two operators $A_x$ and $B_y$ acting on different sites x and y, the commutator between $A_x(t)$ and $B_y$ is exp small outside an effective light cone
$$ || [A_x(t), B_y] || \lesssim  e^{-\mu(d(x,y) - v_{LR}t)}$$
where d(x,y) is the Manhathan distance between $x$ and $y$, $v_{LB}$ is the Lieb-Robison velocity, and $\mu$ is constant. 
The $v_{LB}$ is  a upper bound, the actual velocity is the butterfly. 


## Light-cone pruning

- Remove gates that don't affect an chosen observable - outside of the casual cone. 

- Idea: it is not every gate that the final observable depends on. It only depends on gates connected by a path of previous gates. 
Starting from the final measurment trace backwards throught the circuit (geometric light cone)
