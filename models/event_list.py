from models.event import Event

event_1 = Event('2021-09-16', 'Jeff Goldblum Live', 20000, 'Madison Square Garden', 'Amazing entertainment', False)
event_2 = Event('2021-09-17', 'Chaos Theory', 20, "Jeff's House", 'How chaos theory applies to dinosaurs', False)

events = [event_1, event_2]

def add_event(event):
    events.append(event)

def delete_event(event):
    events.remove(event)