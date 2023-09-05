# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from collective.relationhelpers import api as api_relations
from plone import api
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class CitedBy(ViewletBase):

    def resource_type_title(self,value):

        factory = getUtility(IVocabularyFactory,
                             'sinar.resource.ResourceType')

        vocabulary = factory(self)
        term = vocabulary.getTerm(value)

        return term.title

    def cited_by(self):
        """Get objects that link to this item, sort by effective date
           reversed.
        """
        citations = api_relations.backrelations(self.context,
                                                attribute="cites")

        citations.sort(key=lambda x: x.effective(), reverse=True)

        return citations

    def cited_by_links(self, obj):
        "Get Links for objects that link to this item"

        links = []

        brains = api.content.find(context=obj, depth=1,
                                 portal_type='Link')

        for brain in brains:
            link_obj = brain.getObject()
            links.append(link_obj)

        return links

    def index(self):
        return super(CitedBy, self).render()
