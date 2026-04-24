# -*- coding: utf-8 -*-

from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from sinar.resource import _
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.interface import Interface, provider


class ICitesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ICites(model.Schema):
    """
    """

    directives.widget('cites',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    cites = RelationList(
        title='Cites',
        description=_('''
                Item that this Resource cites
                        '''),
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(portal_type=[
                                 'Project',
                                 'Activity',
                                 'Resource',
                                 ]
                                 ),
        ),
        required=False,
    )

    # fieldset set the tabs on the edit form
    fieldset(
        'citation',
        label=_('Citations'),
        fields=[
            'cites',
        ],
    )


class Cites(object):
    def __init__(self, context):
        self.context = context

    @property
    def cites(self):
        if safe_hasattr(self.context, 'cites'):
            return self.context.cites
        return None

    @cites.setter
    def cites(self, value):
        self.context.cites = value
