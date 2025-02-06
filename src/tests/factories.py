import datetime

import faker


class UserFactory:
    def __init__(self, user_role):
        self.user_role = user_role
        self.fake = faker.Faker()

    def dump(self):
        return {
            "id": self.fake.pyint(),
            "username": self.fake.user_name(),
            "role": self.user_role,
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        }


class SheetFactory:
    def __init__(self):
        self.fake = faker.Faker()

    def dump_create(self):
        return {
            "name": self.name,
            "description": self.description,
        }

    @property
    def id(self):
        return self.fake.pyint()

    @property
    def name(self):
        return self.fake.user_name()

    @property
    def description(self):
        return self.fake.user_name()

    @property
    def created_at(self):
        return datetime.datetime.now()

    @property
    def updated_at(self):
        return datetime.datetime.now()

    @property
    def creator_id(self):
        return self.fake.pyint()


class TaskFactory:
    def __init__(self):
        self.fake = faker.Faker()

    def dump_create(self):
        return {
            "name": self.name,
            "description": self.description,
            "sheet_id": self.sheet_id,
            "estimated_date": str(self.estimated_date),
            "status_id": self.status_id,
        }

    @property
    def id(self):
        return self.fake.pyint()

    @property
    def name(self):
        return self.fake.user_name()

    @property
    def description(self):
        return self.fake.user_name()

    @property
    def sheet_id(self):
        return self.fake.pyint()

    @property
    def status_id(self):
        return self.fake.pyint()

    @property
    def created_at(self):
        return datetime.datetime.now()

    @property
    def updated_at(self):
        return datetime.datetime.now()

    @property
    def estimated_date(self):
        return datetime.datetime.now()
