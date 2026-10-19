from os import path

from dependency_injector import containers, providers

from config import ConfigRegistry


def get_config_file(file_name: str) -> str:
    current_file_path: str = path.dirname(path.abspath(__file__))
    root_dir: str = path.dirname(current_file_path)
    return path.join(root_dir, file_name)


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration(
        ini_files=[get_config_file("config.ini")],
        strict=True,
    )

    config_registry = providers.Singleton(
        ConfigRegistry.model_validate,
        config,
    )
