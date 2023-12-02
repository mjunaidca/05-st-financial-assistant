
import streamlit as st

from assistant import FinancialAssistantManager
from seed import financial_tools, INSTRUCTIONS
import os
import requests
# get streamlit session state
if "message" not in st.session_state:
    st.session_state.message = []

# Set up the Streamlit page title & icon
st.set_page_config(
    page_title="AI Financial Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.header("Sneak in Financial analyst Brain")
st.sidebar.write("See what am I doing in the background...")

st.header(" :dollar: AI Financial Analyst")

fmp_analyst: FinancialAssistantManager = FinancialAssistantManager()

assistant = fmp_analyst.create_assistant(
    name="Financial Analyst",
    instructions=INSTRUCTIONS,
    tools=financial_tools,
    file_obj=[])

thread = fmp_analyst.create_thread()

# show chat interface

# show existing messages in chat
for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# chat input
if prompt := st.chat_input("compare last year financial health of Microsoft and Apple focusing on their balance sheets and key financial ratios"):

    # adding user in state
    st.session_state.message.append({
        "role": "user",
        "content": prompt
    })

    # Show the user prompt
    with st.chat_message("user"):
        st.write(prompt)

    try:
        fmp_analyst.add_message_to_thread(
            role="user",
            content=prompt
        )
    except Exception:
        # logging.error("Error adding message to thread")
        st.sidebar.error(
            "Error in processing your request. Please refresh and try again later.")
        st.stop()  # Optionally stop further execution

    # Step =4: Create a Run
    run = fmp_analyst.run_assistant(
        instructions=INSTRUCTIONS
    )

    final_res = fmp_analyst.wait_for_completion(
        run=run,
        thread=thread
    )

    # Step 06: Retrive and Display the assistant response
    assistant_message_in_run = [
        message for message in final_res
        if message.run_id == run.id and message.role == "assistant"
    ]

    for message in assistant_message_in_run:

        role_label = "User" if message.role == "user" else "Assistant"

        # Check the type of message content and handle accordingly
        for content in message.content:
            print('=================\n', content)
            if content.type == "text":
                message_content = content.text.value
                st.session_state.message.append({
                    "role": role_label,
                    "content": message_content
                })
                with st.chat_message(role_label):
                    st.markdown(message_content, unsafe_allow_html=True)

            elif content.type == "image_file":
                # Handle image file content, e.g., display the image
                image_file_id = content.image_file.file_id
                image_url = f"https://api.openai.com/v1/files/{image_file_id}/content"
                headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}

                # Perform the HTTP GET request to download the image
                response = requests.get(image_url, headers=headers)

                # Check if the request was successful
                if response.status_code == 200:
                    # Display the image
                    st.image(response.content, caption=f"{role_label}: Image File ID: {image_file_id}", use_column_width=True)
                else:
                    st.warning(f"Failed to download image: HTTP Status Code {response.status_code}")
