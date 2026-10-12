import torch


class EmptyLatentPreset:
    """常用出图尺寸预设的 Empty Latent,免手填宽高。"""

    PRESETS = {
        "SD1.5 - 512x512 (方图)": (512, 512),
        "SD1.5 - 512x768 (竖图)": (512, 768),
        "SD1.5 - 768x512 (横图)": (768, 512),
        "SDXL - 1024x1024 (方图)": (1024, 1024),
        "SDXL - 832x1216 (竖图)": (832, 1216),
        "SDXL - 1216x832 (横图)": (1216, 832),
        "SDXL - 1344x768 (宽屏)": (1344, 768),
        "SDXL - 768x1344 (长条)": (768, 1344),
        "16:9 - 1920x1080": (1920, 1080),
        "9:16 - 1080x1920": (1080, 1920),
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("latent", "width", "height")
    FUNCTION = "generate"
    CATEGORY = "essentials/latent"

    def generate(self, preset, batch_size):
        width, height = self.PRESETS[preset]
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples": latent}, width, height)
