import numpy as np

w = [0]
for i in range(1, 8):
    w.append(np.loadtxt(
        './static/train-data/weights{}.csv'.format(i), delimiter=','))


class ActivationFunction:
    def leaky_relu(self, x):
        return np.maximum(0.01, x)

    def leaky_relu_derivative(self, x):
        y = np.copy(x)
        y[x < 0] = 0.01
        y[x > 0] = 1
        return y

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        y = np.copy(x)
        y[x <= 0] = 0
        y[x > 0] = 1
        return y

    def sigmoid(self, x):
        x = np.clip(x, -100, 100)
        x = 1.0/(1 + np.exp(-x))
        return x

    def tanh(self, x):
        return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

    def softmax(self, x):
        exp_x = np.exp(x - np.amax(x))
        return exp_x / (np.sum(exp_x, axis=1, keepdims=True))


class NeuralNetwork:
    def __init__(self, layers):
        a, b = 0, 0.01
        self.layers = layers
        self.num_layer = len(layers)

        self.W = [0]*self.num_layer
        self.Z = [0]*self.num_layer
        self.A = [0]*self.num_layer
        self.dW = [0]*self.num_layer
        self.dZ = [0]*self.num_layer
        self.dA = [0]*self.num_layer

        self.D = [0]*self.num_layer

        for layer in range(1, self.num_layer):
            self.W[layer] = (b - a) * \
                np.random.rand(layers[layer-1] + 1, layers[layer]) + a

        self.activation_function = ActivationFunction()

        self.accuracy = []
        self.loss_train = []
        self.loss_test = []

    def __add_one_column(self, x):
        return np.concatenate((np.ones((x.shape[0], 1)), x), axis=1)

    def __forward(self, X, W):
        self.A[0] = X
        self.A[0] = self.__add_one_column(self.A[0])

        # -1 vì để dành layer cuối cho active output
        for layer in range(1, self.num_layer - 1):
            self.Z[layer] = np.dot(self.A[layer-1], W[layer])
            self.A[layer] = self.activation_function.relu(self.Z[layer])
            self.A[layer] = self.__add_one_column(self.A[layer])

        self.Z[-1] = np.dot(self.A[-2], W[-1])
        self.A[-1] = self.activation_function.softmax(self.Z[-1])

    def __backpropagation(self, X, Y):

        self.dZ[-1] = self.A[-1] - Y
        self.dW[-1] = np.dot(self.A[-2].T, self.dZ[-1]) / X.shape[0]
        for layer in reversed(range(1, self.num_layer - 1)):  # tương tự
            self.dA[layer] = np.dot(self.dZ[layer+1], self.W[layer+1].T)
            self.dA[layer] = self.dA[layer][:, 1:]
            self.dZ[layer] = self.dA[layer] * \
                self.activation_function.relu_derivative(self.Z[layer])
            self.dW[layer] = np.dot(
                self.A[layer-1].T, self.dZ[layer]) / X.shape[0]

    def __create_mini_batch(self, X, Y, batch_size):

        batch_X = []
        batch_Y = []
        data = np.hstack((X, Y))
        np.random.shuffle(data)
        iter = X.shape[0] // batch_size

        for i in range(0, iter):
            batch_X.append(data[i * batch_size:(i + 1) *
                           batch_size][:, :self.layers[0]])
            batch_Y.append(data[i * batch_size:(i + 1) *
                           batch_size][:, self.layers[0]:])
        if iter % batch_size != 0:
            batch_X.append(X[(i + 1) * batch_size: -1])
            batch_Y.append(Y[(i + 1) * batch_size: -1])
        return batch_X, batch_Y, iter

    def __adam_processing(self, v, s, beta1, beta2, k):

        for layer in range(1, self.num_layer):
            v[layer] = beta1*v[layer] + (1 - beta1)*self.dW[layer]
            # v[layer] /= (1 - beta1**k)
            s[layer] = beta2*s[layer] + \
                (1 - beta2)*(self.dW[layer]**2)
            # s[layer] /= (1 - beta2**k)

        return v, s

    def __update_weight_normal(self, LR):
        for layer in range(1, self.num_layer):
            self.W[layer] -= LR * self.dW[layer]

    def __update_weight_adam(self, LR, v, s, beta1, beta2, k, epsilon):
        v, s = self.__adam_processing(v, s, beta1, beta2, k + 1)
        for layer in range(1, self.num_layer):
            self.W[layer] -= LR * \
                np.array(v[layer] / np.sqrt(s[layer] + epsilon))

    def __update_performance(self, X, Y, k):

        self.__forward(X, self.W)

        Y1 = np.zeros((Y.shape[0], Y.shape[1]))
        cnt = 0
        for i in range(len(self.A[-1])):
            Y1[i][np.where(self.A[-1][i] == np.amax(self.A[-1][i]))] = 1
            comparsion = Y[i] == Y1[i]
            if comparsion.all():
                cnt += 1
        self.accuracy.append(cnt)

        loss = -np.nansum(Y*np.log(self.A[-1])) / X.shape[0]
        self.loss_train.append(loss)

        print("Epoch: " + str(k) + " Loss: " + str(loss) +
              " Accuracy: " + str(cnt*100/len(X)))

    def train(self, X, Y, optimizer, LR=0.01, batch_size=32, beta1=0.9, beta2=0.99, epsilon=10e-8, decay=False, DR=1, epoch=1000, verbose=True):

        LR_0 = LR
        DR = 0.1

        if optimizer == "gd":
            batch_size = X.shape[0]
        elif optimizer == "mini":
            pass
        elif optimizer == "adam":
            v = [0]*self.num_layer
            s = [0]*self.num_layer

        for k in range(epoch):
            batch_X, batch_Y, iter = self.__create_mini_batch(X, Y, batch_size)\

            for mini in range(iter):
                self.__forward(batch_X[mini], self.W)
                self.__backpropagation(batch_X[mini], batch_Y[mini])

                if optimizer == "gd" or optimizer == "mini":
                    self.__update_weight_normal(LR)
                elif optimizer == "adam":
                    self.__update_weight_adam(
                        LR, v, s, beta1, beta2, k, epsilon)

            if decay:
                LR = LR_0 / (1 + DR * k)

            if verbose:
                self.__update_performance(X, Y, k)

    def predict(self, test):
        # change w to self.W if dont wanna use trained weights
        self.__forward(test, w)
        self.result = self.A[-1]
        return self.result
