import os
def upload_f(f):
    go = open(f, 'wb+')
    for chunk in f.chunks():
        go.write(chunk)