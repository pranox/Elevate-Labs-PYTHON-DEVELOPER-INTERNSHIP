from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = data
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<string:username>', methods=['PUT'])
def update_user(username):
    data = request.json
    if username not in users:
        return jsonify({'message': 'User not found'}), 404
    users[username].update(data)
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    if username in users:
        del users[username]
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

