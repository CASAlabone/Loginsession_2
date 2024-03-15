document.getElementById('login-form').addEventListener('submit', function(event) {
  event.preventDefault();
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  // Perform login validation here
  // For demonstration, simply log the credentials
  console.log('Username: ' + username);
  console.log('Password: ' + password);
});

