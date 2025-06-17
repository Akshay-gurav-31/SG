from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        flash("Thank you for contacting us!", "success")
        return redirect("/")
    return render_template("index.html")


@app.route("/piano")
def piano():
    return render_template("piano.html")

@app.route("/guitar")
def guitar():
    return render_template("guitar.html")

@app.route("/vocal")
def vocal():
    return render_template("vocal.html")

@app.route("/Enroll")
def enroll():
    return render_template("Enroll.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Placeholder for storing user data (replace with database logic)
        print(f"New user: {name}, {email}")

        flash('Account created successfully!', 'success')
        return redirect('/')  # Redirect to the home page after signup
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(f"Attempting login with email: {email} and password: {password}")

        # Placeholder: ANY credentials are valid
        print("Login successful!")
        session['email'] = email
        flash('Login successful!', 'success')
        return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home_page():
    email = session.get('email')
    if not email:
        return redirect('/login')
    return render_template('home.html', email=email)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

@app.route('/check_session')
def check_session():
    email = session.get('email')
    return {'email': email}

@app.route('/dashboard')
def dashboard():
    email = session.get('email')
    if not email:
        return redirect('/login')
    return render_template('dashboard.html')

@app.route('/my_courses')
def my_courses():
    email = session.get('email')
    if not email:
        return redirect('/login')
    return render_template('my_courses.html')

@app.route('/profile')
def profile():
    email = session.get('email')
    if not email:
        return redirect('/login')
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
