from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UnicodeSetAttribute


class JobOffer(Model):
    class Meta:
        table_name = 'jobs'
        region = 'us-east-1'

    hash = UnicodeAttribute(hash_key=True)
    url = UnicodeAttribute()
    position = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=True)
    company = UnicodeAttribute()
    date = UnicodeAttribute()
    tags = UnicodeSetAttribute(null=True)
