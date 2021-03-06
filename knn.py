import numpy as np


# TODO: ask about code style here
# noinspection PyPep8Naming
class kNN:

    def __init__(self, n_neighbors, metric='cosine'):
        self.n_neighbors = n_neighbors
        self._metric = metric

    def __str__(self):
        return 'kNN(n_neighbors=' + str(self.n_neighbors) + ')'

    def fit(self, X_train, y_train):   # no math for knn, since do not need to be learned
        self._X_train = X_train
        self._y_train = y_train

    def predict(self, x_test):
        predicts = np.zeros([len(x_test)], dtype=int)
        for n in range(len(x_test)):
            predicts[n] = self._point_predict(x_test[n])
        return predicts

    @staticmethod
    def _edistance(a_point, b_point):  # Euclidean distance, static method
        return np.linalg.norm(a_point - b_point)

    @staticmethod
    def _cosdistance(a_point, b_point):
        return 1 - np.dot(a_point, b_point) / (np.linalg.norm(a_point) * np.linalg.norm(b_point))

    @staticmethod
    def _chebdistance(a_point, b_point):
        return np.abs(a_point - b_point).max()
        # return np.linalg.norm(a_point-b_point, ord=np.inf)

    @staticmethod
    def _mandistance(a_point, b_point):
        return np.sum(np.abs(a_point - b_point))
        # return np.linalg.norm(a_point - b_point,ord=1)

    @staticmethod
    def _onepoint(x_testpoint, X_train, metric):

        dict = {
            'cosine': kNN._cosdistance,
            'chebyshev': kNN._chebdistance,
            'euclidean': kNN._edistance,
            'manhattan': kNN._mandistance,
        }

        dists = np.zeros([len(X_train)])
        for n in range(len(X_train)):
            dists[n] = dict[metric](x_testpoint, X_train[n])
        return dists.argsort()  # points indexes of sorted distances

    def _point_predict(self, x_testpoint):  # return which feature, when they are equal? randome?
        order = kNN._onepoint(x_testpoint, self._X_train, self._metric)[0:self.n_neighbors]  # first n neigbours fromm all distances
        nearest_k_y = self._y_train[order]
        return np.argmax(np.bincount(nearest_k_y))  # 1 1 0 0 3 returns 0

#bc = np.bincount(nearest_k_y)
#prediction = np.argwhere(bc == np.amax(bc))

#if len(prediction) != 1:
#    prediction = prediction[np.random.randint(0,lp)]

#Am Ende von der PredictFunction
