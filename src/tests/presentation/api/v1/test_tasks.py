import faker
import pytest

from tests.factories import TaskFactory


class TestTask:
    url = "api/v1/tasks"

    def setup_method(self):
        self.new_task = TaskFactory()
        self.fake = faker.Faker()

    @pytest.mark.asyncio
    async def test_list_ok(
        self, client, mock_kafka, mock_user_permission, mock_task_repo
    ):
        response = client.get(url=self.url)

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert isinstance(response.json()[0], dict)

    @pytest.mark.asyncio
    async def test_create_ok(
        self, client, mock_kafka, mock_admin_permission, mock_task_repo
    ):
        response = client.post(url=self.url, json=self.new_task.dump_create())

        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        assert response.json().get("id")

    @pytest.mark.asyncio
    async def test_create_with_user_permission(
        self, client, mock_kafka, mock_user_permission, mock_task_repo
    ):
        response = client.post(url=self.url, json=self.new_task.dump_create())

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_create_with_incorrect_data(
        self, client, mock_kafka, mock_admin_permission, mock_task_repo
    ):
        response = client.post(url=self.url, json={})

        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_retrieve_ok(
        self, client, mock_kafka, mock_admin_permission, mock_task_repo
    ):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_update_ok(
        self, client, mock_kafka, mock_admin_permission, mock_task_repo
    ):
        response = client.put(
            url=f"{self.url}/{self.fake.pyint()}", json=self.new_task.dump_create()
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_update_with_user_permission(
        self, client, mock_kafka, mock_user_permission, mock_task_repo
    ):
        response = client.put(
            url=f"{self.url}/{self.fake.pyint()}", json=self.new_task.dump_create()
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_update_with_incorrect_data(
        self, client, mock_kafka, mock_admin_permission, mock_task_repo
    ):
        response = client.put(url=f"{self.url}/{self.fake.pyint()}", json={})

        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_done_ok(
        self, client, mock_kafka, mock_user_permission, mock_task_repo
    ):
        response = client.patch(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_delete_ok(
        self, client, mock_kafka, mock_admin_permission, mock_task_repo
    ):
        response = client.delete(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_delete_with_user_permission(
        self, client, mock_kafka, mock_user_permission, mock_task_repo
    ):
        response = client.delete(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 403
