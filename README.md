# Task: Backend2
## Description:

There is a virtual machine with limited resources (512MB of RAM and the same amount of free disk space)
There is also an AWS S3-like service (Yandex, PS.kz , Self-hosted Mini)

It is necessary to organize the fastest (in several streams) downloading of large files, more than 1.5 GB.

It is necessary to write a small web application consisting of two parts:
On the endpoint's backend receiving data and uploading it immediately to S3.
On the front, selecting a file and sending it to the endpoint implemented on the backend.

Uploading via a presigned url is NOT counted as a solution to the problem.
The file must pass through backend applications.

## Solution:

Steps to solving problems:
1) Implemented a backend endpoint that receives data from the external interface and loads it into S3. This part is implemented using the Flask web framework.
2) A streaming approach is used to upload a large file into multiple streams, which provides faster downloads.
3) Split the file into several parts and load them in parallel using the Python's multiprocessing module.
4) Once the file is uploaded, assemble the parts into a complete file and upload it to S3 using the backend endpoint.


## How to run the code:
1) Use the Python's keyring library to write your data for S3 service (config.py).
2) Install all the libraries that are specified in the file requirements.txt
3) Run the flask app in app.py
4) Open the service and upload the file.
5) Get the status of S3 bucket.

<br>

<!-- 
Below, separated by commas, enter the tags of the service (adjectives in the masculine gender), for example: selenium, RASA
-->
> Tags: Flask
<!--
Specify the criticality as a number from 0 (not critical) to 5 (simple leads to serious financial losses)
-->
> Criticality: 1
## Authors

| Role   | FIO            | Post             | email                                                       | Phone |
|--------|----------------|------------------|-------------------------------------------------------------|-------|
| Master | Shatekov Sabyr | Python Developer | [shatekov.sabyr@gmail.com](mailto:shatekov.sabyr@gmail.com) |       |
|        |                |                  |                                                             |       |
|        |                |                  |                                                             |       |
|        |                |                  |                                                             |       |

## Dependencies

- requriements
- Flask

## Technology accounts

| System | Title                   |
|--------|-------------------------|
| S3     | <S3_ENDPOINT_URL>       |
| AWS    | <AWS_ACCESS_KEY_ID>     |
| AWS    | <AWS_SECRET_ACCESS_KEY> |


### Programming language:
*Python 3.9*
