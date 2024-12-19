```bash
# SEE: https://github.com/OpenAPITools/openapi-generator/issues/14096
export _JAVA_OPTIONS=-DmaxYamlCodePoints=99999999
openapi-generator-cli generate -i https://api.tailscale.com/api/v2\?outputOpenapiSchema\=true -g python -o tailscale_openapi --package-name tailscale_openapi
uv add "tailscale-openapi@tailscale-openapi"


openapi-generator-cli generate -i https://raw.githubusercontent.com/github/rest-api-description/refs/heads/main/descriptions/api.github.com/api.github.com.yaml -g python -o github_openapi --package-name github_openapi
uv add "github_openapi@github_openapi"

echo $'\n[tool.pyright]\nvenvPath = "."\nvenv = ".venv"\n' >> pyproject.toml
```
