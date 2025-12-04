# Event Management Web Application

This project is a **full‑stack web application** designed to streamline event planning for university clubs and organisations. Built with a modern JavaScript stack (React, Node.js, Express, and MongoDB), it provides functionality for creating events, registering participants, and sending automated reminder emails.

## Overview

In 2025 I developed an event management platform as part of a university initiative. The original system reduced administrative overhead by **40 %** thanks to automated scheduling, registration, and email notifications. It also employed continuous integration and deployment (CI/CD) via GitHub Actions and deployed on Amazon Web Services (AWS) using EC2 and RDS.

This repository contains a minimal example demonstrating the core architecture without linking to actual AWS services. The client side is a single‑page React app, while the server side uses Express and Mongoose. The skeleton can be extended into a fully functional application.

## Structure

```text
event-management-web-app/
├── README.md                ← Project documentation (this file)
├── client/                  ← React front‑end
│   ├── package.json         ← Client dependencies and scripts
│   ├── public/
│   │   └── index.html       ← HTML template
│   └── src/
│       ├── App.js           ← Main React component
│       └── index.js         ← Entry point
└── server/                  ← Node.js/Express back‑end
    ├── package.json         ← Server dependencies and scripts
    ├── server.js            ← Express application
    ├── models/
    │   └── Event.js         ← Mongoose model for events
    └── routes/
        └── events.js        ← API endpoints for event operations
```

## Getting Started

1. **Install dependencies**: Navigate to the `client` and `server` directories separately and run `npm install` to install the required packages. Ensure you have Node.js (v16+) and npm installed.
2. **Run the client and server**: In two separate terminal windows:
   - Front‑end: `cd client && npm start` — this starts the React development server on [http://localhost:3000](http://localhost:3000).
   - Back‑end: `cd server && npm run dev` — this starts the Express server using nodemon on [http://localhost:5000](http://localhost:5000).
3. **Connect to MongoDB**: The server skeleton expects a `MONGODB_URI` environment variable. You can create a local MongoDB instance or use a cloud service (e.g., MongoDB Atlas) for testing.

## Features

* **Create and manage events** — users can create new events with a title, description, date, and capacity.
* **Event registration** — participants can sign up for events; the server stores registrations in MongoDB.
* **Automated emails** — a stub function demonstrates where to implement email reminders; integrate with an email service provider (e.g., SendGrid) to send real emails.
* **Responsive design** — the React app uses basic Bootstrap styling (optional) to ensure a usable interface across devices.

## Extending This Project

This skeleton lays the foundation for a more robust application. To take it further, consider implementing:

* Authentication with JWT or OAuth to secure event management features.
* Advanced scheduling features, such as repeating events and calendar integration.
* A real email service (e.g., nodemailer with Gmail API, SendGrid, or AWS SES) for notifications.
* Deployment using AWS EC2 (with Nginx reverse proxy) and a managed database like RDS or Atlas.

## License

This example is provided for educational purposes and is released under the MIT License. You may use it as a starting point for your own projects.
