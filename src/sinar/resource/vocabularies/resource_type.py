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
    A vocabulary factory for resource types. This is used in the
    ResourceType field of the Resource content type.
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem('activity', _('Activity or Event Report')),
            VocabItem('application', _('Application or Product')),
            VocabItem('updates', _('Articles, Blogs and Updates')),
            VocabItem('books', _('Books')),
            VocabItem('promotional',
                      _('Brochure, Promotional Materials')),
            VocabItem('project_report',
                      _('Project or Organization Reports')),
            VocabItem('data', _('Data, Surveys, Fact Sheets')),
            VocabItem('kmrepo', _('Knowledge Respository')),
            VocabItem('legal', _('Legal Documents, Filings, Judgements')),
            VocabItem('legislation', _('Legislation, Regulations')),
            VocabItem('newsmedia', _('News Media Coverage')),
            VocabItem('periodical', _('Newsletter, Journal')),
            VocabItem('policy', _('Policy, Strategy or Plan')),
            VocabItem('presentation', ('Panel, Presentation')),
            VocabItem('pressstatement',
                      ('Press Statement or News Release')),
            VocabItem('research', _('Research Reports, Working Paper')),
            VocabItem('training',
                      _('Training Material, Guides, Organizing/Educational Materials')),
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
