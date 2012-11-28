from sgmllib import SGMLParser
import urllib2
import urllib

# Define the class that will parse the suggestion XML
class PullSuggestions(SGMLParser):

   def reset(self):
      SGMLParser.reset(self)
      self.suggestions = []
      self.queries = []

   def start_suggestion(self, attrs):
      for a in attrs:
         if a[0] == 'data': self.suggestions.append(a[1])

   def start_num_queries(self, attrs):
      for a in attrs:
         if a[0] == 'int': self.queries.append(a[1])


# -----------------------------------------------------------
# Enter your phrase here.  Be sure to leave the %s at the end!
# -----------------------------------------------------------
base_query = "how do i %s"  #This is the base query

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
   q = base_query % letter;
   query = urllib.urlencode({'q' : q})
   url = "http://google.com/complete/search?output=toolbar&%s" % query

   res = urllib2.urlopen(url)
   parser = PullSuggestions()
   parser.feed(res.read())
   parser.close()

   for i in range(0,len(parser.suggestions)):
      print "%s\t%s" % (parser.suggestions[i], parser.queries[i])
