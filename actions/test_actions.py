import unittest
from unittest.mock import Mock, MagicMock
import sys
import os

# Add the actions directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from actions.actions import ActionShowServicesCarousel, ActionShowProductsCarousel, ActionShowHelpOptions


class TestCarouselActions(unittest.TestCase):

    def setUp(self):
        self.dispatcher = Mock()
        self.tracker = Mock()
        self.domain = {}

    def test_action_show_services_carousel_facebook(self):
        """Test services carousel action for Facebook channel"""
        action = ActionShowServicesCarousel()
        
        # Mock Facebook channel
        self.tracker.get_latest_input_channel.return_value = "facebook"
        
        # Execute action
        result = action.run(self.dispatcher, self.tracker, self.domain)
        
        # Verify action name
        self.assertEqual(action.name(), "action_show_services_carousel")
        
        # Verify dispatcher was called
        self.dispatcher.utter_message.assert_called_once()
        
        # Verify result is empty list
        self.assertEqual(result, [])

    def test_action_show_services_carousel_telegram(self):
        """Test services carousel action for Telegram channel"""
        action = ActionShowServicesCarousel()
        
        # Mock Telegram channel
        self.tracker.get_latest_input_channel.return_value = "telegram"
        
        # Execute action
        result = action.run(self.dispatcher, self.tracker, self.domain)
        
        # Verify dispatcher was called
        self.dispatcher.utter_message.assert_called_once()
        
        # Verify result
        self.assertEqual(result, [])

    def test_action_show_products_carousel_facebook(self):
        """Test products carousel action for Facebook channel"""
        action = ActionShowProductsCarousel()
        
        # Mock Facebook channel
        self.tracker.get_latest_input_channel.return_value = "facebook"
        
        # Execute action
        result = action.run(self.dispatcher, self.tracker, self.domain)
        
        # Verify action name
        self.assertEqual(action.name(), "action_show_products_carousel")
        
        # Verify dispatcher was called
        self.dispatcher.utter_message.assert_called_once()
        
        # Verify result
        self.assertEqual(result, [])

    def test_action_show_products_carousel_telegram(self):
        """Test products carousel action for Telegram channel"""
        action = ActionShowProductsCarousel()
        
        # Mock Telegram channel
        self.tracker.get_latest_input_channel.return_value = "telegram"
        
        # Execute action
        result = action.run(self.dispatcher, self.tracker, self.domain)
        
        # Verify dispatcher was called
        self.dispatcher.utter_message.assert_called_once()
        
        # Verify result
        self.assertEqual(result, [])

    def test_action_show_help_options_fallback(self):
        """Test help options action with fallback channel"""
        action = ActionShowHelpOptions()
        
        # Mock unknown channel
        self.tracker.get_latest_input_channel.return_value = "rest"
        
        # Execute action
        result = action.run(self.dispatcher, self.tracker, self.domain)
        
        # Verify action name
        self.assertEqual(action.name(), "action_show_help_options")
        
        # Verify dispatcher was called with template
        self.dispatcher.utter_message.assert_called_once_with(template="utter_help_carousel")
        
        # Verify result
        self.assertEqual(result, [])

    def test_all_actions_exist(self):
        """Test that all required actions exist and have correct names"""
        services_action = ActionShowServicesCarousel()
        products_action = ActionShowProductsCarousel()
        help_action = ActionShowHelpOptions()
        
        # Verify action names
        self.assertEqual(services_action.name(), "action_show_services_carousel")
        self.assertEqual(products_action.name(), "action_show_products_carousel")
        self.assertEqual(help_action.name(), "action_show_help_options")


if __name__ == '__main__':
    unittest.main()