from datetime import datetime

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash

from db.database import Base

class User(Base):
    """
    __tablename__
        User
    __table_args__
        {'extend_existing': True}
    """
    __tablename__ = 'users'
    id = _sql.Column(_sql.Integer, primary_key=True)
    username = _sql.Column(_sql.String(32), unique=True, nullable=False)
    password = _sql.Column(_sql.String(128), nullable=False)
    hashed_password = _sql.Column(_sql.String)
    email = _sql.Column(_sql.String(128), unique=True, nullable=False)
    created_at = _sql.Column(_sql.DateTime, default=datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=datetime.utcnow)

    def __init__(self, username, password, email):
        self.username = username
        self.password = _hash.sha256_crypt.encrypt(password)
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, password):
        return _hash.sha256_crypt.verify(password, self.password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


