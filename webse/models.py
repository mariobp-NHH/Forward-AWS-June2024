from datetime import datetime
from webse import application, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Database User
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_register = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    institution = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    chats_gender = db.relationship('ChatGender', backref='author', lazy=True)
    questionnaires_gender = db.relationship('QuestionnaireGender', backref='author', lazy=True)
    questionnaires_gender_chat = db.relationship('QuestionnaireGenderChat', backref='author', lazy=True)
    chats_gd = db.relationship('ChatGD', backref='author', lazy=True)
    announcement_gd = db.relationship('AnnouncementGD', backref='author', lazy=True)
    questionnaires_gd = db.relationship('QuestionnaireGD', backref='author', lazy=True)
    emissions_gd = db.relationship('EmissionsGD', backref='author', lazy=True)
    moduls_gd = db.relationship('ModulsGD', backref='author', lazy=True)
    questionnaires_gd_chat = db.relationship('QuestionnaireGDChat', backref='author', lazy=True)
    chats_se = db.relationship('Chat', backref='author', lazy=True)
    announcement_se = db.relationship('AnnouncementSE', backref='author', lazy=True)
    moduls_se = db.relationship('Moduls', backref='author', lazy=True)
    emissions_se = db.relationship('EmissionsSE', backref='author', lazy=True)
    chats_sep = db.relationship('ChatSEP', backref='author', lazy=True)
    chats_es = db.relationship('ChatES', backref='author', lazy=True)
    announcement_es = db.relationship('AnnouncementES', backref='author', lazy=True)
    questionnaires_es = db.relationship('QuestionnaireES', backref='author', lazy=True)    
    moduls_es = db.relationship('ModulsES', backref='author', lazy=True)
    sentence_es = db.relationship('SentenceES', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Database Gender Platform
class ChatGender(db.Model):
    __bind_key__ = 'gender_platform'
    __tablename__ = 'chat_gender'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatGender('{self.title}', '{self.date_posted}')"

class QuestionnaireGender(db.Model):
    __bind_key__ = 'gender_platform'
    __tablename__= 'questionnaire_gender'
    id = db.Column(db.Integer, primary_key=True)
    title_questionnaire = db.Column(db.String(100), nullable=False)
    title_question = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_option = db.Column(db.Integer, nullable=True)
    university = db.Column(db.String(100))
    date_question = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireGender('{self.question_str}', '{self.date_exercise}')"

class QuestionnaireGenderChat(db.Model):
    __bind_key__ = 'gender_platform'
    __tablename__= 'questionnaire_gender_chat'
    id = db.Column(db.Integer, primary_key=True)
    title_questionnaire = db.Column(db.String(100), nullable=False)
    title_chat = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    university = db.Column(db.String(100))
    date_chat = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireGenderChat('{self.question_str}', '{self.date_exercise}')"


# Database Green Digitalization Course
class ChatGD(db.Model):
    __bind_key__ = 'gd_course'
    __tablename__ = 'chat_gd'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    institution = db.Column(db.String(120))
    chapter = db.Column(db.String(120))
    group = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatGD('{self.title}', '{self.date_posted}')"  

class AnnouncementGD(db.Model):
    __bind_key__= 'gd_course'
    __tablename__= 'announcement_gd'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"AnnouncementGD('{self.title}', '{self.date_posted}')"

class QuestionnaireGD(db.Model):
    __bind_key__= 'gd_course'
    __tablename__ = 'questionnaire_gd'
    id = db.Column(db.Integer, primary_key=True)
    title_questionnaire = db.Column(db.String(100), nullable=False)
    title_question = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_option = db.Column(db.Integer, nullable=True)
    university = db.Column(db.String(100))
    date_question = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireGD('{self.question_str}', '{self.date_exercise}')" 

class QuestionnaireGDChat(db.Model):
    __bind_key__ = 'gd_course'
    __tablename__= 'questionnaire_gd_chat'
    id = db.Column(db.Integer, primary_key=True)
    title_chat = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    university = db.Column(db.String(100))
    date_chat = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireGDChat('{self.question_str}', '{self.date_exercise}')"        

class EmissionsGD(db.Model):
    __bind_key__= 'gd_course'
    __tablename__= 'emissions_gd'
    id = db.Column(db.Integer, primary_key=True)
    kms = db.Column(db.Float)
    transport = db.Column(db.String)
    fuel = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    co2= db.Column(db.Float)
    ch4= db.Column(db.Float)
    total = db.Column(db.Float)
    student = db.Column(db.String, nullable=False)
    institution = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Emissions('{self.kms}', '{self.transport}', '{self.fuel}', '{self.date}', '{self.co2}', '{self.ch4}', '{self.total}', '{self.user_id}')"

class ModulsGD(db.Model):
    __bind_key__= 'gd_course'
    __tablename__= 'moduls_gd'
    id = db.Column(db.Integer, primary_key=True)
    title_mo = db.Column(db.String(100), nullable=False)
    title_ch = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_result = db.Column(db.Integer)
    question_option = db.Column(db.Integer, nullable=True)
    question_section = db.Column(db.String(100), nullable=True)
    date_exercise = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ModulsGD('{self.question_str}', '{self.question_result}', '{self.date_exercise}')"        

#Database Sustainable Energy Course
class Chat(db.Model):
    __bind_key__= 'se_course'
    __tablename__= 'chat_se'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    chat_module = db.Column(db.String(100), nullable=False)
    chat_group = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Chat('{self.title}', '{self.date_posted}')"

class AnnouncementSE(db.Model):
    __bind_key__= 'se_course'
    __tablename__= 'announcement_se'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Announcement('{self.title}', '{self.date_posted}')"

class Moduls(db.Model):
    __bind_key__= 'se_course'
    __tablename__= 'moduls_se'
    id = db.Column(db.Integer, primary_key=True)
    title_mo = db.Column(db.String(100), nullable=False)
    title_ch = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_result = db.Column(db.Integer)
    question_option = db.Column(db.Integer, nullable=True)
    question_section = db.Column(db.String(100), nullable=True)
    date_exercise = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Moduls('{self.question_str}', '{self.question_result}', '{self.date_exercise}')"

class EmissionsSE(db.Model):
    __bind_key__= 'se_course'
    __tablename__= 'emissions_se'
    id = db.Column(db.Integer, primary_key=True)
    kms = db.Column(db.Float)
    transport = db.Column(db.String)
    fuel = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    co2= db.Column(db.Float)
    ch4= db.Column(db.Float)
    total = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Emissions('{self.kms}', '{self.transport}', '{self.fuel}', '{self.date}', '{self.co2}', '{self.ch4}', '{self.total}', '{self.user_id}')"


#Database Sustainable Energy Platform
class ChatSEP(db.Model):
    __bind_key__= 'se_platform'
    __tablename__= 'chat_sep'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    chat_module = db.Column(db.String(100), nullable=False)
    chat_group = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatSEP('{self.title}', '{self.date_posted}')"
    

# Database Economies of the Spanish Course
class ChatES(db.Model):
    __bind_key__ = 'es_course'
    __tablename__ = 'chat_es'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    institution = db.Column(db.String(120))
    chapter = db.Column(db.String(120))
    group = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ChatES('{self.title}', '{self.date_posted}')"  

class AnnouncementES(db.Model):
    __bind_key__= 'es_course'
    __tablename__= 'announcement_es'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"AnnouncementES('{self.title}', '{self.date_posted}')"

class QuestionnaireES(db.Model):
    __bind_key__= 'es_course'
    __tablename__ = 'questionnaire_es'
    id = db.Column(db.Integer, primary_key=True)
    title_questionnaire = db.Column(db.String(100), nullable=False)
    title_question = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_option = db.Column(db.Integer, nullable=True)
    university = db.Column(db.String(100))
    date_question = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"QuestionnaireES('{self.question_str}', '{self.date_exercise}')" 


class ModulsES(db.Model):
    __bind_key__= 'es_course'
    __tablename__= 'moduls_es'
    id = db.Column(db.Integer, primary_key=True)
    title_mo = db.Column(db.String(100), nullable=False)
    title_ch = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_result = db.Column(db.Integer)
    question_option = db.Column(db.Integer, nullable=True)
    question_section = db.Column(db.String(100), nullable=True)
    date_exercise = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ModulsES('{self.question_str}', '{self.question_result}', '{self.date_exercise}')"
    

class SentenceES(db.Model):
    __bind_key__ = 'es_course'
    __tablename__= 'sentence_table_es'
    id = db.Column(db.Integer, primary_key=True)
    incorrect_sentence = db.Column(db.String)
    correct_sentence_one = db.Column(db.String)
    correct_sentence_two = db.Column(db.String)
    correct_sentence_three = db.Column(db.String)
    correct_sentence_four = db.Column(db.String)
    objective = db.Column(db.String)
    source = db.Column(db.String)
    your_sentence = db.Column(db.String)
    result_string = db.Column(db.String)
    result_num= db.Column(db.Float)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    group = db.Column(db.String)
    university = db.Column(db.String)
    year = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

                        
        
