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
            "expected_contains": "Замена в расписании на 16.02.2026"
        },
        {
            "href": "https://example.com/schedule.pdf",
            "today": "15.02",
            "tomorrow": "16.02",
            "text": 'Замена в расписании на 16.02.2026',
            "expected_contains": "Замена в расписании на 16.02.2026"
        },
        {
            "href": "https://example.com/schedule.pdf",
            "today": "15.02",
            "tomorrow": "16.02",
            "text": 'Замена в расписании на 16.02',
            "expected_contains": "Замена в расписании на 16.02"
        }
    ]
    
    print("Testing date extraction functionality...")
    
    for i, test_case in enumerate(test_cases, 1):
        result = preparation_message(
            test_case["href"],
            test_case["today"],
            test_case["tomorrow"],
            test_case["text"]
        )
        
        print(f"\nTest case {i}:")
        print(f"Input text: {test_case['text'][:50]}...")
        print(f"Result: {result}")
        
        if test_case["expected_contains"] in result:
            print(f"✅ Test {i} PASSED - Found expected date in result")
        else:
            print(f"❌ Test {i} FAILED - Expected '{test_case['expected_contains']}' not found in result")
    
    print("\nDate extraction test completed!")

if __name__ == "__main__":
    test_date_extraction()