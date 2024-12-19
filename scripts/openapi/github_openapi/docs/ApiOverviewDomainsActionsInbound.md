# ApiOverviewDomainsActionsInbound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_domains** | **List[str]** |  | [optional] 
**wildcard_domains** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.api_overview_domains_actions_inbound import ApiOverviewDomainsActionsInbound

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOverviewDomainsActionsInbound from a JSON string
api_overview_domains_actions_inbound_instance = ApiOverviewDomainsActionsInbound.from_json(json)
# print the JSON string representation of the object
print(ApiOverviewDomainsActionsInbound.to_json())

# convert the object into a dict
api_overview_domains_actions_inbound_dict = api_overview_domains_actions_inbound_instance.to_dict()
# create an instance of ApiOverviewDomainsActionsInbound from a dict
api_overview_domains_actions_inbound_from_dict = ApiOverviewDomainsActionsInbound.from_dict(api_overview_domains_actions_inbound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


