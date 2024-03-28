import csv
import random


class Perceptron:
    """ A class to represent a Perceptron
    
        ...
       
        Attributes
        ----------
        alpha : float
            learning constant
        weights : list
            vector (as list) of weights
        activating_result : str
            name of the class that should activate perceptron
        
        Methods
        -------
        __set_weights(number_of_attributes):
            Sets random weights
        compute(vector) : 
            Computes net value and returns verdict for given vector
        learn(good_result, vector) : 
            Modifies weights and threshold using delta funcition

    """

    def __init__(self, alpha, activating_result, number_of_attributes) :
        """Contstructs all necessary attributes
        
            Args: 
                alpha(float): learning constant
                activating_result(str) : name of the class that should activate perceptron
                number_of_attributes(int): number of entries of perceptron
        """
        
        self.alpha = alpha
        self.weights = []
        self.activating_result = activating_result
        self.__set_weights(number_of_attributes)
        
    def __set_weights(self, number_of_attributes):
        """Sets begining weights as random generated numbers

        Args:
            number_of_attributes (int): number of weights to generate (without threshold)
        """        
        
        for i in range(number_of_attributes + 1):
            self.weights.append(random.randint(-5, 5))

    def compute(self, vector):
        """Computes output of perceptron

        Args:
            vector (list): vector to compute output from

        Returns:
            int: 1 activated or 0 if not
        """        
        
        vector.append(-1)
        net = 0
        
        for i in range(len(vector)):
            net += (float(vector[i]) * self.weights[i])
        if net >= 0:
            return 1
        
        return 0

    def learn(self, good_result, vector):
        """Function that teaches percpetron by changing weights and threshold using delta function

        Args:
            good_result (int): 0 or 1 depanding on the result given in train_set in Trainer
            vector (list): vector to compute and learn on
        """        
        prev_result = self.compute(vector)
        
        vector.append(-1)

        for i in range(len(self.weights)):
            
            self.weights[i] += ((good_result - prev_result)
                                * self.alpha 
                                * float(vector[i]))
            

class Trainer:
    """A class to train the perceptron
    
        ...
       
        Attributes
        ----------
        percpeptron : Perceptron
            perceptron to train
        train_set_fname : str
            name of train_set file
        train_set : list
            list of vector to train on
        names_of_classes : list
            list of names of classes in dataset
        
        Methods
        -------
        __set_names_of_classes() :
            Finds and sets names of classes from dataset in correct order
        train(number_of_trainings) :
            Method to train perceptron on given train_set
        
    """    
    
    def __init__(self, perceptron, train_set_fname): 
        """Contructor of Trainer class

        Args:
            perceptron (Perceptron): perceptron to train passed from ui
            train_set_fname (str): name of file containing train_set
        """        
        
        self.perceptron = perceptron
        self.train_set_fname = train_set_fname
        self.train_set = read_file(self.train_set_fname)
        self.names_of_classes = self.__set_names_of_classes()
        
        random.shuffle(self.train_set)

    def __set_names_of_classes(self):
        """Sets list of names of classes (index 0 nonactivating, 1 - activating)

        Returns:
            list: list of names of classes
        """        
        
        classes = [self.perceptron.activating_result]
        
        for line in self.train_set:
            if line[-1] not in classes:
                classes.append(line[-1])
                
        classes[0], classes[1] = classes[1], classes[0]
        
        return classes

    def train(self, number_of_trainings):
        """Method that trains perceptron

        Args:
            number_of_trainings (int): number of passes perceptron has to do through train_set
        """        
        
        for i in range(number_of_trainings):
            for line in self.train_set:
                class_index = self.names_of_classes.index(line[-1])
                self.perceptron.learn(class_index, line[:-1])


class UI:
    """A class containing ui elements and invoking them
    
        ...
       
        Attributes
        ----------
        test_set : list
            List of vectors used to test perceptron.
        number_of_attributes : int
            Number of attributes (coords) for vectors.
        perceptron : Perceptron
            Perceptron to test.
        trainer : Trainer
            Trainer that traines perceptron.
        classes : list
            List of classes in dataset (passed from trainer).
        
        Methods
        -------
        print_ui() :
            Main ui class, responsible for printing ui.
        test() :
            Method to test perceptron on given test_set.
        user_vector() : 
            Method that lets user test perceptron on vectors given by them
    """
    
    def __init__(self):
        """Constructor of ui class
        """
                
        self.test_set = read_file("test_set.csv")
        random.shuffle(self.test_set)
        
        self.number_of_attributes = len(self.test_set[0])-1
        self.perceptron = Perceptron(1.0, 
                                     "Iris-setosa", 
                                     self.number_of_attributes)
        self.trainer = Trainer(self.perceptron, "train_set.csv")
        self.classes = self.trainer.names_of_classes

    def print_ui(self):
        """Invokes UI methods.
        """        
        
        self.trainer.train(1)
        self.test()
        self.user_vector
    
    def test(self):
        """Method that tests accuracy of percpetron.
        """        
        
        number_of_good_guesses = 0;
        for i in range(len(self.test_set)):
            acitavtion = self.perceptron.compute(self.test_set[i][:-1])
            result = self.classes[acitavtion]
            if result == self.test_set[i][-1]:
                number_of_good_guesses += 1 
            print(i + 1, 
                  "| Set: ", self.test_set[i][-1], 
                  " Peceptron: ", result)
        print("accuracy: ", number_of_good_guesses/len(self.test_set))
        
    def user_vector(self):
        """Methods that lets user test perceptron on custom vectors (not in dataset).
        """
                
        while True:
            input_vec = []             
            for i in range(len(self.test_set[0])-1):
                input_vec.append(float(input("Podaj współrzędną: ")))
            print(self.perceptron.compute(input_vec))
            
        
def read_file(file_name):
    """This is a function that reads CSV file and returns list of lines.

    Args:
        file_name (str): File name

    Returns:
        list : List of lines
    """
    list_vec = []
    with open(file_name, newline='') as f:
        lines = csv.reader(f, delimiter=";")
        for row in lines:
            list_vec.append(row)
    f.close()
    return list_vec


ui = UI()
UI.print_ui(ui)