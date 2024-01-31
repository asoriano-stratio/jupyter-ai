import os

here = os.path.abspath(os.path.dirname(__file__))

# ------------------------------------------------------------------
# Jupyter AI extension: traitlets configurable attributes
# ------------------------------------------------------------------

# See code at: from jupyter_ai.extension import AiExtension
c = get_config()

# => allowed_providers: Identifiers of allowlisted providers. If `None`, all are allowed.

# · Default provider: Stratio GenAI provider (custom provider defined in intell-genai package)
allowed_providers = ["stratio_genai_provider"]

# · Extra providers: comma-separated list of native Jupyter AI integrated providers
#       ai21
#       anthropic
#       anthropic-chat
#       azure-chat-openai
#       bedrock
#       bedrock-chat
#       cohere
#       gpt4all
#       huggingface_hub
#       openai
#       openai-chat
#       sagemaker-endpoint

extra_providers = os.environ.get("INTELL_GENAI_JUPYTER_AI_EXTRA_PROVIDERS", None)
if extra_providers:
    allowed_providers.extend([x.strip() for x in extra_providers.split(",")])

c.AiExtension.allowed_providers = allowed_providers



# => blocked_providers: Identifiers of blocklisted providers. If `None`, none are blocked.


# => allowed_models:    Language models to allow, as a list of global model IDs in the format
#                       `<provider>:<local-model-id>`. If `None`, all are allowed. Defaults to
#                       `None`.
#
#                       Note: Currently, if `allowed_providers` is also set, then this field is
#                       ignored. This is subject to change in a future non-major release. Using
#                       both traits is considered to be undefined behavior at this time.


# => blocked_models:    Language models to block, as a list of global model IDs in the format
#                       `<provider>:<local-model-id>`. If `None`, none are blocked. Defaults to
#                       `None`.


# => model_parameters:  Key-value pairs for model id and corresponding parameters that
#                       are passed to the provider class. The values are unpacked and passed to
#                       the provider class as-is.


# ------------------------------------------------------------------
# Jupyter AI: User-modifiable properties in the front-end interface
# ------------------------------------------------------------------

# Note: Implementation of configuration at front-end level => ConfigManager
#
#   - Default paths
#       from jupyter_ai.config_manager import DEFAULT_CONFIG_PATH, DEFAULT_SCHEMA_PATH, OUR_SCHEMA_PATH
#
#       · OUR_SCHEMA_PATH: JSON Schema file. Descriptor of User-modifiable properties in the front-end interface.
#           Code          => os.path.join(os.path.dirname(__file__), "config", "config_schema.json") # From jupyter_ai/config_manager.py
#           Analytic path => /miniconda/lib/python3.9/site-packages/jupyter_ai/config/config_schema.json
#
#       · DEFAULT_CONFIG_PATH: JSON file with the properties set by the user. It must match with the Json schema file at OUR_SCHEMA_PATH
#           Code          => from jupyter_core.paths import jupyter_data_dir; os.path.join(jupyter_data_dir(), "jupyter_ai", "config.json")
#           Analytic path => /home/${JPY_USER}/.local/share/jupyter/jupyter_ai/config.json
#
#  - Jupyter AI ConfigManager traitlets configurable attributes

config_path = os.path.join(here, "jupyter_ai", "config.json")
schema_path = os.path.join(here, "jupyter_ai", "config_schema.json")
os.remove(config_path)
os.remove(schema_path)
c.ConfigManager.config_path = config_path
c.ConfigManager.schema_path = schema_path

stratio_genai_provider_init    = os.environ.get("INTELL_GENAI_STRATIO_GENAI_PROVIDER_INIT", "false") == "true"
stratio_genai_service_url      = os.environ.get("INTELL_GENAI_STRATIO_GENAI_SERVICE_URL", None)
# stratio_genai_service_endpoint = os.environ.get("INTELL_GENAI_STRATIO_GENAI_SERVICE_ENDPOINT", None)
intell_genai_chat_manager      = os.environ.get("INTELL_GENAI_CHAT_MANAGER", "intelligence")

if stratio_genai_provider_init and stratio_genai_service_url:
    import json

    stratio_genai_provider_conf = {
        "model_provider_id": "stratio_genai_provider:*",
        "embeddings_provider_id": None,
        "send_with_shift_enter": True,
        "fields": {
            "stratio_ai_provider:*": {
                "stratio_genai_service_url": stratio_genai_service_url,
                "intell_genai_chat_manager": intell_genai_chat_manager
            }
        },
        "api_keys": {}
    }
    with open(config_path, "w") as f:
        json.dump(stratio_genai_provider_conf, f)
