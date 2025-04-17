const express = require('express');
const app = express();

const hostname = '127.0.0.1';
const port = 3000;

// Route handler for root path
app.get('/', (req, res) => {
  res.status(200).contentType('text/plain').send('Hello, World!');
});

// Route handler for alternate path
app.get('/good-evening', (req, res) => {
  res.status(200).contentType('text/plain').send('Good evening');
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});