# -*- coding: utf-8 -*-

from app import app, base_config, db_conn

from flask import Response, session, render_template, request, redirect, jsonify
from werkzeug.routing import BaseConverter

from hashids import Hashids


class RegexConverter(BaseConverter):

    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter


# This function should eventually be replaced to avoid getting
# more data than we actually need
def psql_query(query, args=None, include_columns=False):
    cursor = db_conn.cursor()
    if args is not None:
        cursor.execute(query, args)
    else:
        cursor.execute(query)

    if include_columns:
        return ([desc[0] for desc in cursor.description], cursor.fetchall())
    else:
        return cursor.fetchall()

@app.route('/')
def index():

    if 'filter_id' in session:
        filter_id = session["filter_id"]
        del session["filter_id"]
        return render_template("index.html", config=base_config,
                               filter_id=filter_id)
    else:
        return render_template("index.html", config=base_config, filter_id="")
