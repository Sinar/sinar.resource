# -*- coding: utf-8 -*-
from sinar.resource.content.resource import IResource  # NOQA E501
from sinar.resource.testing import SINAR_RESOURCE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ResourceIntegrationTest(unittest.TestCase):

    layer = SINAR_RESOURCE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_resource_schema(self):
        fti = queryUtility(IDexterityFTI, name='Resource')
        schema = fti.lookupSchema()
        self.assertEqual(IResource, schema)

    def test_ct_resource_fti(self):
        fti = queryUtility(IDexterityFTI, name='Resource')
        self.assertTrue(fti)

    def test_ct_resource_factory(self):
        fti = queryUtility(IDexterityFTI, name='Resource')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IResource.providedBy(obj),
            u'IResource not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_resource_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Resource',
            id='resource',
        )

        self.assertTrue(
            IResource.providedBy(obj),
            u'IResource not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('resource', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('resource', parent.objectIds())

    def test_ct_resource_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Resource')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_resource_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Resource')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'resource_id',
            title='Resource container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
