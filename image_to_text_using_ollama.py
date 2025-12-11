import base64
import requests
import ollama

# ---------------------------------------------------------
# Convert local image to Base64
# ---------------------------------------------------------
def image_to_base64(image_path):
    """Converts a local image to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# ---------------------------------------------------------
# Extract text from image via URL (download → base64 → LLM)
# ---------------------------------------------------------
def image_to_text_from_url(image_url):
    """Downloads image from URL, converts to base64, sends to deepseek-r1."""
    img_bytes = requests.get(image_url).content
    image_base64 = base64.b64encode(img_bytes).decode("utf-8")

    response = ollama.chat(
        model="qwen2.5vl:3b",
        messages=[
            {
                "role": "user",
                "content": "Extract ALL text from this image, preserving order and completeness.",
                "images": [image_base64],
            }
        ]
    )

    return response["message"]["content"]


# ---------------------------------------------------------
# Extract text from image using Base64
# ---------------------------------------------------------
def image_to_text_from_base64(image_base64):
    """Extracts text using a base64 encoded image."""
    response = ollama.chat(
        model="qwen2.5vl:3b",
        messages=[
            {
                "role": "user",
                "content": (
                    "Extract all text from this image thoroughly. "
                    "Do NOT miss any words, headings, lists, faint text, "
                    "or text near edges. Maintain the original reading order."
                ),
                "images": [image_base64],
            }
        ]
    )

    return response["message"]["content"]


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":

    # ---- Example 1 → From URL ----
    # image_url = "https://example.com/sample.png"
    # extracted_text = image_to_text_from_url(image_url)
    # print("Extracted Text from URL:\n", extracted_text)


    # ---- Example 2 → From local image path ----
    local_image_path = "image.jpg"  # replace with real image path
    image_base64 = image_to_base64(local_image_path)

    print("\nExtracted Text from Base64:\n")
    extracted_text = image_to_text_from_base64(image_base64)
    print(extracted_text)

    # Save output
    output_file_path = "extracted_text.txt" # replace with the target output file path
    with open(output_file_path, "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)
        text_file.write("\n")
