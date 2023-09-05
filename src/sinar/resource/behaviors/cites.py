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
                                 'Activity (Event)',
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



@implementer(ICites)
@adapter(ICitesMarker)
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
