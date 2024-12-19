# ReleaseAsset1

Data related to a release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_download_url** | **str** |  | 
**content_type** | **str** |  | 
**created_at** | **datetime** |  | 
**download_count** | **int** |  | 
**id** | **int** |  | 
**label** | **str** |  | 
**name** | **str** | The file name of the asset. | 
**node_id** | **str** |  | 
**size** | **int** |  | 
**state** | **str** | State of the release asset. | 
**updated_at** | **datetime** |  | 
**uploader** | [**User**](User.md) |  | [optional] 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.release_asset1 import ReleaseAsset1

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseAsset1 from a JSON string
release_asset1_instance = ReleaseAsset1.from_json(json)
# print the JSON string representation of the object
print(ReleaseAsset1.to_json())

# convert the object into a dict
release_asset1_dict = release_asset1_instance.to_dict()
# create an instance of ReleaseAsset1 from a dict
release_asset1_from_dict = ReleaseAsset1.from_dict(release_asset1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


