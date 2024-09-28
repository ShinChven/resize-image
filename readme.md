# Resize Image CLI

A command-line interface (CLI) tool to resize images while maintaining their aspect ratio. This tool supports various image formats and allows you to specify the maximum length, quality, and target file type.

## Installation

To install the Resize Image CLI from the GitHub repository, use the following command:

```bash
pip install git+https://github.com/ShinChven/resize-image.git
```

## Upgrade

To upgrade the Resize Image CLI to the latest version, use the following command:

```bash
pip install upgrade git+https://github.com/ShinChven/resize-image.git
```

## Usage

After installation, you can use the CLI by running the following command in your terminal:

```bash
resize-image <path> <max_length> [--quality <quality>] [--filetype <filetype>]
```

### Arguments

- `<path>`: The file path to an image or a directory containing images.
- `<max_length>`: The maximum length for resizing (in pixels).
- `--quality <quality>`: (Optional) Set the target image quality (default is 100%).
- `--filetype <filetype>`: (Optional) Set the target file type (default is the original type).
- **Supported Formats**: JPEG (`.jpg`, `.jpeg`), PNG (`.png`), BMP (`.bmp`), GIF (`.gif`), WebP (`.webp`).

### Example

To resize a single image:

```bash
resize-image path/to/image.jpg 800 --quality 90 --filetype png
```

To resize all images in a directory:

```bash
resize-image path/to/directory 800
```

## Requirements

- Python 3.x
- Pillow library

## License

This project is licensed under the MIT License.

[LICENSE](LICENSE)
