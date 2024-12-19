# PropertyMappingPreview

Preview how the current user is mapped via the property mappings selected in a provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | **Dict[str, object]** |  | [readonly] 

## Example

```python
from authentik_openapi.models.property_mapping_preview import PropertyMappingPreview

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyMappingPreview from a JSON string
property_mapping_preview_instance = PropertyMappingPreview.from_json(json)
# print the JSON string representation of the object
print(PropertyMappingPreview.to_json())

# convert the object into a dict
property_mapping_preview_dict = property_mapping_preview_instance.to_dict()
# create an instance of PropertyMappingPreview from a dict
property_mapping_preview_from_dict = PropertyMappingPreview.from_dict(property_mapping_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


