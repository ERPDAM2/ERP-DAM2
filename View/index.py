#! /usr/bin/env python
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# -*- coding: utf-8 -*-

from flask import Flask, render_template,redirect, url_for

index = Flask(__name__)

@index.route('/')
def Index():
    return render_template('index.html')

@index.route('/validator')
def validator():
    return redirect(url_for('Index'))

if __name__ == '__main__':
    index.run(port = 3000, debug = True)
