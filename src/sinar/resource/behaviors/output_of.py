# -*- coding: utf-8 -*-

from sinar.resource import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.supermodel.directives import fieldset
from plone.autoform import directives
from plone.app.vocabularies.catalog import CatalogSource


class IOutputOfMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IOutputOf(model.Schema):
    """
    """

    directives.widget('output_of',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    output_of = RelationList(
        title='Output Of',
        description=_('''
                Project or Activity that this Resource is an output of
                        '''),
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(portal_type=[
                                 'Project',
                                 'Activity',
                                 'ProjectActivity',
                                 ]
                                 ),
        ),
        required=False,
    )


@implementer(IOutputOf)
@adapter(IOutputOfMarker)
class OutputOf(object):
    def __init__(self, context):
        self.context = context

    @property
    def output_of(self):
        if safe_hasattr(self.context, 'output_of'):
            return self.context.output_of
        return None

    @output_of.setter
    def output_of(self, value):
        self.context.output_of = value
