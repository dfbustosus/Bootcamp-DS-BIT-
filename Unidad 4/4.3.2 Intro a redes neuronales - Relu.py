import numpy as np

# Input data
input_data = np.array([3,5])

#Definir pesos (OJO AQUI)
weights = { 'node_0': np.array([2, 4]), 
            'node_1': np.array([ 4, -5]), 
            'output': np.array([2, 7])}

def relu(input):
    '''relu activation function'''
    output = max(0, input)
    return(output)

# node_0_output
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = relu(node_0_input)

# node_1_output
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = relu(node_1_input)

# hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_output, node_1_output])

# Relu
model_output = (hidden_layer_outputs * weights['output']).sum()
print(model_output)


#### Generalizando
def predict_with_network(input_data_row, weights):
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)
    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)
    return(model_output)

input_data = [np.array([3, 5]), np.array([ 1, -1]), np.array([0, 0]), np.array([8, 4])]

# Lista para resultados
results = []
for input_data_row in input_data:
    results.append(predict_with_network(input_data_row,weights))

print(results)