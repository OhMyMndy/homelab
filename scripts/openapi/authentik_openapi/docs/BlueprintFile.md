# BlueprintFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**last_m** | **datetime** |  | 
**hash** | **str** |  | 
**meta** | [**Metadata**](Metadata.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.blueprint_file import BlueprintFile

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintFile from a JSON string
blueprint_file_instance = BlueprintFile.from_json(json)
# print the JSON string representation of the object
print(BlueprintFile.to_json())

# convert the object into a dict
blueprint_file_dict = blueprint_file_instance.to_dict()
# create an instance of BlueprintFile from a dict
blueprint_file_from_dict = BlueprintFile.from_dict(blueprint_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


