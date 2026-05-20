Feature: Current Weather API

  Background:
    Given the weather API is available

  Scenario: Get current weather for valid coordinates
    When I request the current weather for latitude 20.6767 and longitude -103.3475
    Then the response status code should be 200
    And the response should contain weather data

  Scenario: Validate mandatory fields in the response
    When I request the current weather for latitude 20.6767 and longitude -103.3475
    Then the response should include "temperature" and "windspeed"
    And these fields should contain numeric values

    Scenario: Request weather with invalid coordinates
    When I request the current weather for latitude 999 and longitude 999
    Then the response status code should be 400
    And the response body should contain an "Latitude must be in range" error message

