from marshmallow import fields, Schema

class TodoGetSchema(Schema):
    id = fields.Int()

class TodoDisplay(Schema):
    sno = fields.Int()
    title = fields.String(required=True)
    description = fields.String(required=True)

class TodoPostSchema(Schema):
    todo = fields.String(required=True)
    description = fields.String(required=True)

class TodoPutIdSchema(Schema):
    id = fields.Int(required=True)

class TodoPutSchema(Schema):
    todo = fields.String(required=True)
    description = fields.String(required=True)

class TodoMessage(Schema):
    msg = fields.String(required = True)