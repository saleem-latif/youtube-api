__author__ = 'Saleem Latif'


class Base(object):
    pass


class Thumbnail(Base):
    default = ''
    medium = ''
    high = ''
    standard = ''
    maxres = ''

    def __init__(self, default='', medium='', high='', standard='', maxres=''):
        self.default = default
        self.medium = medium
        self.high = high
        self.standard = standard
        self.maxres = maxres


class Category(Base):
    category_id = ''
    title = ''

    def __init__(self, category_id, title):
        self.category_id = category_id
        self.title = title

    def __unicode__(self):
        return u"{category_id}: {title}".format(category_id=self.category_id, title=self.title)

