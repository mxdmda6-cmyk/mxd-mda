from pathlib import Path

ENV_TEMPLATE = Path("config/.env.example")

SENSITIVE_PREFIXES = (
    "sk-",
    "sk-ant-",
    "AIza",
    "secret_",
    "fo1_",
    "amzn1.",
    "Atzr|",
    "IGAA",
    "phc_",
    "eyJ",
)

REQUIRED_DISABLED_FLAGS = (
    "ENABLE_DISCORD_BOT=false",
    "ENABLE_NOTION_SYNC=false",
    "ENABLE_EMAIL_AUTOMATION=false",
    "ENABLE_SOCIAL_POSTING=false",
    "ENABLE_VECTOR_SEARCH=false",
)


def test_env_example_uses_safe_placeholders() -> None:
    content = ENV_TEMPLATE.read_text(encoding="utf-8")

    for prefix in SENSITIVE_PREFIXES:
        assert prefix not in content

    assert "replace-me" in content
    assert "Do not paste real keys" in content


def test_risky_feature_flags_default_to_disabled() -> None:
    content = ENV_TEMPLATE.read_text(encoding="utf-8")

    for flag in REQUIRED_DISABLED_FLAGS:
        assert flag in content
