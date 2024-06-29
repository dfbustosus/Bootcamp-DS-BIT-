import numpy as np

# Input data
input_data = np.array([3,5])

#Definir pesos (OJO AQUI)
weights = { 'node_0': np.array([2, 4]), 
            'node_1': np.array([ 4, -5]), 
            'output': np.array([2, 7])}

# Calcular valor de node 0: node_0_value
node_0_value = (input_data * weights['node_0']).sum()
print(node_0_value)

# Calcular valor de node 1: node_1_value
node_1_value = (input_data * weights['node_1']).sum()
print(node_1_value)

# Poner los valores de nodos en un array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_value, node_1_value])
print(hidden_layer_outputs)

# Calcular output
output = (hidden_layer_outputs*weights['output']).sum()

# Salida
print(output)