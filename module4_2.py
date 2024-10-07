def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
   # inner_function() - выводит ошибку, так как вне функции test_function, нет функции inner_function

