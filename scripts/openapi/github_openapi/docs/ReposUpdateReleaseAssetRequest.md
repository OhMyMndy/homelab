# ReposUpdateReleaseAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The file name of the asset. | [optional] 
**label** | **str** | An alternate short description of the asset. Used in place of the filename. | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.repos_update_release_asset_request import ReposUpdateReleaseAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateReleaseAssetRequest from a JSON string
repos_update_release_asset_request_instance = ReposUpdateReleaseAssetRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateReleaseAssetRequest.to_json())

# convert the object into a dict
repos_update_release_asset_request_dict = repos_update_release_asset_request_instance.to_dict()
# create an instance of ReposUpdateReleaseAssetRequest from a dict
repos_update_release_asset_request_from_dict = ReposUpdateReleaseAssetRequest.from_dict(repos_update_release_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


