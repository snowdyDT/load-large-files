import flask
import boto3


def get_upload_id(client, file_name: str) -> str:
    """
    Create a multipart upload
    :param file_name: file name from request
    :param client: boto3 client
    :return: upload id
    """
    upload_id = client.create_multipart_upload(Bucket='my-bucket', Key=file_name)['UploadId']

    return upload_id


def get_parts_file(file, client, file_name: str, upload_id: str) -> list:
    """
    Divide the file into parts and upload them in parallel
    :param file: file from request
    :param client: boto3 client
    :param file_name: file name from request
    :param upload_id: upload id from multipart upload
    :return: file parts
    """
    parts = []
    with file as f:
        while True:
            data = f.read(5 * 1024 * 1024)  # 5MB chunk size
            if not data:
                break

            # Upload each part in parallel using multiprocessing
            part_num = len(parts) + 1
            response = client.upload_part(Bucket='my-bucket', Key=file_name, PartNumber=part_num, UploadId=upload_id,
                                          Body=data)
            parts.append({'PartNumber': part_num, 'ETag': response['ETag']})

    return parts


def multipart_upload(client, file_name: str, upload_id: str, parts: list) -> None:
    """
    Complete the multipart upload
    :param client: boto3 client
    :param file_name: file name from request
    :param upload_id: upload id from multipart upload
    :param parts: file parts
    :return: None
    """
    client.complete_multipart_upload(Bucket='my-bucket', Key=file_name, UploadId=upload_id,
                                     MultipartUpload={'Parts': parts})

    return
