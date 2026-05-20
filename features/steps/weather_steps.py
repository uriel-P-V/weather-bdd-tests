from behave import given, when, then
import requests

API_BASE_URL = "https://api.open-meteo.com/v1/forecast"

@given("the weather API is available")
def step_given_api_available(context):
    params = {
        "latitude": 20.6767,
        "longitude": -103.3475,
        "current_weather": "true"
    }

    context.api_available = requests.get(
        API_BASE_URL,
        params=params
    )

    assert context.api_available.status_code == 200, (
        f"Weather API is unavailable. "
        f"Status code: {context.api_available.status_code}"
    )

@when("I request the current weather for latitude {lat} and longitude {lon}")
def step_when_request_weather(context, lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    context.response = requests.get(API_BASE_URL, params=params)


@then("the response status code should be {expected_status:d}")
def step_then_status_code(context, expected_status):
    assert context.response.status_code == expected_status, (
        f"Expected {expected_status}, "
        f"but got {context.response.status_code}"
    )


@then("the response should contain weather data")
def step_then_contains_weather_data(context):
    response_json = context.response.json()

    assert "current_weather" in response_json, (
        "Response does not contain current_weather data"
    )


# Scenario 2
@then('the response should include "{field1}" and "{field2}"')
def step_then_validate_fields_exist(context, field1, field2):
    response_json = context.response.json()
    weather_data = response_json["current_weather"]

    assert field1 in weather_data, f"{field1} was not found"
    assert field2 in weather_data, f"{field2} was not found"


@then("these fields should contain numeric values")
def step_then_fields_are_numeric(context):
    response_json = context.response.json()
    weather_data = response_json["current_weather"]

    assert isinstance(weather_data["temperature"], (int, float)), (
        "temperature is not numeric"
    )

    assert isinstance(weather_data["windspeed"], (int, float)), (
        "windspeed is not numeric"
    )


# Scenario 3
@then('the response body should contain an "{error_message}" error message')
def step_then_contains_error_message(context, error_message):
    response_json = context.response.json()

    actual_error_message = response_json["reason"]

    assert error_message in actual_error_message, (
        f'Expected error message "{error_message}" was not found'
    )