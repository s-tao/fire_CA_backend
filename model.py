from manage import db, app

# association table to establish many-to-many relationship
fire_locations = db.Table('fire_locations',
        db.Column('location_id', db.Integer, 
                                 db.ForeignKey('locations.id'), primary_key=True),
        db.Column('fire_id', db.Integer, 
                             db.ForeignKey('fires.id'), primary_key=True)
        )

class Location(db.Model):
    """Initial location of fire"""

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(25), unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):  
        return f'Located in {self.county}'


class Fire(db.Model):
    """All information pertaining to the fire""" 

    __tablename__ = 'fires'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    containment = db.Column(db.Float, nullable=True)
    cause = db.Column(db.Text, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    relocated = db.Column(db.Integer, nullable=True)
    death = db.Column(db.Integer, nullable=True)
    injured = db.Column(db.Integer, nullable=True)

    # relationship created with locations
    locations = db.relationship('Location', secondary=fire_locations,
                                            backref=db.backref('fires', lazy=True))

    # proximity to water source, roads / highways (future fields)

    def __repr__(self):  
        return f'Fire: {self.name}'


if __name__ == '__main__':
    db.create_all()