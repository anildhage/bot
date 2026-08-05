from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    x_consumer_key: str = os.getenv("X_CONSUMER_KEY", "")
    x_consumer_secret: str = os.getenv("X_CONSUMER_SECRET", "")
    x_bearer_token: str = os.getenv("X_BEARER_TOKEN", "")
    x_access_token: str = os.getenv("X_ACCESS_TOKEN", "")
    x_access_token_secret: str = os.getenv("X_ACCESS_TOKEN_SECRET", "")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
    x_dry_run: bool = os.getenv("X_DRY_RUN", "true").lower() == "true"

    def x_credentials_ready(self) -> bool:
        return all(
            [
                self.x_consumer_key,
                self.x_consumer_secret,
                self.x_bearer_token,
                self.x_access_token,
                self.x_access_token_secret,
            ]
        )


settings = Settings()
