# Python standard library
import os

# SQL
import sqlalchemy
import sqlalchemy_utils
import psycopg2

# Flask
import flask




app = flask.Flask(__name__) # create the application instance :)





'''
Data base
'''

# Preliminaries
username = 'postgres'
password = 'password'
host = 'localhost'
port = '5432'
db_name = 'permits'

engine = sqlalchemy.create_engine('postgresql://{}:{}@{}:{}/{}'.format(username, password, host, port, db_name))


# Create database
if not sqlalchemy_utils.database_exists(engine.url):
    sqlalchemy_utils.create_database(engine.url)

# Conect to database and get a cursor
db_connection = psycopg2.connect(database = db_name, user = username, password = password, host = host)
db_cursor = db_connection.cursor()

# Create tables
db_cursor.execute(
"""CREATE TABLE IF NOT EXISTS firewatch (
  job_id text primary key,
  fire_risk text,
  firewatch_first text,
  firewatch_last text,
  extinguish_equip_avail text,
  equip_inspct text,
  firewatch_trained text,
  firewatch_other_duties text
);
"""
)





# Commit
db_connection.commit()







@app.route('/')
def get_index():
    return flask.render_template('index.html')




@app.route('/heavylift', methods=['GET', 'POST'])
def get_heavylift():

    # Get method type
    method = flask.request.method

    # Get form
    if method == 'GET':
        return flask.render_template('heavylift.html', form_type = 'heavylift')

    elif method == 'POST':
        data = flask.request.form

        post_permit_to_database(flask.request.form, 'heavylift')
        return flask.redirect('/', code=302)


@app.route('/firewatch', methods=['GET', 'POST'])
def get_firewatch():
    # Get method type
    method = flask.request.method

    # Get form
    if method == 'GET':
        job_id = get_new_job_id()
        return flask.render_template('firewatch.html', form_type = 'firewatch', job_id = job_id)

    elif method == 'POST':
        data = flask.request.form

        post_permit_to_database(flask.request.form, 'firewatch')
        return flask.redirect('/', code=302)


@app.route('/database')
def get_database():

    command = """
    SELECT * FROM firewatch;
    """

    db_cursor.execute(command)
    data = db_cursor.fetchall()

    print(data)

    return flask.render_template('database.html', data = data)

def get_new_job_id():

    command = """
    SELECT job_id FROM firewatch;
    """


    db_cursor.execute(command)
    job_ids = db_cursor.fetchall()

    if job_ids == []:
        new_job_id = '000000000'

    else:
        job_ids = [int(job_id[0]) for job_id in job_ids]
        job_ids.sort()
        last_job_id = job_ids[-1]
        new_job_id = str(last_job_id + 1).zfill(9)


    return new_job_id




def post_permit_to_database(form, form_type):
    success = False

    if form_type == 'firewatch':

        # job_id <==> JobID
        if 'JobID' in form.keys():
            job_id = form['JobID']
        else:
            job_id = '-1'

        # fire_risk <==> field_0
        if 'field_0' in form.keys():
            fire_risk = form['field_0']
        else:
            fire_risk = '-1'

        # firewatch_first <==> field_0_0_FirstName
        if 'field_0_0_FirstName' in form.keys():
            firewatch_first = form['field_0_0_FirstName']
        else:
            firewatch_first = '-1'
        if firewatch_first == '':
            firewatch_first = '-1'

        # firewatch_last <==> field_0_0_LastName
        if 'field_0_0_LastName' in form.keys():
            firewatch_last = form['field_0_0_LastName']
        else:
            firewatch_last = '-1'
        if firewatch_last == '':
            firewatch_last = '-1'

        # extinguish_equip_avail <==> field_0_1
        if 'field_0_1' in form.keys():
            extinguish_equip_avail = form['field_0_1']
        else:
            extinguish_equip_avail = '-1'

        # equip_inspct <==> field_0_1_0
        if 'field_0_1_0' in form.keys():
            equip_inspct = form['field_0_1_0']
        else:
            equip_inspct = '-1'

        # firewatch_trained <==> field_0_1_1
        if 'field_0_1_1' in form.keys():
            firewatch_trained = form['field_0_1_1']
        else:
            firewatch_trained = '-1'

        # firewatch_other_duties <==> field_0_2
        if 'field_0_2' in form.keys():
            firewatch_other_duties = form['field_0_2']
        else:
            firewatch_other_duties = '-1'

        #(job_id, fire_risk, firewatch_first, firewatch_last, extinguish_equip_avail, equip_inspct, firewatch_trained, firewatch_other_duties)
        command = f'''
        INSERT INTO firewatch (job_id, fire_risk, firewatch_first, firewatch_last, extinguish_equip_avail, equip_inspct, firewatch_trained, firewatch_other_duties)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''




        db_cursor.execute(command, (job_id, fire_risk, firewatch_first, firewatch_last, extinguish_equip_avail, equip_inspct, firewatch_trained, firewatch_other_duties))
        db_connection.commit()
