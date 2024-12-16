#!/usr/bin/env python3

import re
from os import system
from pprint import pprint

import yaml
import json
import subprocess


def remove_null_values(data):
    if isinstance(data, dict):
        # Iterate and recursively clean the dictionary
        return {k: remove_null_values(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        # Recursively clean each item in the list
        return [remove_null_values(item) for item in data if item is not None]
    else:
        # Return the data as-is for non-dict, non-list types
        return data


def get_exposed_ports(image):
    result = subprocess.run(f"docker inspect {image}".split(" "), capture_output=True)
    result = json.loads(result.stdout)
    return list(result[0].get("Config").get("ExposedPorts", {}).keys())


compose = {}
with open("docker-compose.yml") as stream:
    try:
        compose = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit

new_compose = {"services": {}, "volumes": {}}
for service_name, service in compose.get("services", {}).items():
    new_compose.get("services", {}).update(
        remove_null_values(
            {
                service_name: {
                    "labels": {},
                    "image": service.get("image"),
                    "volumes": [],
                    "restart": "always",
                    "depends_on": service.get("depends_on"),
                    "command": service.get("command"),
                    "env_file": service.get("env_file"),
                    "ports": get_exposed_ports(service.get("image")),
                }
            }
        )
    )
    for label in service.get("labels", []):
        label, value = label.split("=")
        if re.search("traefik.http.routers.(.+).rule", label):
            host = re.search(r"Host\(`(.+)`\)", value).group(1)
            new_compose.get("services").get(service_name).get("labels").update(
                {"kompose.service.expose": host}
            )

    for volume in service.get("volumes", []):
        if volume.startswith("./"):
            key, value = volume.split(":", 1)
            volume = re.sub(r"\./|[/]", r"_", key).strip("_")
            new_compose.get("volumes").update({volume: {}})
            new_compose.get("services").get(service_name).get("volumes").append(
                f"{volume}:{value}"
            )


with open("docker-compose-converted.yml", "w") as file:
    file.write(yaml.dump(new_compose))
    file.close()
