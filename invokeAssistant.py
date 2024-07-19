import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('NhGk8OmAHn0ejnCa4yQ9DmCxWNMkZEU_k16emts2rO6u')
assistant = AssistantV2(
    version='2018-09-20',
    authenticator=authenticator)
assistant.set_service_url('https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/c502732b-69a9-4b26-b993-26b12f31cfd2')

#########################
# Sessions
#########################
ENV_ID = "fbbd61ce-310d-4e2e-955a-3e027b2a3b91"
session = assistant.create_session(
    assistant_id = ENV_ID).get_result()
print("xxxxx")
print(json.dumps(session, indent=2))

# assistant.delete_session("cd0ed898-4b6b-4a36-a035-82f4646a52f4", "<YOUR SESSION ID>").get_result()

#########################
# Message
#########################

message = assistant.message(
    assistant_id = ENV_ID,
    session_id=session["session_id"],
    input={'text': 'test'},
).get_result()
print(json.dumps(message, indent=2))


message = assistant.message(
    assistant_id = ENV_ID,
    session_id=session["session_id"],
    input={'text': '1'},
).get_result()
print(json.dumps(message, indent=2))

message = assistant.message(
    assistant_id = ENV_ID,
    session_id=session["session_id"],
    # input={'text': '1'},
).get_result()
print(json.dumps(message, indent=2))


# logs = assistant.list_logs(
#     "<YOUR ASSISTANT ID>"
# )
# print(json.dumps(logs, indent=2))