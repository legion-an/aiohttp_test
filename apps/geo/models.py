from sqlalchemy import Column, Integer, String, ForeignKey
from main.settings import DB


class Region(DB.Model):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class City(DB.Model):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), default='')
    region_id = Column(Integer, ForeignKey('regions.id'))
    image = Column(String(300), nullable=True)

    def to_dict(self):
        return {c: getattr(self, c) for c in self._column_name_map}
