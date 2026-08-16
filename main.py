import os
import csv
import time
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, ANALYSIS_PROMPT

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from the environment.")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-3.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def process_leads(csv_path: str, output_dir: str):
    print(f"Loading leads from {csv_path}...")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    metrics = {
        "processed": 0,
        "failed": 0,
        "total_time_ms": 0
    }

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            start_time = time.time()
            post_id = row['post_id']
            print(f"Processing lead {post_id} from {row['platform']}...")
            
            prompt = ANALYSIS_PROMPT.format(
                title=row['post_title'],
                content=row['post_content'],
                author=row['author_username'],
                platform=row['platform']
            )
            
            try:
                response = model.generate_content(prompt)
                draft = response.text
                
                # Save the drafted outreach to the output folder
                output_file = os.path.join(output_dir, f"outreach_{post_id}.md")
                with open(output_file, "w", encoding="utf-8") as out_f:
                    out_f.write(f"# Outreach Draft for {row['author_username']} on {row['platform']}\n")
                    out_f.write(f"**Original Post URL:** {row['url']}\n")
                    out_f.write(f"**Original Post Title:** {row['post_title']}\n")
                    out_f.write("---\n\n")
                    out_f.write(draft)
                    
                metrics["processed"] += 1
            except Exception as e:
                print(f"Error processing lead {post_id}: {e}")
                metrics["failed"] += 1
                
            elapsed_ms = (time.time() - start_time) * 1000
            metrics["total_time_ms"] += elapsed_ms
            
            # Rate limiting buffer
            time.sleep(1)

    print("\n=== RUN COMPLETE ===")
    print(f"Successfully processed: {metrics['processed']}")
    print(f"Failed: {metrics['failed']}")
    print(f"Average time per lead: {metrics['total_time_ms'] / max(1, metrics['processed']):.2f} ms")

if __name__ == "__main__":
    process_leads("data/real_pain_leads.csv", "output")
