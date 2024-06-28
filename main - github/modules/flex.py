from flask import Flask, render_template, request, redirect, session, url_for
from env import user1

class login_system():

    def __init__(self):
        pass

    def new_login(self, id, password):

        self.id = id
        self.password = password

        if id == user1.id and password==user1.password :
            return 1
        else:
            return 0