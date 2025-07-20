Task Overview:
You are tasked with correcting a FastAPI microservice where the /v1/items endpoint currently fails due to a datetime serialization error. The current implementation returns HTTP 500 with an error indicating that datetime objects cannot be serialized into JSON. Your objective is to fix this bug so that the endpoint returns valid JSON data with proper ISO-8601 formatted timestamps for the created_at field.

Guidance:
- Review the API endpoint responsible for returning item data and consider how FastAPI serializes responses.
- Ensure that datetime objects in the returned data are encoded into formats that JSON can support.
- No changes outside of addressing the serialization issue in the /v1/items handler are expected.
- Use testing procedures provided to verify your solution.

Objectives:
- Resolve the datetime serialization problem so that the endpoint returns HTTP 200 and valid JSON.
- Confirm that the created_at field in the response uses an ISO-8601 datetime string for each item.
- Ensure that the provided tests pass without any serialization errors in the logs.

How to Verify:
- After applying your fix, request the /v1/items endpoint and check for an HTTP 200 response with JSON output containing properly formatted timestamps.
- Run the provided tests to ensure they all pass and no TypeError or serialization errors occur in the application logs.
