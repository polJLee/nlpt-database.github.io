from flask import Flask, render_template, request
import os


# Defined Globals
TEMPLATE_DIR = os.path.abspath('/Users/paullee/Library/Mobile Documents/com~apple~CloudDocs/Code/nlpt-database/templates')
STATIC_DIR = os.path.abspath('/Users/paullee/Library/Mobile Documents/com~apple~CloudDocs/Code/nlpt-database/templates/static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/search.html', methods=['POST', 'GET'])
def search_post():
  if request.method == 'POST':
    txt = request.form.get('search')
    return search_result(txt)
  return render_template('search.html')  

@app.route('/sundays.html')
def sundays():
  return render_template('sundays.html')

@app.route('/members.html')
def members():
  return render_template('members.html')

@app.route('/roster.html')
def roster():
  return render_template('roster.html')


@app.route('/search_result.html/', methods=['GET', 'POST'])
def search_result(txt):
  text = '''
  <!DOCTYPE html>
  <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <title>NLPT22</title>
        <!-- Css -->
        <link rel="stylesheet" href="{{ url_for('static',filename='bootstrap.css') }}">
        <link rel="stylesheet" href="{{ url_for('static',filename='style.css') }}">
    </head>
    <body>
        <nav class="navbar navbar-default navbar-fixed-top">
          <div class="col-md-12">
              <div class="nav">
                <button class="btn-nav">
                <span class="icon-bar inverted top"></span>
                <span class="icon-bar inverted middle"></span>
                <span class="icon-bar inverted bottom"></span>
                </button>
              </div>
              <a class="navbar-brand" href="http://127.0.0.1:5000/">
              <img class="logo" src="{{url_for('static', filename='logo.png')}}" alt="logo">
              </a>
              <div class="nav-content hideNav hidden">
                <ul class="nav-list vcenter">
                    <li class="nav-item"><a class="item-anchor" href="http://127.0.0.1:5000/index.html">Home</a></li>
                    <li class="nav-item"><a class="item-anchor" href="http://127.0.0.1:5000/search.html">Search</a></li>
                    <li class="nav-item"><a class="item-anchor" href="http://127.0.0.1:5000/sundays.html">Sundays</a></li>
                    <li class="nav-item"><a class="item-anchor" href="http://127.0.0.1:5000/members.html">Members</a></li>
                    <li class="nav-item"><a class="item-anchor" href="http://127.0.0.1:5000/roster.html">Roster</a></li>
                </ul>
              </div>
          </div>
        </nav>
        <!-- Header -->
  
        <div class="span12">
          <div class="col-md-6 no-gutter text-center fill">
              <br>
              <br>
              <br>
              <br>
              <br>
              <br> 
              <h2 class="center">Search</h2>
              <br> 
              <br>
              <br>
          </div>
          <div class="col-md-6 no-gutter text-center">
              <div id="header" data-speed="2" data-type="background">
                <div id="headslide" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner" role="listbox">
                      <div class="item active">
                          <img src="{{url_for('static',filename='search.jpg')}}" alt="Slide">
                      </div>
                    </div>
                </div>
              </div>
          </div>
        </div>
        <div style="clear:both;"></div>
        <!-- script -->
        <script src="{{url_for('static',filename='jquery.js') }}"> </script>
        <script src="{{url_for('static',filename='bootstrap.min.js') }}"> </script> 
        <script src="{{url_for('static',filename='menu-color.js') }}"> </script>
        <script src="{{url_for('static',filename='modernizer.js') }}"> </script>
        <script src="{{url_for('static',filename='script.js') }}"> </script>
    </body>
  </html>
  '''
  
  with open('/Users/paullee/Library/Mobile Documents/com~apple~CloudDocs/Code/nlpt-database/templates/search_result.html', 'w', encoding='utf-8') as f:
    f.write(text)
    f.close()

  return render_template('search_result.html')

if __name__ == '__main__':
  # bootstrap = Bootstrap(app)
  app.run(debug=True)