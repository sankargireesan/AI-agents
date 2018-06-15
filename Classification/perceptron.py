# perceptron.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Perceptron implementation
import util
PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels);
        self.weights = weights;

    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """

        self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.

        # print trainingData[0]
        # trainingData[0]# {(7, 3): 0, (20, 25): 0, (16, 9): 1, (19, 4): 0, (17, 20): 1, (7, 25): 0, (22, 19): 0,
        # trainingData# [{(7, 3): 0, (20, 25): 0, (16, 9): 1, (19, 4): 0, (17, 20): 1, (7, 25): 0, (22, 19): 0,

        # print len(trainingData),100
        # print self.features[0],(7,3)
        # print trainingData[0][self.features[0]],0
        # print validationData
        # print trainingLabels
        # print validationLabels
        # print self.legalLabels
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # print trainingData[1]
        # print self.weights
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            for i in range(len(trainingData)):
                # print i
                "*** YOUR CODE HERE ***"
                # util.raiseNotDefined()
                vectors = util.Counter()
                # feature = self.features[i]
                # print trainingData[i]
                # print trainingLabels[i]
                for l in self.legalLabels:
                    vectors[l] = self.weights[l]*trainingData[i]

                if vectors.argMax() != trainingLabels[i]:
                    self.weights[vectors.argMax()] -= trainingData[i]
                    self.weights[trainingLabels[i]] += trainingData[i]
        #
        # print self.weights[0]
        # print self.weights[1]
                # elif vectors.argMax() < trainingLabels[i]::
                # # print self.weights[i]
                # # break


    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


    def findHighWeightFeatures(self, label):
        """
        Returns a list of the 100 features with the greatest weight for some label
        """
        featuresWeights = []

        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        return featuresWeights
