from unittest.mock import patch, MagicMock

MOCK_WEATHER_RESPONSE = {
    "current_weather": {
        "temperature": 25.0,
        "windspeed": 10.0,
        "winddirection": 180,
        "weathercode": 1,
        "is_day": 1
    }
}

MOCK_ERROR_RESPONSE = {
    "error": True,
    "reason": "Latitude must be in range of -90 to 90°. Given: 999.0."
}


def mock_response(url, params=None, **kwargs):
    lat = float(params.get("latitude", 0))

    if lat == 999:
        mock = MagicMock()
        mock.status_code = 400
        mock.json.return_value = MOCK_ERROR_RESPONSE
        return mock

    else:
        mock = MagicMock()
        mock.status_code = 200
        mock.json.return_value = MOCK_WEATHER_RESPONSE
        return mock


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

    if "regression" in scenario.tags:
  
        context.mock_get = patch(
            "requests.get",
            side_effect=mock_response
        )

  
        context.mock_get.start()


def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name} - Status: {scenario.status}")

    if "regression" in scenario.tags:
  
        context.mock_get.stop()