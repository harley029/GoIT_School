from mongoengine import (
    Document,
    StringField,
    BooleanField
)


class Contact(Document):
    full_name = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)
    phone_number = StringField(max_length=22)
    preferred_contact_method = StringField(choices=["SMS", "Email"], default="Email")
    message_sent = BooleanField(default=False)