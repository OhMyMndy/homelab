# PreviewRuleMatches200ResponseMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | Source entities affected by the rule.  | 
**ports** | **List[str]** | Destinations that can be accessed.  | 
**line_number** | **float** | The rule&#39;s location in the policy file.  | 

## Example

```python
from tailscale_openapi.models.preview_rule_matches200_response_matches_inner import PreviewRuleMatches200ResponseMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewRuleMatches200ResponseMatchesInner from a JSON string
preview_rule_matches200_response_matches_inner_instance = PreviewRuleMatches200ResponseMatchesInner.from_json(json)
# print the JSON string representation of the object
print(PreviewRuleMatches200ResponseMatchesInner.to_json())

# convert the object into a dict
preview_rule_matches200_response_matches_inner_dict = preview_rule_matches200_response_matches_inner_instance.to_dict()
# create an instance of PreviewRuleMatches200ResponseMatchesInner from a dict
preview_rule_matches200_response_matches_inner_from_dict = PreviewRuleMatches200ResponseMatchesInner.from_dict(preview_rule_matches200_response_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


