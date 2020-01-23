from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    upc = db.Column(db.String())
    asin = db.Column(db.String())
    title = db.Column(db.String())
    category_restricted = db.Column(db.Boolean(), default=False)
    brand_restricted = db.Column(db.Boolean(), default=False)
    sellable = db.Column(db.Boolean(), default=False)
    unsellable_reason = db.Column(db.String())

    def __init__(self, upc, asin, title, category_restricted, brand_restricted, sellable, unsellable_reason):
        self.upc = upc
        self.asin = asin
        self.title = title
        self.category_restricted = category_restricted
        self.brand_restricted = brand_restricted
        self.sellable = sellable
        self.unsellable_reason = unsellable_reason

    def __repr__(self):
        return '<id {}>'.format(self.id)
