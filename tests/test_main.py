from unittest import TestCase

from pazgas_power import PazGasPowerApi  # noqa: F401


class MainTest(TestCase):
    def test_main_hello(self):
        self.assertEqual("Hello", "Hello")
