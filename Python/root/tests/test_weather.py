import unittest

from core.weather import get_weather_result
from core.weather import WeatherType
from core.weather import ALL_JABOS_AVAILABLE, CARPET_BOMBING_UNAVAILABLE

# =========================================================
# TEST WEATHER
# =========================================================

class TestWeather(unittest.TestCase):

    def test_weather_roll_1(self):
        result = get_weather_result(1)

        self.assertEqual(result.weather_type, WeatherType.OVERCAST)
        self.assertEqual(result.available_jabos, 0)
        self.assertEqual(result.resource_drm, 1)
        self.assertEqual(result.carpet_bombing_drm, CARPET_BOMBING_UNAVAILABLE)

    def test_weather_roll_2(self):
        result = get_weather_result(2)

        self.assertEqual(result.weather_type, WeatherType.PARTLY_CLEAR)
        self.assertEqual(result.available_jabos, 1)
        self.assertEqual(result.resource_drm, 0)
        self.assertEqual(result.carpet_bombing_drm, 1)

    def test_weather_roll_3(self):
        result = get_weather_result(3)

        self.assertEqual(result.weather_type, WeatherType.PARTLY_CLEAR)
        self.assertEqual(result.available_jabos, 1)
        self.assertEqual(result.resource_drm, 0)
        self.assertEqual(result.carpet_bombing_drm, 1)

    def test_weather_roll_4(self):
        result = get_weather_result(4)

        self.assertEqual(result.weather_type, WeatherType.CLEAR)
        self.assertEqual(result.available_jabos,ALL_JABOS_AVAILABLE)
        self.assertEqual(result.resource_drm, 0)
        self.assertEqual(result.carpet_bombing_drm, 0)

    def test_weather_roll_5(self):
        result = get_weather_result(5)

        self.assertEqual(result.weather_type, WeatherType.CLEAR)
        self.assertEqual(result.available_jabos, ALL_JABOS_AVAILABLE)
        self.assertEqual(result.resource_drm, 0)
        self.assertEqual(result.carpet_bombing_drm, 0)

    def test_weather_roll_6(self):
        result = get_weather_result(6)

        self.assertEqual(result.weather_type, WeatherType.CLEAR)
        self.assertEqual(result.available_jabos, ALL_JABOS_AVAILABLE)
        self.assertEqual(result.resource_drm, 0)
        self.assertEqual(result.carpet_bombing_drm, 0)