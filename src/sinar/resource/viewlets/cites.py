# -*- coding: utf-8 -*-

from collective.relationhelpers import api
from plone.app.layout.viewlets import ViewletBase


class Cites(ViewletBase):

    def cites(self):
        """Get objects that this item cites, sort by effective date
           reversed.
        """

        citations = api.relations(self.context,
                                  attribute="cites")

        citations.sort(key=lambda x: x.effective(), reverse=True)

        return citations

    def index(self):
        return super(Cites, self).render()
