# Measurement: Pain-First Developer Outbound Engine

## Core Hypothesis
Developers ignore traditional SaaS marketing, but actively seek out tools when they are blocked by a specific technical problem (e.g., PDF pagination, manipulating DOCX structures without losing styling, memory limits of headless browsers). Reaching out *only* when they express these specific pain points, using empathetic and highly technical language, will yield a much higher conversion rate than generic cold outreach.

## The Funnel
1. **Total Scraped Mentions:** Volume of scraped comments matching our keyword groups.
2. **AI-Qualified Leads:** Number of mentions the AI confirms are genuinely trying to solve a programmatic document problem (filtering out false positives).
3. **Drafted Outreaches:** Number of personalized messages successfully generated.
4. **Human Approvals:** Number of messages the human reviewer approves and posts/sends.
5. **Click-Through Rate (CTR):** Clicks on the SuperDocs link in the drafted message.
6. **Signups:** Accounts created from that tracking link.

## Expected Cost & Scaling Limits
- **Execution Time:** ~1.5 - 2 seconds per lead to process the prompt, query Gemini, and generate the response. 
- **Token Usage:** ~300 input tokens, ~150 output tokens per lead.
- **Cost:** At Gemini 1.5 Flash / 3.5 Flash pricing, the API cost is negligible (fractions of a cent per lead).
- **Scale Breaking Point:** At 10x volume (e.g., 500 leads a day), the bottleneck shifts entirely to **Human Review**. A human cannot thoughtfully review 500 highly technical responses a day without fatigue, meaning we would risk sounding like a bot if we automated the final send.

## The Human-in-the-Loop Requirement
The human is strictly required *at the very end of the loop*. The machine finds the lead, categorizes the pain, and writes the message. The human reviewer only needs to read the drafted response and click "Approve/Post." This prevents us from embarrassing ourselves if the AI misunderstands a highly nuanced technical context or recommends a feature SuperDocs does not support.
