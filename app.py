from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

PROJECTS = {
    "thumbnail-maker": {
        "title": "YOUTUBE THUMBNAIL MAKER",
        "label": "AI Agent · LangGraph",
        "year": "2025",
        "tags": ["LangGraph orchestration", "Vision workflow", "Brand-safe output"],
        "summary": "LangGraph-powered agent that turns YouTube scripts into on-brand thumbnail concepts in a few clicks.",
        "description": "The agent generates multiple thumbnail options, scores them with a small eval loop, and then returns the top pick with title, layout notes, and prompt references so designers or other tools can ship assets consistently."
    },
    "shorts-maker": {
        "title": "YOUTUBE SHORT MAKER",
        "label": "AI Agent · Google ADK",
        "year": "2025",
        "tags": ["Clip detection", "Hook generation", "Auto metadata"],
        "summary": "Agent that slices long-form videos into short clips, writes hooks, and prepares upload-ready metadata.",
        "description": "Pipeline parses the transcript, ranks highlight moments, drafts titles and descriptions, and suggests music or sound effects so creators can push Shorts faster with less manual editing."
    },
    "customer-service": {
        "title": "CUSTOMER SERVICE AGENT",
        "label": "AI Agent · LangGraph",
        "year": "2025",
        "tags": ["Intent routing", "RAG", "Safe escalation"],
        "summary": "Tier-1 support agent that understands FAQs, pulls answers from docs, and knows when to hand off to humans.",
        "description": "The graph classifies each message, retrieves the right policy or FAQ content, drafts a response, and escalates tricky cases with a clean summary so human agents can jump in without re-reading the whole thread."
    },
    "finance-agent": {
        "title": "FINANCE SUPPORT AGENT",
        "label": "AI Agent · OpenAI",
        "year": "2025",
        "tags": ["OpenAI SDK", "API integrations", "Stock market"],
        "summary": "Internal agent that triages finance requests, drafts replies, and keeps Notion and Slack in sync.",
        "description": "The flow reads incoming tickets, detects the type of request, fills a brief with key details, and posts updates to Slack and Notion so PMs and stakeholders always see the latest status without asking."
    },
    "workflow-automator": {
        "title": "WORKFLOW AUTOMATOR",
        "label": "Workflow · LangGraph",
        "year": "2025",
        "tags": ["FastAPI backend", "Webhooks", "Event pipeline"],
        "summary": "Backend-first automation hub that runs approvals, data enrichment, and alerts on top of FastAPI.",
        "description": "Webhook events drop into a LangGraph workflow that cleans data, calls external APIs, requests approvals, and ships notifications. Logs and simple metrics help debug runs and keep an eye on failures."
    },
    "job-hunter": {
        "title": "Job-Hunter AGENT",
        "label": "AI Agent · CrewAI",
        "year": "2025",
        "tags": ["Multi-agent flow", "Profile memory", "Job matching"],
        "summary": "Job search copilot that finds roles, tailors resumes, and tracks applications in one place.",
        "description": "Agents work together to read the user’s profile, search job boards, suggest matches, and draft customized resumes and emails. A lightweight memory layer remembers preferences like tech stack, location, and salary range."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project/<project_id>')
def project_detail(project_id):
    project = PROJECTS.get(project_id)
    if not project:
        return redirect(url_for('home'))
    return render_template('project.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        services = request.form.getlist('service')
        consent = request.form.get('consent')

        # Save message to a file
        with open('messages.txt', 'a') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Phone: {phone}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Services: {', '.join(services)}\n")
            f.write(f"Consent: {consent}\n")
            f.write("-" * 20 + "\n")

        return redirect(url_for('success'))
    
    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
