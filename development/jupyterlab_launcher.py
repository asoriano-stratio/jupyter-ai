# ------------------------------
# => Jupyter directories
# ------------------------------
import os
HERE = os.path.abspath(os.path.dirname(__file__))
os.environ["JUPYTERLAB_SETTINGS_DIR"] = os.path.join(HERE, "jupyter_dirs", "jupyterlab_user_settings_dir")
os.environ["JUPYTERLAB_WORKSPACES_DIR"] = os.path.join(HERE, "jupyter_dirs", "jupyterlab_workspaces_dir")
os.environ["JUPYTER_CONFIG_DIR"] = os.path.join(HERE, "jupyter_dirs", "jupyter_config_dir")
os.environ["JUPYTER_DATA_DIR"] = os.path.join(HERE, "jupyter_dirs", "jupyter_data_dir")
os.environ["JUPYTER_RUNTIME_DIR"] = os.path.join(HERE, "jupyter_dirs", "jupyter_data_dir")
# With recent releases of jupyter_core, it is now possible to set the JUPYTER_PREFER_ENV_PATH environment variable
# to change this order so the path to the virtual environment shows up first.
#   If not, path /home/asoriano/miniconda3/envs/local-jupyterlab/share/jupyter has the highest priority
os.environ["JUPYTER_PREFER_ENV_PATH"] = "0"

# ------------------------------
# => Configuration
# ------------------------------

# · Enable/Disable extension
os.environ["INTELL_GENAI_ENABLE_JUPYTER_AI"] = "true"

# · Providers whitelist (Note: stratio_genai_provider is always included)
#os.environ["INTELL_GENAI_JUPYTER_AI_EXTRA_PROVIDERS"] = "openai, openai-chat"

# · stratio_genai_provider integration
os.environ["INTELL_GENAI_STRATIO_GENAI_PROVIDER_INIT"] = "true"
os.environ["INTELL_GENAI_STRATIO_GENAI_SERVICE_URL"] = "http://127.0.0.1:8081"
os.environ["INTELL_GENAI_STRATIO_GENAI_SERVICE_ENDPOINT"] = "/v1/chains/openai_chat_chain/invoke"


# => Note: Code executed in docker entrypoint
enable_jupyter_ai = os.environ.get("INTELL_GENAI_ENABLE_JUPYTER_AI", "false") == "true"
if enable_jupyter_ai:
    os.system('jupyter server extension enable jupyter_ai')
    os.system('jupyter labextension enable @jupyter-ai/core jupyter_ai')
else:
    os.system('jupyter server extension disable jupyter_ai')
    os.system('jupyter labextension disable @jupyter-ai/core jupyter_ai')

# Note: the others env.vars are applied in traitlets file jupyter_jupyter_ai_config.py

# ------------------------------
# => Launching JupyterLab
# ------------------------------

from jupyterlab.labapp import main as jupyterlab_main
from jupyterlab.labapp import LabPathApp

LabPathApp().start()

jupyterlab_main([
    "--notebook-dir", os.path.join(HERE, "jupyter_dirs", "workspace")
])
