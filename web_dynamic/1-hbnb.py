#!/usr/bin/python3
""" Starts a Flash Web Application """
import os
import uuid
from flask import Flask, render_template

from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove SQLAlchemy Session """
    storage.close()


@app.route('/1-hbnb', strict_slashes=False)
def hbnb():
    """ hbnb is live """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)
    ctxt = {
        'states': st_ct,
        'amenities': amenities,
        'places': places,
        'cache_id': uuid.uuid4()
    }
    return render_template('1-hbnb.html', **ctxt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
