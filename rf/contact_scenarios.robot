*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  fname123  lname123
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append to list  ${old_list}  ${contact}
    Contact lists should be equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Contact List
    ${contact_for_editing}=  Random contact  ${old_list}
    ${contact_data}=  Create contact data  Updated_first_name  Updated_last_name  ${contact_for_editing}
    Edit Contact  ${contact_data}
    ${new_list}=  Get Contact List
    Remove values from list  ${old_list}  ${contact_for_editing}
    Append to list  ${old_list}  ${contact_data}
    Contact lists should be equal  ${new_list}  ${old_list}


Delete contact
    ${old_list}=  Get Contact List
    ${contact}=  Random contact  ${old_list}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove values from list  ${old_list}  ${contact}
    Contact lists should be equal  ${new_list}  ${old_list}