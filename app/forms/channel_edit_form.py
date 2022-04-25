from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, URL, Optional
from app.models import Channel


class ChannelEditForm(FlaskForm):
    profileImageUrl = StringField('profileImageUrl', validators=[DataRequired(), URL(), Length(max=255)])
    bannerImageUrl = StringField('bannerImageUrl', validators=[Optional(), URL(), Length(max=255)])
    about = StringField('about', validators=[Length(max=5000)])
    
    
class ChannelEditFormDefaultPfp(FlaskForm):
    profileImageUrl = StringField('profileImageUrl', validators=[DataRequired(), Length(max=255)])
    bannerImageUrl = StringField('bannerImageUrl', validators=[Optional(), URL(), Length(max=255)])
    about = StringField('about', validators=[Length(max=5000)])