# imageRecognition
Code for Image Recognition using [docomo API](https://dev.smt.docomo.ne.jp/?p=index)

For more information, visit [docomo Developer support](https://dev.smt.docomo.ne.jp/?p=index)

## Requirements
    $ pip install poster

## Usage
    $ python imageRecognition.py [--image (JPEG file name)] [--scene (modelName)]

    usage: imageRecognition.py [-h] [--image IMAGE] [--model MODEL]

    optional arguments:
      -h, --help     show this help message and exit
      --image IMAGE  name of input image
      --model MODEL  modelName = {scene, fashion_pattern, fashion_type,
                     fashion_style, fashion_color, food, flower, kinoko}
