# ComfyUI Essentials Pack

一组轻量、零依赖的 ComfyUI 常用自定义节点,覆盖文本、数值、图像、Latent 四类高频操作。

## 节点一览

| 节点 | 分类 | 功能 |
| --- | --- | --- |
| Prompt Text Box | essentials/text | 多行提示词输入框,输出 STRING,便于连线复用 |
| Text Combine | essentials/text | 用自定义分隔符拼接两段文本 |
| Random Seed | essentials/number | 带随机/递增控件的种子节点,可直接连 KSampler 的 seed |
| Math Operation | essentials/number | 两个数的四则运算,同时输出 FLOAT 与 INT |
| Image Resize By Ratio | essentials/image | 按比例缩放图像,支持 lanczos 等采样算法 |
| Get Image Size | essentials/image | 读取图像的宽、高、批数量 |
| Empty Latent Preset | essentials/latent | 常用出图尺寸预设(SD1.5 / SDXL / 16:9 等),免手填宽高 |

## 安装

```bash
cd ComfyUI/custom_nodes
git clone <本仓库地址> comfyui-essentials-pack
```

重启 ComfyUI 后,在节点菜单的 `essentials` 分类下即可找到所有节点。

无需安装任何额外 Python 依赖(仅使用 ComfyUI 自带的 torch 与 comfy.utils)。

## 目录结构

```
comfyui-essentials-pack/
├── __init__.py            # 节点注册入口
├── nodes/
│   ├── text_nodes.py      # 文本类节点
│   ├── number_nodes.py    # 数值类节点
│   ├── image_nodes.py     # 图像类节点
│   └── latent_nodes.py    # Latent 类节点
└── README.md
```
