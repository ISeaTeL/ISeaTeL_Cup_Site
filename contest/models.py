# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
# Create your models here.

class Clarification(models.Model):
    cid = models.IntegerField()
    asker = models.TextField()
    question = models.TextField()
    reply = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    def __unicode__(self):
        return 'question: ' + self.question + ' | reply: ' + self.reply + ' @' + str(self.time.date())


class Contest(models.Model):
    cid = models.IntegerField(unique=True)
    problem_url = models.TextField()
    scoreboard_url = models.TextField()
    solution_url = models.TextField()
    signup_url = models.TextField()
    date = models.TextField()
    title = models.TextField()
    content = models.TextField()
    STATUS = (
        ('incoming', 'incoming'),
        ('running', 'running'),
        ('ended', 'ended'),
    )
    status = models.TextField(choices=STATUS)
    def __unicode__(self):
        return 'cid: ' + str(self.cid) + '| date: ' + self.date

class SignUp(models.Model):
    nthu_oj_id = models.TextField()
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    cid = models.IntegerField()
    def __unicode__(self):
        return 'oj_id: ' + str(self.nthu_oj_id) + '| time: ' + str(self.time)



class Feedback(models.Model):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    cid = models.IntegerField()
    def __unicode__(self):
        return 'cid ' + str(self.cid) + '| time: ' + str(self.time)



# Dictionary Helper Models

class Dictionary(models.Model):
    """A model that represents a dictionary. This model implements most of the dictionary interface,
    allowing it to be used like a python dictionary.

    """
    name = models.CharField(max_length=255)

    @staticmethod
    def getDict(name):
        """Get the Dictionary of the given name.

        """
        df = Dictionary.objects.select_related().get(name=name)

        return df

    def __getitem__(self, key):
        """Returns the value of the selected key.

        """
        return self.keyvaluepair_set.get(key=key).value

    def __setitem__(self, key, value):
        """Sets the value of the given key in the Dictionary.

        """
        try:
            kvp = self.keyvaluepair_set.get(key=key)

        except KeyValuePair.DoesNotExist:
            KeyValuePair.objects.create(container=self, key=key, value=value)

        else:
            kvp.value = value
            kvp.save()

    def __delitem__(self, key):
        """Removed the given key from the Dictionary.

        """
        try:
            kvp = self.keyvaluepair_set.get(key=key)

        except KeyValuePair.DoesNotExist:
            raise KeyError

        else:
            kvp.delete()

    def __len__(self):
        """Returns the length of this Dictionary.

        """
        return self.keyvaluepair_set.count()

    def iterkeys(self):
        """Returns an iterator for the keys of this Dictionary.

        """
        return iter(kvp.key for kvp in self.keyvaluepair_set.all())

    def itervalues(self):
        """Returns an iterator for the keys of this Dictionary.

        """
        return iter(kvp.value for kvp in self.keyvaluepair_set.all())

    __iter__ = iterkeys

    def iteritems(self):
        """Returns an iterator over the tuples of this Dictionary.

        """
        return iter((kvp.key, kvp.value) for kvp in self.keyvaluepair_set.all())

    def keys(self):
        """Returns all keys in this Dictionary as a list.

        """
        return [kvp.key for kvp in self.keyvaluepair_set.all()]

    def values(self):
        """Returns all values in this Dictionary as a list.

        """
        return [kvp.value for kvp in self.keyvaluepair_set.all()]

    def items(self):
        """Get a list of tuples of key, value for the items in this Dictionary.
        This is modeled after dict.items().

        """
        return [(kvp.key, kvp.value) for kvp in self.keyvaluepair_set.all()]

    def get(self, key, default=None):
        """Gets the given key from the Dictionary. If the key does not exist, it
        returns default.

        """
        try:
            return self[key]

        except KeyError:
            return default

    def has_key(self, key):
        """Returns true if the Dictionary has the given key, false if not.

        """
        return self.contains(key)

    def contains(self, key):
        """Returns true if the Dictionary has the given key, false if not.

        """
        try:
            self.keyvaluepair_set.get(key=key)
            return True

        except KeyValuePair.DoesNotExist:
            return False

    def clear(self):
        """Deletes all keys in the Dictionary.

        """
        self.keyvaluepair_set.all().delete()

    def __unicode__(self):
        """Returns a unicode representation of the Dictionary.

        """
        return unicode(self.asPyDict())

    def asPyDict(self):
        """Get a python dictionary that represents this Dictionary object.
        This object is read-only.

        """
        fieldDict = dict()

        for kvp in self.keyvaluepair_set.all():
            fieldDict[kvp.key] = kvp.value

        return fieldDict


class KeyValuePair(models.Model):
    """A Key-Value pair with a pointer to the Dictionary that owns it.

    """
    container = models.ForeignKey(Dictionary, db_index=True)
    key = models.CharField(max_length=240, db_index=True)
    value = models.CharField(max_length=65536, db_index=True)