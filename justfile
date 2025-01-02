no-restart-policy:
  find . -maxdepth 2 -type f -iname 'docker-compose.y*ml' | tr '\n' '\0' | xargs -0 -I{} bash -c "docker compose --file '{}' config 2>/dev/null | yq '.services.* | select(.restart == null) | key | (. | parent | parent | .name) + \" \" + .'"

gh-login:
  gh auth login -s user

bw-config:
  bw config server https://passwords.home.ohmymndy.com

bw-login:
  bw login --raw "$(gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /user/emails | jq -r ".[0].email")"

bw-unlock:
  bw unlock --raw > "{{justfile_directory()}}/.bw-token"
