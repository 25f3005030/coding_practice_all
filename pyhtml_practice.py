import pyhtml   as h 

t=h.html(
    h.head(
        h.title('this is title of webpage')
    ),
    h.body(
        h.h1('this is first division '),
        h.div('this is some text'),
        h.div(
            h.h2('inside titel')
            ,h.p('some text in paragraph '))
    )

)

print(t.render())