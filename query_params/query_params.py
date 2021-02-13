import streamlit as st
import st_state_patch


def is_int(val):
    try:
        int(val)
    except Exception:
        return False
    return True


def is_float(val):
    try:
        int(val)
    except Exception:
        return False
    return True


def get():
    '''
    The first time this is called in your app, it reads the query parameters in the URL bar and saves it as the original (i.e. default) state.
    On subsequent runs, returns the original (i.e. default) query parameters to avoid issues with Streamlit's component states. See https://github.com/streamlit/streamlit/issues/2370
    '''

    # Get state
    state = st.SessionState('query_params')
    if not hasattr(state, 'default_query_params'):
        state.default_query_params = st.experimental_get_query_params()

    # Get values
    query_params = state.default_query_params
    for key, vals in query_params.items():
        if isinstance(vals, list) and len(vals) == 1:
            val = vals[0]
            if is_int(val):
                val = int(val)
            elif is_float(val):
                val = float(val)
            query_params[key] = val

    return query_params


def get_helper(extract, default=None, query_params=None):
    '''
    A helper function for getting query parameters.
    '''

    # Basic assertion
    assert isinstance(extract, list)

    # Get query params
    if query_params is None:
        query_params = get()

    # Loop over vars to extract
    output = {}
    for var in extract:
        val = default
        if var in query_params.keys():
            val = query_params[var]
        output[var] = val

    return output


def reset():
    '''
    Resets the query parameters state. The query parameters will update throughout the app as update() is called

    This should be called once at the very start of your Streamlit app. For this example, we only call it at the beginning of main.py.
    '''

    # Get and reset state
    state = st.SessionState('query_params')
    if hasattr(state, 'query_params'):  # attr won't exist on first app run
        # Remember previous query parameters; used in set()
        state.prev_query_params = state.query_params
    else:
        state.prev_query_params = {}
    state.query_params = {}


def update(**kwargs):
    '''
    Update the query parameters state.

    This should be called whenever you want to add a query parameter.
    '''

    # Get state
    state = st.SessionState('query_params')
    if not hasattr(state, 'query_params'):
        state.query_params = {}

    # Set values
    query_params = state.query_params
    for param, val in kwargs.items():
        query_params[param] = val

    # Update state
    state.query_params = query_params


def set():
    '''
    Actually updates the query parameters in the URL bar. Will also update the original (i.e. default) query parameters so that

    This should only be called once at the very end of your Streamlit app. For this example, we only call it at the end of main.py.
    '''

    # Get state
    state = st.SessionState('query_params')
    curr_query_params = state.query_params
    prev_query_params = state.prev_query_params
    default_query_params = state.default_query_params

    # Set query params
    st.experimental_set_query_params(**state.query_params)

    # Update default query params if any keys were removed (i.e. that part of the stream)
    # This allows the app to remember downstream query params
    for prev_key, prev_val in prev_query_params.items():
        if prev_key not in curr_query_params.keys():
            default_query_params[prev_key] = prev_val

    # Update state
    state.default_query_params = default_query_params
