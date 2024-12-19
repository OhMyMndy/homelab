# ShortBlob

Short Blob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**sha** | **str** |  | 

## Example

```python
from github_openapi.models.short_blob import ShortBlob

# TODO update the JSON string below
json = "{}"
# create an instance of ShortBlob from a JSON string
short_blob_instance = ShortBlob.from_json(json)
# print the JSON string representation of the object
print(ShortBlob.to_json())

# convert the object into a dict
short_blob_dict = short_blob_instance.to_dict()
# create an instance of ShortBlob from a dict
short_blob_from_dict = ShortBlob.from_dict(short_blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


