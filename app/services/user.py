import hashlib

from app.dao.user import UserDAO
from app.helpers.constans import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get('id')
        user = self.get_one(uid)

        user.username = data.get('username')
        user.password = data.get('password')
        user.role = data.get('role')

        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get('id')
        user = self.get_one(uid)
        if 'username' in data:
            user.username = data.get('username')
        if 'password' in data:
            user.password = data.get('password')
        if 'username' in data:
            user.role = data.get('role')
        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
