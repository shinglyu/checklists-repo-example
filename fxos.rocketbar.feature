Feature: fxos.rocketbar

  Scenario Outline: fxos.rocketbar.search-provider
    When I search "<search term>" using <search provider>
    Then The search page of <search provider> that searches "<search term>" is shown correctly

    Examples:
      | search term | search provider |
      | star trek   | Yahoo           |
      | star wars   | Google          |
      | Dr. Who     | DuckDuckGo      |

  Scenario: fxos.rocketbar.launch
    When Tap the rocketbar 
    Then The rocket bar search window opens
