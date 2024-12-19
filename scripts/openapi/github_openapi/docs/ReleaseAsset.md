# ReleaseAsset

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
from github_openapi.models.release_asset import ReleaseAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseAsset from a JSON string
release_asset_instance = ReleaseAsset.from_json(json)
# print the JSON string representation of the object
print(ReleaseAsset.to_json())

# convert the object into a dict
release_asset_dict = release_asset_instance.to_dict()
# create an instance of ReleaseAsset from a dict
release_asset_from_dict = ReleaseAsset.from_dict(release_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


