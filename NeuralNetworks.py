import numpy as np
import random, pickle


class NeuralNetwork:
    def __init__(self, layer_lengths ,act_func=None):
        if act_func is None:
            act_func = reLU
        act_func = np.vectorize(act_func)
        self.network = []
        for i in range(len(layer_lengths) - 1):
            self.network.append(NeuronLayer(layer_lengths[i], layer_lengths[i + 1], act_func))
        self.train_accuracy = 0.0  # the accuracy of the last 100 trains
        self.test_accuracy = 0.0 # the accuracy of all tests from last change of the network

    def __repr__(self):
        s = "==NEURAL NETWORK==\n"
        s += "Layers:\n"
        for i, layer in enumerate(self.network):
            s += "\tlayer {0}: ".format(i) + str(layer) + "\n"
        s += "Train accuracy rate: " + str(self.train_accuracy * 100) + "%\n"
        s += "Test accuracy rate: " + str(self.test_accuracy * 100) + "%\n"
        s += "Activation function: " + str(self.get_activation_func())
        return s

    def __str__(self):
        return repr(self)

    def run(self, curr_inputs):
        for layer in self.network:
            curr_inputs = layer.process(curr_inputs)
        return curr_inputs

    def train(self, database, batch_size=1, multiprocessing=False):
        raise NotImplementedError("train function for a neural network not implemented yet")

    def propagate(self, gradiant):
        raise NotImplementedError("backward propagation in a neural network not implemented yet")

    def calculate_gradiant(self, output, expected_output):
        raise NotImplementedError("calculate_gradiant for a neural network not implemented yet")

    def save(self, path):
        raise NotImplementedError("save function for a neural network not implemented yet")

    def load(self, layers_data):
        raise NotImplementedError("load function for a neural network not implemented yet")

    def get_activation_func(self):
        return self.network[0].act_func

class NeuronLayer:
    def __init__(self, input_size, output_size, act_func):
        self.neural_links = np.array([random.uniform(0, 1) for _ in range(input_size * output_size)])
        self.neural_links = self.neural_links.reshape((output_size, input_size))
        self.biases = np.array([random.uniform(0, 1) for _ in range(output_size)])
        self.act_func = act_func

    def process(self, input_vector):
        return self.act_func(np.matmul(self.neural_links, input_vector) + self.biases)


def load_network(path):
    raise NotImplementedError("load_network function not implemented yet")

def reLU(x):
    return max(0, x)

def main():
    network = NeuralNetwork([3, 4, 4, 1])
    v = np.array([random.uniform(0, 1) for _ in range(3)])
    print(network.run(v))


if __name__ == '__main__':
    main()
