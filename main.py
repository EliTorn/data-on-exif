import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
                st.write(f"{tag_name}: {value}")
        else:
            print("No EXIF data found.")
            st.write("No EXIF data found.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    st.title("exif data Uploader : ")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        get_exif_data(uploaded_file)


if __name__ == "__main__":
    main()
