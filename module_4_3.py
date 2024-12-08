def test_function():
    #words = "Я в области видимости функции test_function"
    #print(words)
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # без вызова test_function не работает

#inner_function() не работает так как не внутри функции inner, и мешает выполнению test_function

test_function() # работает только с вызовом inner_function внутри функции

'''inner_function()  NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                   выдаёт ошибку'''