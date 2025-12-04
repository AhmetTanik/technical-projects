import React, { useEffect, useState } from 'react';

// Basic event form component
function EventForm({ onAdd }) {
  const [title, setTitle] = useState('');
  const [date, setDate] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newEvent = { title, date, description };
    onAdd(newEvent);
    setTitle('');
    setDate('');
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <h2>Create Event</h2>
      <div className="mb-3">
        <label htmlFor="title" className="form-label">Title</label>
        <input
          type="text"
          className="form-control"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="date" className="form-label">Date</label>
        <input
          type="date"
          className="form-control"
          id="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="description" className="form-label">Description</label>
        <textarea
          className="form-control"
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary">Add Event</button>
    </form>
  );
}

// Event list component
function EventList({ events }) {
  if (!events.length) return <p>No events yet.</p>;
  return (
    <div>
      <h2>Upcoming Events</h2>
      <ul className="list-group">
        {events.map((evt, idx) => (
          <li key={idx} className="list-group-item">
            <strong>{evt.title}</strong> — {evt.date}<br />
            <small>{evt.description}</small>
          </li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Load existing events from the API
    const fetchEvents = async () => {
      try {
        const res = await fetch('http://localhost:5000/api/events');
        const data = await res.json();
        setEvents(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchEvents();
  }, []);

  const addEvent = async (evt) => {
    try {
      const res = await fetch('http://localhost:5000/api/events', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(evt),
      });
      const newEvent = await res.json();
      setEvents((prev) => [...prev, newEvent]);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="container py-4">
      <h1>Event Management App</h1>
      <EventForm onAdd={addEvent} />
      <EventList events={events} />
    </div>
  );
}

export default App;