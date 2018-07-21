"""Helpers to be used in /views"""

from website.model import get_table, db
from sqlalchemy.sql import select, func


# NOTE this does the same thing as model.lookup_by_key but i like it's called fetch_subject
def fetch_subject(subject_id):
    """Fetch subject table by id."""
    subjects_table = get_table('COE_HOME_SUBJECTS')
    query = select([subjects_table]).\
            where(subjects_table.c.COE_HOME_SUBJECT_KEY == subject_id)
    return db.engine.execute(query).fetchone()


def fetch_website_summary(website_id):
    """Fetch website table by id and humanize foreign keys."""

    website_table = get_table("website")
    class_lengths_table = get_table("CLASS_LENGTHS")
    min_grade_table = get_table("MINIMUM_GRADES_REQUIRED")
    subjects_table = get_table("COE_HOME_SUBJECTS")
    abet_table = get_table("ABET_OUTCOMES")
    website_abet_table = get_table("website_ABET_OUTCOMES")

    j = website_table.\
        join(subjects_table, website_table.c.COE_HOME_SUBJECT_KEY == subjects_table.c.COE_HOME_SUBJECT_KEY).\
        join(class_lengths_table, website_table.c.CLASS_LENGTH_KEY == class_lengths_table.c.CLASS_LENGTH_KEY).\
        join(min_grade_table, website_table.c.MINIMUM_GRADE_REQUIRED_KEY == min_grade_table.c.MINIMUM_GRADE_REQUIRED_KEY).\
        join(website_abet_table, website_table.c.website_KEY == website_abet_table.c.website_KEY).\
        join(abet_table, website_abet_table.c.ABET_OUTCOME_KEY == abet_table.c.ABET_OUTCOME_KEY)

    cols = [website_table,
            subjects_table.c.COE_HOME_SUBJECT_DESCRIPTION,
            subjects_table.c.COE_HOME_SUBJECT,
            class_lengths_table.c.CLASS_LENGTH,
            min_grade_table.c.MINIMUM_GRADE_REQUIRED,
            func.group_concat(abet_table.c.ABET_OUTCOME).label("ABET_OUTCOMES")
            ]

    q = select(cols).select_from(j).where(website_table.c.website_KEY == website_id)

    x =  db.engine.execute(q).fetchone()
    return x
