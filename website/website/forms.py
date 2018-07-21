"""WTForms html forms."""

from website.dictionaries import website_form_labels as labels

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Optional, Required, NumberRange


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class Coewebsite(FlaskForm):
    FACULTY_FIRST_NAME = StringField(labels['FACULTY_FIRST_NAME'], validators=[DataRequired()])
    FACULTY_LAST_NAME = StringField(labels['FACULTY_LAST_NAME'], validators=[DataRequired()])
    FACULTY_UNIQNAME = StringField(labels['FACULTY_UNIQNAME'], validators=[DataRequired()])

    EFFECTIVE_TERM_KEY = SelectField(labels['EFFECTIVE_TERM_KEY'], coerce=int, validators=[DataRequired()])
    EFFECTIVE_YEAR = IntegerField(labels['EFFECTIVE_YEAR'], validators=[DataRequired(), NumberRange(2000, 3000, "Effective year must be in the 21st century.")])
    TERMS_OFFERED = MultiCheckboxField(labels['TERMS_OFFERED'], coerce=int, validators=[DataRequired()])

    CATALOG_NUMBER = IntegerField(labels['CATALOG_NUMBER'], validators=[DataRequired()])
    CROSS_LISTINGS_TEXT = StringField(labels['CROSS_LISTINGS_TEXT'], validators=[Optional()])
    COURSE_TITLE = StringField(labels['COURSE_TITLE'], validators=[DataRequired()])
    ABBREVIATED_TITLE = StringField(labels['ABBREVIATED_TITLE'], validators=[Optional()])
    COURSE_DESCRIPTION_TEXT = TextAreaField(labels['COURSE_DESCRIPTION_TEXT'], validators=[DataRequired()])
    ENFORCED_PREREQUISITES_TEXT = StringField(labels['ENFORCED_PREREQUISITES_TEXT'], validators=[Optional()])
    ADVISED_PREREQUISITES_TEXT = StringField(labels['ADVISED_PREREQUISITES_TEXT'], validators=[Optional()])
    INSTRUCTOR_CONSENT_ALWAYS_REQUIRED_INDICATOR = BooleanField(labels['INSTRUCTOR_CONSENT_ALWAYS_REQUIRED_INDICATOR'])
    MINIMUM_GRADE_REQUIRED_KEY = RadioField(labels['MINIMUM_GRADE_REQUIRED_KEY'], coerce=int, validators=[Optional()])
    CREDIT_EXCLUSIONS_TEXT = StringField(labels['CREDIT_EXCLUSIONS_TEXT'], validators=[Optional()])
    CLASS_LENGTH_KEY = RadioField(labels['CLASS_LENGTH_KEY'], coerce=int, validators=[DataRequired()])

    CREDIT_TYPES = MultiCheckboxField(labels['CREDIT_TYPES'], coerce=int, validators=[DataRequired()])
    MINIMUM_CREDIT_HOURS = IntegerField(labels['MINIMUM_CREDIT_HOURS'], validators=[Optional()])
    MAXIMUM_CREDIT_HOURS = IntegerField(labels['MAXIMUM_CREDIT_HOURS'], validators=[Optional()])
    COURSE_REPEATABLE_CREDIT_INDICATOR = BooleanField(labels['COURSE_REPEATABLE_CREDIT_INDICATOR'])
    MAXIMUM_NUMBER_REPEATABLE_CREDITS = IntegerField(labels['MAXIMUM_NUMBER_REPEATABLE_CREDITS'], validators=[Optional()])
    MORE_THAN_ONCE_SAME_TERM_INDICATOR = BooleanField(labels['MORE_THAN_ONCE_SAME_TERM_INDICATOR'])
    Y_GRADE_ALLOWED_INDICATOR = BooleanField(labels['Y_GRADE_ALLOWED_INDICATOR'])

    # fills website_COURSE_COMPONENTS table
    COURSE_COMPONENTS = MultiCheckboxField(labels['COURSE_COMPONENTS'], coerce=int, validators=[DataRequired()])
    GRADED_COMPONENTS = MultiCheckboxField(labels['GRADED_COMPONENTS'], coerce=int, validators=[DataRequired()])
    CONTACT_HOURS_LECTURE = IntegerField(labels['CONTACT_HOURS_LECTURE'], validators=[Optional()])
    CONTACT_HOURS_RECITATION = IntegerField(labels['CONTACT_HOURS_RECITATION'], validators=[Optional()])
    CONTACT_HOURS_LAB = IntegerField(labels['CONTACT_HOURS_LAB'], validators=[Optional()])

    GRADING_BASIS_KEY = RadioField(labels['GRADING_BASIS_KEY'], coerce=int, validators=[DataRequired()])
    SUBMITTED_BY_KEY = RadioField(labels['SUBMITTED_BY_KEY'], coerce=int, validators=[DataRequired()])
    DEGREE_REQUIREMENTS_DESCRIPTION_TEXT = TextAreaField(labels['DEGREE_REQUIREMENTS_DESCRIPTION_TEXT'], validators=[Optional()])

    ABET_OUTCOMES = MultiCheckboxField(labels['ABET_OUTCOMES'], coerce=int, validators=[Optional()])

    SPECIAL_RESOURCES_TEXT = TextAreaField(labels['SPECIAL_RESOURCES_TEXT'], validators=[Optional()])
    SUPPORTING_STATEMENT_TEXT = TextAreaField(labels['SUPPORTING_STATEMENT_TEXT'], validators=[DataRequired()])
    submit = SubmitField('Submit')


# inherit from Coewebsite
class NonCoewebsite(Coewebsite):
    NONCOE_HOME_SUBJECT = StringField(labels['NONCOE_HOME_SUBJECT'], validators=[DataRequired()])

class ModifyCoeCourse(Coewebsite):
    COE_HOME_SUBJECT_KEY = SelectField(labels['COE_HOME_SUBJECT_KEY'], coerce=int)

class ModifyNonCoeCourse(NonCoewebsite):
    COE_HOME_SUBJECT_KEY = SelectField(labels['COE_HOME_SUBJECT_KEY'], coerce=int)


class UpdateRequestStatus(FlaskForm):
    DEPARTMENT_STATUS_KEY = SelectField(labels['DEPARTMENT_STATUS_KEY'], coerce=int, validators=[Optional()])
    COLLEGE_STATUS_KEY = SelectField(labels['COLLEGE_STATUS_KEY'], coerce=int, validators=[Optional()])
    REGISTRAR_STATUS_KEY = SelectField(labels['REGISTRAR_STATUS_KEY'], coerce=int, validators=[Optional()])
    submit = SubmitField('Submit')
