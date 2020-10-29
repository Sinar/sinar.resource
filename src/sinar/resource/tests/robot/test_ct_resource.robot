# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.resource -t test_resource.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.resource.testing.SINAR_RESOURCE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/resource/tests/robot/test_resource.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Resource
  Given a logged-in site administrator
    and an add Resource form
   When I type 'My Resource' into the title field
    and I submit the form
   Then a Resource with the title 'My Resource' has been created

Scenario: As a site administrator I can view a Resource
  Given a logged-in site administrator
    and a Resource 'My Resource'
   When I go to the Resource view
   Then I can see the Resource title 'My Resource'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Resource form
  Go To  ${PLONE_URL}/++add++Resource

a Resource 'My Resource'
  Create content  type=Resource  id=my-resource  title=My Resource

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Resource view
  Go To  ${PLONE_URL}/my-resource
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Resource with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Resource title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
