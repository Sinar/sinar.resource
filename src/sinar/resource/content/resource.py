# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from sinar.resource import _
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema
from zope.interface import implementer


class IResource(model.Schema):
    """ Marker interface and Dexterity Python Schema for Resource
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('resource.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IResource)
class Resource(Container):
    """
    """
