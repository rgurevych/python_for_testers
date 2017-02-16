Scenario Outline: Add new contact
  Given a contact list
  Given a new contact
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact


Scenario Outline: Delete random contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list with removed contact


Scenario Outline: Edit random contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact data containing <firstname> and <lastname>
  When I replace the data in selected contact
  Then the new contact list is equal to the old contact list with selected contact replaced by a new contact

  Examples:
  | firstname    | lastname     |
  | fname_edited | lname_edited |
