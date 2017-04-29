from watson_developer_cloud import VisualRecognitionV3

def classify_image(filepath, api_key):
    predefined_classes = ['banana', 'apple', 'cucumber']
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)

    with open(filepath, "rb") as file:
        res = visual_recognition.classify(images_file=file)
        
        try:
            classes = res['images'][0]['classifiers'][0]['classes']
            classes.sort(key=lambda x: x['score'], reverse=True)

            for i in classes:
                if i['class'] in predefined_classes:
                    return {'class': i['class'] }
        except e:
            print(e)
        
        return {'class': 'undefined' }

#print(classify_image("banana-crop.jpg", "<api-key>"))