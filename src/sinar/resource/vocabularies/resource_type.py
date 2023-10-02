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
            VocabItem(u'updates', _(u'Articles, Blogs and Updates')),
            VocabItem(u'books', _(u'Books')),
            VocabItem(u'promotional',
                      _(u'Brochure, Promotional Materials')),
            VocabItem(u'project_report',
                      _(u'Project or Organization Reports')),
            VocabItem(u'data', _(u'Data, Surveys, Fact Sheets')),
            VocabItem(u'legal', _(u'Legal Documents, Filings, Judgements')),
            VocabItem(u'legislation', _(u'Legislation, Regulations')),
            VocabItem(u'media_article', _(u'News Article')),
            VocabItem(u'media_video', _(u'News Video')),
            VocabItem(u'media_audio', _(u'Podcast or Radio')),
            VocabItem(u'periodical', _(u'Newsletter, Journal')),
            VocabItem(u'policy', _(u'Policy, Strategy or Plan')),
            VocabItem('presentation', ('Panel, Presentation')),
            VocabItem(u'pressstatement',
                    _(u'Press Statement or News Release')),
            VocabItem(u'research', _(u'Research Reports, Working Paper')),
            VocabItem(u'training',
                      _(u'Training Material, Guides, Organizing/Educational Materials')),
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
