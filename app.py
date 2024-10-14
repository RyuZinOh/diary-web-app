from flask import Flask, render_template, request, redirect, session, flash
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') 
client = MongoClient(os.getenv('MONGODB_URI')) 
db = client['the_diary']
users_collection = db['users']
entries_collection = db['user_mania']

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect('/diary')
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            flash('Username already exists. Please choose another one.')
        else:
            users_collection.insert_one({'username': username, 'password': password})
            flash('Registration successful! You can log in now.')
            return redirect('/login')
    return render_template('register.html')

@app.route('/diary', methods=['GET', 'POST'])
def diary():
    if 'username' not in session:
        return redirect('/login')
    if request.method == 'POST':
        entry_content = request.form['entry']
        entry = {
            'username': session['username'],
            'content': entry_content,
            'timestamp': datetime.now()
        }
        entries_collection.insert_one(entry)
        flash('Diary entry saved!')
    entries = entries_collection.find({'username': session['username']})
    return render_template('diary.html', username=session['username'], entries=entries)

@app.route('/delete_entry/<entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entries_collection.delete_one({'_id': ObjectId(entry_id)})
    flash('Diary entry deleted.')
    return redirect('/diary')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'username' not in session:
        return redirect('/login')
    if request.method == 'POST':
        new_password = request.form['new_password']
        users_collection.update_one({'username': session['username']}, {'$set': {'password': new_password}})
        flash('Password updated successfully!')
    return render_template('settings.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
