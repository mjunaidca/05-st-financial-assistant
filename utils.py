# Show Messages and Plot Images in Financial Analysis If ANY

import requests
from IPython.display import Image, display
import os


# def process_citations(text):
#     process_text = text.content[0].text.value
#     print('====================', process_text)
#     return process_text

def process_citations(messages):
    for message in messages:
        st.write("-" * 50)
        # Print the role of the sender
        st.write(f"Role: {message['role']}")

        # Process each content item in the message
        for content in message['content']:
            # Check if the content is text
            if content['type'] == 'text':
                st.write(content['text'])

                # Check and print details about annotations if they exist
                if 'annotations' in content['text']:
                    for annotation in content['text']['annotations']:
                        st.write(f"Annotation Text: {annotation['text']}")
                        st.write(f"File_Id: {annotation['file_path']['file_id']}")
                        annotation_data = requests.get(f"https://api.openai.com/v1/files/{annotation['file_path']['file_id']}/content", headers={"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"})
                        annotation_data_bytes = annotation_data.content

                        filename = annotation['text'].split('/')[-1]

                        with open(f"{filename}", "wb") as file:
                            file.write(annotation_data_bytes)

            # Check if the content is an image file
            elif content['type'] == 'image_file':
                st.write(f"Image File ID: {content['image_file']['file_id']}")
                download_and_save_image(content['image_file']['file_id'], f"{content['image_file']['file_id']}.png")

        # Print a horizontal line for separation between messages
        st.write("-" * 50)
        st.write('\n')


def download_and_save_image(file_id: str, save_path: str) -> None:
    """
    Downloads an image from OpenAI using its file ID and saves it to the specified path.

    Args:
    - file_id (str): The ID of the file to download.
    - save_path (str): The path where the image will be saved.

    Returns:
    - None
    """
    # Construct the URL to download the image
    download_url = f"https://api.openai.com/v1/files/{file_id}/content"

    # Perform the HTTP GET request to download the image
    response = requests.get(download_url, headers={"Authorization": f"Bearer {
                            os.environ.get("OPENAI_API_KEY")}"})

    # Check if the request was successful
    if response.status_code == 200:
        # Write the image to the specified file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved to {save_path}")
    else:
        print(f"Failed to download image: HTTP Status Code {
              response.status_code}")


def pretty_print(messages) -> None:
    print("# Messages")
    for message in messages.data:
        role_label = "User" if message.role == "user" else "Assistant"
        # Check the type of message content and handle accordingly
        for content in message.content:
            if content.type == "text":
                message_content = content.text.value
                print(f"{role_label}: {message_content}\n")
                print()
            elif content.type == "image_file":
                # Handle image file content, e.g., print the file ID or download the image
                image_file_id = content.image_file.file_id
                # Define a path to save the image
                image_save_path = f"image_{image_file_id}.png"
                # Download and save the image
                print(f"{role_label}: Image file ID: {image_file_id}")
                download_and_save_image(image_file_id, image_save_path)

                # Display the image within Jupyter Notebook
                display(Image(filename=image_save_path))
