from qiskit.quantum_info import Operator 
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister,Aer,execute
from qiskit.visualization import plot_histogram
import numpy as np
from math import sqrt

from qiskit.result import Counts

def search_counts(counts, target_key):
    if not isinstance(counts, Counts):
        raise ValueError("Input 'counts' should be of type 'Counts'.")

    if target_key not in counts.keys():
        print("Target key not found in the counts.")
        return None

    return counts[target_key]


def solve_maze(maze):
    # Get the number of rows and columns in the maze
    n = len(maze)
    m = len(maze[0])

    # Calculate the number of decisions and counting qubits
    num_decisions = n * m
    num_counting_qubits = int(num_decisions.bit_length())

    # Create a quantum circuit with the required number of qubits
    qc = QuantumCircuit(num_counting_qubits + num_decisions, num_counting_qubits)

    # Step 2: Determine the initial position
    for i in range(num_counting_qubits):
        qc.h(i)

    # Step 5: Repeat steps 2, 3, and 4 till reaching the end of the maze
    for step in range(num_decisions):
        # Step 2: Apply the up or down operation based on the maze
        row = step // m
        col = step % m
        if maze[row][col] == 1:  # Wall, go to the next step
            continue

        # Open path, apply a controlled-Z gate
        qc.h(num_counting_qubits + step)
        qc.mct(list(range(num_counting_qubits)), num_counting_qubits + step)
        qc.h(num_counting_qubits + step)

        # Step 3: Apply the Hadamard transformation
        qc.h(num_counting_qubits + step)

        # Step 4: Increase the counting qubits
        if step < num_decisions - 1:
            qc.barrier()
            for i in range(num_counting_qubits):
                qc.ccx(i, num_counting_qubits + step, num_counting_qubits + step + 1)


    # Measure the counting qubits
    qc.measure(range(num_counting_qubits), range(num_counting_qubits))

    # Simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator).result()
    counts = result.get_counts()
    print(qc)
    plot_histogram(counts)

    return counts, maze , qc


maze = [
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

# Solve the maze using the quantum algorithm
counts, final_maze, qc = solve_maze(maze)

#Print the measurement outcomes
print(f' {counts}')

#Print the final modified maze
for row in final_maze:
    print(row)
 
# to check if path to thhe exit is found 
target_key = '00100'
count = counts
result = search_counts(count, target_key)
print(f"Counts for '{target_key}': {result}")
