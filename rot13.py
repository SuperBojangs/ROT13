import webapp2

form="""
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(answer)s
</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

key = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}

def encrypt(word):
        new_string = ""
    
        for char in word:
            if char in "ABCDEFGHIJKLMNOPQRSTUVQWXYZabcdefghijklmnopqrstuvwxyz":
                for letter in key:    
                    if char.lower() == letter:
                        if char.isupper():
                            new_string +=key[letter].capitalize()
                        else:    
                            new_string+=key[letter]
            else:
                new_string +=char
        return new_string              


def escape_html(s):
    new_string = ""
    for each in s:
        if ">" == each:
            new_string +="&gt;"
        elif "<" == each:
            new_string +="&lt;"
        elif "&" == each:
            new_string +="&amp;"
        elif '"' == each:
            new_string +="&quot;"
        else:
            new_string+=each
            
    return new_string 

class MainPage(webapp2.RequestHandler):
    def write_form(self, answer="Your text here"):
        self.response.out.write(form % {"answer":escape_html(answer)})

    def get(self):
        self.write_form()

    def post(self):
        user_input = self.request.get('text')

        answer2 = encrypt(user_input)
        self.write_form(answer2)




    


application = webapp2.WSGIApplication([('/', MainPage)], debug=True)
