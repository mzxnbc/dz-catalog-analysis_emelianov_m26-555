import unittest

import catalog_analysis as app


class CatalogAnalysisTests(unittest.TestCase):
    def test_rating_tier_boundaries(self):
        self.assertEqual(app.rating_tier(9), "шедевр")
        self.assertEqual(app.rating_tier(7), "хорошо")
        self.assertEqual(app.rating_tier(5), "средне")
        self.assertEqual(app.rating_tier(4.9), "слабо")

    def test_decade_label_boundaries(self):
        self.assertEqual(app.decade_label(2021), "новые")
        self.assertEqual(app.decade_label(2020), "недавние")
        self.assertEqual(app.decade_label(2015), "недавние")
        self.assertEqual(app.decade_label(2014), "старые")

    def test_title_helpers(self):
        self.assertEqual(app.normalize_title("silent hours"), "Silent Hours")
        self.assertEqual(app.make_slug("Silent Hours"), "silent-hours")

    def test_top_n_returns_tuples(self):
        result = app.top_n_by_rating(app.movies, 3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(item, tuple) for item in result))
        self.assertEqual(result[0][0], "The Quiet Algorithm")

    def test_genres_and_common_actors(self):
        self.assertIn("mystery", app.all_genres(app.movies))
        self.assertEqual(
            app.common_actors(app.movies[0], app.movies[3]),
            {"O. Isaac"},
        )

    def test_high_rated_is_generator(self):
        result = app.iter_high_rated(app.movies)
        self.assertTrue(hasattr(result, "__next__"))
        self.assertEqual(next(result)["title"], "The Dune Chronicles")


if __name__ == "__main__":
    unittest.main()
