from podcastfy.client import generate_podcast

transcribe_example = "https://engageli-eksdev-media-manager-matan-us-east-1.s3.us-east-1.amazonaws.com/matan/20/5eefbb17-0d68-4f86-99a5-515d38061106-hls/transcribe.txt"
pdf_example_engageli = "https://engageli-eksdev-media-manager-matan-us-east-1.s3.us-east-1.amazonaws.com/matan/20/5eefbb17-0d68-4f86-99a5-515d38061106-hls/overview-engageli.pdf"
URLS = [
    pdf_example_engageli
]

conversation_config = {
    "conversation_style": ["engaging", "enthusiastic"],  # Appropriate for academic discourse
    "roles_person1": "main summarizer",  
    "roles_person2": "questioner/clarifier",  
    "dialogue_structure": [
        "Introduction",
        "Main Content Discussion",
        "Closing Remarks and Conclusion"
    ],  # Mimics a structured debate format
    "podcast_name": "The Engagely Podcast",
    "podcast_tagline": "Engagely product overview",
    "creativity": 0.6  
}

audio_file = generate_podcast(urls=URLS, tts_model="geminimulti", longform=True, conversation_config=conversation_config)