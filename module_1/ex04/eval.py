class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            print("ERROR wrong data type")
            return None
        if len(coefs) == 0 or len(words) == 0:
            return None
        if (type(coefs[0]) != float and type(coefs[0]) != int)\
                or type(words[0]) != str:
            print("ERROR wrong data type")
            return None
        if len(coefs) != len(words):
            return -1
        return sum(len(x) * y for x,y in zip(words, coefs))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            print("ERROR wrong data type")
            return None
        if len(coefs) == 0 or len(words) == 0:
            return None
        if (type(coefs[0]) != float and type(coefs[0]) != int)\
                or type(words[0]) != str:
            print("ERROR wrong data type")
            return None
        if len(coefs) != len(words):
            return -1

        return sum(x * len(words[i]) for i,x in enumerate(coefs))
