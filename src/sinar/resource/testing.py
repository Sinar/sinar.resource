# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.resource


class SinarResourceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.resource)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.resource:default')


SINAR_RESOURCE_FIXTURE = SinarResourceLayer()


SINAR_RESOURCE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_RESOURCE_FIXTURE,),
    name='SinarResourceLayer:IntegrationTesting',
)


SINAR_RESOURCE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_RESOURCE_FIXTURE,),
    name='SinarResourceLayer:FunctionalTesting',
)


SINAR_RESOURCE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_RESOURCE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarResourceLayer:AcceptanceTesting',
)
