from .nodes.text_nodes import PromptTextBox, TextCombine
from .nodes.number_nodes import RandomSeedNode, MathOperation
from .nodes.image_nodes import ImageResizeByRatio, GetImageSize
from .nodes.latent_nodes import EmptyLatentPreset

NODE_CLASS_MAPPINGS = {
    "Essentials_PromptTextBox": PromptTextBox,
    "Essentials_TextCombine": TextCombine,
    "Essentials_RandomSeed": RandomSeedNode,
    "Essentials_MathOperation": MathOperation,
    "Essentials_ImageResizeByRatio": ImageResizeByRatio,
    "Essentials_GetImageSize": GetImageSize,
    "Essentials_EmptyLatentPreset": EmptyLatentPreset,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Essentials_PromptTextBox": "Prompt Text Box (Essentials)",
    "Essentials_TextCombine": "Text Combine (Essentials)",
    "Essentials_RandomSeed": "Random Seed (Essentials)",
    "Essentials_MathOperation": "Math Operation (Essentials)",
    "Essentials_ImageResizeByRatio": "Image Resize By Ratio (Essentials)",
    "Essentials_GetImageSize": "Get Image Size (Essentials)",
    "Essentials_EmptyLatentPreset": "Empty Latent Preset (Essentials)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
