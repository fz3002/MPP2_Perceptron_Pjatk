import random

class Perceptron:

    def __init__(self, alpha, activatingResult) :
        self.alpha = alpha
        self.weights = [];
        self.currentResult = 0;
        self.activatingResult = activatingResult;

    def set_weights(self, numberOfAttributes):
        for i in range(numberOfAttributes):
            self.weights.append(random.randint(-5, 5)

    def Compute(self, vector):
        net = 0
        for i in range(len(vector)):
            net += (vector[i] * self.weights[i])
        net -= alpha
        if(net >= 0):
            return 1;
            
        return result

    def Learn(self, prevResult, goodResult):
        for weight in weights:
            weight += (goodResult - prevResult) * self.alpha

    
    
class Trainer:


class UI:
    def printUI():
        print("UI");