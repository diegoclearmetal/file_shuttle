from flask import Flask, request
import boto3

app = Flask(__name__)

BUCKET = 'cm-file-bucket'

@app.route("/")
def hello():
    app.logger.info('hello world')
    return "Hello World!"

@app.route("/upload", methods=['POST'])
def upload():
    app.logger.info('uploading file')
    if request.method == 'POST':
        name = request.args.get('file_name', 'NO_NAME')
        app.logger.info('recieved file %s' % name)
        file = request.files['file']
        _upload_file(file, name)
        return "Success"

def _upload_file(file, file_name):
    if not file:
        raise ValueError('No file supplied')
    app.logger.info('uploading file %s' % file_name)
    raw_content = file.read()
    boto3.resource('s3').meta.client.put_object(
        Bucket=BUCKET,
        Key=file_name,
        Body=raw_content,
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
