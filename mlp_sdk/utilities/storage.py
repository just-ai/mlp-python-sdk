from logging import Logger
from pathlib import Path
from typing import Callable, Dict, Optional


def check_and_download_dl_model(
    storage_creator: Callable,
    logger: Logger,
    source_model_path: Path,
    target_model_path: Path,
    source_backbone_model_path: Optional[Path] = None,
    target_backbone_model_path: Optional[Path] = None,
):
    logger.info(f'Model file {target_model_path} does{" " if target_model_path.exists() else " NOT"} exist')

    if not target_model_path.exists():
        logger.debug("Downloading model checkpoint from storage")

        storage = storage_creator()

        try:
            storage.download(source_model_path, str(target_model_path))
        except Exception as e:
            logger.error(str(e))
            raise

        logger.info(f"Successfully downloaded model {target_model_path} from storage.")

    if target_backbone_model_path is not None and source_backbone_model_path is not None:
        logger.info(
            f'Backbone model archive path {target_backbone_model_path}'
            f'does{" " if target_backbone_model_path.exists() else " NOT"} exist'
        )

        if not target_backbone_model_path.exists():
            logger.debug("Downloading backbone model from storage")

            storage = storage_creator()

            try:
                storage.download(source_backbone_model_path, str(target_backbone_model_path))
            except Exception as e:
                logger.error(str(e))
                raise

            logger.info(f"Successfully downloaded backbone model {target_backbone_model_path} from storage.")


def check_and_download_dl_model_artifacts(
    storage_creator: Callable,
    logger: Logger,
    artifact_name_to_source_path: Dict,
    resources_path: Path,
) -> Dict:
    artifact_name_to_target_path = {}
    storage = None

    for artifact_name_path, remote_path in artifact_name_to_source_path.items():
        artifact_path = resources_path / remote_path

        if not artifact_path.exists():
            if storage is None:
                logger.debug("Creating storage")
                storage = storage_creator()

            logger.debug(f"Downloading model from storage: '{remote_path}'")

            try:
                storage.download(remote_path, str(artifact_path))
            except Exception as e:
                logger.error(str(e))
                raise

            logger.debug("Successfully downloaded")

        artifact_name_to_target_path[artifact_name_path] = artifact_path

    return artifact_name_to_target_path
