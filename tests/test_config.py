from core.config import settings


def test_settings_object_exists() -> None:
    assert settings is not None


def test_ollama_base_url_has_default() -> None:
    assert settings.ollama_base_url


def test_ollama_model_has_default() -> None:
    assert settings.ollama_model
