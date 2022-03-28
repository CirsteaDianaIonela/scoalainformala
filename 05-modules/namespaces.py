# def my_function():
#     global msg
#     msg="Hello" #se afla in namespa-ul local al functiei
#     print(msg)
#     return None
#
# my_function()
# print(msg)
#
def my_function():
    def my_second_function():
        msg = "Hello"
        print(f'functia mea secundara: {msg}')
        return None


    my_second_function()  #de aici apare primul mesaj afisat

    msg = "buna"

    print(f'functia mea principala {msg}')
    return None

my_function() #de aici apare al 2lea mesaj afisat

# #la apelare se executa si se afiseara totul







