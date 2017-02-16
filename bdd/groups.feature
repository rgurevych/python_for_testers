Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old group list with the added group

  Examples:
  | name    | header    | footer    |
  | name444 | header444 | footer444 |
  | name555 | header555 | footer555 |

Scenario Outline: Delete group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old group list with removed group
