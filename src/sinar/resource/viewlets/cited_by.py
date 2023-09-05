# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class CitedBy(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'My message'

    def index(self):
        return super(CitedBy, self).render()
