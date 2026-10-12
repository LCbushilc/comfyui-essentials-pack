class RandomSeedNode:
    """带随机/递增控件的种子节点,输出 INT,可直接连到 KSampler 的 seed。"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "control_after_generate": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "get_seed"
    CATEGORY = "essentials/number"

    def get_seed(self, seed):
        return (seed,)


class MathOperation:
    """对两个数做四则运算,同时输出 FLOAT 和 INT 结果。"""

    OPERATIONS = ["add", "subtract", "multiply", "divide"]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0, "min": -1e9, "max": 1e9, "step": 0.01}),
                "b": ("FLOAT", {"default": 0.0, "min": -1e9, "max": 1e9, "step": 0.01}),
                "operation": (cls.OPERATIONS,),
            }
        }

    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_result", "int_result")
    FUNCTION = "calculate"
    CATEGORY = "essentials/number"

    def calculate(self, a, b, operation):
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        else:  # divide
            if b == 0:
                raise ZeroDivisionError("Math Operation: division by zero (b = 0)")
            result = a / b
        return (float(result), int(round(result)))
