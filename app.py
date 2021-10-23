from flask import Flask, render_template

# # root route
# app = Flask(__name__)
# @app.route('/')
# def index():
#   """Return homepage."""
#   return render_template('home.html', msg='Flask is cool!!')

if __name__ == '__main__':
  app.run(debug=True)


# Mock array of projects
playlists = [
  {'title': 'Cat Videos', 'description': 'Cats being weird'},
  {'title': '80\'s Music', 'description': 'Don\'t stop believing!'}  
]

@app.route('/')
def playlists_index():
  """Show all playlists."""
  return render_template('playlists_index.html', playlists=playlists)