from pyspark.sql import SparkSession
from pyspark.testing.utils import  ReusedPySparkTestCase


class DummySparkTest(ReusedPySparkTestCase):
    def setUp(self):
        self.spark = SparkSession(self.sc)

    def test_samplefunc(self):
        df = self.spark.createDataFrame(data=[[1, 'a'], [2, 'b']],
                                        schema=['c1', 'c2'])
        self.assertEqual(df.count(), 1)

    def tearDown(self):
        self.spark.stop()



if __name__ == "__main__":
    import unittest

    unittest.main()