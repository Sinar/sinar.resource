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

class ICitedByMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ICitedBy(model.Schema):
    """
    """

    directives.widget('cited_by',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    cited_by = RelationList(
        title=u'Cited By',
        description=_(u'''
            Resources such as news article or publication that cites
            this item.
            '''),
        default=[],
        value_type=RelationChoice(
              source=CatalogSource(portal_type='Resource'),
        ),
        required=False,
    )

    # fieldset set the tabs on the edit form
    fieldset(
        'citation',
        label=_('Citations'),
        fields=[
            'cited_by',
        ],
    )


@implementer(ICitedBy)
@adapter(ICitedByMarker)
class CitedBy(object):
    def __init__(self, context):
        self.context = context

    @property
    def cited_by(self):
        if safe_hasattr(self.context, 'cited_by'):
            return self.context.cited_by
        return None

    @cited_by.setter
    def cited_by(self, value):
        self.context.cited_by = value
