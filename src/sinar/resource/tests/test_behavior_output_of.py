# -*- coding: utf-8 -*-
from sinar.resource.behaviors.output_of import IOutputOfMarker
from sinar.resource.testing import SINAR_RESOURCE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class OutputOfIntegrationTest(unittest.TestCase):

    layer = SINAR_RESOURCE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_output_of(self):
        behavior = getUtility(IBehavior, 'sinar.resource.output_of')
        self.assertEqual(
            behavior.marker,
            IOutputOfMarker,
        )
