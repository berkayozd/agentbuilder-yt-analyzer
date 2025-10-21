📊 Agent Builder YouTube Content Strategy Analyzer

This project showcases an advanced AI workflow built using OpenAI Agent Builder to automatically analyze the Turkish YouTube Trending list and generate actionable, presentation-ready content strategy reports.

✨ Technical Highlights

This project successfully addresses the core challenge of large-scale RAG (Retrieval-Augmented Generation) in Agent Builder by solving the Context Window Truncation issue:

1. Context Window Mitigation (CRITICAL): The final Analyst Agent, upon realizing the input data is incomplete, intelligently triggers its internal File Search Tool to retrieve and process the full 100-video dataset. This showcases self-correction and advanced tool usage logic.

2. Full Control Data Flow: Implementation of Transform and Set State nodes ensures clean, structured data is fed to the Large Language Model (LLM).

3. Visual Output: The final Agent generates a professional, aesthetically pleasing Markdown Report by filtering out platform-enforced file citation icons and raw JSON.


📂 File/Folder

* data_collector.py → Python script to fetch the full 100-video trending dataset using the YouTube Data API.

* example.env → Template for environment variables (copy to .env for use).

* trending_videos_data.json → The collected raw JSON dataset (Uploaded to Agent Builder's Vector Store).

* docs/ → Stores source prompts, final report text, and CEL logic examples.

* screenshots/ → Visual documentation of the entire workflow and final report.

🛠️ Local Setup (Data Collection Layer)

Clone this repository and navigate to the directory.

Install Python dependencies: 
```
pip install google-api-python-client requests python-dotenv
```
Configure API Key: Copy example.env to a new file named .env and paste your YouTube Data API Key.

Generate Data: 
Run the collector script to fetch the data. The output is saved to trending_videos_data.json.
```
python data_collector.py
```

🔁 Agent Builder Workflow Implementation (5 Steps)

The workflow consists of a 5-step linear process designed for data integrity:

1. Start → Define state variables if needed

2. File Search → Initial retrieval of the large JSON file from the Vector Store.

3. DataCleanup → Uses Transform (CEL) to isolate the raw JSON string from metadata.

4. Set state → Stores the cleaned JSON object into the global variable json_report_object.

5. Content Strategy Analyst (Agent) → Performs analysis and generates the final, professional content strategy report.

📝 CRITICAL LOGIC: Reads data from state, and if incomplete, triggers its internal File Search Tool (the fallback mechanism) to read the full 100-video context. 

📸 Visual Documentation

Check the /screenshots folder for a step-by-step visual guide:

