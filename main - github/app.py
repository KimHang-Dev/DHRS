from flask import Flask, render_template, request, redirect, session, url_for
from env import user1
from modules.flex import login_system

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'

# user1(id = "dongguk1004", password = "ddbk23_205")

# KAKAO_API_KEY = 'ebc5ee6ed10cd99a2859d7d136b65bbd'

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('main'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        kras_login_system=login_system()

        admin_id = request.form['id']
        admin_password = request.form['password']
        print(admin_id, admin_password)

        user_login=kras_login_system.new_login(admin_id,admin_password)
        
        if(user_login==1):
            session['user_id'] = admin_id
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error='Invalid credentials. Please try again.')

    return render_template('login.html')

@app.route('/main')
def main():
    if 'user_id' in session:
        return render_template('index.html', username=session['user_id'])
    
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/charts')
def charts():

    if 'user_id' in session:
        return render_template('charts.html', username=session['user_id'])
    
    else:
        return redirect(url_for('login'))

@app.route('/map')
def map():

    if 'user_id' in session:
        return render_template('map.html', username=session['user_id'])
    
    else:
        return redirect(url_for('login'))
    
@app.route('/egg')
def egg():

    if 'user_id' in session:
        return render_template('egg.html', username=session['user_id'])
    
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5133)