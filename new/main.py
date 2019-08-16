from project import app, db
from flask_restful import Resource, Api
from flask_restful import Api
from project.users.views import SendSerial
from project.admin.views import Login,Logout,PostProduct,GetProduct,GetPhone,Getby,Request

api = Api(app)


api.add_resource(SendSerial, '/SendSerial')

api.add_resource(Login, '/login-admin')
api.add_resource(Logout, '/logout-user')
api.add_resource(PostProduct, '/PostProduct')
api.add_resource(GetProduct, '/GetProduct')
api.add_resource(GetPhone, '/GetPhone')
api.add_resource(Getby, '/Getby')
api.add_resource(Request, '/Request')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

