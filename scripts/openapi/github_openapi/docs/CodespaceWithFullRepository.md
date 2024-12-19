# CodespaceWithFullRepository

A codespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | Automatically generated name of this codespace. | 
**display_name** | **str** | Display name for this codespace. | [optional] 
**environment_id** | **str** | UUID identifying this codespace&#39;s environment. | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**billable_owner** | [**SimpleUser**](SimpleUser.md) |  | 
**repository** | [**FullRepository**](FullRepository.md) |  | 
**machine** | [**NullableCodespaceMachine**](NullableCodespaceMachine.md) |  | 
**devcontainer_path** | **str** | Path to devcontainer.json from repo root used to create Codespace. | [optional] 
**prebuild** | **bool** | Whether the codespace was created from a prebuild. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_used_at** | **datetime** | Last known time this codespace was started. | 
**state** | **str** | State of this codespace. | 
**url** | **str** | API URL for this codespace. | 
**git_status** | [**CodespaceGitStatus**](CodespaceGitStatus.md) |  | 
**location** | **str** | The initally assigned location of a new codespace. | 
**idle_timeout_minutes** | **int** | The number of minutes of inactivity after which this codespace will be automatically stopped. | 
**web_url** | **str** | URL to access this codespace on the web. | 
**machines_url** | **str** | API URL to access available alternate machine types for this codespace. | 
**start_url** | **str** | API URL to start this codespace. | 
**stop_url** | **str** | API URL to stop this codespace. | 
**publish_url** | **str** | API URL to publish this codespace to a new repository. | [optional] 
**pulls_url** | **str** | API URL for the Pull Request associated with this codespace, if any. | 
**recent_folders** | **List[str]** |  | 
**runtime_constraints** | [**CodespaceRuntimeConstraints**](CodespaceRuntimeConstraints.md) |  | [optional] 
**pending_operation** | **bool** | Whether or not a codespace has a pending async operation. This would mean that the codespace is temporarily unavailable. The only thing that you can do with a codespace in this state is delete it. | [optional] 
**pending_operation_disabled_reason** | **str** | Text to show user when codespace is disabled by a pending operation | [optional] 
**idle_timeout_notice** | **str** | Text to show user when codespace idle timeout minutes has been overriden by an organization policy | [optional] 
**retention_period_minutes** | **int** | Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days). | [optional] 
**retention_expires_at** | **datetime** | When a codespace will be auto-deleted based on the \&quot;retention_period_minutes\&quot; and \&quot;last_used_at\&quot; | [optional] 

## Example

```python
from github_openapi.models.codespace_with_full_repository import CodespaceWithFullRepository

# TODO update the JSON string below
json = "{}"
# create an instance of CodespaceWithFullRepository from a JSON string
codespace_with_full_repository_instance = CodespaceWithFullRepository.from_json(json)
# print the JSON string representation of the object
print(CodespaceWithFullRepository.to_json())

# convert the object into a dict
codespace_with_full_repository_dict = codespace_with_full_repository_instance.to_dict()
# create an instance of CodespaceWithFullRepository from a dict
codespace_with_full_repository_from_dict = CodespaceWithFullRepository.from_dict(codespace_with_full_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


