import csv
import random

class Perceptron:

    def __init__(self, alpha, activatingResult) :
        self.alpha = alpha
        self.weights = [];
        self.currentResult = 0;
        self.activatingResult = activatingResult;

    def set_weights(self, numberOfAttributes):
        for i in range(numberOfAttributes):
            self.weights.append(random.randint(-5, 5))

    def compute(self, vector):
        net = 0
        for i in range(len(vector)):
            net += (vector[i] * self.weights[i])
        net -= self.alpha
        if(net >= 0):
            return 1;
            
        return result

    def learn(self, prevResult, goodResult):
        for weight in self.weights:
            weight += (goodResult - prevResult) * self.alpha

    
    
class Trainer:
    def __init__(self, file_name, test_set_size):
        self.file_name = file_name
        
    def read_file(file_name):
        list = []
        with open(file_name, newline='') as f:
            lines = csv.reader(f, delimiter=";")
        for row in lines:
            list.append(row)
        f.close()
    
    def create_sets(trains):
        test_set_ids = []
        for ()


class UI:
    def printUI():
        print("UI");