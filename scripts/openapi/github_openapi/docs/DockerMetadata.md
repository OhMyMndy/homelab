# DockerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.docker_metadata import DockerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DockerMetadata from a JSON string
docker_metadata_instance = DockerMetadata.from_json(json)
# print the JSON string representation of the object
print(DockerMetadata.to_json())

# convert the object into a dict
docker_metadata_dict = docker_metadata_instance.to_dict()
# create an instance of DockerMetadata from a dict
docker_metadata_from_dict = DockerMetadata.from_dict(docker_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


