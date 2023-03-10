import flask
import boto3

import util
import config

app = flask.Flask(__name__)

# Initialize S3-like client
client = boto3.client('s3',
                      endpoint_url=config.S3_ENDPOINT_URL,
                      aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)


@app.route('/')
def upload_file():
    return flask.render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file_post():
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
