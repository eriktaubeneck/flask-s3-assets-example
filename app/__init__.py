from flask import Flask, render_template
from flask_s3 import FlaskS3
app = Flask(__name__)

app.config['AWS_ACCESS_KEY_ID'] = 'aws_key'
app.config['AWS_SECRET_ACCESS_KEY'] = 's3_secret'
app.config['S3_BUCKET_NAME'] = 'why_not_zoidberg'
app.config['DEBUG'] = True

s3 = FlaskS3(app)

@app.route("/")
def index():
    return render_template('index.html')