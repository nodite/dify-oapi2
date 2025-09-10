#!/usr/bin/env python3
"""
Get App Feedbacks Example

This example demonstrates how to retrieve application feedbacks using the Chatflow Feedback API
with both sync and async operations, supporting pagination.
"""

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_app_feedbacks_request import GetAppFeedbacksRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def validate_environment():
    """Validate required environment variables."""
    api_key = os.getenv("API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")
    return api_key, domain


def get_feedbacks_basic():
    """Get application feedbacks with default pagination (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    req = GetAppFeedbacksRequest.builder().build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.feedback.list(req, req_option)

    if response.success:
        print("✅ Feedbacks retrieved successfully!")
        print(f"Total feedbacks: {len(response.data)}")

        for i, feedback in enumerate(response.data, 1):
            print(f"\n📝 Feedback {i}:")
            print(f"  ID: {feedback.id}")
            print(f"  Message ID: {feedback.message_id}")
            print(f"  Rating: {feedback.rating}")
            print(f"  Content: {feedback.content}")
            print(f"  From User: {feedback.from_end_user_id}")
            print(f"  Created: {feedback.created_at}")
    else:
        print(f"❌ Error: {response.msg}")


def get_feedbacks_with_pagination():
    """Get application feedbacks with custom pagination (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request with pagination
    req = GetAppFeedbacksRequest.builder().page(1).limit(5).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.feedback.list(req, req_option)

    if response.success:
        print("✅ Feedbacks retrieved with pagination!")
        print("Page: 1, Limit: 5")
        print(f"Retrieved feedbacks: {len(response.data)}")

        for i, feedback in enumerate(response.data, 1):
            print(f"\n📝 Feedback {i}:")
            print(f"  ID: {feedback.id}")
            print(f"  Rating: {feedback.rating}")
            print(
                f"  Content: {feedback.content[:100]}..."
                if len(feedback.content) > 100
                else f"  Content: {feedback.content}"
            )
    else:
        print(f"❌ Error: {response.msg}")


async def get_feedbacks_async():
    """Get application feedbacks (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    req = GetAppFeedbacksRequest.builder().page(1).limit(10).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async request
    response = await client.chatflow.v1.feedback.alist(req, req_option)

    if response.success:
        print("✅ Async feedbacks retrieved successfully!")
        print(f"Retrieved feedbacks: {len(response.data)}")

        # Group by rating
        like_count = sum(1 for f in response.data if f.rating == "like")
        dislike_count = sum(1 for f in response.data if f.rating == "dislike")
        neutral_count = sum(1 for f in response.data if f.rating is None)

        print("\n📊 Feedback Summary:")
        print(f"  👍 Likes: {like_count}")
        print(f"  👎 Dislikes: {dislike_count}")
        print(f"  ➖ Neutral: {neutral_count}")
    else:
        print(f"❌ Error: {response.msg}")


def get_feedbacks_multiple_pages():
    """Get feedbacks from multiple pages."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    all_feedbacks = []
    page = 1
    limit = 10

    print("📄 Retrieving feedbacks from multiple pages...")

    while True:
        print(f"  Fetching page {page}...")

        # Build request for current page
        req = GetAppFeedbacksRequest.builder().page(page).limit(limit).build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.feedback.list(req, req_option)

        if response.success:
            if not response.data:
                print(f"    No more feedbacks on page {page}")
                break

            print(f"    Retrieved {len(response.data)} feedbacks")
            all_feedbacks.extend(response.data)

            # Check if we have fewer results than limit (last page)
            if len(response.data) < limit:
                print("    Last page reached")
                break

            page += 1
        else:
            print(f"    ❌ Error on page {page}: {response.msg}")
            break

    print(f"\n✅ Total feedbacks retrieved: {len(all_feedbacks)}")

    # Analyze all feedbacks
    if all_feedbacks:
        ratings = {}
        for feedback in all_feedbacks:
            rating = feedback.rating or "neutral"
            ratings[rating] = ratings.get(rating, 0) + 1

        print("\n📊 Overall Feedback Analysis:")
        for rating, count in ratings.items():
            print(f"  {rating.capitalize()}: {count}")


def get_feedbacks_with_error_handling():
    """Get feedbacks with comprehensive error handling."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    try:
        # Build request
        req = GetAppFeedbacksRequest.builder().page(1).limit(20).build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.feedback.list(req, req_option)

        if response.success:
            print("✅ Feedbacks retrieved with error handling!")
            print(f"Retrieved {len(response.data)} feedbacks")

            if response.data:
                print("\n📝 Sample feedback:")
                sample = response.data[0]
                print(f"  ID: {sample.id}")
                print(f"  Rating: {sample.rating}")
                print(f"  Content: {sample.content}")
            else:
                print("No feedbacks found for this application")
        else:
            # Handle different types of errors
            if "401" in str(response.code):
                print("❌ Error: Unauthorized")
                print("Suggestion: Check your API key")
            elif "403" in str(response.code):
                print("❌ Error: Forbidden")
                print("Suggestion: Check your permissions for this application")
            elif "400" in str(response.code):
                print("❌ Error: Bad request")
                print("Suggestion: Check pagination parameters")
            else:
                print(f"❌ Failed to retrieve feedbacks: {response.msg}")
                print(f"Error code: {response.code}")

    except Exception as e:
        print(f"❌ Unexpected error during feedback retrieval: {e}")
        print("Please check your network connection and API configuration")


def demonstrate_feedback_analysis():
    """Demonstrate feedback analysis workflow."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    print("🔄 Demonstrating feedback analysis workflow:")
    print("1. Retrieve feedbacks")
    print("2. Analyze ratings")
    print("3. Show recent feedback trends")
    print()

    # Step 1: Retrieve feedbacks
    print("📊 Step 1: Retrieving feedbacks...")
    req = GetAppFeedbacksRequest.builder().page(1).limit(50).build()

    req_option = RequestOption.builder().api_key(api_key).build()
    response = client.chatflow.v1.feedback.list(req, req_option)

    if not response.success:
        print(f"❌ Failed to retrieve feedbacks: {response.msg}")
        return

    feedbacks = response.data
    print(f"  ✅ Retrieved {len(feedbacks)} feedbacks")
    print()

    # Step 2: Analyze ratings
    print("📈 Step 2: Analyzing ratings...")
    rating_stats = {"like": 0, "dislike": 0, "neutral": 0}

    for feedback in feedbacks:
        if feedback.rating == "like":
            rating_stats["like"] += 1
        elif feedback.rating == "dislike":
            rating_stats["dislike"] += 1
        else:
            rating_stats["neutral"] += 1

    total = len(feedbacks)
    if total > 0:
        print(f"  👍 Likes: {rating_stats['like']} ({rating_stats['like'] / total * 100:.1f}%)")
        print(f"  👎 Dislikes: {rating_stats['dislike']} ({rating_stats['dislike'] / total * 100:.1f}%)")
        print(f"  ➖ Neutral: {rating_stats['neutral']} ({rating_stats['neutral'] / total * 100:.1f}%)")
    print()

    # Step 3: Show recent feedback trends
    print("📅 Step 3: Recent feedback trends...")
    if feedbacks:
        # Sort by creation time (most recent first)
        sorted_feedbacks = sorted(feedbacks, key=lambda x: x.created_at, reverse=True)

        print("  Most recent feedbacks:")
        for i, feedback in enumerate(sorted_feedbacks[:5], 1):
            rating_emoji = "👍" if feedback.rating == "like" else "👎" if feedback.rating == "dislike" else "➖"
            content_preview = feedback.content[:50] + "..." if len(feedback.content) > 50 else feedback.content
            print(f"    {i}. {rating_emoji} {content_preview}")

    print("\n✅ Feedback analysis completed!")


if __name__ == "__main__":
    print("🔄 Running Get App Feedbacks Examples...")
    print()

    # Run sync examples
    print("=== Sync Examples ===")
    get_feedbacks_basic()
    print()
    get_feedbacks_with_pagination()
    print()
    get_feedbacks_multiple_pages()
    print()
    get_feedbacks_with_error_handling()
    print()
    demonstrate_feedback_analysis()
    print()

    # Run async example
    print("=== Async Examples ===")
    asyncio.run(get_feedbacks_async())
    print()

    print("✅ All Get App Feedbacks examples completed!")
