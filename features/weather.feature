Feature: Current Weather API

  Background:
    Given the weather API is available

  @smoke
  Scenario: Get current weather for valid coordinates
    When I request the current weather for latitude 20.6767 and longitude -103.3475
    Then the response status code should be 200
    And the response should contain weather data

  @regression
  Scenario: Validate mandatory fields in the response
    When I request the current weather for latitude 20.6767 and longitude -103.3475
    Then the response should include "temperature" and "windspeed"
    And these fields should contain numeric values
    
  @regression
  Scenario: Request weather with invalid coordinates
    When I request the current weather for latitude 999 and longitude 999
    Then the response status code should be 400
    And the response body should contain an "Latitude must be in range" error message

  @regression
  Scenario Outline: Get current weather for different cities
    When I request the current weather for latitude <lat> and longitude <lon>
    Then the response status code should be 200
    And the response should contain weather data

    Examples:
        | city         | lat      | lon       |
        | Guadalajara  | 20.6767  | -103.3475 |
        | London       | 51.5074  | -0.1278   |
        | Tokyo        | 35.6762  | 139.6503  |

