import express from 'express';
import Event from '../models/Event.js';

const router = express.Router();

// GET /api/events - list all events
router.get('/', async (req, res) => {
  try {
    const events = await Event.find().sort({ date: 1 });
    res.json(events);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Server error' });
  }
});

// POST /api/events - create a new event
router.post('/', async (req, res) => {
  try {
    const { title, date, description } = req.body;
    const newEvent = new Event({ title, date, description });
    await newEvent.save();

    // TODO: send reminder email using nodemailer or another service

    res.status(201).json(newEvent);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Server error' });
  }
});

export default router;