# ImportProjectChoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcs** | **str** |  | [optional] 
**tfvc_project** | **str** |  | [optional] 
**human_name** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.import_project_choices_inner import ImportProjectChoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProjectChoicesInner from a JSON string
import_project_choices_inner_instance = ImportProjectChoicesInner.from_json(json)
# print the JSON string representation of the object
print(ImportProjectChoicesInner.to_json())

# convert the object into a dict
import_project_choices_inner_dict = import_project_choices_inner_instance.to_dict()
# create an instance of ImportProjectChoicesInner from a dict
import_project_choices_inner_from_dict = ImportProjectChoicesInner.from_dict(import_project_choices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


