import csv
import random

class Perceptron:

    def __init__(self, alpha, activatingResult, numberOfAttributes) :
        self.alpha = alpha
        self.weights = []
        self.activatingResult = activatingResult
        self.set_weights(numberOfAttributes)
        

    def set_weights(self, numberOfAttributes):
        for i in range(numberOfAttributes + 1):
            self.weights.append(random.randint(-5, 5))

    def compute(self, vector):
        vector.append(-1)
        net = 0
        for i in range(len(vector)):
            net += (float(vector[i]) * self.weights[i])
        if net >= 0:
            return 1
        return 0

    def learn(self, prevResult, goodResult, vector):
        vector.append(-1)
        
        for i in range(len(self.weights)):        
            self.weights[i] += (goodResult - prevResult) * self.alpha * float(vector[i])
            

    
    
class Trainer:
    
    def __init__(self, perceptron, trainSetFname):
        self.perceptron = perceptron
        self.trainSetFname = trainSetFname
        self.trainSet = readFile(self.trainSetFname)
        random.shuffle(self.trainSet)
        self.namesOfClasses = self.setNamesOfClasses()

    def setNamesOfClasses(self):
        listOfClasses = [self.perceptron.activatingResult]
        
        for line in self.trainSet:
            if line[-1] not in listOfClasses:
                listOfClasses.append(line[-1])
                
        listOfClasses[0], listOfClasses[1] = listOfClasses[1], listOfClasses[0]
        
        return listOfClasses

    def train(self, number_of_trainings):
        for i in range(number_of_trainings):
            for line in self.trainSet:
                result = self.perceptron.compute(line[:-1])
                self.perceptron.learn(result, self.namesOfClasses.index(line[-1]), line[:-1])

class UI:

    def __init__(self):
        self.testSet = readFile("test_set.csv")
        random.shuffle(self.testSet)
        self.perceptron = Perceptron(1, "Iris-setosa", len(self.testSet[0])-1)
        self.trainer = Trainer(self.perceptron, "train_set.csv")
        self.classes = self.trainer.namesOfClasses

    def printUI(self):
        self.trainer.train(1)
        self.test()
    
    def test(self):
        numberOfGoodGuesses = 0;
        for i in range(len(self.testSet)):
            acitavtion = self.perceptron.compute(self.testSet[i][:-1])
            result = self.classes[acitavtion]
            if result == self.testSet[i][-1]:
                numberOfGoodGuesses += 1 
            print(i + 1, "| Set: ", self.testSet[i][-1], " Peceptron: ", result)
        print("accuracy: ", numberOfGoodGuesses/len(self.testSet))
        
def readFile(file_name):
    listVec = []
    with open(file_name, newline='') as f:
        lines = csv.reader(f, delimiter=";")
        for row in lines:
            listVec.append(row)
    f.close()
    return listVec

ui = UI()
UI.printUI(ui)