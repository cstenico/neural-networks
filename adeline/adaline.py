import random
random.randrange(start=-1, stop=1)
class Adaline:

    def __init__(self):
        self.weights = []
        self.expected_outputs = []
        self.inputs = []
        self.error = 1
        self.alpha = 0.9
        self.function = 1

    def setInput(self, input):
        if inputs.__len__() >= 2:
            self.inputs = inputs
            self.weights = []
            for i in range(0, inputs[0].__len__()):
                self.weights.append(random.random())

    def setExpectedOutputs(self, outputs):
        if expected_outputs.__len__() >= 2:
            self.expected_outputs = expected_outputs

    def test(self, numEntrada):
        sum = self.sum(numEntrada)
        if sum == self.function:
            return 1
        elif sum == -self.function:
            return -1
        return 0

    def sum(self, numinput):
        sum = 0
        for i in range(0, self.inputs[numinput].__len__()):
            sum += self.weights[i] * self.inputs[numinput][i]
        return sum

    def learning(self):
        if self.expected_outputs.__len__() != self.inputs.__len__():
            raise Runtimeerrorr('Whoops! O desejadas.'
                                )
        while self.error != 0:
            self.error = 0
            self.training()

    def training(self):
        for i in range(0, self.inputs.__len__()):
            test = self.test(i)
            error = self.expected_outputs[i] - test
            self.error += error.__abs__()
            print ' inputs', self.inputs[i]
            print ' Saida desejada: ', self.expected_outputs[i]
            print ' Saida encontrada: ', test
            print ' error: ', error
            print ' Pesos:', self.weights
            self.changeWeights(error, i)

    def changeWeights(self, error, numinput):
        if error != 0:
            plen = self.weights.__len__()
            for j in range(0, plen):
                self.weights[j] = self.weights[j] + self.alpha * error \
                    * self.inputs[numinput][j]
                print ' Pesos atualizados:', self.weights

    def answers(self, input):
        if input.__len__() != self.inputs[0].__len__():
            raise Runtimeerrorr('A input deve ter o mesmo tamanho das usadas no trainingmento'
                                )
            self.inputs.append(input)
            result= self.test(self.inputs.__len__() - 1)
            self.inputs.pop()
            return result

    def main():
        print 'Hello World'

    # certo

        inverseA0 = [
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]

    # errado

        inverseA1 = [
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]

    # certo

        inverseA2 = [
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]

    # certo

        inverseA3 = [
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]

    # errado

        inverseA4 = [
            1,
            1,
            1,
            1,
            1,
            1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            ]

    # errado

        inverseA5 = [
            1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            1,
            1,
            1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]

    # errado

        normalA0 = [
            1,
            -1,
            1,
            1,
            -1,
            -1,
            1,
            -1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            1,
            -1,
            1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]

    # certo

        normalA1 = [
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]

    # errado

        normalA2 = [
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]

    # errado

        normalA3 = [
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]

    # certo

        normalA4 = [
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]

    # certo

        normalA5 = [
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]
        testInverse = [
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]
        testA = [
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]
        testWrong = [
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            1,
            -1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            -1,
            1,
            -1,
            -1,
            1,
            -1,
            -1,
            -1,
            -1,
            -1,
            1,
            ]
        testWrong2 = [
            1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            1,
            -1,
            1,
            1,
            1,
            1,
            1,
            -1,
            1,
            1,
            -1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            1,
            1,
            -1,
            -1,
            1,
            1,
            ]
        inputs = [
            inverseA0,
            inverseA0,
            inverseA0,
            inverseA0,
            inverseA0,
            inverseA0,
            normalA0,
            normalA1,
            normalA2,
            normalA3,
            normalA4,
            normalA5,
            ]
        expected_outputs = [
            -1,
            0,
            -1,
            -1,
            0,
            0,
            0,
            1,
            0,
            0,
            1,
            1,
            ]
        
        neuron = Adaline()
        neuron.setInput(inputs)
        neuron.setExpectedOutputs(expected_outputs)
        neuron.learning()
        neuron.answers(testInverse)
        neuron.answers(testA)
        neuron.answers(testWrong)
        neurons.answers(testWrong2)

    if __name__ == '__main__':
        main()
