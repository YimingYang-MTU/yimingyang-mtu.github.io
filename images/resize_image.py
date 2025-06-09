from PIL import Image
import os

def resize_image(input_path, output_width=None, output_height=None, keep_aspect=True):
    """
    Resize a PNG image to specified dimensions.
    
    Args:
        input_path (str): Path to the input PNG file
        output_width (int): Desired width in pixels (None to calculate from height)
        output_height (int): Desired height in pixels (None to calculate from width)
        keep_aspect (bool): Whether to maintain aspect ratio (default: True)
    
    Returns:
        str: Path to the resized image
    """
    # Open the image
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        
        # Calculate new dimensions if keeping aspect ratio
        if keep_aspect:
            if output_width and output_height:
                # Calculate scaling factors for both dimensions
                width_ratio = output_width / original_width
                height_ratio = output_height / original_height
                # Use the smaller ratio to maintain aspect
                ratio = min(width_ratio, height_ratio)
                new_width = int(original_width * ratio)
                new_height = int(original_height * ratio)
            elif output_width:
                ratio = output_width / original_width
                new_width = output_width
                new_height = int(original_height * ratio)
            elif output_height:
                ratio = output_height / original_height
                new_height = output_height
                new_width = int(original_width * ratio)
            else:
                raise ValueError("Either width or height must be specified")
        else:
            new_width = output_width or original_width
            new_height = output_height or original_height
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Create output filename
        dirname, basename = os.path.split(input_path)
        name, ext = os.path.splitext(basename)
        output_filename = f"{name}_{new_width}x{new_height}{ext}"
        output_path = os.path.join(dirname, output_filename)
        
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image saved to: {output_path}")
        return output_path

# Example usage:
if __name__ == "__main__":
    input_image = "C://Users//yimin//cv//academicpages.github.io//images//portfolio5//lane_polygon_map_matching.png"  # Change this to your image path
    resize_image(input_image, 500, 300)  # Resize to 500x300
    #resize_image(input_image, 800)       # Resize width to 800, height auto
    #resize_image(input_image, None, 600) # Resize height to 600, width auto