# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of table
        ninjas = []
        # Iterate over the db results and create instances of table with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s,NOW(),NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

