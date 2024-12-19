# Release

The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[ReleaseAsset1]**](ReleaseAsset1.md) |  | 
**assets_url** | **str** |  | 
**author** | [**User2**](User2.md) |  | 
**body** | **str** |  | 
**created_at** | **datetime** |  | 
**discussion_url** | **str** |  | [optional] 
**draft** | **bool** | Whether the release is a draft or published | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 
**prerelease** | **bool** | Whether the release is identified as a prerelease or a full release. | 
**published_at** | **datetime** |  | 
**reactions** | [**Reactions**](Reactions.md) |  | [optional] 
**tag_name** | **str** | The name of the tag. | 
**tarball_url** | **str** |  | 
**target_commitish** | **str** | Specifies the commitish value that determines where the Git tag is created from. | 
**upload_url** | **str** |  | 
**url** | **str** |  | 
**zipball_url** | **str** |  | 

## Example

```python
from github_openapi.models.release import Release

# TODO update the JSON string below
json = "{}"
# create an instance of Release from a JSON string
release_instance = Release.from_json(json)
# print the JSON string representation of the object
print(Release.to_json())

# convert the object into a dict
release_dict = release_instance.to_dict()
# create an instance of Release from a dict
release_from_dict = Release.from_dict(release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


