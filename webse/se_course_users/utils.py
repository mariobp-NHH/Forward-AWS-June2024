from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional
from webse.models import Userpage
from PIL import Image
import boto3
from botocore.exceptions import NoCredentialsError
import base64
import io
import os
import secrets

###-------Bucket Info

ACCESS_KEY=os.environ.get('ACCESS_KEY', None)

SECRET_KEY=os.environ.get('SECRET_KEY', None)

BUCKET=os.environ.get('BUCKET', None)


s3_r = boto3.resource('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

def read_image(image_filename):
    im = Image.open(s3_r.Bucket(BUCKET).Object(image_filename).get().get('Body'))
    data = io.BytesIO()
    im.save(data, im.format)
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data.decode('utf-8')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    in_mem_file = io.BytesIO()
    i.save(in_mem_file, format=i.format)

    in_mem_file.seek(0)

    s3_r.Bucket(BUCKET).put_object(Key=picture_fn, Body=in_mem_file)

    return picture_fn
