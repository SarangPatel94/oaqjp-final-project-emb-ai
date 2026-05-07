"""Unit tests for emotion detection."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def test_sentiment_analyzer(self):
        """Test joy, anger, disgust, sadness and fear emotions."""

        text_joy = "I am glad this happened"
        self.assertEqual(
            emotion_detector(text_joy)["dominant_emotion"],
            "joy"
        )

        text_anger = "I am really mad about this"
        self.assertEqual(
            emotion_detector(text_anger)["dominant_emotion"],
            "anger"
        )
        
        text_disgust = "I feel disgusted just hearing about this"
        self.assertEqual(
            emotion_detector(text_disgust)["dominant_emotion"],
            "disgust"
        )
        
        text_sadness = "I am so sad about this"
        self.assertEqual(
            emotion_detector(text_sadness)["dominant_emotion"],
            "sadness"
        )
        
        text_fear = "I am really afraid that this will happen"
        self.assertEqual(
            emotion_detector(text_fear)["dominant_emotion"],
            "fear"
        )


if __name__ == "__main__":
    unittest.main()