from marshmallow import fields
from nails import Serializer

class RegisterSerializer(Serializer):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class LoginSerializer(Serializer):
    email = fields.Email(required=True)
    password = fields.Str(required=True)