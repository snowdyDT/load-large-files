import flask
import boto3
import os

import util

app = flask.Flask(__name__)

# Initialize S3-like client
client = boto3.client('s3',
                      endpoint_url=os.getenv('S3_ENDPOINT_URL'),
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))


@app.route('/upload', methods=['POST'])
def upload_file():
    file = flask.request.files['file']
    file_name = file.filename

    # Create a multipart upload
    upload_id = util.get_upload_id(client=client, file_name=file_name)

    # Divide the file into parts and upload them in parallel
    parts = util.get_parts_file(file=file, client=client, file_name=file_name, upload_id=upload_id)

    # Complete the multipart upload
    util.multipart_upload(client=client, file_name=file_name, upload_id=upload_id, parts=parts)

    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
