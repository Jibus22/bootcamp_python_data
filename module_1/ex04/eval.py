class Evaluator:
    @classmethod
    def _sanitize_arg(self, coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            print("ERROR wrong data type")
            return None
        if len(coefs) == 0 or len(words) == 0:
            return None
        if not all([isinstance(x, float) or isinstance(x, int) for x in coefs])\
                    or not all([isinstance(x, str) for x in words]):
            print("ERROR wrong data type")
            return None
        if len(coefs) != len(words):
            return -1

        return 42

    @staticmethod
    def zip_evaluate(coefs, words):
        ret = Evaluator._sanitize_arg(coefs, words)
        if ret is None:
            return None
        elif ret == -1:
            return -1

        return sum(len(x) * y for x,y in zip(words, coefs))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        ret = Evaluator._sanitize_arg(coefs, words)
        if ret is None:
            return None
        elif ret == -1:
            return -1

        return sum(x * len(words[i]) for i,x in enumerate(coefs))
