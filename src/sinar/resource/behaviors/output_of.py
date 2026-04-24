# -*- coding: utf-8 -*-

from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model

from Products.CMFPlone.utils import safe_hasattr
from sinar.resource import _
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.component import adapter
from zope.interface import implementer, Interface, provider


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
