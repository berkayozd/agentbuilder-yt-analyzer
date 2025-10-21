📊 Agent Builder YouTube Content Strategy Analyzer

This project showcases an advanced AI workflow built using OpenAI Agent Builder to automatically analyze the Turkish YouTube Trending list and generate actionable, presentation-ready content strategy reports.

✨ Technical Highlights

This project addresses and successfully overcomes key limitations of developing complex agents on platforms like Agent Builder:

Context Window Mitigation (CRITICAL): The workflow successfully processes a large 100-video JSON dataset, proving that the Agent can bypass the platform's security-enforced context limits by intelligently invoking the File Search Tool on demand.

Full Control Data Flow: Implementation of Set State and Transform nodes ensures clean data (free from API wrappers) is fed to the Large Language Model (LLM).

Structured to Visual Transformation: The final Agent handles a two-stage task: first, analyzing the raw data, and second, converting that complex analysis into a visually appealing, production-ready Markdown Report (no raw JSON output).

🛠️ Project Structure and Setup

The repository is divided into two primary sections: the Python Data Layer and the Agent Builder Documentation.

File/Folder

Purpose

data_collector.py

Python script to fetch the full 100-video trending dataset using the YouTube Data API.

.env

Stores the confidential YOUTUBE_API_KEY (Ignored by Git).

trending_videos_data.json

The collected raw JSON dataset (Uploaded to Agent Builder's Vector Store).

docs/

Stores the source prompts and final report text.

screenshots/

Visual documentation of the workflow, vector store, and final report output.

1. Local Setup

Clone this repository: git clone git@github.com:<YOUR_USERNAME>/agentbuilder-yt-analyzer.git

Install Python dependencies: pip install google-api-python-client requests python-dotenv

Create a .env file and add your YouTube API Key.

Run the data collector to fetch the data: python data_collector.py

2. Agent Builder Workflow Implementation

The workflow is a 5-step linear process designed for data integrity:

Step

Node

CEL/Logic Key

1.

File Search

Retrieves trending_videos_data.json from the Vector Store.

2.

DataCleanup

Uses Transform to isolate the raw JSON string from the File Search metadata.

3.

Set state

Stores the cleaned JSON object into the global variable json_report_object.

4.

Content Strategy Analyst (Agent)

CRITICAL LOGIC: Reads data from state, and if truncated, triggers its internal File Search Tool to retrieve the full 100-video context. Performs analysis and generates the final Markdown report.

5.

End

Outputs the final, professional content strategy report.