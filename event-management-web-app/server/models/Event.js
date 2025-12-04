import mongoose from 'mongoose';

const eventSchema = new mongoose.Schema(
  {
    title: { type: String, required: true },
    date: { type: Date, required: true },
    description: { type: String },
    createdAt: { type: Date, default: Date.now },
  },
  { collection: 'events' }
);

export default mongoose.model('Event', eventSchema);