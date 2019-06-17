# cd Assignments
# cd Website_With_Database
# python -m flask run

from flask import Flask, render_template, request
import pyodbc
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['POST'])
def showindexpage():
    global conn, cursor
    # Connection to DB.
    conn = pyodbc.connect(Trusted_Connection='yes',
                          driver='{SQL Server}',
                          server='CHRISTOFFER-PC',
                          database='car_db')
    # Creates a list/table for our data with DB connection.
    cursor = conn.cursor()

    if request.method == 'POST':
        if request.form['myaction'] == "Create car":
            addcar()
        elif request.form['myaction'] == "Update car":
            updatecar()
        else:
            deletecar()

    # Shows a list of all the cars.
    # SQL statement; saves data to our list from DB.
    cursor.execute("SELECT * FROM car")
    allcars = cursor.fetchall()  # Fetch all the rows one at a time.

    # Show the cars with the fastest speed.
    # SQL statement; saves data to our list from DB.
    cursor.execute("SELECT * FROM car ORDER BY car_max_speed DESC")
    fastestcar = cursor.fetchone()  # Fetch only one row.

    conn.close()  # Close connection.
    return render_template('index.html', carlist=allcars, carspeed=fastestcar)
#####################

# Create car function.


def addcar():
    try:
        # Defines variables that will hold data for a car.
        carmodel = request.form['model']
        carmaxspeed = request.form['speed']

        # ?; is a substitude for our defined variables.
        cursor.execute(
            "INSERT INTO car(car_model, car_max_speed) VALUES(?, ?)", carmodel, carmaxspeed)
        # Remember to commit all changes else the data won't be saved.
        conn.commit()
    except Exception as ex:
        print("There was an error : ", ex)

#####################

# Update car function.


def updatecar():
    try:
        # Defines variables that will hold data for a car.
        carid = request.form['id']
        carmodel = request.form['model']
        carmaxspeed = request.form['speed']

        # Remember the WHERE.
        cursor.execute(
            "UPDATE Car SET car_model = ?, car_max_speed = ? WHERE car_id = ?",
            carmodel, carmaxspeed, carid)
        # Remember to commit all changes else the data won't be saved.
        conn.commit()
    except Exception as ex:
        print("There was an error : ", ex)

#####################

# Delete car function.


def deletecar():
    try:
        # Defines a variable to store the ID for a specific car.
        carid = request.form['id']

        # Remember the WHERE; else it deletes all the Cars.
        cursor.execute("DELETE FROM car WHERE car_id = ?", carid)
        # Remember to commit all changes else the data won't be saved.
        conn.commit()
    except Exception as ex:
        print("There was an error : ", ex)

#####################


# Run the application server on localhost: 4449;
# set it on properties - debug - portnumber.
# If we are a stand alone program, then run this application.
if __name__ == '__main__':
    app.run('localhost', 5000)
