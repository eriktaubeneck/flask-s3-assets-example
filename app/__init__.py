from flask import Flask, render_template
from flask_s3 import FlaskS3
app = Flask(__name__)

app.config['AWS_ACCESS_KEY_ID'] = 'aws_key'
app.config['AWS_SECRET_ACCESS_KEY'] = 's3_secret'
app.config['S3_BUCKET_NAME'] = 'why_not_zoidberg'
app.config['DEBUG'] = True
app.config['USE_S3_DEBUG'] = True
app.config['S3_CDN_DOMAIN'] = 'd14tm1m1qgdu96.cloudfront.net'

s3 = FlaskS3(app)

@app.route("/")
def index():
    return render_template('index.html')