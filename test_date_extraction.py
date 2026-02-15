#!/usr/bin/env python3
"""
Test script to verify the date extraction functionality
"""

from utils import preparation_message

def test_date_extraction():
    """Test the date extraction from schedule replacement messages"""
    
    # Test cases based on the sample provided
    test_cases = [
        {
            "href": "https://example.com/schedule.pdf",
            "today": "15.02",
            "tomorrow": "16.02",
            "text": '<a href="/netcat_files/userfiles/3/Zamena_1602.pdf"><strong>16.02.2026</strong></a>\n<strong>16.02.2026</strong>\n<a href="/netcat_files/userfiles/3/Zamena_1602.pdf"><strong>16.02.2026</strong></a>\n<strong><a href="/netcat_files/userfiles/3/Zamena_1602.pdf">Замена в расписании на&nbsp;</a></strong>\n<a href="/netcat_files/userfiles/3/Zamena_1602.pdf">Замена в расписании на&nbsp;</a>',
            "expected_contains": ["Расписание на завтра найдено!", "16.02.2026", "("]  # Should contain day of week indicator
        },
        {
            "href": "https://example.com/schedule.pdf",
            "today": "15.02",
            "tomorrow": "16.02",
            "text": 'Замена в расписании на 16.02.2026',
            "expected_contains": ["Расписание на завтра найдено!", "16.02.2026", "("]  # Should contain day of week indicator
        },
        {
            "href": "https://example.com/schedule.pdf",
            "today": "15.02",
            "tomorrow": "16.02",
            "text": 'Замена в расписании на 15.02.2026',
            "expected_contains": ["Расписание на завтра не найдено, найдено на сегодня!", "15.02.2026", "("]  # Should contain day of week indicator
        },
        {
            "href": "https://example.com/schedule.pdf",
            "today": "15.02",
            "tomorrow": "16.02",
            "text": 'Замена в расписании на 20.10.2025',
            "expected_contains": ["Найдено только такое расписание!", "20.10.2025", "("]  # Should contain day of week indicator
        }
    ]
    
    print("Testing date extraction functionality...")
    
    for i, test_case in enumerate(test_cases, 1):
        result = preparation_message(
            test_case["href"],
            test_case["today"],
            test_case["tomorrow"],
            test_case["text"],
            test_case["text"]  # Using the same text as page_text for testing
        )
        
        print(f"\nTest case {i}:")
        print(f"Input text: {test_case['text'][:50]}...")
        print(f"Result: {result}")
        
        # Check if all expected substrings are in the result
        expected_items = test_case["expected_contains"]
        if isinstance(expected_items, list):
            all_found = all(item in result for item in expected_items)
            if all_found:
                print(f"✅ Test {i} PASSED - Found all expected items in result")
            else:
                missing_items = [item for item in expected_items if item not in result]
                print(f"❌ Test {i} FAILED - Missing items: {missing_items}")
        else:
            if expected_items in result:
                print(f"✅ Test {i} PASSED - Found expected date in result")
            else:
                print(f"❌ Test {i} FAILED - Expected '{expected_items}' not found in result")
    
    print("\nDate extraction test completed!")

if __name__ == "__main__":
    test_date_extraction()