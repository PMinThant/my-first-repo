def login_signup(username, password):
  # Check if username exists in the database
  if username in users:
    # Check if the password is correct
    if password == users[username]:
      # Login the user
      return True
    else:
      # Return an error message
      return "Incorrect password"
  else:
    # Create a new user account
    users[username] = password
    # Return a success message
    return "Successfully created new account"