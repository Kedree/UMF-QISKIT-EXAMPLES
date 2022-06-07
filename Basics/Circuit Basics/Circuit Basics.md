Basic Quantum Circuits can be made quite easily but more complexities can be added:
One can make quantum circuit with qubits as such:
```'Circuit Name' = QuantumCircuit('# Qubits', '# Classical Bits', name="Name")```

As an example of a simple circuit:
```qc = QuantumCircuit(2,2)```
'Classical bits' and 'name' are optional components that can be added in.

To see a representation of our circuit we can use the code below:
```'Circuit Name'.draw('Optionals available, see Representation documentation')```

The most simple form of this command is as follows:
```'Circuit Name.draw()'```

This will print a plot that should look like this:      ![Alt text](BasicCircuit.PNG?raw=true "Optional Title")
