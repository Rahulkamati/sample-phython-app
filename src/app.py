
from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return 'Hello World'

if __name__ == '__main__':
    app.run()




#'/api/v1/details'
# 'api/v1/healthz'