from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html', company_name='portifolio')


@app.route("/projects")
def projects():
  # You can pass different parameters if needed, or render a different template
  return render_template('projects.html', company_name='projects')


@app.route("/aboutme")
def aboutme():
  # You can pass different parameters if needed, or render a different template
  return render_template('aboutme.html', company_name='about me')


@app.route("/contact")
def contact():
  # You can pass different parameters if needed, or render a different template
  return render_template('contact.html', company_name='contact me')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
