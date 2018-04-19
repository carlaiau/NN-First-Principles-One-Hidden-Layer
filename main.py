import numpy as np

#Input array
X=np.array([
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1]
])

#Output
y=np.array([
    [1],
    [1],
    [0]
])

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

#Variable initialization


epoch = 3000 #Setting training iterations

lr = 0.1 #Setting learning rate


inputlayer_neurons = X.shape[1]  #number of features in data set

hiddenlayer_neurons = 2 #number of hidden layers neurons

output_neurons = 1 #number of neurons at output layer

#weight and bias initialization

np.random.seed(1)


wh = np.random.uniform(size = (inputlayer_neurons,hiddenlayer_neurons) )
bh = np.random.uniform(size = (1, hiddenlayer_neurons) )
wout = np.random.uniform(size = (hiddenlayer_neurons,output_neurons) )
bout = np.random.uniform(size = (1,output_neurons) )

print("Intials")
print("weights hidden")
print(wh)
print("\nbias hidden")
print(bh)

print("weights out")
print(wout)
print("\nbias out")
print(bout)
print("\n\n")

for i in range(2):

    #Forward Propogation
    hidden_layer_input1 = np.dot(X,wh)

    print("hidden layer 1")
    print(hidden_layer_input1)
    print("\n")
    print("bh")
    print(bh)

    hidden_layer_input = hidden_layer_input1 + bh
    print("\n")

    print("hidden layer input")
    print(hidden_layer_input)
    print("\n\n\n")

    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1 = np.dot(hiddenlayer_activations,wout)
    output_layer_input = output_layer_input1+ bout
    output = sigmoid(output_layer_input)

    #Backpropagation
    
    E = y-output
    slope_output_layer = derivatives_sigmoid(output)
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) *lr
    bout += np.sum(d_output, axis=0,keepdims=True) *lr
    wh += X.T.dot(d_hiddenlayer) *lr
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr

print output