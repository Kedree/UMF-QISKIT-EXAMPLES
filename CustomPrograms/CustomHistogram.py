# KEDREE PROFFITT UM-F Alusp's Quantum Research Team
from qiskit import * # Imports
from qiskit.opflow import X,Y,Z,I,One,Zero
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import *
from qiskit.opflow import *
import time

qc = QuantumCircuit(3) # Make a basic circuit
qc.h([0,2]) # Hadamard the first qubit
qc.cx(0,1)

def getResults(qc, shots):
    qc.measure_all() # Gate to measure the qubits

    simulator = Aer.get_backend('aer_simulator') # Set our desired simulator, AER is for simulating ciruit on fake quantum machine
    qc = transpile(qc, simulator) # Does machine optimization, returns our optimized and prepared circuit, ready for simulation

    result = simulator.run(qc, shots = shots, memory=True).result() # Run a simulation and store the results, attempt 36000 times, get a list of all attempts results as memory

    counts = result.get_counts(qc) # Store the result numbers
    
    memory =(result.get_memory(qc)) # Get the list of attempts
    memory = pd.Series(memory) # Store it as a series, easier to manipulate
    memory = memory.sort_values() # Sort the values so that the color order is always the same, not neccessary

    unique=memory.unique()
    return counts, memory, unique

def plotCustHist(counts, memory, unique):
    #sns.set_style("whitegrid", {"grid.color": ".6"}) # Change Overall seaborn style

    qc.draw(output='mpl')
    
    counter = 0 # Counter used for labels

    qualitative_colors = sns.color_palette("muted", len(unique)) # Set our color palette for the plot
    qualitative_colors = qualitative_colors[::-1]

    pyplot.figure(figsize=(12,6)) # Set figure size

    ax = sns.histplot(x=memory, stat='percent', palette=qualitative_colors, shrink=0.75, hue=memory, hue_order=unique[::-1], alpha=1, edgecolor=(0,0,0,0)) # Create a histogram with memory as our y data, doing percentage calculataion, use color palette above, color by result
    ax.set(ylabel="Percent of Shots", xlabel="Final State") # Set the labels
    ax.yaxis.grid(True, linestyle='--', color='grey') # Turn on y axis grid
    ax.xaxis.grid(False) # Turn off x axis grid
    ax.tick_params(left=False) # Get rid of left ticks
    ax.set_axisbelow(True)

    labels = list(state + ": {}" for state in unique) # For every unique state get ready to format with counts
    for label in labels: # For every unique state from above:
        labels[counter] = label.format(counts[unique[counter]]) # Add the number of counts for each state from results
        counter += 1 # Move to the next state

    pyplot.legend(labels=labels, title="Counts", fancybox=True, framealpha=0.9) # Add a legend with the above labels

    sns.move_legend(ax, "upper left", bbox_to_anchor=(1,1)) # Move the legend to outside the figure
    sns.despine(left=True) # Remove the left, top, and right spines

    pyplot.title("Results", fontsize=20) # Add a title to the plot
    pyplot.show() # Show the plot

counts, memory, unique = getResults(qc, 36000) # Call the get results function
plotCustHist(counts, memory, unique) # Call the plot histogram function

# or plotCustHist(getResults(qc, 36000))

