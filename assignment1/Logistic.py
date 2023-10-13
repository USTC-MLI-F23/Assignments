import numpy as np

class LogisticRegression:

    def __init__(self, penalty="l2", gamma=0, fit_intercept=True):
        """
        Parameters:
        - penalty: str, "l1" or "l2". Determines the regularization to be used.
        - gamma: float, regularization coefficient. Used in conjunction with 'penalty'.
        - fit_intercept: bool, whether to add an intercept (bias) term.
        """
        err_msg = "penalty must be 'l1' or 'l2', but got: {}".format(penalty)
        assert penalty in ["l2", "l1"], err_msg
        self.penalty = penalty
        self.gamma = gamma
        self.fit_intercept = fit_intercept
        self.coef_ = None

    def sigmoid(self, x):
        """The logistic sigmoid function"""
        ################################################################################
        # TODO:                                                                        #
        # Task1: Implement the sigmoid function.
        ################################################################################
        
        pass  # Remove this line when you write the code
        
        ################################################################################
        #                                 END OF YOUR CODE                             #
        ################################################################################

    def fit(self, X, y, lr=0.01, tol=1e-7, max_iter=1e7):
        """
        Fit the regression coefficients via gradient descent or other methods 
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features), input data.
        - y: numpy array of shape (n_samples,), target data.
        - lr: float, learning rate for gradient descent.
        - tol: float, tolerance to decide convergence of gradient descent.
        - max_iter: int, maximum number of iterations for gradient descent.
        """
        # If fit_intercept is True, add an intercept column
        if self.fit_intercept:
            X = np.c_[np.ones(X.shape[0]), X]

        # Initialize coefficients
        self.coef_ = np.zeros(X.shape[1])
        
        ################################################################################
        # TODO:                                                                        #
        # Task2: Implement gradient descent with optional regularization.
        # 1. Compute the gradient 
        # 2. Apply the update rule
        # 3. Check for convergence
        ################################################################################

        pass  # Remove this line when you write the code
        
        ################################################################################
        #                                 END OF YOUR CODE                             #
        ################################################################################

    def predict(self, X):
        """
        Use the trained model to generate prediction probabilities on a new
        collection of data points.
        
        Parameters:
        - X: numpy array of shape (n_samples, n_features), input data.
        
        Returns:
        - probs: numpy array of shape (n_samples,), prediction probabilities.
        """
        if self.fit_intercept:
            X = np.c_[np.ones(X.shape[0]), X]

        # Compute the linear combination of inputs and weights
        linear_output = np.dot(X, self.coef_)
        
        ################################################################################
        # TODO:                                                                        #
        # Task3: Apply the sigmoid function to compute prediction probabilities.
        ################################################################################

        pass  # Remove this line when you write the code
        
        ################################################################################
        #                                 END OF YOUR CODE                             #
        ################################################################################
