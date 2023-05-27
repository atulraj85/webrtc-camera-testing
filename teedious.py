import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2


st.title("TeeDiouS")

th1 = st.slider("Threshold 1", 0, 1000)

th2 = st.slider("Threshold 2", 0, 1000)

# Inputs a videoframe and converts it
def openCVCallback(frame: av.VideoFrame) -> av.VideoFrame:
    # input frame to array of 3 channel colors
    #  3 * 8bits = 24 bit

    img = frame.to_ndarray(format = "bgr24")

    # edge extraction filter
    img = cv2.Canny(img, th1, th2)

    # color conversion
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)



    # return a videoframe from img as array
    return av.VideoFrame.from_ndarray(img, format = "bgr24")

# After camera the feed is going to be send to 
# callback function openCVCallback
webrtc_streamer(key = "liveInput", video_frame_callback = openCVCallback)





