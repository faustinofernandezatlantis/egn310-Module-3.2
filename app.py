import streamlit as st
from doubly_linked_list import Playlist

st.set_page_config(page_title="Playlist Manager", page_icon="🎵", layout="centered")

# Initialize playlist in Streamlit Session State
if "playlist" not in st.session_state:
    pl = Playlist()
    # Sample initial tracks
    pl.add_track("Bohemian Rhapsody", "Queen", "5:55")
    pl.add_track("Hotel California", "Eagles", "6:30")
    pl.add_track("Billie Jean", "Michael Jackson", "4:54")
    st.session_state.playlist = pl

playlist = st.session_state.playlist

st.title("🎵 Playlist Manager")
st.caption("Powered by a custom Doubly Linked List")

# --- CURRENTLY PLAYING SECTION ---
st.subheader("🎧 Currently Playing")
if playlist.current:
    st.info(f"**{playlist.current.title}** by *{playlist.current.artist}* ({playlist.current.duration})")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏮️ Previous Track", disabled=(playlist.current.prev is None), use_container_width=True):
            playlist.prev_track()
            st.rerun()
    with col2:
        if st.button("Next Track ⏭️", disabled=(playlist.current.next is None), use_container_width=True):
            playlist.next_track()
            st.rerun()
else:
    st.warning("The playlist is empty.")

st.divider()

# --- ADD TRACK SECTION ---
st.subheader("➕ Add New Track")
with st.form("add_track_form", clear_on_submit=True):
    title = st.text_input("Track Title")
    artist = st.text_input("Artist")
    duration = st.text_input("Duration (e.g., 3:45)")
    submitted = st.form_submit_button("Add to Playlist")

    if submitted:
        if title and artist and duration:
            playlist.add_track(title, artist, duration)
            st.success(f"Added '{title}' to the playlist!")
            st.rerun()
        else:
            st.error("Please fill in all fields.")

st.divider()

# --- PLAYLIST TRACKS & REORDERING ---
st.subheader("📜 Playlist Tracks")
tracks = playlist.to_list()

if not tracks:
    st.write("No tracks in playlist.")
else:
    for idx, track in enumerate(tracks):
        is_playing = (track == playlist.current)
        prefix = "▶️ " if is_playing else "🎵 "
        
        col_info, col_up, col_del = st.columns([6, 2, 2])
        
        with col_info:
            st.write(f"{prefix}**{idx + 1}. {track.title}** — {track.artist} (`{track.duration}`)")
            
        with col_up:
            if st.button("⬆️ Move Up", key=f"up_{idx}", disabled=(idx == 0)):
                playlist.move_track_up(idx)
                st.rerun()
                
        with col_del:
            if st.button("🗑️ Delete", key=f"del_{idx}"):
                playlist.remove_track(idx)
                st.rerun()