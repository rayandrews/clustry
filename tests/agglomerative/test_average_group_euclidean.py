import unittest

from numpy import ndarray, testing

from ..context import iris_data, iris_target, check_model_exist, purity_score, print_in_test
from cleverly.agglomerative.Agglomerative import Agglomerative


class AgglomerativeAverageGroupEuclideanTestSuite(unittest.TestCase):
    """Agglomerative Average-Group with Euclidean Distance test cases."""

    @classmethod
    def setUpClass(self):
        self.filename = './tests/models/agglo-avg-group_euclidean.model'
        self.agg = Agglomerative(
            linkage="average-group", affinity="euclidean", n_clusters=3)
        self.agg.fit_predict(iris_data)

    def test_agglo_return_labels_with_type_numpy_array(self):
        self.assertIsInstance(self.agg.labels_, ndarray)
        print_in_test("Agglomerative (Distance=Euclidean, Linkage=Average-group): %f" %
                      purity_score(iris_target, self.agg.labels_))


if __name__ == '__main__':
    unittest.main()
