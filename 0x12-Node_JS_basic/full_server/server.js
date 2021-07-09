const express = require('express');
const router = require('./routes/index');

const app = express();
const PORT = 1245;

const URLPREFIX = '/';

app.use(URLPREFIX, router);

app.listen(PORT, () => {
  console.log(`Listening at http://localhost:${PORT}`);
});

module.exports = app;
