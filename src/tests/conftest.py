import faker
import pytest
from starlette.testclient import TestClient

from domain.utils.roles import UserRole
from main import app
from tests.factories import SheetFactory, TaskFactory, UserFactory

client = TestClient(app=app)
fake = faker.Faker()


def mock_user(user, mocker):
    mocker.patch(
        "infrastructure.utils.user.UserInfo.get_user_info", return_value=user.dump()
    )


@pytest.fixture()
def mock_admin_permission(mocker):
    user = UserFactory(UserRole.admin.value)
    mock_user(user, mocker)


@pytest.fixture()
def mock_user_permission(mocker):
    user = UserFactory(UserRole.user.value)
    mock_user(user, mocker)


@pytest.fixture()
def mock_sheet_repo(mocker):
    repo_path = "infrastructure.repositories.sheets.SheetRepository"
    sheet = SheetFactory()

    mocker.patch(f"{repo_path}.insert", return_value=fake.pyint())
    mocker.patch(f"{repo_path}.update_by_id", return_value=fake.pyint())
    mocker.patch(f"{repo_path}.get_all", return_value=[sheet])
    mocker.patch(f"{repo_path}.get_by_id", return_value=sheet)
    mocker.patch(f"{repo_path}.delete_by_id", return_value=fake.pyint())


@pytest.fixture()
def mock_task_repo(mocker):
    repo_path = "infrastructure.repositories.tasks.TaskRepository"
    task = TaskFactory()

    mocker.patch(f"{repo_path}.insert", return_value=fake.pyint())
    mocker.patch(f"{repo_path}.update_by_id", return_value=task)
    mocker.patch(f"{repo_path}.get_all", return_value=[task])
    mocker.patch(f"{repo_path}.get_by_id", return_value=task)
    mocker.patch(f"{repo_path}.delete_by_id", return_value=fake.pyint())


@pytest.fixture()
async def mock_kafka(mocker):
    kafka_path = "application.use_cases.kafka.KafkaUseCase"
    mocker.patch(f"{kafka_path}.send_create_task", return_value=None)
    mocker.patch(f"{kafka_path}.send_retrieve_task", return_value=None)
    mocker.patch(f"{kafka_path}.send_done_task", return_value=None)
    mocker.patch(f"{kafka_path}.send_create_sheet", return_value=None)
    mocker.patch(f"{kafka_path}.send_retrieve_sheet", return_value=None)

    kafka_manager_path = "infrastructure.managers.kafka.KafkaManager"
    mocker.patch(f"{kafka_manager_path}.connect", return_value=None)
    mocker.patch(f"{kafka_manager_path}.close", return_value=None)
