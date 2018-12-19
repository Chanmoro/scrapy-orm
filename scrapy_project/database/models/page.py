from orator import Model


class Page(Model):

    __fillable__ = ['url', 'title']
