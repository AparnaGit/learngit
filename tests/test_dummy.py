from pyspark.sql import SparkSession
import unittest


class test_pyu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = (SparkSession
                     .builder
                     .master("local[2]")
                     .appName("dummy")
                     .getOrCreate())

    def test_samplefunc(self):
        df = self.spark.createDataFrame(data=[[1, 'a'], [2, 'b']],
                                        schema=['c1', 'c2'])
        self.assertEqual(df.count(), 2)

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

