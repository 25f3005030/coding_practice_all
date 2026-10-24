from jinja2 import Template 

html_template=Template("""
    <!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <div>
      <div>
        <h2>{{ heading }}</h2>
      </div>
      <p>{{ paragraph }}</p>
    </div>
  </body>
</html>
""")

html=html_template.render(
    title='this is title',
    heading='this is heading',
    paragraph='this is the paragraph'
)

print(html) 