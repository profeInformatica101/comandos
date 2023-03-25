from flask import Flask, request
from djitellopy import Tello
import threading

app = Flask(__name__)
tello = Tello()

@app.route('/control', methods=['POST'])
def control():
    direction = request.form.get('direction')
    if direction == 'forward':
        tello.move_forward(20)
    elif direction == 'backward':
        tello.move_backward(20)
    elif direction == 'left':
        tello.move_left(20)
    elif direction == 'right':
        tello.move_right(20)
    return 'OK'

if __name__ == '__main__':
    tello.connect()
    tello.streamon()
    threading.Thread(target=tello.stream).start()
    app.run(host='0.0.0.0', port=5000)
