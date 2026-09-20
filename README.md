Here is a complete, professional `README.md` template tailored for your Playlist Manager project, ready to be committed to your GitHub repository.

```markdown
# 🎵 Playlist Manager (Shipped Application 1)

An interactive, web-based Music Playlist Manager built with **Streamlit** and powered by a custom **Doubly Linked List** implementation from scratch.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://egn310-module-3-2.streamlit.app/)

> 🔗 **Live Demo:** [Click here to view the deployed application on Streamlit Community Cloud](https://egn310-module-3-2.streamlit.app/)

---

## 📌 Project Overview

This project demonstrates how a **Doubly Linked List** data structure can manage sequential and stateful data in a real-world application. The UI provides continuous navigation, track reordering, track additions, and deletions—all maintaining runtime efficiency through pointer manipulation rather than array shifting.

### Key Features
- 🎧 **Player Controls:** Seamlessly step forward (`Next`) and backward (`Previous`) through tracks using bidirectional pointers (`next` and `prev`).
- ➕ **Add Tracks:** Insert new tracks dynamically to the tail of the playlist.
- 🗑️ **Delete Tracks:** Remove any track by index, automatically updating adjacent pointers and maintaining player state.
- ⬆️ **Track Reordering:** Swap track positions directly within the linked list structure.
- 🔄 **Session State Persistence:** Powered by `st.session_state` to retain playlist integrity across Streamlit rerenders.

---

## 📂 Repository Structure

```text
playlist-manager/
├── app.py                   # Streamlit web application & state management
├── doubly_linked_list.py    # Custom DoublyLinkedList and TrackNode classes
├── requirements.txt         # Project dependencies
└── README.md                # Documentation & deployment links

```

---

## 🚀 Local Setup & Installation

### Prerequisites

* Python 3.8 or higher installed on your machine.

### Instructions

1. **Clone the repository:**
```bash
git clone [https://github.com/faustinofernandezatlantis/playlist-manager.git](https://github.com/faustinofernandezatlantis/playlist-manager.git)
cd playlist-manager

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Streamlit application:**
```bash
streamlit run app.py

```


4. Open your browser at `http://localhost:8501` to use the application.

---

## 🛠️ Data Structure Implementation Details

| Operation | Method | Time Complexity |
| --- | --- | --- |
| Add Track (Tail) | `add_track()` | $O(1)$ |
| Traverse Forward / Backward | `next_track()` / `prev_track()` | $O(1)$ |
| Remove Track | `remove_track(index)` | $O(N)$ lookup, $O(1)$ removal |
| Reorder Track | `move_track_up(index)` | $O(N)$ lookup, $O(1)$ pointer swap |

---

## ☁️ Deployment

This project is deployed on **Streamlit Community Cloud**. Any updates pushed to the `main` branch automatically trigger a rebuild on the live site.

```
