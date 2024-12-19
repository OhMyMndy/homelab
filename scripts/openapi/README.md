```bash
# SEE: https://github.com/OpenAPITools/openapi-generator/issues/14096
export _JAVA_OPTIONS=-DmaxYamlCodePoints=99999999
openapi-generator-cli generate -i https://api.tailscale.com/api/v2\?outputOpenapiSchema\=true -g python -o tailscale_openapi --package-name tailscale_openapi
uv add "tailscale-openapi@tailscale-openapi"


openapi-generator-cli generate -i https://raw.githubusercontent.com/github/rest-api-description/refs/heads/main/descriptions/api.github.com/api.github.com.yaml -g python -o github_openapi --package-name github_openapi
uv add "github_openapi@github_openapi"


openapi-generator-cli generate -i https://docs.gitea.com/redocusaurus/plugin-redoc-1.yaml -g python -o gitea_openapi --package-name gitea_openapi
uv add "gitea_openapi@gitea_openapi"

openapi-generator-cli generate -i https://auth.home.ohmymndy.com/api/v3/schema/ -g python -o authentik_openapi --package-name authentik_openapi
uv add "authentik_openapi@authentik_openapi"


echo $'\n[tool.pyright]\nvenvPath = "."\nvenv = ".venv"\n' >> pyproject.toml
```
