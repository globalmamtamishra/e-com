import tornado.web
import json
from models.user import User


class UserHandler(tornado.web.RequestHandler):

    # POST: Create a new user
    def post(self):
        try:
            data = json.loads(self.request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            if not username or not password or not email:
                self.set_status(400)
                self.write({"status": "error", "message": "Missing required parameters"})
                return

            User.create(username, password, email)
            self.write({"status": "success", "message": "User created successfully"})
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"status": "error", "message": "Invalid JSON"})

    # GET: Retrieve user information
    def get(self, user_id=None):
        if user_id:
            user = User.get_by_id(user_id)
            if user:
                self.write({"status": "success", "data": user})
            else:
                self.set_status(404)
                self.write({"status": "error", "message": "User not found"})
        else:
            users = User.get_all()
            self.write({"status": "success", "data": users})

    # PUT: Update user information
    def put(self, user_id):
        try:
            data = json.loads(self.request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            if not username and not password and not email:
                self.set_status(400)
                self.write({"status": "error", "message": "At least one field must be provided for update"})
                return

            updated = User.update(user_id, username, password, email)
            if updated:
                self.write({"status": "success", "message": "User updated successfully"})
            else:
                self.set_status(404)
                self.write({"status": "error", "message": "User not found"})
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"status": "error", "message": "Invalid JSON"})

    # DELETE: Delete a user
    def delete(self, user_id):
        deleted = User.delete(user_id)
        if deleted:
            self.write({"status": "success", "message": "User deleted successfully"})
        else:
            self.set_status(404)
            self.write({"status": "error", "message": "User not found"})