import faker
import pytest

from tests.factories import SheetFactory


class TestSheet:
    url = "api/v1/sheets/"

    def setup_method(self):
        self.new_sheet = SheetFactory()
        self.fake = faker.Faker()

    @pytest.mark.asyncio
    async def test_list_ok(
        self, client, mock_kafka, mock_user_permission, mock_sheet_repo
    ):
        response = client.get(url=self.url)

        print(response.json())

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert isinstance(response.json()[0], dict)

    @pytest.mark.asyncio
    async def test_create_ok(
        self,
        client,
        mock_kafka,
        mock_admin_permission,
        mock_sheet_repo,
        mock_status_repo,
    ):
        response = client.post(url=self.url, json=self.new_sheet.dump_create())

        print(response.json())

        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        assert response.json().get("id")

    @pytest.mark.asyncio
    async def test_retrieve_ok(
        self, client, mock_kafka, mock_user_permission, mock_sheet_repo
    ):
        response = client.get(
            url=f"{self.url}{self.fake.pyint()}/",
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_update_ok(
        self, client, mock_kafka, mock_admin_permission, mock_sheet_repo
    ):
        response = client.put(
            url=f"{self.url}{self.fake.pyint()}/", json=self.new_sheet.dump_create()
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_delete_ok(
        self, client, mock_kafka, mock_admin_permission, mock_sheet_repo
    ):
        response = client.delete(
            url=f"{self.url}{self.fake.pyint()}/",
        )

        assert response.status_code == 204
