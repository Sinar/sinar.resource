# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from sinar.resource.testing import (
    SINAR_RESOURCE_FUNCTIONAL_TESTING,
    SINAR_RESOURCE_INTEGRATION_TESTING,
)
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = SINAR_RESOURCE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_resource_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='resource-view'
        )
        self.assertTrue(view.__name__ == 'resource-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in resource-view'
        # )

    def test_resource_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='resource-view'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = SINAR_RESOURCE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
