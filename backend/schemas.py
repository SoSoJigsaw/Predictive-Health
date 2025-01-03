from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "medico", "paciente"]))
    cpf = fields.Int(required=True, validate=validate.Length(max=11))

class ConsentSchema(Schema):
    consent_status = fields.Boolean(required=True, error_messages={"required": "Consent status is required"})
