import streamlit as st
import query_params as qp

# Reset query params; the query params will update throughout the app as qp.update() is called
qp.reset()


# ----- START: MAIN APP -----

# Display the title
st.markdown('# Query Parameters Demo')
st.markdown('## Inputs')


# Get query params
query_params = qp.get_helper(['color_enabled', 'color_index', 'pet_index', 'size_index'], default=0)

# Create a pet selectbox
pets = ['dog', 'cat', 'fish', 'hamster']
pet = st.selectbox('Pet', options=pets, index=query_params['pet_index'], key='pet_select')

# Create a size radio
enable_options = [False, True]
color_enabled = st.radio('Enable color?', enable_options, index=query_params['color_enabled'], key='color_enable_radio')

# Toggle color selection on and off
# If color is not enabled, then the query won't appear in the URL. However, it will be remembered in the state!
if color_enabled:
    # Create a color selectbox
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    color = st.selectbox('Color', options=colors, index=query_params['color_index'], key='color_select')

    # Update query params
    qp.update(color_index=colors.index(color))


# Create a size radio
sizes = ['small', 'big']
size = st.radio('Text Size', sizes, index=query_params['size_index'], key='size_radio')

# Create the text
if color_enabled:
    text = 'Hello {} {}!'.format(color, pet)
else:
    text = 'Hello {}!'.format(pet)
if size == 'big':
    text = '## ' + text

# Display the text
st.markdown('## Result')
st.markdown(text)

# Update query params
qp.update(color_enabled=enable_options.index(color_enabled), pet_index=pets.index(pet), size_index=sizes.index(size))


# ----- END: MAIN APP -----


# Set query params; this actually updates the URL
qp.set()
