import unittest
import os
from PIL import Image
from optimizer import image_optimizer, ImageOptimizerError

class TestImageOptimizer(unittest.TestCase):

    def setUp(self):

        self.test_image = "test_image.png"
        self.output_image = "output_image.png"
        self.invalid_file = "invalid_file.txt"

        # Fake image for testing purposes
        image = Image.new("RGB", (2, 2), color="red")
        image.save(self.test_image)

        with open(self.invalid_file, "w") as f:
            f.write("This is not an image file.")

    def tearDown(self):
        if os.path.exists(self.test_image):
            os.remove(self.test_image)
        if os.path.exists(self.output_image):
            os.remove(self.output_image)
        if os.path.exists(self.invalid_file):
            os.remove(self.invalid_file)

    def test_valid_image(self):
        try:
            image_optimizer(self.test_image, self.output_image, verbose=False)
            self.assertTrue(os.path.exists(self.output_image))
        except Exception as e:
            self.fail(f"image_optimizer raised an exception unexpectedly: {e}")

    def test_image_not_found(self):
        with self.assertRaises(ImageOptimizerError):
            image_optimizer("non_existent_image.png", self.output_image)

    def test_invalid_image(self):
        with self.assertRaises(ImageOptimizerError):
            image_optimizer(self.invalid_file, self.output_image)

if __name__ == "__main__":
    unittest.main()
