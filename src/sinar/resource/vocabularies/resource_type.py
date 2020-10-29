# -*- coding: utf-8 -*-

from plone.dexterity.interfaces import IDexterityContent
# from plone import api
from sinar.resource import _
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class ResourceType(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'activity', _(u'Activity or Event Report')),
            VocabItem(u'application', _(u'Application or Product')),
            VocabItem(u'books', _(u'Books')),
            VocabItem(u'promotional',
                      _(u'Brochure, PromotionalMaterials')),
            VocabItem(u'data', _(u'Data, Surveys, Fact Sheets')),
            VocabItem(u'legislation', _(u'Legislation, Regulations')),
            VocabItem(u'media', _(u'Interview, Panel, Presentation')),
            VocabItem(u'periodical', _(u'Newsletter, Journal')),
            VocabItem(u'policy', _(u'Policy, Strategy or Plan')),
            VocabItem(u'project', _(u'Project')),
            VocabItem(u'research', _(u'Research reports, working paper')),
            VocabItem(u'training',
                      _(u'Training Material, Guides, Organizaing/Educational Materials')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


ResourceTypeFactory = ResourceType()
