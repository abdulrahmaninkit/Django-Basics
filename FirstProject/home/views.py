from django.shortcuts import render
from django.http import HttpResponse

# This is the logical part.

def home(request):
    peoples = [
        {'name':'AR','age':12},
        {'name':'BR','age':13},
        {'name':'CR','age':14},
        {'name':'DR','age':21}

    ]

    vege = ['cucumber', 'carrot', 'pumkin', 'raddish']

    text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Possimus quis natus iure suscipit nulla voluptas delectus libero architecto repudiandae doloribus enim ipsum nostrum blanditiis dolores sed perspiciatis eum id deserunt, veniam excepturi assumenda. Error, amet! Saepe quaerat dolorem recusandae fugit sed tempora nisi est laborum dolorum, officia quis. Recusandae placeat hic esse accusamus odio nulla labore possimus, fugiat, quos, magni neque deserunt amet quia dolores minus doloremque debitis. Eos repudiandae, aut omnis esse modi cum quos reiciendis rerum corrupti aliquid? Labore autem animi quos repellat vel libero eveniet natus, vero soluta sunt deserunt voluptas corporis ipsum doloribus quidem ab nulla!
        """
    return render (request, "index.html",context = {'peoples':peoples, 'text':text, 'vege':vege})


def demo(request):
    return HttpResponse("""
                       
                        <h1>This is a django server</h1>
                        <h2>Learning Django first time</h2>      
                        
                        """)
# Always add the path in the urls.py
def success_page(request):
    return render(request, "index.html")

# Always add the path in the urls.py
def about(request):
    context = {"page":about}
    return render(request, "about.html",context)
# Always add the path in the urls.py
def contact(request):

    text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Possimus quis natus iure suscipit nulla voluptas delectus libero architecto repudiandae doloribus enim ipsum nostrum blanditiis dolores sed perspiciatis eum id deserunt, veniam excepturi assumenda. Error, amet! Saepe quaerat dolorem recusandae fugit sed tempora nisi est laborum dolorum, officia quis. Recusandae placeat hic esse accusamus odio nulla labore possimus, fugiat, quos, magni neque deserunt amet quia dolores minus doloremque debitis. Eos repudiandae, aut omnis esse modi cum quos reiciendis rerum corrupti aliquid? Labore autem animi quos repellat vel libero eveniet natus, vero soluta sunt deserunt voluptas corporis ipsum doloribus quidem ab nulla!
        """
    return render(request, "contact.html",context={"text":text, "page":contact})
#Comments:
#Multiple lines can be returned in HttpResponse using """" but this is not a feesible method
#In order to create a seperate html file create a templates folder inside of app->'home' and then file.html
# Always add the path in the urls.py