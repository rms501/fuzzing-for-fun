from pathlib import Path

class PromptProvider:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not getattr(self, "_initialized", False):
            prompts_dir = Path(__file__).parent / ".." / "prompts"
            self.system_prompts = { prompt.stem: prompt.read_text() for prompt in (prompts_dir / "system").iterdir() }
            self.user_prompts = { prompt.stem: prompt.read_text() for prompt in (prompts_dir / "user").iterdir() }
            self._initialized = True
