# upload.py

import streamlit as st
from PIL import Image
import os
import shutil
from yolov5 import detect 



def upload():
    st.write('### Upload')
    if getattr(st.session_state, 'logged_in', False):
        st.write('#### Upload an image.')
        uploaded_file = st.file_uploader('', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)

        if uploaded_file is None:
            st.warning("No file has been uploaded.")
        else:
            if os.path.exists('yolov5/runs/detect/exp'):
                shutil.rmtree('yolov5/runs/detect/exp')

            image = Image.open(uploaded_file).convert("RGB")
            filename = str(uploaded_file.name)
            image = image.save(filename)

            detect.run(weights='best.pt', conf_thres=0.1, source=filename)
            #run(weights='best.pt', conf_thres=0.1, source=filename)


            st.image('yolov5/runs/detect/exp/' + filename)

            os.remove(filename)
            os.remove('yolov5/runs/detect/exp/' + filename)
    else:
        st.write("Please login to upload an image.")
