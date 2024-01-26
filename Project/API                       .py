# const express = require('express');
# const bodyParser = require('body-parser');

# const app = express();
# const port = 3000;

# // In-memory storage for simplicity (replace with a database in a real application)
# const users = [
#   { username: 'user1', password: 'password1' },
#   { username: 'user2', password: 'password2' },
# ];

# const loggedInUsers = {};

# app.use(bodyParser.json());

# // Login endpoint
# app.post('/login', (req, res) => {
#   const { username, password } = req.body;

#   // Check if the user exists
#   const user = users.find(u => u.username === username && u.password === password);

#   if (user) {
#     // Store the user as logged in
#     loggedInUsers[username] = true;
#     res.json({ message: 'Login successful' });
#   } else {
#     res.status(401).json({ message: 'Invalid credentials' });
#   }
# });

# // Logoff endpoint
# app.post('/logoff', (req, res) => {
#   const { username } = req.body;

#   // Check if the user is logged in
#   if (loggedInUsers[username]) {
#     // Log the user off
#     delete loggedInUsers[username];
#     res.json({ message: 'Logoff successful' });
#   } else {
#     res.status(401).json({ message: 'User not logged in' });
#   }
# });

# app.listen(port, () => {
#   console.log(`Server is running at http://localhost:${port}`);
# });
