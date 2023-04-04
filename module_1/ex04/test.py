from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

print("test lists of different lenghts")
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))

print("test int in words:")
words = [1, "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))

print("test dict:")
words = {'hey': 1}
print(Evaluator.zip_evaluate(coefs, words))


print("test empty:")
words = []
coefs = []
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

print("test int in words:")
words = ["la", "Lorem", 3, "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))

print("test int in coef:")
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1, 3, 0.5]
print(Evaluator.zip_evaluate(coefs, words))

print("test char in coef:")
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 'c', 3.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
