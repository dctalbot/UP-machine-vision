This was a contest submission at a hackathon.

##Getting started

    git clone https://github.com/dctalbot/UP-machine-vision.git
    cd UP-machine-vision/website
    python3 -m venv env
    source env/bin/activate
    pip3 install -e .
    yarn
    flask run

In a separate terminal:

    sudo yarn run watch

##Sample tensorflow command

python label_image.py --image data/TruckSpring/testing/broken/testing_broken_1.jpg --graph retrained_graph.pb --labels retrained_labels.txt --input_layer=Placeholder --output_layer=final_result
