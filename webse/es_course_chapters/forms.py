from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class ChatForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#Chapter 1
class ModulsForm_gdc_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Associate files with Python',
                                 'Associate files with Python'),
                                ('Add Python to environmental variables',
                                 'Add Python to environmental variables'),
                                ('Create shortcuts for installed applications',
                                 'Create shortcuts for installed applications')])
    submit = SubmitField('Submit')  

class ModulsForm_gdc_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Creating the routes for your app',
                                 'Creating the routes for your app'),
                                ('Creating the functions for your routes',
                                 'Creating the functions for your routes'),
                                ('Installing the basic tools in your virtual environment to run your first app',
                                 'Installing the basic tools in your virtual environment to run your first app')])
    submit = SubmitField('Submit')    

class ModulsForm_gdc_ch1_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('@application.route(/methodology)',
                                 '@application.route(/methodology)'),
                                ('def methodology():',
                                 'def methodology():'),
                                ('Both lines of code',
                                 'Both lines of code')])
    submit = SubmitField('Submit') 

#Chapter 2
class ModulsForm_gdc_ch2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('redirect',
                                 'redirect'),
                                ('render_template',
                                 'render_template'),
                                ('submit',
                                 'submit')])
    submit = SubmitField('Submit')  

class ModulsForm_gdc_ch2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('<title>{title}</title>',
                                 '<title>{title}</title>'),
                                ('<title>(title)</title>',
                                 '<title>(title)</title>'),
                                ('<title>{{title}}</title>',
                                 '<title>{{title}}</title>')])
    submit = SubmitField('Submit')    

class ModulsForm_gdc_ch2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('<ul><li>...</li></ul>',
                                 '<ul><li>...</li></ul>'),
                                ('<ol><li>...</li></ol>',
                                 '<ol><li>...</li></ol>'),
                                ('<p><li>...</li></p>',
                                 '<p><li>...</li></p>')])
    submit = SubmitField('Submit') 

class ModulsForm_gdc_ch2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('forward',
                                 'forward'),
                                ('url_for',
                                 'url_for'),
                                ('redirect',
                                 'redirect')])
    submit = SubmitField('Submit')   

class ModulsForm_gdc_ch2_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Jinja2 main objective is to facilitate the introduction of JavaScript code in our templates',
                                 'Jinja2 main objective is to facilitate the introduction of JavaScript code in our templates'),
                                ('Jinja2 aims the introduction of CSS code in our templates',
                                 'Jinja2 aims the introduction of CSS code in our templates'),
                                ('Jinja2 is the Flask template engine that allows us to render logical statements in our html files',
                                 'Jinja2 is the Flask template engine that allows us to render logical statements in our html files')])
    submit = SubmitField('Submit')   

class ModulsForm_gdc_ch2_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('{% block content %} {% endblock %}',
                                 '{% block content %} {% endblock %}'),
                                ('{% extends %} {% extends %}',
                                 '{% extends %} {% extends %}'),
                                ('{% if statement %} {% endif statement %}',
                                 '{% if statement %} {% endif statement %}')])
    submit = SubmitField('Submit')       

#Chapter 3
class ModulsForm_gdc_ch3_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('It help us to organize our code',
                                 'It help us to organize our code'),
                                ('It is used by search engine algorithms to list pages in search results',
                                 'It is used by search engine algorithms to list pages in search results'),
                                ('It helps the routes to pass information to HTML files',
                                 'It helps the routes to pass information to HTML files')])
    submit = SubmitField('Submit')  

class ModulsForm_gdc_ch3_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The color and size of the elements in the body',
                                 'The color and size of the elements in the body'),
                                ('The padding and background color of the elements in the body',
                                 'The padding and background color of the elements in the body'),
                                ('The description of your web page, the authorship, or the viewport',
                                 'The description of your web page, the authorship, or the viewport')])
    submit = SubmitField('Submit') 

class ModulsForm_gdc_ch3_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('It connects html files inside the app',
                                 'It connects html files inside the app'),
                                ('It connects the routes and the html files inside the apps',
                                 'It connects the routes and the html files inside the apps'),
                                ('It defines the relationship between the current document and an external resource',
                                 'It defines the relationship between the current document and an external resource')])
    submit = SubmitField('Submit')  

class ModulsForm_gdc_ch3_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The viewport defines a static design and a fixed size',
                                 'The viewport defines a static design and a fixed size'),
                                ('The viewport is the user visible area of a web page',
                                 'The viewport is the user visible area of a web page'),
                                ('The viewport defines the size of the font used in the body',
                                 'The viewport defines the size of the font used in the body')])
    submit = SubmitField('Submit') 

class ModulsForm_gdc_ch3_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The padding of that element is not included in the width and height',
                                 'The padding of that element is not included in the width and height'),
                                ('The margin of that element is not included in the width and height',
                                 'The margin of that element is not included in the width and height'),
                                ('The padding and border of that element are included in the width and height',
                                 'The padding and border of that element are included in the width and height')])
    submit = SubmitField('Submit') 
  

class ModulsForm_gdc_ch3_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('It takes up its width plus some margin',
                                 'It takes up its width plus some margin'),
                                ('It always takes up the full width available',
                                 'It always takes up the full width available'),
                                ('It takes up as much width as necessary',
                                 'It takes up as much width as necessary')])
    submit = SubmitField('Submit')    

class ModulsForm_gdc_ch3_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('It is formatted as an inline element, but with margins',
                                 'It is formatted as an inline element, but with margins'),
                                ('It is formatted as a block element, but without margins',
                                 'It is formatted as a block element, but without margins'),
                                ('It is formatted as an inline element, but you can apply height and width values',
                                 'It is formatted as an inline element, but you can apply height and width values')])
    submit = SubmitField('Submit')     

class ModulsForm_gdc_ch3_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('justify-content: space-between;  align-items: center',
                                 'justify-content: space-between;  align-items: center'),
                                ('justify-content: center;  align-items: center',
                                 'justify-content: center;  align-items: center'),
                                ('flex-direction: row; justify-content: center',
                                 'flex-direction: row; justify-content: center')])
    submit = SubmitField('Submit') 

class ModulsForm_gdc_ch3_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('How much a flex item will grow relative to the rest of the flex items',
                                 'How much a flex item will grow relative to the rest of the flex items'),
                                ('How much a flex item will shrink relative to the rest of the flex items',
                                 'How much a flex item will shrink relative to the rest of the flex items'),
                                ('The initial length of a flex item',
                                 'The initial length of a flex item')])
    submit = SubmitField('Submit')      

class ModulsForm_gdc_ch3_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The orientation of the device',
                                 'The orientation of the device'),
                                ('The type of the device',
                                 'The type of the device'),
                                ('The capability of the device',
                                 'The capability of the device')])
    submit = SubmitField('Submit')   


  
