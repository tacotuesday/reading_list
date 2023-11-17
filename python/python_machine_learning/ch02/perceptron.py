import numpy as np


class Perceptron(object):
    """
    Perceptron classifier

    Parameters
    ------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.
    random_state : int
        Random number generator seed for random weight initialization.

    Attributes
    ------------
    w_ : 1d-array
        Weights after fitting.
    errors_ : list
        Number of misclassifications in every epoch.
    """

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        # Learning rate
        self.eta = eta
        # Number of passes over the training dataset
        self.n_iter = n_iter
        # Random number generator seed for random weight initialization
        self.random_state = random_state

    def fit(self, X, y):
        """
        Fit training data by looping over all individual examples in the training dataset and updates the weights according to the
        perceptron learning rule.

        Parameters
        ------------
        X : {array-like}, shape = [n_examples, n_features]
            Training vectors, where n_examples is the number of examples and n_features is the number of features.
        y : {array-like}, shape = [n_examples]
            Target values.

        Returns
        ------------
        self : object
        """

        rgen = np.random.RandomState(
            self.random_state
        )  # Creates a RandomState instance with a seed specified by self.random_state
        self.w_ = rgen.normal(
            loc=0.0, scale=0.01, size=1 + X.shape[1]
        )  # Initialize weights to a vector of zeros with length 1 + number of features.
        # We don't initialize the weights to zero because the learning rate only has an effect on the classification outcome if the weights are initialized to non-zero values.
        # `normal` creates small random numbers in a normal distribution with standard deviation 0.01. The standard deviation was arbitrary and only chosen to avoid initializing the weights to 0.

        self.errors_ = (
            []
        )  # Initialize a list to store the number of misclassifications in every epoch

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (
                    target - self.predict(xi)
                )  # Calculate the update based on the difference between the true class label and the predicted class label
                self.w_[1:] += update * xi  # Update the weights w1 to wm
                self.w_[0] += update  # Update the weight w0, which is the bias unit
                errors += int(
                    update != 0.0
                )  # Count the number of misclassifications by checking if the update is not equal to zero and converting the Boolean result to an integer
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input by taking the dot product of X and w1 to wm, and adding w0 to the result."""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Return the class label after the unit step. Return 1 if the net input is greater than or equal to zero; otherwise, return -1."""
        return np.where(self.net_input(X) >= 0, 1, -1)
