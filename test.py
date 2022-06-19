import unittest

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that
from apache_beam.testing.util import equal_to
import random

class testPipeline(unittest.TestCase):
    def test_random(self):
        # Create a random floating figure with normal distribution
        sample_weight = random.gauss(10, 3)
        
        # Assert on the result.
        self.assertGreater(sample_weight, 0, 'Sample weight larger than 0')

    def test_beam(self):
        # Our static input data, which will make up the initial PCollection.
        WORDS = ["hi", "hello", "", "hi"]

        # Create a test pipeline
        with TestPipeline() as p:

            # Create an input PCollection
            input = p | beam.Create(WORDS)

            # Apply the Count transform under test.
            output = input | beam.combiners.Count.PerElement()

            # Assert on the results.
            assert_that(
                output,
                equal_to([
                    ("hi", 2),
                    ("", 1),
                    ("hello", 1)
                ])
            )

if __name__ == '__main__':
    unittest.main()