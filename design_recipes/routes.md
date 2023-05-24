{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE


# User story
As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

# Home route
GET /home



# Submit message route
POST /submit
  name: string
  message: string
2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
Bob peeped: Peep 1
"""
Jill peeped: Peep 2 


# POST /submit
#  Parameters:
#    name: Emma
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you peeped: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""

# GET /home
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Bob peeped: Peep 1
"""
Jill peeped: Peep 2 
"""
Emma peeped: Hello world
"""
3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'