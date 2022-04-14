# import the function that will return an instance of a connection
from flask_app.models import ninja
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos ORDER BY name;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of table
        dojos = []
        # Iterate over the db results and create instances of table with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_by_id(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        target_dojo = results[0]
        return target_dojo

    @classmethod
    def get_ninjas_at_dojo(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls( results[0] )
        for ninja_row in results:
            ninja_data = {
                "id": ninja_row["ninjas.id"],
                "first_name": ninja_row["first_name"],
                "last_name": ninja_row["last_name"],
                "age": ninja_row["age"],
                "dojo_id": ninja_row["dojo_id"],
                "created_at": ninja_row["ninjas.created_at"],
                "updated_at": ninja_row["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )
        return dojo