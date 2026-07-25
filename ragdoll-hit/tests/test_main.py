import unittest
from unittest.mock import patch

import pygame

import main


class FontFallbackTests(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()

    def tearDown(self) -> None:
        pygame.quit()

    def test_make_font_falls_back_to_default_font_when_sysfont_raises(self) -> None:
        with patch("pygame.font.SysFont", side_effect=TypeError("simulated font issue")):
            font = main._make_font("Arial", 24, bold=True)

        self.assertIsInstance(font, pygame.font.Font)


if __name__ == "__main__":
    unittest.main()
