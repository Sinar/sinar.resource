# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from sinar.resource import _
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IResourceTypeMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IResourceType(model.Schema):
    """
    """

    directives.widget(resource_type=SelectFieldWidget)
    resource_type = schema.Choice(
        title=_(u'Resource Type'),
        description=_(u'''
        
        '''),

        required=False,
        vocabulary='sinar.resource.ResourceType',
    )


@implementer(IResourceType)
@adapter(IResourceTypeMarker)
class ResourceType(object):
    def __init__(self, context):
        self.context = context

    @property
    def resource_type(self):
        if safe_hasattr(self.context, 'resource_type'):
            return self.context.resource_type
        return None

    @resource_type.setter
    def resource_type(self, value):
        self.context.resource_type = value
