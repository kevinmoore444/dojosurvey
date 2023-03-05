from mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.yourname = data['yourname']
        self.dojolocation = data['dojolocation']
        self.favoritelanguage = data['favoritelanguage']
        self.comment = data['comment']

    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO dojos (name,location,language,comments)
            VALUES (%(yourname)s,%(dojolocation)s,%(favoritelanguage)s,%(comment)s);
        """
        return connectToMySQL("dojo_survey_schema").query_db(query,data)

    @staticmethod
    def validator(potential_survey):
        is_valid = True
        if len(potential_survey['yourname']) < 1:
            is_valid = False
            flash("Name required")
        if len(potential_survey['comment']) < 1:
            is_valid = False
            flash("Comment required")
        return is_valid