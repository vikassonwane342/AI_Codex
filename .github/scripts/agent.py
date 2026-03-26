import os
import re
from openai import OpenAI

# Initialize OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

issue_title = os.environ.get("ISSUE_TITLE", "")
comment = os.environ.get("COMMENT", "")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

# Load project context (optional but powerful)
project = read_file("docs/project.md")
architecture = read_file("docs/architecture.md")
conventions = read_file("docs/conventions.md")
skill = read_file("skills/bug-fixer.md")

# 🔥 Strong prompt (important)
prompt = f"""
You are a senior .NET developer working on a production system.

TASK:
Fix the issue described below.

Issue Title:
{issue_title}

Instruction:
{comment}

Project Context:
{project}

Architecture Rules:
{architecture}

Coding Conventions:
{conventions}

Skill:
{skill}

INSTRUCTIONS:
- Identify root cause
- Fix the bug properly
- Follow clean architecture
- Do NOT break existing code

OUTPUT FORMAT (STRICT):

FILE: path/to/file.cs
CODE:
<full updated code>

Repeat for multiple files if needed.
"""

# Call OpenAI
response = client.responses.create(
    model="gpt-4o-mini",  # you can upgrade to gpt-4o
    input=prompt
)

output = response.output_text

print("===== AI OUTPUT =====")
print(output)

# 🧠 Parse output
matches = re.findall(
    r"FILE:\s*(.*?)\nCODE:\n([\s\S]*?)(?=\nFILE:|$)",
    output
)

# 🛠 Apply changes
for file_path, code in matches:
    file_path = file_path.strip()

    if not file_path:
        continue

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code.strip())

    print(f"✅ Updated: {file_path}")

# 🔥 Ensure PR always triggers
with open("README.md", "a", encoding="utf-8") as f:
    f.write("\nUpdated by AI Agent\n")

print("🚀 DONE")