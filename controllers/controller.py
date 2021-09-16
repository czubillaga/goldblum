from flask import render_template, request
from app import app
from models.event_list import delete_event, events, add_event, delete_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/events', methods=['POST'])
def add_new_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_location = request.form['room_location']
    event_guests = request.form['number_of_guests']
    event_description = request.form['description']
    event_recurring = bool(request.form['recurring'])
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring)
    add_event(new_event)
    return render_template('index.html', title="Home", events=events)

@app.route('/events/<index>')
def show_event(index):
    return render_template('event.html', title="Event", events=events, index=int(index))

@app.route('/events/delete/<index>')
def delete_event_by_index(index):
    event = events[int(index)]
    delete_event(event)
    return render_template('index.html', title="Home", events=events)
