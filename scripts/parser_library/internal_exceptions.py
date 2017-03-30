class ParseError(Exception): pass
class CourseParseError(ParseError):
	'''Raise during runtime login error in course parsers.'''
	# TODO - add stats here like department, course, current request, etc.
	# TODO - move, doesn't belong in this module

class JsonException(Exception):
	'''Parent class to all exceptions relating to json.'''
	def __init__(self, message, json=None, *args):
		self.message = message
		self.json = json
		super(JsonException, self).__init__(message, json, *args)

	def __str__(self):
		return self.message + '\n' + pretty_json(self.json)

class JsonValidationError(JsonException, ValueError):
	'''Raise when fatal failure of validation condition.'''
	def __init__(self, message, json=None, *args):
		self.message = message
		self.json = json # TODO - validate json
		super(JsonValidationError, self).__init__(message, json, *args)

	def __str__(self):
		return 'error: ' + super(JsonValidationError, self).__str__()

class JsonValidationWarning(JsonException, UserWarning):
	'''Raise when user `should` be made aware of non-optimal, non-fatal condition.'''
	def __init__(self, message, json=None, *args):
		self.message = message
		self.json = json
		super(JsonValidationWarning, self).__init__(message, json, *args)

	def __str__(self):
		return 'warning: ' + self.message + '\n' + pretty_json(self.json)

class JsonDuplicationWarning(JsonValidationWarning):
	'''Raise when validation detects duplicate json objects in the same parse.'''
	def __init__(self, message, json=None, *args):
		super(JsonDuplicationWarning, self).__init__(message, json, *args)

	def __str__(self):
		return 'warning: ' + self.message + '\n' + pretty_json(self.json)

class DigestionError(ValueError):
	'''Raise when fails digestion invariant.'''
	def __init__(self, message, json=None, *args):
		self.message = message
		self.json = json
		super(DigestionError, self).__init__(message, json, *args)

	def __str__(self):
		return 'error (digestion): ' + self.message + '\n' + pretty_json(self.json)

class IngestorWarning(UserWarning):
	'''Raise when user should be notified of non-optimal usage of ingestor.'''
	def __init__(self, message, json=None, *args):
		self.message = message
		self.json = json
		super(IngestorWarning, self).__init__(message, json, *args)

	def __str__(self):
		return 'warning: ' + self.message + '\n' + pretty_json(self.json)

import simplejson as json
from pygments import highlight, lexers, formatters, filters
def pretty_colored_json(j):
	if j is None:
		return 'None'
	'''Format and colorize json for prettified output.'''
	j = pretty_json(j)
	l = lexers.JsonLexer()
	l.add_filter('whitespace')
	colorful_json = highlight(unicode(j, 'UTF-8'), l, formatters.TerminalFormatter())
	return colorful_json

def pretty_json(j):
	'''Format and colorize json for prettified output.'''
	if isinstance(j, basestring):
		j = json.loads(j)
	if isinstance(j, dict):
		j = json.dumps(j, sort_keys=True, indent=2, separators=(',', ': '))
	return j