# NullableCodespaceMachine

A description of the machine powering a codespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the machine. | 
**display_name** | **str** | The display name of the machine includes cores, memory, and storage. | 
**operating_system** | **str** | The operating system of the machine. | 
**storage_in_bytes** | **int** | How much storage is available to the codespace. | 
**memory_in_bytes** | **int** | How much memory is available to the codespace. | 
**cpus** | **int** | How many cores are available to the codespace. | 
**prebuild_availability** | **str** | Whether a prebuild is currently available when creating a codespace for this machine and repository. If a branch was not specified as a ref, the default branch will be assumed. Value will be \&quot;null\&quot; if prebuilds are not supported or prebuild availability could not be determined. Value will be \&quot;none\&quot; if no prebuild is available. Latest values \&quot;ready\&quot; and \&quot;in_progress\&quot; indicate the prebuild availability status. | 

## Example

```python
from github_openapi.models.nullable_codespace_machine import NullableCodespaceMachine

# TODO update the JSON string below
json = "{}"
# create an instance of NullableCodespaceMachine from a JSON string
nullable_codespace_machine_instance = NullableCodespaceMachine.from_json(json)
# print the JSON string representation of the object
print(NullableCodespaceMachine.to_json())

# convert the object into a dict
nullable_codespace_machine_dict = nullable_codespace_machine_instance.to_dict()
# create an instance of NullableCodespaceMachine from a dict
nullable_codespace_machine_from_dict = NullableCodespaceMachine.from_dict(nullable_codespace_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


