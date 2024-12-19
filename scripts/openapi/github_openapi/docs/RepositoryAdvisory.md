# RepositoryAdvisory

A repository security advisory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ghsa_id** | **str** | The GitHub Security Advisory ID. | [readonly] 
**cve_id** | **str** | The Common Vulnerabilities and Exposures (CVE) ID. | 
**url** | **str** | The API URL for the advisory. | [readonly] 
**html_url** | **str** | The URL for the advisory. | [readonly] 
**summary** | **str** | A short summary of the advisory. | 
**description** | **str** | A detailed description of what the advisory entails. | 
**severity** | **str** | The severity of the advisory. | 
**author** | [**SimpleUser**](SimpleUser.md) | The author of the advisory. | [readonly] 
**publisher** | [**SimpleUser**](SimpleUser.md) | The publisher of the advisory. | [readonly] 
**identifiers** | [**List[GlobalAdvisoryIdentifiersInner]**](GlobalAdvisoryIdentifiersInner.md) |  | [readonly] 
**state** | **str** | The state of the advisory. | 
**created_at** | **datetime** | The date and time of when the advisory was created, in ISO 8601 format. | [readonly] 
**updated_at** | **datetime** | The date and time of when the advisory was last updated, in ISO 8601 format. | [readonly] 
**published_at** | **datetime** | The date and time of when the advisory was published, in ISO 8601 format. | [readonly] 
**closed_at** | **datetime** | The date and time of when the advisory was closed, in ISO 8601 format. | [readonly] 
**withdrawn_at** | **datetime** | The date and time of when the advisory was withdrawn, in ISO 8601 format. | [readonly] 
**submission** | [**RepositoryAdvisorySubmission**](RepositoryAdvisorySubmission.md) |  | 
**vulnerabilities** | [**List[RepositoryAdvisoryVulnerability]**](RepositoryAdvisoryVulnerability.md) |  | 
**cvss** | [**GlobalAdvisoryCvss**](GlobalAdvisoryCvss.md) |  | 
**cvss_severities** | [**CvssSeverities**](CvssSeverities.md) |  | [optional] 
**cwes** | [**List[GlobalAdvisoryCwesInner]**](GlobalAdvisoryCwesInner.md) |  | [readonly] 
**cwe_ids** | **List[str]** | A list of only the CWE IDs. | 
**credits** | [**List[RepositoryAdvisoryCreditsInner]**](RepositoryAdvisoryCreditsInner.md) |  | 
**credits_detailed** | [**List[RepositoryAdvisoryCredit]**](RepositoryAdvisoryCredit.md) |  | [readonly] 
**collaborating_users** | [**List[SimpleUser]**](SimpleUser.md) | A list of users that collaborate on the advisory. | 
**collaborating_teams** | [**List[Team]**](Team.md) | A list of teams that collaborate on the advisory. | 
**private_fork** | [**SimpleRepository**](SimpleRepository.md) | A temporary private fork of the advisory&#39;s repository for collaborating on a fix. | [readonly] 

## Example

```python
from github_openapi.models.repository_advisory import RepositoryAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisory from a JSON string
repository_advisory_instance = RepositoryAdvisory.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisory.to_json())

# convert the object into a dict
repository_advisory_dict = repository_advisory_instance.to_dict()
# create an instance of RepositoryAdvisory from a dict
repository_advisory_from_dict = RepositoryAdvisory.from_dict(repository_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


