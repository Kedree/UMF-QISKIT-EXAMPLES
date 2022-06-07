# Circuit Basics

## Circuit Creation and Representation (Testing to show different heading sizes)

### Circuit Code

Basic Quantum Circuits can be made quite easily but more complexities can be added:
One can make quantum circuit with qubits as such:

```
'Circuit Name' = QuantumCircuit('# Qubits', '# Classical Bits', name="Name")
```

'Classical bits' and 'name' are optional components that can be added in.

### Making A Simple Circuit

An example of a simple circuit is as follows:
```
qc = QuantumCircuit(2,2)
```

### Simple Circuit Representation Code

To see a representation of our circuit we can use the code below:

```
'Circuit Name'.draw('Optionals available, see Representation documentation')
```

### Circuit Representation

The most simple form of this command is as follows using the above simple circuit with the variable name of 'qc':
```
qc.draw()
```

This will print a plot that should look like this:

![Basic Circuit](BasicCircuit.PNG?raw=true "Basic Circuit")

The above plot shows a quantum circuit which consists of two qubits (qubit 0 or q0 and qubit 1 or q1) starting from zero as programmers love zero. Alongside these two qubits is the two classical bits, these are put together onto one line graphically and are only used for measuring a quantum state.
