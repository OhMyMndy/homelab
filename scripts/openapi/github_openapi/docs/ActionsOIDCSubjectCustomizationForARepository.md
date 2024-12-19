# ActionsOIDCSubjectCustomizationForARepository

Actions OIDC subject customization for a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_default** | **bool** | Whether to use the default template or not. If &#x60;true&#x60;, the &#x60;include_claim_keys&#x60; field is ignored. | 
**include_claim_keys** | **List[str]** | Array of unique strings. Each claim key can only contain alphanumeric characters and underscores. | [optional] 

## Example

```python
from github_openapi.models.actions_oidc_subject_customization_for_a_repository import ActionsOIDCSubjectCustomizationForARepository

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsOIDCSubjectCustomizationForARepository from a JSON string
actions_oidc_subject_customization_for_a_repository_instance = ActionsOIDCSubjectCustomizationForARepository.from_json(json)
# print the JSON string representation of the object
print(ActionsOIDCSubjectCustomizationForARepository.to_json())

# convert the object into a dict
actions_oidc_subject_customization_for_a_repository_dict = actions_oidc_subject_customization_for_a_repository_instance.to_dict()
# create an instance of ActionsOIDCSubjectCustomizationForARepository from a dict
actions_oidc_subject_customization_for_a_repository_from_dict = ActionsOIDCSubjectCustomizationForARepository.from_dict(actions_oidc_subject_customization_for_a_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


