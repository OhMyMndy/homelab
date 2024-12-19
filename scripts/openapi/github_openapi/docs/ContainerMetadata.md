# ContainerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | 

## Example

```python
from github_openapi.models.container_metadata import ContainerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerMetadata from a JSON string
container_metadata_instance = ContainerMetadata.from_json(json)
# print the JSON string representation of the object
print(ContainerMetadata.to_json())

# convert the object into a dict
container_metadata_dict = container_metadata_instance.to_dict()
# create an instance of ContainerMetadata from a dict
container_metadata_from_dict = ContainerMetadata.from_dict(container_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


