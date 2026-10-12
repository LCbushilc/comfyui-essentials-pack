import torch


class ImageResizeByRatio:
    """按比例缩放图像,保持宽高比,支持多种采样算法。"""

    UPSCALE_METHODS = ["nearest-exact", "bilinear", "area", "bicubic", "lanczos"]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "ratio": ("FLOAT", {"default": 1.0, "min": 0.01, "max": 8.0, "step": 0.01}),
                "method": (cls.UPSCALE_METHODS,),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "resize"
    CATEGORY = "essentials/image"

    def resize(self, image, ratio, method):
        # ComfyUI 图像张量形状为 [B, H, W, C]
        _, h, w, _ = image.shape
        new_w = max(1, round(w * ratio))
        new_h = max(1, round(h * ratio))

        samples = image.movedim(-1, 1)  # [B, C, H, W]
        try:
            import comfy.utils

            out = comfy.utils.common_upscale(samples, new_w, new_h, method, "disabled")
        except Exception:
            mode = method if method in ("nearest-exact", "bilinear", "area", "bicubic") else "bicubic"
            out = torch.nn.functional.interpolate(
                samples, size=(new_h, new_w), mode=mode
            )
        out = out.movedim(1, -1)  # 还原为 [B, H, W, C]
        return (out,)


class GetImageSize:
    """读取图像的宽、高和批数量。"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "count")
    FUNCTION = "get_size"
    CATEGORY = "essentials/image"

    def get_size(self, image):
        b, h, w, _ = image.shape
        return (int(w), int(h), int(b))
