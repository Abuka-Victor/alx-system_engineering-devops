# Postmortem

## Issue Summary
There was an outage of service in some kubernetes pods at 23:11:06 UTC+1, the time of the release of version 2.0.4 of our application. We have identified using AWS X-Ray about 3200 requests affected. This resulted in a 6% decrease in weekly traffic compared to the last week. We also got a number of complaint emails from customers mostly within West Africa and South America. The root cause was the build type for the docker image set to ARM64.

## Issue Timeline
- Discovered 23:11:06 UTC when the QA Engineer tested the new version in production.
- Spent a few hours trying to debug the code and finally found the issue with the build script in the docker compose file.
- The incident was resolved by changing the build type to correspond to the Linus distro that the AWS EC2s were running at the time.
- During the debugging time, some extra logical bugs were fixed such as the issue with time conversion across zones on the calendar feature of the application.
