from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        text = 'I am glad this happened'
        emotions = emotion_detector(text)
        self.assertEqual(emotions['dominant_emotion'], 'joy')
    
    def test_anger(self):
        text = 'I am really mad about this'
        emotions = emotion_detector(text)
        self.assertEqual(emotions['dominant_emotion'], 'anger')

    def test_disgust(self):
        text = 'I feel disgusted just hearing this'
        emotions = emotion_detector(text)
        self.assertEqual(emotions['dominant_emotion'], 'disgust')

    def test_sadness(self):
        text = 'I am so sad about this'
        emotions = emotion_detector(text)
        self.assertEqual(emotions['dominant_emotion'], 'sadness')
    
    def test_fear(self):
        text = 'I am really afraid that this will happen'
        emotions = emotion_detector(text)
        self.assertEqual(emotions['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()