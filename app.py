import streamlit as st

# List to store event posts
events = []
# Sample event for demonstration
sample_event = {
    'title': 'Ganesh Event',
    'description': 'This is a sample event description. It can include details about the event and what participants can expect.',
    'user': 'SampleUser',
    'images': ['https://godhindus.com/wp-content/uploads/2023/05/ganesh-ji-wallpaper.jpg'],
    'videos': ['https://www.youtube.com/watch?v=FAq9rruhi3Q'],
    'links': [{'text': 'Example Website', 'url': 'https://example.com'}]
}

# Append the sample event to the events list
events.append(sample_event)

import streamlit as st


# Function to display event posts
def display_events():
    st.header("Event Posts")
    for event in events:
        st.write(f"**{event['title']}**")
        st.write(f"Description: {event['description']}")
        st.write(f"Posted by: {event['user']}")

        # Display images
        for image in event['images']:
            st.image(image, caption='Image')

        # Display videos
        for video_url in event['videos']:
            st.video(video_url)

        # Display links
        for link in event['links']:
            st.markdown(f"[{link['text']}]({link['url']})")

        st.write("----")

# Function to add a new event post
def add_event():
    st.header("Add Event")
    title = st.text_input("Event Title")
    description = st.text_area("Event Description")
    user = "User123"  # For simplicity, using a hardcoded user here

    # Allow uploading images
    images = st.file_uploader("Upload Image(s)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    # Allow entering video URLs
    st.write("You can also provide video URLs (e.g., YouTube, Vimeo).")
    videos = st.text_area("Video URLs (one per line)")

    # Allow entering links
    st.write("You can also provide links with a description (e.g., 'My Website: https://example.com').")
    links = st.text_area("Links (one per line)")

    if st.button("Post Event"):
        event = {'title': title, 'description': description, 'user': user, 'images': images, 'videos': videos.split('\n'), 'links': []}
        for link in links.split('\n'):
            if link:
                link_parts = link.split(': ')
                if len(link_parts) == 2:
                    event['links'].append({'text': link_parts[0], 'url': link_parts[1]})
        events.append(event)
        st.success("Event posted successfully!")

# Main application
st.title("\t\t\t\t\tLocal Posts")

# Display existing events
display_events()

add_event()
