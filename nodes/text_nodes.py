class PromptTextBox:
    """多行提示词输入框,把文本转成 STRING 输出,方便连线复用。"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "run"
    CATEGORY = "essentials/text"

    def run(self, text):
        return (text,)


class TextCombine:
    """把两段文本用分隔符拼接成一段。"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {"multiline": True, "forceInput": True}),
                "text_b": ("STRING", {"multiline": True, "forceInput": True}),
                "delimiter": ("STRING", {"multiline": False, "default": ", "}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "combine"
    CATEGORY = "essentials/text"

    def combine(self, text_a, text_b, delimiter):
        a = (text_a or "").strip()
        b = (text_b or "").strip()
        if a and b:
            return (a + delimiter + b,)
        return (a or b,)
